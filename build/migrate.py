#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
migrate.py — Migrazione assistita dei file «Scartafacci» dal vecchio impianto
Versioning Machine al nuovo modello (edizione critico-genetica, apparato senza <lem>).

NON è un convertitore «magico»: la mappatura delle fasi e la rimodellazione
dell'apparato richiedono giudizio filologico. Questo script fa due cose:

  1. CORREZIONI AUTOMATICHE (deterministiche e sicure) — vedi `fix_*`;
  2. SEGNALAZIONI (`flag`) — tutto ciò che va rivisto a mano, con il motivo.

Per ogni file produce una bozza ripulita in OUTDIR e una riga nel report Markdown.
La bozza NON è ancora valida: è il punto di partenza della revisione a lotti.

Uso:
    python3 build/migrate.py <file-o-cartella> [--out bozze/] [--report report-migrazione.md]

Dipendenze: lxml.
"""
import argparse, re, sys, datetime
from pathlib import Path
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"
XML = "http://www.w3.org/XML/1998/namespace"
def q(tag): return f"{{{TEI}}}{tag}"            # nome qualificato TEI
def ln(el): return etree.QName(el).localname     # local-name

# Vocabolari controllati del progetto
MEDIUM_VALIDI = {"inchiostro-nero", "inchiostro-blu", "matita-grigia", "dattiloscritto"}
MEDIUM_MAP = {
    "black_ink_1": "inchiostro-nero", "black_ink": "inchiostro-nero",
    "inchiostro_nero": "inchiostro-nero", "nero": "inchiostro-nero",
    "grey_pencil_1": "matita-grigia", "grey_pencil": "matita-grigia",
    "pencil": "matita-grigia", "matita": "matita-grigia",
    "blue_ink": "inchiostro-blu", "typescript": "dattiloscritto",
}
LANG_MAP = {"italiano": "it", "ita": "it", "italian": "it", "it-it": "it"}
REND_VALIDI = {"overstrike", "overstrike-wavy", "underline", "strikethrough"}
SIGLA_RE = re.compile(r"\b(Tc|Tb\d+|T\d+)\b")


def migra(path: Path):
    """Elabora un file; ritorna (xml_output:str|None, fixes:list, flags:list)."""
    fixes, flags = [], []
    try:
        tree = etree.parse(str(path))
    except etree.XMLSyntaxError as e:
        return None, [], [f"XML non ben formato: {e}"]
    root = tree.getroot()

    # — F1. PI <?xml-stylesheet?> (verrà esclusa serializzando dal root) ----------
    if root.getprevious() is not None or tree.xpath('//processing-instruction("xml-stylesheet")'):
        fixes.append("Rimossa la PI <?xml-stylesheet?> (Versioning Machine).")

    # — F2. <facsimile> e rimandi a immagini ------------------------------------
    for fac in root.findall(q("facsimile")):
        fac.getparent().remove(fac)
        fixes.append("Rimosso <facsimile> (immagini dei manoscritti: non si pubblicano).")
    npb = 0
    for pb in list(root.iter(q("pb"))):
        if pb.get("ed") or pb.get("facs"):
            pb.getparent().remove(pb); npb += 1
    if npb:
        fixes.append(f"Rimossi {npb} <pb> con @ed/@facs (segnapagina per-testimone della VM).")
    nfacs = 0
    for el in root.iter():
        if el.get("facs"):
            del el.attrib["facs"]; nfacs += 1
    if nfacs:
        fixes.append(f"Rimosso @facs pendente da {nfacs} elementi.")

    # — F3. @wit: ogni sigla deve iniziare con un solo '#' ----------------------
    nwit = 0
    for el in root.xpath("//*[@wit]"):
        toks = el.get("wit").split()
        new = ["#" + t.lstrip("#") for t in toks]
        if new != toks:
            el.set("wit", " ".join(new)); nwit += 1
    if nwit:
        fixes.append(f"Normalizzato @wit (aggiunto '#') su {nwit} letture.")

    # — F4. lingua: @ident, @xml:lang, @mainLang → 'it' -------------------------
    for lang in root.iter(q("language")):
        v = lang.get("ident")
        if v and v != "it":
            if v.lower() in LANG_MAP:
                lang.set("ident", "it"); fixes.append(f'language/@ident="{v}" → "it".')
            else:
                flags.append(f'language/@ident="{v}" non riconosciuto: verificare il codice lingua.')
    nlang = 0
    for el in root.iter():
        for att in (f"{{{XML}}}lang", "mainLang", "otherLangs"):
            v = el.get(att)
            if v and v.lower() in LANG_MAP and v != "it":
                el.set(att, "it"); nlang += 1
    if nlang:
        fixes.append(f"Normalizzato il codice lingua 'ita/italiano' → 'it' su {nlang} attributi.")

    # — F5. handNote/@medium: vocabolario controllato ---------------------------
    for hn in root.iter(q("handNote")):
        m = hn.get("medium")
        if not m:
            continue
        if "+" in m or ("ink" in m.lower() and "pencil" in m.lower()):
            flags.append(f'handNote/@medium="{m}" composito: nel nuovo modello le mani sono '
                         f'due (#pen1 inchiostro-nero, #pen2 matita-grigia) nell\'header di corpus.')
        elif m in MEDIUM_MAP:
            hn.set("medium", MEDIUM_MAP[m]); fixes.append(f'@medium "{m}" → "{MEDIUM_MAP[m]}".')
        elif m not in MEDIUM_VALIDI:
            flags.append(f'handNote/@medium="{m}" fuori vocabolario: mappare su {sorted(MEDIUM_VALIDI)}.')

    # — F6. <del type="rend"> → <del rend="…"> ----------------------------------
    nrend = 0
    for d in root.iter(q("del")):
        t = d.get("type")
        if t and not d.get("rend"):
            if t in REND_VALIDI:
                d.set("rend", t); del d.attrib["type"]; nrend += 1
            else:
                flags.append(f'<del type="{t}">: valore non di resa, verificare (atteso @rend).')
    if nrend:
        fixes.append(f"Convertito <del type> → <del rend> su {nrend} cancellature.")

    # — F7. <supplied>: responsabilità al curatore, via @source non standard ----
    for s in root.iter(q("supplied")):
        r = s.get("resp")
        if not r:
            s.set("resp", "#LL"); fixes.append('<supplied>: aggiunto @resp="#LL".')
        elif not r.startswith("#") or "txt" in r:
            flags.append(f'<supplied resp="{r}">: la responsabilità dell\'integrazione va a #LL.')
        if s.get("source"):
            flags.append(f'<supplied source="{s.get("source")}">: attributo non standard, rimuovere o motivare.')

    # ====================  SEGNALAZIONI (giudizio filologico)  ==================

    # G1. <msDesc> commentato → riattivare
    for c in root.xpath("//comment()"):
        if "msDesc" in (c.text or ""):
            flags.append("<msDesc> commentato: riattivare e ripulire a mano (incipit, dimensioni, mani).")
            break

    # G2. @change che punta a un testimone (uso errato: @change = elemento <change>)
    for el in root.xpath("//*[@change]"):
        v = el.get("change")
        if "txt" in v:
            flags.append(f'<{ln(el)} @change="{v}">: @change punta a un testimone (errato). '
                         f'Sostituire con @hand (lo strumento della fase va verificato sull\'autografo).')

    # G3. apparato di sola rivergatura (retrace senza del/add) → fuori apparato
    for app in root.iter(q("app")):
        if app.findall(f".//{q('retrace')}") and not app.findall(f".//{q('del')}") \
           and not app.findall(f".//{q('add')}"):
            flags.append("Apparato con sola rivergatura (<retrace>, lezione invariata): "
                         "spostare il <retrace> in linea nel verso, fuori da <app> (dec. 2).")

    # G4. attribuzione: solo il curatore (dec. 5)
    extra = sorted({(n.text or "").strip() for n in root.findall(f".//{q('respStmt')}//{q('name')}")
                    if (n.text or "").strip() and "Longo" not in n.text})
    if extra:
        flags.append(f"respStmt con nomi oltre Longo {extra}: rimuovere i supervisori (dec. 5).")
    if root.findall(f".//{q('sponsor')}") or root.findall(f".//{q('distributor')}"):
        flags.append("Presenti <sponsor>/<distributor> (Università di Palermo): rimuovere (dec. 5).")

    # G5. sigle usate nelle note ma non dichiarate in <listWit>
    dichiarate = set()
    for w in root.iter(q("witness")):
        dichiarate |= set(SIGLA_RE.findall("".join(w.itertext())))
    usate = set()
    for note in root.iter(q("note")):
        usate |= set(SIGLA_RE.findall("".join(note.itertext())))
    fantasma = usate - dichiarate
    if fantasma:
        flags.append(f"Sigle usate nelle note ma non in <listWit>: {sorted(fantasma)} — riallineare.")

    # G6. statuto: nessun <lem>
    if root.findall(f".//{q('lem')}"):
        flags.append('Presente <lem>: lo statuto lo vieta → convertire in <rdg wit="#txt-c">.')

    # G7. header per-file ridondante (ora nell'header di corpus)
    if root.findall(f".//{q('variantEncoding')}") or root.findall(f".//{q('projectDesc')}"):
        flags.append("encodingDesc per-file presente: i criteri comuni stanno in header/corpus-header.xml; "
                     "sfoltire il teiHeader del singolo file.")

    # Serializzazione dal root: esclude la PI <?xml-stylesheet?> e la DTD esterna
    out = '<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tostring(root, encoding="unicode")
    return out, fixes, flags


def main():
    ap = argparse.ArgumentParser(description="Migrazione primo passaggio dei file TEI «Scartafacci».")
    ap.add_argument("input", help="file .xml o cartella da migrare")
    ap.add_argument("--out", default="bozze", help="cartella di output (default: bozze/)")
    ap.add_argument("--report", default="report-migrazione.md", help="file di report Markdown")
    args = ap.parse_args()

    src = Path(args.input)
    files = sorted(src.glob("*.xml")) if src.is_dir() else [src]
    if not files:
        sys.exit("Nessun file .xml trovato.")
    outdir = Path(args.out); outdir.mkdir(parents=True, exist_ok=True)

    righe = [f"# Report di migrazione — primo passaggio\n",
             f"*Generato: {datetime.date.today().isoformat()} · file: {len(files)}*\n"]
    tot_fix = tot_flag = 0
    for f in files:
        xml, fixes, flags = migra(f)
        tot_fix += len(fixes); tot_flag += len(flags)
        if xml is not None:
            (outdir / f.name).write_text(xml, encoding="utf-8")
        righe.append(f"\n## {f.name}\n")
        righe.append(f"**Correzioni automatiche ({len(fixes)}):**" if fixes else "**Correzioni automatiche:** nessuna.")
        righe += [f"- {x}" for x in fixes]
        righe.append(f"\n**Da rivedere a mano ({len(flags)}):**" if flags else "\n**Da rivedere a mano:** nulla di segnalato.")
        righe += [f"- ⚠ {x}" for x in flags]

    righe.insert(2, f"\n**Sintesi:** {tot_fix} correzioni automatiche · {tot_flag} segnalazioni "
                    f"su {len(files)} file. Le bozze in `{outdir}/` **non sono ancora valide**: "
                    f"sono il punto di partenza della revisione a lotti.\n")
    Path(args.report).write_text("\n".join(righe), encoding="utf-8")
    print(f"Elaborati {len(files)} file → {outdir}/")
    print(f"Correzioni automatiche: {tot_fix} · Segnalazioni: {tot_flag}")
    print(f"Report: {args.report}")


if __name__ == "__main__":
    main()

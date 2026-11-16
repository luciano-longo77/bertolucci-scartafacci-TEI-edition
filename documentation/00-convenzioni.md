# 0. Convenzioni — quadro normativo

## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Pagina di riferimento rapido: le regole **vincolanti**, cioè ciò che lo schema di progetto
(`schema/bertolucci.rng` + `schema/bertolucci.isosch.sch`) verifica su ogni file. Per la trattazione
distesa si rimanda alle schede indicate. Gli esempi sono schematici.*

---

## Quando un file è conforme

Un file è «a norma» quando passa **entrambi** i controlli. Procedura in
[`schema/README.md`](../schema/README.md) — **validare contro `bertolucci.rng`, non contro il TEI
standard** (`tei_all.rng`).

| Livello | File | Verifica |
|---|---|---|
| Grammatica | `schema/bertolucci.rng` | elementi/attributi ammessi, struttura, **niente `<lem>`**, `@medium` da vocabolario chiuso |
| Integrità | `schema/bertolucci.isosch.sch` | `@wit` con `#` che risolve a un `<witness>`; puntatori di mano/responsabilità risolti; `<subst>` con `del`+`add`; lingua `it`; `variantEncoding/@method = parallel-segmentation` |

---

## 1. Apparato senza `<lem>` · sigle dei testimoni

Apparato in *parallel-segmentation*: le fasi coesistono come più `<rdg>`, **nessun `<lem>`**; la lezione
critica è `<rdg wit="#txt-c">`; la cronologia è in `@varSeq`. → scheda
[`04-apparato-genetico.md`](04-apparato-genetico.md).

Sigle **normative** (ogni file le dichiara in `<front><listWit>`; il numero di fasi varia per componimento):

| `xml:id` | Sigla | Significato |
|---|---|---|
| `txt-c` | **Tc** | testo criticamente ricostruito |
| `txt-1` | **Tb0** | prima stesura (*base*) |
| `txt-2` | **Tb1** | correzione successiva nella **stessa campagna** (stesso strumento) |
| `txt-3` | **T1** | intervento di una campagna **distinta** e più tarda (es. matita) |

**`xml:id` e sigla sono indipendenti.** L'`xml:id` è **posizionale** (`txt-c`, poi `txt-1`, `txt-2`… in
ordine di comparsa, senza salti); la **sigla** nel `<witness>` esprime il **senso genetico** e non è legata
al numero. Un componimento con sole due fasi avrà `txt-1`=Tb0 e `txt-2`=**T1** (senza Tb1): **non** dare per
scontato che `txt-2`≡Tb1.

**Come crescono le sigle.** `Tb0, Tb1, Tb2…` = interventi successivi con lo **stesso strumento** della base
(campagna a inchiostro); `T1, T2…` = campagne **distinte** e più tarde (es. la matita); `Tc` = testo critico.

**Quando una correzione apre una fase.** Solo se **cambia la lezione** (cassature, aggiunte, sostituzioni
sostanziali). Una correzione istantanea *a penna currente* che non altera il testo resta dentro la sua
fase: una fase nuova deve avere un contenuto testuale reale, non un micro-fenomeno materiale.

Regola tecnica: `@varSeq` interi crescenti; `#txt-c` di norma senza `@varSeq`; lezioni identiche accorpate
(`wit="#txt-c #txt-1"`).

---

## 2. Identificatori (`xml:id`) e puntatori

- `xml:id` unico nel file; ogni riferimento con `#` (`#txt-1`, `#pen1`, `#LL`).
- File `xml:id="AuInN"`; descrizione ms. `xml:id="ms-AuInN"`; testimoni `txt-c`/`txt-1`…
- Mani (`#pen1`, `#pen2`) e responsabilità (`#LL`): dichiarate nell'header di corpus, richiamate con `#`.

---

## 3. Mani e mezzi scrittori (vocabolario chiuso)

`handNote/@medium` è a vocabolario **chiuso** (imposto dallo schema). → scheda
[`03-mani-e-medium.md`](03-mani-e-medium.md).

| `@medium` ammessi | Mani standard (uso *tipico*) |
|---|---|
| `inchiostro-nero`, `inchiostro-blu`, `matita-grigia`, `dattiloscritto` | `#pen1` = `inchiostro-nero` (fasi a inchiostro) · `#pen2` = `matita-grigia` (interventi a matita) |

**Una mano, un mezzo.** Ogni `<handNote>` dichiara **un solo** `@medium`. Se in un autografo convivono più
strumenti (inchiostro + matita), si dichiarano **più mani** (`#pen1`, `#pen2`), **mai** un `@medium`
composito (es. `black_ink+pencil`). L'associazione mano→fase (`#pen1`→inchiostro, `#pen2`→matita) è
*tipica*, non una legge: conta lo strumento osservato sull'autografo.

> Aggiungere un mezzo = **due** modifiche coordinate: `valList` nell'ODD **e** `$medium-ammessi` nello
> Schematron.

---

## 4. Interventi d'autore e fenomeni materiali

Modulo `transcr`, sempre con `@hand`. → scheda [`05-fenomeni-materiali.md`](05-fenomeni-materiali.md).

`<del>` · `<add>` · `<subst>` (**almeno un `del` e un `add`**) · `<retrace>` · `<gap>` ·
`<supplied resp="#LL">` · `<space>`. Gli interventi che **cambiano la lezione** stanno **dentro** i `<rdg>`
delle fasi in cui avvengono.

**Rivergature e fenomeni materiali che non cambiano la lezione.** Un ripasso di lettera (`<retrace>`) che
non altera il testo **non è una variante** e **non va in apparato**: si marca **in linea** nel verso, con
una `<note type="physical">`. Niente `<app>` con `<rdg>` identici solo per ospitare un ripasso.

```xml
<l n="11">Oh com<retrace rend="overwritten" hand="#pen1">e</retrace> è stata tua stagione breve
   <note type="physical">La -e- è rivergata con lo stesso inchiostro del resto del ms.</note></l>
```

> Nota tecnica: su `<retrace>` usare `@hand` (chi), non `@change` — `@change` punta a un elemento
> `<change>`, non a un testimone.

---

## 5. Note, lingua, struttura

- **`<note>`/@type** raccomandati: `critical`, `physical`, `biographical`, `metrical`, `context`
  (assenza ammessa).
- **Lingua**: `xml:lang="it"` sul `<TEI>`; `<language ident="it">` (codice `it`, non «italiano»).
- **Struttura**: `<body>` › `<div type="poem">` › `<lg>` › `<l n="…">`; titolo in `<head>`, colophon in
  `<ab type="colophon">`. → scheda [`06-struttura-del-testo.md`](06-struttura-del-testo.md).
- Grafia conservativa (maiuscole e interpunzione dell'autografo). Encoding UTF-8.

---

## Dove trovo cosa

| Tema | Scheda |
|---|---|
| Impianto e scelte editoriali | [`01-modello-editoriale.md`](01-modello-editoriale.md) |
| Intestazione e metadati | [`02-teiHeader.md`](02-teiHeader.md) |
| Mani e mezzi | [`03-mani-e-medium.md`](03-mani-e-medium.md) |
| Apparato genetico | [`04-apparato-genetico.md`](04-apparato-genetico.md) |
| Fenomeni materiali | [`05-fenomeni-materiali.md`](05-fenomeni-materiali.md) |
| Struttura del testo | [`06-struttura-del-testo.md`](06-struttura-del-testo.md) |
| Diritti e facsimili | [`07-diritti-e-facsimili.md`](07-diritti-e-facsimili.md) |
| Schema e validazione | [`../schema/README.md`](../schema/README.md) |

---

*Ultimo aggiornamento: 2026-11-16. Ogni modifica alle regole vincolanti va riportata insieme nell'ODD,
nello Schematron e in questa pagina.*

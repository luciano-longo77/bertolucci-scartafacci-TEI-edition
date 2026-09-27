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
| `txt-2` | **Tb1** | interventi della stessa campagna |
| `txt-3` | **T1** | intervento successivo, campagna distinta |

Regola: `xml:id` sequenziali senza salti (`txt-c`, `txt-1`, `txt-2`…); `@varSeq` interi crescenti;
`#txt-c` di norma senza `@varSeq`; lezioni identiche accorpate (`wit="#txt-c #txt-1"`).

---

## 2. Identificatori (`xml:id`) e puntatori

- `xml:id` unico nel file; ogni riferimento con `#` (`#txt-1`, `#pen1`, `#LL`).
- File `xml:id="AuInN"`; descrizione ms. `xml:id="ms-AuInN"`; testimoni `txt-c`/`txt-1`…
- Mani (`#pen1`, `#pen2`) e responsabilità (`#LL`): dichiarate nell'header di corpus, richiamate con `#`.

---

## 3. Mani e mezzi scrittori (vocabolario chiuso)

`handNote/@medium` è a vocabolario **chiuso** (imposto dallo schema). → scheda
[`03-mani-e-medium.md`](03-mani-e-medium.md).

| `@medium` ammessi | Mani standard |
|---|---|
| `inchiostro-nero`, `inchiostro-blu`, `matita-grigia`, `dattiloscritto` | `#pen1` = `inchiostro-nero` (Tb0/Tb1) · `#pen2` = `matita-grigia` (T1) |

> Aggiungere un mezzo = **due** modifiche coordinate: `valList` nell'ODD **e** `$medium-ammessi` nello
> Schematron.

---

## 4. Interventi d'autore e fenomeni materiali

Modulo `transcr`, sempre con `@hand`. → scheda [`05-fenomeni-materiali.md`](05-fenomeni-materiali.md).

`<del>` · `<add>` · `<subst>` (**almeno un `del` e un `add`**) · `<retrace>` · `<gap>` ·
`<supplied resp="#LL">` · `<space>`. Gli interventi stanno **dentro** i `<rdg>` delle fasi in cui avvengono.

---

## 5. Note, lingua, struttura

- **`<note>`/@type** raccomandati: `critical`, `physical`, `biographical` (assenza ammessa).
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

*Ultimo aggiornamento: 2026-09-27. Ogni modifica alle regole vincolanti va riportata insieme nell'ODD,
nello Schematron e in questa pagina.*

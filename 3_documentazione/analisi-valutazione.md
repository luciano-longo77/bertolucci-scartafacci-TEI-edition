# Analisi e valutazione filologico-tecnica dell'edizione

**Oggetto:** edizione digitale TEI degli *Scartafacci* di Attilio Bertolucci
(60 file XML in `1_xml/`).
**Tipo di intervento:** valutazione del modello di codifica, della conformità
TEI P5 e dell'integrità interna dell'apparato. Non è una revisione del testo
critico né della trascrizione, che presuppongono il collazionamento sugli
originali.
**Metodo:** controllo di buona formazione (`xmllint`), controlli filologici
automatici su tutto il corpus (`3_documentazione/valida_corpus.py`,
`lxml`), ispezione mirata dei casi anomali. La validazione contro
`tei_all.rng` **non** è stata eseguita (schema non disponibile in ambiente):
le non-conformità di schema indicate sotto sono da confermare in oXygen.

---

## 1. Quadro generale

Il corpus raccoglie autografi inediti di Bertolucci (1930-1940 e anteriori),
codificati come edizione di **filologia d'autore** a testimone unico
stratificato: per ciascun testo si distinguono le fasi elaborative (Tb0, Tb1,
T1, T3…) e un testo critico (Tc). Il modello dichiarato nel `teiHeader` è
`parallel-segmentation` interna, secondo la prassi di *Versioning Machine*, con
`<app>` che contengono più `<rdg>` **senza `<lem>`** (scelta esplicita e
coerente con il README).

- 60 file, **tutti ben formati** (nessun errore di parsing).
- Namespace TEI corretto in tutti i file.
- `<variantEncoding method="parallel-segmentation">` dichiarato ovunque.
- 315 `<app>` complessivi; **315 senza `<lem>`** (100%): coerente col modello.

La scelta di fondo — rappresentare le fasi come *versioni* parallele e affidare
al testimone `txt-c` (Tc) la funzione di testo di riferimento — è legittima e
ben adatta a un avant-texte a testimone unico. Il giudizio che segue riguarda
la **realizzazione** di questo modello, non il modello in sé.

---

## 2. Criticità gravi (compromettono l'edizione)

### 2.1 La descrizione dei manoscritti non esiste nel markup attivo
Il README indica fra i contenuti «descrizione dei manoscritti: `msDesc`,
`physDesc`, `handNotes`». In realtà **`<msDesc>` è racchiuso in un commento XML
in tutti e 60 i file**: l'interrogazione XPath trova 0 `msDesc` attivi su 60.
Tutta la descrizione materiale (supporto, dimensioni, mani, storia, *locus*,
*incipit/explicit*) è quindi presente solo come testo commentato e **non fa
parte del documento TEI**. È lo scarto più rilevante fra ciò che l'edizione
dichiara e ciò che effettivamente codifica. Le informazioni descrittive
sopravvivono in forma discorsiva dentro `<sourceDesc><p>` e nelle `<note>`, ma
non sono interrogabili come dati strutturati.

**Azione:** decommentare e riattivare i blocchi `<msDesc>`, oppure — se la scelta
è consapevole — rimuovere la promessa dal README ed esplicitare che la
descrizione è solo discorsiva.

### 2.2 Apparati con sigle di testimone non dichiarate
In più file i `@wit` puntano a testimoni **mai dichiarati** nel `<listWit>` del
file stesso, rendendo l'apparato irrisolvibile:

- **`AuIn24.xml`** — `<listWit>` dichiara solo `txt22-c/1/2/3`, ma il corpo usa
  `#txt24-*` e `#txt23-*` (collazione a tre testi) mai dichiarati.
- **`AuIn7.xml`** — accanto ai validi `#txt-c #txt-1` compaiono `#a7-txt-c` e
  `#a7-txt-1`, non dichiarati.
- **`AuIn44.xml`** — usato `#txt4-1` (refuso per `#txt44-1`); inoltre
  `hand="black_ink_1"` punta al *medium* invece che all'`xml:id` `pen1`.

Sono 9 riferimenti-testimone pendenti in totale: in un'edizione di varianti la
sigla non risolta equivale a una lezione senza testimone.

### 2.3 `<retrace>` non è un elemento TEI P5
`<retrace>` è usato **27 volte in 14 file** (AuIn1, AuIn4, AuIn7, AuIn9_2,
AuIn14, AuIn17, AuIn18_1, AuIn21_1, AuIn44…). Non esiste nel vocabolario TEI:
il file **non validerà** contro `tei_all` e la dichiarazione di conformità del
`teiHeader` risulta, allo stato, non veritiera. Il fenomeno (tratto ripassato)
va reso con gli strumenti TEI: `<hi rend="retraced">…</hi>` o
`<add>`/`<restore>` con nota, dichiarando la convenzione in `<editorialDecl>`.

### 2.4 `<div1>`/`<div2>` mescolati a `<div>` in `AuIn5.xml`
`AuIn5.xml` usa i `div` numerati (`<div1>`, `<div2>`) insieme al `<div>` non
numerato. I due modelli sono mutuamente esclusivi in TEI: la compresenza è
errore di schema.

---

## 3. Criticità di conformità e coerenza (diffuse ma sistematiche)

### 3.1 `@wit` senza `#` — puntatori spezzati (48 occorrenze)
Molti `@wit`/`@lem` scrivono la sigla senza cancelletto (`wit="txt-2"` invece di
`wit="#txt-2"`), talora **nello stesso file** in cui altrove il `#` è presente
(p. es. `AuIn1.xml`, `AuIn2.xml`, `AuIn12.xml`). `@wit` è di tipo
`data.pointer`: senza `#` non è un puntatore risolvibile. Va normalizzato in
tutto il corpus.

### 3.2 Puntatori `@resp`/`@hand` pendenti
- `AuIn13_1.xml` — `@resp="#berty"` (9 occorrenze) verso un `xml:id` mai
  dichiarato: i `respStmt` del header hanno `<name>` senza `xml:id`.
- `AuIn44.xml` — `hand="black_ink_1"` (vedi 2.2).

### 3.3 `@ident="italiano"` non standard (60/60 file)
`<language ident="italiano">` usa un'etichetta non conforme a BCP 47: il valore
atteso è `it` (o `ita`). Correzione meccanica su tutto il corpus.

### 3.4 Doppio schema di sigle nel corpus
Convivono uno schema **globale** (`txt-c`, `txt-1`, `txt-2`… in 51 file) e uno
**per-file** (`txt24-c`, `txt43-1`, `a7-txt-1`… in 9 file). La convivenza non è
un problema finché ogni file è autoconsistente e trattato singolarmente da
Versioning Machine; lo diventa proprio nei file misti del §2.2, dove i due
schemi si sovrappongono e generano i riferimenti pendenti. Va scelta e
documentata una convenzione unica.

---

## 4. Osservazioni metodologiche

Non sono errori, ma scelte che conviene rendere esplicite perché incidono sul
valore scientifico dell'edizione.

- **Nessun `<subst>` nel corpus** (0 occorrenze), a fronte di 193 `<del>` e 156
  `<add>`. Dentro i singoli `<rdg>` le cassature e le aggiunte restano dunque
  *sciolte*: si perde il legame «X sostituisce Y» che `<subst>` codifica. Nel
  modello a parallel-segmentation, dove ogni `<rdg>` è già lo stato di una fase,
  la perdita è attenuata; resta però il caso, frequente nella filologia
  d'autore, della sostituzione *interna* a una singola fase, che qui non è
  rappresentabile.
- **`@varSeq` mai usato** (0 file) e **`<listChange>`/`@change` mai usati** (0
  file). L'ordine cronologico delle varianti — che *è* il contenuto di
  un'edizione d'autore — è affidato interamente alla descrizione testuale delle
  sigle in `<listWit>` («prima stesura», «seconda stesura»…) e alle `<note>`.
  Funziona per la lettura umana, ma non è machine-actionable: non è possibile
  estrarre automaticamente il testo a una data altezza redazionale. Se
  l'obiettivo resta la sola visualizzazione parallela in VM, la scelta è
  sostenibile; se si vuole vera critica genetica computabile, andrebbero
  introdotti `@varSeq` e/o `listChange` in `<creation>`.
- **Testimoni dichiarati e mai usati** (14 casi, p. es. `AuIn32_1`, `AuIn45`,
  `PreSirio_5`): file a redazione unica dove `txt-c`/`txt-1` sono dichiarati ma
  non essendoci varianti nessun `<app>` li richiama. Innocuo, ma il `<listWit>`
  in questi casi è boilerplate.

---

## 5. Punti di forza

- Buona formazione integrale e namespace corretto: base solida.
- Modello editoriale unico e dichiarato (`variantEncoding`, `<editorialDecl>`,
  `<listWit>` con descrizione delle fasi): l'impianto è coerente e leggibile.
- Ricchezza dell'annotazione critica, biografica e contestuale nelle `<note>`,
  con distinzione tipizzata (`@type="critical|physical|biographical|metrical"`).
- Trattamento onesto delle lacune materiali: `<gap reason="punched">`,
  `<supplied>`, `<space>` usati per non inventare lezioni (17 `supplied`, 18
  `gap`, 8 `unclear`), in linea con la buona prassi ecdotica.
- Uso corretto di `<app>` senza `<lem>` come modello dichiarato, non come
  dimenticanza.

---

## 6. Raccomandazioni in ordine di priorità

1. **Riattivare o rimuovere `msDesc`** (§2.1): decidere se la descrizione
   materiale è parte dell'edizione. È la scelta con più impatto.
2. **Sanare i riferimenti pendenti** `@wit`/`@resp`/`@hand` (§2.2, §3.2):
   allineare `AuIn24`, `AuIn7`, `AuIn44`, `AuIn13_1` fra `listWit`/header e
   corpo. Sono errori che invalidano l'apparato dei file coinvolti.
3. **Sostituire `<retrace>`** con marcatura TEI valida e ricontrollare
   `AuIn5` (`div1`/`div2`) (§2.3-2.4): condizione per poter davvero dichiarare
   la conformità.
4. **Normalizzare `@wit` con `#`** e **`@ident="it"`** su tutto il corpus
   (§3.1, §3.3): correzioni meccaniche, verificabili con lo script allegato.
5. **Documentare la convenzione delle sigle** e, se si vuole critica genetica
   computabile, **introdurre `@varSeq`/`listChange`** (§3.4, §4).
6. **Eseguire la validazione RelaxNG** contro `tei_all.rng` in oXygen prima di
   ogni rilascio.

---

## 7. Giudizio complessivo

L'edizione poggia su un impianto metodologico chiaro e appropriato
all'oggetto (avant-texte a testimone unico, fasi parallele à la Versioning
Machine) ed è ricca sul piano dell'annotazione critica. È però **allo stato non
conforme** allo standard che dichiara di seguire — per l'uso di `<retrace>`, per
i `div` numerati misti e per i puntatori spezzati — e presenta **due lacune di
sostanza**: la descrizione materiale dei manoscritti disattivata nel markup e
alcuni apparati con sigle non risolvibili. Nessuna di queste criticità mette in
discussione il lavoro filologico sottostante; tutte sono sanabili con
interventi mirati e in buona parte meccanizzabili. Sanati i punti del §2 e del
§3, l'edizione raggiunge un livello pienamente pubblicabile.

---

*Controlli riproducibili con `python3 3_documentazione/valida_corpus.py` dalla
radice del repository (richiede `lxml`).*

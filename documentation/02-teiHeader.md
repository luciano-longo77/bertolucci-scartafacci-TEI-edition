# 2. Il teiHeader
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

Il `<teiHeader>` è il «frontespizio elettronico»: raccoglie i metadati e le
dichiarazioni editoriali. I **metadati comuni** a tutto il corpus (responsabilità,
criteri editoriali, mani/`medium`, lingua) sono dichiarati **una sola volta**
nell'**header di corpus** (`teiCorpus`, file `header/corpus-header.xml`); il
singolo componimento porta nel proprio `<teiHeader>` solo ciò che **varia**:
titolo, `notesStmt`, `msDesc`.

## 2.1 `<fileDesc>` — fonte e responsabilità

Contiene `titleStmt` (titolo + responsabilità del curatore), `publicationStmt`
(rimando all'header di corpus; master non distribuito), `notesStmt` (note
critiche, biografiche, di contesto) e `sourceDesc` con il `<msDesc>`.

```xml
<titleStmt>
  <title>I. Un triste canto, un dolce e triste canto</title>
  <respStmt><resp>edizione</resp><name ref="#LL">Luciano Longo</name></respStmt>
</titleStmt>
```

> La responsabilità è del solo curatore (`#LL`): i crediti di supervisione del
> vecchio progetto dottorale non figurano nel master dell'edizione.

## 2.2 Metodo e criteri — nell'header di corpus

Metodo d'apparato e criteri editoriali sono dichiarati nell'`<encodingDesc>`
dell'**header di corpus**, non nel singolo file:

```xml
<encodingDesc>
  <variantEncoding method="parallel-segmentation" location="internal"/>
  <editorialDecl>
    <normalization><p>Si conservano maiuscola d'inizio verso e interpunzione.</p></normalization>
  </editorialDecl>
</encodingDesc>
```

## 2.3 `<profileDesc>` — mani e lingua (header di corpus)

Ospita la dichiarazione delle mani/mezzi scrittori (`<handNotes>`, vedi
[03 – Mani e mezzi scrittori](03-mani-e-medium.md)) e la lingua (`<langUsage>`).
Il codice lingua è **`it`** (BCP 47), non `italiano`; lo Schematron lo verifica.

```xml
<langUsage>
  <language ident="it">Italiano</language>
</langUsage>
```

## 2.4 `<revisionDesc>` — storia del *file*

Registra le modifiche al **file XML** (chi, quando, cosa). Da non confondere con
le **fasi del testo**: queste sono i `<witness>` dichiarati in `<front><listWit>`
e ordinati da `@varSeq` (vedi [01 §1.2](01-modello-editoriale.md)). Sono due piani
diversi — il file non usa `<listChange>`/`@change` per le fasi.

## 2.5 `<msDesc>` — descrizione del manoscritto

La descrizione materiale del testimone (identificazione, contenuto, supporto,
dimensioni, mani, storia, *locus*, *incipit/explicit*) è **opera descrittiva del
curatore** e fa parte del documento TEI (non di un testo discorsivo a parte).

```xml
<sourceDesc>
  <msDesc xml:id="ms-AuIn1">
    <msIdentifier><settlement>Parma</settlement>
      <institution>Archivio di Stato</institution>
      <repository>Archivio della Letteratura – Archivio Bertolucci</repository>
      <idno>Busta II, fascicolo 4, 1</idno></msIdentifier>
    <!-- msContents, physDesc, history, additional/surrogates -->
  </msDesc>
</sourceDesc>
```

> L'esistenza delle riproduzioni fotografiche e la loro sede si documentano, in
> forma descrittiva, in `<additional><surrogates>` (vedi
> [07 – Diritti e facsimili](07-diritti-e-facsimili.md)); le immagini non sono
> distribuite.

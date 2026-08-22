# 2. Il teiHeader

Il `<teiHeader>` è il «frontespizio elettronico»: raccoglie i metadati del file e
le dichiarazioni editoriali. Si articola in `fileDesc`, `encodingDesc`,
`profileDesc`, `revisionDesc`.

## 2.1 `<fileDesc>` — fonte e responsabilità

Contiene `titleStmt` (titolo, autore, responsabilità), `publicationStmt`
(editore, sede, data, `availability@status`), `notesStmt` (note critiche,
biografiche, di contesto, con `@type` e `@anchored`) e `sourceDesc` (descrizione
del testimone).

```xml
<titleStmt>
  <title>I. Un triste canto, un dolce e triste canto</title>
  <respStmt><resp>Trascrizione, codifica ed edizione critica</resp>
            <name>Luciano Longo</name></respStmt>
</titleStmt>
```

## 2.2 `<encodingDesc>` — metodo e criteri

Dichiara il metodo di apparato e i criteri editoriali:

```xml
<encodingDesc>
  <variantEncoding method="parallel-segmentation" location="internal"/>
  <editorialDecl>
    <normalization><p>Si conservano maiuscola d'inizio verso e interpunzione.</p></normalization>
    <correction><p>Le integrazioni di lacuna sono rese con &lt;supplied&gt; (@resp, @source).</p></correction>
  </editorialDecl>
</encodingDesc>
```

## 2.3 `<profileDesc>` — mani e lingua

Ospita la dichiarazione delle mani/mezzi scrittori (`<handNotes>`, vedi
[03 – Mani e mezzi scrittori](03-mani-e-medium.md)) e la lingua (`<langUsage>`).

```xml
<langUsage>
  <language ident="it">Italiano</language>
</langUsage>
```

> **» In evoluzione.** Il valore corretto di `@ident` è il codice **`it`** (BCP 47),
> non `italiano`.

## 2.4 `<revisionDesc>` — storia del *file*

Registra le modifiche al **file XML** (chi, quando, cosa). Da non confondere con
le **fasi del testo**: quelle vanno in `<creation><listChange>` (vedi
[01 – Modello editoriale §1.2](01-modello-editoriale.md)). Sono due piani diversi.

## 2.5 `<msDesc>` — descrizione del manoscritto

La descrizione materiale del testimone (identificazione, contenuto, supporto,
dimensioni, mani, storia, *locus*, *incipit/explicit*) è **opera descrittiva del
curatore**.

> **» In evoluzione.** Nel corpus attuale i blocchi `<msDesc>` risultano
> disattivati (racchiusi in commento): vanno **riattivati** perché la descrizione
> dei manoscritti faccia parte del documento TEI e non solo del testo discorsivo.

> **» In evoluzione.** I metadati comuni a tutti i testi (responsabilità, criteri,
> mani, fasi) saranno centralizzati in un **header di corpus** (`teiCorpus`), e il
> singolo file porterà solo ciò che varia (titolo + `msDesc`).

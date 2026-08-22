# Documentazione tecnica dell'edizione
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)


Documentazione di codifica TEI P5 dell'edizione critico-genetica digitale degli
*Scartafacci* di Attilio Bertolucci. Questi file sostituiscono la precedente
documentazione in PDF con una versione **navigabile e più leggibile**; il
contenuto è aggiornato allo statuto attuale dell'edizione.

## Statuto dell'edizione (in breve)

- **Tipo:** edizione **critico-genetica** di *avant-texte* a testimone unico
  stratificato: si rappresenta il *processo* di scrittura (fasi, correzioni,
  stratificazioni), non un testo fisso.
- **Apparato:** *parallel-segmentation* con `<app>`/`<rdg>` **senza `<lem>`** — scelta
  statutaria dell'edizione: le tipologie testuali non esprimono una lezione
  definitiva, e la compresenza delle «virtualità» del testo è resa senza
  gerarchizzarla in un lemma. Vedi [04 – Apparato genetico](04-apparato-genetico.md).
- **Standard:** TEI P5 (moduli *Header, Manuscript Description, Verse, Transcription of
  Primary Sources, Critical Apparatus, Linking*).

## Indice

1. [Modello editoriale](01-modello-editoriale.md) — tipo di edizione, fasi, criteri.
2. [Il teiHeader](02-teiHeader.md) — struttura dell'intestazione e dichiarazioni.
3. [Mani e mezzi scrittori](03-mani-e-medium.md) — `handNotes`, `@medium`, `@hand`.
4. [Apparato genetico](04-apparato-genetico.md) — `app`/`rdg` senza `lem`, `add`/`del`, fasi.
5. [Fenomeni materiali e incertezza](05-fenomeni-materiali.md) — `space`, `gap`, `supplied`, `unclear`, `choice`, `retrace`, `hi`.
6. [Struttura del testo](06-struttura-del-testo.md) — `body`/`div`, `head`, `lg`/`l`, `lb`, `pb`, `ab`.
7. [Diritti e facsimili](07-diritti-e-facsimili.md) — testo non distribuito, immagini non esposte.

## Nota sulla fase precedente

L'edizione è in **reingegnerizzazione**: si abbandonano gli strumenti legati a
*Versioning Machine* e si consolidano header di corpus unico, vocabolari
controllati e validazione via ODD/Schematron. I punti ancora in evoluzione sono
segnalati nei singoli file con la dicitura **» In evoluzione**. L'apparato
**senza `<lem>`** non è in discussione: è statuto dell'edizione.

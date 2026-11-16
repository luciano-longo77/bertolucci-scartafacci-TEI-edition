# Documentazione tecnica dell'edizione
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

Documentazione di codifica TEI P5 dell'edizione critico-genetica digitale degli
*Scartafacci* di Attilio Bertolucci. Questi file sostituiscono la precedente
documentazione in PDF con una versione **navigabile**; il contenuto è allineato
allo **statuto attuale** dell'edizione e allo schema di progetto.

## Statuto dell'edizione (in breve)

- **Tipo:** edizione **critico-genetica** di *avant-texte* a testimone unico
  stratificato: si rappresenta il *processo* di scrittura (fasi, correzioni,
  stratificazioni), non un testo fisso.
- **Apparato:** *parallel-segmentation* con `<app>`/`<rdg>` **senza `<lem>`** —
  scelta statutaria. Le fasi sono i `<witness>` di `<listWit>`, ordinate da
  `@varSeq`. Vedi [04 – Apparato genetico](04-apparato-genetico.md).
- **Governance:** header di corpus unico, vocabolari controllati (mani/`medium`),
  validazione via **ODD + Schematron** con CI (vedi [`../schema/README.md`](../schema/README.md)).
- **Standard:** TEI P5 (moduli *Header, Manuscript Description, Verse, Transcription
  of Primary Sources, Critical Apparatus, Linking*).

## Indice

0. [Convenzioni — quadro normativo](00-convenzioni.md) — le regole **vincolanti** (sigle, `medium`, validazione).
1. [Modello editoriale](01-modello-editoriale.md) — tipo di edizione, fasi, criteri.
2. [Il teiHeader](02-teiHeader.md) — intestazione, header di corpus, `msDesc`.
3. [Mani e mezzi scrittori](03-mani-e-medium.md) — `handNotes`, `@medium` (vocabolario chiuso), `@hand`.
4. [Apparato genetico](04-apparato-genetico.md) — `app`/`rdg` senza `lem`, `add`/`del`/`subst`, `@varSeq`.
5. [Fenomeni materiali e incertezza](05-fenomeni-materiali.md) — `space`, `gap`, `supplied`, `unclear`, `choice`, `retrace`, `hi`.
6. [Struttura del testo](06-struttura-del-testo.md) — `body`/`div`, `head`, `lg`/`l`, `ab`.
7. [Diritti e facsimili](07-diritti-e-facsimili.md) — testo non distribuito, immagini non esposte, due strati.

## Nota sulla reingegnerizzazione

L'edizione ha **abbandonato** gli strumenti legati a *Versioning Machine* e
consolidato: header di corpus unico, vocabolari controllati, validazione via
ODD/Schematron con integrazione continua. L'apparato **senza `<lem>`** non è in
discussione: è statuto dell'edizione. Resta da completare la **migrazione** dei
file ancora nel vecchio impianto (strato privato).

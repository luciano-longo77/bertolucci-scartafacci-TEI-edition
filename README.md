# Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Validazione](https://img.shields.io/badge/validazione-ODD%20%2B%20Schematron-blue) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## Descrizione

Il progetto realizza l'**edizione critico-genetica digitale** di un nucleo di
autografi poetici inediti di Attilio Bertolucci (1930–1940), con l'obiettivo di
rappresentare non un testo fisso ma il **processo di scrittura**: le fasi
redazionali, le correzioni, le stratificazioni della pagina. La codifica segue le
*Guidelines* della **TEI P5** ed è governata da uno schema di progetto (ODD) con
controlli di integrità automatici (Schematron) in integrazione continua.

## Oggetto e corpus

Autografi conservati presso l'**Archivio di Stato di Parma**, «Archivio della
Letteratura – Archivio Bertolucci», sezione *Poesie inedite degli anni tra le due
guerre e del primo dopoguerra*. Il corpus comprende autografi inediti degli anni
Trenta, testi coevi senza data, testi anteriori al 1929 e appendici (redazioni
plurime, testi depennati, appunti d'autore).

## Modello di codifica

- **Standard:** TEI P5 (moduli *Header, Manuscript Description, Verse, Transcription
  of Primary Sources, Critical Apparatus, Linking*).
- **Apparato:** *parallel-segmentation* con `<app>`/`<rdg>` **senza `<lem>`** (scelta
  statutaria): le fasi coesistono senza gerarchizzarle in un lemma; la lezione
  critica è a sua volta un `<rdg>` (`#txt-c`), ordinata insieme alle altre da `@varSeq`.
- **Fenomeni codificati:** aggiunte, cassature, sostituzioni, rivergature, spazi
  bianchi, lacune materiali e incertezze grafiche (`add`, `del`, `subst`,
  `retrace`, `space`, `gap`, `supplied`, `unclear`).
- **Governance:** header di corpus unico (`teiCorpus`), vocabolari controllati
  (mani/`medium`), validazione via **ODD + Schematron** con CI. Vedi
  [`documentation/00-convenzioni.md`](documentation/00-convenzioni.md) e
  [`schema/README.md`](schema/README.md).

## Contenuto del repository

```
README.md             questo file
.gitignore            esclude lo strato privato (testi, immagini)
.github/workflows/    CI di validazione (well-formedness + RNG + Schematron)
documentation/        documentazione tecnica — vedi documentation/README.md
schema/               ODD di progetto, RNG, Schematron — vedi schema/README.md
header/               header di corpus condiviso (teiCorpus)
build/                strumenti (migrazione; redazione e statistiche in arrivo)
```

In programma: `specimen/` (file TEI dimostrativi redatti, senza testo protetto),
`analysis/` (statistiche delle varianti), `CITATION.cff` + DOI.

> **Due strati.** Questo repository è il **motore pubblico** (metodo, schema,
> strumenti). I file TEI col **testo integrale** vivono in uno **strato privato**
> separato e non sono distribuiti qui (vedi *Diritti*).

## Diritti e disponibilità

- Il **testo poetico** di Attilio Bertolucci è protetto dal diritto d'autore
  (tutela sino al 2070) ed è edito a stampa in *Il fuoco e la cenere. Versi e prose
  dal tempo perduto*, a cura di P. Lagazzi e G. Palli Baroni, Diabasis, 2014. **Non
  è distribuito in questo repository.**
- Le **riproduzioni fotografiche** dei manoscritti appartengono all'Archivio di
  Stato di Parma e non sono distribuite.
- La documentazione può citare **brevi frammenti** dei testi a fini di studio e
  critica (art. 70, l. 633/1941).

## Stato del progetto

Reingegnerizzazione dal precedente modello *Versioning Machine* **consolidata**:
header di corpus unico, vocabolari controllati e schema di progetto (ODD) con
Schematron e CI sono **attivi**. È in corso la **migrazione** dei file del corpus
al nuovo modello (strato privato). La documentazione tecnica in `documentation/` è
il riferimento metodologico dell'edizione.

## Come citare

> Luciano Longo, *Edizione scientifica digitale degli «Scartafacci» di Attilio
> Bertolucci*, 2015– . Repository:
> `https://github.com/luciano-longo77/bertolucci-scartafacci-TEI-edition`.

- **Autore:** Luciano Longo — [ORCID 0009-0005-7557-7546](https://orcid.org/0009-0005-7557-7546)

## Licenza

- **Codice** (ODD, script, fogli di trasformazione): licenza MIT.
- **Contenuti originali del curatore** (documentazione, descrizione dei manoscritti,
  apparato, note): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Testo di Attilio Bertolucci:** © aventi diritto; non incluso e non licenziato in
  questa sede.

## Contatti

**Luciano Longo**

- Email: [luciano.longo@dedalus.com](mailto:luciano.longo@dedalus.com)
- ORCID: <https://orcid.org/0009-0005-7557-7546>
- GitHub: <https://github.com/luciano-longo77>
- Sito: <https://luciano-longo77.github.io>

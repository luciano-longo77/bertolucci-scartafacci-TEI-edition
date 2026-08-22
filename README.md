# Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)

## Descrizione

Il progetto realizza l'**edizione critico-genetica digitale** di un nucleo di
autografi poetici inediti di Attilio Bertolucci (1930–1940), con l'obiettivo di
rappresentare non un testo fisso ma il **processo di scrittura**: le fasi
redazionali, le correzioni, le stratificazioni della pagina. La codifica segue le
*Guidelines* della **TEI P5** ed è governata da uno schema di progetto (ODD) con
controlli di integrità automatici.

## Oggetto e corpus

Autografi conservati presso l'**Archivio di Stato di Parma**, «Archivio della
Letteratura – Archivio Bertolucci», sezione *Poesie inedite degli anni tra le due
guerre e del primo dopoguerra*. Il corpus comprende autografi inediti degli anni
Trenta, testi coevi senza data, testi anteriori al 1929 e appendici (redazioni
plurime, testi depennati, appunti d'autore).

## Modello di codifica

- **Standard:** TEI P5 (moduli *Header, Manuscript Description, Verse, Transcription
  of Primary Sources, Critical Apparatus, Linking*).
- **Impianto:** critico-genetico. Il testo a testo è la lezione critica stabilita
  dal curatore; le lezioni rappresentano le **fasi elaborative** dell'autografo,
  ordinate cronologicamente e ancorate alla fase su base materiale (strumento
  scrittorio, inchiostro, topografia).
- **Fenomeni codificati:** aggiunte, cassature, sostituzioni, rivergature, spazi
  bianchi, lacune materiali e incertezze grafiche (`add`, `del`, `subst`,
  `retrace`, `space`, `gap`, `supplied`, `unclear`).
- **Governance:** schema di progetto in **ODD** con regole **Schematron** per
  l'integrità dei riferimenti interni e i vocabolari controllati; validazione
  automatica in integrazione continua.

## Contenuto del repository

```
3_documentazione/     Documentazione tecnica e metodologica dell'edizione (PDF)
README.md             Questo file
```

In corso di sviluppo (reingegnerizzazione, vedi [Stato](#stato-del-progetto)):

```
schema/               ODD di progetto, schema RNG, regole Schematron
header/               Header di corpus condiviso (teiCorpus)
docs/                 Criteri di edizione, modello genetico, tassonomie, nota diritti
specimen/             File TEI dimostrativi in forma redatta (senza testo protetto)
analysis/             Statistiche delle varianti (senza testo)
build/                Script di validazione, redazione e pubblicazione
```

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

Progetto **in reingegnerizzazione**: migrazione dal precedente modello *Versioning
Machine* a un impianto critico-genetico con ODD di progetto e header di corpus
unico. La documentazione tecnica in `3_documentazione/` descrive la fase precedente
e resta il riferimento metodologico complessivo.

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

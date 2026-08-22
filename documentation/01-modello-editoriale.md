# 1. Modello editoriale
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)

## 1.1 Che cosa è l'edizione

L'edizione ricostruisce il **processo compositivo** di un nucleo di autografi
poetici inediti di Attilio Bertolucci (1930–1940), conservati presso l'Archivio
di Stato di Parma. Ogni componimento è un *avant-texte* a **testimone unico
stratificato**: sulla stessa carta convivono più momenti di scrittura, distinti
su base materiale (strumento, inchiostro, topografia della pagina).

L'obiettivo non è fissare un testo, ma **rendere leggibile il transito del testo**:
le fasi, le correzioni, le alternative non risolte.

## 1.2 Le fasi elaborative

Le campagne correttorie sono ricondotte a **fasi** identificate materialmente. Le
sigle usate nell'apparato rimandano a questi momenti:

| Sigla | Significato |
|---|---|
| `txt-c` | testo criticamente ricostruito dal curatore (Tc) |
| `txt-1` | prima stesura (Tb0) |
| `txt-2` | interventi successivi (Tb1) |
| `txt-3`, `txt-4`… | fasi ulteriori (T1, T3…) |

> **» In evoluzione.** Nella reingegnerizzazione le fasi saranno dichiarate una
> sola volta a livello di corpus (in `<listChange>`) e richiamate dagli interventi
> con `@change`/`@varSeq`, così da rendere l'ordine cronologico *estraibile
> automaticamente*. La logica resta identica; cambia il punto in cui le fasi sono
> dichiarate.

## 1.3 Criterio dell'apparato: nessun lemma

L'apparato adotta la *parallel-segmentation* con `<app>` contenente più `<rdg>`
**senza `<lem>`**. È una scelta **statutaria**: nelle tipologie testuali degli
scartafacci spesso non esiste una lezione definitiva da eleggere a testo, e la
compresenza delle diverse virtualità va resa **senza gerarchizzarla** in un
lemma. Il testo criticamente ricostruito è a sua volta una lezione (`txt-c`), non
un `<lem>`. Dettagli in [04 – Apparato genetico](04-apparato-genetico.md).

## 1.4 Criteri di trascrizione

- Si conserva la **maiuscola** a inizio verso e il **sistema interpuntivo**
  dell'autografo.
- La **numerazione dei versi** non è presente nell'autografo: è integrazione
  editoriale (`<l n="1">`).
- Gli interventi editoriali (integrazioni di lacune, correzioni di errori) sono
  sempre **esplicitati** con gli elementi appositi (`<supplied>`, `<choice>`), mai
  taciti. Vedi [05 – Fenomeni materiali e incertezza](05-fenomeni-materiali.md).

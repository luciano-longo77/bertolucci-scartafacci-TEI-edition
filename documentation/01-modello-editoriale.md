# 1. Modello editoriale
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## 1.1 Che cosa è l'edizione

L'edizione ricostruisce il **processo compositivo** di un nucleo di autografi
poetici inediti di Attilio Bertolucci (1930–1940), conservati presso l'Archivio
di Stato di Parma. Ogni componimento è un *avant-texte* a **testimone unico
stratificato**: sulla stessa carta convivono più momenti di scrittura, distinti
su base materiale (strumento, inchiostro, topografia della pagina).

L'obiettivo non è fissare un testo, ma **rendere leggibile il transito del testo**:
le fasi, le correzioni, le alternative non risolte.

## 1.2 Le fasi elaborative

Le campagne correttorie sono ricondotte a **fasi** identificate materialmente e
dichiarate, in ciascun file, in `<front><listWit>` (ogni fase è un `<witness>`).
Le sigle usate nell'apparato rimandano a questi momenti:

| `xml:id` | Sigla | Significato |
|---|---|---|
| `txt-c` | **Tc** | testo criticamente ricostruito dal curatore |
| `txt-1` | **Tb0** | prima stesura (*base*) |
| `txt-2` | **Tb1** | correzione successiva nella **stessa campagna** (stesso strumento) |
| `txt-3`… | **T1**, **T2**… | campagne **distinte** e più tarde (es. la matita) |

**`xml:id` e sigla sono indipendenti.** L'`xml:id` è posizionale (`txt-1`, `txt-2`…
in ordine di comparsa); la sigla esprime il senso genetico. Un testo con sole due
fasi avrà `txt-1`=Tb0 e `txt-2`=**T1** (senza Tb1). La cronologia è resa
*machine-actionable* da **`@varSeq`** sui `<rdg>` (interi crescenti). Regole
normative in [00 – Convenzioni §1](00-convenzioni.md).

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

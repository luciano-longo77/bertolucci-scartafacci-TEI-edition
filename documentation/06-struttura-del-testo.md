# 6. Struttura del testo
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## 6.1 `<body>` / `<div>`

Il corpo del testo è in `<text><body>`. Ogni componimento è un `<div type="poem">`;
al suo interno l'intestazione (`<head>`) e le strofe. Si usa **solo** `<div>`
(mai la coppia numerata `<div1>`/`<div2>`).

```xml
<text>
  <body>
    <div type="poem" n="I">
      <head>…</head>
      …
    </div>
  </body>
</text>
```

## 6.2 `<head>` e apparato sul titolo

Il titolo può a sua volta essere luogo variante e ospitare un `<app>` (senza
`<lem>`), oltre a note metriche o critiche.

## 6.3 `<lg>` / `<l>` — strofe e versi

La struttura strofica si annida su due livelli: un `<lg>` esterno per la strofa,
uno interno per la forma metrica (`quatrain`, `couplet`…); `@type` semantizza la
struttura.

```xml
<lg type="quatrain" n="1">
  <l n="1">Un triste canto, un dolce e triste canto</l>
  <l n="2">Voglio cantarvi, o bianche nubi erranti</l>
</lg>
```

- **`<l>`** — verso; `@n` dà la numerazione (integrazione editoriale, assente
  nell'autografo).

## 6.4 `<ab>` — colophon; `<pb/>`

- **`<ab>`** — blocco anonimo, usato per il *colophon* (luogo e data in calce):
  `<ab type="colophon">…</ab>`.
- **`<pb/>`** — cambio di carta, da usare solo per un reale passaggio di supporto
  (con `@n`). I segnapagina **per-testimone** della Versioning Machine
  (`<pb ed="…" facs="…"/>`) sono **rimossi**: niente `@facs`, perché le immagini
  non sono esposte (vedi [07 – Diritti e facsimili](07-diritti-e-facsimili.md)).

## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)

# 6. Struttura del testo

## 6.1 `<body>` / `<div>`

Il corpo del testo è in `<text><body>`. Ogni componimento è un `<div>`; al suo
interno l'intestazione (`<head>`) e le strofe.

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
<lg n="1" type="stanza">
  <lg type="quatrain">
    <l n="1">Un triste canto, un dolce e triste canto<lb/></l>
    <l n="2">Voglio cantarvi, o bianche nubi erranti<lb/></l>
  </lg>
</lg>
```

- **`<l>`** — verso; `@n` dà la numerazione (integrazione editoriale, assente
  nell'autografo).
- **`<lb/>`** — passaggio da una linea di scrittura (reale o potenziale) a un'altra.

## 6.4 `<pb/>` e `<ab>`

- **`<pb/>`** — cambio di «pagina»/testualità processata (con `@ed`, `@facs`).
- **`<ab>`** — blocco anonimo, usato ad es. per il *colophon* (luogo e data in
  calce): `<ab type="colophon">…</ab>`.

> **» In evoluzione.** In un file (`AuIn5`) coesistono `<div1>`/`<div2>` numerati e
> `<div>` non numerati: i due modelli sono mutuamente esclusivi in TEI e vanno
> uniformati su `<div>`.

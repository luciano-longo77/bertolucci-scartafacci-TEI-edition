## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)

# 4. Apparato genetico

## 4.1 Metodo: *parallel-segmentation* senza `<lem>`

L'apparato è dichiarato in `<encodingDesc>`:

```xml
<variantEncoding method="parallel-segmentation" location="internal"/>
```

Ogni luogo variante è un `<app>` che contiene **più `<rdg>` e nessun `<lem>`**:

```xml
<app>
  <rdg wit="#txt-c">…</rdg>   <!-- testo criticamente ricostruito (Tc) -->
  <rdg wit="#txt-1">…</rdg>   <!-- prima stesura (Tb0) -->
  <rdg wit="#txt-2">…</rdg>   <!-- fase successiva (Tb1) -->
</app>
```

**Perché senza `<lem>`** (statuto dell'edizione): le tipologie testuali degli
scartafacci spesso non esprimono una lezione definitiva; eleggere un `<lem>`
imporrebbe una gerarchia che falserebbe la compresenza delle virtualità del
testo. Il testo criticamente ricostruito è *anch'esso* una lezione (`#txt-c`),
non un lemma privilegiato.

> **Nota di codifica.** `@wit` è un puntatore: va scritto **con `#`** e deve
> corrispondere a una `<witness>` dichiarata in `<listWit>`. La coerenza di questi
> riferimenti sarà imposta in validazione (Schematron).

## 4.2 Correzioni: `<add>` e `<del>`

I processi correttori si codificano con `<add>` (aggiunta) e `<del>` (cassatura):

```xml
<add place="inline" type="substitution" hand="#pen1">…</add>
<del rend="overstrike" hand="#pen1">…</del>
```

- **`@place`** (topografia dell'intervento): `inline`, `above`, `below`,
  `superscript`, `subscript`, `margin`.
- **`@type`** su `<add>` (qualità dell'aggiunta): `substitution`, `integration`,
  `adiaforia`.
- **`@rend`** su `<del>` (modalità della cassatura): es. `overstrike`,
  `overstrike-wavy`.
- **`@hand`** (mezzo scrittorio): `#pen1`, `#pen2`… → semantizza il *tempo* del
  manoscritto.

Quando cassatura e aggiunta sono un **unico atto** (X sostituisce Y), è
opportuno legarle con `<subst>`:

```xml
<subst>
  <del rend="overstrike" hand="#pen1">lieve</del>
  <add place="above" hand="#pen1">fioco</add>
</subst>
```

## 4.3 Ordine delle fasi

L'ordine cronologico delle lezioni è il contenuto stesso dell'edizione.

> **» In evoluzione.** Va reso esplicito e machine-actionable con `@varSeq` sui
> `<rdg>` e/o con `@change` che rimanda alla fase dichiarata in `<listChange>`
> (vedi [01 – Modello editoriale §1.2](01-modello-editoriale.md)). L'assenza di
> `<lem>` resta invariata.

## 4.4 Annidamento

Un `<rdg>` può contenere a sua volta cassature e aggiunte (è il caso normale della
filologia d'autore): l'asse fra fasi è l'`<app>`, dentro il quale vivono gli atti
interni (`<subst>`, `<add>`, `<del>`, `<retrace>`).

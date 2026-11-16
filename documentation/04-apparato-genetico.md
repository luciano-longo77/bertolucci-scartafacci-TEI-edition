# 4. Apparato genetico
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## 4.1 Metodo: *parallel-segmentation* senza `<lem>`

Il metodo è dichiarato nell'header di corpus:

```xml
<variantEncoding method="parallel-segmentation" location="internal"/>
```

Ogni luogo variante è un `<app>` che contiene **più `<rdg>` e nessun `<lem>`**:

```xml
<app>
  <rdg wit="#txt-c">Sempre smorta e stanca</rdg>          <!-- Tc: testo critico -->
  <rdg wit="#txt-1" varSeq="1">E stanca <space unit="char" quantity="12"/> e stanca</rdg>
  <rdg wit="#txt-2" varSeq="2"><del rend="overstrike-wavy" hand="#pen1">E stanca</del>
    <space unit="char" quantity="12"/> e stanca</rdg>
</app>
```

**Perché senza `<lem>`** (statuto dell'edizione): le tipologie testuali degli
scartafacci spesso non esprimono una lezione definitiva; eleggere un `<lem>`
imporrebbe una gerarchia che falserebbe la compresenza delle virtualità del
testo. Il testo criticamente ricostruito è *anch'esso* una lezione (`#txt-c`),
non un lemma privilegiato.

> **Nota di codifica.** `@wit` è un puntatore: va scritto **con `#`** e deve
> corrispondere a un `<witness>` dichiarato in `<listWit>`. La coerenza di questi
> riferimenti è imposta in validazione (Schematron).

## 4.2 Correzioni: `<add>`, `<del>`, `<subst>`

I processi correttori si codificano con `<add>` (aggiunta) e `<del>` (cassatura):

```xml
<add place="inline" type="integration" hand="#pen1">…</add>
<del rend="overstrike" hand="#pen1">…</del>
```

- **`@place`** (topografia): `inline`, `above`, `below`, `supralinear`, `margin`…
- **`@type`** su `<add>` (qualità dell'aggiunta): es. `integration`, `substitution`.
- **`@rend`** su `<del>` (modalità della cassatura): es. `overstrike`, `overstrike-wavy`.
- **`@hand`** (mano/mezzo): `#pen1`, `#pen2`… → semantizza il *tempo* del manoscritto.

Quando cassatura e aggiunta sono un **unico atto** (X sostituisce Y), si legano
con `<subst>`, che **richiede** almeno un `<del>` e un `<add>`:

```xml
<subst>
  <del rend="overstrike" hand="#pen1">lieve</del>
  <add place="above" hand="#pen1">fioco</add>
</subst>
```

## 4.3 Ordine delle fasi

L'ordine cronologico delle lezioni è il contenuto stesso dell'edizione ed è reso
esplicito e *machine-actionable* da **`@varSeq`** sui `<rdg>` (interi crescenti:
1, 2, 3…); `#txt-c` di norma non porta `@varSeq`. Le fasi sono i `<witness>`
dichiarati in `<listWit>` (vedi [01 §1.2](01-modello-editoriale.md)): il progetto
**non** usa `<listChange>`/`@change`. L'assenza di `<lem>` resta invariata.

## 4.4 Annidamento e rivergature

Un `<rdg>` può contenere a sua volta cassature e aggiunte (è il caso normale della
filologia d'autore): l'asse fra fasi è l'`<app>`, dentro il quale vivono gli atti
che **cambiano la lezione** (`<subst>`, `<add>`, `<del>`).

Al contrario, una **rivergatura** (`<retrace>`) che *non* altera il testo non è
una variante: **non** va in apparato, ma in linea nel verso con una
`<note type="physical">` (vedi [05 §5.6](05-fenomeni-materiali.md) e
[00 §4](00-convenzioni.md)).

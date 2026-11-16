# 3. Mani e mezzi scrittori
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## 3.1 `<handNotes>` / `<handNote>` (nell'header di corpus)

Nel `<profileDesc>` dell'header di corpus si dichiarano le **mani/mezzi
scrittori** del corpus: ogni mano riceve un identificativo, richiamato poi nel
corpo del testo dagli interventi (`@hand`).

```xml
<handNotes>
  <handNote xml:id="pen1" medium="inchiostro-nero"  scribe="Bertolucci" script="handwritten"/>
  <handNote xml:id="pen2" medium="matita-grigia"    scribe="Bertolucci" script="handwritten"/>
</handNotes>
```

- **`@xml:id`** — identificativo (`pen1`, `pen2`): è il «ponte» fra la
  dichiarazione nell'header e i richiami in `<text><body>` (`hand="#pen1"`).
- **`@medium`** — mezzo scrittorio, da **vocabolario controllato** (§3.3).
- **`@scribe`** — soggetto operante (qui sempre *Bertolucci*).

**Una mano, un mezzo.** Ogni `<handNote>` dichiara **un solo** `@medium`. Se in un
autografo convivono più strumenti, si dichiarano **più mani** (`#pen1`, `#pen2`),
mai un `@medium` composito.

## 3.2 Richiamo nel testo

Ogni intervento scrittorio dichiara la mano con `@hand`:

```xml
<add place="inline" type="integration" hand="#pen2">Sempre smorta e</add>
<del rend="overstrike" hand="#pen1">E stanca</del>
```

## 3.3 Vocabolario dei `@medium` (chiuso)

I valori di `@medium` sono **vincolati** dallo schema (ODD + Schematron): fuori
vocabolario, il file non valida.

| Valore | Significato |
|---|---|
| `inchiostro-nero` | penna a inchiostro nero |
| `inchiostro-blu` | penna a inchiostro blu |
| `matita-grigia` | matita grigia |
| `dattiloscritto` | battitura a macchina |

Mani standard del progetto (uso *tipico*): `#pen1` = `inchiostro-nero` (fasi a
inchiostro: Tb0/Tb1), `#pen2` = `matita-grigia` (interventi a matita: T1).

> Il numero di inchiostrazione, se serve distinguerlo, va tenuto separato
> (es. in `@n` o in nota), **non** fuso nel valore. Aggiungere un mezzo richiede
> **due** modifiche coordinate: la `valList` nell'ODD **e** la lista
> `$medium-ammessi` nello Schematron.

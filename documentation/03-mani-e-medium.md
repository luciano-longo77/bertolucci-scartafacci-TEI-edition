## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-in%20reingegnerizzazione-orange) ![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY%204.0-green)

# 3. Mani e mezzi scrittori

## 3.1 `<handNotes>` / `<handNote>`

Dentro `<profileDesc>` si dichiara il **sistema di inchiostrazione** del
testimone: ogni mano/mezzo scrittorio riceve un identificativo, richiamato poi
nel corpo del testo dagli interventi (`@hand`).

```xml
<handNotes>
  <handNote xml:id="pen1" medium="black_ink_1" scribe="Bertolucci"/>
  <handNote xml:id="pen2" medium="blu_ink_1"   scribe="Bertolucci"/>
  <handNote xml:id="pen3" medium="grey_pencil_1" scribe="Bertolucci"/>
</handNotes>
```

- **`@xml:id`** — identificativo (`pen1`, `pen2`…): è il «ponte» fra la
  dichiarazione nel header e i richiami in `<text><body>` (`hand="#pen1"`).
- **`@medium`** — mezzo scrittorio, codificato come *colore + strumento + numero*:
  `black_ink_1` = inchiostro nero, prima inchiostrazione; `grey_pencil_1` = matita
  grigia, ecc. Il numero conta **quante inchiostrazioni distinte** sono
  riconoscibili.
- **`@scribe`** — soggetto operante (qui sempre *Bertolucci*).

## 3.2 Richiamo nel testo

Ogni intervento scrittorio dichiara la mano con `@hand`:

```xml
<add place="above" type="substitution" hand="#pen1">…</add>
<del rend="overstrike" hand="#pen2">…</del>
```

## 3.3 Vocabolario dei `@medium`

> **» In evoluzione.** Nel corpus i valori di `@medium` sono liberi e presentano
> **incoerenze e refusi** (es. `blu_ink_2` accanto a `blue_ink_3`; `pencil_1`
> accanto a `black_pencil_1`; `datt_ink_1`). Va fissato un **vocabolario
> controllato** e dichiarato (nell'ODD), p. es.:

| Valore normalizzato | Significato |
|---|---|
| `inchiostro-nero` | penna a inchiostro nero |
| `inchiostro-blu` | penna a inchiostro blu |
| `matita-grigia` | matita grigia |
| `dattiloscritto` | battitura a macchina |

> Il numero di inchiostrazione, se serve distinguerlo, va tenuto separato (es. in
> un `@n` o nel commento), non fuso nel valore con grafie diverse.

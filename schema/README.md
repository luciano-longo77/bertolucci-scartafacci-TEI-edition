# `schema/` — Schema di progetto e validazione

Questa cartella contiene il **gate di qualità** dell'edizione: la personalizzazione TEI da cui si
generano gli schemi e le regole d'integrità che ogni file del corpus deve rispettare.

```
schema/
├── odd/
│   └── bertolucci.odd.xml     ODD di progetto (sorgente): moduli, «niente <lem>», vocabolario dei medium
├── bertolucci.rng             schema RNG generato dall'ODD (grammatica) — si rigenera dall'ODD (§1)
├── bertolucci.isosch.sch      Schematron ISO (XSLT2): integrità relazionale, statuto, vocabolari
└── README.md                  questo file
```

> **`bertolucci.rng` è un file generato**: la fonte di verità è l'ODD. Ogni volta che si tocca
> `odd/bertolucci.odd.xml` (nuovo modulo, nuovo `medium`, nuova radice) si **rigenera** l'RNG (§1) e si
> ricommettono insieme ODD e RNG. Le radici ammesse sono `TEI` (un componimento), `teiCorpus` (il corpus
> assemblato) e `teiHeader` (il file condiviso `header/corpus-header.xml`, validabile anche da solo).

## Chi controlla che cosa

| Livello | File | Garantisce |
|--------|------|-----------|
| **Grammatica** | `bertolucci.rng` (da `odd/bertolucci.odd.xml`) | elementi/attributi ammessi, struttura, **assenza di `<lem>`** (eliminato nell'ODD), `handNote/@medium` da vocabolario chiuso |
| **Integrità** | `bertolucci.isosch.sch` | `@wit` comincia con `#` e rimanda a un `<witness>` dichiarato; puntatori di mano/responsabilità risolti; `<subst>` con `del`+`add`; lingua `it`; `variantEncoding/@method = parallel-segmentation`; ribadisce «niente `<lem>`» |

Grammatica e integrità sono **complementari**: la prima dice *quali marche esistono*, la seconda *se i
rimandi fra le marche tengono*. Un file è conforme quando passa entrambe.

## 1. Generare l'RNG dall'ODD

### In oXygen (consigliato)
1. Aprire `odd/bertolucci.odd.xml`.
2. Menu **Document ▸ Transformation ▸ Configure Transformation Scenarios…**
3. Scegliere lo scenario **TEI ODD to RELAX NG XML** ed eseguirlo (*Apply associated*).
4. Salvare l'output come `schema/bertolucci.rng`.

### Da riga di comando (TEI Stylesheets / `oddc`)
```bash
# con le TEI Stylesheets installate:
teitorelaxng --odd odd/bertolucci.odd.xml bertolucci.rng
# oppure con l'oddc del pacchetto jTEI/roma
```

> L'ODD **elimina `<lem>`**: nell'RNG generato l'elemento non esiste e ogni suo uso è respinto già
> dalla grammatica, prima ancora dello Schematron.

## 2. Associare gli schemi ai file TEI

In testa a ciascun file dei testi (e all'header di corpus) si possono dichiarare entrambi gli schemi:

```xml
<?xml-model href="../schema/bertolucci.rng"
            type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="../schema/bertolucci.isosch.sch"
            type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
```

In oXygen, in alternativa: **Document ▸ Schema ▸ Associate schema…** (una volta per l'RNG, una per lo
Schematron, tipo *ISO Schematron*).

> **Attenzione — validare contro `bertolucci.rng`, non contro il TEI standard.** Se non si associa
> esplicitamente lo schema, oXygen valida i file TEI contro il suo `tei_all.rng` incorporato: quello
> **non ammette un `<teiHeader>` da solo** e boccia `header/corpus-header.xml` con
> *«element "teiHeader" not allowed here»*. Non è un errore del file: è lo schema sbagliato. Associare
> `bertolucci.rng` (dove `teiHeader` è una radice ammessa) e l'errore sparisce.

## 3. Validare

- **oXygen**: aprire il file e lanciare **Validate** (⌥⌘V). Le violazioni di grammatica e di
  Schematron compaiono insieme.
- **Riga di comando**:
  ```bash
  # grammatica
  jing schema/bertolucci.rng texts/AuIn1.xml
  # integrità (Schematron ISO, richiede un processore XSLT2, es. Saxon-HE)
  #   compilare la .sch nella pipeline ISO e applicare l'XSLT risultante al file TEI
  ```

## 4. Validazione dei file dei testi (id «esterni»)

Le mani (`#pen1`, `#pen2`) e la responsabilità (`#LL`) sono dichiarate **una sola volta**
nell'header di corpus (`header/corpus-header.xml`). Poiché i file dei testi si validano
singolarmente, lo Schematron elenca gli id attesi in una variabile `$esterni`:

```xml
<sch:let name="esterni" value="('pen1','pen2','LL')"/>
```

Quando si aggiunge una mano nuova all'header, **aggiungerne l'id anche qui** (e il relativo `medium`
nell'ODD e in `$medium-ammessi`). Validando invece il **corpus assemblato** (header + testo insieme)
tutti gli id sono locali e `$esterni` diventa ridondante.

## 5. Note

- Lo Schematron è in `queryBinding="xslt2"`: usa `tokenize`, `every … satisfies`, `starts-with`.
  Richiede un processore **XSLT2** (Saxon-HE) o oXygen. La libreria Python `lxml` (isoschematron,
  XSLT1) **non** lo esegue: per prove rapide in ambienti senza XSLT2 si replicano i controlli con
  query XPath equivalenti, ma la validazione ufficiale resta oXygen/Saxon.
- Aggiungendo elementi o attributi al modello (nuovi `@type`, nuovi `medium`, nuove lingue) si
  aggiornano **insieme** l'ODD e le liste dello Schematron, così la validazione resta un filtro reale.

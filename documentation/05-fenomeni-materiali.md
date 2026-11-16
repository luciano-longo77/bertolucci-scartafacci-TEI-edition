# 5. Fenomeni materiali e incertezza
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

Elementi per rendere lo spazio, le lacune, le integrazioni, l'incertezza e le
particolarità grafiche del documento.

## 5.1 `<space>` — spazio bianco intenzionale

Rappresenta un **luogo semantico vuoto** lasciato dall'autore, con l'estensione:

```xml
<space unit="char" quantity="12"/>
```

Spesso accompagnato da una nota fisica: `<note type="physical">…</note>`.
`<space>` **non** interpreta una lacuna: dice solo che lì c'è spazio non scritto.

## 5.2 `<gap>` — lacuna materiale

Indica una **lacuna** (perdita materiale del supporto). Attributi: `@reason` (la
causa) ed `@extent` (l'estensione):

```xml
<gap reason="damage" extent="alcuni caratteri"/>
```

## 5.3 `<supplied>` — integrazione editoriale

Elemento **conseguente** a `<gap>`: quando l'editore può integrare la lacuna. La
responsabilità dell'integrazione è del curatore (`@resp="#LL"`):

```xml
<supplied reason="damage" resp="#LL">rola</supplied>
```

## 5.4 `<unclear>` — lettura incerta

Per l'incertezza di lettura o la difficoltà di ricostruire la lezione, con
`@cert` e, se serve, `@resp`:

```xml
<unclear cert="low">cagna</unclear>
```

## 5.5 `<choice>` — correzione di errore

Per gli interventi **correttivi** (non integrativi): si affiancano la forma del
documento e quella corretta, senza normalizzare tacitamente.

```xml
<choice>
  <sic>della</sic>
  <corr resp="#LL">del</corr>
</choice>
```

## 5.6 `<retrace>` — rivergatura

Indica la **rivergatura** di una lettera o parola (tratto ripassato), elemento del
modulo *transcr*. Si marca con `@hand` (la mano/mezzo), **non** con `@change`
(che punta a un elemento `<change>`, non a un testimone). Una rivergatura che non
cambia la lezione **non** va in apparato: sta in linea nel verso (vedi
[04 §4.4](04-apparato-genetico.md)).

```xml
<l n="11">Oh com<retrace rend="overwritten" hand="#pen1">e</retrace> è stata tua stagione breve
   <note type="physical">La -e- è rivergata con lo stesso inchiostro del resto del ms.</note></l>
```

## 5.7 `<hi>` — evidenziazione grafica

Segnala **particolarità grafiche** (sottolineatura, ecc.) con `@rend`:

```xml
<hi rend="underline">Canzone compiuta</hi>
```

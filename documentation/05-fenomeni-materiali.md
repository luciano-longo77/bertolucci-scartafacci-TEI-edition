# 5. Fenomeni materiali e incertezza

Elementi per rendere lo spazio, le lacune, le integrazioni, l'incertezza e le
particolarità grafiche del documento.

## 5.1 `<space>` — spazio bianco intenzionale

Rappresenta un **luogo semantico vuoto** lasciato dall'autore, con l'estensione e
la testualità in cui ricorre:

```xml
<space resp="#txt-1" quantity="12" unit="chars"/>
```

Spesso accompagnato da una nota fisica: `<note type="physical" anchored="true">…</note>`.
`<space>` **non** interpreta una lacuna: dice solo che lì c'è spazio non scritto.

## 5.2 `<gap>` — lacuna materiale

Indica una **lacuna** (perdita materiale del supporto). Attributi: `@reason` (la
causa) ed `@extent` (l'estensione):

```xml
<gap reason="punched" extent="several_character"/>
```

## 5.3 `<supplied>` — integrazione editoriale

Elemento **conseguente** a `<gap>`: quando l'editore può integrare la lacuna.
Attributi `@resp` (responsabilità) e `@source`:

```xml
<supplied resp="#txt-c" source="other_verse_author">Casarola</supplied>
```

## 5.4 `<unclear>` — lettura incerta

Per l'incertezza di lettura o la difficoltà di ricostruire la lezione, con
`@cert`:

```xml
<unclear cert="unknown">cagna</unclear>
<unclear>[?]</unclear>
```

## 5.5 `<choice>` — correzione di errore

Per gli interventi **correttivi** (non integrativi): si affiancano la forma del
documento e quella corretta, senza normalizzare tacitamente.

```xml
<choice>
  <sic>della</sic>
  <corr resp="#txt-c">del</corr>
</choice>
```

## 5.6 `<retrace>` — rivergatura

Indica la **rivergatura** di una lettera o parola (tratto ripassato). È elemento
TEI del modulo *transcr*.

```xml
<l n="11">Oh com<retrace instant="false" rend="overwritten" cause="unclear" change="#txt-2">e</retrace> è stata tua stagione breve<lb/>
  <note>La -e- è rivergata con lo stesso inchiostro del resto del ms.</note>
</l>
```

## 5.7 `<hi>` — evidenziazione grafica

Segnala **particolarità grafiche** (sottolineatura, ecc.) con `@rend`:

```xml
<hi rend="underline">A una ballerina di tango</hi>
```

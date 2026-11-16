# 7. Diritti e facsimili
## Edizione scientifica digitale degli «Scartafacci» di Attilio Bertolucci

*Edizione critico-genetica in TEI P5 degli autografi inediti di Attilio Bertolucci
(1930–1940) conservati presso l'Archivio di Stato di Parma.*

![TEI P5](https://img.shields.io/badge/TEI-P5-blue) ![Stato](https://img.shields.io/badge/stato-attiva-brightgreen) ![Documentazione](https://img.shields.io/badge/documentazione-CC%20BY%204.0-green) ![Testi](https://img.shields.io/badge/testi-%C2%A9%20protetti-lightgrey)

## 7.1 Testo poetico

Il testo di Attilio Bertolucci è protetto dal diritto d'autore (tutela sino al
2070) ed è edito a stampa in *Il fuoco e la cenere. Versi e prose dal tempo
perduto*, a cura di P. Lagazzi e G. Palli Baroni, Diabasis, 2014. **Non è
distribuito** nell'edizione digitale pubblica. La documentazione può citare
**brevi frammenti** a fini di studio e critica (art. 70, l. 633/1941).

> **Licenze.** La **documentazione** e il **metodo** (schede, schema, strumenti)
> sono rilasciati CC BY 4.0. Il **testo poetico** e le **immagini** dei
> manoscritti **non** rientrano in questa licenza: restano tutelati e non
> distribuiti.

## 7.2 Facsimili

Le riproduzioni fotografiche dei manoscritti appartengono all'**Archivio di Stato
di Parma** e **non sono distribuite**. L'edizione **non** usa
`<facsimile>`/`<graphic>` né puntatori `@facs`: l'esistenza delle riproduzioni e
la loro sede sono documentate, in forma descrittiva, in
`<msDesc><additional><surrogates>`:

```xml
<additional>
  <surrogates>
    <p>Riproduzione fotografica consultabile presso l'Archivio di Stato di Parma;
       non distribuita in questa edizione.</p>
  </surrogates>
</additional>
```

## 7.3 I due strati

L'edizione è **una cosa sola in due strati**:

- un **master privato** (locale) coi file TEI a testo integrale;
- un **motore pubblico** (questo repository) che espone **metodo, schema,
  strumenti e documentazione** senza i testi protetti.

La build pubblica redatta si **genera** dal master oscurando i versi e conservando
struttura, apparato, note del curatore e descrizione dei manoscritti: così si
espone il **modello** senza distribuire il testo.

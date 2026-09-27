<?xml version="1.0" encoding="UTF-8"?>
<!--
  Schematron ISO (XSLT2) — gate di qualità dell'edizione «Scartafacci».
  Verifica ciò che la grammatica (RNG) non può esprimere: integrità dei rimandi,
  forma delle sigle, statuto «senza lem», vocabolari.

  Uso: associare questo file ai documenti TEI in oXygen (Document ▸ Schema ▸ Associate schema…,
  tipo «ISO Schematron»), oppure in CI compilandolo con XSLT2 (Saxon-HE) via la pipeline ISO.

  Note di funzionamento:
   · Le mani (#pen1, #pen2) e la responsabilità (#LL) sono dichiarate UNA volta nell'header di
     corpus (header/corpus-header.xml). Poiché i file dei testi si validano singolarmente, gli id
     "esterni" attesi sono elencati in $esterni: aggiungere qui ogni nuovo id dichiarato nell'header.
   · Validando il corpus assemblato (header + testo) tutti gli id risultano locali e $esterni è ridondante.
-->
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:title>Regole d'integrità — edizione «Scartafacci» (apparato senza lem)</sch:title>
  <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>

  <!-- id dichiarati altrove (header di corpus). Estendere quando si aggiungono mani/responsabili. -->
  <sch:let name="esterni" value="('pen1','pen2','LL')"/>
  <sch:let name="locali"  value="//@xml:id"/>
  <sch:let name="noti"    value="($locali, $esterni)"/>
  <sch:let name="medium-ammessi" value="('inchiostro-nero','inchiostro-blu','matita-grigia','dattiloscritto')"/>
  <sch:let name="lingue-ammesse" value="('it')"/>

  <!-- =========================================================================
       1 · STATUTO — l'apparato non usa <lem>
       ========================================================================= -->
  <sch:pattern id="statuto-no-lem">
    <sch:rule context="tei:lem">
      <sch:report test="true()" role="error">Statuto dell'edizione: l'apparato è in
        parallel-segmentation SENZA &lt;lem&gt;. La lezione critica va codificata come
        &lt;rdg wit="#txt-c"&gt;, non come &lt;lem&gt;.</sch:report>
    </sch:rule>
  </sch:pattern>

  <!-- =========================================================================
       2 · APPARATO — ogni <app> ha almeno una lettura; sigle di @wit
       ========================================================================= -->
  <sch:pattern id="apparato">
    <sch:rule context="tei:app">
      <sch:assert test="tei:rdg or tei:rdgGrp" role="error">Ogni &lt;app&gt; deve contenere almeno
        una lettura (&lt;rdg&gt; o &lt;rdgGrp&gt;).</sch:assert>
    </sch:rule>

    <!-- ogni <rdg> dentro un apparato porta una sigla -->
    <sch:rule context="tei:rdg">
      <sch:assert test="@wit" role="error">Ogni &lt;rdg&gt; deve dichiarare la sigla del testimone/fase
        in @wit (es. wit="#txt-1").</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- =========================================================================
       3 · SIGLE @wit — forma («#…») e risoluzione a un <witness> dichiarato
       ========================================================================= -->
  <sch:pattern id="sigle-wit">
    <sch:rule context="tei:*[@wit]">
      <sch:let name="tok" value="tokenize(normalize-space(@wit),'\s+')"/>
      <sch:let name="witIds" value="//tei:witness/@xml:id"/>
      <sch:assert test="every $t in $tok satisfies starts-with($t,'#')" role="error">
        @wit deve elencare puntatori che iniziano con «#» (trovato: «<sch:value-of select="@wit"/>»).</sch:assert>
      <sch:assert test="every $t in $tok satisfies substring-after($t,'#') = $witIds" role="error">
        Ogni sigla di @wit deve corrispondere a un &lt;witness&gt; dichiarato in &lt;listWit&gt;
        (verificare: «<sch:value-of select="@wit"/>»).</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- =========================================================================
       4 · PUNTATORI di mano/responsabilità — forma e risoluzione
       (@hand, @resp, @ref su name, @who su change, @target di ptr, @change)
       ========================================================================= -->
  <sch:pattern id="puntatori">
    <sch:rule context="tei:*[@hand]">
      <sch:assert test="starts-with(@hand,'#')" role="error">@hand deve iniziare con «#».</sch:assert>
      <sch:assert test="substring-after(@hand,'#') = $noti" role="error">@hand rimanda a una mano non
        dichiarata: «<sch:value-of select="@hand"/>». Le mani vanno dichiarate in &lt;handNotes&gt;
        (header di corpus); se nuova, aggiungerla anche a $esterni.</sch:assert>
    </sch:rule>

    <sch:rule context="tei:ptr[@target]">
      <sch:assert test="every $t in tokenize(normalize-space(@target),'\s+') satisfies starts-with($t,'#')"
        role="error">@target di &lt;ptr&gt; deve elencare puntatori interni («#…»).</sch:assert>
      <sch:assert test="every $t in tokenize(normalize-space(@target),'\s+') satisfies substring-after($t,'#') = $noti"
        role="error">@target di &lt;ptr&gt; non si risolve: «<sch:value-of select="@target"/>».</sch:assert>
    </sch:rule>

    <sch:rule context="tei:*[@resp]">
      <sch:assert test="every $t in tokenize(normalize-space(@resp),'\s+') satisfies starts-with($t,'#')"
        role="error">@resp deve elencare puntatori interni («#…»): «<sch:value-of select="@resp"/>».</sch:assert>
      <sch:assert test="every $t in tokenize(normalize-space(@resp),'\s+') satisfies substring-after($t,'#') = $noti"
        role="warning">@resp rimanda a un responsabile non dichiarato: «<sch:value-of select="@resp"/>».</sch:assert>
    </sch:rule>

    <sch:rule context="tei:name[@ref]">
      <sch:assert test="every $t in tokenize(normalize-space(@ref),'\s+') satisfies starts-with($t,'#')"
        role="error">@ref su &lt;name&gt; deve usare puntatori interni («#…»): «<sch:value-of select="@ref"/>».</sch:assert>
    </sch:rule>

    <sch:rule context="tei:change[@who]">
      <sch:assert test="starts-with(@who,'#')" role="error">@who deve iniziare con «#».</sch:assert>
      <sch:assert test="substring-after(@who,'#') = $noti" role="warning">@who rimanda a un responsabile
        non dichiarato: «<sch:value-of select="@who"/>».</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- =========================================================================
       5 · GENESI — <subst> richiede almeno un <del>/<surplus> e almeno un <add>
       (ridondante con TEI di base: utile su file ancora da migrare)
       ========================================================================= -->
  <sch:pattern id="subst">
    <sch:rule context="tei:subst">
      <sch:assert test="(tei:del or tei:surplus) and tei:add" role="error">&lt;subst&gt; deve contenere
        almeno un &lt;del&gt; (o &lt;surplus&gt;) e almeno un &lt;add&gt;.</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- =========================================================================
       6 · VOCABOLARI — mezzo scrittorio e lingua
       ========================================================================= -->
  <sch:pattern id="vocabolari">
    <sch:rule context="tei:handNote[@medium]">
      <sch:assert test="@medium = $medium-ammessi" role="error">@medium fuori vocabolario:
        «<sch:value-of select="@medium"/>». Ammessi: inchiostro-nero, inchiostro-blu, matita-grigia,
        dattiloscritto (estendere l'ODD e $medium-ammessi per aggiungerne).</sch:assert>
    </sch:rule>

    <sch:rule context="tei:language">
      <sch:assert test="@ident = $lingue-ammesse" role="error">La lingua va dichiarata con il codice
        «it» (non «italiano»): trovato «<sch:value-of select="@ident"/>». Per altre lingue estendere
        $lingue-ammesse.</sch:assert>
    </sch:rule>

    <!-- coerenza del modello: la codifica delle varianti è parallel-segmentation -->
    <sch:rule context="tei:variantEncoding">
      <sch:assert test="@method = 'parallel-segmentation'" role="error">L'edizione adotta la
        parallel-segmentation: variantEncoding/@method deve valere «parallel-segmentation».</sch:assert>
    </sch:rule>
  </sch:pattern>

</sch:schema>

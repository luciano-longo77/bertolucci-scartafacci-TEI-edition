#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analisi filologico-tecnica del corpus TEI Bertolucci-Scartafacci."""
import glob, os, collections
from lxml import etree

NS = {'t': 'http://www.tei-c.org/ns/1.0'}
XMLID = '{http://www.w3.org/XML/1998/namespace}id'
LANG = '{http://www.w3.org/XML/1998/namespace}lang'
files = sorted(glob.glob('1_xml/*.xml'))

report = collections.defaultdict(list)   # categoria -> [(file, dettaglio)]
stats = collections.Counter()
per_file = {}

for f in files:
    base = os.path.basename(f)
    try:
        doc = etree.parse(f)
    except Exception as e:
        report['NON_PARSABILE'].append((base, str(e)))
        continue
    root = doc.getroot()

    # namespace
    if etree.QName(root).namespace != 'http://www.tei-c.org/ns/1.0':
        report['NS_ERRATO'].append((base, etree.QName(root).namespace))

    # raccogli tutti gli xml:id dichiarati
    ids = set()
    for e in doc.iter():
        i = e.get(XMLID)
        if i:
            ids.add(i)

    # 1. riferimenti pendenti su attributi puntatori
    for attr in ('wit', 'change', 'hand', 'target', 'resp', 'facs', 'ed', 'corresp'):
        for el in doc.xpath(f'//*[@{attr}]'):
            val = el.get(attr) or ''
            for ref in val.split():
                if ref.startswith('#') and ref[1:] not in ids:
                    report['RIF_PENDENTE'].append(
                        (base, f'@{attr}="{ref}" su <{etree.QName(el).localname}>'))

    # 2. app senza rdg / lem multipli
    apps = doc.xpath('//t:app', namespaces=NS)
    stats['app_totali'] += len(apps)
    for app in apps:
        rdgs = app.xpath('t:rdg', namespaces=NS)
        lems = app.xpath('t:lem', namespaces=NS)
        if not rdgs:
            report['APP_SENZA_RDG'].append((base, doc.getpath(app)))
        if len(lems) > 1:
            report['APP_LEM_MULTIPLI'].append((base, doc.getpath(app)))
        if lems:
            stats['app_con_lem'] += 1
        else:
            stats['app_senza_lem'] += 1

    # 3. rdg: presenza di @wit e correttezza del prefisso #
    for rdg in doc.xpath('//t:rdg | //t:lem', namespaces=NS):
        w = rdg.get('wit')
        ln = etree.QName(rdg).localname
        if w is None:
            report['RDG_SENZA_WIT'].append((base, doc.getpath(rdg)))
        else:
            for token in w.split():
                if not token.startswith('#'):
                    report['WIT_SENZA_CANCELLETTO'].append((base, f'{ln} wit="{w}" (token: {token})'))

    # 4. varSeq presente? (edizione di varianti d'autore)
    if doc.xpath('//t:rdg[@varSeq]', namespaces=NS):
        stats['file_con_varSeq'] += 1

    # 5. listChange / creation
    if doc.xpath('//t:listChange', namespaces=NS):
        stats['file_con_listChange'] += 1

    # 6. subst ben formati (contengono del e add)
    for subst in doc.xpath('//t:subst', namespaces=NS):
        has_del = bool(subst.xpath('.//t:del', namespaces=NS))
        has_add = bool(subst.xpath('.//t:add', namespaces=NS))
        if not (has_del and has_add):
            report['SUBST_INCOMPLETO'].append((base, doc.getpath(subst)))

    # 7. app annidato dentro subst (rovesciamento concettuale)
    for app in doc.xpath('//t:subst//t:app', namespaces=NS):
        report['APP_DENTRO_SUBST'].append((base, doc.getpath(app)))

    # 8. listWit e coerenza @wit -> witness dichiarati
    wit_ids = set()
    for w in doc.xpath('//t:witness[@xml:id]', namespaces=NS):
        wit_ids.add(w.get(XMLID))
    used_wits = set()
    for rdg in doc.xpath('//t:rdg[@wit] | //t:lem[@wit]', namespaces=NS):
        for token in (rdg.get('wit') or '').split():
            used_wits.add(token.lstrip('#'))
    # wit usati ma non dichiarati in listWit
    for uw in used_wits - wit_ids:
        report['WIT_NON_DICHIARATO'].append((base, uw))
    # witness dichiarati ma mai usati
    for dw in wit_ids - used_wits:
        report['WITNESS_NON_USATO'].append((base, dw))

    # 9. handNote dichiarate vs @hand usate
    hand_ids = set(h.get(XMLID) for h in doc.xpath('//t:handNote[@xml:id]', namespaces=NS))
    used_hands = set()
    for el in doc.xpath('//*[@hand]'):
        for token in (el.get('hand') or '').split():
            used_hands.add(token.lstrip('#'))
    for uh in used_hands - hand_ids:
        report['HAND_NON_DICHIARATA'].append((base, uh))

    # 10. lingua dichiarata
    langs = doc.xpath('//t:language/@ident', namespaces=NS)
    for lg in langs:
        if lg not in ('it', 'ita', 'la', 'lat'):
            report['LANG_IDENT_NONSTD'].append((base, lg))

    per_file[base] = {
        'app': len(apps),
        'wit_dichiarati': sorted(wit_ids),
        'wit_usati': sorted(used_wits),
        'varSeq': bool(doc.xpath('//t:rdg[@varSeq]', namespaces=NS)),
    }
    stats['file_ok'] += 1

# --- stampa report ---
print('='*70)
print(f'CORPUS: {len(files)} file XML')
print('='*70)
print('\n### STATISTICHE GENERALI')
for k in sorted(stats):
    print(f'  {k}: {stats[k]}')

print('\n### PROBLEMI RILEVATI (per categoria)')
if not any(k for k in report):
    print('  nessuno')
for cat in sorted(report):
    items = report[cat]
    print(f'\n[{cat}] — {len(items)} occorrenze')
    # mostra al massimo 12 esempi
    for (fb, det) in items[:12]:
        print(f'    {fb}: {det}')
    if len(items) > 12:
        print(f'    ... e altre {len(items)-12}')

# --- coerenza sigle testimoni nel corpus ---
print('\n### SIGLE DEI TESTIMONI (witness @xml:id) usate nel corpus')
allwit = collections.Counter()
for b, d in per_file.items():
    for w in d['wit_dichiarati']:
        allwit[w] += 1
for w, c in allwit.most_common():
    print(f'  {w}: dichiarato in {c} file')

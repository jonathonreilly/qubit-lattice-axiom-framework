#!/usr/bin/env python3
"""Read-only, independently assembled publication/provenance checks.

Does not rerun the scientific controls or fetch the excluded external PDF.
Writes results only beside this file. Git is used only to read the tracked
baseline manifest; citation_graph.json itself is an untracked generated cache.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent
ROOT = EVIDENCE.parents[2]
SHA = lambda b: hashlib.sha256(b).hexdigest()
identities = {}


def read(p):
    b = p.read_bytes()
    identities[str(p.relative_to(ROOT))] = {"sha256": SHA(b), "bytes": len(b)}
    return b


def rows(obj):
    if isinstance(obj, dict):
        if "path" in obj and "sha256" in obj:
            yield obj
        for value in obj.values():
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)


note_path = ROOT / 'docs/MOBILE_RECORDS_GAUSS_LOOPS_STATIC_PHASE_AND_FORMATION_LOCALITY_BOUNDED_THEOREM_NOTE_2026-09-21.md'
note = read(note_path).decode()
assert SHA(note.encode()) == '7f88d63e632ce83e983b684979792b864a816f69545124f7850f4c4bbc1e829f'
runner_path = ROOT / 'scripts/mobile_records_gauss_loops_static_phase_and_formation_locality_2026_09_21.py'
assert SHA(read(runner_path)) == 'c3f3230e7b47b317d62996a7c62867e34bb9303fb34e9dbdc29c1044fba114ed'
transform = json.loads(read(EVIDENCE / 'PUBLICATION_TRANSFORM.json'))
parts = re.split(r'(?m)(?=^## Part [ABC]\. |^## Verification and review boundaries)', note)[1:4]
source_hashes = [
    '684f10acda3ebf659ed4b1b47e3fbe35a29c92dfbe1fee77e9cd9469b27f0c30',
    '1337cd3b2d7488e639b2c5e72e5a08ff3423bbf12770f21593f4817ceb640d7b',
    'f1d5234bbff516995f2ec445c889fb9bc4eaccf381274b382d3206b2dec33d3f',
]
status_replacements = [
    ('2026-09-21. Primary construction and exact finite controls; independent\nreconstruction pending.',
     '2026-09-21. Primary construction and exact finite controls; selective\nindependent reconstruction completed.'),
    ('2026-09-21. Primary derivation; selective independent reconstruction pending.\nThe finite-volume coefficient checks are complete. The polymer proof below\nis newly derived and has not yet received an independent proof check.',
     '2026-09-21. Primary derivation with completed selective independent\nfinite-volume and polymer-proof review. Two scope clarifications were\ncorrected and acknowledged; there is no formal audit verdict.'),
    None,
]
assembly = []
for i, (part, spec, expected_hash) in enumerate(zip(parts, transform['parts'], source_hashes)):
    source = read(EVIDENCE / 'primary_sources' / spec['source'])
    assert SHA(source) == spec['source_sha256'] == expected_hash
    title, body = source.decode().split('\n', 1)
    body = re.sub(r'(?m)^(#+) ', r'#\1 ', body).strip()
    changes = []
    replacement = status_replacements[i]
    if replacement:
        assert body.count(replacement[0]) == 1
        body = body.replace(*replacement)
        changes.append({'old': replacement[0], 'new': replacement[1]})
    if i == 1:
        closing = spec['additional_status_correction']
        assert body.count(closing['old']) == 1
        body = body.replace(closing['old'], closing['new'])
        changes.append(closing)
    published_title, published_body = part.split('\n', 1)
    assert published_title == f'## Part {"ABC"[i]}. ' + title[2:]
    assert body == published_body.strip()
    assert SHA(body.encode()) == spec['published_body_sha256']
    assembly.append({'source': spec['source'], 'complete_body_equal_after_only_declared_transforms': True,
                     'published_body_sha256': SHA(body.encode()), 'status_replacements': changes})

old_note = read(EVIDENCE / 'author_development/publication_status_correction' / note_path.name)
assert SHA(old_note) == '7d13b012a6e05a23ae1d195c10954814ca628afee3cfb52443134d1193af4c1e'
closing = transform['parts'][1]['additional_status_correction']
assert old_note.decode().replace(closing['old'], closing['new']) == note
assert note.replace(closing['new'], closing['old']).encode() == old_note
read(EVIDENCE / 'author_development/publication_status_correction/PUBLICATION_TRANSFORM.json')

expected_reviews = {
    'gauss_loop_independent': {
        'review/REPORT.md': '046a5c60999173d8f3a18dfab02586f2d923e61ce18d3f75b718776695bfe5af',
        'review/FINAL_SEAL.json': '2f66cd392f2caa7d0fab7192382170a930c39097cdc4c2b3aefb056769108dbf',
        'review/PRE_SOURCE_SEAL.json': 'c08bc205347df4c93f12439738293e336361935e6192f2cc1544ee02e67de817'},
    'gauss_polymer_independent': {
        'review/REPORT.md': 'b2e32ff53688d5e8e0d42aae428ae84f1f8d6d66a02213db38fea0ad48633db7',
        'review/FINAL_SEAL.json': '287bf746d940f3c70eb5c74f34fe29f7497c3b4ca9681f237e1448db629c10a5',
        'review/PRE_CHECKER_SEAL.json': '771a65053783c39cb5865e922c4211cb0e234e682613af98c735b3f159342045',
        'review/CORRECTION_ACK.json': '5f69b132dc26a9cfdec5de3c2b8c2b6beafdb778dbc7624f06456f298c1a5471'},
    'local_curl_independent': {
        'review/REPORT.md': '53c3a1455b7dc5b21084c96f4525ba7358faeedd1e2e9d16e3c7b34dff633232',
        'review/FINAL_SEAL.json': 'e687e466fd8505ad7f98e205bae0c611fd742139a638cc063b3d9e1c988240bb',
        'review/PRE_COMPARISON_SEAL.json': '6aa16724081ff1d271883722e2ca0506477c0a8e725eaae84d75c3e324804a22'},
}
manifest = json.loads(read(EVIDENCE / 'INDEPENDENT_CAPSULES.json'))
capsules = []
excluded = []
for cap in manifest['capsules']:
    raw = read(EVIDENCE / cap['archive'])
    assert SHA(raw) == cap['zip_sha256']
    with zipfile.ZipFile(EVIDENCE / cap['archive']) as z:
        assert len(z.namelist()) == len(set(z.namelist()))
        data = {name: z.read(name) for name in z.namelist()}
    declared = {x['path']: x for x in cap['members']}
    assert len(declared) == len(cap['members']) and set(data) == set(declared)
    for name, b in data.items():
        assert not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts
        assert SHA(b) == declared[name]['sha256'] and len(b) == declared[name]['bytes']
    for name, expected in expected_reviews[cap['name']].items():
        assert SHA(data[name]) == expected
    assert read(EVIDENCE / cap['report']) == data['review/REPORT.md']
    assert SHA(data['review/REPORT.md']) == cap['report_sha256']
    bindings = {(b['original_path'], b['sha256']): b for b in cap['bindings']}
    assert len(bindings) == len(cap['bindings'])
    bundled = 0
    for b in cap['bindings']:
        if b['disposition'] == 'bundled':
            payload = data[b['member']]
            assert SHA(payload) == b['sha256'] and len(payload) == b['bytes']
            bundled += 1
        else:
            assert cap['name'] == 'gauss_polymer_independent'
            assert b['disposition'] == 'external_reference_not_bundled'
            assert b['sha256'] == '2cc3e036af5b2a46afe95acf0b5863fe5c7d31554debb10a2a5cade4122bdbfc'
            assert b['bytes'] == 191795 and b['url'] == 'https://arxiv.org/pdf/math-ph/0304003v3'
            assert not any(SHA(v) == b['sha256'] for v in data.values())
            excluded.append(b)
    references = []
    for name in cap['seal_members']:
        for row in rows(json.loads(data[name])):
            bound = bindings[(row['path'], row['sha256'])]
            assert 'bytes' not in row or bound['bytes'] == row['bytes']
            references.append({'seal': name, 'path': row['path'], 'sha256': row['sha256'],
                               'disposition': bound['disposition']})
    capsules.append({'name': cap['name'], 'members': len(data), 'bundled_bindings': bundled,
                     'seal_references': len(references), 'known_original_seals_match': True,
                     'reference_details': references})
assert sum(c['members'] for c in capsules) == 115
assert sum(c['bundled_bindings'] for c in capsules) == 80
assert sum(c['seal_references'] for c in capsules) == 125
assert len(excluded) == 1

checker_hashes = {
 'microscopic_gauss_record_loop_check.py': 'dea415ec4d6be7662efff041bd7e303c03c9b0243548cbc429552f4478f616b9',
 'gauss_loop_fugacity_check.py': 'f1c6921b5dc887b4de59bbfccee5e5cad1e11dfd97270864472dfdab426908e0',
 'gauss_loop_polymer_check.py': '493542d38c4489a6245eff38846d7de80207c899b05833fcbfc38f8807912eec',
 'loop_birth_locality_check.py': 'e501e4c931a8ce9df577d3ba70a2f7706df154e5763c2b0c1021f78724e499b4'}
for name, expected in checker_hashes.items():
    assert SHA(read(EVIDENCE / 'author_checks' / name)) == expected

axioms_path = ROOT / 'docs/MINIMAL_AXIOMS_2026-06-29.md'
assert SHA(read(axioms_path)) == '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'
assert '[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)' in note
assert (note_path.parent / 'MINIMAL_AXIOMS_2026-06-29.md').resolve() == axioms_path

baseline_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
assert baseline_commit == '5d784d8ccda5268f2b7c056fcdf0d81fdb703319'
manifest_path = 'docs/audit/data/citation_graph_manifest.json'
old_bytes = subprocess.check_output(['git', 'show', baseline_commit + ':' + manifest_path], cwd=ROOT)
old = json.loads(old_bytes)
new = json.loads(read(ROOT / manifest_path))
graph = json.loads(read(ROOT / 'docs/audit/data/citation_graph.json'))
claim = 'mobile_records_gauss_loops_static_phase_and_formation_locality_bounded_theorem_note_2026-09-21'
computed_nodes = {k: {'out_degree': len(v.get('deps', [])),
                      'deps_hash': SHA('\n'.join(sorted(v.get('deps', []))).encode())[:12]}
                  for k, v in graph['nodes'].items()}
assert computed_nodes == new['nodes']
assert set(new['nodes']) - set(old['nodes']) == {claim}
assert not set(old['nodes']) - set(new['nodes'])
assert all(old['nodes'][k] == new['nodes'][k] for k in old['nodes'])
assert new['node_count'] == old['node_count'] + 1 == len(new['nodes'])
assert new['edge_count'] == old['edge_count'] + 1 == len(graph['edges'])
edge_set = {(x['from'], x['to']) for x in graph['edges']}
node_edges = {(k, d) for k, v in graph['nodes'].items() for d in v.get('deps', [])}
assert edge_set == node_edges and len(edge_set) == len(graph['edges'])
assert graph['nodes'][claim]['deps'] == ['minimal_axioms']
assert graph['nodes'][claim]['note_hash'] == SHA(note.encode())
assert graph['nodes'][claim]['runner_path'] == str(runner_path.relative_to(ROOT))
graph_receipt = json.loads(read(EVIDENCE / 'GRAPH_VERIFICATION.json'))
assert graph_receipt['manifest_sha256'] == SHA((ROOT / manifest_path).read_bytes())
graph_result = {'baseline_commit': baseline_commit, 'baseline_manifest_sha256': SHA(old_bytes),
                'baseline_nodes': old['node_count'], 'baseline_edges': old['edge_count'],
                'current_nodes': new['node_count'], 'current_edges': new['edge_count'],
                'old_manifest_entries_unchanged': len(old['nodes']),
                'actual_graph_matches_manifest': True, 'new_edge': [claim, 'minimal_axioms'],
                'limitation': 'Old graph cache is untracked. Old topology is compared through every tracked manifest dependency hash and degree, not an unavailable old full cache.'}
read(ROOT / 'docs/audit/scripts/write_citation_graph_manifest.py')
read(EVIDENCE / 'README.md')
read(EVIDENCE / 'verify_evidence.py')
verifier = subprocess.run([sys.executable, str(EVIDENCE / 'verify_evidence.py')], cwd=ROOT,
                          text=True, capture_output=True)
(HERE / 'VERIFY_EVIDENCE.stdout').write_text(verifier.stdout)
(HERE / 'VERIFY_EVIDENCE.stderr').write_text(verifier.stderr)
assert verifier.returncode == 0
for rel, identity in identities.items():
    assert SHA((ROOT / rel).read_bytes()) == identity['sha256'], 'source changed during check: ' + rel
result = {'scope': 'Assembly and provenance authentication, not new mathematics or an audit verdict.',
          'assembly': assembly, 'status_correction_inverse_verified': True,
          'capsules': capsules, 'external_exclusions': excluded, 'graph': graph_result,
          'scientific_checker_identity_matches': checker_hashes,
          'author_scientific_controls_rerun': False, 'source_identities': identities}
(HERE / 'ASSEMBLY_RESULTS.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps({'assembly_parts': len(assembly), 'members': 115, 'bundled_bindings': 80,
                  'original_seal_references': 125, 'external_pdf_exclusions': len(excluded),
                  'status_correction_inverse_verified': True, 'graph': graph_result,
                  'source_files_authenticated': len(identities), 'all_checks_passed': True}, indent=2))

#!/usr/bin/env python3
"""Independent read-only assembly/provenance check; no scientific suite execution.

The baseline is an immutable commit, never mutable HEAD. All outputs are written
beside this script; existing scientific checks, capsules and sources are read only.
"""
from pathlib import Path, PurePosixPath
import ast
import hashlib
import json
import re
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent
ROOT = EVIDENCE.parents[2]
BASE = 'c26b0171974c456f68dd92a4c8661ade1cc5ddbd'
SUPPLIER = '4ae52ade2299b4dfaff388971f423aa8f6ddf64a'
CLAIM = 'mobile_records_local_curl_quantum_interface_and_born_formation_bounded_theorem_note_2026-09-21'
NOTE = 'docs/MOBILE_RECORDS_LOCAL_CURL_QUANTUM_INTERFACE_AND_BORN_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-21.md'
RUNNER = 'scripts/mobile_records_local_curl_quantum_interface_and_born_formation_2026_09_21.py'
sha = lambda b: hashlib.sha256(b).hexdigest()
identities = {}

def read(p):
    p = Path(p)
    b = p.read_bytes()
    identities[str(p.relative_to(ROOT))] = {'sha256': sha(b), 'bytes': len(b)}
    return b

def rows(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get('path'), str) and 'sha256' in obj:
            yield obj
        for value in obj.values():
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)

def commit_read(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=ROOT)

note = read(ROOT / NOTE).decode()
runner = read(ROOT / RUNNER)
assert sha(note.encode()) == 'd39b33a6ab8bf58b1c3daab87865bbc2effb2543cab48402a57daa8dca03adbb'
assert sha(runner) == '9c38ba3dcb1b1573072d45998f380e5ead4a0dda8fd69ef2b93d7b279118b0b4'
transform = json.loads(read(EVIDENCE / 'PUBLICATION_TRANSFORM.json'))
assert transform['note'] == NOTE
parts = re.split(r'(?m)(?=^## Part [ABC]\. |^## Reproduction and remaining physical obligations)', note)[1:4]
assert len(parts) == len(transform['parts']) == 3
expected_source_hashes = [
 'a300dc4f0095cc274b6b9f4d82f0466e0cad55011c48b94e644617c4ee18280f',
 '9bb453c1041ea2a548989f14e2666df6a27c76adb8e35bf2d833eb2334bd2f5d',
 '42197693e57ead840ef3fc174c62cb56c1ae1ab7b49e3d164a36241698685c8f']
expected_replacements = [
 [('Independent review pending.', 'Selective independent mathematical review is complete.')],
 [('not yet independently reviewed.', 'with completed selective independent review.')],
 [('not independently checked yet.', 'with completed selective independent review.')]]
assembly = []
for part, spec, expected, replacements in zip(parts, transform['parts'], expected_source_hashes, expected_replacements):
    source = read(EVIDENCE / 'primary_sources' / spec['source'])
    assert sha(source) == spec['source_sha256'] == expected
    body = source.decode().split('\n', 1)[1].strip()
    body = re.sub(r'(?m)^(#+) ', r'#\1 ', body)
    assert [(r['old'], r['new']) for r in spec['replacements']] == replacements
    for old, new in replacements:
        assert body.count(old) == 1
        body = body.replace(old, new)
    published = part.split('\n', 1)[1].strip()
    assert published == body, spec['source']
    assert sha(published.encode()) == spec['published_body_sha256']
    assembly.append({'source': spec['source'], 'original_source_sha256': expected,
                     'published_body_sha256': sha(published.encode()),
                     'complete_body_equal_under_only_declared_changes': True})

known = {
 'local_curl_independent': {
  'review/REPORT.md': '53c3a1455b7dc5b21084c96f4525ba7358faeedd1e2e9d16e3c7b34dff633232',
  'review/FINAL_SEAL.json': 'e687e466fd8505ad7f98e205bae0c611fd742139a638cc063b3d9e1c988240bb',
  'review/PRE_COMPARISON_SEAL.json': '6aa16724081ff1d271883722e2ca0506477c0a8e725eaae84d75c3e324804a22'},
 'fourteen_quantum_independent': {
  'review/REPORT.md': 'ae8bdc776893ae9b7873d57f6664d7b6c36dbb56cb623948c93a958762fa47a2',
  'review/FINAL_SEAL.json': '5798645f8682e40b2238536e01146773a41689fa8b07efb15e4195ee12e9fd7b',
  'review/PRE_COMPARISON_SEAL.json': 'b8d703de6cf7c9618c51d1294a35f0d867b63ba85a61085f793e4f423aeb4ef5'}}
manifest = json.loads(read(EVIDENCE / 'INDEPENDENT_CAPSULES.json'))
assert {c['name'] for c in manifest['capsules']} == set(known)
capsules = []
exclusions = []
sealed_source_ids = set()
sealed_bytes = {}
for cap in manifest['capsules']:
    archive = read(EVIDENCE / cap['archive'])
    assert sha(archive) == cap['zip_sha256']
    with zipfile.ZipFile(EVIDENCE / cap['archive']) as z:
        assert len(z.namelist()) == len(set(z.namelist()))
        data = {name: z.read(name) for name in z.namelist()}
    declared = {m['path']: m for m in cap['members']}
    assert len(declared) == len(cap['members']) and set(declared) == set(data)
    for name, payload in data.items():
        path = PurePosixPath(name)
        assert not path.is_absolute() and '..' not in path.parts
        assert sha(payload) == declared[name]['sha256'] and len(payload) == declared[name]['bytes']
    for name, expected in known[cap['name']].items():
        assert sha(data[name]) == expected
    assert data['review/REPORT.md'] == read(EVIDENCE / cap['report'])
    assert sha(data['review/REPORT.md']) == cap['report_sha256']
    lookup = {(r['original_path'], r['sha256']): r for r in cap['bindings']}
    assert len(lookup) == len(cap['bindings'])
    bundled = 0
    for r in cap['bindings']:
        if r['disposition'] == 'bundled':
            payload = data[r['member']]
            assert sha(payload) == r['sha256'] and len(payload) == r['bytes']
            sealed_bytes[r['sha256']] = payload
            bundled += 1
        else:
            assert cap['name'] == 'fourteen_quantum_independent'
            assert r['disposition'] == 'external_reference_not_bundled'
            assert r['sha256'] == 'c919dec4d75cafd53138a9ec64d09d344ce520caadb5a85a77f7561faa70106d'
            assert r['bytes'] == 197504 and r['url'] == 'https://arxiv.org/pdf/1010.5064v1'
            assert not any(sha(b) == r['sha256'] for b in data.values())
            exclusions.append(r)
    references = []
    assert set(cap['seal_members']) == {'review/FINAL_SEAL.json', 'review/PRE_COMPARISON_SEAL.json'}
    for member in cap['seal_members']:
        for r in rows(json.loads(data[member])):
            bound = lookup[r['path'], r['sha256']]
            assert 'bytes' not in r or r['bytes'] == bound['bytes']
            sealed_source_ids.add(r['sha256'])
            references.append({'seal': member, 'path': r['path'], 'sha256': r['sha256'],
                               'disposition': bound['disposition']})
    capsules.append({'name': cap['name'], 'members': len(data), 'bundled_bindings': bundled,
                     'known_original_report_and_seals_match': True, 'seal_rows': len(references),
                     'seal_reference_details': references})
assert sum(c['members'] for c in capsules) == 109
assert sum(c['bundled_bindings'] for c in capsules) == 78
assert sum(c['seal_rows'] for c in capsules) == 129 and len(exclusions) == 1
for spec in transform['parts']:
    h = spec['source_sha256']
    assert h in sealed_source_ids
    assert read(EVIDENCE / 'primary_sources' / spec['source']) == sealed_bytes[h]

# Parse, but do not execute or import, canonical scientific runner.
values = {}
for node in ast.parse(runner).body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        key = getattr(node.targets[0], 'id', None)
        if key in {'SUITES', 'MUTATIONS', 'AUDIT_INPUT_PATHS'}:
            values[key] = ast.literal_eval(node.value)
expected_ids = {rel: sha(read(ROOT / rel)) for rel in values['AUDIT_INPUT_PATHS']}
expected_ids[RUNNER] = sha(runner)
for name, _, _ in values['SUITES']:
    payload = read(EVIDENCE / 'author_checks' / name)
    assert sha(payload) in sealed_source_ids
    assert payload == sealed_bytes[sha(payload)]
runs = json.loads(read(EVIDENCE / 'AUTHOR_RUNS.json'))
assert len(runs) == 8 and {r['mutation'] for r in runs} == {None, *values['MUTATIONS']}
author = []
for run in runs:
    mutation = run['mutation']
    raw = read(EVIDENCE / ('PRIMARY_RESULTS.json' if mutation is None else 'mutation_results/' + mutation + '.json'))
    assert sha(raw) == run['result_sha256']
    result = json.loads(raw)
    assert result['claim_id'] == CLAIM and result['identities'] == expected_ids
    assert result['mutation'] == mutation
    if mutation is None:
        assert run['returncode'] == 0 and result['passed'] and result['control_count'] == 52
        assert len(result['suites']) == 5
        for record, (name, _, count) in zip(result['suites'], values['SUITES']):
            h = sha(read(EVIDENCE / 'author_checks' / name))
            assert record['suite'] == name and record['returncode'] == 0
            assert record['source_sha256'] == record['executed_source_sha256'] == h
            assert record['results']['source_sha256'] == h
            assert len(record['results']['checks']) == count
            assert all(x['passed'] is True for x in record['results']['checks'])
        author.append({'mutation': None, 'reported_controls': 52, 'exact_source_bindings_match': True})
        baseline_stdout = run['stdout']
    else:
        assert run['returncode'] == 1 and result['passed'] is False and len(result['suites']) == 1
        name, old, new = values['MUTATIONS'][mutation]
        source = read(EVIDENCE / 'author_checks' / name).decode()
        assert source.count(old) == 1
        record = result['suites'][0]
        assert record['suite'] == name and record['returncode'] == 1
        assert record['source_sha256'] == sha(source.encode())
        assert record['executed_source_sha256'] == sha(source.replace(old, new).encode())
        assert 'AssertionError' in record['stderr'] and 'AssertionError' in run['stdout']
        assert not any(s in record['stderr'] for s in ['SyntaxError', 'ModuleNotFoundError', 'TimeoutExpired'])
        author.append({'mutation': mutation, 'suite': name, 'declared_mutated_bytes_match': True,
                       'reported_assertion': record['stderr'].splitlines()[-1]})
verification = json.loads(read(EVIDENCE / 'AUTHOR_VERIFICATION.json'))
assert verification['primary_controls'] == 52 and verification['mutations_rejected'] == 7
assert verification['runner_sha256'] == sha(runner) and verification['note_sha256'] == sha(note.encode())

# The canonical cache binds exactly the declared input list, not every proof dependency.
cache = read(ROOT / 'logs/runner-cache' / (Path(RUNNER).stem + '.txt')).decode()
digest = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
for rel in values['AUDIT_INPUT_PATHS']:
    path = rel.encode(); payload = read(ROOT / rel)
    digest.update(len(path).to_bytes(8, 'big')); digest.update(path)
    digest.update(len(payload).to_bytes(8, 'big')); digest.update(payload)
assert 'runner_sha256: ' + sha(runner) in cache
assert 'input_fingerprint_sha256: ' + digest.hexdigest() in cache
assert '\nstatus: ok\n' in cache and '\nexit_code: 0\n' in cache
stdout, stderr = cache.split('----- stdout -----\n', 1)[1].split('----- stderr -----\n')
assert stdout.strip() == baseline_stdout.strip() and not stderr.strip()
cache_result = {'fingerprint_sha256': digest.hexdigest(), 'reported_status': 'ok',
                'reported_controls': 52, 'scientific_suite_rerun': False,
                'binding_scope': 'Runner and eight declared inputs; separate review authenticates proof suppliers, capsules and graph.'}

supplier_rows = []
for commit, relative, actual, expected in [
 (BASE, 'docs/MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
  ROOT/'docs/MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
  'd5f3ef5dbe1d43c22bb63bfa4c09c71de839c59c9a405a770b7f051002d011f0'),
 (SUPPLIER, 'docs/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md',
  EVIDENCE/'suppliers/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md',
  'b10c0ad5fb9e0802b9fb7a5c206d5d9e1970b2c2573a5d792ab29b2758aea0dc')]:
    committed = commit_read(commit, relative)
    assert sha(committed) == expected and committed == read(actual)
    supplier_rows.append({'commit': commit, 'committed_path': relative, 'sha256': expected,
                          'bytes': len(committed), 'exact_worktree_or_snapshot_equality': True})
assert transform['provisional_suppliers'][0]['head'] == BASE
assert transform['provisional_suppliers'][1]['head'] == SUPPLIER
assert transform['provisional_suppliers'][1]['sha256'] == supplier_rows[1]['sha256']
axioms = read(ROOT / 'docs/MINIMAL_AXIOMS_2026-06-29.md')
assert sha(axioms) == '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'
assert '[the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)' in note
assert BASE in note and SUPPLIER in note and supplier_rows[1]['sha256'] in note
assert 'explicit provisional dependencies' in note and 'no independent audit verdict' in note

manifest_path = 'docs/audit/data/citation_graph_manifest.json'
old_bytes = commit_read(BASE, manifest_path)
old = json.loads(old_bytes); new = json.loads(read(ROOT / manifest_path))
graph = json.loads(read(ROOT / 'docs/audit/data/citation_graph.json'))
computed = {k: {'out_degree': len(v.get('deps', [])),
                'deps_hash': sha('\n'.join(sorted(v.get('deps', []))).encode())[:12]}
            for k,v in graph['nodes'].items()}
assert computed == new['nodes']
assert set(new['nodes']) - set(old['nodes']) == {CLAIM}
assert not set(old['nodes']) - set(new['nodes'])
assert all(old['nodes'][k] == new['nodes'][k] for k in old['nodes'])
assert new['node_count'] == old['node_count'] + 1 == len(new['nodes'])
assert new['edge_count'] == old['edge_count'] + 2 == len(graph['edges'])
edge_set = {(e['from'],e['to']) for e in graph['edges']}
assert len(edge_set) == len(graph['edges'])
assert edge_set == {(k,d) for k,v in graph['nodes'].items() for d in v.get('deps', [])}
assert graph['nodes'][CLAIM]['deps'] == ['minimal_axioms', 'mobile_records_immutable_transverse_curl_limits_bounded_theorem_note_2026-09-21']
assert graph['nodes'][CLAIM]['note_hash'] == sha(note.encode())
assert graph['nodes'][CLAIM]['runner_path'] == RUNNER
receipt = json.loads(read(EVIDENCE / 'GRAPH_VERIFICATION.json'))
assert receipt['nodes_added'] == 1 and receipt['edges_added'] == 2 and receipt['existing_topology_unchanged']
assert receipt['manifest_sha256'] == sha((ROOT/manifest_path).read_bytes())
graph_result = {'fixed_base_commit': BASE, 'base_manifest_sha256': sha(old_bytes),
 'base_nodes': old['node_count'], 'base_edges': old['edge_count'],
 'current_nodes': new['node_count'], 'current_edges': new['edge_count'],
 'old_manifest_entries_unchanged': len(old['nodes']), 'current_graph_matches_manifest': True,
 'current_note_hash_matches_graph': True,
 'limitation': 'Old topology comparison uses every tracked manifest dependency hash/degree; no bytewise old full generated graph comparison is asserted.'}

# Authenticate metadata and preserved development failure; execute only portable byte verifier.
for rel in ['README.md', 'verify_evidence.py', 'author_development/CACHE_ATTEMPT_01_RECEIPT.json',
            'author_development/ATTEMPT_01_CACHE_REFRESH.log']:
    read(EVIDENCE / rel)
for rel in ['docs/audit/scripts/write_citation_graph_manifest.py', 'scripts/runner_cache.py']:
    read(ROOT / rel)
verifier = subprocess.run([sys.executable, str(EVIDENCE / 'verify_evidence.py')], cwd=ROOT,
                          capture_output=True, text=True)
(HERE/'VERIFY_EVIDENCE.stdout').write_text(verifier.stdout)
(HERE/'VERIFY_EVIDENCE.stderr').write_text(verifier.stderr)
assert verifier.returncode == 0
verified = json.loads(verifier.stdout)
assert (verified['capsules'],verified['bundled_members'],verified['bundled_source_bindings'],verified['seal_rows']) == (2,109,78,129)
for rel,item in identities.items():
    assert sha((ROOT/rel).read_bytes()) == item['sha256'], 'Source changed during verification: '+rel
output = {'scope': 'Independent assembly/provenance authentication. No unchanged mathematical theorem re-proved, scientific suite rerun or audit verdict.',
 'assembly': assembly, 'capsules': capsules, 'external_exclusions': exclusions,
 'author_receipt_authentication': author, 'canonical_cache': cache_result,
 'supplier_commit_bindings': supplier_rows, 'graph': graph_result,
 'source_identities': identities, 'all_checks_passed': True}
(HERE/'ASSEMBLY_RESULTS.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
print(json.dumps({'all_checks_passed': True, 'assembly_parts': 3, 'capsules': 2, 'members': 109,
 'bundled_bindings': 78, 'original_seal_rows': 129, 'external_reference_exclusions': len(exclusions),
 'author_baseline_controls_authenticated': 52, 'assertion_rejections_authenticated': 7,
 'scientific_controls_executed': 0, 'source_files_authenticated': len(identities),
 'graph': graph_result},indent=2))

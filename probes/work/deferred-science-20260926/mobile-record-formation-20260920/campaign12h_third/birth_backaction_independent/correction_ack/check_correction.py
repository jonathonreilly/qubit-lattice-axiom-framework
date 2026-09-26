#!/usr/bin/env python3
"""Narrow H0 qualification authentication; no mathematical rerun."""
from pathlib import Path
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent
ROOT = PRIOR.parent
HISTORY = ROOT / 'birth_backaction_source_history/before_H0_qualification'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def row(p):
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}


corrected = ROOT / 'BIRTH_BACKACTION_AUTHOR_CORRECTED_SEAL.json'
assert sha(corrected) == 'b41ab32e8815b94d7eb12c8810dff6a22656b29c5ba7de39e61415f132b0f701'
new_manifest = json.loads(corrected.read_text())
mapping_path = HISTORY / 'SOURCE_PATH_MAPPING.json'
mapping = json.loads(mapping_path.read_text())
by_original = {r['path']: r for r in mapping['artifacts']}
assert len(by_original) == 12
old_seal = HISTORY / 'BIRTH_BACKACTION_AUTHOR_PRECOMPARISON_SEAL.json'
assert sha(old_seal) == mapping['preserved_author_seal_sha256'] == '437ce4aa2f75bcde51eab5e7e31a27d4387d58d19dde0e54b4d155227dec859b'
old_manifest = json.loads(old_seal.read_text())
for r in old_manifest['artifacts']:
    m = by_original[r['path']]
    assert all(m[k] == r[k] for k in ('path', 'bytes', 'sha256'))
    p = Path(m['archive_path'])
    assert p.stat().st_size == r['bytes'] and sha(p) == r['sha256']
for r in new_manifest['artifacts']:
    p = Path(r['path'])
    assert p.stat().st_size == r['bytes'] and sha(p) == r['sha256']

prior_seal = PRIOR / 'FINAL_COMPARISON_SEAL.json'
assert sha(prior_seal) == '3034807baa8f8cbc69fb7ba40b109a0878718b43d3c92e04a47e4cbeb33db366'
prior = json.loads(prior_seal.read_text())
for r in prior['artifacts']:
    p = Path(r['path'])
    assert p.stat().st_size == r['bytes'] and sha(p) == r['sha256']
for r in prior['sources']:
    p = old_seal if Path(r['path']).name == old_seal.name else Path(by_original[r['path']]['archive_path'])
    assert p.stat().st_size == r['bytes'] and sha(p) == r['sha256']

changes = [
    ('OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md',
     'Use one occupied color, a four-cycle, uniform coherent hopping kappa > 0,',
     'Use one occupied color, a four-cycle, H_0 = 0, uniform coherent hopping kappa > 0,'),
    ('pair_birth_dephasing_check.py',
     "conditions='kappa>0, beta>0, d>0; pair birth beta on every cycle edge; local dephasing d at every site')",
     "conditions='H_0=0; kappa>0, beta>0, d>0; pair birth beta on every cycle edge; local dephasing d at every site')")]
inverse_rows = []
for name, before, after in changes:
    old = (HISTORY / name).read_text()
    new = (ROOT / name).read_text()
    assert old.count(before) == new.count(after) == 1
    assert old.replace(before, after) == new
    assert new.replace(after, before) == old
    inverse_rows.append({'name': name, 'old_sha256': sha(HISTORY / name),
                         'new_sha256': sha(ROOT / name),
                         'removed': before, 'inserted': after,
                         'inverse_replacement_recovers_reviewed_bytes': True})

result_name = 'PAIR_BIRTH_DEPHASING_RESULTS.json'
old_result = json.loads((HISTORY / result_name).read_text())
new_result = json.loads((ROOT / result_name).read_text())
assert new_result['symbolic_waiting']['conditions'] == 'H_0=0; ' + old_result['symbolic_waiting']['conditions']
assert new_result['script_sha256'] == sha(ROOT / 'pair_birth_dephasing_check.py')
restored = json.loads(json.dumps(new_result))
restored['created_utc'] = old_result['created_utc']
restored['script_sha256'] = old_result['script_sha256']
restored['symbolic_waiting']['conditions'] = old_result['symbolic_waiting']['conditions']
assert restored == old_result
assert (ROOT / result_name).read_bytes() == (ROOT / 'PAIR_BIRTH_DEPHASING_RUN.log').read_bytes()
assert (ROOT / 'PAIR_BIRTH_DEPHASING_RUN.stderr').read_bytes() == b''
receipt = json.loads((ROOT / 'PAIR_BIRTH_DEPHASING_RUN_RECEIPT.json').read_text())
old_receipt = json.loads((HISTORY / 'PAIR_BIRTH_DEPHASING_RUN_RECEIPT.json').read_text())
assert receipt['command'] == old_receipt['command']
assert receipt['returncode'] == 0
assert receipt['script_sha256'] == new_result['script_sha256']
assert receipt['started_utc'] < new_result['created_utc'] < receipt['completed_utc']
changed = []
for r in new_manifest['artifacts']:
    name = Path(r['path']).name
    if r['sha256'] != by_original[r['path']]['sha256']:
        changed.append(name)
assert set(changed) == {changes[0][0], changes[1][0], result_name,
                        'PAIR_BIRTH_DEPHASING_RUN.log', 'PAIR_BIRTH_DEPHASING_RUN_RECEIPT.json'}
sources = {str(p): row(p) for p in [corrected, old_seal, mapping_path, prior_seal]}
for r in new_manifest['artifacts']:
    p = Path(r['path']); sources[str(p)] = row(p)
for m in mapping['artifacts']:
    p = Path(m['archive_path']); sources[str(p)] = row(p)
ack = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'finding': 'F1', 'status': 'closed at corrected source identities',
       'scope': 'Only the H0=0 qualification and updated result/receipt; no unchanged mathematical check rerun.',
       'exact_source_replacements': inverse_rows,
       'all_computational_results_unchanged': True,
       'new_result_changes_only': ['created_utc', 'script_sha256', 'symbolic_waiting.conditions'],
       'successful_source_bound_author_rerun_authenticated': True,
       'original_author_manifest_bindings_preserved': 12,
       'corrected_author_manifest_bindings_authenticated': 12,
       'prior_independent_artifacts_unchanged': len(prior['artifacts']),
       'prior_source_bindings_recovered_via_archive': len(prior['sources']),
       'unchanged_author_files': 12-len(changed),
       'failed_attempts': [],
       'unresolved_findings_in_this_correction': [],
       'sources': list(sources.values()),
       'limitations': 'Narrow source confirmation only; inherits the earlier proof scope and limitations. No formal audit status or broader review.'}
(HERE / 'CORRECTION_ACK.json').write_text(json.dumps(ack, indent=2)+'\n')
print(json.dumps({k:v for k,v in ack.items() if k != 'sources'}, indent=2))

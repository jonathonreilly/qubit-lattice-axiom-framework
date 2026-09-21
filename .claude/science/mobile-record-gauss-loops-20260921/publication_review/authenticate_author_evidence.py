#!/usr/bin/env python3
"""Authenticate existing author logs; never execute their scientific checks."""
from pathlib import Path
import ast
import hashlib
import json

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent
ROOT = EVIDENCE.parents[2]
sha = lambda b: hashlib.sha256(b).hexdigest()
identities = {}


def read(p):
    b = p.read_bytes()
    identities[str(p.relative_to(ROOT))] = {'sha256': sha(b), 'bytes': len(b)}
    return b


runner = ROOT / 'scripts/mobile_records_gauss_loops_static_phase_and_formation_locality_2026_09_21.py'
tree = ast.parse(read(runner))
values = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        name = getattr(node.targets[0], 'id', None)
        if name in {'SUITES', 'MUTATIONS', 'AUDIT_INPUT_PATHS'}:
            values[name] = ast.literal_eval(node.value)
expected_identities = {rel: sha(read(ROOT / rel)) for rel in values['AUDIT_INPUT_PATHS']}
expected_identities[str(runner.relative_to(ROOT))] = sha(runner.read_bytes())
runs = json.loads(read(EVIDENCE / 'AUTHOR_RUNS.json'))
assert isinstance(runs, list) and len(runs) == 1 + len(values['MUTATIONS'])
assert {r['mutation'] for r in runs} == {None, *values['MUTATIONS']}
details = []
for run in runs:
    mutation = run['mutation']
    p = EVIDENCE / ('PRIMARY_RESULTS.json' if mutation is None else 'mutation_results/' + mutation + '.json')
    raw = read(p)
    assert sha(raw) == run['result_sha256']
    result = json.loads(raw)
    assert result['identities'] == expected_identities
    assert result['mutation'] == mutation
    if mutation is None:
        assert run['returncode'] == 0 and result['passed'] is True and result['control_count'] == 35
        assert len(result['suites']) == len(values['SUITES'])
        for record, (name, _, count) in zip(result['suites'], values['SUITES']):
            h = sha(read(EVIDENCE / 'author_checks' / name))
            assert record['suite'] == name and record['returncode'] == 0
            assert record['source_sha256'] == record['executed_source_sha256'] == h
            assert record['results']['source_sha256'] == h
            assert len(record['results']['checks']) == count
            assert all(row['passed'] is True for row in record['results']['checks'])
        details.append({'mutation': None, 'controls_reported': 35, 'source_binding_authenticated': True})
    else:
        assert run['returncode'] == 1 and result['passed'] is False
        assert len(result['suites']) == 1
        name, before, after = values['MUTATIONS'][mutation]
        source = read(EVIDENCE / 'author_checks' / name).decode()
        assert source.count(before) == 1
        record = result['suites'][0]
        assert record['suite'] == name and record['returncode'] == 1
        assert record['source_sha256'] == sha(source.encode())
        assert record['executed_source_sha256'] == sha(source.replace(before, after).encode())
        assert 'AssertionError' in record['stderr'] and 'AssertionError' in run['stdout']
        assert not any(x in record['stderr'] for x in ['SyntaxError', 'ModuleNotFoundError', 'TimeoutExpired'])
        details.append({'mutation': mutation, 'suite': name,
                        'declared_mutated_bytes_authenticated': True,
                        'reported_assertion': record['stderr'].splitlines()[-1]})
verification = json.loads(read(EVIDENCE / 'AUTHOR_VERIFICATION.json'))
assert verification['primary_controls'] == 35 and verification['mutations_rejected'] == 6
assert verification['runner_sha256'] == expected_identities[str(runner.relative_to(ROOT))]
assert verification['note_sha256'] == expected_identities[values['AUDIT_INPUT_PATHS'][0]]
for rel, item in identities.items():
    assert sha((ROOT / rel).read_bytes()) == item['sha256'], rel
out = {'scope': 'Authenticated existing author records and reconstructed declared mutation bytes in memory. No scientific execution or extra independence claimed.',
       'author_runs': details, 'source_identities': identities,
       'source_bound_baseline': True, 'mutations_bound_to_exact_declared_bytes': 6}
(HERE / 'AUTHOR_EVIDENCE_AUTHENTICATION.json').write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps({'source_bound_baseline_controls_reported': 35, 'authenticated_assertion_rejections': 6,
                  'files_authenticated': len(identities), 'scientific_checks_executed': 0}, indent=2))

from pathlib import Path
import hashlib, json, difflib, math
from datetime import datetime, timezone

S = Path(__file__).resolve().parent
E = S / 'energy_adapted_refinement'
O = S / 'energy_adapted_author_root_verification'
O.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(S / 'ENERGY_ADAPTED_REFINEMENT_PROBE.md') == '65d49c82eb14b88e4880983eb8b41ecb5141cb0ff00f4e5e4760bbb12a151b9d'
assert sha(E / 'final_manifest.json') == 'a9287eb6b86016905a2e11e3e751beaee91238e5e079ca1938bdbe3425540466'
final = json.loads((E / 'final_manifest.json').read_text())
for p, h in final['files'].items():
    assert sha(p) == h, p
assert len(final['files']) == 69
core = E / 'frozen/ENERGY_ADAPTED_REFINEMENT_PROBE.md'
assert sha(core) == 'f442f32f6c40102d3378f0dc96145250b78c1c13275683ac2bc1f9125828bd80'
assert (S / 'ENERGY_ADAPTED_REFINEMENT_PROBE.md').read_bytes().startswith(core.read_bytes())
parents = json.loads((E / 'parent_final_refresh.json').read_text())
for row in parents['rows']:
    assert sha(row['source']) == sha(row['copy']) == row['sha256']
assert len(parents['rows']) == 8
manifest = json.loads((E / 'execution_manifest.json').read_text())
mh = sha(E / 'execution_manifest.json')
assert mh == 'de6d88613c3c5a362d3d80a9122b9e68dc64fee82a03c6ad52a513d010732ce1'
for p, h in manifest['files'].items():
    recovered = core if Path(p) == S / 'ENERGY_ADAPTED_REFINEMENT_PROBE.md' else Path(p)
    assert sha(recovered) == h, p
repro = json.loads((E / 'reproduction_manifest.json').read_text())
recovered_map = dict(manifest['files'])
del recovered_map[str(S / 'ENERGY_ADAPTED_REFINEMENT_PROBE.md')]
assert recovered_map == repro['files']
assert sha(E / 'reproduction_manifest.json') == '3fbcd8c8c808d8932f9d1e6ac084639a7800edad6b84021d42c5090999905907'
base = (E / 'candidate.py').read_text()
for job, old, new in [('drop_jacobian', 'JACOBIAN_POWER = .5', 'JACOBIAN_POWER = 0.'), ('reverse_cell_phase', 'CELL_PHASE_SIGN = +1', 'CELL_PHASE_SIGN = -1')]:
    assert base.count(old) == 1
    assert (E / 'variants' / (job + '.py')).read_text() == base.replace(old, new)
rows, diagnostics, receipts, summaries = [], [], [], {}
for job, expected_fail in [('baseline', 0), ('drop_jacobian', 48), ('reverse_cell_phase', 12)]:
    pair = {}
    for layer, bound in [('inner', 60), ('outer', 70)]:
        p = E / 'runs' / f'{job}_{layer}.receipt.json'
        r = json.loads(p.read_text())
        assert r['expected_manifest_sha256'] == r['actual_manifest_sha256'] == mh
        assert r['source_before'] == r['source_after'] == manifest['files']
        assert r['source_unchanged'] and not r['timeout'] and 'error' not in r
        assert r['timeout_seconds'] == bound and r['elapsed_seconds'] < bound
        assert r['returncode'] == (1 if expected_fail else 0)
        assert r['start_utc'] > manifest['created_utc'] and r['end_utc'] > r['start_utc']
        for kind in ['stdout', 'stderr']:
            assert sha(r[kind]) == r[kind + '_sha256']
        assert Path(r['stderr']).read_bytes() == b''
        pair[layer] = r
        receipts.append({'path': str(p), 'sha256': sha(p), **r})
    assert pair['outer']['start_utc'] < pair['inner']['start_utc'] < pair['inner']['end_utc'] < pair['outer']['end_utc']
    record = json.loads(Path(pair['outer']['stdout']).read_text())
    assert record['returncode'] == pair['inner']['returncode'] and not record['timeout']
    assert record['elapsed_seconds'] == pair['inner']['elapsed_seconds']
    own, diags, summary, scope = [], [], [], []
    raw = Path(pair['inner']['stdout'])
    for n, line in enumerate(raw.read_text().splitlines(), 1):
        if not line.startswith('{'):
            scope.append(line)
            continue
        d = json.loads(line)
        indexed = {'job': job, 'raw_path': str(raw), 'raw_line': n, **d}
        if 'name' in d:
            assert isinstance(d['passed'], bool)
            if 'tolerance' in d:
                assert math.isfinite(d['value']) and (d['value'] < d['tolerance']) is d['passed']
            elif 'threshold' in d:
                if 'norm_error' in d:
                    assert (d['norm_error'] < d['threshold']) is d['passed']
                else:
                    assert (d['value'] > d['threshold']) is d['passed']
            else:
                assert d['name'].startswith('exact/') or d['name'].endswith('/solver_completed')
            own.append(indexed)
        elif 'diagnostic' in d:
            diags.append(indexed)
        elif d.get('summary'):
            summary.append(d)
        else:
            raise AssertionError(d)
    assert len(own) == 238 and len({r['name'] for r in own}) == 238
    assert len(diags) == 10 and len(summary) == 1
    assert sum(not r['passed'] for r in own) == expected_fail
    assert summary[0]['total'] == 238 and summary[0]['failed'] == expected_fail and summary[0]['passed'] == 238 - expected_fail
    assert len(scope) == 5
    assert [s.split(':')[0] for s in scope] == ['per_element', 'per_site', 'per_mode', 'per_block', 'lattice_wide']
    rows += own
    diagnostics += diags
    summaries[job] = summary[0]
assert rows == json.loads((E / 'row_inventory.json').read_text())
assert diagnostics == json.loads((E / 'diagnostic_inventory.json').read_text())
(O / 'verified_receipts.json').write_text(json.dumps(receipts, indent=2) + '\n')
(O / 'complete_diagnostic_values.json').write_text(json.dumps(diagnostics, indent=2) + '\n')
result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'stored_author_evidence_checked',
    'source_files': 69, 'parent_pins': 8, 'complete_receipts': 6,
    'complete_predicates': len(rows), 'complete_diagnostics': len(diagnostics),
    'summaries': summaries,
    'manual_source_coverage': 'Complete 415-line analytic core previously read and hand checked; every 105-line final appendix addition, all 252 lines of helpers and recording code, literal variants and protocol fully read.',
    'data_coverage': 'All 714 predicates, their thresholds and original raw-line inventories mechanically checked from complete files; all 30 diagnostic values emitted for root inspection. No truncated raw print counted as complete manual review.',
    'science_rerun': False, 'independent_check': False,
    'limits': ['Finite quadrature and ODE diagnostics are not interval certificates.', 'Both mutants survive the loose geometric convergence gate; inverse-support sign correction is post-execution.', 'Infinite-dimensional domains and local sections rely on analytic proof and parent hypotheses.'],
    'pending': ['fresh independent source and evidence integration'],
}
(O / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
print(json.dumps({'all_diagnostic_values': diagnostics}))

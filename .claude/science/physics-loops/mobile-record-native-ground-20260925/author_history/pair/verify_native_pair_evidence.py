"""Exact evidence checks, without rerunning matrix/path or eigensolver controls."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib
import json

P = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text())
rat = lambda d: Fraction(d['numerator'], d['denominator'])

counts = []
data = load(P/'NATIVE_PAIR_RESULTS.json')
assert data['source_sha256'] == sha(P/'native_pair_controls.py')
for row in data['quotients']:
    matrix = [dict(pairs) for pairs in row['delta_Q_rows']]
    v = row['positive_integer_test_vector']; w = row['orbit_weights']; c = row['nonnegative_shift']
    assert all(isinstance(a, int) and a > 0 for a in v)
    assert sum(w) == row['occupancy_pair_dimension']
    ratios = []
    for i, entries in enumerate(matrix):
        for j, a in entries.items():
            assert isinstance(a, int) and (i == j or a >= 0)
            assert w[i]*a == w[j]*matrix[j].get(i, 0)
        assert entries.get(i, 0)+c >= 0
        ratios.append(Fraction(sum(a*v[j] for j, a in entries.items()), v[i]))
    bounds = row['exact_delta_Q_Perron_interval']
    assert min(ratios) == rat(bounds['lower']) and max(ratios) == rat(bounds['upper'])
    gap = row['proposed_ground_gap_g2_tau_interval']
    assert rat(gap['lower']) == -max(ratios)/4 and rat(gap['upper']) == -min(ratios)/4
    counts.append({'side': row['side'], 'rows': len(matrix), 'integer_entries': sum(map(len, matrix)),
                   'gap_exact': gap, 'row_sum_min': min(sum(r.values()) for r in matrix),
                   'row_sum_max': max(sum(r.values()) for r in matrix)})
cube = data['full_colored_cube']; q = cube['full_positive_Q']; occ = cube['occupancy_positive_Q']
assert len(q) == 36 and all(len(r) == 36 for r in q)
assert all(a >= 0 and a == q[j][i] for i, r in enumerate(q) for j, a in enumerate(r))
assert {sum(r) for r in q} == {98} == {sum(r) for r in occ}
for i in range(36):
    for j in range(6):
        assert sum(q[i][j*6:(j+1)*6]) == occ[i//6][j]
assert cube['vacuum_flat_H4'] == -108 and cube['exact_flat_H4_ground_difference'] == 10

local = load(P/'LOCAL_ROW_CERTIFICATE.json')
poly = load(P/'ROW_POLYNOMIAL_CERTIFICATE.json')
assert local['source_sha256'] == sha(P/'native_pair_local_row_certificate.py')
assert local['helper_sha256'] == sha(P/'native_pair_controls.py')
assert poly['source_sha256'] == sha(P/'native_pair_row_polynomial_certificate.py')
assert poly['topology_helper_sha256'] == local['source_sha256']
assert poly['prior_row_certificate_sha256'] == sha(P/'LOCAL_ROW_CERTIFICATE.json')
assert len(local['near_rows']) == 84 and len(local['far_controls']) == 4
assert poly['synthetic']['exhaustive_input_pairs'] == 180
assert sum(r['count']*r['row_contribution'] for r in poly['single_occupied_B_contributions']) == 6048
for r in poly['two_occupied_B_interactions']:
    assert sum(x['pairs'] for x in r['interaction_counts']) == r['common_active_pairs']
    correction = sum(x['pairs']*x['interaction_per_pair'] for x in r['interaction_counts'])
    assert correction == r['interaction_row_correction']
    assert 12096+correction == r['full_row_sum']
    matching = [x for x in local['near_rows'] if tuple(x['displacement']) == tuple(r['displacement'])]
    assert len(matching) == 1 and matching[0]['row_sum'] == r['full_row_sum']
assert min(r['row_sum'] for r in local['near_rows']+local['far_controls']) == 11512
assert max(r['row_sum'] for r in local['near_rows']+local['far_controls']) == 12248

executions = []
for prefix, receipt, code in [('CONTROL','EXECUTION.json','native_pair_controls.py'),
                               ('LOCAL','LOCAL_EXECUTION.json','native_pair_local_row_certificate.py'),
                               ('POLYNOMIAL','POLYNOMIAL_EXECUTION.json','native_pair_row_polynomial_certificate.py')]:
    d = load(P/receipt)
    assert d['code_sha256'] == sha(P/code)
    assert d['stdout_sha256'] == sha(P/(prefix+'.stdout'))
    assert (P/(prefix+'.stderr')).stat().st_size == d['stderr_bytes'] == 0
    assert d['exit_code'] == 0
    executions.append(d)

report = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'verifier_sha256': sha(Path(__file__)),
          'quotient_certificates': counts, 'full_cube_integer_rows': 36,
          'unwrapped_near_rows': 84, 'far_controls': 4, 'synthetic_pair_cases': 180,
          'all_live_code_result_execution_bindings': True, 'executions': executions,
          'new_scientific_runs': 0,
          'scope': 'Root exact certificate arithmetic and bindings, not independent scientific reconstruction or a numerical check of the unbounded-operator limit.'}
(P/'ROOT_VERIFICATION.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))

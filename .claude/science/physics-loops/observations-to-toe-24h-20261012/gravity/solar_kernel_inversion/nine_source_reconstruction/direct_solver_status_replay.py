#!/usr/bin/env python3
"""Supplement omitted second-stage status with an identified, unchanged replay."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import datetime as dt
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity/response_inverse/nine_source')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    path = ROOT / 'SOLVER_STATUS_REPLAY_v1.json'
    assert not path.exists()
    original = json.loads((ROOT / 'CANDIDATES_v1.json').read_text())
    options = {'primal_feasibility_tolerance': 1e-9, 'dual_feasibility_tolerance': 1e-9,
               'ipm_optimality_tolerance': 1e-10}
    rows = []
    for case in original['cases']:
        mp = ROOT / 'finite_lp_certificates_v1' / (case['name'] + '_matrix.json')
        m = json.loads(mp.read_text())
        a = np.array([[float.fromhex(x) for x in row] for row in m['A_hex']])
        b = np.array([float.fromhex(x) for x in m['b_hex']])
        first = linprog(np.r_[np.zeros(20), 1.], A_ub=a, b_ub=b,
                        bounds=[(0, None)] * 21, method='highs', options=options)
        assert first.success
        second = linprog(np.r_[np.ones(20), 0.],
                         A_ub=np.vstack([a, np.r_[np.zeros(20), 1.]]),
                         b_ub=np.r_[b, first.x[-1] + 1e-8],
                         bounds=[(0, None)] * 21, method='highs', options=options)
        assert second.success
        old = case['solution']
        assert np.array_equal(second.x[:-1], np.array(old['weights']))
        assert float(second.x[-1]) == old['fitted_t']
        rows.append({'name': case['name'], 'matrix_sha256': sha(mp),
                     'first': {'status': int(first.status), 'message': first.message},
                     'second': {'status': int(second.status), 'message': second.message},
                     'weights_and_t_bitwise_match_original': True})
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'source_sha256': sha(Path(__file__)),
              'candidates_sha256': sha(ROOT / 'CANDIDATES_v1.json'),
              'purpose': 'The original helper asserted second-stage success but omitted its explicit status/message from the saved receipt. These are replay statuses, not retroactively original-run logs. No fit or selection is changed.',
              'cases': rows}
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact rational lower bounds for the frozen binary64 nine-source LPs."""
from __future__ import annotations
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import direct_nine_source as nine
import numpy as np
from scipy.optimize import linprog

OUT = nine.OUT / 'finite_lp_certificates_v1'

def read(p):
    return json.loads(p.read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(p, value):
    assert not p.exists(), 'Never overwrite a certificate'
    p.write_text(json.dumps(value, indent=2) + '\n')

def ratio(x):
    return [str(x.numerator), str(x.denominator)]

def floor_decimal(x, places=12):
    scale = 10 ** places
    n = (x.numerator * scale) // x.denominator
    return ('-' if n < 0 else '') + str(abs(n) // scale) + '.' + str(abs(n) % scale).zfill(places)

def row_labels(rows, differential, external, solar):
    labels = []
    for row in rows:
        for side in ['upper_velocity_rectangle', 'lower_velocity_rectangle']:
            labels += [{'kind': side, 'source': row['name'], 'scored_bin': i,
                        'R_kpc': float(r)} for i, r in enumerate(row['R'])]
    labels.append({'kind': 'weight_cap', 'cap': 100})
    if differential:
        labels += [{'kind': 'D_nonnegative_upper_ramp_limit', 'ramp': j} for j in range(20)]
    if external is not None:
        labels += [{'kind': 'external_upper'}, {'kind': 'external_lower'}]
        if solar:
            labels.append({'kind': 'solar_upper'})
    return labels

def main():
    nine.op.guard()
    OUT.mkdir(exist_ok=False)
    freeze = read(nine.OUT / 'FREEZE.json')
    assert nine.identities() == freeze['identities']
    paths = {name: (nine.op.OUT if name in nine.OLD else nine.OUT) / f'operator_{name}_v1.json'
             for name in nine.NAMES}
    candidates = read(nine.OUT / 'CANDIDATES_v1.json')
    assert candidates['operators'] == {name: sha(p) for name, p in paths.items()}
    rows = nine.training_rows(paths)
    identities = {'source_sha256': sha(Path(__file__)),
                  'protocol_sha256': sha(HERE / 'FINITE_LP_CERTIFICATE_PROTOCOL.md'),
                  'fit_source_sha256': sha(Path(nine.fit.__file__)),
                  'nine_source_sha256': sha(Path(nine.__file__)),
                  'freeze_sha256': sha(nine.OUT / 'FREEZE.json'),
                  'candidates_sha256': sha(nine.OUT / 'CANDIDATES_v1.json'),
                  'results_sha256': sha(nine.OUT / 'RESULTS_v1.json')}
    results = []
    objective = np.r_[np.zeros(20), 1.]
    for case in candidates['cases']:
        nine.op.guard()
        s = case['solution']
        differential = s['differential_response_constraint']
        external, solar = s['external_newtonian_SI'], s['solar_bound_imposed']
        a, b, _ = nine.fit.constraints(rows, differential, external, solar)
        labels = row_labels(rows, differential, external, solar)
        assert len(labels) == len(b) and a.shape == (len(b), 21)
        matrix_file = OUT / (case['name'] + '_matrix.json')
        write(matrix_file, {'name': case['name'], 'identities': identities,
                           'A_hex': [[float(v).hex() for v in row] for row in a],
                           'b_hex': [float(v).hex() for v in b], 'row_labels': labels,
                           'objective': [0] * 20 + [1], 'variables': 'w0..w19,t >= 0'})
        solved = linprog(objective, A_ub=a, b_ub=b, bounds=[(0, None)] * 21,
                         method='highs', options={'primal_feasibility_tolerance': 1e-9,
                         'dual_feasibility_tolerance': 1e-9, 'ipm_optimality_tolerance': 1e-10})
        assert solved.success and abs(float(solved.fun) - s['primary_minimum_t']) < 1e-10
        ar = [[F(float(v)) for v in row] for row in a]
        br = [F(float(v)) for v in b]
        proposed = [F(float(v)) for v in solved.ineqlin.marginals]
        y = [min(F(0), v) for v in proposed]
        time_column = sum(row[-1] * yi for row, yi in zip(ar, y))
        multiplier = 1 / max(F(1), time_column)
        y = [v * multiplier for v in y]
        at_y = [sum(row[j] * yi for row, yi in zip(ar, y)) for j in range(21)]
        assert all(yi <= 0 for yi in y) and at_y[-1] <= 1
        deficit = max([F(0)] + at_y[:-1])
        dual_value = sum(bi * yi for bi, yi in zip(br, y))
        lower = dual_value - 100 * deficit
        assert lower > 0
        certificate = {'name': case['name'], 'identities': identities,
                       'matrix_sha256': sha(matrix_file), 'y_rational': [ratio(v) for v in y],
                       'proposed_y_hex': [float(v).hex() for v in solved.ineqlin.marginals],
                       'rescale_rational': ratio(multiplier), 'weight_cap': 100,
                       'weight_deficit_rational': ratio(deficit),
                       'time_residual_rational': ratio(1 - at_y[-1]),
                       'lower_bound_rational': ratio(lower),
                       'lower_bound_decimal_downward': floor_decimal(lower),
                       'solver_primary_t_approximate': float(solved.fun),
                       'nonzero_dual_rows': [{**labels[i], 'row': i, 'y_approximate': float(v)}
                                            for i, v in enumerate(y) if v],
                       'scope': 'Exact finite binary64 matrix interpreted rationally; not a continuum no-go.'}
        cert_file = OUT / (case['name'] + '_certificate.json')
        write(cert_file, certificate)
        results.append({'name': case['name'], 'matrix_sha256': sha(matrix_file),
                        'certificate_sha256': sha(cert_file),
                        'lower_bound_decimal_downward': certificate['lower_bound_decimal_downward'],
                        'nonzero_dual_rows': certificate['nonzero_dual_rows']})
        print(json.dumps(results[-1]), flush=True)
    assert nine.identities() == freeze['identities']
    write(OUT / 'RESULTS.json', {'at': dt.datetime.now(dt.timezone.utc).isoformat(),
                               'identities': identities, 'certificates': results})

if __name__ == '__main__':
    main()

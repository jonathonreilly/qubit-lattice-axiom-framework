#!/usr/bin/env python3
"""Frozen linear inverse problems; candidate fields require later validation."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import direct_galaxy_response_operator as operator
import direct_response_basis as solar

NAMES = ['NGC2976', 'UGC07577', 'KK98-251']
GM = 1.32712440018e20
EXTERNAL = np.array([2.00e-10, 2.64e-10])
QMAX = 5.2e-27


def training_rows():
    control_path = operator.OUT / 'operator_controls_v1.json'
    controls = json.loads(control_path.read_text())
    assert controls['passed'] and controls['source_sha256'] == operator.field.sha(operator.__file__)
    rows = []
    with np.load(operator.field.DATA / 'baryonic_forward_64.npz') as source, np.load(operator.field.DATA / 'sealed_targets.npz') as target:
        for name in NAMES:
            path = operator.OUT / f'operator_{name}_v1.json'
            receipt = json.loads(path.read_text())
            assert receipt['source_sha256'] == operator.field.sha(operator.__file__)
            assert receipt['protocol_sha256'] == operator.PROTOCOL_HASH
            assert receipt['solver_sha256'] == operator.SOLVER_HASH
            mask = source[name + '_score_mask']
            radius = source[name + '_R'][mask]
            assert np.array_equal(radius, receipt['R_kpc'])
            assert np.array_equal(operator.KNOTS, receipt['knots_SI'])
            velocity, error = target[name + '_v'][mask], target[name + '_error'][mask]
            assert np.all(np.isfinite(error) & (error >= 0))
            assert np.all(np.isfinite(velocity) & (velocity > 0) & (radius > 0))
            rows.append({'name': name, 'R': radius, 'A': velocity ** 2 / radius,
                         'low': np.maximum(0, velocity - 2 * error) ** 2 / radius,
                         'high': (velocity + 2 * error) ** 2 / radius,
                         'g_N': np.array(receipt['g_N']), 'K': np.array(receipt['K']),
                         'operator_receipt_sha256': operator.field.sha(path)})
    return rows


def constraints(rows, differential=False, external=None, solar_limit=False):
    matrix, bound = [], []
    for row in rows:
        k = row['K'] / row['A'][:, None]
        g = row['g_N'] / row['A']
        matrix.extend(np.c_[k, -np.ones(len(k))])
        bound.extend(row['high'] / row['A'] - g)
        matrix.extend(np.c_[-k, -np.ones(len(k))])
        bound.extend(g - row['low'] / row['A'])
    matrix.append(np.r_[np.ones(20), 0.])
    bound.append(100.)
    if differential:
        for j in range(20):
            row = np.zeros(21)
            row[j] = 1 / np.log(operator.KNOTS[j + 1] / operator.KNOTS[j])
            row[j + 1:20] = -1
            matrix.append(row)
            bound.append(1.)
    solar_coeff = None
    if external is not None:
        value = np.array([float(operator.ramp(external, lo, hi))
                          for lo, hi in zip(operator.KNOTS[:-1], operator.KNOTS[1:])])
        # Divide by E so the bound is N(E), with the same response as galaxies.
        matrix.extend([np.r_[value, 0.], np.r_[-value, 0.]])
        bound.extend([EXTERNAL[1] / external - 1, 1 - EXTERNAL[0] / external])
        solar_coeff = external ** 1.5 / np.sqrt(GM) * np.array([
            solar.positive_integral(lo / external, hi / external)[0]
            for lo, hi in zip(operator.KNOTS[:-1], operator.KNOTS[1:])])
        assert np.all(np.isfinite(solar_coeff) & (solar_coeff > 0))
        if solar_limit:
            matrix.append(np.r_[solar_coeff / QMAX, 0.])
            bound.append(1.)
    elif solar_limit:
        raise ValueError('The solar operator requires an explicit Newtonian external field')
    return np.array(matrix), np.array(bound), solar_coeff


def solve(rows, differential, external=None, solar_limit=False):
    operator.guard()
    matrix, bound, q = constraints(rows, differential, external, solar_limit)
    options = {'primal_feasibility_tolerance': 1e-9, 'dual_feasibility_tolerance': 1e-9,
               'ipm_optimality_tolerance': 1e-10}
    objective = np.r_[np.zeros(20), 1.]
    first = linprog(objective, A_ub=matrix, b_ub=bound, bounds=[(0, None)] * 21,
                    method='highs', options=options)
    row = {'external_newtonian_SI': external, 'differential_response_constraint': differential,
           'solar_bound_imposed': solar_limit, 'status': int(first.status), 'message': first.message}
    if not first.success:
        return row
    primary_minimum = float(first.x[-1])
    matrix2 = np.vstack([matrix, np.r_[np.zeros(20), 1.]])
    bound2 = np.r_[bound, primary_minimum + 1e-8]
    second = linprog(np.r_[np.ones(20), 0.], A_ub=matrix2, b_ub=bound2,
                     bounds=[(0, None)] * 21, method='highs', options=options)
    assert second.success, second.message
    value = second.x
    max_violation = float(max(0., np.max(matrix2 @ value - bound2), -np.min(value)))
    assert max_violation <= 1e-7, f'Failed scaled primal residual: {max_violation}'
    weights, tolerance = value[:-1], float(value[-1])
    external_pred = None
    if external is not None:
        external_pred = external * (1 + sum(weight * float(operator.ramp(external, lo, hi))
                           for weight, lo, hi in zip(weights, operator.KNOTS[:-1], operator.KNOTS[1:])))
    row.update(primary_minimum_t=primary_minimum, fitted_t=tolerance,
               weights=weights.tolist(), total_weight=float(weights.sum()),
               max_scaled_primal_violation=max_violation, predicted_external_physical_SI=external_pred,
               Q2_s_minus2=None if q is None else float(q @ weights),
               force_positive=all(np.all(r['g_N'] + r['K'] @ weights > 0) for r in rows))
    return row


def rank(row):
    return row['primary_minimum_t'], row['total_weight'], row['external_newtonian_SI'] or 0.


def external_scan(rows, differential, solar_limit):
    grid = np.geomspace(EXTERNAL[0] / 101, EXTERNAL[1], 129)
    evaluated = {}
    def evaluate(e):
        e = float(e)
        if e not in evaluated:
            evaluated[e] = solve(rows, differential, e, solar_limit)
        return evaluated[e]
    for e in grid:
        evaluate(e)
    eligible = [i for i in range(len(grid)) if evaluated[float(grid[i])]['status'] == 0]
    best_indices = sorted(eligible, key=lambda i: rank(evaluated[float(grid[i])]))[:3]
    intervals = set()
    for i in best_indices:
        if i > 0:
            intervals.add((float(grid[i - 1]), float(grid[i])))
        if i + 1 < len(grid):
            intervals.add((float(grid[i]), float(grid[i + 1])))
    for _ in range(4):
        next_intervals = set()
        for low, high in sorted(intervals):
            midpoint = np.sqrt(low * high)
            evaluate(midpoint)
            next_intervals.update([(low, midpoint), (midpoint, high)])
        intervals = next_intervals
    solutions = [row for row in evaluated.values() if row['status'] == 0]
    return {'evaluated_nodes': len(evaluated),
            'best_sampled': min(solutions, key=rank) if solutions else None,
            'samples': sorted(evaluated.values(), key=lambda x: x['external_newtonian_SI']),
            'continuous_external_optimality_claimed': False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    operator.guard()
    assert not args.output.exists(), 'Never overwrite inverse-fit receipts'
    source_hash = operator.field.sha(__file__)
    rows = training_rows()
    cases = []
    for differential in [False, True]:
        family = 'D' if differential else 'M'
        alone = solve(rows, differential)
        cases.append({'family': family, 'constraints': 'galaxies_only', 'best_sampled': alone})
        print(json.dumps({'family': family, 'constraints': 'galaxies_only', 'solution': alone}), flush=True)
        for solar_limit in [False, True]:
            label = 'galaxies_external_solar' if solar_limit else 'galaxies_external'
            scan = external_scan(rows, differential, solar_limit)
            cases.append({'family': family, 'constraints': label, **scan})
            print(json.dumps({'family': family, 'constraints': label, 'best_sampled': scan['best_sampled'],
                              'nodes': scan['evaluated_nodes']}), flush=True)
    assert operator.field.sha(__file__) == source_hash
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source_hash,
              'operator_source_sha256': operator.field.sha(operator.__file__),
              'solar_basis_source_sha256': operator.field.sha(solar.__file__),
              'protocol_sha256': operator.PROTOCOL_HASH,
              'operator_receipts': {r['name']: r['operator_receipt_sha256'] for r in rows},
              'targets_sha256': operator.field.sha(operator.field.DATA / 'sealed_targets.npz'),
              'cases': cases, 'candidate_field_validation_required': True,
              'limits': 'Numerical best sampled inverse fits on three exposed sources. Solar and external measurements are fitted constraints, not predictions. No candidate is empirically accepted before direct/refined field validation. No universal exclusion or joint confidence statement.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Compare independently rebuilt histories, selected bootstrap quantiles and theory."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import runpy
import numpy as np
import sympy as sp
from scipy.linalg import expm

OUT = Path(__file__).resolve().parent
RAW = OUT.parent
EXTERNAL_ANALYSIS = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/dimer_routed_dynamic_analysis')


def ident(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def verify(row):
    assert ident(Path(row['path'])) == row, row['path']
    return row


def numeric_error(actual, expected, tolerance=2e-12):
    a, b = np.asarray(actual, dtype=float), np.asarray(expected, dtype=float)
    assert a.shape == b.shape and np.isfinite(a).all() and np.isfinite(b).all()
    absolute = float(np.max(abs(a - b)))
    scaled = float(np.max(abs(a - b) / np.maximum(1., abs(b))))
    assert scaled < tolerance, (a.shape, absolute, scaled)
    return {'entries': a.size, 'absolute_error': absolute, 'scaled_error': scaled}


def main():
    pre = json.loads((OUT / 'PRE_COMPARISON_SEAL.json').read_text())
    rawseal = json.loads((OUT / 'RAW_RECONSTRUCTION_SEAL.json').read_text())
    for row in [pre['primary_source']] + pre['reused_dependencies'] + pre['artifacts'] + rawseal['artifacts']:
        verify(row)
    ownh = json.loads((OUT / 'REBUILT_PER_HISTORY.json').read_text())
    owna = json.loads((OUT / 'REBUILT_AGGREGATES.json').read_text())
    ownauth = json.loads((OUT / 'RAW_HISTORY_AUTHENTICATION.json').read_text())
    files = ['dimer_routed_dynamic_results/RESULTS.json', 'dimer_routed_dynamic_results/PER_HISTORY.json',
             'dimer_routed_dynamic_results/AUTHENTICATION.json', 'DIMER_ROUTED_DYNAMIC_ANALYSIS_SIGN_CONTROLS.json',
             'dimer_routed_finite_wavelength_checks/RESULTS.json', 'dimer_routed_finite_wavelength_comparison/RESULTS.json']
    sources = [ident(RAW / f) for f in files]
    original, histories, authentication, signs, theory, comparison = [json.loads((RAW / f).read_text()) for f in files]
    external_bindings = []
    for name in ['RESULTS.json', 'PER_HISTORY.json', 'AUTHENTICATION.json']:
        e = ident(EXTERNAL_ANALYSIS / name); r = ident(RAW / 'dimer_routed_dynamic_results' / name)
        assert e['sha256'] == r['sha256'] and e['bytes'] == r['bytes']
        external_bindings.append(e)
    for name in ['analyzer', 'sign_controls', 'manifest', 'summary', 'per_history', 'authentication']:
        verify(original[name])
    for row in theory['sources']:
        verify(row)
    for name in ['comparison_source', 'frozen_projection', 'original_analysis']:
        verify(comparison[name])
    assert signs['analyzer'] == original['analyzer']
    assert original['bootstrap']['draws'] == signs['bootstrap_draws'] == 10000
    assert original['bootstrap']['seed'] == signs['bootstrap_seed'] == 202609211855
    assert len(signs['checks']) == 3
    assert len(histories['rows']) == len(ownh['rows']) == 960
    assert histories['times'] == ownh['times'] and histories['metric_order'] == ownh['metrics']
    original_h = {(r['N'], r['kind'], r['replicate']): r for r in histories['rows']}
    herrors = []
    for row in ownh['rows']:
        key = row['N'], row['kind'], row['replicate']
        target = original_h[key]
        for name in ['seed', 'attempts', 'accepted', 'color_changes', 'wall_seconds']:
            assert row[name] == target[name]
        herrors.append(numeric_error(row['by_time_mode_metric'], target['by_time_mode_metric']))
    original_cells = {(r['N'], r['kind']): r for r in original['cells']}
    assert set(original_cells) == {(n, k) for n in [16, 32, 64, 128] for k in ['winding', 'irregular']}
    aggregates = []
    for row in owna['cells']:
        target = original_cells[row['N'], row['kind']]
        assert all(row[n] == target[n] for n in ['histories', 'times', 'metrics'])
        errs = {}
        for family in ['by_mode', 'mode_average', 'normalized_component_variances', 'attempts', 'accepted', 'color_changes', 'wall_seconds']:
            errs[family] = {stat: numeric_error(row[family][stat], target[family][stat]) for stat in ['mean', 'standard_error']}
        aggregates.append({'N': row['N'], 'kind': row['kind'], 'comparison': errs})
    expected = [[0, math.cos(4 * math.pi * t / 7), math.sin(4 * math.pi * t / 7), 1] for t in ownh['times']]
    numeric_error(expected, original['expected_mode_average'])
    assert authentication['authenticated_history_files'] == len(ownauth['history_payloads']) == 3840
    assert authentication['authenticated_history_bytes'] == ownauth['authenticated_payload_bytes']
    assert {r['receipt']['sha256'] for r in authentication['history_receipts']} == {r['sha256'] for r in ownauth['history_receipts']}
    for name in ['manifest', 'dispatch', 'summary']:
        verify(authentication[name])

    # Only the independently preselected eight intervals are computed. RNG
    # weights are advanced through all original cells to preserve the seed law.
    sel = json.loads((OUT / 'QUANTILE_SELECTION.json').read_text())
    selected = {tuple(k) for k in sel['selected_cells']}
    rng = np.random.default_rng(sel['seed']); quantiles = []
    for key in sorted(original_cells):
        rows = [r for r in ownh['rows'] if (r['N'], r['kind']) == key]
        count = len(rows)
        vals = np.asarray([r['by_time_mode_metric'] for r in rows])
        indices = sel['selected_time_metric_indices']
        if key in selected:
            data = np.asarray([[math.fsum(vals[h, ti, :, mi]) / 3 for ti, mi in indices] for h in range(count)])
            samples = []
        for first in range(0, sel['draws'], 500):
            weights = rng.multinomial(count, np.ones(count) / count, size=min(500, sel['draws'] - first))
            assert np.all(weights.sum(axis=1) == count)
            if key in selected:
                samples.append(weights @ data / count)
        if key in selected:
            ordered = np.sort(np.vstack(samples), axis=0)
            for j, (ti, mi) in enumerate(indices):
                lohi = []
                for prob in sel['probabilities']:
                    position = prob * (sel['draws'] - 1)
                    lower = int(math.floor(position)); frac = position - lower
                    lohi.append(float((1 - frac) * ordered[lower, j] + frac * ordered[lower + 1, j]))
                target = original_cells[key]['mode_average']
                expected_interval = [target['bootstrap95_low'][ti][mi], target['bootstrap95_high'][ti][mi]]
                err = numeric_error(lohi, expected_interval)
                quantiles.append({'N': key[0], 'kind': key[1], 'time': ownh['times'][ti],
                                  'metric': ownh['metrics'][mi], 'manual_interval': lohi,
                                  'saved_interval': expected_interval, 'comparison': err})

    # The already sealed independent symbolic function supplies the finite-k
    # matrix. Original observation times are now substituted without fitting.
    independent = runpy.run_path(str(OUT / 'independent_projection.py'))
    symbol = independent['symbol']; moment = independent['moment_matrix']
    theory_predictions = {}; theory_errors = []
    assert len(theory['local_projection']) == 3
    for row in theory['local_projection']:
        assert row['contexts'] == 14 ** 4 and row['all_four_conditional_coefficients_exact']
        assert row['actual_rate_denominator'] == 40 and row['context_coefficient'] == 'T_delta/56 = A_delta/4'
    T = sp.Matrix(moment([0, 0, 1]).astype(int).tolist())
    for row in theory['closure_control']:
        gamma = row['gamma']
        R = sp.zeros(6) if gamma == 0 else sp.diag(sp.Rational(11, 98), sp.Rational(11, 98), sp.Rational(2, 49), *[sp.Rational(15, 196)] * 3)
        B = -sp.Rational(11, 10) * sp.eye(6) + sp.I * sp.Rational(gamma, 7) * T
        assert row['exact_memory_curvature_matrix'] == str(R)
        assert row['exact_memory_trace'] == str(sp.trace(R))
        assert row['exact_first_derivative'] == str(B)
        assert row['states'] == 14 ** 4 and row['cycle_positions'] == 4
        assert row['exact_initial_covariance_identity'] and row['exact_second_derivative_identity']
    for row in theory['predictions']:
        N = row['N']
        if N == 256:
            continue  # The file contains theoretical predictions, no N256 data.
        assert N in [16, 32, 64, 128]
        axis = row['axis']; unit = np.eye(3)[axis]; Q = 2 * np.pi * unit
        B, d, qe = symbol(Q / N, 1.1, 1)
        PL = np.kron(np.eye(2), np.outer(unit, unit)); PT = np.eye(6) - PL
        D = -1j * moment(unit)
        values = []
        for t in row['times']:
            U = expm(-2j / 7 * moment(Q) * t); C = expm(N * t * B)
            values.append([2 - np.trace(U.conj().T @ C).real / 3,
                           np.trace(PT @ C).real / 4,
                           np.trace(D.conj().T @ C).real / 4,
                           np.trace(PL @ C).real / 2])
        assert row['times'] == ownh['times']
        numeric_error(d, row['microscopic_damping']); numeric_error(qe, row['effective_wavevector'])
        err = numeric_error(values, row['projected_benchmark'])
        theory_predictions[N, axis] = np.asarray(values)
        theory_errors.append({'N': N, 'axis': axis, 'comparison': err})
    assert len(theory_errors) == 12
    assert len(comparison['by_axis']) == 12 and len(comparison['mode_average']) == 4
    comparison_errors = []
    plot_outside_limits = []
    for row in comparison['by_axis']:
        N, axis = row['N'], row['axis']; target = original_cells[N, 'winding']
        pred = theory_predictions[N, axis]
        mean = np.asarray(target['by_mode']['mean'])[:, axis]
        se = np.asarray(target['by_mode']['standard_error'])[:, axis]
        errs = [numeric_error(row['projected_benchmark'], pred), numeric_error(row['observed_mean'], mean),
                numeric_error(row['observed_standard_error'], se), numeric_error(row['difference'], mean - pred)]
        comparison_errors.append({'N': N, 'axis': axis, 'comparisons': errs})
        for metric, limits in [(0, (-.08, 2.3)), (2, (-.15, 1.18))]:
            for ti in range(5):
                if mean[ti, metric] - se[ti, metric] < limits[0] or mean[ti, metric] + se[ti, metric] > limits[1]:
                    plot_outside_limits.append({'N': N, 'axis': axis, 'time_index': ti, 'metric': metric})
    for row in comparison['mode_average']:
        N = row['N']; target = original_cells[N, 'winding']
        pred = np.mean([theory_predictions[N, axis] for axis in range(3)], axis=0)
        assert row['observed'] == target['mode_average']
        numeric_error(row['projected_benchmark'], pred)
        numeric_error(row['difference'], np.asarray(target['mode_average']['mean']) - pred)
    result = {'created_utc': datetime.now(timezone.utc).isoformat(), 'primary_evidence': sources,
              'external_original_analysis_copies': external_bindings,
              'history_statistic_values_compared': sum(r['entries'] for r in herrors),
              'maximum_history_absolute_error': max(r['absolute_error'] for r in herrors),
              'aggregate_comparisons': aggregates,
              'selected_manual_bootstrap_quantiles': quantiles,
              'theory_comparison': theory_errors, 'by_axis_comparison': comparison_errors,
              'plot_points_or_one_SE_bars_outside_display_limits': plot_outside_limits,
              'all_author_authentication_counts_match_independent_authentication': True,
              'no_author_observable_function_imported': True, 'no_dynamics_replay': True,
              'N256_observables_accessed': False,
              'limits': 'Bootstrap check covers the preselected eight pointwise intervals, not all intervals or simultaneous coverage. No finite-time closure accuracy or phase conclusion inferred.'}
    (OUT / 'POST_COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'history_values': result['history_statistic_values_compared'],
                      'max_history_absolute_error': result['maximum_history_absolute_error'],
                      'cells': len(aggregates), 'selected_intervals': len(quantiles),
                      'theory_axis_cases': len(theory_errors), 'plot_clipping': plot_outside_limits}))


if __name__ == '__main__':
    main()

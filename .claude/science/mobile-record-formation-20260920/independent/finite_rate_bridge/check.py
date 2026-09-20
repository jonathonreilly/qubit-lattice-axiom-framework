#!/usr/bin/env python3
"""Exact independent checks of the finite-epsilon pre-birth TV bound.

All matrices and test distributions are specified locally. No primary campaign
calculation is read or imported. Inequalities are checked after squaring their
nonnegative sides, using rational arithmetic.
"""
from pathlib import Path
import hashlib
import json
import platform
import subprocess

import sympy as sp

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
S = sp.Rational


def exact(x):
    return sp.cancel(x)


def norm_squared(x, pi):
    return exact(sum(pi[i] * x[i]**2 for i in range(len(pi))))


def test_model(name, Q, pi, B, entrances):
    n = Q.rows
    one = sp.ones(n, 1)
    pi_row = sp.Matrix([pi])
    Dpi, DB = sp.diag(*pi), sp.diag(*B)
    assert Q * one == sp.zeros(n, 1)
    assert pi_row * Q == sp.zeros(1, n)
    assert Dpi * Q == Q.T * Dpi
    assert all(Q[i, j] >= 0 for i in range(n) for j in range(n) if i != j)
    eigenvalues = (-Q).eigenvals()
    assert eigenvalues[sp.Integer(0)] == 1
    gap = min(v for v in eigenvalues if v > 0)
    mu = exact((pi_row * sp.Matrix(B))[0])
    bmin, bmax = min(B), max(B)
    sigma2 = exact(sum(pi[i] * (B[i] - mu)**2 for i in range(n)))
    palm = [exact(pi[i] * B[i] / mu) for i in range(n)]
    R = DB.inv() * Q
    assert sp.diag(*palm) * R == R.T * sp.diag(*palm)
    assert sp.Matrix([palm]) * R == sp.zeros(1, n)
    P = sp.eye(n) - one * pi_row
    b = sp.Matrix(B) - mu * one
    T = P * DB * P - b * b.T * Dpi / mu
    L = -Q
    noncommuting = L * T != T * L
    output = []
    for entrance_name, alpha in entrances.items():
        assert sum(alpha) == 1 and min(alpha) >= 0
        alpha_row = sp.Matrix([alpha])
        f = sp.Matrix([exact(alpha[i] / pi[i]) for i in range(n)])
        g = f - sp.Matrix(B) / mu
        g2 = norm_squared(g, pi)
        chi_pi = norm_squared(f - one, pi)
        cov_f_b = exact(sum(pi[i] * (f[i] - 1) * (B[i] - mu) for i in range(n)))
        assert g2 == chi_pi + sigma2 / mu**2 - 2 * cov_f_b / mu
        chi_palm = exact(sum((alpha[i] - palm[i])**2 / palm[i] for i in range(n)))
        assert chi_palm == exact(mu * sum(pi[i] * g[i]**2 / B[i] for i in range(n)))
        for eps in (S(1, 1000), S(1, 100), S(1, 10), S(1), S(10), S(100)):
            occupation = eps * alpha_row * (eps * DB - Q).inv()
            nu = occupation * DB
            time_changed = eps * alpha_row * (eps * sp.eye(n) - R).inv()
            assert nu == time_changed
            assert sum(nu) == 1 and min(nu) >= 0
            h = sp.Matrix([exact(occupation[i] / pi[i] - 1 / mu) for i in range(n)])
            u = P * h
            assert (L + eps * DB) * h == eps * g
            assert (pi_row * DB * h)[0] == 0
            assert (L + eps * T) * u == eps * g
            assert h == u - one * (pi_row * DB * u)[0] / mu
            tu = exact((u.T * Dpi * T * u)[0])
            u2 = norm_squared(u, pi)
            assert bmin * u2 <= tu <= bmax * u2
            assert tu == exact((h.T * Dpi * DB * h)[0])
            tv = exact(sum(abs(nu[i] - palm[i]) for i in range(n)) / 2)
            bound1_squared = exact(eps**2 * mu * bmax * g2 / (4 * (gap + eps * bmin)**2))
            bound2_squared = exact(eps**2 * chi_palm / (4 * (eps + gap / bmax)**2))
            assert tv**2 <= bound1_squared
            assert tv**2 <= bound2_squared
            if entrance_name == 'event_stationary':
                assert tv == bound1_squared == bound2_squared == 0
            if name == 'constant_hazard_symmetric_two_state':
                assert tv**2 == bound1_squared
            output.append({
                'entrance': entrance_name, 'epsilon': str(eps),
                'TV_exact': str(tv), 'TV_decimal': float(tv),
                'main_bound_squared': str(bound1_squared),
                'main_bound_decimal_capped_at_one': min(1.0, float(sp.sqrt(bound1_squared))),
                'clock_bound_squared': str(bound2_squared),
                'clock_bound_decimal_capped_at_one': min(1.0, float(sp.sqrt(bound2_squared))),
                'entrance_chi2_from_pi': str(chi_pi),
                'mismatch_norm_squared': str(g2),
                'mean_pi_h': str(exact((pi_row * h)[0])),
            })
    return {'name': name, 'Q': str(Q), 'pi': [str(x) for x in pi],
            'B': [str(x) for x in B], 'motion_eigenvalues': {str(k): v for k, v in eigenvalues.items()},
            'gap': str(gap), 'mean_hazard': str(mu), 'hazard_variance': str(sigma2),
            'event_stationary': [str(x) for x in palm],
            'L_T_noncommuting': noncommuting, 'rows': output}


q2 = sp.Matrix([[-2, 2], [3, -3]])
p2, b2 = [S(3, 5), S(2, 5)], [S(1), S(4)]
e2 = {'point_0': [S(1), S(0)], 'point_1': [S(0), S(1)],
      'motion_stationary': p2, 'event_stationary': [S(3, 11), S(8, 11)],
      'uniform': [S(1, 2), S(1, 2)]}
q3 = sp.Matrix([[-1, 1, 0], [1, -2, 1], [0, 1, -1]])
p3, b3 = [S(1, 3)] * 3, [S(1), S(2), S(5)]
e3 = {'point_0': [S(1), S(0), S(0)], 'point_1': [S(0), S(1), S(0)],
      'point_2': [S(0), S(0), S(1)], 'motion_stationary': p3,
      'event_stationary': [S(1, 8), S(1, 4), S(5, 8)],
      'skew': [S(1, 2), S(1, 3), S(1, 6)]}
qflat = sp.Matrix([[-1, 1], [1, -1]])
pflat, bflat = [S(1, 2)] * 2, [S(3)] * 2
eflat = {'point_0': [S(1), S(0)], 'point_1': [S(0), S(1)],
         'motion_stationary': pflat, 'event_stationary': pflat}
models = [test_model('asymmetric_two_state', q2, p2, b2, e2),
          test_model('noncommuting_three_state', q3, p3, b3, e3),
          test_model('constant_hazard_symmetric_two_state', qflat, pflat, bflat, eflat)]
assert models[1]['L_T_noncommuting']

# A symbolic check for every positive epsilon and every two-state entrance.
eps = sp.Symbol('epsilon', positive=True)
a = sp.Symbol('alpha0', real=True)
alpha = sp.Matrix([[a, 1-a]])
palm2 = sp.Matrix([[S(3, 11), S(8, 11)]])
nu = eps * alpha * (eps * sp.diag(*b2) - q2).inv() * sp.diag(*b2)
assert all(sp.cancel(x) == 0 for x in nu - palm2 - eps / (eps + S(11, 4)) * (alpha - palm2))
tv_squared = eps**2 / (eps + S(11, 4))**2 * (a - S(3, 11))**2
bound_squared = S(55, 6) * eps**2 / (eps + 5)**2 * (a - S(3, 11))**2
gap_polynomial = 784*eps**2 + 3880*eps + 4255
expected_gap = eps**2 * (a-S(3, 11))**2 * gap_polynomial / (6*(eps+5)**2*(4*eps+11)**2)
assert sp.cancel(bound_squared - tv_squared - expected_gap) == 0
assert all(c > 0 for c in sp.Poly(gap_polynomial, eps).all_coeffs())

# Omitting hazard mismatch falsely predicts zero error from stationary entry.
wrong_bound_case = next(row for row in models[0]['rows']
                        if row['entrance'] == 'motion_stationary' and row['epsilon'] == '1')
assert S(wrong_bound_case['entrance_chi2_from_pi']) == 0
assert S(wrong_bound_case['TV_exact']) > 0

summary = {'models': models, 'exact_test_cases': sum(len(m['rows']) for m in models),
           'symbolic_two_state_TV': 'abs(alpha0-3/11) * epsilon/(epsilon+11/4)',
           'symbolic_two_state_bound_squared_minus_TV_squared': str(sp.factor(expected_gap)),
           'wrong_entrance_only_bound_rejected': wrong_bound_case,
           'constant_hazard_control': 'main bound is exact for every tested symmetric two-state entrance and epsilon; stationary error is exactly zero',
           'scope': 'finite reversible motion class, fixed positive hazard; no primary calculation imported'}
(OUT/'RESULTS.json').write_text(json.dumps(summary, indent=2)+'\n')
sha = lambda data: hashlib.sha256(data).hexdigest()
git = lambda *args: subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()
source_paths = [OUT/'DERIVATION.md', Path(__file__).resolve(), OUT.parent/'REPORT.md',
                OUT.parent/'INITIAL_SEAL.json', ROOT/'docs/ai_methodology/SCIENCE_WORKFLOW.md']
manifest = {'head': git('rev-parse','HEAD'), 'planning_ref': git('rev-parse','origin/ai/execution'),
            'sha256': {str(p): sha(p.read_bytes()) for p in source_paths},
            'python': platform.python_version(), 'sympy': sp.__version__,
            'primary_new_calculations_read': False}
(OUT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
brief = {'exact_test_cases': summary['exact_test_cases'],
         'selected_rows': {m['name']: [row for row in m['rows'] if row['epsilon']=='1' and row['entrance'] in ('motion_stationary','point_0','event_stationary')] for m in models},
         'symbolic_two_state_TV': summary['symbolic_two_state_TV'],
         'symbolic_gap': summary['symbolic_two_state_bound_squared_minus_TV_squared'],
         'all_exact_inequalities_satisfied': True,
         'three_state_noncommutation_confirmed': models[1]['L_T_noncommuting']}
print(json.dumps(brief,indent=2))

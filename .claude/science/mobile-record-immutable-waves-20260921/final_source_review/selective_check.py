#!/usr/bin/env python3
"""Independent finite checks of the publication's changed proof route.

No production function is imported. Writes only RESULTS.json beside this file.
Finite checks do not prove an asymptotic limit.
"""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
import platform

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = HERE.parent
vectors = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0),
           (0, -1, 0), (0, 0, 1), (0, 0, -1))
f = tuple(v[0] for v in vectors)
feature = tuple(2 * int(a != 0) - 3 * f[a] ** 2 for a in range(7))
checks = []


def checked(name, condition, details=None):
    if not condition:
        raise AssertionError((name, details))
    checks.append(dict(name=name, passed=True, details=details))


def drive2(word, omit_cross=False):
    l, a, b, r = word
    ans = (f[a] - f[b]) * (feature[l] + feature[r])
    if not omit_cross:
        ans += (feature[a] - feature[b]) * (f[l] + f[r])
    return ans


def rates(state):
    return [F(1 + max(10 * drive2(tuple(state[(x+d) % 4]
                    for d in (-1, 0, 1, 2))), 0), 20) for x in range(4)]


def moved(state, x):
    new = list(state)
    new[x], new[(x+1) % 4] = new[(x+1) % 4], new[x]
    return tuple(new)


# A complete four-cycle retains distinct footprint sites. Test the adjoint
# used in the publication, with genuinely inhomogeneous full-support marginals.
weights = [[1 + (3*x + 2*a + a*x) % 11 for a in range(7)] for x in range(4)]
prob = [[F(a, sum(row)) for a in row] for row in weights]
beta = F(2, 7)
bad_cross = None
max_adjoint = max_birth = F(0)
nonzero_adjoint = 0
for state in product(range(7), repeat=4):
    outgoing = rates(state)
    adjoint = expanded = F(0)
    for x in range(4):
        y = (x+1) % 4
        reverse = rates(moved(state, x))[x]
        ratio = prob[x][state[y]] * prob[y][state[x]] / (prob[x][state[x]] * prob[y][state[y]])
        adjoint += reverse * ratio - outgoing[x]
        expanded += reverse * (ratio - 1)
    max_adjoint = max(max_adjoint, abs(adjoint - expanded))
    nonzero_adjoint += int(adjoint != 0)
    # Independent incoming-birth construction versus reference-product score.
    birth_adjoint = sum(beta * prob[x][0] / prob[x][a] if a else -6*beta
                        for x, a in enumerate(state))
    derivatives = [[-6*beta*row[0]] + [beta*row[0]]*6 for row in prob]
    score = sum(derivatives[x][a] / prob[x][a] for x, a in enumerate(state))
    max_birth = max(max_birth, abs(birth_adjoint - score))
    if bad_cross is None:
        defect = sum(drive2(tuple(state[(x+d) % 4] for d in (-1, 0, 1, 2)),
                                  omit_cross=True) for x in range(4))
        if defect:
            bad_cross = dict(state=state, sum_h=F(defect, 2))
checked('complete_cycle_adjoint_identity', max_adjoint == 0 and nonzero_adjoint > 0,
        dict(states=7**4, max_exact_residual=str(max_adjoint), nonzero_adjoint_states=nonzero_adjoint))
checked('complete_cycle_birth_reference_cancellation', max_birth == 0,
        dict(states=7**4, max_exact_residual=str(max_birth)))
checked('omitted_cross_term_has_pointwise_balance_counterexample', bad_cross is not None,
        {k: str(v) for k, v in bad_cross.items()})

# Actual, nonreversible 24-state generator: test inverse-form normalization
# and its additive-functional inequality, not only a symmetric template.
states = sorted(set(permutations((0, 1, 3, 4))))
index = {state: i for i, state in enumerate(states)}
size = len(states)
Q = sp.zeros(size)
currents = []
for state in states:
    c = rates(state)
    currents.append(c[0] * (int(state[0] == 1) - int(state[1] == 1)))
    for x, rate in enumerate(c):
        i, j = index[state], index[moved(state, x)]
        if i != j:
            Q[i, j] += sp.Rational(rate.numerator, rate.denominator)
            Q[i, i] -= sp.Rational(rate.numerator, rate.denominator)
checked('complete_sector_stationary_and_nonreversible',
        Q * sp.ones(size, 1) == sp.zeros(size, 1)
        and sp.ones(1, size) * Q == sp.zeros(1, size) and Q != Q.T,
        dict(states=size))
current = sp.Matrix(currents)
mean = sum(current) / size
centered = current - sp.ones(size, 1) * mean
S = (Q + Q.T) / 2
projection = sp.ones(size) / size
u = (-S + projection).inv() * centered
norm = (centered.T * u)[0] / size
checked('inverse_form_identity', -S*u == centered and sum(u) == 0
        and norm == -(u.T*S*u)[0] / size and norm > 0,
        dict(inverse_form=str(norm), canonical_current_mean=str(mean)))
qn = np.array(Q, dtype=float)
fn = np.array(centered, dtype=float).reshape(-1)
N, t = 4, 2/7
accelerated = N * qn
project = np.ones((size, size)) / size
v = np.linalg.solve(accelerated + project, fn)
w = np.linalg.solve(accelerated + project, v)
integrated = (expm(t*accelerated) - np.eye(size) - t*accelerated) @ w
variance = float(2 * fn @ integrated / size)
bound = float(2*t/N*float(norm))
checked('nonreversible_additive_function_bound_at_finite_time',
        0 <= variance <= bound * (1 + 1e-11),
        dict(N=N, t=t, exact_generator_variance_numeric=variance,
             bound=bound, ratio=variance/bound, tolerance=1e-11))

# Metadata claim requires a nonzero drive: alpha=0 remains an allowed
# positive-floor process but gives zero current and six zero Euler speeds.
rho, alpha, kx, ky, kz = sp.symbols('rho alpha kx ky kz')
matrix = sp.zeros(6)
for i, wave in enumerate((kx, ky, kz)):
    matrix[0, i+1] = 2*alpha*rho*(1-rho)*wave
    matrix[i+1, 0] = 2*alpha*rho*wave/3
checked('zero_alpha_counterexample_to_unqualified_nonzero_pair',
        matrix.subs(alpha, 0) == sp.zeros(6),
        dict(alpha=0, allowed_positive_floor='kappa0=1', rank=0,
             correction='Qualify the nonzero pair by alpha != 0.'))

# Authenticate and inspect cached execution coverage. No repeated baseline or
# seven repeated full runs are used as evidence for the limiting proofs.
runner = ROOT / 'scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py'
note = ROOT / 'docs/MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md'
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
author = json.loads((BASE / 'AUTHOR_RUNS.json').read_text())
checked('cached_author_source_identity',
        author['identities'][str(runner.relative_to(ROOT))] == sha(runner)
        and author['identities'][str(note.relative_to(ROOT))] == sha(note))
expected = {'wrong_axis_feature': 'all_density_all_direction_field_matrix',
            'drop_polarized_cross_term': 'FAIL:',
            'omit_current_mean_subtraction': 'product_current_case_3_axis_0_minimal',
            'wrong_acoustic_dimension': 'all_density_all_direction_field_matrix',
            'discard_zero_modes': 'all_direction_acoustic_polynomial',
            'reverse_fourier_sign': 'exact_configuration_fourier_drift_sign',
            'fast_birth_scaling': 'slow_birth_generator_scaling'}
coverage = []
for record in author['runs']:
    mutation = record['mutation']
    if mutation is None:
        checked('cached_baseline_execution_identity', record['returncode'] == 0
                and 'TOTAL: PASS=49 FAIL=0' in record['stdout'] and not record['stderr'])
        continue
    fail = next(line for line in record['stdout'].splitlines() if line.startswith('FAIL:'))
    checked('cached_mutation_' + mutation,
            record['returncode'] == 1 and expected[mutation] in fail and not record['stderr'])
    coverage.append(dict(mutation=mutation, failure=fail))
checked('all_declared_mutation_records_present', {x['mutation'] for x in coverage} == set(expected))

result = dict(scope='Selective independent finite evidence; no audit or asymptotic proof by enumeration.',
              environment=dict(python=platform.python_version(), numpy=np.__version__,
                               scipy=scipy.__version__, sympy=sp.__version__),
              count=len(checks), checks=checks, mutation_cache=coverage,
              source_sha256={str(x.relative_to(ROOT)): sha(x) for x in (note, runner)})
text = json.dumps(result, indent=2) + '\n'
(HERE / 'RESULTS.json').write_text(text)
print(text, end='')

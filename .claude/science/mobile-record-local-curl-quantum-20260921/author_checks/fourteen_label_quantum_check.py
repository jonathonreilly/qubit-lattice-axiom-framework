#!/usr/bin/env python3
"""Exact kernel controls and unrestricted POVM fits for fourteen Bloch rays.

The numerical POVM problem does not impose covariance. The input encoding
is fixed for those fits; the rank obstruction itself allows any encoding.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import numpy as np
import sympy as s
import cvxpy as cp

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition, detail=None):
    assert bool(condition), (name, detail)
    checks.append(dict(name=name, passed=True, detail=detail))
    print('PASS:', name, flush=True)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


unit = [s.eye(3)[:, i] for i in range(3)]
zero = s.zeros(3, 1)
features = [(sign*unit[i], zero) for i in range(3) for sign in (-1, 1)]
features += [(zero, s.Matrix(signs)) for signs in product((-1, 1), repeat=3)]
F = s.Matrix([[*list(e), *list(b/2)] for e, b in features])
T = F*F.T
one = s.ones(14, 1)
check('rank_six_feature_Gram_and_orthogonality', F.T*F == 2*s.eye(6) and F.T*one == s.zeros(6, 1) and T.rank() == 6)
j = s.symbols('j', real=True)
P = (s.ones(14)+j*T)/14
check('full_kernel_eigenspaces', P*one == one and clean(P*F-j*F/7) == s.zeros(14, 6)
      and P.subs(j, s.Rational(1, 2)).rank() == 7 and P.subs(j, -s.Rational(1, 2)).rank() == 7)
check('every_parent_column_is_distinct_for_nonzero_coupling',
      all(T[:, a] != T[:, b] for a in range(14) for b in range(a)))
clock = s.diag(*[s.Rational(a+1, 15) for a in range(14)])
check('positive_content_clock_preserves_rank', (P.subs(j, s.Rational(1, 2))*clock).rank() == 7)

sigma = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]


def spin(v):
    return sum((v[i]*sigma[i] for i in range(3)), s.zeros(2))


rays = [e if a < 6 else b/s.sqrt(3) for a, (e, b) in enumerate(features)]
states = [(s.eye(2)+spin(v))/2 for v in rays]
w = j*(2-s.sqrt(3))/56
effects = [s.eye(2)/14 if a < 6 else s.eye(2)/14+w*spin(b)
           for a, (e, b) in enumerate(features)]
check('natural_encoding_witness_complete', clean(sum(effects, s.zeros(2))-s.eye(2)) == s.zeros(2))
Q = s.Matrix(14, 14, lambda a, b: s.simplify(s.trace(effects[a]*states[b])))
tv = []
for b in range(14):
    tv.append(s.simplify(sum(s.Abs((P-Q)[a, b].subs(j, s.Rational(1, 2))) for a in range(14))/2))
check('all_fourteen_witness_column_total_variations', all(s.simplify(q-(3-s.sqrt(3))/28) == 0 for q in tv))
u, z = s.symbols('u z', nonnegative=True)
weight_a = s.sqrt(3)/(s.sqrt(3)+2)
weight_b = 2/(s.sqrt(3)+2)
average = weight_a*(j/14-u+4*z)+weight_b*(s.sqrt(3)*u+3*j/28-2*s.sqrt(3)*z)
check('reduced_minimax_dual_bound', s.simplify(average-j*(3-s.sqrt(3))/14-weight_a*u) == 0
      and s.simplify(weight_a+weight_b) == 1)

# Six off-diagonal Gell-Mann matrices, with exact Hilbert-Schmidt norms.
G = []
for a, b in ((0, 1), (0, 2), (1, 2)):
    real = s.zeros(3); real[a, b] = real[b, a] = 1
    imag = s.zeros(3); imag[a, b] = -s.I; imag[b, a] = s.I
    G.extend([real, imag])
check('qutrit_operator_basis', all(s.trace(G[a]*G[b]) == 2*int(a == b) for a in range(6) for b in range(6)))
operator = [sum((F[a, r]*G[r] for r in range(6)), s.zeros(3)) for a in range(14)]
qutrit_states = [s.eye(3)/3+g/(3*s.sqrt(2)) for g in operator]
qutrit_effects = [s.eye(3)/14+3*s.sqrt(2)*j*g/28 for g in operator]
qutrit_Q = s.Matrix(14, 14, lambda a, b: s.simplify(s.trace(qutrit_effects[a]*qutrit_states[b])))
check('qutrit_all_196_exact_probabilities', clean(qutrit_Q-P) == s.zeros(14))
check('qutrit_completeness_and_state_traces',
      clean(sum(qutrit_effects, s.zeros(3))-s.eye(3)) == s.zeros(3)
      and all(s.trace(rho) == 1 for rho in qutrit_states))

four_states = []
four_effects = []
for a, (e, b) in enumerate(features):
    if a < 6:
        four_states.append(s.diag((s.eye(2)+spin(e))/2, s.zeros(2)))
        four_effects.append(s.diag((s.eye(2)+j*spin(e))/14, s.eye(2)/14))
    else:
        four_states.append(s.diag(s.zeros(2), (s.eye(2)+spin(b)/s.sqrt(3))/2))
        four_effects.append(s.diag(s.eye(2)/14, (s.eye(2)+j*s.sqrt(3)*spin(b)/4)/14))
four_Q = s.Matrix(14, 14, lambda a, b: s.simplify(s.trace(four_effects[a]*four_states[b])))
check('four_dimensional_all_196_exact_probabilities', clean(four_Q-P) == s.zeros(14)
      and clean(sum(four_effects, s.zeros(4))-s.eye(4)) == s.zeros(4))

minimum = 1.0
for js in (-s.Rational(1, 3), 0, s.Rational(1, 3)):
    for mat in qutrit_states+qutrit_effects:
        minimum = min(minimum, float(np.linalg.eigvalsh(np.array(mat.subs(j, js)).astype(complex)).min()))
for js in (-1, -s.Rational(1, 2), 0, s.Rational(1, 2), 1):
    for mat in four_states+four_effects+effects:
        minimum = min(minimum, float(np.linalg.eigvalsh(np.array(mat.subs(j, js)).astype(complex)).min()))
check('positive_carrier_and_witness_endpoint_controls', minimum >= -2e-14, dict(minimum_eigenvalue=minimum))

# An arbitrary qubit effect is alpha*I + vector.sigma. The SOC is its full
# positivity condition; no cubic averaging or orbit ansatz enters this fit.
rays_array = np.array(rays, dtype=float).reshape(14, 3)
T_array = np.array(T, dtype=float)
alpha = cp.Variable(14)
vectors = cp.Variable((14, 3))
delta = cp.Variable(nonneg=True)
target = cp.Parameter((14, 14))
predicted = cp.reshape(alpha, (14, 1), order='C') + vectors@rays_array.T
constraints = [cp.sum(alpha) == 1, cp.sum(vectors, axis=0) == 0,
               cp.norm(vectors, axis=1) <= alpha]
constraints += [cp.norm1(predicted[:, b]-target[:, b])/2 <= delta for b in range(14)]
problem = cp.Problem(cp.Minimize(delta), constraints)
fits = []
for js in (-.99, -.75, -.5, -.1, 0, .1, .5, .75, .99):
    target.value = (np.ones((14, 14))+js*T_array)/14
    problem.solve(solver='CLARABEL', tol_gap_abs=1e-10, tol_feas=1e-10,
                  tol_gap_rel=1e-10, max_iter=300)
    reference = abs(js)*(3-np.sqrt(3))/14
    probabilities = alpha.value[:, None]+vectors.value@rays_array.T
    primal = float(max(np.sum(np.abs(probabilities-target.value), axis=0))/2)
    feasibility = max(abs(np.sum(alpha.value)-1), np.max(abs(np.sum(vectors.value, axis=0))),
                      np.max(np.linalg.norm(vectors.value, axis=1)-alpha.value), 0)
    discrepancy = abs(float(problem.value)-reference)
    fit = dict(j=js, status=problem.status, objective=float(problem.value), reference=reference,
               discrepancy=discrepancy, largest_actual_TV=primal, feasibility_residual=float(feasibility))
    fits.append(fit)
    assert problem.status == 'optimal', fit
    assert discrepancy < 2e-8 and abs(primal-reference) < 2e-8 and feasibility < 2e-9, fit
check('nine_unrestricted_qubit_POVM_optimizations', True,
      dict(maximum_objective_discrepancy=max(row['discrepancy'] for row in fits)))

report = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), checks=checks,
              fits=fits, versions=dict(numpy=np.__version__, sympy=s.__version__, cvxpy=cp.__version__),
              scope='Primary exact finite kernel/carrier checks and floating-point unrestricted POVM optima for fixed natural inputs. No spatial carrier, physical quantum bridge or minimal carrier dimension above |j|=1/3 is certified.')
(HERE/'FOURTEEN_LABEL_QUANTUM_RESULTS.json').write_text(json.dumps(report, indent=2)+'\n')
print('TOTAL:', len(checks), 'PASS', flush=True)

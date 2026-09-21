"""Reconstruct the full-cubic, uniform-entropy principal-symbol family.

No stochastic trajectory, hydrodynamic limit, or empirical physics is tested.
Character counts and the Gram formula are exact. Group covariance and a
finite-difference current check are floating-point controls with stated bounds.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
labels = [("0", (0, 0, 0))]
labels += [("A", tuple(s if j == i else 0 for j in range(3)))
           for i in range(3) for s in (-1, 1)]
labels += [("B", v) for v in itertools.product((-1, 1), repeat=3)]
index = {v: i for i, v in enumerate(labels)}
group = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1, 1), repeat=3):
        Q = np.zeros((3, 3), dtype=int)
        for i in range(3):
            Q[i, perm[i]] = signs[i]
        det = int(round(np.linalg.det(Q)))
        mapping = [index[(t, tuple((det if t == "B" else 1) * Q @ v))]
                   for t, v in labels]
        P = np.zeros((15, 15), dtype=int)
        P[mapping, np.arange(15)] = 1
        group.append((Q, P, det))

def multiplicity(proper_only=False):
    numerator = 0
    count = 0
    for Q, P, det in group:
        if proper_only and det < 0:
            continue
        chi = int(np.trace(P)) - 1
        chi2 = int(np.trace(P @ P)) - 1
        numerator += int(np.trace(Q)) * (chi * chi + chi2)
        count += 1
    value = sp.Rational(numerator, 2 * count)
    assert value.q == 1
    return int(value)

D = [np.diag([1., -1., 0.]) / np.sqrt(2),
     np.diag([1., 1., -2.]) / np.sqrt(6)]
T = []
for i, j in ((0, 1), (0, 2), (1, 2)):
    M = np.zeros((3, 3))
    M[i, j] = M[j, i] = 1 / np.sqrt(2)
    T.append(M)
U = np.zeros((15, 14))
for row, (kind, raw) in enumerate(labels):
    w = np.asarray(raw)
    if kind == "A":
        U[row, :3] = w / np.sqrt(2)
        U[row, 3] = 4 / np.sqrt(168)
        U[row, 8:10] = [w @ d @ w / np.sqrt(2) for d in D]
    elif kind == "B":
        U[row, 3] = -3 / np.sqrt(168)
        U[row, 5:8] = w / np.sqrt(8)
        U[row, 10:13] = [w[0]*w[1], w[0]*w[2], w[1]*w[2]] / np.sqrt(8)
        U[row, 13] = np.prod(w) / np.sqrt(8)
    U[row, 4] = (14 if kind == "0" else -1) / np.sqrt(210)
assert np.max(np.abs(U.T @ U - np.eye(14))) < 1e-14
assert np.max(np.abs(U.sum(axis=0))) < 1e-14

def cross(q):
    x, y, z = q
    return np.array([[0., -z, y], [z, 0., -x], [-y, x, 0.]])

def symbol(q, coefficients):
    a1, a2, m, u, v = coefficients
    K = np.column_stack([a1*q, a2*q, m*cross(q),
                         *[u*d@q for d in D],
                         *[v*t@q for t in T], np.zeros(3)])
    A = np.zeros((14, 14))
    A[:3, 3:] = K
    A[3:, :3] = K.T
    return A

cov_error = 0.
families = []
for c in np.eye(5):
    families.append(np.concatenate([symbol(q, c).ravel() for q in np.eye(3)]))
    for Q, P, _ in group:
        R = U.T @ P @ U
        for q in np.eye(3):
            cov_error = max(cov_error, float(np.max(np.abs(
                R @ symbol(q, c) @ R.T - symbol(Q @ q, c)))))
assert cov_error < 1e-12
assert np.linalg.matrix_rank(np.asarray(families)) == 5
assert multiplicity() == 5

x, y, z, a1, a2, m, u, v = sp.symbols('x y z a1 a2 m u v', real=True)
q = sp.Matrix([x, y, z])
C = sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
Ds = [sp.diag(1, -1, 0)/sp.sqrt(2), sp.diag(1, 1, -2)/sp.sqrt(6)]
Ts = []
for i, j in ((0, 1), (0, 2), (1, 2)):
    t = sp.zeros(3)
    t[i, j] = t[j, i] = 1/sp.sqrt(2)
    Ts.append(t)
K = sp.Matrix.hstack(a1*q, a2*q, m*C,
                    *[u*d*q for d in Ds], *[v*t*q for t in Ts], sp.zeros(3, 1))
r2 = x*x+y*y+z*z
expected = ((m*m+v*v/2)*r2*sp.eye(3)
            +(a1*a1+a2*a2-m*m-u*u/3+v*v/2)*(q*q.T)
            +(u*u-v*v)*sp.diag(x*x, y*y, z*z))
assert (K*K.T-expected).applyfunc(sp.expand) == sp.zeros(3)
isotropic = expected.subs(v*v, u*u)
longitudinal = a1*a1+a2*a2+2*u*u/3
assert (isotropic*q-longitudinal*r2*q).applyfunc(sp.expand) == sp.zeros(3, 1)
transverse = m*m+u*u/2
test_transverse = sp.Matrix([-y, x, 0])
assert (isotropic*test_transverse-transverse*r2*test_transverse).applyfunc(sp.expand) == sp.zeros(3, 1)

maxwell = symbol(np.array([1., 2., 3.]), [0, 0, 2, 0, 0])
eigenvalues = np.linalg.eigvalsh(maxwell)
assert np.count_nonzero(abs(eigenvalues)<1e-10) == 10
assert np.allclose(eigenvalues[[0, 1, 12, 13]], [-2*np.sqrt(14)]*2+[2*np.sqrt(14)]*2)
generic = symbol(np.array([1., 2., 3.]), [1, 2, 3, 4, 5])
assert np.count_nonzero(abs(np.linalg.eigvalsh(generic))<1e-10) == 8

# Independent current derivative rather than differentiating the target A.
rng = np.random.default_rng(202609211054)
derivative_error = 0.
row_sum_error = 0.
for c in [*np.eye(5), np.array([1., -2., 3., -.5, 2.])]:
    for direction in np.eye(3):
        target = U @ symbol(direction, c) @ U.T
        S = 15/2*target
        row_sum_error = max(row_sum_error, float(np.max(abs(S.sum(axis=1)))))
        p0 = np.ones(15)/15
        def current(p):
            return 2*p*(S@p - p@S@p)
        w = U @ rng.normal(size=14)
        w /= np.linalg.norm(w)
        eps = 1e-5
        observed = (current(p0+eps*w)-current(p0-eps*w))/(2*eps)
        derivative_error = max(derivative_error, float(np.max(abs(observed-target@w))))
assert row_sum_error < 1e-12
assert derivative_error < 1e-7  # Central difference has a cubic-current O(eps^2) error.

# Pointwise stationarity residual, central swap antisymmetry, and covariance
# use arbitrary S from the entire family, not the curl subfamily alone.
residual = 0.
swap_error = 0.
for c in rng.normal(size=(6, 5)):
    for direction in np.eye(3):
        S = 15/2 * U @ symbol(direction, c) @ U.T
        word = rng.integers(0, 15, size=17)
        hs = []
        for n in range(len(word)):
            l, a, d, r = [word[k % len(word)] for k in (n-1, n, n+1, n+2)]
            h = S[l,a]+S[a,r]-S[l,d]-S[d,r]
            swapped = S[l,d]+S[d,r]-S[l,a]-S[a,r]
            hs.append(h)
            swap_error = max(swap_error, abs(h+swapped))
        residual = max(residual, abs(sum(hs)))
assert residual < 1e-12 and swap_error < 1e-12

result = {
    'status': 'author-checked finite classification; independent check pending',
    'full_cubic_group_order': 48,
    'full_cubic_symmetric_symbol_dimension_exact': multiplicity(),
    'proper_cubic_symmetric_symbol_dimension_exact': multiplicity(True),
    'explicit_family_dimension': 5,
    'group_covariance_max_abs_error': cov_error,
    'exact_gram_formula': 'verified by symbolic polynomial expansion',
    'maxwell_nonzero_modes': 4,
    'maxwell_zero_modes': 10,
    'generic_nonzero_modes': 6,
    'generic_zero_modes': 8,
    'microscopic_current_derivative_max_abs_error': derivative_error,
    'pair_tensor_row_sum_max_abs_error': row_sum_error,
    'telescoping_residual_max_abs_error': residual,
    'swap_antisymmetry_max_abs_error': swap_error,
    'limits': ['uniform full-support fifteen-state product',
               'full 48-element polar/axial cubic symmetry is added',
               'first-order principal symbol only',
               'no axiom selection, physical Maxwell identification or new limit theorem']
}
(HERE/'CUBIC_ENTROPY_SYMBOL_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

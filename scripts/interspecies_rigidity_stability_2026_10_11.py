#!/usr/bin/env python3
"""Exact finite controls for conditional six-anchor interspecies stability.

Uses SymPy and fixed rational/symbolic fixtures; no network or physical input.
The unchanged mathematical control body writes its finite dual certificates
only into a temporary directory. Historical full certificates are preserved
in the milestone evidence. These controls are author replay, not independent
continuum proof or scoped Lean verification. TOTAL counts nine control
families, not individual assertions or mathematical proof obligations.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/INTERSPECIES_RIGIDITY_STABILITY_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/INTERSPECIES_COLLISION_CURRENT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from itertools import combinations, permutations, product
from pathlib import Path
import json
import sympy as sp
import tempfile

_certificate_workspace = tempfile.TemporaryDirectory(prefix="toe-rigidity-control-")
HERE = Path(_certificate_workspace.name)
Q = sp.Rational
E1, E2, E3 = (sp.eye(3)[:, i] for i in range(3))
ZERO = sp.zeros(3, 1)


def norm2(v):
    return (v.T * v)[0]


def height2(z, a, b):
    return sp.cancel(norm2((z - a).cross(b - a)) / norm2(b - a))


def constant(D, sigma, h):
    rho, tau = D / sigma, D / h
    B0 = 3 + 8 * rho
    T = 2 * rho + 2 * tau * (1 + rho)
    Z = 6 * rho + 8 * rho**2
    W = 8 * rho**3 + 6 * rho**2 + 3 * rho
    R = max(T * (1 + Z * B0), W * B0)
    return T * (1 + R)


def wedge_bound(C, omega, sigma):
    return 2 * C * omega / sigma


def right_cross(d):
    return sp.Matrix([[0, d[2], -d[1]], [-d[2], 0, d[0]],
                      [d[1], -d[0], 0]])


def constraint_and_residual(X, Y):
    n = len(X) + len(Y)
    rows, edge_ids, omitted = [], [], []
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            d = x - y
            if d == ZERO:
                omitted.append([i, j])
                continue
            block = sp.zeros(3, 3 * n)
            block[:, 3*i:3*i+3] = right_cross(d)
            k = len(X) + j
            block[:, 3*k:3*k+3] = -right_cross(d)
            rows.append(block)
            edge_ids.extend([[i, j, axis] for axis in range(3)])
    W = sp.Matrix.vstack(*rows)
    d11 = X[0] - Y[0]
    lam = sp.zeros(1, 3 * n)
    lam[0, 0:3] = d11.T / norm2(d11)
    lam[0, 3*len(X):3*len(X)+3] = -d11.T / norm2(d11)
    pick0 = sp.zeros(3, 3 * n)
    pick0[:, 0:3] = sp.eye(3)
    b = pick0 - X[0] * lam
    residuals = []
    for i, z in enumerate(X + Y):
        pick = sp.zeros(3, 3 * n)
        pick[:, 3*i:3*i+3] = sp.eye(3)
        residuals.append(pick - z * lam - b)
    return W, sp.Matrix.vstack(*residuals), edge_ids, omitted


def finite_dual_certificate(name, X, Y, D, sigma, h, branch):
    M = sp.Matrix.hstack(X[1]-X[0], Y[1]-Y[0], Y[0]-X[0])
    assert M.det() != 0
    gram_gap = M.T*M - sigma**2*sp.eye(3)
    for size in (1, 2, 3):
        for ids in combinations(range(3), size):
            assert gram_gap.extract(ids, ids).det() >= 0
    assert max(norm2(a-b) for a in X+Y for b in X+Y) <= D**2
    assert height2(X[2], X[0], X[1]) >= h**2
    assert height2(Y[2], Y[0], Y[1]) >= h**2
    far = height2(Y[2], X[0], X[1]) >= sigma**2/16
    assert far == (branch == 'far')
    W, R, edge_ids, omitted = constraint_and_residual(X, Y)
    basis_rows = list(W.T.rref()[1])
    B = W[basis_rows, :]
    assert B.rows == R.cols - 4
    pivot_cols = list(B.rref()[1])
    coeff = R[:, pivot_cols] * B[:, pivot_cols].inv()
    assert coeff * B == R
    l1 = max(sum(abs(c) for c in coeff.row(i)) for i in range(coeff.rows))
    finite_normalized_bound = 2 * D * l1
    finite_wedge_bound = 2 * l1
    C = constant(D, sigma, h)
    assert finite_normalized_bound <= C
    assert finite_wedge_bound <= 2*C/sigma
    record = {
        'fixture': name, 'X': [list(map(str, x)) for x in X],
        'Y': [list(map(str, y)) for y in Y], 'D': str(D),
        'sigma': str(sigma), 'h': str(h), 'branch': branch,
        'unknowns': R.cols, 'constraint_rows': W.rows, 'rank': B.rows,
        'omitted_equal_edges': omitted, 'basis_row_indices': basis_rows,
        'basis_edge_components': [edge_ids[i] for i in basis_rows],
        'residual_dual_coefficients': [[str(t) for t in coeff.row(i)]
                                       for i in range(coeff.rows)],
        'max_dual_row_l1': str(l1),
        'finite_normalized_bound': str(finite_normalized_bound),
        'finite_wedge_bound': str(finite_wedge_bound), 'theorem_C': str(C),
        'identity_checked': 'R = coefficients * selected wedge rows, exactly',
    }
    (HERE / f'certificate_{name}.json').write_text(json.dumps(record, indent=2)+'\n')
    print(f'EXACT {name}: rank={B.rows}/{R.cols}, equal_edges={len(omitted)}, '
          f'dual_bound={finite_normalized_bound}, theorem_C={C}')
    return W, R


def check_cycle_and_projection():
    r = sp.Matrix(sp.symbols('r0:3'))
    d = sp.Matrix(sp.symbols('d0:3'))
    assert sp.expand(norm2(r.cross(d)) - norm2(r)*norm2(d) + (r.dot(d))**2) == 0
    l11, l21, l22, l12 = sp.symbols('l11 l21 l22 l12')
    u = sp.Matrix([2, 0, 1])
    v = sp.Matrix([1, 3, 1])
    d = sp.Matrix([-1, 1, 2])
    M = sp.Matrix.hstack(u, v, d)
    c = sp.Matrix([l22-l21, l12-l22, -l11+l21-l22+l12])
    cycle = l11*(-d) - l21*(u-d) + l22*(u-d-v) - l12*(-d-v)
    assert (cycle - M*c).applyfunc(sp.expand) == ZERO
    assert sp.expand((c[2]-c[1]) - (l21-l11)) == 0
    assert sp.expand((c[0]+c[2]) - (l12-l11)) == 0
    print('EXACT cycle signs, multiplier recovery, and normalized projection identity')


def nonnegative_coefficients(expr, variables):
    polynomial = sp.Poly(sp.expand(expr), *variables)
    assert all(coef >= 0 for coef in polynomial.coeffs())


def check_constants():
    p, q = sp.symbols('p q', nonnegative=True)
    rho, tau = p+1, q+1
    T = 2*rho + 2*tau*(1+rho)
    B0, Z = 3+8*rho, 6*rho+8*rho**2
    W = 8*rho**3+6*rho**2+3*rho
    assert sp.expand(W-(2*rho+rho*(2*rho+1)*(4*rho+1))) == 0
    for expr in [W-Z, 6*tau*rho-T, 11*rho-B0, 14*rho**2-Z,
                 17*rho**3-W, 930*tau*rho**4-T*(1+Z*B0),
                 930*tau*rho**4-W*B0,
                 5586*tau**2*rho**5-T*(1+930*tau*rho**4)]:
        nonnegative_coefficients(expr, [p, q])
    print('EXACT polynomial nonnegativity certificates for all rho,tau >= 1')


def check_counterexample_and_wedge_scaling():
    t, arm, delta = sp.symbols('t arm delta', real=True)
    lhs = delta**2*(t**2+arm**2*delta**2)-4*(t-1)**2*arm**2*delta**2
    rhs = delta**2*(t**2*(1-arm**2)+arm**2*(2-t)*(3*t-2)+arm**2*delta**2)
    assert sp.expand(lhs-rhs) == 0
    X4 = [ZERO, E1, E2, E2+2*E3]
    # A dual functional annihilates every homothety and is 1 on the data.
    H = sp.Matrix.vstack(*[sp.Matrix.hstack(x, sp.eye(3)) for x in X4])
    L = sp.Matrix.hstack(2*E1.T, -2*E1.T, -E3.T, E3.T)
    data = sp.Matrix.vstack(ZERO, ZERO, ZERO, E3)
    assert L*H == sp.zeros(1, 4)
    assert (L*data)[0] == 1
    assert sum(sp.sqrt(norm2(L[:, 3*i:3*i+3].T)) for i in range(4)) == 6
    delta_value = Q(1, 10**12)
    C = constant(Q(3), Q(1), delta_value)
    assert C*delta_value/2 >= Q(1, 6), 'h conditioning cannot be dropped'
    X = [ZERO, E1, E2+2*E3, E2]
    Y = [E2, E2+E3, 2*E1]
    W, R, _, _ = constraint_and_residual(X, Y)
    baseC = constant(Q(3), Q(1), Q(1))
    scale = 1/(100*baseC)
    Ws, Rs, _, _ = constraint_and_residual([scale*x for x in X], [scale*y for y in Y])
    assert Ws == scale*W and Rs == R
    assert constant(3*scale, scale, scale) == baseC
    # Choosing P=e3 only at e2+2e3 gives all wedges <= 3*scale.
    assert wedge_bound(baseC, 3*scale, scale) >= Q(1, 6), 'wedge factor 1/sigma is necessary'
    print('EXACT connected thin-image defect identity and homothety lower bound 1/6')
    print('EXACT velocity dilation: wedge matrix scales, residual matrix is invariant')


def check_cone_family():
    t = sp.symbols('t', positive=True)
    s, a = 2*t/(1+t*t), 2*t*t/(1+t*t)
    X = [sp.Matrix([0,0,1]), sp.Matrix([s,0,1-a]), sp.Matrix([0,-s,1-a])]
    Y = [sp.Matrix([0,s,1-a]), sp.Matrix([-s,0,1-a]), X[0]]
    assert all(sp.factor(norm2(z)-1) == 0 for z in X+Y)
    M = sp.Matrix.hstack(X[1]-X[0], Y[1]-Y[0], Y[0]-X[0])
    inverse_frob = sum(z*z for z in M.inv())
    assert sp.factor(inverse_frob - (3/(2*s*s)+3/(4*a*a))) == 0
    assert sp.factor(height2(X[2], X[0], X[1]) - s*s*(s*s+2*a*a)/(s*s+a*a)) == 0
    assert sp.factor(height2(Y[2], Y[0], Y[1]) - (s*s/2+a*a)) == 0
    assert sp.cancel((2*s)/(a/2)) == 4/t
    assert sp.cancel((2*s)/(s/2)) == 4
    # All pair lengths are zero, ring chords <= 2s, or sqrt(s^2+a^2);
    # 0<t<=1 implies a<=s. The following exact values check the finite pattern.
    distances = sorted({str(sp.factor(norm2(x-y))) for x in X+Y for y in X+Y})
    assert len(distances) == 4
    print('EXACT cone family: unit velocities, triangle heights, inverse norm, rho=4/t, tau=4')


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1,3))


def check_current_and_derivative_interfaces():
    rotations = []
    for p in permutations(range(3)):
        for signs in product((-1,1), repeat=3):
            if permutation_sign(p)*signs[0]*signs[1]*signs[2] != 1:
                continue
            R = sp.zeros(3)
            for i in range(3):
                R[i,p[i]] = signs[i]
            rotations.append(R)
    assert len(rotations) == 24
    assert sum(rotations, sp.zeros(3)) == sp.zeros(3)
    a,b,c,d,e,f = sp.symbols('a b c d e f')
    S = sp.Matrix([[a,d,e],[d,b,f],[e,f,c]])
    assert sum((R*S*R.T for R in rotations), sp.zeros(3))/24 == (a+b+c)*sp.eye(3)/3
    nu, m, k1, r, eta, length = sp.symbols('nu m k1 r eta length', positive=True)
    defect_gradient = sp.diff(nu*sp.sin(m*k1), k1).subs(k1,0)
    assert defect_gradient == nu*m
    assert (defect_gradient*E1).dot(-E2) == 0
    assert 2*sp.integrate(eta*r, (r,0,length)) == eta*length**2
    print('EXACT cubic averaging, high-frequency transverse derivative, and potential factor two')


def main():
    check_cycle_and_projection()
    check_constants()
    X = [ZERO, E1, E2+2*E3, E2, E2+2*E3]
    Ynear = [E2, E2+E3, 2*E1, ZERO, ZERO]
    finite_dual_certificate('skew_and_duplicates', X, Ynear, Q(3), Q(1), Q(1), 'near')
    Yfar = [E2, E2+E3, E1+E2+E3, ZERO, ZERO]
    finite_dual_certificate('off_line', X, Yfar, Q(3), Q(1), Q(1), 'far')
    Xe = [ZERO, E1, E2, E2+2*E3, E2]
    Ye = [E2, E2+E3, ZERO, 2*E1, ZERO]
    finite_dual_certificate('equal_triangle_anchors', Xe, Ye, Q(3), Q(1), Q(1), 'near')
    A = sp.Matrix([[2,1,-1],[0,3,1],[1,1,2]])
    shift = sp.Matrix([-2,1,3])
    Xt, Yt = [A*x+shift for x in X], [A*y+shift for y in Ynear]
    M = sp.Matrix.hstack(Xt[1]-Xt[0], Yt[1]-Yt[0], Yt[0]-Xt[0])
    sigma = 1/sum(abs(z) for z in M.inv())
    D = max(sum(abs(z) for z in x-y) for x in Xt+Yt for y in Xt+Yt)
    finite_dual_certificate('nonorthogonal', Xt, Yt, D, sigma, Q(1), 'near')
    check_counterexample_and_wedge_scaling()
    check_cone_family()
    check_current_and_derivative_interfaces()
    print('SCOPE: exact finite/symbolic controls; universal proof and supplied physical hypotheses are separate.')


if __name__ == '__main__':
    main()
    print('TOTAL: PASS=9 FAIL=0')

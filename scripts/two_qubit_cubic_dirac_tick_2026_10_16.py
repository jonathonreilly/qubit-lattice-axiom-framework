#!/usr/bin/env python3
"""A two-qubit site unfreezes the cubic-covariant tick: an exact Dirac-walk family.

Site C^2 (flavor, tau) (x) C^2 (spin, sigma); proper cubic rotations act as
1 (x) D(R). Ansatz U = f + i(h1 tau1 + h2 tau2) (x) 1 + i tau3 (x) g.sigma with
f, h1, h2 O-invariant and g O-equivariant real trigonometric polynomials on
the 27-point cell. The four Hermitian terms anticommute, so U is unitary iff
f^2 + h1^2 + h2^2 + |g|^2 = 1. Writing g = sum b_j v_j, the quadratic form of
(f, h1, h2) over the invariant basis is a Gram matrix G that the identity fixes
uniquely in terms of b; walks exist iff G(b) is positive semidefinite of rank
<= 3. Exact parts: Clifford relations, covariance, the formula for G(b), and an
algebraic point b* with det G(b*) = 0 and the other three eigenvalues > 0.
Numerical parts (labelled): the factorised walk's unitarity, its single
massless Dirac cone and the gapped doublers.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    'docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

C = sp.symbols('c1:4')
S = sp.symbols('s1:4')


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def reduce_trig(expr):
    e = sp.expand(expr)
    while True:
        poly = sp.Poly(e, *S)
        new = 0
        changed = False
        for mon, coef in poly.terms():
            term = coef
            for a, p in enumerate(mon):
                q, r = divmod(p, 2)
                if q:
                    changed = True
                term *= (1 - C[a] ** 2) ** q * S[a] ** r
            new += term
        e = sp.expand(new)
        if not changed:
            return e


c1, c2, c3 = C
s1, s2, s3 = S
PHI = [sp.Integer(1), c1 + c2 + c3, c1 * c2 + c1 * c3 + c2 * c3, c1 * c2 * c3]
VEC = [[s1, s2, s3], [s1 * (c2 + c3), s2 * (c1 + c3), s3 * (c1 + c2)], [s1 * c2 * c3, s2 * c1 * c3, s3 * c1 * c2]]
SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(a, b):
    return sp.kronecker_product(a, b)


def main() -> int:
    ck = Checks()
    # Clifford structure
    gam = [kron(SIG[1], SIG[0]), kron(SIG[2], SIG[0])] + [kron(SIG[3], SIG[a]) for a in (1, 2, 3)]
    anti = all((gam[i] * gam[j] + gam[j] * gam[i]) == (2 * sp.eye(4) if i == j else sp.zeros(4)) for i in range(5) for j in range(5))
    ck.check('tau1(x)1, tau2(x)1, tau3(x)sigma_a are five anticommuting Hermitian involutions', anti)
    # covariance: 1 (x) D commutes with the flavor terms and rotates the vector terms
    Jz = SIG[3] / 2
    Jx = SIG[1] / 2
    ok_cov = True
    for J, R in ((Jz, sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])), (Jx, sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]))):
        D = sp.cos(sp.pi / 4) * sp.eye(2) - sp.I * sp.sin(sp.pi / 4) * 2 * J
        W = kron(sp.eye(2), D)
        ok_cov &= all(sp.expand(W * g_ * W.H - g_) == sp.zeros(4) for g_ in gam[:2])
        for a in range(3):
            lhs = sp.expand(W * gam[2 + a] * W.H)
            rhs = sum((R[b, a] * gam[2 + b] for b in range(3)), sp.zeros(4))
            ok_cov &= sp.expand(lhs - rhs) == sp.zeros(4)
    ck.check('coin action 1 (x) D(R) fixes the flavor terms and rotates tau3 (x) sigma as a vector (generators)', ok_cov)
    # Gram matrix formula
    b = sp.symbols('b0:3', real=True)
    g = [sum(b[j] * VEC[j][i] for j in range(3)) for i in range(3)]
    G = sp.Matrix([[1 - 3 * b[0] ** 2, -2 * b[0] * b[1], -b[0] ** 2 - b[0] * b[2] + b[1] ** 2, -3 * b[1] * (b[0] - b[2])],
                   [0, b[0] ** 2 - 2 * b[1] ** 2, b[1] * (b[0] - b[2]), b[0] * b[2] - b[1] ** 2 + b[2] ** 2],
                   [0, 0, 2 * b[1] ** 2 - b[2] ** 2, 2 * b[1] * b[2]],
                   [0, 0, 0, 3 * b[2] ** 2]])
    for i in range(4):
        for j in range(i):
            G[i, j] = G[j, i]
    quad = sum(G[i, j] * PHI[i] * PHI[j] for i in range(4) for j in range(4))
    ck.check('Gram identity: sum G_ij phi_i phi_j + |g|^2 - 1 = 0 identically in k and b',
             reduce_trig(quad + sum(x ** 2 for x in g) - 1) == 0)
    Gsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'G{min(i, j)}{max(i, j)}'))
    quad2 = sum(Gsym[i, j] * PHI[i] * PHI[j] for i in range(4) for j in range(4))
    lin = sp.Poly(reduce_trig(quad2), *C, *S).as_dict()
    unknowns = sorted({Gsym[i, j] for i in range(4) for j in range(4)}, key=str)
    Mlin = sp.Matrix([[sp.diff(v, x) for x in unknowns] for v in lin.values()])
    ck.check('the identity determines G uniquely (the map G -> sum G_ij phi_i phi_j is injective)',
             Mlin.rank() == len(unknowns))
    # Theorem 4: speed bound and the axis-doubler trade-off (exact identities in b)
    s_ = b[0] + 2 * b[1] + b[2]
    v = sp.Matrix([1, 2, 1, 0])   # axis restriction: phi(t,0,0) = v + w cos t
    w_ = sp.Matrix([0, 1, 2, 1])
    ck.check('axis restriction: phi(t,0,0) = (1,2,1,0) + (0,1,2,1) cos t',
             all(sp.expand(PHI[i].subs({c2: 1, c3: 1}) - (v[i] + w_[i] * c1)) == 0 for i in range(4)))
    ck.check('v^T G v = 1 - s^2, w^T G w = s^2, v^T G w = 0 with s = b0 + 2 b1 + b2 (so s^2 <= 1 when G >= 0)',
             sp.expand((v.T * G * v)[0] - (1 - s_ ** 2)) == 0 and sp.expand((w_.T * G * w_)[0] - s_ ** 2) == 0
             and sp.expand((v.T * G * w_)[0]) == 0)
    ck.check('F(0).F(pi,0,0) = (v+w)^T G (v-w) = 1 - 2 s^2: the axis doubler gap is 2 arcsin|s|',
             sp.expand(((v + w_).T * G * (v - w_))[0] - (1 - 2 * s_ ** 2)) == 0)
    # Theorem 5: the unique light-speed member, over Q(sqrt 5)
    r5 = sp.sqrt(5)
    bgold = {b[0]: (9 * r5 - 5) / 38, b[1]: (5 * r5 - 7) / 19, b[2]: (71 - 29 * r5) / 38}
    Gg = G.subs(bgold).applyfunc(sp.expand)
    ck.check('golden member: G(b_gold) v = 0 and s = 1 exactly', all(sp.expand(x) == 0 for x in Gg * v) and sp.expand(s_.subs(bgold)) == 1)
    lam = sp.Symbol('lam')
    cpg = sp.Poly(sp.expand((Gg - lam * sp.eye(4)).det(method='berkowitz')), lam)
    eg = [sp.expand(-cpg.coeff_monomial(lam ** 3)), sp.expand(cpg.coeff_monomial(lam ** 2)), sp.expand(-cpg.coeff_monomial(lam))]
    ck.check('golden member: e1, e2, e3 > 0 and det = 0 exactly, so G >= 0 of rank 3',
             all(sp.N(e, 50) > 0 for e in eg) and sp.expand(cpg.coeff_monomial(1)) == 0)
    sols_v = sp.solve(list(G * v), list(b), dict=True)
    def is_psd(M):
        cp_ = sp.Poly(sp.expand((M.applyfunc(sp.expand) - lam * sp.eye(4)).det(method='berkowitz')), lam)
        es = [(-1) ** k * cp_.coeff_monomial(lam ** (4 - k)) for k in range(1, 5)]   # e1..e4 of a symmetric matrix
        return all(sp.re(sp.N(e, 40)) >= -sp.Rational(1, 10 ** 30) for e in es)
    psd = [sv for sv in sols_v if is_psd(G.subs(sv))]
    ck.check('G v = 0 has four solutions; exactly the pair +-b_gold is positive semidefinite (light speed is unique up to sign)',
             len(sols_v) == 4 and len(psd) == 2)
    phi0 = sp.Matrix([1, 3, 3, 1])
    fg = sum(((Gg * phi0)[i] * PHI[i] for i in range(4)), sp.Integer(0))
    ck.check('golden member: f(t,0,0) = cos t exactly (light-like along the axes), so U(pi,0,0) = -1 (pi-mode doublers)',
             sp.expand(sp.expand(fg.subs({c2: 1, c3: 1}) - c1)) == 0)
    eps = sp.Symbol('eps', positive=True)
    nn = sp.symbols('n1:4', real=True)
    fe = fg.subs({C[a]: sp.cos(eps * nn[a]) for a in range(3)})
    one_f = sp.expand(sp.series(1 - fe, eps, 0, 6).removeO())
    w2 = sp.expand(sp.series(2 * one_f + one_f ** 2 / 3, eps, 0, 6).removeO())
    nsq = nn[0] ** 2 + nn[1] ** 2 + nn[2] ** 2
    kap = sp.Rational(7, 6) - r5 / 2
    target = eps ** 2 * nsq - kap * eps ** 4 * (nsq ** 2 - (nn[0] ** 4 + nn[1] ** 4 + nn[2] ** 4))
    ck.check('golden member: omega^2 = |k|^2 - (7/6 - sqrt5/2)(|k|^4 - sum k_a^4) + O(k^6) (quadratic, parity-even anisotropy)',
             sp.expand(w2 - target) == 0)
    # Theorem 6: exact chirality tau3 (x) 1 commutes with the coin action
    T3 = kron(SIG[3], SIG[0])
    ck.check('tau3 (x) 1 commutes with 1 (x) D(R): a chirality-symmetric walk splits into two one-qubit covariant blocks',
             all(sp.expand(kron(sp.eye(2), sp.cos(sp.pi / 4) * sp.eye(2) - sp.I * sp.sin(sp.pi / 4) * P_) * T3 - T3 * kron(sp.eye(2), sp.cos(sp.pi / 4) * sp.eye(2) - sp.I * sp.sin(sp.pi / 4) * P_)) == sp.zeros(4)
                 for P_ in (SIG[1], SIG[3])))

    # Corollary (staggering): parities of the cell functions under k -> k + (pi,pi,pi)
    Qsub = {c1: -c1, c2: -c2, c3: -c3, s1: -s1, s2: -s2, s3: -s3}
    phi_par = [sp.cancel(PHI[i].subs(Qsub, simultaneous=True) / PHI[i]) for i in range(4)]
    vec_par = [sp.cancel(VEC[j][0].subs(Qsub, simultaneous=True) / VEC[j][0]) for j in range(3)]
    ck.check('under k -> k + Q: phi = (1, sum c, sum cc, c1c2c3) has parities (+,-,+,-); v0, v1, v2 have (-,+,-)',
             phi_par == [1, -1, 1, -1] and vec_par == [-1, 1, -1])
    # twist epsilon = -1 forces g odd: b1 = 0; then G >= 0 forces b = 0
    G0 = G.subs(b[1], 0)
    ck.check('staggered, epsilon = -1: with b1 = 0, G22 = -b2^2 and G02 = -b0^2 - b0 b2, so G >= 0 forces b2 = 0 then b0 = 0',
             sp.expand(G0[2, 2] + b[2] ** 2) == 0 and sp.expand(G0.subs(b[2], 0)[2, 2]) == 0
             and sp.expand(G0.subs(b[2], 0)[0, 2] + b[0] ** 2) == 0)
    Gp = G.subs({b[0]: 0, b[2]: 0})
    ck.check('staggered, epsilon = +1: with b0 = b2 = 0, G33 = 0 and G13 = -b1^2, so G >= 0 forces b1 = 0',
             sp.expand(Gp[3, 3]) == 0 and sp.expand(Gp[1, 3] + b[1] ** 2) == 0)

    # algebraic point on det G = 0 with G >= 0 of rank 3
    B0, B2 = sp.Rational(11, 30), sp.Rational(3, 20)
    u = sp.Symbol('u')
    Gb = G.subs({b[0]: B0, b[2]: B2})
    detq = sp.Poly(sp.expand(Gb.det().subs(b[1], sp.sqrt(u))), u)
    ck.check('det G(b) is even in b1, so det = 0 is a quartic in u = b1^2', detq.degree() == 4)
    ustar = min(r for r in detq.real_roots() if r > 0)
    charp = (Gb.subs(b[1], sp.sqrt(u)) - sp.Symbol('lam') * sp.eye(4)).det()
    cp = sp.Poly(sp.expand(charp), sp.Symbol('lam'))
    co = [sp.expand(cp.coeff_monomial(sp.Symbol('lam') ** k)) for k in range(5)]
    # charpoly = lam^4 - e1 lam^3 + e2 lam^2 - e3 lam + e4 ; e4 = det = 0 at u*
    e1, e2, e3 = -co[3], co[2], -co[1]
    signs = []
    for e in (e1, e2, e3):
        pe = sp.Poly(sp.expand(e), u)
        val = pe.eval(ustar) if pe.degree() > 0 else pe.as_expr()
        signs.append(sp.sign(sp.nsimplify(val) if pe.degree() == 0 else sp.N(val, 50)))
    ck.check('at b* = (11/30, sqrt(u*), 3/20): det G = 0 exactly (the minimal polynomial of u* divides the quartic)', detq.rem(sp.Poly(ustar.poly.as_expr().subs(ustar.poly.gen, u), u)).is_zero)
    ck.check('at b*: e1, e2, e3 of G are positive, so the three nonzero eigenvalues are positive (G >= 0, rank 3)',
             all(sg == 1 for sg in signs))

    # numerical construction (labelled numerical)
    bnum = np.array([float(B0), float(sp.sqrt(ustar).evalf(40)), float(B2)])
    Gn = np.array(Gb.subs(b[1], sp.sqrt(ustar)).evalf(40).tolist(), float)
    w, V = np.linalg.eigh(Gn)
    F = (V[:, w > 1e-12] * np.sqrt(w[w > 1e-12])).T

    def phin(k):
        cc = np.cos(k)
        return np.array([1, cc.sum(), cc[0] * cc[1] + cc[0] * cc[2] + cc[1] * cc[2], cc.prod()])
    F0 = F @ phin(np.zeros(3))
    Q = np.linalg.qr(np.column_stack([F0, np.eye(3)[:, :2]]))[0]
    if Q[:, 0] @ F0 < 0:
        Q[:, 0] *= -1
    F = Q.T @ F

    def gn(k):
        cc, ss = np.cos(k), np.sin(k)
        v2 = np.array([ss[0] * (cc[1] + cc[2]), ss[1] * (cc[0] + cc[2]), ss[2] * (cc[0] + cc[1])])
        v3 = np.array([ss[0] * cc[1] * cc[2], ss[1] * cc[0] * cc[2], ss[2] * cc[0] * cc[1]])
        return bnum[0] * ss + bnum[1] * v2 + bnum[2] * v3
    t = [np.eye(2), np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])]

    def U(k):
        f, h1, h2 = F @ phin(k)
        gg = gn(k)
        return (f * np.eye(4) + 1j * (h1 * np.kron(t[1], t[0]) + h2 * np.kron(t[2], t[0]))
                + 1j * np.kron(t[3], gg[0] * t[1] + gg[1] * t[2] + gg[2] * t[3]))
    rng = np.random.default_rng(0)
    K = rng.uniform(-np.pi, np.pi, (2000, 3))
    err = max(np.abs(U(k) @ U(k).conj().T - np.eye(4)).max() for k in K)
    ck.check(f'[numerical] factorised walk is unitary to 1e-12 on 2000 random momenta (max error {err:.1e})', err < 1e-12)
    ck.check('[numerical] F(0) = (1,0,0): U(0) = 1, a massless point at k = 0', np.allclose(F @ phin(np.zeros(3)), [1, 0, 0]))
    gaps = []
    for Kp in itertools.product((0.0, np.pi), repeat=3):
        if any(Kp):
            gaps.append(float(np.arccos(np.clip((F @ phin(np.array(Kp)))[0], -1, 1))))
    ck.check(f'[numerical] all seven doublers are gapped (quasienergy gaps {min(gaps):.3f}..{max(gaps):.3f} rad)', min(gaps) > 1.0)
    grid = np.linspace(-np.pi, np.pi, 41)[:-1]
    mins = sorted(1 - (F @ phin(np.array(k)))[0] ** 2 for k in itertools.product(grid, grid, grid))
    ck.check('[numerical] on a 40^3 grid the bands touch only at k = 0', abs(mins[0]) < 1e-12 and mins[1] > 1e-3)
    speed = bnum[0] + 2 * bnum[1] + bnum[2]
    print(f'cone: omega = {speed:.6f} |k| + O(k^2), isotropic (g = (b0 + 2 b1 + b2) k + O(k^3); invariant h have zero gradient at k = 0)')
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

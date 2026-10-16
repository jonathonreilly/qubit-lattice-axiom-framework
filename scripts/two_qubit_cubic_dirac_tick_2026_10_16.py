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
massless Dirac cone and the gapped doublers. Theorem 7 (exact): the massless
member's dispersion is cos omega = phi0^T G(b) phi(k); its cubic anisotropy at
order k^4 vanishes exactly on the plane b0 = b1 + 2 b2, where speeds are at
most sqrt(2/3) (attained at b_iso over Q(sqrt6, sqrt15)) and the order-k^6
anisotropy -(s^2/360)|k|^2 sum k^4 never vanishes.
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
    Wsq = sp.expand((w_.T * G * w_)[0] - ((v + w_).T * G * w_)[0] ** 2)
    ck.check('Wilson-gap identity: the flavor part W of the k^2 term of the massless member has |W|^2 = w^T G w - (phi0^T G w)^2 = s^2 (1 - s^2) = sin^2(theta_X)/4',
             sp.expand(Wsq - s_ ** 2 * (1 - s_ ** 2)) == 0)
    ck.check('F(0).F(pi,0,0) = (v+w)^T G (v-w) = 1 - 2 s^2: the axis doubler gap is 2 arcsin|s|',
             sp.expand(((v + w_).T * G * (v - w_))[0] - (1 - 2 * s_ ** 2)) == 0)
    phiK = lambda c: sp.Matrix([1, sum(c), c[0] * c[1] + c[0] * c[2] + c[1] * c[2], c[0] * c[1] * c[2]])
    p0v = phiK((1, 1, 1))
    cM = sp.expand((p0v.T * G * phiK((-1, -1, 1)))[0])
    cR = sp.expand((p0v.T * G * phiK((-1, -1, -1)))[0])
    ck.check('doubler gaps: cos(theta_M) = 1 - 8 s (b0 - b2), cos(theta_R) = 1 - 6(3 b0^2 + 2 b0 b2 + 3 b2^2 - 8 b1^2)',
             sp.expand(cM - (1 - 8 * s_ * (b[0] - b[2]))) == 0
             and sp.expand(cR - (1 - 6 * (3 * b[0] ** 2 + 2 * b[0] * b[2] + 3 * b[2] ** 2 - 8 * b[1] ** 2))) == 0)
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

    # Corollary to Theorem 5: the hw=1 triplet at the light-speed member
    q1s, q2s, es = sp.symbols('q1s q2s es')
    kx = [sp.pi + es * q1s, es * q2s, sp.Integer(0)]
    cx = [sp.cos(x) for x in kx]
    phx = sp.Matrix([1, sum(cx), cx[0] * cx[1] + cx[0] * cx[2] + cx[1] * cx[2], cx[0] * cx[1] * cx[2]])
    fx = (sp.Matrix([1, 3, 3, 1]).T * Gg * phx)[0]
    c2x = sp.expand(sp.series(1 + fx, es, 0, 3).removeO()).coeff(es, 2)
    ck.check('light-speed member: at X = (pi,0,0) a massless pi-mode cone, (omega - pi)^2 = q_par^2 + (sqrt5 - 2)^2 q_perp^2 (uniaxial, v_perp = sqrt5 - 2 = phi^-3)',
             sp.simplify(sp.expand(fx.subs(es, 0)) + 1) == 0 and sp.simplify(2 * c2x - (q1s ** 2 + (r5 - 2) ** 2 * q2s ** 2)) == 0)
    # Theorem 7: quartic isotropy and the sqrt(2/3) bound
    phi0c = sp.Matrix([1, 3, 3, 1])
    ck.check('phi0^T G phi0 = 1 identically in b: the massless member has f = phi0^T G phi(k)',
             sp.expand((phi0c.T * G * phi0c)[0]) == 1)
    def omega2_series(Gm, order):
        cs = [sum((-1) ** j * (eps * x) ** (2 * j) / sp.factorial(2 * j) for j in range(order // 2 + 1)) for x in nn]
        ph = sp.Matrix([1, sum(cs), cs[0] * cs[1] + cs[0] * cs[2] + cs[1] * cs[2], cs[0] * cs[1] * cs[2]])
        uu = sp.expand((phi0c.T * Gm * (phi0c - ph))[0])
        uu = sum(uu.coeff(eps, j) * eps ** j for j in range(order + 1))
        ww = sp.expand(2 * uu + uu ** 2 / 3 + 8 * uu ** 3 / 45)
        return [sp.expand(ww.coeff(eps, j)) for j in range(order + 1)]
    N4 = sum(x ** 4 for x in nn)
    alpha = s_ * (b[0] ** 3 + 6 * b[0] ** 2 * b[1] + 3 * b[0] ** 2 * b[2] + 12 * b[0] * b[1] ** 2 + 12 * b[0] * b[1] * b[2]
                  + 3 * b[0] * b[2] ** 2 + 3 * b[0] + 8 * b[1] ** 3 + 12 * b[1] ** 2 * b[2] + 6 * b[1] * b[2] ** 2
                  - 6 * b[1] + b[2] ** 3 - 9 * b[2]) / 12
    beta = -s_ * (b[0] - b[1] - 2 * b[2]) / 3
    w = omega2_series(G, 4)
    ck.check('massless member: omega^2 = s^2 |k|^2 + alpha(b) |k|^4 + beta(b) sum k_a^4 + O(k^6), beta = -s (b0 - b1 - 2 b2)/3',
             sp.expand(w[2] - s_ ** 2 * nsq) == 0 and sp.expand(w[4] - alpha * nsq ** 2 - beta * N4) == 0)
    ck.check('alpha(b) = s (s^3 + 3 b0 - 6 b1 - 9 b2)/12', sp.expand(alpha - s_ * (s_ ** 3 + 3 * b[0] - 6 * b[1] - 9 * b[2]) / 12) == 0)
    ck.check('golden member: beta(b_gold) = 7/6 - sqrt5/2 (agrees with Theorem 5)',
             sp.expand(beta.subs(bgold) - kap) == 0)
    Gp = G.subs(b[0], b[1] + 2 * b[2]).applyfunc(sp.expand)
    Qp = sp.cancel(Gp.det() / (b[1] + b[2]) ** 2)
    ck.check('on the isotropy plane b0 = b1 + 2 b2: det G = (b1 + b2)^2 Q(b1, b2) with Q polynomial; there s = 3(b1 + b2)',
             sp.denom(sp.together(Qp)) == 1 and sp.expand(s_.subs(b[0], b[1] + 2 * b[2]) - 3 * (b[1] + b[2])) == 0)
    Ssym = sp.Symbol('S')
    disc = sp.discriminant(sp.Poly(sp.expand(Qp.subs(b[2], Ssym / 3 - b[1])), b[1]))
    expected = {sp.Poly(Ssym, Ssym): 12, sp.Poly(8 * Ssym ** 2 + 3, Ssym): 1, sp.Poly(3 * Ssym ** 2 - 2, Ssym): 2,
                sp.Poly(Ssym ** 4 + 84 * Ssym ** 2 + 36, Ssym): 1}
    got = {sp.Poly(f_, Ssym).monic(): m for f_, m in sp.factor_list(disc)[1]}
    ck.check('discriminant in b1 of Q at fixed speed S is c S^12 (8S^2 + 3)(3S^2 - 2)^2 (S^4 + 84 S^2 + 36): real critical speeds 0, +-sqrt(2/3)',
             got == {k.monic(): v for k, v in expected.items()})
    minors = [sp.expand(Gp.extract(list(r_), list(c_)).det()) for r_ in itertools.combinations(range(4), 3) for c_ in itertools.combinations(range(4), 3)]
    Gm2 = sp.groebner([m for m in minors if m != 0], b[1], b[2], order='grevlex')
    ck.check('on the plane, rank G <= 2 only at b = 0 (b1, b2 in the radical of the 3x3 minors), so the PSD part of {Q = 0} is a union of compact components',
             any(Gm2.contains(b[1] ** p) for p in range(1, 9)) and any(Gm2.contains(b[2] ** p) for p in range(1, 9)))
    r6, r15 = sp.sqrt(6), sp.sqrt(15)
    biso = {b[0]: (r6 + 2 * r15) / 27, b[1]: (5 * r6 - 2 * r15) / 27, b[2]: (2 * r15 - 2 * r6) / 27}
    Gi = G.subs(biso).applyfunc(sp.expand)
    cpi = sp.Poly(sp.expand((Gi - lam * sp.eye(4)).det(method='berkowitz')), lam)
    ei = [sp.expand(-cpi.coeff_monomial(lam ** 3)), sp.expand(cpi.coeff_monomial(lam ** 2)), sp.expand(-cpi.coeff_monomial(lam))]
    ck.check('b_iso = ((sqrt6 + 2 sqrt15)/27, (5 sqrt6 - 2 sqrt15)/27, (2 sqrt15 - 2 sqrt6)/27): on the plane, s = sqrt(2/3), det G = 0, e1, e2, e3 > 0 (G >= 0, rank 3)',
             sp.expand(biso[b[0]] - biso[b[1]] - 2 * biso[b[2]]) == 0 and sp.simplify(s_.subs(biso) - sp.sqrt(sp.Rational(2, 3))) == 0
             and sp.expand(cpi.coeff_monomial(1)) == 0 and all(sp.N(e, 50) > 0 for e in ei))
    wi = omega2_series(Gi, 6)
    N6 = sum(x ** 6 for x in nn)
    P222 = nn[0] ** 2 * nn[1] ** 2 * nn[2] ** 2
    target6 = sp.Rational(1, 243) * nsq ** 3 - sp.Rational(1, 540) * nsq * N4 + (sp.sqrt(10) / 9 - sp.Rational(16, 45)) * P222
    ck.check('b_iso: omega^2 = (2/3)|k|^2 - (1/54)|k|^4 + (1/243)|k|^6 - (1/540)|k|^2 sum k^4 + (sqrt10/9 - 16/45) k1^2 k2^2 k3^2 + O(k^8)',
             sp.expand(wi[2] - sp.Rational(2, 3) * nsq) == 0 and sp.expand(wi[4] + nsq ** 2 / 54) == 0
             and sp.expand(sp.radsimp(wi[6] - target6)) == 0)
    del N6
    bi = [float(biso[x]) for x in b]
    ck.check('b_iso doubler gaps: cos theta_X = -1/3, cos theta_M = -7/9 (exact, from Theorem 4 formulas)',
             sp.simplify((1 - 2 * s_ ** 2).subs(biso) + sp.Rational(1, 3)) == 0
             and sp.simplify((1 - 8 * s_ * (b[0] - b[2])).subs(biso) + sp.Rational(7, 9)) == 0)
    Gin = np.array(Gi.evalf(30), dtype=float)
    ai = Gin @ np.array([1.0, 3, 3, 1])
    tg = np.linspace(-np.pi, np.pi, 41)
    KK = np.stack(np.meshgrid(tg, tg, tg, indexing='ij'), -1).reshape(-1, 3)
    cc = np.cos(KK)
    phg = np.stack([np.ones(len(cc)), cc.sum(1), cc[:, 0] * cc[:, 1] + cc[:, 0] * cc[:, 2] + cc[:, 1] * cc[:, 2], cc.prod(1)], 1)
    om = np.arccos(np.clip(phg @ ai, -1, 1))
    kl = np.linalg.norm(2 * np.sin(KK / 2), axis=1)   # lattice momentum, zero only at k = 0
    ck.check('[numerical] b_iso: on a 41^3 grid omega >= 0.9 s |2 sin(k/2)| (single cone at k = 0, no doublers)',
             np.all(om >= 0.9 * np.sqrt(2 / 3) * kl))
    # sampled check along the isotropic curve: which speeds occur
    lamv = sp.Symbol('lamv')
    Ql = sp.expand(Qp.subs(b[2], lamv * b[1]) / b[1] ** 4)
    P6l, P4l = sp.lambdify(lamv, Ql.coeff(b[1], 2)), sp.lambdify(lamv, Ql.coeff(b[1], 0))
    yco = -s_ * (20 * b[0] ** 3 + 60 * b[0] ** 2 * b[1] - 120 * b[0] * b[1] * b[2] - 60 * b[0] * b[2] ** 2 - 9 * b[0] - 80 * b[1] ** 3
                 - 240 * b[1] ** 2 * b[2] - 180 * b[1] * b[2] ** 2 + 12 * b[1] - 40 * b[2] ** 3 + 21 * b[2]) / 360
    w6 = omega2_series(G, 6)[6]
    xs_, ys_, zs_ = sp.symbols('xs ys zs')
    s6 = sp.solve(sp.Poly(sp.expand(w6 - xs_ * nsq ** 3 - ys_ * nsq * N4 - zs_ * P222), *nn).coeffs(), [xs_, ys_, zs_], dict=True)[0]
    ck.check('sextic coefficient of |k|^2 sum k^4 in omega^2 is y(b) = -s (20 b0^3 + ... + 21 b2)/360', sp.expand(s6[ys_] - yco) == 0)
    onp = {b[0]: b[1] + 2 * b[2]}
    sp_ = 3 * (b[1] + b[2])
    ck.check('on the isotropy plane: alpha = -s^2 (1 - s^2)/12, x = s^2 (8 s^4 - 5 s^2 + 2)/360, y = -s^2/360 (depend on s only)',
             sp.expand(alpha.subs(onp) + sp_ ** 2 * (1 - sp_ ** 2) / 12) == 0
             and sp.expand(s6[xs_].subs(onp) - sp_ ** 2 * (8 * sp_ ** 4 - 5 * sp_ ** 2 + 2) / 360) == 0
             and sp.expand(s6[ys_].subs(onp) + sp_ ** 2 / 360) == 0)
    ck.check('|k|^6, |k|^2 sum k^4 and k1^2 k2^2 k3^2 are linearly independent, so y != 0 is a genuine k^6 anisotropy for every moving isotropic member',
             len(s6) == 3)
    G_f = sp.lambdify(b, G)
    samples = []
    for L in np.linspace(0.55, 0.85, 3001):
        q = -P4l(L) / P6l(L)
        if not np.isfinite(q) or q <= 0:
            continue
        for sg in (1, -1):
            B1 = sg * np.sqrt(q)
            B = (B1 + 2 * L * B1, B1, L * B1)
            if np.linalg.eigvalsh(np.array(G_f(*B), float))[0] >= -1e-10:
                samples.append((0.0, 0.0, B[0] + 2 * B[1] + B[2]))
    samples = np.array(samples)
    sv = np.sort(np.abs(samples[:, 2]))
    ck.check(f'[numerical] {len(samples)} PSD samples of the isotropic curve: speeds fill [{sv[0]:.3f}, sqrt(2/3)] (largest gap {np.diff(sv).max():.1e}), never above',
             len(samples) > 100 and sv[0] < 0.1 and sv[-1] > np.sqrt(2 / 3) - 1e-6 and np.diff(sv).max() < 0.01
             and sv[-1] <= np.sqrt(2 / 3) + 1e-9)
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

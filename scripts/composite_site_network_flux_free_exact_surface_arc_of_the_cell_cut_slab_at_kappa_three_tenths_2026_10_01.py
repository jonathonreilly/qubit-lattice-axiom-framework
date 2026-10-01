#!/usr/bin/env python3
"""Composite-site network, flux-free u = +1 Majorana comparator, J = (1,1,1), kappa = 3/10: exact / interval-certified description of the top-surface zero
modes (the Fermi arc) of the cell-cut a3 HALF-INFINITE slab (layers 0, 1, 2, ...; periodic in (u, v) = (f1, f2); surface = layer 0; supplied model only).

Setting.  Layer blocks A(u,v) = H_{L,L}, B(u,v) = H_{L,L+1} (H_{L,L-1} = B^dagger) of H = iM, copied from the landed network rules (is_site/flavour/neighbours/reduce/terms);
the bulk recursion B^dag psi_{L-1} + A psi_L + B psi_{L+1} = 0 has characteristic quartic P(lambda) = lambda^2 det(B^dag/lambda + A + lambda B); with lambda = e^{i pi (u+v)} mu it is a REAL
quadratic in x = mu + 1/mu.  Notation: S_u = sin pi u, C_u = cos pi u, S_v, C_v likewise, X = S_u^2, Y = S_v^2, k = 2 kappa = 3/5, K = k^2 = 9/25.

EXACT (sympy / Fraction identities, no floating point):  blocks and rank B = 2; gauge-fixed real-coefficient blocks; the quartic r0 (mu^4+1) + r1 (mu^3+mu) + r2 mu^2 with closed forms r0, r1, r2;
Schur complement onto the q-components (sites 2,3): n(mu), g(mu) with K g^2 + mu^2 n(mu) n(1/mu) = (1 + K X) mu^2 det Hh(mu); the two quadratics Eq1, Eq2 in tau = n/g, the identities C1 = -K A1,
A2 C1 = A1 C2, R = Res_tau = -K Y^2 and the eliminant Y = A1 B2 - A2 B1 = const * S_u^2 S_v^3 * H * G' (H = common-root factor of (n,g), G' irreducible over Q), the integer form
625 G' = S_u a0 + C_u C_v S_v b0, a0 = 625 + 300Y + 27Y^2 - (750+108Y)X + 81X^2, b0 = 2500 - 300Y - (600+108Y)X - 540X^2, the full-angle polynomial P = s_u a0 + (1/2)(1+c_u) s_v b0 = 2 C_u 625 G'
(factor C_u = the straight line u = 1/2), the closed form of Xi = n(1) n(-1) + K g(1) g(-1) = F_tau(1) F_tau(-1) on G' = 0 (Omega divisible by G'), and the endpoint algebra: on u + v = 1,
G' = S_u (1 - 2KX)(4KX^2 + 4(1-K)X - 3) (the second factor is the landed family-(i) condition), and at the node cos 2 pi u0 = (25 - 7 sqrt 19)/9, v0 = 1 - u0: mu = -1 (lambda = 1, |lambda| = 1) is a common root of
n and g (so the middle-band touching kernel is 2-dimensional), Q(-2) = 0, Xi = 0.
THEOREM USED (argued, see NOT machine-checked): for generic (u,v) a zero mode exists iff G'(u,v) = 0 and Xi(u,v) > 0.
INTERVAL-CERTIFIED (mpmath.iv, outward rounding, exact rational polynomial coefficients, mean-value centred forms): (6) over u in [1e-5, 0.34] the zero set of G' is the graph of a unique continuous v = f(u)
(sign change of G' across a v-bracket for all u of each box + dG'/dv != 0), Xi > 0, Res_mu(n,g) != 0 and no bulk root on |mu| = 1 (both x-roots non-real or |x| > 2), adjacent boxes share the root;
(7) over the node window [0.34, 0.37] the graph exists and dXi/du along the curve is < 0, the node (u0, 1-u0) lies on it; (8) branch-and-bound over u in [0.001, 0.499] x v in [0, 1]: every box is cleared by
G' != 0, Xi < 0, or lies in a certified corridor box: there is no other point with G' = 0 and Xi >= 0 (0 undecided boxes).
FLOAT DIAGNOSTIC: (9) the N = 40 finite-slab top-half negative-weight contour (80 x 80 half-offset grid, |jump| > 0.5) equals the set of grid edges where G' changes sign with Xi > 0, and the set where the
direct 4x4 criterion (sin of the angle between the q-parts of the two inside-root null vectors < 1e-6) holds.  Also the float singular values of A + B + B^dag at the node.
NOT machine-checked (open): the root-pair step from Xi > 0 to an actual zero mode (an argument: Xi > 0 means the real quadratic F_tau has both roots inside or both outside, tau and -K/tau give reciprocal
pairs, so exactly one gives the inside pair; only checked numerically in (9)); the disc(Q) = 0 crossing of the arc at u = 0.30518 (the two inside roots coincide: 4 corridor boxes straddle it; the zero mode
there rests on continuity); the loci u = 0 and v = 0 (B drops rank), the common-root curve H = 0, and zero modes exactly ON those loci or on disc(Q) = 0; the strips u < 1e-5 and u in (0.499, 0.501); the
node neighbourhood within ~0.015 of u0 for H != 0 and for "no unimodular root" (only dXi/du < 0 and the graph are certified there); the mirror part u in (1-u0, 1) (used through the exact invariance of
G' and Xi under (u,v) -> (1-u,1-v), which is checked symbolically); the straight line u = 1/2 itself (exact result in the sline note; here only the factor C_u and Q4 = (det A_qp)^2 are checked).  No statement
about other kappa, other J, other terminations, or physical identifications.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import resource
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 900
iv = mp.iv
iv.dps = 40
RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label} :: {detail}", flush=True)


# ------------------------------------------------------------------------------------------------ network rules (as landed; copied)
AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce_(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms_sym(J, kappa):
    """Real hopping terms (a, b, n, t): M[a,b] += t z1^n1 z2^n2, M[b,a] -= t conj(.), amplitudes 2 J_flavour and 2 kappa (as in sline_lib / arcs_runner)."""
    out = []
    for p in REPS:
        a, n0 = reduce_(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_(q)
                out.append((a, b, tuple(int(x) for x in n), 2 * J[AX[flavour(p, q)]]))
        nb = {flavour(p, q): q for q in neighbours(p)}
        assert len(nb) == 3
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce_(nb[l]); r2, n2 = reduce_(nb[m])
            out.append((r1, r2, tuple(int(x) for x in (n2[0] - n1[0], n2[1] - n1[1], n2[2] - n1[2])), 2 * kappa))
    return out


Jx, Jy, Jz, kap = sp.symbols("J_x J_y J_z kappa", real=True)
z1, z2 = sp.symbols("z1 z2")


def layer_blocks(T):
    M = {}
    def blk(m):
        if m not in M:
            M[m] = sp.zeros(4, 4)
        return M[m]
    for (a, b, n, t) in T:
        ph = z1 ** n[0] * z2 ** n[1]; phc = z1 ** (-n[0]) * z2 ** (-n[1])
        blk(n[2])[a, b] += t * ph
        blk(-n[2])[b, a] -= t * phc
    return {m: (sp.I * B).applyfunc(sp.expand) for m, B in M.items()}


def dag(Xm):
    return Xm.subs({z1: 1 / z1, z2: 1 / z2}, simultaneous=True).xreplace({sp.I: -sp.I}).T.applyfunc(sp.expand)


kap_s = sp.Rational(3, 10); k_s = 2 * kap_s; K_s = k_s ** 2
Su, Cu, Sv, Cv = sp.symbols("S_u C_u S_v C_v", real=True)
mu, tau, lam, pp, qq = sp.symbols("mu tau lambda p q")


def red2(e):
    """reduce C_u^2 -> 1 - S_u^2, C_v^2 -> 1 - S_v^2"""
    e = sp.expand(e)
    out = 0
    for (m,), c in sp.Poly(e, Cu).terms():
        out += c * Cu ** (m % 2) * (1 - Su ** 2) ** (m // 2)
    e = sp.expand(out); out = 0
    for (m,), c in sp.Poly(e, Cv).terms():
        out += c * Cv ** (m % 2) * (1 - Sv ** 2) ** (m // 2)
    return sp.expand(out)


_SUBPQ = {Su: 2 * pp / (1 + pp ** 2), Cu: (1 - pp ** 2) / (1 + pp ** 2), Sv: 2 * qq / (1 + qq ** 2), Cv: (1 - qq ** 2) / (1 + qq ** 2)}


def to_pq(e):
    """numerator of e(S,C) under S = 2p/(1+p^2), C = (1-p^2)/(1+p^2) (p = tan(pi u/2), q = tan(pi v/2)), as a Poly in (p, q) over QQ"""
    num, den = sp.fraction(sp.cancel(sp.together(sp.sympify(e).subs(_SUBPQ))))
    return sp.Poly(num, pp, qq, domain=sp.QQ)


def degs(P):
    return (P.degree(pp), P.degree(qq))


# ------------------------------------------------------------------------------------------------ (1) blocks, rank structure
Bk = layer_blocks(terms_sym((Jx, Jy, Jz), kap))
Asym, Bsym = Bk[0], Bk[1]
ok_off = sorted(Bk.keys()) == [-1, 0, 1]
ok_dag = (Bk[-1] - dag(Bsym)).applyfunc(sp.simplify) == sp.zeros(4, 4) and (Asym - dag(Asym)).applyfunc(sp.simplify) == sp.zeros(4, 4)
nz = [(i, j) for i in range(4) for j in range(4) if Bsym[i, j] != 0]
Csym = Bsym[2:4, 0:2]
ok_det = sp.simplify(Csym.det().subs({Jx: 1, Jy: 1, Jz: 1}) - 4 * kap ** 2 * (z1 - 1) * (z2 - 1) / (z1 * z2)) == 0
A = Asym.subs({Jx: 1, Jy: 1, Jz: 1, kap: kap_s}).applyfunc(sp.expand)
B = Bsym.subs({Jx: 1, Jy: 1, Jz: 1, kap: kap_s}).applyfunc(sp.expand)
rankB = Bsym.rank()
fA = sp.lambdify((z1, z2), A, "numpy"); fB = sp.lambdify((z1, z2), B, "numpy")


def blocks_num(u, v):
    a, b = np.exp(2j * np.pi * u), np.exp(2j * np.pi * v)
    return np.array(fA(a, b), dtype=complex), np.array(fB(a, b), dtype=complex)


def slab_direct(Tn, fperp, N):
    """independent float slab (arcs_runner.slab_hamiltonian logic, open along a3): M[(a,L),(b,L+n3)] += t e^{2 pi i (u n1 + v n2)}, M^T block -conj, H = iM"""
    M = np.zeros((4 * N, 4 * N), dtype=complex)
    for (a, b, n, t) in Tn:
        ph = np.exp(2j * np.pi * (fperp[0] * n[0] + fperp[1] * n[1]))
        for L in range(N):
            L2 = L + n[2]
            if 0 <= L2 < N:
                M[4 * L + a, 4 * L2 + b] += t * ph
                M[4 * L2 + b, 4 * L + a] -= t * np.conj(ph)
    return 1j * M


Tn = [(a, b, n, float(t)) for (a, b, n, t) in terms_sym((1, 1, 1), kap_s)]
rng = np.random.default_rng(20261001)
worst = 0.0
for _ in range(20):
    u, v = rng.uniform(0, 1, 2)
    H = slab_direct(Tn, (u, v), 5); Af, Bf = blocks_num(u, v)
    for L in range(5):
        worst = max(worst, np.abs(H[4 * L:4 * L + 4, 4 * L:4 * L + 4] - Af).max())
    for L in range(4):
        worst = max(worst, np.abs(H[4 * L:4 * L + 4, 4 * L + 4:4 * L + 8] - Bf).max(), np.abs(H[4 * L + 4:4 * L + 8, 4 * L:4 * L + 4] - Bf.conj().T).max())
    for L in range(5):
        for L2 in range(5):
            if abs(L - L2) >= 2:
                worst = max(worst, np.abs(H[4 * L:4 * L + 4, 4 * L2:4 * L2 + 4]).max())
check("(1) exact blocks and rank structure of B", ok_off and ok_dag and nz == [(2, 0), (3, 0), (3, 1)] and ok_det and rankB == 2 and worst < 1e-12,
      f"offsets {{-1,0,1}}, H_(L,L-1) = B^dag and A Hermitian exact; B nonzero at {nz}, symbolic rank {rankB}, det B[2:4,0:2] = 4 kappa^2 (z1-1)(z2-1)/(z1 z2) (rank 1 on u=0 or v=0); "
      f"symbolic blocks vs independent float slab (20 points, N=5) max diff {worst:.1e}")

# ------------------------------------------------------------------------------------------------ (2) characteristic quartic and the real quadratic in x
a_, b_ = sp.symbols("a b")
Ssub = {z1: a_ ** 2, z2: b_ ** 2}
phi = [sp.Integer(1), a_, a_, a_ * b_]
Wm = sp.diag(*phi); Winv = sp.diag(*[sp.Integer(1) / x for x in phi]); s_ = a_ * b_
k = k_s
s2u = 2 * Su * Cu; s2v = 2 * Sv * Cv
Ap_h = sp.Matrix([[-k * s2u, 2 * sp.I * Cu, k * Su, 0], [-2 * sp.I * Cu, k * s2u, -sp.I, -k * Sv],
                  [k * Su, sp.I, -k * s2v, 2 * sp.I * Cv], [0, -k * Sv, -2 * sp.I * Cv, k * s2v]])
Bp_h = sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [k * Sv, 0, 0, 0], [-sp.I, -k * Su, 0, 0]])
rep_h = {Su: (a_ - 1 / a_) / (2 * sp.I), Cu: (a_ + 1 / a_) / 2, Sv: (b_ - 1 / b_) / (2 * sp.I), Cv: (b_ + 1 / b_) / 2}
dA = (Winv * A.subs(Ssub) * Wm - 2 * Ap_h.subs(rep_h)).applyfunc(sp.simplify)
dB = (Winv * B.subs(Ssub) * Wm * s_ - 2 * Bp_h.subs(rep_h)).applyfunc(sp.simplify)
ok_gauge = dA == sp.zeros(4, 4) and dB == sp.zeros(4, 4)
Hh = Bp_h.H / mu + Ap_h + mu * Bp_h
Q4 = sp.expand(sp.cancel(Hh.det(method="berkowitz")) * mu ** 2)
Q4p = sp.Poly(Q4, mu)
cf = [sp.expand(Q4p.coeff_monomial(mu ** j)) for j in range(5)]
X_, Y_ = Su ** 2, Sv ** 2
sg, gm = Su * Sv, Cu * Cv
r0c = K_s ** 2 * X_ * Y_
r1c = -2 * (gm * (4 * sg ** 2 * K_s ** 2 - 6 * (X_ + Y_) * K_s + 2) - sg * ((X_ + Y_) * K_s ** 2 + K_s))
r2c = 16 * gm ** 2 * (1 + K_s * X_) * (1 + K_s * Y_) - 8 * K_s * gm * sg * (K_s * (X_ + Y_) - 7) + (1 + K_s * (X_ + Y_)) ** 2 + 2 * K_s ** 2 * X_ * Y_
r0, r1, r2 = cf[4], cf[3], cf[2]
ok_pal = sp.expand(cf[0] - cf[4]) == 0 and sp.expand(cf[1] - cf[3]) == 0 and Q4p.degree() == 4
ok_closed = sp.expand(r0 - r0c) == 0 and red2(r1 - r1c) == 0 and red2(r2 - r2c) == 0
xx = mu + 1 / mu
ok_quad = sp.expand(Q4 - mu ** 2 * (r0 * (xx ** 2 - 2) + r1 * xx + r2)) == 0
# the ORIGINAL blocks: P(lambda) = lambda^2 det(B^dag/lambda + A + lambda B), lambda = s mu  ->  P/(s^2 mu^2) = 16 det Hh
Hl = dag(B) / lam + A + lam * B
Pl = sp.expand(sp.cancel(sp.expand((lam ** 2 * Hl).det(method="berkowitz")) / lam ** 6))
Ppoly = sp.Poly(Pl, lam)
c0_expect = 16 * kap_s ** 4 * (z1 - 1) ** 2 * (z2 - 1) ** 2
ok_P = Ppoly.degree() == 4 and sp.simplify(Ppoly.coeff_monomial(lam ** 0) - c0_expect) == 0 and sp.simplify(Ppoly.coeff_monomial(lam ** 4) - c0_expect / (z1 * z2) ** 2) == 0 \
    and sp.simplify(Ppoly.coeff_monomial(lam ** 3) - Ppoly.coeff_monomial(lam ** 1) / (z1 * z2)) == 0
Pmu = sp.expand(sp.cancel(Pl.subs(Ssub).subs(lam, a_ * b_ * mu) / (a_ ** 2 * b_ ** 2 * mu ** 2)))
Eexp = 16 * (r0 * (mu ** 2 + mu ** -2) + r1 * (mu + 1 / mu) + r2)
ok_orig = sp.cancel(sp.together((Pmu - Eexp.subs(rep_h)))) == 0
check("(2) bulk quartic = real quadratic in x = mu + 1/mu", ok_gauge and ok_pal and ok_closed and ok_quad and ok_P and ok_orig,
      "gauge psi=s^L e^{i phi}xi (s=e^{i pi(u+v)}) exact; P(lambda) degree 4 with c0 = 16k^4(z1-1)^2(z2-1)^2 = c4 (z1z2)^2, c3 = c1/(z1z2); P(s mu)/(s^2 mu^2) = 16 det Hh; "
      "det Hh*mu^2 = r0(mu^4+1)+r1(mu^3+mu)+r2 mu^2 = mu^2 [r0(x^2-2)+r1 x+r2] with closed forms r0 = K^2 X Y, r1, r2 (x=mu+1/mu, K=9/25)")

# ------------------------------------------------------------------------------------------------ (3) q-space reduction, eliminant, integer form, irreducibility
App = Hh[0:2, 0:2]; Apq = Hh[0:2, 2:4]; Aqp = Hh[2:4, 0:2]; Aqq = Hh[2:4, 2:4]
detApp = sp.factor(App.det())
Sig = (Aqq - Aqp * App.adjugate() * Apq / App.det()).applyfunc(sp.cancel)
Dn = 2 * Cu * (1 + K_s * Su ** 2)
n_ = sp.expand(sp.cancel(Sig[0, 1] * mu * Dn / sp.I)); g_ = sp.expand(sp.cancel(-Sig[0, 0] * mu * Dn / k_s))
n2, n1, n0 = [n_.coeff(mu, j) for j in (2, 1, 0)]; g1, g0 = g_.coeff(mu, 2), g_.coeff(mu, 1)
ok_g = sp.expand(g_.coeff(mu, 0) - g1) == 0 and sp.expand(n_ - n2 * mu ** 2 - n1 * mu - n0) == 0
n2c = K_s * Y_; n1c = 4 * (gm * (1 + K_s * X_) + K_s * sg); n0c = 3 * K_s * X_ - 1
g1c = Sv * (1 - K_s * X_); g0c = 4 * gm * Sv * (1 + K_s * X_) + Su * (3 - K_s * (X_ + Y_))
ok_ng = red2(n2 - n2c) == 0 and red2(n1 - n1c) == 0 and red2(n0 - n0c) == 0 and red2(g1 - g1c) == 0 and red2(g0 - g0c) == 0
ok_detApp = sp.expand(detApp - (-4 * Cu ** 2 * (1 + K_s * Su ** 2))) == 0
nbar = n_.subs(mu, 1 / mu)
ok_sig = sp.simplify(Sig[1, 1] + Sig[0, 0]) == 0 and sp.simplify(Sig[1, 0] - (-sp.I * mu * nbar) / Dn) == 0 and sp.simplify(Sig.det() * App.det() - Hh.det()) == 0
ok_id = red2(sp.expand(sp.cancel(K_s * g_ ** 2 + mu ** 2 * n_ * nbar - (1 + K_s * Su ** 2) * Q4))) == 0
# Eq1, Eq2 and the eliminant
a1_ = n0 - tau * g1; c1_ = n2 - tau * g1; b1_ = tau * g0 - n1
Eq1 = sp.expand(r1 * a1_ * c1_ + r0 * b1_ * (a1_ + c1_)); Eq2 = sp.expand(r2 * a1_ * c1_ - r0 * (a1_ ** 2 + b1_ ** 2 + c1_ ** 2))
P1 = sp.Poly(Eq1, tau); P2 = sp.Poly(Eq2, tau)
A1, B1, C1 = [P1.coeff_monomial(tau ** m) for m in (2, 1, 0)]; A2, B2, C2 = [P2.coeff_monomial(tau ** m) for m in (2, 1, 0)]
ok_C1 = red2(C1 + K_s * A1) == 0
ok_X0 = red2(A2 * C1 - A1 * C2) == 0
Yel = red2(A1 * B2 - A2 * B1); Zel = red2(B1 * C2 - B2 * C1)
ok_R = red2(Zel - K_s * Yel) == 0            # R = X^2 - Y Z = -Y Z = -K Y^2
a0e = 625 + 300 * Y_ + 27 * Y_ ** 2 - (750 + 108 * Y_) * X_ + 81 * X_ ** 2
b0e = 2500 - 300 * Y_ - (600 + 108 * Y_) * X_ - 540 * X_ ** 2
G625 = sp.expand(Su * a0e + Cu * Cv * Sv * b0e)
Ypq = to_pq(Yel)
fl = sp.factor_list(Ypq.as_expr())
fac = [(sp.Poly(f, pp, qq), m) for f, m in fl[1]]
dsig = sorted((degs(P) + (m,)) for P, m in fac)
Gint_pq = to_pq(G625)
Gf = [P for P, m in fac if degs(P) == (10, 8)]
Hf = [P for P, m in fac if degs(P) == (16, 10)]
ok_Gint = len(Gf) == 1 and sp.cancel(Gf[0].as_expr() / Gint_pq.as_expr()).is_number
Gfl = sp.factor_list(Gint_pq.as_expr())
ok_irred = len(Gfl[1]) == 1 and Gfl[1][0][1] == 1
# H = common-root factor of (n, g): factor of Res_mu(n,g)
Resng = sp.expand((n2 * g1 - g1 * n0) ** 2 - (n2 * g0 - g1 * n1) * (n1 * g1 - g0 * n0))
Rpq = to_pq(Resng)
Rfl = sp.factor_list(Rpq.as_expr())
Hr = [sp.Poly(f, pp, qq) for f, m in Rfl[1] if degs(sp.Poly(f, pp, qq)) == (16, 10)]
ok_H = len(Hf) == 1 and len(Hr) == 1 and sp.cancel(Hf[0].as_expr() / Hr[0].as_expr()).is_number
ok_sig_fac = dsig == [(0, 1, 3), (1, 0, 2), (10, 8, 1), (16, 10, 1)]
check("(3) eliminant Y = c S_u^2 S_v^3 H G', integer form 625 G' = S_u a0 + C_u C_v S_v b0 (irreducible)",
      ok_g and ok_ng and ok_detApp and ok_sig and ok_id and ok_C1 and ok_X0 and ok_R and ok_sig_fac and ok_Gint and ok_irred and ok_H,
      "det A_pp = -4 C_u^2 (1+KX); n, g closed forms; K g^2 + mu^2 n n~ = (1+KX) mu^2 det Hh; C1 = -K A1, A2 C1 = A1 C2, Z = K Y (R = -K Y^2); Y factors in (p,q)=(tan(pi u/2),tan(pi v/2)) as "
      f"p^2 q^3 * G'(deg {degs(Gf[0])}) * H(deg {degs(Hf[0])}); G' = const*(S_u a0 + C_u C_v S_v b0), irreducible over Q; H = factor of Res_mu(n,g)")

# ------------------------------------------------------------------------------------------------ (3') the line u = 1/2
cu2 = 1 - 2 * Su ** 2; su2 = 2 * Su * Cu; cv2 = 1 - 2 * Sv ** 2; sv2 = 2 * Sv * Cv
Pfull = sp.expand(su2 * a0e + (1 + cu2) / 2 * sv2 * b0e)
ok_P2 = red2(Pfull - 2 * Cu * G625) == 0
ok_line = sp.expand(Pfull.subs({Su: 1, Cu: 0})) == 0 and sp.expand(G625.subs({Su: 1, Cu: 0})) != 0
Q4u = sp.expand(Q4.subs({Su: 1, Cu: 0}))
ok_Q4u = sp.expand(Q4u - sp.expand(Aqp.subs({Su: 1, Cu: 0}).det() ** 2)) == 0 and App.subs({Su: 1, Cu: 0}) == sp.zeros(2, 2)
check("(3b) straight line u = 1/2 is the factor C_u of P", ok_P2 and ok_line and ok_Q4u,
      "P = s_u a0 + (1/2)(1+c_u) s_v b0 = 2 C_u (625 G') exactly, so P(u=1/2, v) = 0 for all v while G'(1/2, v) != 0; at u = 1/2: A_pp = 0 and Q4 = (det A_qp)^2 (all roots double, outside the generic theorem)")

# ------------------------------------------------------------------------------------------------ (4) closed form of Xi, Xi = F_tau(1) F_tau(-1)
n_p1 = n2 + n1 + n0; n_m1 = n2 - n1 + n0; g_p1 = 2 * g1 + g0; g_m1 = 2 * g1 - g0
Xi_expr = red2(n_p1 * n_m1 + K_s * g_p1 * g_m1)
KK, XX, YY = K_s, X_, Y_
Xi0 = (XX ** 3 * (-16 * KK ** 3 * YY ** 2 + 16 * KK ** 3 * YY - KK ** 3 - 16 * KK ** 2 * YY + 16 * KK ** 2)
       + XX ** 2 * (16 * KK ** 3 * YY ** 2 - 14 * KK ** 3 * YY - 32 * KK ** 2 * YY ** 2 + 48 * KK ** 2 * YY - KK ** 2 - 32 * KK * YY + 32 * KK)
       + XX * (-KK ** 3 * YY ** 2 + 32 * KK ** 2 * YY ** 2 - 44 * KK ** 2 * YY - 16 * KK * YY ** 2 + 48 * KK * YY - 47 * KK - 16 * YY + 16) + YY ** 2 * (KK ** 2 + 16 * KK) + YY * (16 - 14 * KK) - 15)
Xi_closed = Xi0 + Su * Cu * Sv * Cv * 8 * KK * (1 + KK * XX) * (KK * (XX + YY) - 7)
ok_xi = red2(Xi_expr - Xi_closed) == 0
Omega = sp.expand(B1 * g_p1 * g_m1 + A1 * (n_p1 * g_m1 + n_m1 * g_p1))
Q_om, R_om = sp.div(to_pq(Omega), Gint_pq)
ok_om = R_om.is_zero
# Xi for complex-x: Xi > 0 automatically (spot: Xi(0, 1/2) = (1+K)^2)
xi_00 = sp.expand(Xi_expr.subs({Su: 0, Cu: 1, Sv: 1, Cv: 0}))
check("(4) Xi = n(1)n(-1)+K g(1)g(-1): closed form; Xi = F_tau(1)F_tau(-1) on G' = 0", ok_xi and ok_om and xi_00 == (1 + K_s) ** 2,
      "Xi = Xi0(X,Y) + S_u C_u S_v C_v 8K(1+KX)(K(X+Y)-7) exact (K = 9/25); Omega = B1 g(1)g(-1) + A1 (n(1)g(-1)+n(-1)g(1)) is divisible by G' (so Xi = F_tau(1)F_tau(-1) for both roots tau of Eq1 where G' = 0); "
      f"Xi(0, 1/2) = (1+K)^2 = {float(xi_00):.4f}")

# ------------------------------------------------------------------------------------------------ (5) exact endpoint
Kx, Xs, ss, cs = sp.symbols("K X s c")
a_anti = 625 + 300 * Xs + 27 * Xs ** 2 - (750 + 108 * Xs) * Xs + 81 * Xs ** 2
b_anti = 2500 - 300 * Xs - (600 + 108 * Xs) * Xs - 540 * Xs ** 2
anti = sp.expand(a_anti - (1 - Xs) * b_anti)                # 625 G'(u, 1-u) / S_u
target = sp.expand(625 * (1 - 2 * K_s * Xs) * (4 * K_s * Xs ** 2 + 4 * (1 - K_s) * Xs - 3))
ok_anti = sp.expand(anti - target) == 0
cfam = sp.expand((4 * kap_s ** 2 * (1 - 2 * Xs) ** 2 - 2 * (1 - 2 * Xs) + 1 - 4 * kap_s ** 2 - 2) - (4 * K_s * Xs ** 2 + 4 * (1 - K_s) * Xs - 3))
ok_fam = cfam == 0
ideal = [ss ** 2 - Xs, cs ** 2 - (1 - Xs), 36 * Xs ** 2 + 64 * Xs - 75]
GB = sp.groebner(ideal, ss, cs, Xs, order="lex", domain=sp.QQ)
nodesub = {Su: ss, Sv: ss, Cu: cs, Cv: -cs}
red_node = lambda e: GB.reduce(sp.expand(e.subs(nodesub)))[1]
Qm2 = 2 * r0 - 2 * r1 + r2
vals = [red_node(Qm2), red_node(G625), red_node(n_m1), red_node(g_m1), red_node(Xi_expr)]
ok_node_alg = all(v == 0 for v in vals) and red_node(Q4.subs(mu, -1)) == 0
X0 = (7 * sp.sqrt(19) - 16) / 18
mp.mp.dps = 40
c0m = (25 - 7 * mp.sqrt(19)) / 9
u0m = mp.acos(c0m) / (2 * mp.pi)
ok_u0 = sp.simplify(36 * X0 ** 2 + 64 * X0 - 75) == 0 and abs(float(u0m) - 0.354913387) < 1e-9 and abs(sp.N(1 - 2 * X0, 30) - sp.N((25 - 7 * sp.sqrt(19)) / 9, 30)) < 1e-25
u0f = float(u0m); v0f = 1 - u0f
Af0, Bf0 = blocks_num(u0f, v0f)
lam1 = np.exp(1j * np.pi * (u0f + v0f)) * (-1.0)       # lambda = s mu, s = e^{i pi (u0+v0)} = -1, mu = -1
sv_node = np.linalg.svd(Bf0.conj().T / lam1 + Af0 + lam1 * Bf0, compute_uv=False)
check("(5) exact endpoint: node of family (i)", ok_anti and ok_fam and ok_node_alg and ok_u0 and abs(lam1 - 1) < 1e-12 and sv_node[-1] < 1e-12 and sv_node[-2] < 1e-12 and sv_node[1] > 0.1,
      f"625 G'(u,1-u) = 625 S_u (1-2KX)(4KX^2+4(1-K)X-3) exact (2nd factor = landed 4k^2c^2-2c+1-4k^2-2, c=1-2X); at X0=(7 sqrt19-16)/18 (cos 2pi u0=(25-7 sqrt19)/9, u0={u0f:.12f}, v0=1-u0): "
      f"Q(-2)=G'=n(-1)=g(-1)=Xi=0 exactly (Groebner reduction), mu=-1 => lambda=+1; float: A+B+B^dag at the node has singular values {sv_node[-2]:.1e}, {sv_node[-1]:.1e} (rank 2)")

# ------------------------------------------------------------------------------------------------ interval machinery
def ivfrac(fr):
    fr = Fraction(fr)
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def exact_iv(fr):
    return ivfrac(fr)


def hull(x, y):
    return iv.mpf([x.a, y.b])


class IPoly:
    """polynomial in (S_u, C_u, S_v, C_v) with exact rational coefficients (interval-enclosed), evaluated from precomputed power tables."""
    def __init__(self, expr=None, terms=None, pi_factor=False):
        if terms is None:
            P = sp.Poly(sp.expand(expr), Su, Cu, Sv, Cv)
            terms = [(e, Fraction(int(c.p), int(c.q))) for e, c in P.terms()]
        self.terms = terms; self.pi = pi_factor
        self.civ = [ivfrac(c) for _, c in terms]
        self.nmax = [max([e[t] for e, _ in terms] + [0]) for t in range(4)]
    def ev(self, T):
        tot = iv.mpf(0)
        for (e, _), c in zip(self.terms, self.civ):
            tot = tot + c * T[0][e[0]] * T[1][e[1]] * T[2][e[2]] * T[3][e[3]]
        return tot * iv.pi if self.pi else tot
    def deriv(self, which):
        acc = {}
        for (i, a, j, b), c in self.terms:
            if which == "u":
                if i: acc[(i - 1, a + 1, j, b)] = acc.get((i - 1, a + 1, j, b), 0) + c * i
                if a: acc[(i + 1, a - 1, j, b)] = acc.get((i + 1, a - 1, j, b), 0) - c * a
            else:
                if j: acc[(i, a, j - 1, b + 1)] = acc.get((i, a, j - 1, b + 1), 0) + c * j
                if b: acc[(i, a, j + 1, b - 1)] = acc.get((i, a, j + 1, b - 1), 0) - c * b
        return IPoly(terms=[(e, c) for e, c in acc.items() if c != 0], pi_factor=True)


Gp = IPoly(G625); dGu = Gp.deriv("u"); dGv = Gp.deriv("v")
Xi_p = IPoly(Xi_expr); dXu = Xi_p.deriv("u"); dXv = Xi_p.deriv("v")
R0p, R1p, R2p = IPoly(r0), IPoly(r1), IPoly(r2)
Rngp = IPoly(Resng)
_allp = [Gp, dGu, dGv, Xi_p, dXu, dXv, R0p, R1p, R2p, Rngp]
NS = max(max(p.nmax[0], p.nmax[2]) for p in _allp); NC = max(max(p.nmax[1], p.nmax[3]) for p in _allp)


def pows(x, n):
    L = [iv.mpf(1), x]
    for _ in range(n - 1):
        L.append(L[-1] * x)
    return L


def tab(U, V):
    su, cu_, sv, cv_ = iv.sin(iv.pi * U), iv.cos(iv.pi * U), iv.sin(iv.pi * V), iv.cos(iv.pi * V)
    return (pows(su, NS), pows(cu_, NC), pows(sv, NS), pows(cv_, NC))


def mid(U):
    return (U.a + U.b) / 2


def cen_u(P, dPu, U, v):
    c = mid(U)
    return P.ev(tab(c, v)) + dPu.ev(tab(U, v)) * (U - c)


def cen_uv(P, dPu, dPv, U, V, T=None):
    cu_, cv_ = mid(U), mid(V)
    if T is None:
        T = tab(U, V)
    return P.ev(tab(cu_, cv_)) + dPu.ev(T) * (U - cu_) + dPv.ev(T) * (V - cv_)


def no_unimodular(T):
    r0i, r1i, r2i = R0p.ev(T), R1p.ev(T), R2p.ev(T)
    if not (r0i.a > 0):
        return False
    D = r1i * r1i - 4 * r0i * (r2i - 2 * r0i)
    if D.b < 0:
        return True
    xv = -r1i / (2 * r0i)
    if D.a > 0:
        s = iv.sqrt(D) / (2 * r0i)
        return all((x.a > 2 or x.b < -2) for x in (xv + s, xv - s))
    s = iv.sqrt(iv.mpf(D.b)) / (2 * r0i)
    return ((xv - s).a > 2) or ((xv + s).b < -2)


# float helpers
def Gf(u, v):
    Su_, Cu_, Sv_, Cv_ = np.sin(np.pi * u), np.cos(np.pi * u), np.sin(np.pi * v), np.cos(np.pi * v)
    X1, Y1 = Su_ ** 2, Sv_ ** 2
    return Su_ * (625 + 300 * Y1 + 27 * Y1 ** 2 - (750 + 108 * Y1) * X1 + 81 * X1 ** 2) + Cu_ * Cv_ * Sv_ * (2500 - 300 * Y1 - (600 + 108 * Y1) * X1 - 540 * X1 ** 2)


def bisect_root(f, lo, hi, it=70):
    flo = f(lo)
    for _ in range(it):
        m = 0.5 * (lo + hi); fm = f(m)
        if (fm > 0) == (flo > 0):
            lo, flo = m, fm
        else:
            hi = m
    return 0.5 * (lo + hi)


def vroot(u, vg):
    lo, hi = vg - 0.04, vg + 0.04
    f = lambda v: Gf(u, v)
    if f(lo) * f(hi) > 0:
        lo, hi = 0.45, 0.7
    return bisect_root(f, lo, hi)


# ------------------------------------------------------------------------------------------------ (6) corridor
def cert_box(Ua, Ub, Vlo, Vhi, window=False):
    uA, uB, vA, vB = exact_iv(Ua), exact_iv(Ub), exact_iv(Vlo), exact_iv(Vhi)
    U = hull(uA, uB); V = hull(vA, vB)
    T = tab(U, V)
    glo = cen_u(Gp, dGu, U, vA); ghi = cen_u(Gp, dGu, U, vB)
    sgn_ok = (glo.b < 0 and ghi.a > 0) or (glo.a > 0 and ghi.b < 0)
    dv = dGv.ev(T); mono = (dv.a > 0) or (dv.b < 0)
    if window:
        if not (sgn_ok and mono):
            return False, None
        dXi = dXu.ev(T) - dXv.ev(T) * dGu.ev(T) / dv
        return bool(dXi.b < 0), float(dXi.b)
    xi = cen_uv(Xi_p, dXu, dXv, U, V, T)
    rn = Rngp.ev(T)
    ok = sgn_ok and mono and bool(xi.a > 0) and ((rn.a > 0) or (rn.b < 0)) and no_unimodular(T)
    return ok, float(xi.a)


def run_corridor(ulo, uhi, nseg, window=False, extra_edges=(), maxdepth=14):
    boxes, fails = [], []
    def recurse(ua, ub, vg, depth):
        um = float((ua + ub) / 2)
        vc = vroot(um, vg) if not window else bisect_root(lambda v: Gf(um, v), vg - 0.03, vg + 0.03)
        h = 1e-7
        gu = (Gf(um + h, vc) - Gf(um - h, vc)) / (2 * h); gv = (Gf(um, vc + h) - Gf(um, vc - h)) / (2 * h)
        slope = abs(gu / gv); width = float(ub - ua)
        info = None
        for mult in (10.0, 3.0, 1.0):
            w = mult * (slope + 0.05) * width / 2 + 1e-9
            Vlo = Fraction(vc - w).limit_denominator(10 ** 13); Vhi = Fraction(vc + w).limit_denominator(10 ** 13)
            ok, info = cert_box(ua, ub, Vlo, Vhi, window)
            if ok:
                boxes.append((ua, ub, Vlo, Vhi, info)); return vc
        if depth >= maxdepth:
            fails.append((float(ua), float(ub))); return vc
        m = (ua + ub) / 2
        recurse(ua, m, vc, depth + 1)
        return recurse(m, ub, vc, depth + 1)
    edges = sorted(set([ulo + (uhi - ulo) * i / nseg for i in range(nseg + 1)] + list(extra_edges)))
    vg = vroot(float(ulo), 0.505) if not window else bisect_root(lambda v: Gf(float(ulo), v), 0.55, 0.7)
    for i in range(len(edges) - 1):
        vg = recurse(edges[i], edges[i + 1], vg, 0)
    return boxes, fails


def joints_ok(bl):
    bad = 0
    for i in range(len(bl) - 1):
        a, b = bl[i], bl[i + 1]
        if a[1] != b[0]:
            bad += 1; continue
        lo = max(a[2], b[2]); hi = min(a[3], b[3])
        if lo > hi:
            bad += 1; continue
        ub = exact_iv(a[1])
        glo = Gp.ev(tab(ub, exact_iv(lo))); ghi = Gp.ev(tab(ub, exact_iv(hi)))
        if not ((glo.b < 0 and ghi.a > 0) or (glo.a > 0 and ghi.b < 0)):
            bad += 1
    return bad


t6 = time.time()
mainb, mainf = run_corridor(Fraction(1, 1000), Fraction(34, 100), 34)
extb, extf = run_corridor(Fraction(1, 100000), Fraction(1, 1000), 4)
allb = sorted(extb + mainb, key=lambda x: x[0])
bad6 = joints_ok(allb)
minxi = min(b[4] for b in allb)
contig = all(allb[i][1] == allb[i + 1][0] for i in range(len(allb) - 1)) and allb[0][0] == Fraction(1, 100000) and allb[-1][1] == Fraction(34, 100)
check("(6) interval corridor u in [1e-5, 0.34]: arc = graph v = f(u), Xi > 0, no unimodular root", len(mainf) == 0 and len(extf) == 0 and bad6 == 0 and contig and minxi > 0.1,
      f"{len(allb)} boxes ({len(extb)} on [1e-5,1e-3], {len(mainb)} on [1e-3,0.34]), 0 failures, contiguous, {bad6} of {len(allb)-1} joints fail the common-root test; min certified lower bound of Xi = {minxi:.4f}; "
      f"Res_mu(n,g) != 0, x-roots non-real or |x|>2 on every box ({time.time()-t6:.0f} s)")

# ------------------------------------------------------------------------------------------------ (7) node window
c0i = (iv.mpf(25) - 7 * iv.sqrt(iv.mpf(19))) / 9
cosv = lambda fr: iv.cos(2 * iv.pi * exact_iv(fr))
lo_, hi_ = Fraction(35, 100), Fraction(36, 100)
assert cosv(lo_).a > c0i.b and cosv(hi_).b < c0i.a
for _ in range(60):
    m_ = (lo_ + hi_) / 2; cm = cosv(m_)
    if cm.a > c0i.b:
        lo_ = m_
    elif cm.b < c0i.a:
        hi_ = m_
    else:
        break
u0lo, u0hi = lo_, hi_
wb, wf = run_corridor(Fraction(34, 100), Fraction(37, 100), 30, window=True, extra_edges=(u0lo, u0hi))
cont = [b for b in wb if b[0] <= u0lo and b[1] >= u0hi]
v0lo, v0hi = 1 - u0hi, 1 - u0lo
node_in = len(cont) >= 1 and cont[0][2] <= v0lo and v0hi <= cont[0][3]
dmax = max(b[4] for b in wb) if wb else 1.0
allc = sorted(mainb + wb, key=lambda x: x[0])
bad7 = joints_ok(allc)
check("(7) node window [0.34, 0.37]: graph exists, dXi/du < 0 along the curve, node on it", len(wf) == 0 and len(wb) > 0 and dmax < 0 and node_in and bad7 == 0,
      f"{len(wb)} boxes, 0 failures; certified upper bound of dXi/du|curve over the window = {dmax:.4f} < 0; u0 enclosed in [{float(u0lo):.15f}, {float(u0hi):.15f}] (width {float(u0hi-u0lo):.1e}); "
      f"node (u0, 1-u0) inside the V-bracket of its box; {bad7} failing joints (incl. the joint with the main corridor)")

# ------------------------------------------------------------------------------------------------ (8) branch and bound
import bisect
corr = allc
us_ = [b[0] for b in corr]


def in_corridor(ua, ub, va, vb):
    i = bisect.bisect_right(us_, ua) - 1
    if i < 0 or not (corr[i][0] <= ua < corr[i][1]):
        return False
    j = i
    while True:
        b = corr[j]
        if not (b[2] <= va and vb <= b[3]):
            return False
        if ub <= b[1]:
            return True
        j += 1
        if j >= len(corr) or corr[j][0] != b[1]:
            return False


cleared = {"G": 0, "Xi": 0, "corridor": 0}
undec = []
t8 = time.time()


def bnb(ua, ub, va, vb, depth, maxdepth=34):
    uA, uB, vA, vB = exact_iv(ua), exact_iv(ub), exact_iv(va), exact_iv(vb)
    U = hull(uA, uB); V = hull(vA, vB)
    T = tab(U, V)
    g = Gp.ev(T)
    if g.a > 0 or g.b < 0:
        cleared["G"] += 1; return
    g = cen_uv(Gp, dGu, dGv, U, V, T)
    if g.a > 0 or g.b < 0:
        cleared["G"] += 1; return
    xi = Xi_p.ev(T)
    if xi.b < 0:
        cleared["Xi"] += 1; return
    xi = cen_uv(Xi_p, dXu, dXv, U, V, T)
    if xi.b < 0:
        cleared["Xi"] += 1; return
    if in_corridor(ua, ub, va, vb):
        cleared["corridor"] += 1; return
    if depth >= maxdepth:
        undec.append((float(ua), float(ub), float(va), float(vb))); return
    jj = bisect.bisect_right(us_, ua)
    if jj < len(us_) and us_[jj] < ub:
        m = us_[jj]; bnb(ua, m, va, vb, depth, maxdepth); bnb(m, ub, va, vb, depth, maxdepth); return
    if (ub - ua) >= (vb - va):
        m = (ua + ub) / 2; bnb(ua, m, va, vb, depth + 1, maxdepth); bnb(m, ub, va, vb, depth + 1, maxdepth)
    else:
        m = (va + vb) / 2; bnb(ua, ub, va, m, depth + 1, maxdepth); bnb(ua, ub, m, vb, depth + 1, maxdepth)


UA = [Fraction(1, 1000) + (Fraction(499, 1000) - Fraction(1, 1000)) * i / 16 for i in range(17)]
VA = [Fraction(i, 16) for i in range(17)]
for i in range(16):
    for j in range(16):
        bnb(UA[i], UA[i + 1], VA[j], VA[j + 1], 0)
check("(8) branch-and-bound: {G' = 0, Xi >= 0} lies in the corridor for u in [0.001, 0.499], v in [0, 1]", len(undec) == 0,
      f"cleared by G' != 0: {cleared['G']}, by Xi < 0: {cleared['Xi']}, inside the certified corridor: {cleared['corridor']}; undecided: {len(undec)} ({time.time()-t8:.0f} s)")

# ------------------------------------------------------------------------------------------------ (9) float cross-check
MG, NL = 80, 40
fr0 = sp.lambdify((Su, Cu, Sv, Cv), r0, "numpy"); fr1 = sp.lambdify((Su, Cu, Sv, Cv), r1, "numpy"); fr2 = sp.lambdify((Su, Cu, Sv, Cv), r2, "numpy")
fXi = sp.lambdify((Su, Cu, Sv, Cv), Xi_expr, "numpy")
Id = np.eye(NL); Up = np.eye(NL, k=1)
tt = np.zeros((MG, MG))
t9 = time.time()
for i in range(MG):
    for j in range(MG):
        Af, Bf = blocks_num((i + 0.5) / MG, (j + 0.5) / MG)
        H = np.kron(Id, Af) + np.kron(Up, Bf) + np.kron(Up.T, Bf.conj().T)
        w, V = np.linalg.eigh(H)
        pw = (np.abs(V[:, w < 0]) ** 2).sum(axis=1).reshape(NL, 4).sum(axis=1)
        tt[i, j] = pw[:NL // 2].sum()


def epoint(i, j, code, t):
    return (i + 0.5) / MG + (t / MG if code == "u" else 0.0), (j + 0.5) / MG + (t / MG if code == "v" else 0.0)


def qangle(u, v):
    Su_, Cu_, Sv_, Cv_ = np.sin(np.pi * u), np.cos(np.pi * u), np.sin(np.pi * v), np.cos(np.pi * v)
    c0_, c1_, c2_ = float(fr0(Su_, Cu_, Sv_, Cv_)), float(fr1(Su_, Cu_, Sv_, Cv_)), float(fr2(Su_, Cu_, Sv_, Cv_))
    mus = np.roots([c0_, c1_, c2_, c1_, c0_]); ins = mus[np.abs(mus) < 1]
    if len(ins) != 2 or np.abs(ins).min() < 1e-9:
        return 2.0
    Af, Bf = blocks_num(u, v); s = np.exp(1j * np.pi * (u + v)); qs = []
    for m_ in ins:
        l_ = s * m_
        Vh = np.linalg.svd(Bf.conj().T / l_ + Af + l_ * Bf)[2]
        q = Vh[-1].conj()[2:4]; nq = np.linalg.norm(q)
        qs.append(q / nq if nq > 1e-14 else q * 0)
    return abs(qs[0][0] * qs[1][1] - qs[0][1] * qs[1][0])


flag, signch, xipos, direct = set(), set(), set(), set()
for i in range(MG):
    for j in range(MG):
        for code, (di, dj) in (("v", (0, 1)), ("u", (1, 0))):
            if abs(tt[(i + di) % MG, (j + dj) % MG] - tt[i, j]) > 0.5:
                flag.add((i, j, code))
            f2 = lambda t, i=i, j=j, code=code: Gf(*epoint(i, j, code, t))        # unwrapped coordinates (G' is odd under u -> u+1)
            if f2(0.0) * f2(1.0) < 0:
                signch.add((i, j, code))
                t = bisect_root(f2, 0.0, 1.0, 50)
                u, v = epoint(i, j, code, t); u %= 1.0; v %= 1.0
                Su_, Cu_, Sv_, Cv_ = np.sin(np.pi * u), np.cos(np.pi * u), np.sin(np.pi * v), np.cos(np.pi * v)
                if fXi(Su_, Cu_, Sv_, Cv_) > 0:
                    xipos.add((i, j, code))
                if qangle(u, v) < 1e-6:
                    direct.add((i, j, code))
umid = lambda e: ((e[0] + 0.5) / MG + (0.5 / MG if e[2] == "u" else 0.0)) % 1.0
fl_arc = {e for e in flag if abs(umid(e) - 0.5) > 0.02}
n_line = len(flag) - len(fl_arc)
check("(9) float cross-check vs the N = 40 finite-slab top contour (80 x 80 grid)", fl_arc == xipos == direct and len(fl_arc) == 80 and n_line == 80,
      f"flagged top-arc edges {len(fl_arc)} (+{n_line} on the u = 1/2 line); G' sign-change edges {len(signch)}; with Xi > 0: {len(xipos)}; direct 4x4 null-vector criterion: {len(direct)}; "
      f"the three sets are equal: {fl_arc == xipos == direct} ({time.time()-t9:.0f} s)")

# ------------------------------------------------------------------------------------------------ summary
npass = sum(RESULTS); nfail = len(RESULTS) - npass
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_mb = rss / 1e6 if sys.platform == "darwin" else rss / 1e3
print(f"runtime {time.time()-T0:.0f} s, peak RSS {rss_mb:.0f} MB")
print(f"TOTAL: PASS={npass} FAIL={nfail}")

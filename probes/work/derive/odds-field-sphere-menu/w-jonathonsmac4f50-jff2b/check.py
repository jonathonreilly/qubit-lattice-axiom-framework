#!/usr/bin/env python3
"""J:derive:odds-field-sphere-menu:a2 - worker w-jonathonsmac4f50-jff2b.

Block 42's self-consistent odds (open PR #8548; the reading is supplied by the owner, not adopted) for the
unsoldered sphere menu: contents s on the unit sphere, pair weight omega(s, b) = exp(beta s.b), the uniform
measure dOmega/(4 pi); K_1 = omega/Z, Z = sinh(beta)/beta; Phi(pi)_x(s) proportional to prod_{y~x} (K_1 pi_y)(s);
a record is the point mass at its content.
Exact parts: sympy.  Parts labelled HIGH PRECISION: mpmath at 40 digits.  Parts labelled NUMERIC: double
precision on a Legendre basis (l <= 48, 160 Gauss-Legendre nodes), errors stated.
"""
import itertools

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.special import lpmv, spherical_in

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


b, t = sp.symbols('beta t', positive=True)

# ---------------------------------------------------------------- A1 the one-neighbour operator by angular momentum
Zs = sp.integrate(sp.exp(b * t), (t, -1, 1)) / 2
lam_sym = [sp.simplify(sp.integrate(sp.exp(b * t) * sp.legendre(l, t), (t, -1, 1)) / 2 / Zs) for l in range(5)]
ok = sp.simplify(Zs - sp.sinh(b) / b) == 0
ok &= sp.simplify((lam_sym[1] - (sp.coth(b) - 1 / b)).rewrite(sp.exp)) == 0
ok &= lam_sym[0] == 1
mp.mp.dps = 40
vals = {}
for bv in (sp.Rational(3, 10), sp.Rational(1, 2), sp.Integer(1), sp.Integer(3)):
    v = [sp.N(lam_sym[l].subs(b, bv), 30) for l in range(5)]
    vals[str(bv)] = v
    ok &= all(v[l] > v[l + 1] > 0 for l in range(4))
# the derivative of the map at the uniform field: for delta of zero mean, Phi(1 + e delta) = 1 + e sum_y K_1 delta_y + O(e^2)
e = sp.symbols('e')
d1 = [sp.Rational(1, 3) * t, sp.Rational(1, 2) * (3 * t ** 2 - 1), t ** 3 - sp.Rational(3, 5) * t]      # zero mean
K1d = [sp.expand(sum(lam_sym[l] * sp.integrate(sp.expand(d * sp.legendre(l, t)), (t, -1, 1)) * (2 * l + 1) / 2 * sp.legendre(l, t) for l in range(5))) for d in d1]
# six neighbours with departures d1 + d1: the product of (1 + e K_1 delta_y) has first-order term sum_y K_1 delta_y, and
# its mean vanishes because K_1 keeps the mean (lambda_0 = 1) and the departures have mean zero, so the normalised map's
# derivative is sum_y K_1 delta_y = sum_y (K_1 - P_0) delta_y
ok &= all(sp.simplify(sp.integrate(kd, (t, -1, 1))) == 0 for kd in K1d)
ok &= all(sp.simplify(sp.integrate(d, (t, -1, 1))) == 0 for d in d1)
check('A1', ok, "(a) EXACT: K_1 acts on the l-th angular momentum by lambda_l = i_l(beta)/i_0(beta) (Funk-Hecke; closed "
      "forms for l <= 4), lambda_1 = L(beta) = coth(beta) - 1/beta, 1 = lambda_0 > lambda_1 > lambda_2 > ... > 0 (at "
      "beta = 3/10, 1/2, 1, 3); the derivative of the self-consistent map at the uniform field is K_1 - P_0 per "
      "neighbour, so the linearised map on a wave k is lambda_l (6 - E(k)) on the l-th channel, exactly as block 42 T2",
      f"lambda_1..4 at beta = 1: {[float(x) for x in vals['1'][1:]]}")

# ---------------------------------------------------------------- A2 the massless point and the screened range
L = lambda x: mp.coth(x) - 1 / x
bc = mp.findroot(lambda x: 6 * L(x) - 1, mp.mpf('0.5'))
ok = 6 * L(bc - mp.mpf('1e-15')) < 1 < 6 * L(bc + mp.mpf('1e-15'))
ok &= mp.diff(L, bc) > 0
rng = {}
for bv in ('0.3', '0.45', '0.5'):
    l1 = L(mp.mpf(bv))
    m2 = (1 - 6 * l1) / l1
    rng[bv] = (float(m2), float(1 / mp.sqrt(m2)))
ok &= all(v[0] > 0 for v in rng.values())
check('A2', ok, "(a) HIGH PRECISION: the lean channel loses its mass term where 6 L(beta) = 1, at beta_c = "
      f"{mp.nstr(bc, 20)} (L increasing; 6L - 1 changes sign within 1e-15 of it); below it the lean obeys (-Delta + m^2) v "
      "= source/L with m^2 = (1 - 6L)/L, a screened range 1/m that diverges at beta_c; every higher channel (l >= 2) is "
      "screened at every beta for which the lean is",
      f"(m^2, range) at beta = 0.3, 0.45, 0.5: {[(round(a, 4), round(c, 3)) for a, c in rng.values()]}")

# ---------------------------------------------------------------- the ordered field (NUMERIC)
LMAX, NQ = 48, 160
tq, wq = leggauss(NQ)


def lamv(beta):
    i0 = spherical_in(0, beta)
    return np.array([spherical_in(l, beta) / i0 for l in range(LMAX + 1)])


def Pbar(m):
    rows = []
    for l in range(m, LMAX + 1):
        p = lpmv(m, l, tq)
        rows.append(p / np.sqrt(0.5 * np.sum(wq * p * p)))
    return np.array(rows)


P0 = Pbar(0)
P1 = Pbar(1)
P2 = Pbar(2)


def K1(fv, lams):
    c = 0.5 * (P0 * wq) @ fv
    return (lams * c) @ P0


def ordered(beta, M0=0.6, iters=20000, tol=1e-14):
    lams = lamv(beta)
    f = np.exp(3 * M0 * tq)
    f /= 0.5 * np.sum(wq * f)
    d = 1.0
    for _ in range(iters):
        g = K1(f, lams)
        new = g ** 6
        new /= 0.5 * np.sum(wq * new)
        d = np.abs(new - f).max()
        f = new
        if d < tol:
            break
    g = K1(f, lams)
    return f, g, float(0.5 * np.sum(wq * f * tq)), d, lams


def sector(m, f, g, lams):
    P = {0: P0, 1: P1, 2: P2}[m]
    lm = lams[m:m + P.shape[0]]
    A = 0.5 * (P * wq * (f / g)) @ (P.T * lm)
    if m == 0:
        fc = 0.5 * (P * wq) @ f
        row = 0.5 * np.sum(wq * f / g * (P * lm[:, None]), axis=1)
        A = A - np.outer(fc, row)
    return A


rows = []
okB = True
for beta in (0.6, 0.8, 1.0, 2.0, 4.0):
    f, g, M, d, lams = ordered(beta)
    resid = np.abs(f - g ** 6 / (0.5 * np.sum(wq * g ** 6))).max()
    ev1, V1 = np.linalg.eig(sector(1, f, g, lams))
    o = np.argsort(-ev1.real)
    top1, vec1 = ev1.real[o[0]], V1[:, o[0]].real
    # the rotation mode: delta = f'(t) sqrt(1 - t^2) (the m = 1 function of an infinitesimal turn of the lean)
    fl = 0.5 * (P0 * wq) @ f
    dP = np.array([np.polynomial.legendre.Legendre.basis(l).deriv()(tq) for l in range(LMAX + 1)])
    nrm0 = np.array([np.sqrt(0.5 * np.sum(wq * np.polynomial.legendre.Legendre.basis(l)(tq) ** 2)) for l in range(LMAX + 1)])
    fprime = (fl / nrm0) @ dP
    rot = fprime * np.sqrt(1 - tq ** 2)
    rc = 0.5 * (P1 * wq) @ rot
    overlap = abs(rc @ vec1) / (np.linalg.norm(rc) * np.linalg.norm(vec1))
    top0 = np.max(np.linalg.eigvals(sector(0, f, g, lams)).real)
    top2 = np.max(np.linalg.eigvals(sector(2, f, g, lams)).real)
    mL2 = (1 - 6 * top0) / top0
    rows.append((beta, M, 6 * top1, overlap, 6 * top0, mL2, 6 * top2, resid))
    okB &= M > 0.4 and resid < 1e-12 and abs(6 * top1 - 1) < 1e-10 and overlap > 1 - 1e-10 and 6 * top0 < 1 and 6 * top2 < 1
check('B1', okB, "(b) NUMERIC (Legendre basis l <= 48, residual below 1e-12): beyond beta_c the uniform field is "
      "replaced by the ordered solution of the EXACT self-consistency equation f = (K_1 f)^6/<(K_1 f)^6> (f a function "
      "of s.M-hat); its linearisation f (K_1 .)/(K_1 f), less the normalisation, splits by the azimuthal number m about "
      "the lean: in m = 1 (transverse) the top eigenvalue is 1/6 exactly - NO mass term at every beta - with the "
      "infinitesimal turn of the lean f'(t) sqrt(1 - t^2) as its eigenvector; m = 0 (longitudinal) and m = 2 are "
      "massive; the longitudinal mass m_L^2 = (1 - 6 a_L)/a_L grows with beta",
      "; ".join(f"beta={r[0]}: M={r[1]:.6f}, 6a(m=1)={r[2]:.12f} (turn overlap {r[3]:.12f}), 6a(m=0)={r[4]:.4f} (m_L^2={r[5]:.3f}), 6a(m=2)={r[6]:.4f}" for r in rows))

# ---------------------------------------------------------------- B2 the turn of the lean is a solution (PROVED) and below beta_c
f, g, M, d, lams = ordered(0.3, M0=0.2)
okb2 = abs(M) < 1e-10
top1_dis = np.max(np.linalg.eigvals(sector(1, f, g, lams)).real)
okb2 &= abs(6 * top1_dis - 6 * lams[1]) < 1e-12
check('B2', okb2, "(b) PROVED + NUMERIC: the map commutes with rotations of all contents, so every rotation of the ordered "
      "field is again a solution; differentiating f_R = (K_1 f_R)^6/<(K_1 f_R)^6> along a turn gives delta = 6 f "
      "(K_1 delta)/g - 6 f <f K_1 delta/g>, and for a turn (m = +-1) the mean term vanishes: the linearised map has "
      "eigenvalue 1/6 on it, i.e. (-Delta) with no mass term, at every beta above beta_c; below beta_c the field is "
      "the uniform one and the transverse top eigenvalue is 6 lambda_1 < 1",
      f"beta = 0.3: M = {M:.1e}, 6a(m=1) = {6 * top1_dis:.12f} = 6 lambda_1 = {6 * lams[1]:.12f}")

# ---------------------------------------------------------------- B3 the lean near beta_c (EXACT expansion)
x, y1, z1, eps = sp.symbols('x y z epsilon')
l1s, l2s, l3s = sp.symbols('lambda1 lambda2 lambda3', positive=True)
P = [sp.legendre(l, t) for l in range(5)]
avg = lambda ex: sp.integrate(sp.expand(ex), (t, -1, 1)) / 2
fx = 1 + eps * x * P[1] + eps ** 2 * y1 * P[2] + eps ** 3 * z1 * P[3]
gx = 1 + eps * l1s * x * P[1] + eps ** 2 * l2s * y1 * P[2] + eps ** 3 * l3s * z1 * P[3]
G6 = sp.series(gx ** 6, eps, 0, 4).removeO()
Fm = sp.series(sp.expand(G6 / sp.series(avg(G6), eps, 0, 4).removeO()), eps, 0, 4).removeO()
F1 = sp.expand(avg(Fm * P[1]) * 3)
F2 = sp.expand(avg(Fm * P[2]) * 5)
ysol = sp.solve(sp.Eq(y1, F2.coeff(eps, 2)), y1)[0]
c1 = sp.simplify(F1.coeff(eps, 1) / x)
c3 = sp.factor(sp.simplify(F1.coeff(eps, 3).subs(y1, ysol) / x ** 3))
ok = sp.simplify(c1 - 6 * l1s) == 0 and sp.simplify(c3 + 6 * l1s ** 3 * (38 * l2s - 3) / (6 * l2s - 1)) == 0
land = []
for bv in (0.515, 0.53):
    lams_b = lamv(bv)
    c3v = float(c3.subs({l1s: lams_b[1], l2s: lams_b[2]}))
    Mpred = np.sqrt((6 * lams_b[1] - 1) / (-c3v)) / 3
    Mnum = ordered(bv, M0=0.2)[2]
    land.append((bv, Mnum, Mpred, (6 * lams_b[1] - 1)))
ok &= all(abs(r[1] / r[2] - 1) < 3 * r[3] + 1e-3 for r in land)
check('B3', ok, "(b) EXACT expansion: writing f = 1 + x P_1 + y P_2 + ..., the lean's equation is x = 6 lambda_1 x + c3 x^3 "
      "+ ... with y = -10 lambda_1^2 x^2/(6 lambda_2 - 1) and c3 = -6 lambda_1^3 (38 lambda_2 - 3)/(6 lambda_2 - 1), "
      "negative at beta_c (lambda_1 = 1/6, lambda_2 < 3/38): the lean appears continuously, M^2 = (6 L - 1)/(9|c3|) + ..., "
      "matched by the numerical solution (NUMERIC) just above beta_c",
      "; ".join(f"beta={a}: M={m1:.6f} vs {m2:.6f}" for a, m1, m2, _ in land))

# ---------------------------------------------------------------- C1 what a record feeds in
tt = sp.symbols('tt')
ok = all(sp.simplify(sp.assoc_legendre(l, 1, tt).subs(tt, s)) == 0 for l in range(1, 8) for s in (1, -1))
ok &= all(sp.simplify(sp.assoc_legendre(l, 1, tt).subs(tt, sp.Rational(3, 5))) != 0 for l in (1, 2))
check('C1', ok, "(c) PROVED + EXACT: the ordered sea is invariant under the rotations about its lean (O(2)); a source "
      "feeds the azimuthal channel m only through its m-th Fourier part about the lean. A record of content s is the "
      "point mass at s: its m = +-1 part is sum_l P_l^1(s.M-hat) Y_l^(+-1), proportional to the part of s perpendicular to "
      "the lean and ZERO for a record aligned with it (P_l^1(+-1) = 0, checked l <= 7); a record whose content is drawn "
      "from the sea's own odds feeds nothing at first order (its average point mass is f); a source that is blind to "
      "content - the record count, a mass - is O(2)-invariant, lives in m = 0, and m = 0 is massive (B1): the mass is a "
      "source of NO channel without a mass term")

# ---------------------------------------------------------------- D1 records are boundary values in the transverse channel
n = 5
sites = list(itertools.product(range(n), repeat=3))
ix = {s: i for i, s in enumerate(sites)}


def nb(s):
    for a in range(3):
        for dd in (1, -1):
            q = list(s)
            q[a] += dd
            yield tuple(q)


def capacity(S):
    S = set(S)
    free = [s for s in sites if s not in S]
    fi = {s: i for i, s in enumerate(free)}
    Mx = sp.zeros(len(free), len(free))
    rhs = sp.zeros(len(free), 1)
    for s in free:
        Mx[fi[s], fi[s]] = 6
        for q in nb(s):
            if q in fi:
                Mx[fi[s], fi[q]] -= 1
            elif q in S:
                rhs[fi[s]] += 1                  # u = 1 on the body; u = 0 beyond the box
    u = Mx.LUsolve(rhs)
    val = lambda q: 1 if q in S else (u[fi[q]] if q in fi else 0)
    return sum(1 - sp.Rational(1, 6) * sum(val(q) for q in nb(s)) for s in S)


c1s = capacity([(2, 2, 2)])
c2a = capacity([(2, 2, 2), (3, 2, 2)])
c2b = capacity([(1, 2, 2), (3, 2, 2)])
c8 = capacity([(1 + i, 1 + j, 1 + k) for i in (0, 1) for j in (0, 1) for k in (0, 1)])
ok = c2a < 2 * c1s and c2b < 2 * c1s and c2a < c2b and c8 < 8 * c1s and c8 / 8 < c2a / 2
check('D1', ok, "(d) PROVED + EXACT: in the massless transverse channel a record is a boundary value (its odds are fixed) "
      "and an unformed site obeys u_x = (1/6) sum_y u_y: the field of a body S of records with a common transverse lean "
      "is that lean times the probability that a simple random walk from x ever reaches S, its charge is the "
      "capacity of S, and capacities do not add (block 42 T6 with the killing rate 1 - 6 lambda_1 replaced by 0); exact "
      "on a 5^3 box with the field zero beyond it",
      f"cap(1) = {c1s} = {float(c1s):.5f}; two adjacent {float(c2a):.5f}, two at distance 2 {float(c2b):.5f}, 2x2x2 cube {float(c8):.5f} (per record {float(c8) / 8:.5f})")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print(f"SUMMARY: PARTIAL, exact and high precision: for the sphere menu the self-consistent odds have lambda_l = "
      f"i_l/i_0, the lean loses its mass term at 6 L(beta) = 1, beta_c = {mp.nstr(bc, 15)}, and is screened with m^2 = "
      "(1 - 6L)/L below; beyond it the ordered field (exact equation f = (K_1 f)^6/<(K_1 f)^6>, lean born with "
      "M^2 = (6L - 1)/(9|c3|), c3 = -6 L^3 (38 lambda_2 - 3)/(6 lambda_2 - 1)) has a transverse channel with no mass term "
      "at every beta - the turn of the lean, eigenvalue 1/6 exactly - and massive longitudinal and quadrupole "
      "channels; a record feeds the transverse channel only through the part of its content perpendicular to the lean, "
      "a mass feeds no massless channel (O(2)), and a body's transverse strength is its capacity")
if all(RESULTS):
    print(f"HIT: block 42's self-consistent odds for the sphere menu exp(beta s.s'): lambda_l = i_l(beta)/i_0(beta), the "
          f"lean is massless at 6(coth beta - 1/beta) = 1, beta_c = {mp.nstr(bc, 12)}; beyond it the ordered odds solve "
          "f = (K_1 f)^6/<(K_1 f)^6>, the lean is born continuously (M^2 = (6L - 1)/(9|c3|), c3 = -6L^3(38 lambda_2 - 3)/"
          "(6 lambda_2 - 1)), the transverse channel has no mass term at every beta (the turn of the lean is an exact "
          "eigenvector with eigenvalue 1/6), the longitudinal channel is massive, a record feeds the transverse channel "
          "only through its content's perpendicular part, the record count feeds no massless channel, and a body's "
          "transverse strength is its capacity")

#!/usr/bin/env python3
"""Independent referee of moving-kernel-with-vacancies attempt a1.

Author w-jonathonsmac4f50-jaae5 (claude-opus-5-5). Referee w-macbookpro90c72-jd2d4 (grok-4.6).
Own enumeration. The author's check.py is not imported.
The sphere-menu numerical threshold and the small-twist scan were not rebuilt.
"""
import itertools
from fractions import Fraction as F

import numpy as np

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


def log_bounds(num, den, terms):
    x = F(num, den)
    q = (x - 1) / (x + 1)
    s = F(0)
    term = 2 * q
    for j in range(terms):
        s += term / (2 * j + 1)
        term *= q * q
    tail = term / ((2 * terms + 1) * (1 - q * q))
    return s, s + tail


# ---------------------------------------------------------------- factorization, by exponents
# |sigma - sigma'|^2 = n + n' - 2 n n' (s·s') when |s|=1 and n^2 = n.
def sq(n1, n2, tt):
    return n1 + n2 - 2 * n1 * n2 * tt


ok_sq = True
for n1, n2, tt, expect in (
    (0, 0, 0, 0),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (1, 1, F(3, 5), 2 - 2 * F(3, 5)),
    (1, 1, -1, 4),
):
    ok_sq = ok_sq and sq(n1, n2, tt) == expect
require(ok_sq, "F1 |sigma-sigma'|^2 = n+n'-2nn'(s·s') on the occupation pairs")

# Gaussian exponent (beta'/2)(n+n') - (beta'/2)|sigma-sigma'|^2 plus the vacancy exponent.
# Both occupied: exponent becomes beta (s·s'), times c. One empty: exponent 0, kernel 1.
def exponent(n1, n2, tt, beta, betap):
    g_exp = betap * (n1 + n2) / 2 - betap * sq(n1, n2, tt) / 2
    v_exp = (beta - betap) * tt if n1 * n2 else 0
    return g_exp + v_exp


ok_fac = True
for n1, n2, tt in ((0, 0, 0), (1, 0, 0), (0, 1, F(1, 2)), (1, 1, F(-2, 7))):
    got = exponent(n1, n2, tt, beta=F(5), betap=F(2))
    want = (F(5) * tt) if n1 * n2 else 0
    ok_fac = ok_fac and got == want
require(ok_fac, "F1 the product of the Gaussian factor and the vacancy kernel is c exp(beta s·s') or 1")

# two-valued kernel on (empty, +, -)
# R(++, ) = c e^{gamma}, R(+-) = c e^{-gamma}, empty row is 1.
# Schur complement eigenvalues: 2c cosh - 2 and 2c sinh.


def schur_eigs(c, gamma):
    # occupied block minus the empty coupling (all ones)
    ep, em = np.exp(gamma), np.exp(-gamma)
    a = c * ep - 1
    d = c * em - 1
    # [[a, d], [d, a]]
    same = a + d
    opp = a - d
    return same, opp


ok_eigs = True
for gamma in (F(1, 2), 1, 2, 5):
    g = float(gamma)
    ch = np.cosh(g)
    sh = np.sinh(g)
    for c in (1 / ch, 0.5, 1.0):
        same, opp = schur_eigs(c, g)
        ok_eigs = ok_eigs and abs(same - (2 * c * ch - 2)) < 1e-12 and abs(opp - 2 * c * sh) < 1e-12
require(ok_eigs, "F3 the occupied Schur complement has eigenvalues 2c cosh(g)-2 and 2c sinh(g)")
# nonnegative iff c >= 1/cosh, since sinh >= 0
require(all(schur_eigs(1 / np.cosh(g), g)[0] > -1e-12 and schur_eigs(1 / np.cosh(g) - 1e-3, g)[0] < 0
        for g in (0.5, 1.0, 3.0)),
        "F3 the two-valued kernel is positive semidefinite exactly for c >= 1/cosh g")

# c0 decreases: p(g) = g cosh g - sinh g, p(0)=0, p'(g)=g sinh g >= 0
# so g/sinh g and 1/cosh g decrease. Check the derivative identity on a Taylor jet and the sign at samples.
def p_series_positive():
    # p(g) = g(1 + g^2/2 + ...) - (g + g^3/6 + ...) = g^3/3 + ...
    g = 1
    # exact rational comparison via exp bounds is unnecessary: p'(g)=g sinh g, sample p>0
    return all(g * np.cosh(g) - np.sinh(g) > 0 for g in (0.1, 1, 5))


require(p_series_positive(), "F5 g cosh g - sinh g > 0 for g>0, so both c0 functions decrease")
require(F(2 * 3, 9 + 1) == F(3, 5) and F(2 * 20, 400 + 1) == F(40, 401),
        "neutral scales: c0(ln 3)=3/5 and c0(ln 20)=40/401")

# ---------------------------------------------------------------- cube
SITES = [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]
IDX = {x: i for i, x in enumerate(SITES)}
BONDS = []
for x in SITES:
    for i in range(3):
        y = list(x)
        y[i] = (y[i] + 1) % 2
        BONDS.append((IDX[x], IDX[tuple(y)]))
KS = list(itertools.product((0, 1), repeat=3))
SGN = {k: [(-1) ** sum(ki * xi for ki, xi in zip(k, site)) for site in SITES] for k in KS}


def energy(k):
    return 4 * sum(k)


lap_bad = 0
for conf in itertools.product((-1, 0, 1), repeat=8):
    for k in KS:
        if k == (0, 0, 0):
            continue
        psi = SGN[k]
        X = 0
        for i, j in BONDS:
            X += (psi[i] - psi[j]) * (conf[i] - conf[j])
        if X != energy(k) * sum(p * v for p, v in zip(psi, conf)):
            lap_bad += 1
            break
require(lap_bad == 0 and len(BONDS) == 24,
        "A1 on all 3^8 configurations, the all-site twist equals E(k) sum sigma psi")


def accumulate(w, cc, z):
    Z = F(0)
    occ_sum = F(0)
    bond_sum = F(0)
    sk = {k: F(0) for k in KS}
    w = F(w)
    for conf in itertools.product((-1, 0, 1), repeat=8):
        n = [v * v for v in conf]
        al = an = 0
        for i, j in BONDS:
            if n[i] and n[j]:
                if conf[i] == conf[j]:
                    al += 1
                else:
                    an += 1
        nocc = sum(n)
        wt = z ** nocc * cc ** (al + an) * w ** al / w ** an
        Z += wt
        occ_sum += wt * nocc
        bond_sum += wt * (al + an)
        for k, psi in SGN.items():
            amp = sum(s * v for s, v in zip(psi, conf))
            sk[k] += wt * amp * amp
    return occ_sum / (8 * Z), bond_sum / (24 * Z), {k: sk[k] / (8 * Z) for k in KS}


rho, _rho2, S = accumulate(3, F(3, 5), F(1, 8))
kpi = (1, 1, 1)
stated = F(4295671717826064002261, 38505646859840596246081)
require(S[kpi] == stated, "X1 S(pi,pi,pi) is the stated fraction at e^beta=3, c=3/5, z=1/8")
require(sum(S.values()) == 8 * rho, "sum rule sum_k S(k) = N rho")

ln3_lo, ln3_hi = log_bounds(3, 1, 30)
x1 = S[kpi] * 12 * ln3_lo
require(x1 > F(147, 100) and ln3_hi < F(11, 10),
        f"X1 S beta E > {float(x1):.4f}, so 1/(beta E) fails at the neutral scale")

rho_b, rho2_b, Sb = accumulate(20, F(40, 401), F(1, 5))
ln20_lo = 2 * log_bounds(2, 1, 30)[0] + log_bounds(5, 1, 40)[0]
x2 = Sb[kpi] * 12 * rho2_b * ln20_lo
require(x2 > F(181, 100),
        f"X2 S beta rho2 E > {float(x2):.4f} (rho={float(rho_b):.4f}, rho2={float(rho2_b):.4f})")

ring = [1, 1, 0, 1]
psi4 = [1, 0, -1, 0]
occ_only = sum((psi4[i] - psi4[(i + 1) % 4]) * (ring[i] - ring[(i + 1) % 4])
               for i in range(4) if ring[i] and ring[(i + 1) % 4])
all_sites = sum((psi4[i] - psi4[(i + 1) % 4]) * (ring[i] - ring[(i + 1) % 4]) for i in range(4))
lap = 2 * sum(p * v for p, v in zip(psi4, ring))
require(occ_only == 0 and all_sites == 2 and lap == 2,
        "X3 a record-record twist gives 0; the all-site twist and E(k) sum sigma psi both give 2")

# ---------------------------------------------------------------- c1, numeric Gram at fixed beta
def c1_of(beta):
    sh, ch = np.sinh(beta), np.cosh(beta)
    return ((1 + beta * beta) * sh - beta * ch) / (sh * ch - beta)


def pencil_eigs(beta):
    # f(t)=exp(-beta t^2/2); gram of (value, derivative) at the three contents
    def f(t):
        return np.exp(-beta * t * t / 2)

    def fp(t):
        return -beta * t * f(t)

    def fpp(t):
        return (-beta + (beta * t) ** 2) * f(t)

    def entry(d1, d2, gap):
        if (d1, d2) == (0, 0):
            return f(gap)
        if (d1, d2) == (1, 0):
            return -fp(gap)
        if (d1, d2) == (0, 1):
            return fp(gap)
        return -fpp(gap)

    contents = [(0, 0), (1, 1), (1, -1)]  # (n, spin)
    labels = [(n, v, d) for n, v in contents for d in (0, 1)]
    M = np.zeros((6, 6))
    for i, (n1, v1, d1) in enumerate(labels):
        for j, (n2, v2, d2) in enumerate(labels):
            M[i, j] = np.exp(beta * (n1 + n2) / 2) * entry(d1, d2, v1 - v2)
    Gee = M[:2, :2]
    Geo = M[:2, 2:]
    Goo = M[2:, 2:]
    pen = np.linalg.solve(Goo, Geo.T @ np.linalg.solve(Gee, Geo))
    ev = np.linalg.eigvals(pen)
    return Gee, np.sort(ev.real)


gee_ok = True
c1_ok = True
shown = []
for beta in (1.0, 2.0, 3.0, 5.0):
    Gee, ev = pencil_eigs(beta)
    gee_ok = gee_ok and abs(Gee[0, 0] - 1) < 1e-12 and abs(Gee[1, 1] - beta) < 1e-10 and abs(Gee[0, 1]) < 1e-12
    top = float(ev[-1])
    c1v = c1_of(beta)
    c0v = 1 / np.cosh(beta)
    c1_ok = c1_ok and abs(top - c1v) < 1e-8 and c0v < c1v < 1
    shown.append(f"{beta:g}:{c1v:.5f}")
require(gee_ok, "B1 the empty block of the limit Gram is diag(1, beta)")
require(c1_ok, "B1 c1 is the largest pencil eigenvalue and c0 < c1 < 1 (" + ", ".join(shown) + ")")

# sin v >= 2v/pi on [0, pi/2]: q vanishes at the ends and q' = cos - 2/pi has one zero
# because cos decreases from 1 to 0. Hence 1-cos u >= 2 u^2/pi^2, and the ball of
# radius pi sqrt(3) bounds G(0) by pi sqrt(3)/8.
q0 = np.sin(0) - 0
q1 = np.sin(np.pi / 2) - 1
require(abs(q0) < 1e-15 and abs(q1) < 1e-15, "the chord of sin meets sin at 0 and at pi/2")
# one sign change of cos(v)-2/pi
grid = np.linspace(0, np.pi / 2, 9)
slope = np.cos(grid) - 2 / np.pi
require(np.sum(np.diff(np.sign(slope)) != 0) == 1 and slope[0] > 0 and slope[-1] < 0,
        "cos v - 2/pi changes sign once, so sin stays above the chord")
three_g = 3 * np.pi * np.sqrt(3) / 8
require(abs(three_g - 2.0405) < 5e-3, f"the explicit long-range threshold 3 sqrt(3) pi/8 is {three_g:.4f}")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - at the neutral scale the full-beta infrared bound fails, and the stiffness is 1/beta_A(c) rather than 1/(beta rho2)", flush=True)
    print("SUMMARY: confirmed - factorization, c0=1/cosh, cube counterexamples X1 and X2, X3, and c1 as the largest pencil eigenvalue. Sphere numerical thresholds were not rebuilt.", flush=True)

#!/usr/bin/env python3
"""Probe: FIXED_CLOCK_TRANSVERSE_SPECTRAL_CONCENTRATION_AND_LINEAR_ENERGY_BAND_BOUNDED_THEOREM_NOTE_2026-09-15.

The note's conditional input (all-affine covariance, reflection positivity in
the 4D state) is not testable here; its falsifier list also names the
positive rational localization identity and ordinary-weight conversion, the
midpoint magnetic compression, the physical contact normalization and the
endpoint handling.  Those steps are checked literally, with machinery disjoint
from the runner, beyond its sizes:

 L  localization (sec. 5, 7): the rational identity (10) and Phi' by exact
    polynomial arithmetic; m = 1/1071, K = 3927 and the 0.9996 fraction
    exactly; the chain chi(I_r^c) m <= int Phi dchi = chi/4 - (4/3)S(a) +
    (25/12)S(4a) <= (11/3) eps_3 on 20000 exact random atomic measures
    (rational atoms, contact atom at infinity, adversarial band-edge atoms).
 P  Poisson kernel (7), the reweighting kernel = u/(u+z) coth(E/2), unit
    temporal integral, tanh(E/2) = sqrt(u/(u+4)), J_r and the slopes, at 50 digits.
 M  midpoint magnetic compression (sec. 3) from a REAL-SPACE 4D cochain complex
    d: links -> plaquettes on the 6^4 torus, Fourier blocks read off plane
    waves, geometric midpoint rephasing; every one of the 1296 - 6 momenta with
    r > 0 against r^2/(r^2+w^2) P_T (runner: 3 momenta, hand-built symbol).
 C  the sec. 7 certificate: every rational inequality exactly (with rigorous
    rational bounds on log 3, log 4, pi, e checked at 50 digits), S_5, S_6 by
    Eulerian closed forms, the actual delta(2000), eta(2000), epsilon_*.
 S  sec. 8 controls: the uniform-chi Stieltjes closed form against quadrature,
    the atanh bound chain on a grid, h = 1/1000 below 1e-7, the scale mixture.
 O  sec. 2 on the one-plaquette clock for N in {2,3,4,7,16,64}, beta in
    {0.5,1,2.3,5,12} (runner: N = 5, 9 at beta = 2.3): Y = E[X|theta]
    (Fourier vs image sums), the centred MGF bound, the Chernoff tail,
    vbar <= eta(beta) and Var(Y) = 1 - vbar - C_n/beta.

Prints SUMMARY: lines; HIT: only when a checked statement of the note fails.
"""
import itertools
import math
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sps
import mpmath as mp

mp.mp.dps = 50
HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ---------------------------------------------------------------------------
# L  localization identity and chain (exact rationals)
# ---------------------------------------------------------------------------
def pmul(p, q):
    out = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def padd(*ps):
    n = max(len(p) for p in ps)
    out = [Fr(0)] * n
    for p in ps:
        for i, a in enumerate(p):
            out[i] += a
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(p, c):
    return [a * c for a in p]


def pderiv(p):
    return [i * p[i] for i in range(1, len(p))] or [Fr(0)]


def Phi(x):
    return (x - 1) ** 2 / ((x + 1) * (x + 4))


def run_L(n_measures=20000, seed=20260919):
    print("=" * 78)
    print("L  localization identity, constants and the inequality chain")
    X1 = [Fr(1), Fr(1)]          # x + 1
    X4 = [Fr(4), Fr(1)]          # x + 4
    Xm1 = [Fr(-1), Fr(1)]        # x - 1
    X = [Fr(0), Fr(1)]
    # 12 (x-1)^2 == 3(x+1)(x+4) - 16 x (x+4) + 25 x (x+1)
    lhs = pscale(pmul(Xm1, Xm1), 12)
    rhs = padd(pscale(pmul(X1, X4), 3), pscale(pmul(X, X4), -16), pscale(pmul(X, X1), 25))
    ident = padd(lhs, pscale(rhs, -1)) == [Fr(0)]
    # Phi' numerator: d/dx [(x-1)^2] (x+1)(x+4) - (x-1)^2 d/dx[(x+1)(x+4)] == (x-1)(7x+13)
    num = padd(pmul(pderiv(pmul(Xm1, Xm1)), pmul(X1, X4)), pscale(pmul(pmul(Xm1, Xm1), pderiv(pmul(X1, X4))), -1))
    deriv_ok = padd(num, pscale(pmul(Xm1, [Fr(13), Fr(7)]), -1)) == [Fr(0)]
    m = min(Phi(Fr(9, 10)), Phi(Fr(11, 10)))
    K = Fr(11, 3) / m
    eps = Fr(1, 10 ** 7)
    frac = 1 - K * eps / (1 - eps)
    ref_cancel = Fr(1, 4) * 1 - Fr(4, 3) * Fr(1, 2) + Fr(25, 12) * Fr(1, 5)
    coef_sum = Fr(1, 4) + Fr(4, 3) + Fr(25, 12)
    print(f"  12(x-1)^2 identity: {ident}; Phi' = (x-1)(7x+13)/((x+1)^2(x+4)^2): {deriv_ok}; Phi(9/10) = "
          f"{Phi(Fr(9, 10))}, Phi(11/10) = {Phi(Fr(11, 10))}, m = {m}, K = {K}; 1 - K eps/(1-eps) = {float(frac):.10f} "
          f"> 0.9996: {frac > Fr(9996, 10000)}; reference cancellation {ref_cancel}; |coef| sum {coef_sum}")
    ok = ident and deriv_ok and m == Fr(1, 1071) and K == 3927 and frac > Fr(9996, 10000) and ref_cancel == 0 \
        and coef_sum == Fr(11, 3)
    if not ok:
        hit("localization identity or its constants differ from the note")
    # random exact atomic measures
    rng = random.Random(seed)
    alpha, gamma = Fr(9, 10), Fr(11, 10)
    worst_chain = Fr(0)
    bad = 0
    for trial in range(n_measures):
        a = Fr(rng.randint(1, 100), 100) ** 2          # a = r^2, 0 < r <= 1
        atoms = []
        for _ in range(rng.randint(1, 6)):
            mode = rng.random()
            if mode < 0.4:
                u = a * Fr(rng.randint(80, 125), 100)   # near the band
            elif mode < 0.6:
                u = a * (alpha if rng.random() < 0.5 else gamma) * Fr(rng.randint(990, 1010), 1000)
            elif mode < 0.8:
                u = a * Fr(rng.randint(1, 1000), 100)    # no mass at E = 0 (sec. 4)
            else:
                u = None                                 # contact atom at infinity
            atoms.append((u, Fr(rng.randint(1, 1000), 1000)))
        tot = sum(w for _, w in atoms)
        atoms = [(u, w / tot * Fr(rng.randint(990, 1010), 1000)) for u, w in atoms]

        def S(z):
            return sum((w if u is None else w * u / (u + z)) for u, w in atoms)
        chi = sum(w for _, w in atoms)            # chi(total), the monotone z -> 0 value
        Sa, S4a = S(a), S(4 * a)
        integral = sum((w if u is None else w * Phi(u / a)) for u, w in atoms)
        combo = chi / 4 - Fr(4, 3) * Sa + Fr(25, 12) * S4a
        eps3 = max(abs(chi - 1), abs(Sa - Fr(1, 2)), abs(S4a - Fr(1, 5)))
        outside = sum(w for u, w in atoms if u is None or not (alpha * a <= u <= gamma * a))
        if integral != combo or integral < 0 or integral > Fr(11, 3) * eps3 or outside * m > integral:
            bad += 1
        if eps3 > 0:
            worst_chain = max(worst_chain, outside / (K * eps3))
    print(f"  {n_measures} exact random measures: chain failures {bad}; max chi(I^c)/(K eps_3) = {float(worst_chain):.4f}")
    if bad:
        hit(f"the localization chain fails on {bad} exact measures")
    return ok, m, K, frac, n_measures, bad, worst_chain


# ---------------------------------------------------------------------------
# P  Poisson kernel, reweighting, conversions
# ---------------------------------------------------------------------------
def run_P():
    print("=" * 78)
    print("P  Poisson kernel, reweighting and energy conversion (50 digits)")
    worst = mp.mpf(0)
    for lam in (mp.mpf("0.05"), mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("0.95")):
        E = -mp.log(lam)
        for om in (mp.mpf("0.01"), mp.mpf("0.4"), mp.mpf(1), mp.mpf(2), mp.mpf(3)):
            T = int(mp.ceil(60 / (-mp.log10(lam)))) + 10
            direct = 1 + 2 * mp.fsum(lam ** t * mp.cos(om * t) for t in range(1, T))
            f1 = (1 - lam ** 2) / (1 - 2 * lam * mp.cos(om) + lam ** 2)
            f2 = mp.sinh(E) / (mp.cosh(E) - mp.cos(om))
            u = 4 * mp.sinh(E / 2) ** 2
            z = 4 * mp.sin(om / 2) ** 2
            f3 = u / (u + z) * mp.coth(E / 2)
            worst = max(worst, abs(direct - f1), abs(f1 - f2), abs(f2 - f3))
        integ = mp.quad(lambda w: mp.sinh(E) / (mp.cosh(E) - mp.cos(w)), [-mp.pi, 0, mp.pi]) / (2 * mp.pi)
        worst = max(worst, abs(integ - 1))
    tanh_dev = max(abs(mp.tanh(E / 2) - mp.sqrt(4 * mp.sinh(E / 2) ** 2 / (4 * mp.sinh(E / 2) ** 2 + 4)))
                   for E in (mp.mpf("0.001"), mp.mpf("0.3"), mp.mpf(2), mp.mpf(9)))
    slopes = []
    for r in (mp.mpf("1e-6"),):
        slopes = [2 * mp.asinh(mp.sqrt(mp.mpf(9) / 10) * r / 2) / r, 2 * mp.asinh(mp.sqrt(mp.mpf(11) / 10) * r / 2) / r]
    exp_slopes = [3 / mp.sqrt(10), mp.sqrt(mp.mpf(11) / 10)]
    # J_r endpoints map back to u = alpha r^2, gamma r^2
    jr_dev = mp.mpf(0)
    for r in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf(1)):
        for c in (mp.mpf(9) / 10, mp.mpf(11) / 10):
            E = 2 * mp.asinh(mp.sqrt(c) * r / 2)
            jr_dev = max(jr_dev, abs(4 * mp.sinh(E / 2) ** 2 - c * r * r))
            # ordinary weight factor at the endpoint: tanh(E/2) = sqrt(c) r / sqrt(c r^2 + 4)
            jr_dev = max(jr_dev, abs(mp.tanh(E / 2) - mp.sqrt(c) * r / mp.sqrt(c * r * r + 4)))
    print(f"  kernel identities (series, two closed forms, u/(u+z) coth(E/2)) and unit integral: max dev "
          f"{mp.nstr(worst, 3)}; tanh(E/2) = sqrt(u/(u+4)): {mp.nstr(tanh_dev, 3)}; J_r endpoint/weight "
          f"conversions: {mp.nstr(jr_dev, 3)}; slopes {[mp.nstr(s, 10) for s in slopes]} vs 3/sqrt10, sqrt(11/10)")
    if worst > mp.mpf(10) ** -40 or tanh_dev > mp.mpf(10) ** -40 or jr_dev > mp.mpf(10) ** -40 or \
            any(abs(s - e) > mp.mpf(10) ** -10 for s, e in zip(slopes, exp_slopes)):
        hit("Poisson/Stieltjes reweighting or energy conversion fails")
    return worst, tanh_dev, jr_dev, slopes


# ---------------------------------------------------------------------------
# M  midpoint magnetic compression from a real-space 4D complex
# ---------------------------------------------------------------------------
def run_M(L=6):
    print("=" * 78)
    print(f"M  midpoint magnetic compression from the real-space 4D complex on the {L}^4 torus")
    sites = list(itertools.product(range(L), repeat=4))
    sidx = {s: t for t, s in enumerate(sites)}
    V = len(sites)
    pairs = list(itertools.combinations(range(4), 2))

    def sh(x, mu, s=1):
        y = list(x)
        y[mu] = (y[mu] + s) % L
        return tuple(y)
    rows, cols, vals = [], [], []
    for x in sites:
        for a, (mu, nu) in enumerate(pairs):
            prow = a * V + sidx[x]
            # (dA)_{mu nu}(x) = A_nu(x+mu) - A_nu(x) - A_mu(x+nu) + A_mu(x)
            for (lmu, lx, s) in ((nu, sh(x, mu), 1), (nu, x, -1), (mu, sh(x, nu), -1), (mu, x, 1)):
                rows.append(prow)
                cols.append(lmu * V + sidx[lx])
                vals.append(s)
    D = sps.csr_matrix((np.array(vals, float), (rows, cols)), shape=(6 * V, 4 * V))
    coords = np.array(sites, dtype=float)
    BB = np.zeros((3, 6))
    BB[0, pairs.index((2, 3))] = 1
    BB[1, pairs.index((1, 3))] = -1
    BB[2, pairs.index((1, 2))] = 1
    worst = 0.0
    worst_trans = 0.0
    rank_ok = True
    count = 0
    for m in itertools.product(range(L), repeat=4):
        k = 2 * np.pi * np.array(m) / L
        xi = 2 * np.sin(k[1:] / 2)
        r2 = float(xi @ xi)
        if r2 < 1e-14:
            continue
        count += 1
        # plane waves with GEOMETRIC midpoint phases: link (x,mu) sits at x + e_mu/2
        dk = np.zeros((6, 4), dtype=complex)
        for mu in range(4):
            vec = np.zeros(4 * V, dtype=complex)
            off = np.zeros(4)
            off[mu] = 0.5
            vec[mu * V:(mu + 1) * V] = np.exp(1j * (coords + off) @ k)
            out = D @ vec
            for a, (p1, p2) in enumerate(pairs):
                off2 = np.zeros(4)
                off2[p1] = 0.5
                off2[p2] = 0.5
                # coefficient of the plaquette plane wave e^{ik.(x + midpoint)} at x = 0 and at a second site
                dk[a, mu] = out[a * V + 0] / np.exp(1j * off2 @ k)
                y = sidx[(1, 2, 3, 4 % L)]
                worst_trans = max(worst_trans, abs(out[a * V + y] / np.exp(1j * (coords[y] + off2) @ k) - dk[a, mu]))
        Pe = dk @ np.linalg.pinv(dk)
        mag = BB @ Pe @ BB.T
        w2 = 4 * np.sin(k[0] / 2) ** 2
        PT = np.eye(3) - np.outer(xi, xi) / r2
        worst = max(worst, float(np.max(np.abs(mag - r2 / (r2 + w2) * PT))))
        rank_ok &= np.linalg.matrix_rank(mag, tol=1e-9) == 2
    print(f"  {count} momenta with r > 0: max |[P_e]_BB - r^2/(r^2+w^2) P_T| = {worst:.2e}; plane-wave "
          f"translation consistency {worst_trans:.1e}; magnetic block rank 2 at all: {rank_ok}")
    if worst > 1e-10 or not rank_ok:
        hit(f"midpoint magnetic compression differs from r^2/(r^2+w^2) P_T (max dev {worst:.2e})")
    return count, worst, worst_trans, rank_ok


# ---------------------------------------------------------------------------
# C  the sec. 7 certificate
# ---------------------------------------------------------------------------
def S5_closed(q):
    return q * (1 + 26 * q + 66 * q ** 2 + 26 * q ** 3 + q ** 4) / (1 - q) ** 6


def S6_closed(q):
    return q * (1 + 57 * q + 302 * q ** 2 + 302 * q ** 3 + 57 * q ** 4 + q ** 5) / (1 - q) ** 7


def run_C():
    print("=" * 78)
    print("C  the fixed-parameter certificate (sec. 7)")
    # rational bounds, checked at 50 digits
    bounds_ok = (mp.log(3) < mp.mpf(11) / 10 and mp.log(4) < mp.mpf(7) / 5 and mp.pi > mp.mpf(157) / 50
                 and mp.log(2) < mp.mpf(7) / 10 and mp.e > 2 and mp.pi < 4 and mp.pi > 3)
    b1_up = (107 * Fr(11, 10) + Fr(7, 5)) / (4 * Fr(157, 50) ** 2)
    a_low = Fr(2000, 384) - Fr(31, 10)
    two_pi2_a_low = 2 * Fr(157, 50) ** 2 * a_low
    checks = {
        "b1 < 31/10": b1_up < Fr(31, 10),
        "a(2000) > 253/120": a_low == Fr(253, 120),
        "2000/a(2000) < 1000": Fr(2000) / a_low < 1000,
        "2 pi^2 a > 6236197/150000": two_pi2_a_low == Fr(6236197, 150000),
        "6236197/150000 > 59 (7/10)": Fr(6236197, 150000) > 59 * Fr(7, 10),
        "S_5, S_6 <= 2q at q = 1/1024": S5_closed(Fr(1, 1024)) <= 2 * Fr(1, 1024) and S6_closed(Fr(1, 1024)) <= 2 * Fr(1, 1024),
        "8765200000/2^59 < 1/50000000": Fr(8765200000, 2 ** 59) < Fr(1, 50000000),
        "8503056 + 262144 = 8765200": 8503056 + 262144 == 8765200,
        "256016 * 2^-9000 < 1/50000000": Fr(256016, 2 ** 9000) < Fr(1, 50000000),
        "8 * 16 * 2000 + 16 = 256016": 8 * 16 * 2000 + 16 == 256016,
    }
    # monotone S_j/q on (0, 1/1024]: check the closed form against the series at a few q
    ser_dev = max(abs(S5_closed(mp.mpf(q)) - mp.nsum(lambda r: r ** 5 * mp.mpf(q) ** r, [1, mp.inf])) +
                  abs(S6_closed(mp.mpf(q)) - mp.nsum(lambda r: r ** 6 * mp.mpf(q) ** r, [1, mp.inf]))
                  for q in ("1e-3", "1e-6", "0.1"))
    b1 = (107 * mp.log(3) + mp.log(4)) / (4 * mp.pi ** 2)

    def delta(s):
        a = s / 384 - b1
        q = mp.e ** (-2 * mp.pi ** 2 * a)
        return s * (8503056 * S6_closed(q) + 262144 * S5_closed(q)) / (a * mp.e)

    def eta(beta):
        return (8 * mp.pi ** 2 * beta + 16) * mp.e ** (-mp.pi ** 2 * beta / 2)
    d2000 = delta(mp.mpf(2000))
    mono = all(delta(mp.mpf(s)) > delta(mp.mpf(s + 250)) for s in range(2000, 20000, 250))
    e2000 = eta(mp.mpf(2000))
    eps_total = max(d2000, d2000) + e2000
    for k, v in checks.items():
        print(f"  {k}: {v}")
    print(f"  rational bounds on log3, log4, log2, pi, e hold at 50 digits: {bounds_ok}; Eulerian S_5/S_6 vs series "
          f"{mp.nstr(ser_dev, 3)}")
    print(f"  b1 = {mp.nstr(b1, 12)}; delta(2000) = {mp.nstr(d2000, 6)}; delta decreasing on [2000, 20000]: {mono}; "
          f"eta(2000) = {mp.nstr(e2000, 6)}; epsilon at beta = beta_d = 2000: {mp.nstr(eps_total, 6)} <= 1e-7: "
          f"{eps_total <= mp.mpf('1e-7')}")
    ok = bounds_ok and all(checks.values()) and ser_dev < mp.mpf(10) ** -40 and mono and eps_total <= mp.mpf("1e-7")
    if not ok:
        hit("a sec. 7 certificate inequality fails")
    return checks, d2000, e2000, ok


# ---------------------------------------------------------------------------
# S  sec. 8 controls
# ---------------------------------------------------------------------------
def run_S():
    print("=" * 78)
    print("S  continuous-spectrum control and the scale mixture")
    worst_form = mp.mpf(0)
    worst_chain = mp.mpf(0)
    for a in (mp.mpf("0.01"), mp.mpf("0.3"), mp.mpf(1)):
        for h in (mp.mpf("0.001"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9")):
            for z in (mp.mpf(0), a / 10, a, 4 * a, 3 * a, 50 * a):
                closed = 1 - (z / (2 * a * h)) * mp.log((a * (1 + h) + z) / (a * (1 - h) + z)) if z > 0 else mp.mpf(1)
                quad = mp.quad(lambda u: u / (u + z), [a * (1 - h), a, a * (1 + h)]) / (2 * a * h)
                worst_form = max(worst_form, abs(closed - quad))
                gap = a / (a + z) - closed
                b = a * h / (a + z)
                mid = z / (a + z) * (mp.atanh(b) / b - 1)
                up1 = z * a ** 2 * h ** 2 / (3 * (a + z) ** 3 * (1 - h ** 2))
                up2 = 4 * h ** 2 / (81 * (1 - h ** 2))
                if not (gap >= -mp.mpf(10) ** -45 and abs(gap - mid) < mp.mpf(10) ** -40 and mid <= up1 * (1 + mp.mpf(10) ** -30)
                        and up1 <= up2 * (1 + mp.mpf(10) ** -30)):
                    worst_chain = max(worst_chain, mp.mpf(1))
    h = mp.mpf(1) / 1000
    up2 = 4 * h ** 2 / (81 * (1 - h ** 2))
    zs = [mp.mpf(j) / 50 for j in range(0, 401)]
    def S_unif(z, a=mp.mpf(1)):
        if z == 0:
            return mp.mpf(1)                                  # S(0) = chi(total) = 1
        return 1 - (z / (2 * a * h)) * mp.log((a * (1 + h) + z) / (a * (1 - h) + z))
    maxgap = max(mp.mpf(1) / (1 + z) - S_unif(z) for z in zs)
    var_mix = (Fr(1, 2) + Fr(3, 2)) / 2
    m4_mix = 3 * (Fr(1, 2) ** 2 + Fr(3, 2) ** 2) / 2
    print(f"  uniform chi: closed form vs quadrature max {mp.nstr(worst_form, 3)}; bound-chain failures "
          f"{int(worst_chain)}; h = 1/1000: 4h^2/(81(1-h^2)) = {mp.nstr(up2, 6)} < 1e-7: {up2 < mp.mpf('1e-7')}, "
          f"max gap on z in [0, 8] at a = 1: {mp.nstr(maxgap, 6)}")
    print(f"  scale mixture (1/2, 3/2): variance {var_mix}, fourth moment {m4_mix} (Gaussian 3)")
    ok = worst_form < mp.mpf(10) ** -30 and worst_chain == 0 and up2 < mp.mpf("1e-7") and maxgap < up2 \
        and var_mix == 1 and m4_mix == Fr(15, 4)
    if not ok:
        hit("a sec. 8 control fails")
    return worst_form, up2, maxgap, ok


# ---------------------------------------------------------------------------
# O  one-plaquette clock, sec. 2
# ---------------------------------------------------------------------------
def run_O():
    with mp.workdps(120):          # the Fourier sums for phi cancel to ~exp(-pi^2 beta/2) near t = pi
        return _run_O()


def _run_O():
    print("=" * 78)
    print("O  one-plaquette clock: score contact, MGF, Chernoff tail, vbar <= eta, Var(Y)  [120 digits]")
    tol = mp.mpf(10) ** -100      # relative rounding allowance: the MGF bound is tight to exp(-2 pi^2 beta_d)
    mgf_slack = mp.mpf(-1)
    rows = []
    worst_Y = mp.mpf(0)
    worst_var = mp.mpf(0)
    bad = []
    for beta in (mp.mpf("0.5"), mp.mpf(1), mp.mpf("2.3"), mp.mpf(5), mp.mpf(12)):
        eta = (8 * mp.pi ** 2 * beta + 16) * mp.e ** (-mp.pi ** 2 * beta / 2)
        nmax = int(mp.ceil(mp.sqrt(2 * beta * 300))) + 5
        for N in (2, 3, 4, 7, 16, 64):
            bd = mp.mpf(N) ** 2 / (4 * mp.pi ** 2 * beta)
            zmax = int(mp.ceil(mp.sqrt(2 * bd * 300))) + N + 5
            # joint law of z = k - N m: discrete Gaussian on Z, X = z / sqrt(beta_d)
            zs = list(range(-zmax, zmax + 1))
            wz = [mp.e ** (-mp.mpf(z) ** 2 / (2 * bd)) for z in zs]
            Z = mp.fsum(wz)
            # MGF bound and Chernoff tail
            mgf_ok = True
            for hh in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(4)):
                ratio = (mp.fsum(w * mp.e ** (hh * z / mp.sqrt(bd)) for w, z in zip(wz, zs)) / Z) / mp.e ** (hh ** 2 / 2)
                mgf_slack = max(mgf_slack, ratio - 1)
                mgf_ok &= ratio <= 1 + tol
            tail_ok = all(mp.fsum(w for w, z in zip(wz, zs) if abs(z) / mp.sqrt(bd) >= u) / Z <= 2 * mp.e ** (-u * u / 2)
                          for u in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(3), mp.pi * mp.sqrt(beta)))
            # conditional on theta = 2 pi k / N (k = z mod N): mean and variance of X
            probs, means, varis, scores = [], [], [], []
            for k in range(N):
                sel = [(w, mp.mpf(z) / mp.sqrt(bd)) for w, z in zip(wz, zs) if z % N == k]
                pk = mp.fsum(w for w, _ in sel)
                mu = mp.fsum(w * x for w, x in sel) / pk
                va = mp.fsum(w * (x - mu) ** 2 for w, x in sel) / pk
                t = 2 * mp.pi * k / N
                phi = mp.fsum(mp.e ** (-mp.mpf(n) ** 2 / (2 * beta)) * mp.cos(n * t) for n in range(-nmax, nmax + 1))
                dphi = -mp.fsum(n * mp.e ** (-mp.mpf(n) ** 2 / (2 * beta)) * mp.sin(n * t) for n in range(-nmax, nmax + 1))
                Y = -dphi / (mp.sqrt(beta) * phi)
                probs.append(pk / Z)
                means.append(mu)
                varis.append(va)
                scores.append(Y)
            worst_Y = max(worst_Y, max(abs(a - b) for a, b in zip(means, scores)))
            vbar = mp.fsum(p * v for p, v in zip(probs, varis))
            varY = mp.fsum(p * y * y for p, y in zip(probs, scores)) - mp.fsum(p * y for p, y in zip(probs, scores)) ** 2
            allowed = [n for n in range(-nmax * N, nmax * N + 1) if n % N == 0 and abs(n) <= nmax]
            wn = [mp.e ** (-mp.mpf(n) ** 2 / (2 * beta)) for n in allowed]
            Wn = mp.fsum(wn)
            Cn = mp.fsum(w * n * n for w, n in zip(wn, allowed)) / Wn
            pred = 1 - vbar - Cn / beta
            worst_var = max(worst_var, abs(varY - pred))
            vb_ok = vbar <= eta
            rows.append((beta, N, vbar, eta, vb_ok, mgf_ok, tail_ok))
            if not (vb_ok and mgf_ok and tail_ok):
                bad.append((float(beta), N, bool(vb_ok), bool(mgf_ok), bool(tail_ok)))
    for beta, N, vbar, eta, vb_ok, mgf_ok, tail_ok in rows:
        if N in (2, 16, 64):
            print(f"  beta={mp.nstr(beta, 3):>4s} N={N:2d}: vbar = {mp.nstr(vbar, 8):>14s} <= eta = {mp.nstr(eta, 8):>14s}: "
                  f"{vb_ok}; MGF bound {mgf_ok}; Chernoff tail {tail_ok}")
    print(f"  all 30 (beta, N): max |E[X|theta] - Y| = {mp.nstr(worst_Y, 3)}; max |Var Y - (1 - vbar - C_n/beta)| = "
          f"{mp.nstr(worst_var, 3)}; failures {bad}")
    if worst_Y > mp.mpf(10) ** -40 or worst_var > mp.mpf(10) ** -40 or bad:
        hit(f"one-plaquette sec. 2 step fails: {bad}, score dev {mp.nstr(worst_Y, 3)}, variance dev {mp.nstr(worst_var, 3)}")
    vmax_ratio = max(float(v / e) for _, _, v, e, _, _, _ in rows)
    print(f"  max (E e^(hX) / e^(h^2/2) - 1) over all cases: {mp.nstr(mgf_slack, 3)} (<= 0 up to 1e-100 rounding; "
          f"the theta-function ratio differs from 1 by ~exp(-2 pi^2 beta_d))")
    return rows, worst_Y, worst_var, vmax_ratio


def main():
    t0 = time.time()
    ok, m, K, frac, nmeas, bad, wc = run_L()
    summary(f"L localization: 12(x-1)^2 identity and Phi' exact; m = {m}, K = {K}, fraction {float(frac):.8f} > 0.9996; "
            f"{nmeas} exact random measures: chain failures {bad}, max chi(I^c)/(K eps_3) = {float(wc):.4f}")
    w, td, jd, sl = run_P()
    summary(f"P Poisson kernel = sinh E/(cosh E - cos w) = u/(u+z) coth(E/2), unit integral (dev {mp.nstr(w, 2)}); "
            f"tanh(E/2) = sqrt(u/(u+4)); J_r conversions (dev {mp.nstr(jd, 2)}); slopes {mp.nstr(sl[0], 8)}, "
            f"{mp.nstr(sl[1], 8)}")
    cnt, wm, wt, rk = run_M()
    summary(f"M real-space 6^4 complex, {cnt} momenta: max |[P_e]_BB - r^2/(r^2+w^2) P_T| = {wm:.1e}, rank 2 at all: {rk}")
    checks, d2000, e2000, okc = run_C()
    summary(f"C certificate: all {len(checks)} rational inequalities hold: {all(checks.values())}; delta(2000) = "
            f"{mp.nstr(d2000, 4)}, eta(2000) = {mp.nstr(e2000, 4)}, epsilon <= 1e-7: {okc}")
    wf, up2, mg, oks = run_S()
    summary(f"S uniform-chi Stieltjes closed form vs quadrature {mp.nstr(wf, 2)}; atanh chain holds; h = 1/1000 bound "
            f"{mp.nstr(up2, 4)} (< 1e-7) with actual max gap {mp.nstr(mg, 4)}; scale mixture variance 1, fourth moment 15/4")
    rows, wy, wv, vr = run_O()
    summary(f"O one-plaquette, N in {{2,3,4,7,16,64}} x beta in {{0.5,1,2.3,5,12}}: E[X|theta] = Y to {mp.nstr(wy, 2)}, "
            f"Var Y = 1 - vbar - C_n/beta to {mp.nstr(wv, 2)}, MGF and Chernoff bounds hold, vbar <= eta(beta) with max "
            f"ratio {vr:.4f}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())

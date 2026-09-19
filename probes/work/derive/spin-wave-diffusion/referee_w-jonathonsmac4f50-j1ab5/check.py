#!/usr/bin/env python3
"""Referee of J:derive:spin-wave-diffusion:a2 (author w-macbookpro90c72-j8b6e, grok-4.6); referee
w-jonathonsmac4f50-j1ab5 (claude-opus-5). Independent machinery, none of the author's code:

V1  G_4 = 189/128 two ways: the Fourier sum with exact cosines, and a real-space route (the stationary covariance of
    the centred linear field theta' = P theta + xi on the 4x4 torus, solved exactly as a translation-invariant
    Lyapunov equation in rationals)
V2  G_8, G_16 (and G_32, G_64) at 30 digits from block 34's sine form of 1 - |phi|^2 (the sine and cosine forms
    are checked equal symbolically); the log-slope of G_L against the constant used in the attempt's section (4)
V3  the predicted ratios 1/(1 - sigma^2 G_16)^2 at beta = 6, 12, 24, 48, and 1 - sigma^2 G_16 against block 34's
    measured stationary |m| (its table is at L = 16)
V4  the statement's own error terms against the first correction it claims, at fixed L
V5  L = 1 exactly: the one-step ratio is 1/A(3 beta) = 1 + sigma^2 + O(sigma^4) while 1/(1 - sigma^2 G_1)^2 = 1
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


def A(k):
    return mp.coth(k) - 1 / k


# ------------------------------------------------------------------ V1
def G4_fourier():
    cosq = {0: 1, 1: 0, 2: -1, 3: 0}          # cos(2 pi n / 4)
    tot = Fraction(0)
    for n1, n2 in itertools.product(range(4), repeat=2):
        if n1 == n2 == 0:
            continue
        one_minus = Fraction(6 - 2 * cosq[n1] - 2 * cosq[n2] - 2 * cosq[(n1 - n2) % 4], 9)
        tot += 1 / one_minus
    return tot / 16


def G4_realspace():
    """stationary covariance c(d) = Cov(theta_x, theta_{x+d}) of the component orthogonal to the zero mode, for
    theta' = P theta + xi on the 4x4 torus, P theta_x = (theta_x + theta_{x-e1} + theta_{x-e2})/3, Var xi = 1:
    c(d) = (1/9) sum_{a,b in O} c(d - a + b) + delta_{d,0} - 1/16, with sum_d c(d) = 0. Returns c(0)."""
    L = 4
    O = [(0, 0), (1, 0), (0, 1)]
    ds = list(itertools.product(range(L), repeat=2))
    idx = {d: i for i, d in enumerate(ds)}
    n = len(ds)
    rows = []
    rhs = []
    for d in ds:
        row = [Fraction(0)] * n
        row[idx[d]] += 1
        for a in O:
            for b in O:
                e = ((d[0] - a[0] + b[0]) % L, (d[1] - a[1] + b[1]) % L)
                row[idx[e]] -= Fraction(1, 9)
        rows.append(row)
        rhs.append(Fraction(1 if d == (0, 0) else 0) - Fraction(1, 16))
    rows.append([Fraction(1)] * n)       # the zero-mode constraint
    rhs.append(Fraction(0))
    # least-squares-free exact solve: the system is consistent; eliminate
    M = [r[:] + [v] for r, v in zip(rows, rhs)]
    m = len(M)
    col = 0
    piv_rows = []
    r = 0
    for col in range(n):
        p = next((i for i in range(r, m) if M[i][col] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][col]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv_rows.append(col)
        r += 1
    consistent = all(all(x == 0 for x in M[i][:n]) <= (M[i][n] == 0) for i in range(r, m))
    assert r == n and consistent
    sol = {piv_rows[i]: M[i][n] for i in range(n)}
    return sol[idx[(0, 0)]]


def v1():
    g_f = G4_fourier()
    g_r = G4_realspace()
    check("V1", g_f == Fraction(189, 128) and g_r == Fraction(189, 128),
          f"step 1: G_4 = {g_f} from the Fourier sum with exact cosines and {g_r} as the site variance of the stationary "
          "centred field solved exactly in real space (translation-invariant Lyapunov equation): both 189/128")


# ------------------------------------------------------------------ V2
def G_sine(L):
    tot = mp.mpf(0)
    for n1, n2 in itertools.product(range(L), repeat=2):
        if n1 == n2 == 0:
            continue
        k1 = 2 * mp.pi * n1 / L
        k2 = 2 * mp.pi * n2 / L
        tot += 1 / (mp.mpf(4) / 9 * (mp.sin(k1 / 2) ** 2 + mp.sin(k2 / 2) ** 2 + mp.sin((k1 - k2) / 2) ** 2))
    return tot / L ** 2


def v2():
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    one_minus = sp.simplify(sp.expand(1 - phi * sp.conjugate(phi), complex=True))
    sine = sp.Rational(4, 9) * (sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2)
    cosine = (6 - 2 * sp.cos(k1) - 2 * sp.cos(k2) - 2 * sp.cos(k1 - k2)) / 9
    ok_forms = sp.simplify(sp.expand_trig(one_minus - cosine)) == 0 and sp.simplify(sp.expand_trig(sine - cosine)) == 0
    G = {L: G_sine(L) for L in (4, 8, 16, 32, 64)}
    ok = ok_forms and abs(G[4] - mp.mpf(189) / 128) < mp.mpf(10) ** -25
    ok = ok and abs(G[8] - mp.mpf("2.06668527")) < 5e-9 and abs(G[16] - mp.mpf("2.64427100")) < 5e-9
    slopes = [(G[2 * L] - G[L]) / mp.log(2) for L in (8, 16, 32)]
    c_block34 = 3 * mp.sqrt(3) / (2 * mp.pi)
    c_attempt = 3 / mp.pi
    ok = ok and abs(slopes[-1] - c_block34) < 0.01 and abs(slopes[-1] - c_attempt) > 0.1
    check("V2", ok,
          "step 1 and section (4): 1 - |phi|^2 has the cosine form and block 34's sine form (symbolic); G_L at 30 digits: "
          + ", ".join(f"G_{L} = {mp.nstr(G[L], 9)}" for L in (4, 8, 16, 32, 64))
          + f" (the author's G_8, G_16 agree); the doubling slopes (G_2L - G_L)/log 2 = "
          + ", ".join(mp.nstr(s, 5) for s in slopes)
          + f" approach block 34's 2c_0 = 3 sqrt3/(2 pi) = {mp.nstr(c_block34, 5)}, not the 3/pi = {mp.nstr(c_attempt, 5)} "
          "written in the attempt's section (4)")
    return G


# ------------------------------------------------------------------ V3
def v3(G):
    betas = (6, 12, 24, 48)
    author = (mp.mpf("1.348"), mp.mpf("1.160"), mp.mpf("1.077"), mp.mpf("1.037"))
    measured_m = (mp.mpf("0.844"), mp.mpf("0.924"), mp.mpf("0.963"), mp.mpf("0.982"))   # block 34's table, L = 16
    ok = True
    rows = []
    for b, a_val, mm in zip(betas, author, measured_m):
        s2 = A(3 * b) / (3 * b)
        x = s2 * G[16]
        pred = 1 / (1 - x) ** 2
        ok = ok and abs(pred - a_val) < mp.mpf("0.0006")
        rows.append(f"beta={b}: sigma^2 = {mp.nstr(s2, 5)}, 1/(1 - sigma^2 G_16)^2 = {mp.nstr(pred, 5)}, "
                    f"1 - sigma^2 G_16 = {mp.nstr(1 - x, 4)} vs measured |m| = {mm}")
    check("V3", ok, "step 4 arithmetic: the author's predicted ratios are reproduced; " + "; ".join(rows)
          + ". Block 34's executed table is at L = 16 (the same at 32), not unstated and not L = 256")


# ------------------------------------------------------------------ V4
def v4(G):
    G16 = G[16]
    rel = G16 / 2          # [sigma^2 G^2] / [2 sigma^2 G]
    beta_big = 1000
    s2 = A(3 * beta_big) / (3 * beta_big)
    corr = 2 * s2 * G16
    invN = mp.mpf(1) / 256
    ok = rel > 1 and corr < invN
    check("V4", ok,
          f"the statement's error terms against its claimed first correction at fixed L = 16: O(sigma^2 G_L^2) is "
          f"G_16/2 = {mp.nstr(rel, 4)} times the claimed 2 sigma^2 G_L, so it is of the same order in sigma^2; and O(1/N) "
          f"= {mp.nstr(invN, 4)} does not vanish as beta grows (at beta = {beta_big} the claimed correction is "
          f"{mp.nstr(corr, 4)}): as written the statement implies neither ratio -> 1 nor the coefficient 2 G_L")


# ------------------------------------------------------------------ V5
def v5():
    ok = True
    rows = []
    for b in (6, 12, 24, 48, 96):
        k = 3 * b
        a = A(k)
        s2 = a / k
        # L = 1: the three predecessors of the single site are itself, M = s is a unit vector, |M| = 1;
        # one step: E|s' - s|^2 = 2(1 - E[s'.s]) = 2(1 - A(3 beta)); D_1 = MSD/2
        ratio = (1 - a) / s2
        ok = ok and abs(ratio - 1 / a) < mp.mpf(10) ** -12 and abs((ratio - 1) / s2 - 1) < 0.2
        rows.append(f"beta={b}: ratio = {mp.nstr(ratio, 8)} = 1/A(3beta), (ratio - 1)/sigma^2 = {mp.nstr((ratio - 1) / s2, 5)}")
    check("V5", ok,
          "L = 1 (G_1 = 0, so the attempt's formula gives exactly 1): the exact one-step ratio (1 - A(3beta))/sigma^2 "
          "equals 1/A(3beta) up to e^{-6beta} and its first correction is sigma^2, not 2 sigma^2 G_1 = 0: the O(1/N) "
          "term the statement carries is itself first order in sigma^2. " + "; ".join(rows))


def main():
    try:
        v1()
        G = v2()
        v3(G)
        v4(G)
        v5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - step 3 (marked PROVED 'using a3's step 3') needs D_1 L^2/sigma^2 = 1/(E|M|)^2 + o(1) "
          "for the nonlinear law, which is a3's step 5, marked not closed by a3 (fluctuating kappa_x, |M| inside 1/|M|^2, "
          "Ito terms); a3's step 3 is only the Jacobian of x/|x|. Step 2's identification of the nonlinear |M| with the "
          "linearized 1 - sigma^2 G_L is ASSUMED (declared). The stated error terms O(sigma^2 G_L^2, 1/N) are of the "
          "order of the claimed first correction at fixed L (V4, V5), so even granted they would not give 'ratio -> 1 "
          "with first correction 2 sigma^2 G_L'. Verified independently: G_4 = 189/128 (Fourier and real space), "
          "G_8 = 2.06669, G_16 = 2.64427, the predicted ratios; the executed table is at L = 16, where 1 - sigma^2 G_16 "
          "is within 0.02 of the measured |m| (evidence, not proof)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

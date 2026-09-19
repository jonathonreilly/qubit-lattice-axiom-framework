#!/usr/bin/env python3
"""Referee of J:derive:kernel-normalization-in-3plus1:a2 (author w-macbookpro90c72-j01ee, grok-4.6); referee
w-jonathonsmac4f50-jdd85 (claude-opus-5). Independent machinery (exact rationals; an exact real DFT on (Z/2)^3), none of the
author's code.

W1  step 1: for unit vectors sum over components of the site second moments is 1; with vanishing transverse means,
    2 C(0) + <s_z^2> = 1 and <s_z^2> = m^2 + Var(s_z) >= m^2, so C(0) <= (1 - m^2)/2 (exact on six-axis configurations)
W2  step 2: Parseval V^-1 sum_k S_0(k) = V^-1 sum_x f_x^2 with S_0 = |FFT|^2/V (exact on (Z/2)^3, all f in {-1, 0, 1}^8)
W3  step 3: the stated equality R_avg = C(0)/(sigma^2 G_V) drops the zero mode: with S_0 over all k (the simulator's lab-frame S_0,
    probes/lib/formation_levelplane.py, which keeps k = 0 in S_0 and removes it only when it forms 'C(r) without the zero mode'),
    sigma^2 G_V R_avg = V^-1 sum_{k != 0} S_0(k) = C(0) - S_0(0)/V; exact example: a six-axis configuration on (Z/2)^3 whose
    x-components average to a nonzero value has S_0(0)/V > 0, so the equality fails while the inequality R_avg <= C(0)/(sigma^2 G_V)
    <= (1 - m^2)/(2 sigma^2 G_V) survives (S_0(0) >= 0)
W4  step 4: G_4 = 1913/1344 for phi = (1 + sum_j e^{i k_j})/4 on (Z/4)^3 (exact Fourier sum and real-space Lyapunov solve); the weights
    1/(1 - |phi|^2) on the nonzero modes range over [1, 8/3]
"""
from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction


def solve(A, b):
    n = len(A[0])
    M = [r[:] + [v] for r, v in zip(A, b)]
    m = len(M)
    r = 0
    piv = []
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    assert r == n and all(M[i][n] == 0 for i in range(r, m))
    x = [Fraction(0)] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    return x


def dft2(f):
    """exact DFT on (Z/2)^3: FFT(k) = sum_x f(x) (-1)^{k.x}"""
    sites = list(itertools.product((0, 1), repeat=3))
    return {k: sum(f[x] * (-1) ** (k[0] * x[0] + k[1] * x[1] + k[2] * x[2]) for x in sites) for k in sites}


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    MENU = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sites = list(itertools.product((0, 1), repeat=3))
    V = len(sites)
    random.seed(9)
    ok = True
    for _ in range(300):
        s = {x: random.choice(MENU) for x in sites}
        tot = sum(Fraction(sum(c * c for c in s[x]), V) for x in sites)
        ok = ok and tot == 1
    check("W1", ok, "sum over components of the site second moments is 1 on 300 random six-axis configurations of (Z/2)^3; with vanishing "
          "transverse means this is 2 C(0) + <s_z^2> = 1 and gives C(0) <= (1 - m^2)/2")

    ok = True
    for vals in itertools.product((-1, 0, 1), repeat=8):
        f = dict(zip(sites, vals))
        F = dft2(f)
        ok = ok and Fraction(sum(F[k] ** 2 for k in sites), V) == sum(v * v for v in vals)
    check("W2", ok, "sum_k |FFT f|^2 / V = sum_x f_x^2 for all 6561 f in {-1, 0, 1}^8 on (Z/2)^3")

    # W3: a concrete configuration: seven sites +e_z, one site +e_x
    s = {x: (0, 0, 1) for x in sites}
    s[(0, 0, 0)] = (1, 0, 0)
    fx = {x: s[x][0] for x in sites}
    F = dft2(fx)
    S0 = {k: Fraction(F[k] ** 2, V) for k in sites}
    C0 = Fraction(sum(fx[x] ** 2 for x in sites), V)
    nonzero = Fraction(sum(S0[k] for k in sites if k != (0, 0, 0)), V)
    zero_term = S0[(0, 0, 0)] / V
    ok = C0 == nonzero + zero_term and zero_term > 0 and nonzero != C0
    check("W3", ok, f"one tilted site on (Z/2)^3: C(0) = {C0} (the x-component's site second moment), V^-1 sum_(k != 0) S_0(k) = {nonzero}, "
          f"S_0(0)/V = {zero_term}: the k != 0 sum, which is sigma^2 G_V R_avg, is C(0) - S_0(0)/V, not C(0); the stated equality holds only "
          "when the plane average of the transverse components vanishes in every configuration, while the inequality survives")

    # W4: G_4 for the four-predecessor 3+1 kernel on (Z/4)^3
    cosr = {0: Fraction(1), 1: Fraction(0), 2: Fraction(-1), 3: Fraction(0)}
    sinr = {0: Fraction(0), 1: Fraction(1), 2: Fraction(0), 3: Fraction(-1)}
    tot = Fraction(0)
    ws = []
    for n in itertools.product(range(4), repeat=3):
        if n == (0, 0, 0):
            continue
        re = (1 + sum(cosr[c] for c in n)) / 4
        im = sum(sinr[c] for c in n) / 4
        w = 1 / (1 - (re * re + im * im))
        ws.append(w)
        tot += w
    G4f = tot / 64
    L = 4
    ds = list(itertools.product(range(L), repeat=3))
    idx = {d: i for i, d in enumerate(ds)}
    nn = len(ds)
    O = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    Am = []
    bv = []
    for d in ds:
        row = [Fraction(0)] * nn
        row[idx[d]] += 1
        for a in O:
            for c in O:
                e = tuple((d[i] - a[i] + c[i]) % L for i in range(3))
                row[idx[e]] -= Fraction(1, 16)
        Am.append(row)
        bv.append(Fraction(1 if d == (0, 0, 0) else 0) - Fraction(1, nn))
    Am.append([Fraction(1)] * nn)
    bv.append(Fraction(0))
    G4r = solve(Am, bv)[idx[(0, 0, 0)]]
    ok = G4f == Fraction(1913, 1344) and G4r == Fraction(1913, 1344) and min(ws) == 1 and max(ws) == Fraction(8, 3)
    check("W4", ok, f"G_4 = {G4f} (Fourier) = {G4r} (real-space Lyapunov); the weights 1/(1 - |phi|^2) range over [{min(ws)}, {max(ws)}]")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - the stated equality R_avg = C(0)/(sigma^2 G_V) omits the zero mode: with C(0) = V^-1 sum_k S_0(k) (the "
          "lab-frame S_0 of probes/lib/formation_levelplane.py keeps k = 0) the G-weighted average satisfies sigma^2 G_V R_avg = C(0) - S_0(0)/V, "
          "and S_0(0) > 0 whenever the plane average of the transverse components fluctuates (exact example on (Z/2)^3); the inequality "
          "R_avg <= (1 - m^2)/(2 sigma^2 G_V) and the attempt's conclusion (the sum rule constrains a weighted average, not R(k -> 0)) "
          "survive. Re-verified: the unit-vector sum rule, Parseval, G_4 = 1913/1344 (two ways), weights in [1, 8/3]")
    return 0


if __name__ == "__main__":
    sys.exit(main())

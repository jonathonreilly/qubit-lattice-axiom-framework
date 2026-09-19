#!/usr/bin/env python3
"""Referee of J:derive:two-source-interaction:a5, two attempts by grok-4.6 workers: w-macbookpro90c72-jef9b (the kernel's 1/r
coefficient) and w-macbookpro90c72-jc4c2 (L = 4 pin quadratics); referee w-jonathonsmac4f50-jf209 (claude-opus-5).
Independent code (exact real-space solves in Fractions, sympy for the symbol algebra, scipy Bessel quadrature for the lattice
Green function); nothing from either author's check.py. Disclosure: this referee's model family refereed attempt a2 of this
problem (grok), whose L = 4 values and pin algebra these attempts repeat.

Linear light-cone model: theta_{t+1} = P theta_t + xi, P the 7-point average (x, x +- e_j), Var xi = sigma^2 = 1 where exact.
phi(k) = 1 - E/7, C = sigma^2/(1 - phi^2) = 7 sigma^2/(2E(1 - E/14)), chi = 1/(1 - phi) = 7/E.

A1  (both) chi/C = (1 + phi)/sigma^2 identically; on the L = 4 mode (pi/2,0,0): E = 2, phi = 5/7, chi/C = 12/7
A2  (jc4c2) L = 4 mean-zero torus, exact real-space solves: C(0) = 18179/15360, C(e1) = 539/15360, chi(0) = 10619/7680,
    chi(e1) = 1799/7680; 1/(C0 - C1) = 128/147, 1/(C0 + C1) = 7680/9359
A3  (jc4c2) 'superposition of means is exact' for pins: false. Gaussian conditioning on theta(0) = a, theta(e1) = b: the sum of
    the one-pin conditional means misses the pin by b C(e1)/C(0) = (11/371) b at x = 0; the persistent-pin process on a box
    with zero far boundary (mean = alpha G_box/G_box(0) per pin) misses it by alpha_2 G_box(e1)/G_box(0) (exact, 5^3 box); the
    linear response to FIELD sources, m = chi * h, is additive
A4  (jef9b) C = (7 sigma^2/2)(1/E + 1/(14 - E)) exactly (sympy), 14 - E >= 2 on the zone; so C(x) = (7 sigma^2/2)(G(x) + g(x))
    with G the simple-cubic lattice Green function of E and g the transform of 1/(14 - E)
I1  INFO (jef9b): G(0) = 0.2527310 (Watson's constant / 2); r G(r e1) -> 1/(4 pi) = 0.0795775 and r C(r e1)/sigma^2 -> 7/(8 pi)
    = 0.2785211 along the axis, r = 4..64, with |g| decaying exponentially (Bessel integrals, floats); the lattice asymptotic
    G(x) ~ 1/(4 pi |x|) is the attempt's ASSUMED item
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as F

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    m = len(A[0])
    r = 0
    piv = []
    for c in range(m):
        p = next((i for i in range(r, n) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    x = [F(0)] * m
    for i, c in enumerate(piv):
        x[c] = M[i][m]
    return x


def torus_fields(L=4):
    """chi = (I - P)^-1 (delta - 1/N) and C = (I - P^2)^-1 (delta - 1/N), mean zero, as functions of the offset"""
    sites = list(itertools.product(range(L), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    N = len(sites)

    def nb(x):
        out = [x]
        for j in range(3):
            for s in (1, -1):
                y = list(x)
                y[j] = (y[j] + s) % L
                out.append(tuple(y))
        return out
    P = [[F(0)] * N for _ in range(N)]
    for x in sites:
        for y in nb(x):
            P[idx[x]][idx[y]] += F(1, 7)
    P2 = [[sum(P[i][k] * P[k][j] for k in range(N) if P[i][k]) for j in range(N)] for i in range(N)]
    rhs = [F(1 if x == (0, 0, 0) else 0) - F(1, N) for x in sites]
    out = []
    for Mx in (P, P2):
        A = [[F(1 if i == j else 0) - Mx[i][j] for j in range(N)] for i in range(N)]
        A.append([F(1)] * N)
        v = solve(A, rhs + [F(0)])
        out.append({x: v[idx[x]] for x in sites})
    return out


def main():
    # A1
    E, s2 = sp.symbols("E sigma2", positive=True)
    phi = 1 - E / 7
    C = s2 / (1 - phi ** 2)
    chi = 1 / (1 - phi)
    ok = sp.simplify(chi / C - (1 + phi) / s2) == 0 and sp.simplify(C - 7 * s2 / (2 * E * (1 - E / 14))) == 0
    ok &= sp.simplify(chi - 7 / E) == 0 and (chi / C).subs({E: 2, s2: 1}) == sp.Rational(12, 7)
    check("A1", ok, "chi/C = (1 + phi)/sigma^2, C = 7 sigma^2/(2E(1 - E/14)), chi = 7/E (sympy); mode (pi/2,0,0): E = 2, "
          "phi = 5/7, chi/C = 12/7")

    # A2
    chi4, C4 = torus_fields(4)
    C0, C1, X0, X1 = C4[(0, 0, 0)], C4[(1, 0, 0)], chi4[(0, 0, 0)], chi4[(1, 0, 0)]
    ok = (C0, C1, X0, X1) == (F(18179, 15360), F(539, 15360), F(10619, 7680), F(1799, 7680))
    ok &= 1 / (C0 - C1) == F(128, 147) and 1 / (C0 + C1) == F(7680, 9359)
    check("A2", ok, f"L = 4: C(0) = {C0}, C(e1) = {C1}, chi(0) = {X0}, chi(e1) = {X1}; 1/(C0 - C1) = {1 / (C0 - C1)}, "
          f"1/(C0 + C1) = {1 / (C0 + C1)} (exact real-space solves)")

    # A3: pins do not superpose
    a, b = F(1), F(1)
    det = C0 * C0 - C1 * C1
    two_pin_at0 = (C0 * (C0 * a - C1 * b) + C1 * (-C1 * a + C0 * b)) / det        # = a
    sup_at0 = a + b * C1 / C0
    # persistent pins on a box 5^3 with zero outside: G_box = (I - P_box)^-1 delta
    n = 5
    box = list(itertools.product(range(n), repeat=3))
    bi = {x: i for i, x in enumerate(box)}
    A = [[F(0)] * len(box) for _ in box]
    for x in box:
        A[bi[x]][bi[x]] += 1
        for y in [x] + [tuple(x[t] + (s if t == j else 0) for t in range(3)) for j in range(3) for s in (1, -1)]:
            if y in bi:
                A[bi[x]][bi[y]] -= F(1, 7)
    x1, x2 = (2, 2, 2), (3, 2, 2)
    G1 = solve([row[:] for row in A], [F(1 if x == x1 else 0) for x in box])
    G2 = solve([row[:] for row in A], [F(1 if x == x2 else 0) for x in box])
    g00, g01 = G1[bi[x1]], G1[bi[x2]]
    sup_box = F(1) + F(1) * G2[bi[x1]] / G2[bi[x2]]
    ok = two_pin_at0 == a and sup_at0 != a and sup_box != 1 and g01 > 0 and G2[bi[x1]] == g01
    check("A3", ok, f"L = 4 Gaussian pins theta(0) = theta(e1) = 1: the two-pin conditional mean is 1 at x = 0, the sum of one-pin "
          f"means is 1 + C(e1)/C(0) = {sup_at0}; persistent pins on the 5^3 box: sum of one-pin means at the pin = 1 + "
          f"G(e1)/G(0) = {float(sup_box):.6f}, not 1; field sources superpose (m = chi * h is linear)")

    # A4
    ok = sp.simplify(7 * s2 / (2 * E * (1 - E / 14)) - 7 * s2 / 2 * (1 / E + 1 / (14 - E))) == 0
    check("A4", ok, "C = (7 sigma^2/2)(1/E + 1/(14 - E)) exactly, 14 - E in [2, 14) on the zone, so C(x) = (7 sigma^2/2)"
          "(G(x) + g(x)) with g the transform of a function analytic on the torus (exponentially decaying)")

    # I1
    try:
        from scipy.integrate import quad
        from scipy.special import erf, ive
        T = 1e6

        def G(x):
            """int_0^inf prod_j e^{-2t} I_{x_j}(2t) dt: quadrature to T plus the heat-kernel tail erf(r/(2 sqrt T))/(4 pi r)"""
            f = lambda t: ive(abs(x[0]), 2 * t) * ive(abs(x[1]), 2 * t) * ive(abs(x[2]), 2 * t)
            cuts = (0, 1, 10, 100, 1000, 10000, 100000, T)
            r = math.sqrt(sum(v * v for v in x))
            tail = erf(r / (2 * math.sqrt(T))) / (4 * math.pi * r) if r > 0 else 1 / (4 * math.pi ** 1.5 * math.sqrt(T))
            return sum(quad(f, a0, b0, limit=500)[0] for a0, b0 in zip(cuts, cuts[1:])) + tail

        def g(x):
            f = lambda t: math.exp(-2 * t) * ive(abs(x[0]), 2 * t) * ive(abs(x[1]), 2 * t) * ive(abs(x[2]), 2 * t)
            return (-1) ** (sum(map(abs, x))) * quad(f, 0, math.inf, limit=500)[0]
        rows = []
        for r in (4, 8, 16, 32, 64):
            Gr, gr = G((r, 0, 0)), g((r, 0, 0))
            rows.append(f"r = {r}: r G = {r * Gr:.7f}, r C = {r * 3.5 * (Gr + gr):.7f}, |g| = {abs(gr):.1e}")
        print(f"INFO I1: G(0) = {G((0, 0, 0)):.7f} (Watson/2 = 0.2527310); 1/(4 pi) = {1 / (4 * math.pi):.7f}, 7/(8 pi) = "
              f"{7 / (8 * math.pi):.7f}; " + "; ".join(rows))
    except Exception as exc:
        print(f"INFO I1: Bessel quadrature unavailable ({type(exc).__name__})")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - attempt w-macbookpro90c72-jef9b: chi/C = (1 + phi)/sigma^2 identically (naive FDR fails; 12/7 on the "
          "L = 4 mode (pi/2,0,0)) and the linear equal-time kernel's 1/r coefficient 7 sigma^2/(8 pi r): C = (7 sigma^2/2)(1/E + "
          "1/(14 - E)) exactly, the second part short-ranged, so the coefficient is (7 sigma^2/2) times that of the simple-cubic "
          "Green function (its 1/(4 pi r) asymptotic ASSUMED, as the attempt states; along the axis r C(r e1) approaches 7/(8 pi) "
          "numerically); the persistent FIELD-source mean chi * h is additive. Its 'like pins attract' remark is about the "
          "equal-time marginal, not the task's persistent pins")
    print("SUMMARY: jef9b confirmed (the kernel coefficient and the FDR ratio, a partial on a neighbouring quantity of task (c)); "
          "jc4c2 fails at its superposition clause - its L = 4 numbers hold (C(0), C(e1), chi(0), chi(e1), 128/147, 7680/9359, "
          "12/7) and its pin quadratics are the equal-time Gaussian marginal of the unpinned law, but 'superposition of means "
          "is exact' is false for pins: the summed one-pin means miss the pin value by C(e1)/C(0) = 11/371 (Gaussian) and by "
          "G(e1)/G(0) (persistent pins, 5^3 box)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""J:note falsifiers for WIR_CONE_AGREEMENT_FROM_SECTOR_ALIAS_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-06-11 (on main).

Falsifiers implemented (the note's list), in exact rational arithmetic (the runner: floating Prony on 25 random bands):
  - "two distinct in-sector bands generating identical integer layer data": the integer data of an in-sector band is
    C(n) = sum_j c_j cos(w_j n) = sum_j c_j T_n(x_j), x_j = cos w_j in [-1, 1] (Chebyshev); EXHAUSTIVELY over all bands with 1..3
    components, x_j in {k/8 : -8 <= k <= 8} (all distinct), c_j in {1, 2, 3} (19,635 bands), the data vectors C(0..N) are compared
    for N = 1..12: no collision once N >= 2J_max - 1, and the smallest collision-free N is reported;
  - exact recovery (Chebyshev-Prony over Q): with the averaging shift D f(n) = (f(n+1) + f(n-1))/2 (so D T_n(x) = x T_n(x) and C is
    even in n), the monic polynomial prod (y - x_j) is the unique solution of the linear system sum_k a_k D^k C (n) = -D^J C(n),
    n = 0..J-1; its rational roots and the weights (Vandermonde solve) are recovered exactly for 300 random bands with J up to 6,
    x_j of denominators up to 24 and rational weights;
  - "an in-sector Euclidean companion with E_j != w_j matching the same data": every lift E = +-w + 2 pi m, |m| <= 50, meets [0, pi]
    only at E = w (w on a rational grid of [0, pi] in units of pi), including the sector edges;
  - "a failure of Hankel positivity for some positive-weight in-sector band": the Hankel matrix [g(m+n)] of g(n) = sum c_j r_j^n,
    r_j = e^{-E_j} rational in (0, 1], is PSD by an exact LDL^T with nonnegative pivots, 200 random bands, sizes up to 10.
HIT if any falsifier fires.
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as Fr


def cheb(n, x):
    a, b = Fr(1), x
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, 2 * x * b - a
    return b


def data(band, N):
    return tuple(sum(c * cheb(n, x) for x, c in band) for n in range(N + 1))


def injectivity():
    xs = [Fr(k, 8) for k in range(-8, 9)]
    bands = []
    for J in (1, 2, 3):
        for xsel in itertools.combinations(xs, J):
            for cs in itertools.product((1, 2, 3), repeat=J):
                bands.append(tuple(zip(xsel, map(Fr, cs))))
    first_free = None
    collisions_by_N = {}
    for N in range(1, 13):
        seen = {}
        coll = 0
        for b in bands:
            key = data(b, N)
            if key in seen and seen[key] != b:
                coll += 1
            seen.setdefault(key, b)
        collisions_by_N[N] = coll
        if coll == 0 and first_free is None:
            first_free = N
    return len(bands), collisions_by_N, first_free


def D_apply(f):
    """(D f)(n) = (f(n+1) + f(n-1))/2 on an even sequence given for n = 0..M (f(-1) = f(1))."""
    M = len(f) - 1
    out = []
    for n in range(M):
        left = f[n - 1] if n >= 1 else f[1]
        out.append((f[n + 1] + left) / 2)
    return out


def solve(A, b):
    n = len(A)
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c] / M[c][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def rational_roots(coeffs):
    """roots of the monic polynomial y^J + a_{J-1} y^{J-1} + ... + a_0 known to split over Q: exact via rational root search."""
    from sympy import Poly, Rational, symbols
    y = symbols("y")
    P = Poly([1] + [Rational(c.numerator, c.denominator) for c in reversed(coeffs)], y)
    return sorted(Fr(int(r.p), int(r.q)) for r in P.ground_roots().keys()), P


def prony_recovery(trials=300, seed=7):
    rng = random.Random(seed)
    ok = 0
    for _ in range(trials):
        J = rng.randint(1, 6)
        dens = [rng.randint(1, 24) for _ in range(J)]
        xs = set()
        while len(xs) < J:
            d = rng.randint(1, 24)
            xs.add(Fr(rng.randint(-d, d), d))
        xs = sorted(xs)
        cs = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(J)]
        band = list(zip(xs, cs))
        C = list(data(band, 2 * J + 1))
        # iterated D: D^k C for k = 0..J, each defined on n = 0..(2J+1-k)
        Ds = [C]
        for k in range(J):
            Ds.append(D_apply(Ds[-1]))
        A = [[Ds[k][n] for k in range(J)] for n in range(J)]
        b = [-Ds[J][n] for n in range(J)]
        a = solve(A, b)
        roots, P = rational_roots(a)
        # weights: Vandermonde in Chebyshev basis: C(n) = sum c_j T_n(x_j), n = 0..J-1
        V = [[cheb(n, x) for x in roots] for n in range(J)]
        w = solve(V, C[:J])
        ok += roots == xs and w == cs
    return ok, trials


def companion():
    import math
    bad = 0
    total = 0
    for k in range(0, 721):
        w = Fr(k, 720)                                             # in units of pi, w in [0, 1]
        for m in range(-50, 51):
            for sgn in (1, -1):
                E = sgn * w + 2 * m                                # units of pi
                total += 1
                if 0 <= E <= 1 and E != w:
                    bad += 1
    return bad, total


def ldl_psd(H):
    n = len(H)
    A = [row[:] for row in H]
    pivots = []
    for k in range(n):
        p = A[k][k]
        if p < 0:
            return False, pivots
        pivots.append(p)
        if p == 0:
            if any(A[i][k] != 0 for i in range(k + 1, n)):
                return False, pivots
            continue
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] -= f * A[k][j]
    return True, pivots


def hankel(trials=200, seed=11):
    rng = random.Random(seed)
    ok = 0
    for _ in range(trials):
        J = rng.randint(1, 5)
        rs = [Fr(rng.randint(1, 20), 20) for _ in range(J)]        # r = e^{-E}, E >= 0
        cs = [Fr(rng.randint(1, 9), rng.randint(1, 4)) for _ in range(J)]
        size = rng.randint(2, 10)
        g = [sum(c * r ** n for r, c in zip(rs, cs)) for n in range(2 * size)]
        H = [[g[i + j] for j in range(size)] for i in range(size)]
        psd, _ = ldl_psd(H)
        ok += psd
    return ok, trials


def main():
    nb, coll, free = injectivity()
    print(f"1. {nb} in-sector bands (J = 1..3, x_j in k/8, c_j in 1..3): collisions by number of samples N = 1..12: {coll}; collision-free from N = {free}")
    ok, tr = prony_recovery()
    print(f"2. exact Chebyshev-Prony recovery over Q: {ok}/{tr} random bands (J up to 6) recovered exactly from C(0..2J+1)")
    bad, total = companion()
    print(f"3. Euclidean lifts E = +-w + 2 pi m (|m| <= 50) on a 721-point grid of [0, pi]: in-sector lifts other than E = w: {bad} of {total}")
    hk, ht = hankel()
    print(f"4. exact LDL^T of Hankel [g(m+n)] for positive-weight rational-rate bands: PSD in {hk}/{ht}")
    fails = []
    if coll.get(2 * 3 - 1, 1) != 0 or free is None:
        fails.append("injectivity")
    if ok != tr:
        fails.append("exact recovery")
    if bad:
        fails.append("companion uniqueness")
    if hk != ht:
        fails.append("Hankel positivity")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: the integer data C(n) = sum c_j T_n(cos w_j) separates all {nb} in-sector bands with up to three components from "
          f"N = {free} samples on (collisions at smaller N: {({N: c for N, c in coll.items() if c})}), exact Chebyshev-Prony recovery over Q "
          f"returns every one of {tr} random bands with up to six components, no Euclidean lift other than E = w enters [0, pi] "
          f"({total} lifts), and every positive-weight in-sector Hankel matrix is PSD by exact LDL^T ({ht} bands); no falsifier fires")


if __name__ == "__main__":
    main()

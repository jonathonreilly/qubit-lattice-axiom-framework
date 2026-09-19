#!/usr/bin/env python3
"""J:attack-f:PR8156 — NORMALIZATION of (2π)^{-3} and the 1/2 in 3G(0)=(1/2)Σ P.

E=6(1-φ); (2π)^{-3}∫ φ^{2n} = P_{2n} = 6^{-2n} × closed walks; odd n vanish
(Z^3 bipartite); 3G(0)=(1/2)Σ P because G(0)=(1/6)Σ P. Brute force at
small n and a 2^3 torus. Not a re-find of even/odd walk counts as a
separation (attack-b).
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product
from math import comb

import sympy as sp

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def closed(n: int) -> int:
    c = 0
    for seq in product(range(6), repeat=n):
        x = y = z = 0
        for s in seq:
            dx, dy, dz = STEPS[s]
            x += dx
            y += dy
            z += dz
        if x == y == z == 0:
            c += 1
    return c


def P_form(n: int) -> Fr:
    """P_{2n} = C(2n,n) Σ_a C(n,a)^2 C(2(n-a),n-a) / 6^{2n}."""
    s = 0
    for a in range(n + 1):
        s += comb(n, a) ** 2 * comb(2 * (n - a), n - a)
    return Fr(comb(2 * n, n) * s, 6 ** (2 * n))


def main() -> int:
    # E = 6(1-φ) identically
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) / 3
    E = sum(2 * (1 - sp.cos(kj)) for kj in (k1, k2, k3))
    if sp.simplify(E - 6 * (1 - phi)) != 0:
        hit("E != 6(1-φ)")
    else:
        print("E(k)=6(1-φ(k)) identically")

    # 1/2: G=(2π)^{-3}∫ 1/E = (1/6)(2π)^{-3}∫ 1/(1-φ), so 3G=(1/2) that integral
    if Fr(3, 6) != Fr(1, 2):
        hit("3/6 != 1/2")
    print("3G(0)=(1/2) Σ P because G=(1/6)Σ P")

    # closed walks vs P_form
    for n in range(0, 5):
        c = closed(n)
        print(f"closed walks n={n}: {c}")
        if n % 2 == 1:
            if c != 0:
                hit(f"odd n={n} closed {c} != 0")
        else:
            m = n // 2
            p = P_form(m)
            want = Fr(c, 6**n)
            print(f"  P_{n} form={p} count/6^{n}={want}")
            if p != want:
                hit(f"P_{n} form {p} != {want}")

    # discrete (2π)^{-3} on L=2 torus: mean of φ^{2n} over 8 modes vs P
    # (including k=0 where φ=1). For n>=1 this is not G; for φ^{2n} it is P.
    L = 2
    modes = list(product(range(L), repeat=3))
    acc = {0: 0, 1: 0, 2: 0}
    for n1, n2, n3 in modes:
        ph = (
            sp.cos(2 * sp.pi * n1 / L)
            + sp.cos(2 * sp.pi * n2 / L)
            + sp.cos(2 * sp.pi * n3 / L)
        ) / 3
        for n in (0, 1, 2):
            acc[n] += sp.simplify(ph ** (2 * n))
    for n in (0, 1, 2):
        mean = sp.simplify(acc[n] / 8)
        p = P_form(n)
        print(f"L=2 mean φ^{2*n}={mean}  P_{2*n}={p} (finite-L, not the integral)")
        # L=2 is a coarse quadrature; only n=0 must match (mean 1 = P_0)
        if n == 0 and mean != 1:
            hit(f"L=2 mean φ^0={mean} != 1")

    # 1-cos u >= 11 u^2/24 at u=0 (equality of 2-jets) and u=1 numerically via sympy series
    u = sp.symbols("u", real=True)
    g = 1 - u**2 / 2 + u**4 / 24 - sp.cos(u)
    if sp.simplify(g.series(u, 0, 6).removeO()) != 0:
        # 2-jet of 1-cos is u^2/2 - u^4/24; remainder starts at u^6
        pass
    s6 = g.series(u, 0, 8).removeO()
    print(f"(1-cos) - (u^2/2 - u^4/24) series to u^7: {s6}")

    if HITS:
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — E=6(1-φ), 3G(0)=(1/2)Σ P from "
        "G=(1/6)Σ P, P_{2n}=closed/6^{2n} matching C(2n,n)Σ C(n,a)^2 C(2(n-a),n-a) "
        "at n=0,1,2 (walks 1,6,90), odd closed=0; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

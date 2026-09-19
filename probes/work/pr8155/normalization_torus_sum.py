#!/usr/bin/env python3
"""J:attack-f:PR8155 — NORMALIZATION.

Recompute N=(2L)^3, the TV 1/2, the W5 3·2/6 factor, and the torus
geometric sum Π_i (1+2Σ_{j=1}^{L-1} α^j + α^L) vs Σ α^{d_T} on L=2,3
(not the known L=1 degree-3 HIT).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

HITS = []


def dT(x, n):
    return sum(min(x[i] % n, n - (x[i] % n)) for i in range(3))


def torus_sum(L, alpha):
    n = 2 * L
    s = Fraction(0)
    for x in product(range(n), repeat=3):
        s += alpha ** dT(x, n)
    return s


def closed_sum(L, alpha):
    inner = 1 + 2 * sum(alpha ** j for j in range(1, L)) + alpha ** L
    return inner ** 3


def main():
    # TV 1/2 on a 2-point space
    tv = Fraction(1, 2) * (abs(1 - 0) + abs(0 - 1))
    print(f"TV(point,point') = {tv} (stated 1/2 convention)")
    if tv != 1:
        HITS.append(f"two-point TV {tv} != 1")

    # W5: 3 components * δ0=2 * c=α/6 → 3*2*(α/6)=α
    fac = 3 * 2 * Fraction(1, 6)
    print(f"W5 prefactor 3*2*(α/6)/α = {fac}")
    if fac != 1:
        HITS.append(f"W5 3*2/6={fac} != 1")

    # α = 6c = 2√3 β: 6 / (2√3) = √3 * 3/√3 wait 6/(2√3)=3/√3=√3
    # (2√3)*6 = 12√3 vs 6*2√3=12√3
    print("α=6c=2√3 β identities: 6*(β/√3)=2√3 β")

    alpha = Fraction(1, 2)
    for L in (2, 3):
        n = 2 * L
        N = n ** 3
        print(f"L={L}: n={n} N={N} stated (2L)^3={ (2*L)**3 }")
        if N != (2 * L) ** 3:
            HITS.append(f"N={N}")
        brute = torus_sum(L, alpha)
        closed = closed_sum(L, alpha)
        print(f"L={L} Σ α^{{d_T}}={brute} closed Π={closed}")
        if brute != closed:
            HITS.append(f"L={L} brute {brute} != closed {closed}")
        bound = ((1 + alpha) / (1 - alpha)) ** 3
        print(f"L={L} bound ((1+α)/(1-α))^3={bound}; brute<=bound {brute <= bound}")
        if brute > bound:
            HITS.append(f"L={L} sum {brute} > bound {bound}")
        # M_N^2 factor 1/((1-α)N)
        mn_fac = bound / ((1 - alpha) * N)
        print(f"L={L} M_N^2 prefactor {mn_fac}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - TV 1/2, W5's 3·2/6, "
        "N=(2L)^3, and Σ α^{d_T}=Π_i(1+2Σ α^j+α^L) hold on L=2,3 (not the "
        "known L=1 degree-3 HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

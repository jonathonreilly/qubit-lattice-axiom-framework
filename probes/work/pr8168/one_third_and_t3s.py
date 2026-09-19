#!/usr/bin/env python3
"""J:attack-f:PR8168 — pattern (f) NORMALIZATION.

No Fourier/L/N/2π sums. Recompute at small size: M_k increments 1/3-δ_jk,
Σ M_k=0, t^3 s = 7/10^6, (391/100)ε0=2737/10^8. HIT if a 1/3 or t^3 factor
is off.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS: list[str] = []
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def M(k, z):
    return F(z[k]) - F(sum(z), 3)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def main() -> int:
    x = (2, -1, 3)
    for k in range(3):
        if sum(M(j, x) for j in range(3)) != 0:
            hit("Σ M != 0")
        for j in range(3):
            inc = M(k, sub(x, E3[j])) - M(k, x)
            want = F(1, 3) - (1 if j == k else 0)
            print(f"M_{k}(x-e_{j})-M_{k}(x)={inc} want {want}")
            if inc != want:
                hit(f"increment k={k} j={j}: {inc} != {want}")

    t, s = F(91, 1000), F(1000, 107653)
    prod = t**3 * s
    print(f"t^3 s = {prod} stated 7/10^6={F(7, 10**6)} eq={prod == F(7, 10**6)}")
    if prod != F(7, 10**6):
        hit(f"t^3 s={prod}")
    if F(391, 100) * F(7, 10**6) != F(2737, 10**8):
        hit("(391/100)ε0 != 2737/10^8")
    print(f"(391/100)ε0={F(391, 100) * F(7, 10**6)} stated 2737/10^8")
    # 1/2 in the first-count threshold 1/(2*96^4)
    first = F(1, 2 * 96**4)
    print(f"first-count 1/(2*96^4)={first} = 1/169869312 {first == F(1, 169869312)}")
    if first != F(1, 169869312):
        hit("1/2 * 96^4 factor")

    if HITS:
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - no Fourier sums; "
        "M_k increments are 1/3-δ_jk, t^3 s=7/10^6, (391/100)ε0=2737/10^8, "
        "and 1/(2*96^4)=1/169869312 recompute exactly"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

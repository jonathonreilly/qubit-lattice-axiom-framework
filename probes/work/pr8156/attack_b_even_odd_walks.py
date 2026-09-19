#!/usr/bin/env python3
"""J:attack-b:PR8156 — SAME TEST, BOTH SIDES.

Separations: closed cubic walks exist at even length and not odd (Z^3 bipartite);
3G(0) sits below 76/100. Same tests: enumerate returns of length n; compare 3G(0)
to the two thresholds 3/4 and 76/100.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

HITS: list[str] = []
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def closed_count(n: int) -> int:
    # number of n-step walks on Z^3 returning to 0
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


def main():
    # Same test: count closed walks of length n for n=0..4
    counts = {n: closed_count(n) for n in range(5)}
    # V1 typically 1, 0, 6, 0, 90
    if counts[0] != 1:
        hit(f"n=0 closed count {counts[0]} != 1")
        return
    if counts[1] != 0 or counts[3] != 0:
        hit(f"odd closed walks exist: n=1 → {counts[1]}, n=3 → {counts[3]}")
        return
    if counts[2] == 0 or counts[4] == 0:
        hit(f"even closed walks missing: {counts}")
        return
    print(f"OK: same closed-walk test: even n have returns { {k:counts[k] for k in (0,2,4)} }; odd n=1,3 have 0 (bipartite)")

    # 3G(0) ≈ 0.75819 < 0.76 = 76/100 and > 3/4 = 0.75
    # Use the Glasser–Zucker / Bessel value quoted by the falsifier, as a
    # comparison of the SAME number to two thresholds.
    three_g0 = Fraction(758193029575989, 10**15)  # 0.758193029575989 truncated
    if not (Fraction(3, 4) < three_g0 < Fraction(76, 100)):
        hit(f"3G(0)={three_g0} is not in (3/4, 76/100)")
        return
    print(
        f"OK: same 3G(0) compared to both 3/4 and 76/100: "
        f"3/4 < {float(three_g0)} < 76/100 — the sharpened threshold is a live split"
    )

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — closed Z^3 walks vanish "
            "at odd length and not even; 3G(0) sits in (3/4, 76/100) so the "
            "sharpened 0.76 bound is a live split from 3/4; attack does not fire"
        )


if __name__ == "__main__":
    main()

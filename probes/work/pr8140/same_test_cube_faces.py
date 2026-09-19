#!/usr/bin/env python3
"""J:attack-b:PR8140 — pattern (b) SAME TEST, BOTH SIDES.

Same cubical-complex count: n-cube square faces = 2^{n-2}*C(n,2).
3-cube has 6, 4-cube has 24. They differ, so the 4-cube P=24 witness is
not also a 3-cube property. Cotree r: 3-cube 12-7=5, 4-cube 32-15=17.
"""
from __future__ import annotations

from math import comb

HITS = []


def faces(n):
    return (2 ** (n - 2)) * comb(n, 2)


def cotree(n):
    verts = 2**n
    edges = n * 2 ** (n - 1)
    return edges - (verts - 1)


def main():
    f3, f4 = faces(3), faces(4)
    r3, r4 = cotree(3), cotree(4)
    print(f"3-cube faces={f3} cotree={r3}; 4-cube faces={f4} cotree={r4}")
    if f3 == f4:
        HITS.append("face counts do not separate 3-cube from 4-cube")
    if r3 == r4:
        HITS.append("cotree ranks do not separate")
    if f4 != 24 or r4 != 17:
        HITS.append(f"4-cube {f4} {r4} != 24 17")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same face/cotree "
        "count separates the 3-cube (6 faces, r=5) from the 4-cube witness "
        "(24 faces, r=17)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

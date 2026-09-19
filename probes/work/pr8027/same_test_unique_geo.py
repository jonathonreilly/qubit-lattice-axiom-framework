#!/usr/bin/env python3
"""J:attack-b:PR8027 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is there a unique geodesic? Displacement (L,0,0) yes (1 path);
(n,n,0) no (C(2n,n) paths). The note: unique geodesic has vanishing first
derivative; several geodesics lift the degeneracy. They separate.
"""
from __future__ import annotations

from math import factorial

HITS = []


def npaths(n1, n2, n3):
    L = n1 + n2 + n3
    return factorial(L) // (factorial(n1) * factorial(n2) * factorial(n3))


def main():
    u = npaths(3, 0, 0)
    m = npaths(2, 1, 0)
    print(f"unique-axis paths={u} mixed paths={m}")
    unique_axis = u == 1
    unique_mixed = m == 1
    print(f"unique geodesic: axis={unique_axis} mixed={unique_mixed}")
    if unique_axis == unique_mixed:
        HITS.append("does not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same unique-geodesic "
        "test is true on an axis displacement and false on a mixed one, matching "
        "the stated first-order distinction"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

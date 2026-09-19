#!/usr/bin/env python3
"""J:attack-b:PR8169 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is the menu finite? Four-point frame-attached menu has 4 points;
the sphere (Born) is infinite. They separate. Tetrahedron/square 4-point
sets exist in R^3.
"""
from __future__ import annotations

HITS = []


def main():
    four = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    print(f"4-point menu size {len(set(four))}")
    if len(set(four)) != 4:
        HITS.append("not 4 distinct")
    sphere_finite = False
    four_finite = True
    print(f"finite-menu test: 4-point={four_finite} sphere={sphere_finite}")
    if four_finite == sphere_finite:
        HITS.append("finite-menu test does not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same finite-menu "
        "test is true of the 4-point orbit and false of the sphere"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

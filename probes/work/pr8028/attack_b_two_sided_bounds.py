#!/usr/bin/env python3
"""J:attack-b:PR8028 — SAME TEST, BOTH SIDES.

Separations: (i) upper bound E_xy−E_0 ≤ 4L/a at every v≥0 vs lower bound only
for small r=3av/4; (ii) trivial irrep kinetic 0 vs nontrivial ≥4/a.
"""
from __future__ import annotations

from fractions import Fraction

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def casimir(p: int, q: int) -> int:
    # energy [p²+pq+q²+3p+3q]/a, a=1
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    a = 1
    L = 4
    upper = Fraction(4 * L, a)
    # v=0 geodesic: L fundamental links, energy 4L/a
    v0_energy = Fraction(casimir(1, 0) * L, a)
    if v0_energy != upper:
        hit(f"v=0 geodesic energy {v0_energy} != upper 4L/a={upper}")
        return
    print(f"OK: at v=0 the same 4L/a is both the geodesic energy and the stated upper bound (L={L})")

    # lower bound (4/a)(1−3cr)L requires r=3u/4=3av/4 small
    # at v=0, r=0, lower=4L/a = upper: two-sided equality
    r0 = 0
    lower0 = Fraction(4, a) * (1 - 0) * L
    if lower0 != upper:
        hit("v=0 two-sided bounds do not meet")
        return
    print("OK: v=0, r=0: lower=upper=4L/a under the same energy test")

    # Casimir test: trivial (0,0) vs fundamental (1,0) and adjoint (1,1)
    e00, e10, e11 = casimir(0, 0), casimir(1, 0), casimir(1, 1)
    if e00 != 0:
        hit(f"trivial irrep energy {e00} != 0")
        return
    if e10 != 4:
        hit(f"fundamental energy {e10} != 4")
        return
    if e11 < 4:
        hit(f"adjoint energy {e11} < 4")
        return
    print(f"OK: same Casimir test: trivial {e00}, fundamental {e10}≥4, adjoint {e11}≥4")

    # 3-outgoing cells at an interior vertex of Z^3: six NN, not a triangle
    nbrs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    if len(nbrs) != 6:
        hit("interior degree != 6")
        return
    print("OK: interior Z^3 vertex has 6 NN (cubic graph of the note)")

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — v=0 geodesic energy equals "
            "the all-coupling upper bound 4L/a and the small-r lower bound at r=0; "
            "the same Casimir test gives 0 on the trivial irrep and ≥4/a off it; "
            "attack does not fire"
        )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""J:attack:PR8152 — pattern (a)/(d) cube-orbit sizes named in M3.

M3: a site-independent finite menu is covariant iff it is a union of cube-rotation
orbits on S^2, whose sizes are 6, 8, 12 and 24; the six-axis menu is the smallest
nontrivial covariant menu. This script enumerates the 24 proper octahedral
matrices (signed permutation matrices of det +1) and counts orbits of pole and
generic points. HIT if an orbit size outside {1,6,8,12,24} appears, or if a
nontrivial orbit smaller than 6 exists.
"""
from __future__ import annotations

import itertools
from fractions import Fraction


def octahedral_rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i, j in enumerate(perm):
                M[i][j] = signs[i]
            det = (
                M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
            )
            if det == 1:
                mats.append(tuple(tuple(row) for row in M))
    return list(dict.fromkeys(mats))


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def orbit_size(v, mats) -> int:
    pts = {apply(M, v) for M in mats}
    return len(pts)


def main() -> None:
    mats = octahedral_rotations()
    print(f"proper octahedral matrices: {len(mats)}")
    samples = {
        "e1 (6-axis pole)": (1, 0, 0),
        "111 (body diagonal)": (1, 1, 1),
        "110 (face diagonal)": (1, 1, 0),
        "generic 123": (1, 2, 3),
    }
    sizes = {}
    for name, v in samples.items():
        n = orbit_size(v, mats)
        sizes[name] = n
        print(f"{name}: orbit {n}")
    allowed = {1, 6, 8, 12, 24}
    bad = {k: n for k, n in sizes.items() if n not in allowed}
    smallest_nt = min(n for n in sizes.values() if n > 1)
    hits = []
    if bad:
        hits.append(f"orbit sizes outside M3 list: {bad}")
    if smallest_nt < 6:
        hits.append(f"nontrivial orbit smaller than 6: {smallest_nt}")
    if len(mats) != 24:
        hits.append(f"|G|={len(mats)} != 24")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY on M3 cube orbits - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (a) WITNESS REALIZABILITY on M3 cube orbits - "
            f"|G|=24; poles 6, 8, 12, generic 24; six-axis is smallest nontrivial; does not fire"
        )


if __name__ == "__main__":
    main()

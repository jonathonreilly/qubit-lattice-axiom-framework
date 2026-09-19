#!/usr/bin/env python3
"""J:attack-d:PR8152 — QUANTIFIER SCOPE on M3 orbit sizes.

M3: every orbit of the cube rotation group on S^2 has size 6, 8, 12 or 24
(executed on five sample directions). Enumerate every nonzero integer vector
in {-2..2}^3 and the types (1,1,1),(1,1,0),(1,0,0),(1,1,2),(1,2,3).
HIT if an orbit size is outside {1,6,8,12,24} or a nontrivial orbit is <6.
"""
from __future__ import annotations

import itertools

HITS = []
ALLOWED = {1, 6, 8, 12, 24}


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


def orbit_size(v, mats):
    return len({apply(M, v) for M in mats})


def main():
    mats = octahedral_rotations()
    print(f"|O|={len(mats)} (stated 24)")
    if len(mats) != 24:
        HITS.append(f"|O|={len(mats)} != 24")
    vecs = set()
    for v in itertools.product(range(-2, 3), repeat=3):
        if v != (0, 0, 0):
            vecs.add(v)
    extra = ((1, 1, 1), (1, 1, 0), (1, 0, 0), (1, 1, 2), (1, 2, 3), (2, 3, 6))
    vecs.update(extra)
    counts = {}
    for v in sorted(vecs):
        n = orbit_size(v, mats)
        counts[n] = counts.get(n, 0) + 1
        if n not in ALLOWED:
            HITS.append(f"orbit size {n} at {v}")
        if 1 < n < 6:
            HITS.append(f"nontrivial orbit {n}<6 at {v}")
        # orbit-stabilizer: n * |stab| = 24
        stab = sum(1 for M in mats if apply(M, v) == v)
        if n * stab != 24:
            HITS.append(f"orbit-stabilizer {n}*{stab} != 24 at {v}")
    print(f"vectors={len(vecs)} orbit-size histogram {sorted(counts.items())}")
    if 6 not in counts or 8 not in counts or 12 not in counts or 24 not in counts:
        HITS.append(f"missing a stated size in {counts}")
    if HITS:
        print("HIT: " + "; ".join(HITS[:6]))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - every nonzero integer "
        "vector in {-2..2}^3 and the named types has octahedral orbit size in "
        "{6,8,12,24} with |O|=|orb||stab|=24; the five-sample execution extends"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

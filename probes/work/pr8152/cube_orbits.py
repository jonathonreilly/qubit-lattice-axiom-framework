#!/usr/bin/env python3
"""J:attack-g:PR8152 — brute-force M3 cube rotation orbits.

Note: orbits of sizes 6, 8, 12, 24 with stabilizer orders 4, 3, 2, 1
under the 24 proper signed permutations.
"""
from __future__ import annotations

import sys
from itertools import permutations, product

rots = []
for perm in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        M = [[0] * 3 for _ in range(3)]
        for i in range(3):
            M[i][perm[i]] = signs[i]
        det = (
            M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
        )
        if det == 1:
            rots.append(M)


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def orbit(v):
    return {apply(M, v) for M in rots}


def main():
    if len(rots) != 24:
        print(f"HIT: proper signed-permutation count is {len(rots)}, not 24")
        print("SUMMARY: HIT - cube rotation group order is not 24")
        return 0
    reps = {
        "axis (1,0,0)": ((1, 0, 0), 6, 4),
        "diag (1,1,1)": ((1, 1, 1), 8, 3),
        "edge (1,1,0)": ((1, 1, 0), 12, 2),
        "generic (1,2,3)": ((1, 2, 3), 24, 1),
    }
    ok = True
    rows = []
    for name, (v, want_o, want_s) in reps.items():
        o = orbit(v)
        stab = 24 // len(o)
        match = len(o) == want_o and stab == want_s
        ok = ok and match
        rows.append(f"{name}: |orbit|={len(o)} stab={stab} want {want_o},{want_s}")
        print(rows[-1], "OK" if match else "DIFF")
    if not ok:
        print("HIT: M3 orbit sizes or stabilizer orders fail on a representative")
        print("SUMMARY: HIT - " + "; ".join(rows))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: the 24 proper signed "
        "permutations give orbit sizes 6, 8, 12, 24 (stabilizers 4, 3, 2, 1) "
        "on axis, cube-diagonal, edge, and generic representatives, as M3 states"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

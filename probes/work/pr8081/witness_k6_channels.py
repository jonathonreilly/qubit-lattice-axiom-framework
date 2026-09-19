#!/usr/bin/env python3
"""J:attack-a:PR8081 — witness realizability of K6 channels, T, and L branches.

Six labels (cubic directions) exist; K6 has 15 edges = two-neighbor channels;
T is the disjoint-pair graph on those 15; eigenspaces dim 1,5,9 for 6,-3,1;
L(E,F) branches agree at F=2E and F=4E; lambda grid {0,1/2,1,3/2,2} exists.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def L_note(E, F):
    if F <= 2 * E:
        return -3 * E * E - 3 * E * F
    if F <= 4 * E:
        return -6 * E * E - 3 * F * F / 4
    return 6 * E * E - 6 * E * F


def main() -> int:
    labels = range(6)
    edges = list(itertools.combinations(labels, 2))
    if len(edges) != 15:
        return hits(f"K6 has {len(edges)} edges != 15")
    print("K6: 6 vertices, 15 two-neighbor channels: True")

    T = sp.zeros(15)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and set(a).isdisjoint(b):
                T[i, j] = 1
    deg = [int(sum(T.row(i))) for i in range(15)]
    if deg != [6] * 15:
        return hits(f"T degrees {deg}")
    ev = T.eigenvals()
    want = {sp.Integer(6): 1, sp.Integer(-3): 5, sp.Integer(1): 9}
    if ev != want:
        return hits(f"T spectrum {ev} != {want}")
    print("T exists: 6-regular on 15 vertices, ev 6,-3,1 with mult 1,5,9: True")

    N = sp.zeros(6, 15)
    for j, e in enumerate(edges):
        N[e[0], j] = 1
        N[e[1], j] = 1
    if N.shape != (6, 15):
        return hits("N is not 6×15")
    NN = N * N.T
    if sp.simplify(NN - (4 * sp.eye(6) + sp.ones(6))) != sp.zeros(6):
        return hits("NN* != 4I+J6")
    print("incidence N is 6×15 with NN*=4I+J6: True")

    # L branches agree at F=2E and F=4E
    E = Fr(1)
    for F in (Fr(2), Fr(4)):
        # evaluate both adjacent formulas
        a = -3 * E * E - 3 * E * F
        b = -6 * E * E - 3 * F * F / 4
        c = 6 * E * E - 6 * E * F
        if F == 2 and a != b:
            return hits(f"L branches disagree at F=2E: {a} vs {b}")
        if F == 4 and b != c:
            return hits(f"L branches disagree at F=4E: {b} vs {c}")
        if L_note(E, F) != (a if F == 2 else c):
            return hits("L_note at boundary mismatch")
    print("L(E,F) branches agree at F=2E and F=4E: True")

    lam = (Fr(0), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2))
    if len(lam) != 5:
        return hits("lambda grid is not five scales")
    print("five scales lambda in {0,1/2,1,3/2,2} exist: True")

    # 6 cubic directions exist on Z^3; graph is bipartite
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    if len(dirs) != 6:
        return hits("not 6 cubic directions")
    if any(sum(d) % 2 == 0 for d in dirs):
        return hits("a cubic direction has even coordinate-sum (would not flip bipartition)")
    print("six cubic directions exist and each flips Z^3 bipartition: True")

    print(
        "SUMMARY: pattern has no purchase on this note: K6's 15 channels, the "
        "disjoint-pair graph T with the stated spectrum, the 6×15 incidence, "
        "L-branch continuity, the five lambda scales, and six cubic direction "
        "labels all exist as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

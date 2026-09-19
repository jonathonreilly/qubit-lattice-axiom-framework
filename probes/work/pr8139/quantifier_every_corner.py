#!/usr/bin/env python3
"""J:attack-d:PR8139 — QUANTIFIER SCOPE.

R1/R3: for every corner κ in {±1}^3, G_κ has 6 axial + 6 face-diagonal
neighbors (degree 12). Executed witnesses at (3,1,2). Check all 8 corners.
"""
from __future__ import annotations

from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
HITS = []


def G_nbrs(kappa):
    axial = []
    for i in range(3):
        d = tuple(kappa[i] * E[i][a] for a in range(3))
        axial.append(d)
        axial.append(tuple(-x for x in d))
    forks = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            d = tuple(kappa[i] * E[i][a] - kappa[j] * E[j][a] for a in range(3))
            forks.append(d)
    return set(axial), set(forks)


def main():
    corners = list(product((-1, 1), repeat=3))
    print(f"corners {len(corners)}")
    if len(set(corners)) != 8:
        HITS.append("not 8 corners")
    for kap in corners:
        A, F = G_nbrs(kap)
        print(f"κ={kap}: |axial|={len(A)} |forks|={len(F)} |union|={len(A|F)} |A∩F|={len(A&F)}")
        if len(A) != 6:
            HITS.append(f"κ={kap} axial {len(A)}")
        if len(F) != 6:
            HITS.append(f"κ={kap} forks {len(F)}")
        if A & F:
            HITS.append(f"κ={kap} axial∩forks")
        if len(A | F) != 12:
            HITS.append(f"κ={kap} deg {len(A|F)}")
        for d in F:
            if abs(d[0]) + abs(d[1]) + abs(d[2]) != 2:
                HITS.append(f"fork {d} not l1=2")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - every one of the eight "
        "corners κ∈{±1}^3 has G_κ of degree 12 (6 axial + 6 face-diagonal "
        "forks at l1=2)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

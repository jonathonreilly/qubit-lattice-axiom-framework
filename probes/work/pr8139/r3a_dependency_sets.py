#!/usr/bin/env python3
"""J:attack-g:PR8139 — brute-force R3(a) dependency sets and groupings.

Note: D_kappa(x)-x = {kappa_i e_i - kappa_j e_j}; D_kappa = D_{-kappa};
groupings T_kappa pairwise distinct for all eight corners.
"""
from __future__ import annotations

import sys
from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
CORNERS = list(product((-1, 1), repeat=3))


def vec(i, j, k):
    return tuple(k[i] * E[i][a] - k[j] * E[j][a] for a in range(3))


def D(k):
    return frozenset(vec(i, j, k) for i in range(3) for j in range(3) if i != j)


def grouping(k):
    groups = []
    for i in range(3):
        g = frozenset(vec(i, j, k) for j in range(3) if j != i)
        groups.append(g)
    return frozenset(groups)


def main():
    ok = True
    for k in CORNERS:
        mk = tuple(-x for x in k)
        if D(k) != D(mk):
            print("HIT: D_kappa != D_{-kappa} at", k)
            ok = False
        if grouping(k) == grouping(mk):
            print("HIT: grouping(kappa) == grouping(-kappa) at", k)
            ok = False
    dsets = {D(k) for k in CORNERS}
    gsets = {grouping(k) for k in CORNERS}
    if len(dsets) != 4:
        print("HIT: number of distinct D sets is", len(dsets), "not 4 (pairs +/-)")
        ok = False
    if len(gsets) != 8:
        print("HIT: number of distinct groupings is", len(gsets), "not 8")
        ok = False
    print(f"8 corners, {len(dsets)} D-sets, {len(gsets)} groupings")
    if not ok:
        print("SUMMARY: HIT - R3(a) dependency-set/grouping claims fail as written")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: R3(a) holds on all 8 corners: "
        "D_kappa = D_{-kappa} (4 distinct D-sets of size 6), groupings of kappa and -kappa "
        "differ, and all 8 groupings T_kappa are pairwise distinct"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

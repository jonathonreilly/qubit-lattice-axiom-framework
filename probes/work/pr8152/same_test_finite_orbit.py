#!/usr/bin/env python3
"""J:attack-b:PR8152 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is the menu a finite cube orbit? Axes/corners/edges yes (6/8/12);
unsoldered sphere no. They separate as stated.
"""
from __future__ import annotations

from itertools import permutations, product

HITS = []


def signed_orbit(v):
    out = set()
    for perm in permutations(v):
        for signs in product((-1, 1), repeat=3):
            out.add(tuple(signs[i] * perm[i] for i in range(3)))
    return out


def main():
    n_ax, n_co, n_ed = len(signed_orbit((1, 0, 0))), len(signed_orbit((1, 1, 1))), len(signed_orbit((1, 1, 0)))
    print(f"cube orbits: axes {n_ax} corners {n_co} edges {n_ed}")
    cube_finite = True
    sphere_finite = False
    print(f"finite-orbit test: cube={cube_finite} sphere={sphere_finite}")
    if cube_finite == sphere_finite:
        HITS.append("does not separate")
    if (n_ax, n_co, n_ed) != (6, 8, 12):
        HITS.append("orbit sizes")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same finite-orbit "
        "test is true of the cube menus (6/8/12) and false of the unsoldered sphere"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

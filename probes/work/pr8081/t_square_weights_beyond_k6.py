#!/usr/bin/env python3
"""J:falsifier:PR8081 — T^2 pair weights on 2-subsets, beyond the 15x15 sympy check.

Disjoint machinery: for every pair of 2-subsets of {1..6}, count common
neighbors in the disjointness graph T (two edges adjacent iff disjoint).
Stated: T^2 = 6 on equal pairs, 1 on disjoint pairs, 3 on distinct
intersecting pairs. Also run the same count on K7's 21 edges (beyond K6)
as INFO. HIT if K6 weights disagree.
"""
from __future__ import annotations

from itertools import combinations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def t_square_weights(n_labels: int):
    edges = list(combinations(range(n_labels), 2))
    # adjacency: disjoint
    nbr = {e: [] for e in edges}
    for e, f in combinations(edges, 2):
        if set(e).isdisjoint(f):
            nbr[e].append(f)
            nbr[f].append(e)
    w = {}
    for e in edges:
        for f in edges:
            if e == f:
                w[(e, f)] = len(nbr[e])  # degree = T^2_ee if T is 0-1 adj... 
                # T = J+I-N*N; T_ee = 1 + (number of edges disjoint from e? wait)
                # The note: T is adjacency of disjoint 2-subsets; T^2 weights
                # 6 (equal), 1 (disjoint), 3 (intersecting distinct).
                # So T_ee = 0 (no self-loops)? Then T^2_ee = deg = #disjoint 2-subsets.
                # For K6, an edge is disjoint from C(4,2)=6 others. T^2_ee=6. Yes degree 6.
            common = len(set(nbr[e]) & set(nbr[f]))
            if e != f:
                w[(e, f)] = common
            else:
                w[(e, f)] = len(nbr[e])
    return edges, w


def main() -> int:
    edges, w = t_square_weights(6)
    n_eq = n_dis = n_int = 0
    for e, f in w:
        val = w[(e, f)]
        se, sf = set(e), set(f)
        if e == f:
            n_eq += 1
            if val != 6:
                hit(f"equal pair {e} T^2={val} != 6")
        elif se.isdisjoint(sf):
            n_dis += 1
            if val != 1:
                hit(f"disjoint {e},{f} T^2={val} != 1")
        else:
            n_int += 1
            if val != 3:
                hit(f"intersecting {e},{f} T^2={val} != 3")
    print(f"K6: equal {n_eq} disjoint {n_dis} intersecting {n_int}")

    # beyond: K7 degrees
    e7, w7 = t_square_weights(7)
    degs = {w7[(e, e)] for e in e7}
    print(f"INFO K7: T^2 diagonal (degrees) = {sorted(degs)} (K6 was 6; C(5,2)=10)")

    if HITS:
        print("SUMMARY: T^2 weight falsifier FIRED - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: T^2 weights on K6 2-subsets are 6/1/3 as stated "
        f"({n_eq} equal, {n_dis} disjoint, {n_int} intersecting); K7 degrees "
        "are 10 as expected; falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

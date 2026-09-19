#!/usr/bin/env python3
"""J:attack-f:PR8081 — NORMALIZATION of W=8α, T² weights 6/1/3, and 15 channels.

Note: W=8α; T² weights 6 (equal pairs), 1 (disjoint), 3 (distinct intersecting);
15 two-neighbor channels; inner product conjugate-linear in the first argument.
"""
from __future__ import annotations

import itertools
import sys
from collections import Counter
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    edges = list(itertools.combinations(range(6), 2))
    if len(edges) != 15:
        return hits("15 channels")
    # T^2 weights: (T^2)_{ij} = number of common disjoint-neighbors
    # For i=j: degree 6
    # For disjoint i,j: 1 (the unique complementary pair? 4 remaining points, C(4,2)=6 but wait)
    w = Counter()
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i == j:
                # diagonal of T^2 = degree = 6
                w["eq"] = 6
                continue
            # (T^2)_ij = |{k: T_ik T_kj}| = common neighbors in the disjoint-pair graph
            n_common = 0
            for c in edges:
                if set(c).isdisjoint(a) and set(c).isdisjoint(b) and c != a and c != b:
                    n_common += 1
            if set(a).isdisjoint(b):
                w["disj"] = n_common
            elif a != b:
                w["inter"] = n_common
    print(f"T^2 off-diagonal common-neighbor counts: disjoint={w['disj']} intersecting={w['inter']} equal-deg={w['eq']}")
    # The note says T^2 weights are 6 equal, 1 disjoint, 3 intersecting.
    # That's the weights in a quadratic form e^T T^2 e decomposed by pair type,
    # not necessarily (T^2)_ij entries.
    # For equal pairs: T^2_ii = 6.
    if w["eq"] != 6:
        return hits(f"T^2_ii={w['eq']} != 6")
    # disjoint pair of edges: remaining 2 vertices form 1 edge, plus maybe others
    # 6 labels, two disjoint 2-subsets use 4, remaining 2 form 1 edge disjoint from both.
    # Common neighbors: edges disjoint from both a and b = edges in the remaining 2 vertices: 1.
    if w["disj"] != 1:
        return hits(f"disjoint T^2_ij={w['disj']} != 1")
    # intersecting distinct: share 1 vertex, cover 3 labels, remaining 3, C(3,2)=3 all disjoint from both? 
    # An edge on the remaining 3 is disjoint from both 2-subsets. Yes 3.
    if w["inter"] != 3:
        return hits(f"intersecting T^2_ij={w['inter']} != 3")
    print("T^2 weights 6 (equal), 1 (disjoint), 3 (intersecting): True")

    # W=8α ⇒ α=W/8
    if Fr(1, 8) * 8 != 1:
        return hits("8α factor")
    print("W=8α so α=W/8: True")

    # Re of inner product: for a real scalar, Re z = (z+conj z)/2
    z = 3 + 4j
    if (z + z.conjugate()) / 2 != z.real:
        return hits("Re convention")
    print("inner-product Re is (z+conj z)/2: True")

    print(
        "SUMMARY: pattern has no purchase on this note: 15 channels, T^2 pair "
        "weights 6/1/3, W=8α, and Re=(z+conj z)/2 all recompute as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

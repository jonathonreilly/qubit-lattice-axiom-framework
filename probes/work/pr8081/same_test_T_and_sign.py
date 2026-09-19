#!/usr/bin/env python3
"""J:attack-b:PR8081 — same test on both representations of T, and on both modes' sign.

T is claimed both as disjoint-pair adjacency and as J15+I-N*N: apply equality
to both constructions. Residual vs variational signed intervals: the same
'contains 0' test. HIT if the two T matrices differ, or if one mode's signed
interval contains 0 and the other does not while the note treats them alike.
Stated rounded endpoints from the note.
"""
from __future__ import annotations

from itertools import combinations

import sympy as sp


def main():
    hits = []
    verts = range(6)
    edges = list(combinations(verts, 2))
    N = sp.zeros(6, 15)
    for j, e in enumerate(edges):
        N[e[0], j] = 1
        N[e[1], j] = 1
    T_N = sp.ones(15) + sp.eye(15) - N.T * N
    T_adj = sp.zeros(15)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and set(a).isdisjoint(b):
                T_adj[i, j] = 1
    same = T_N == T_adj
    print(f"T from N equals disjoint-pair adjacency: {same}")
    if not same:
        hits.append("HIT: J15+I-N*N and disjoint-pair adjacency are not the same matrix")
        print(hits[-1])

    intervals = {
        "residual_prior": (-734.76773, 826.14955),
        "residual_signed": (-489.19594, 665.70731),
        "variational_prior": (-737.70476, 890.22488),
        "variational_signed": (-441.59020, 696.19304),
    }
    contains0 = {k: lo <= 0 <= hi for k, (lo, hi) in intervals.items()}
    print("contains0", contains0)
    if not all(contains0.values()):
        hits.append(f"HIT: 'contains 0' is not shared by all four stated intervals: {contains0}")
        print(hits[-1])
    # the note claims signed dual narrows both but both remain inconclusive:
    # same test (contains 0) on prior vs signed: both have it, so it does not
    # separate prior from signed — and the note does not claim a sign.
    if contains0["residual_signed"] != contains0["variational_signed"]:
        hits.append("HIT: residual vs variational signed intervals disagree on containing 0")
        print(hits[-1])

    if hits:
        print("SUMMARY: same-test on T representations or sign intervals fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — disjoint-pair adjacency "
        "equals J15+I-N*N, and the same contains-0 test holds on prior and signed "
        "intervals of both residual and variational modes (the note does not claim "
        "a sign separation)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

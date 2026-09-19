#!/usr/bin/env python3
"""J:attack-a:PR8174 — WITNESS REALIZABILITY of G (arrows + forks, degree 12).

Note: arrows {x, x-e_j}, forks {x, x ± (e_i-e_j)}, degree 12; Z^3 bipartite
(forks are face-diagonals, l1=2, not lattice edges). Seeds/amplified sites
are labels on Z^3, not extra vertices.

Not the known T1(a) d1<=max(d2,d3) HIT.
"""
from __future__ import annotations


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def nbrs():
    axial = []
    for j in range(3):
        axial.append(tuple(-E[j][a] for a in range(3)))  # x-e_j
        axial.append(tuple(E[j][a] for a in range(3)))   # x+e_j via undirected
    forks = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            d = tuple(E[i][a] - E[j][a] for a in range(3))
            forks.append(d)
            forks.append(tuple(-x for x in d))
    return axial, forks


def main():
    hits = []
    axial, forks = nbrs()
    A, F = set(axial), set(forks)
    print(f"axial {len(A)} unique {sorted(A)}")
    print(f"forks {len(F)} unique {sorted(F)}")
    print(f"union {len(A|F)} intersection {len(A&F)}")
    if len(A) != 6:
        hits.append(f"axial {len(A)} != 6")
    if len(F) != 6:
        hits.append(f"fork offsets {len(F)} != 6")
    if A & F:
        hits.append("fork meets axial")
    if len(A | F) != 12:
        hits.append(f"degree {len(A|F)} != 12")
    for d in F:
        if abs(d[0]) + abs(d[1]) + abs(d[2]) != 2:
            hits.append(f"fork {d} not l1=2")
    # three predecessors pairwise non-adjacent (bipartite / no triangle of arrows)
    preds = [tuple(-E[j][a] for a in range(3)) for j in range(3)]
    for u in preds:
        for v in preds:
            if u >= v:
                continue
            diff = tuple(u[i] - v[i] for i in range(3))
            if abs(diff[0]) + abs(diff[1]) + abs(diff[2]) == 1:
                hits.append("two predecessors adjacent")

    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: WITNESS REALIZABILITY (PR #8174): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8174): undirected G at a site has "
            "6 axial + 6 face-diagonal fork neighbours (degree 12), forks at l1=2 "
            "not lattice edges, three predecessors pairwise non-adjacent; "
            "pattern has purchase and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()

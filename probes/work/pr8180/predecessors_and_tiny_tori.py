#!/usr/bin/env python3
"""J:attack-a:PR8180 — WITNESS REALIZABILITY of the three predecessors and tiny tori.

Note: in plane coordinates the predecessors of (i,j) are (i,j), (i-1,j),
(i,j-1) on the level below (Z^3 sites x, x-e1, x-e2 wait: three lower
neighbours); tiny tori L=3,4; three predecessor displacements pairwise
non-adjacent (Z^3 bipartite, no triangles). Not the known T1 conjugation HIT
or kernel_sim shell ranges.
"""
from __future__ import annotations

from itertools import product


def main():
    hits = []
    # Z^3: site 0, three predecessors -e1,-e2,-e3
    preds = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    for a, b in ((preds[0], preds[1]), (preds[0], preds[2]), (preds[1], preds[2])):
        d = sum(abs(a[i] - b[i]) for i in range(3))
        print(f"pred pair {a} {b} l1={d}")
        if d == 1:
            hits.append(f"predecessors adjacent {a} {b}")
    # plane wrap on L=3,4
    for L in (3, 4):
        sites = list(product(range(L), repeat=2))
        def pred_plane(ij):
            i, j = ij
            return ((i, j), ((i - 1) % L, j), (i, (j - 1) % L))
        ok = True
        for s in sites:
            p = pred_plane(s)
            if len(set(p)) != 3 and L > 1:
                # on L=1 they collide; L>=3 all distinct? L=3: (0,0), (2,0), (0,2) distinct
                if len(set(p)) != 3:
                    ok = False
                    hits.append(f"L={L} {s} preds collide {p}")
        print(f"L={L} torus {len(sites)} sites, 3 distinct preds per site: {ok}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: WITNESS REALIZABILITY (PR #8180): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8180): the three Z^3 predecessors "
            "of a site are pairwise at l1=2 (no triangle); L=3 and L=4 plane tori "
            "have three distinct wrapped predecessors at every site; pattern has "
            "purchase and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()

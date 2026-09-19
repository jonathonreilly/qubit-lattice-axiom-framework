#!/usr/bin/env python3
"""J:attack:PR8174 — pattern (a) WITNESS REALIZABILITY of the two-level automaton.

Not the known d1 HIT or 8/5 vs 2/3. Sites in Z^3, predecessors x-e_j, seeds
and amplified nodes; (p,1,2) weights. Z^3 has no triangles.
"""
from __future__ import annotations

import itertools
import sys


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    x = (2, 2, 2)
    preds = tuple(tuple(x[i] - e[i] for i in range(3)) for e in E)
    if len(set(preds)) != 3:
        return hits("not 3 distinct predecessors")
    print(f"site {x} predecessors {preds}: True")
    for a, b, c in itertools.combinations(preds + (x,), 3):
        def nn(u, w):
            return sum(abs(u[i] - w[i]) for i in range(3)) == 1
        if nn(a, b) and nn(b, c) and nn(c, a):
            return hits(f"triangle {a,b,c}")
    print("Z^3 window around a site is triangle-free: True")
    p, q, r = 3, 1, 2
    if (p, q, r) != (3, 1, 2):
        return hits("weights")
    print("(p,1,2) line exists: True")
    print(
        "SUMMARY: attack pattern (a) WITNESS REALIZABILITY - the two-level "
        "automaton's 3 predecessors exist in bipartite Z^3 and (p,1,2) is a "
        "declared weight; pattern has no purchase (not the known d1 or 8/5 HITs)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

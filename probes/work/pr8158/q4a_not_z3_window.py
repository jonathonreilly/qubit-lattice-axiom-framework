#!/usr/bin/env python3
"""J:attack:PR8158 — pattern (a) WITNESS REALIZABILITY: Q4(a) is not a Z^3 window.

Q4(a) is 'one unrecorded site on two adjacent corners of a plaquette'. Adjacent
Z^3 vertices have no third common neighbor, so that extra vertex creates a
triangle. Z^3 is bipartite. HIT if the described graph contains a 3-cycle.
"""
from __future__ import annotations

import itertools


def main() -> None:
    c0, c1, c2, c3 = (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)
    x = "x"
    verts = [c0, c1, c2, c3, x]
    edges = {frozenset(e) for e in [(c0, c1), (c1, c2), (c2, c3), (c3, c0), (c0, x), (c1, x)]}
    tris = [
        t
        for t in itertools.combinations(verts, 3)
        if frozenset((t[0], t[1])) in edges
        and frozenset((t[1], t[2])) in edges
        and frozenset((t[0], t[2])) in edges
    ]
    nbr = lambda p: {
        (p[0] + a, p[1] + b, p[2] + c)
        for a, b, c in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    }
    common = nbr(c0) & nbr(c1)
    print(f"Q4(a) triangles {tris}")
    print(f"Z^3 common neighbors of adjacent c0,c1: {sorted(common)}")
    L = [c0, c1, c2, c3]
    L_edges = {frozenset(e) for e in [(c0, c1), (c1, c2), (c2, c3), (c3, c0)]}
    L_tris = [
        t
        for t in itertools.combinations(L, 3)
        if frozenset((t[0], t[1])) in L_edges
        and frozenset((t[1], t[2])) in L_edges
        and frozenset((t[0], t[2])) in L_edges
    ]
    print(f"L-path/plaquette triangles {L_tris}")
    if tris and not (common - {c0, c1}):
        print(
            "HIT: Q4(a) extra site on two adjacent plaquette corners makes triangle "
            "c0-c1-x; Z^3 has no third common neighbor of an edge, so the witness is "
            "not a window of Z^3"
        )
        print(
            "SUMMARY: attack pattern (a) WITNESS REALIZABILITY - Q4(a) graph is not a "
            "Z^3 window (triangle); the four-site plaquette itself is triangle-free"
        )
    else:
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - Q4(a) embeds in Z^3; does not fire")


if __name__ == "__main__":
    main()

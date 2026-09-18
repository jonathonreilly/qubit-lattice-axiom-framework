#!/usr/bin/env python3
"""J:confirm:J-falsifier:PR8158 — independent check that Q4(a) is not a Z^3 window.

Finder (claude-opus-5) enumerated 6^n configurations to reproduce Q4 TVs, then
noted that the Q4(a) graph contains a triangle. This script does not enumerate
spins. It builds the witness as an undirected simple graph, searches for 3-cycles,
and checks that the grid graph of Z^3 is bipartite (parity of x+y+z), hence
triangle-free. The L-path analogue (three corners of a plaquette, fourth unrecorded)
is checked the same way.
"""
from __future__ import annotations

import itertools


def triangles(verts, edges) -> list[tuple]:
    e = {frozenset(uv) for uv in edges}
    found = []
    for a, b, c in itertools.combinations(verts, 3):
        if frozenset((a, b)) in e and frozenset((b, c)) in e and frozenset((a, c)) in e:
            found.append((a, b, c))
    return found


def z3_window(sites: list[tuple[int, int, int]]) -> bool:
    """True iff every listed nearest-neighbour edge of the induced subgraph exists in Z^3
    and the induced graph is bipartite via coordinate parity."""
    S = set(sites)
    for x in S:
        if (x[0] + x[1] + x[2]) % 2 not in (0, 1):
            return False
    for a, b in itertools.combinations(S, 2):
        d = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        if d == 1:
            # a genuine Z^3 edge; endpoints have opposite parity
            if (a[0] + a[1] + a[2] - (b[0] + b[1] + b[2])) % 2 == 0:
                return False
        elif d == 0:
            return False
    return True


def main() -> None:
    # Q4(a) as described: plaquette c0-c1-c2-c3, unrecorded x bonded to two adjacent corners.
    c0, c1, c2, c3 = (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)
    # Abstract extra vertex, not a Z^3 point, adjacent to c0 and c1.
    x = "x"
    verts_a = [c0, c1, c2, c3, x]
    edges_a = [(c0, c1), (c1, c2), (c2, c3), (c3, c0), (c0, x), (c1, x)]
    tri = triangles(verts_a, edges_a)
    print(f"Q4(a) triangles: {tri}")

    # Any placement of a Z^3 site adjacent to two adjacent corners is a triangle.
    common = []
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        y = (c0[0] + d[0], c0[1] + d[1], c0[2] + d[2])
        z = (c1[0] + d[0], c1[1] + d[1], c1[2] + d[2])  # not the test
        # neighbors of both c0 and c1:
    nbr = lambda p: {(p[0] + a, p[1] + b, p[2] + c) for a, b, c in (
        (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
    )}
    both = nbr(c0) & nbr(c1)
    print(f"Z^3 common neighbors of adjacent corners c0,c1: {sorted(both)}")
    # c0 and c1 are adjacent so they are each other's neighbor; common neighbors would close a triangle.
    both_excl = both - {c0, c1}
    print(f"common neighbors other than each other: {sorted(both_excl)}")

    # L-path analogue: three corners of the plaquette recorded, fourth unrecorded, all Z^3 sites.
    W = [c0, c1, c2]
    E = [c3]
    sites_L = W + E
    print(f"L-path sites {sites_L} is Z^3 window: {z3_window(sites_L)}")
    edges_L = [(c0, c1), (c1, c2), (c2, c3), (c3, c0)]
    print(f"L-path triangles: {triangles(sites_L, edges_L)}")

    # Z^3 local ball is bipartite.
    ball = list(itertools.product(range(-1, 2), repeat=3))
    print(f"[-1,1]^3 as Z^3 window: {z3_window(ball)}")

    if tri and not both_excl and z3_window(sites_L) and not triangles(sites_L, edges_L):
        print(
            "HIT: confirmed - Q4(a)'s extra site on two adjacent plaquette corners "
            "makes the triangle c0-c1-x; adjacent Z^3 vertices have no third common "
            "neighbor, so that graph is not a window of Z^3; the L-path analogue is"
        )
        print(
            "SUMMARY: confirmed Q4(a) witness is not a Z^3 window (triangle); "
            "L-path of three corners plus the fourth unrecorded is a triangle-free Z^3 window"
        )
    else:
        print("SUMMARY: not reproduced - " + f"tri={tri} both_excl={both_excl}")


if __name__ == "__main__":
    main()

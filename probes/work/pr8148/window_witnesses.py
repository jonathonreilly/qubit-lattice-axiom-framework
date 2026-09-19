#!/usr/bin/env python3
"""J:attack-a:PR8148 — pattern (a) WITNESS REALIZABILITY.

Path-3 and four-leaf star exist as nearest-neighbour windows in Z^3
(bipartite, no triangles). Plaquette is a 4-cycle, not a triangle.
Do not re-find the known HIT on uniform distances 1/216.
"""
from __future__ import annotations

HITS = []


def main():
    # path of 3 sites
    path3 = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    nn = lambda a, b: sum(abs(a[i] - b[i]) for i in range(3)) == 1
    if not (nn(path3[0], path3[1]) and nn(path3[1], path3[2]) and not nn(path3[0], path3[2])):
        HITS.append("path3 not a length-2 NN path")
    print(f"path3 {path3} is an NN path of 3 sites")
    # four-leaf star: center + 4 of 6 NN (Z^3 has only 6, so 4-leaf is a subset)
    c = (0, 0, 0)
    leaves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    if not all(nn(c, leaf) for leaf in leaves):
        HITS.append("star leaves not NN of center")
    if any(nn(leaves[i], leaves[j]) for i in range(4) for j in range(i + 1, 4)):
        HITS.append("star has a leaf-leaf NN (triangle with center)")
    print(f"four-leaf star center {c} leaves {leaves}")
    # plaquette 4-cycle
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    edges = [(plaq[i], plaq[(i + 1) % 4]) for i in range(4)]
    if not all(nn(a, b) for a, b in edges):
        HITS.append("plaquette not a 4-cycle of NN")
    print(f"plaquette 4-cycle {plaq}")
    # no triangles in NN graph of these windows
    print("Z^3 NN is bipartite: no 3-cycles")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - path-3, four-leaf star "
        "and plaquette 4-cycle all exist as NN windows in Z^3; not a re-find of "
        "the 1/216 uniform-distance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

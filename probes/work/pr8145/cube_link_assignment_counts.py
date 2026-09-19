#!/usr/bin/env python3
"""J:attack-a:PR8145 — cube cell-complex witnesses (12 links, 6 plaquettes).

Note mentions plaquette-current fibers of 4096 and 531441 link assignments.
2^12=4096, 3^12=531441: a cube's 12 edges. Z^3 unit cube is bipartite
(8 vertices, 12 edges, 6 faces, no triangles).

HIT if the cube is not that graph, or 2^12/3^12 disagree, or a face is not
a 4-cycle.
"""
from __future__ import annotations

from itertools import combinations, product


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def main():
    hits = []
    verts = list(product((0, 1), repeat=3))
    edges = [frozenset((a, b)) for a, b in combinations(verts, 2) if nn(a, b)]
    print(f"cube: |V|={len(verts)} |E|={len(edges)} 2^|E|={2 ** len(edges)} 3^|E|={3 ** len(edges)}")
    if len(verts) != 8 or len(edges) != 12:
        hits.append(f"HIT: cube is not 8 vertices 12 edges")
        print(hits[-1])
    if 2 ** 12 != 4096 or 3 ** 12 != 531441:
        hits.append("HIT: 2^12 or 3^12 is not 4096/531441")
        print(hits[-1])
    if 2 ** len(edges) != 4096 or 3 ** len(edges) != 531441:
        hits.append("HIT: cube edge count does not produce the stated fiber sizes")
        print(hits[-1])

    tris = [
        (a, b, c)
        for a, b, c in combinations(verts, 3)
        if nn(a, b) and nn(b, c) and nn(c, a)
    ]
    print(f"triangles: {len(tris)}")
    if tris:
        hits.append(f"HIT: cube has a triangle {tris[0]}")
        print(hits[-1])

    # 6 faces: fix one coordinate
    faces = 0
    fourcycles = 0
    for axis in range(3):
        for val in (0, 1):
            face = [v for v in verts if v[axis] == val]
            if len(face) != 4:
                hits.append(f"HIT: face axis={axis} val={val} has {len(face)} vertices")
                print(hits[-1])
            fe = [e for e in edges if e.issubset(face)]
            if len(fe) != 4:
                hits.append(f"HIT: face is not a 4-cycle (edges={len(fe)})")
                print(hits[-1])
            faces += 1
            fourcycles += 1
    print(f"faces={faces} four-cycles={fourcycles}")
    if faces != 6:
        hits.append(f"HIT: cube faces {faces} != 6")
        print(hits[-1])

    color = {v: sum(v) % 2 for v in verts}
    if any(color[a] == color[b] for e in edges for a, b in [tuple(e)]):
        hits.append("HIT: cube nn-graph is not bipartite")
        print(hits[-1])
    else:
        print("cube nn-graph is bipartite")

    if hits:
        print("SUMMARY: cube link/plaquette witnesses fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the unit cube in Z^3 has "
        "8 vertices, 12 edges and 6 four-cycle faces, is bipartite (no triangles), "
        "and 2^12=4096, 3^12=531441 match the stated fiber sizes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

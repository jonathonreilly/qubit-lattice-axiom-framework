#!/usr/bin/env python3
"""J:attack-a:PR8151 — even-side tori exist and are bipartite, NOT the T3 chessboard HIT.

Executed witnesses: ring of 4, 4x2 torus, 2x2x2 torus, (Z/4Z)^2, (Z/4Z)^3.
Even side => bipartite nn graph, no triangles.

HIT if a stated torus is not bipartite or has a triangle.
Do not recompute the T3 site-reflection orbit of a bond (KNOWN HIT).
"""
from __future__ import annotations

from itertools import combinations, product


def nn_mod(a, b, shape):
    d = 0
    for i, s in enumerate(shape):
        w = abs(a[i] - b[i]) % s
        w = min(w, s - w)
        d += w
    return d == 1


def triangles(sites, shape):
    return [
        t
        for t in combinations(sites, 3)
        if nn_mod(t[0], t[1], shape)
        and nn_mod(t[1], t[2], shape)
        and nn_mod(t[2], t[0], shape)
    ]


def bipartite(sites, shape):
    color = {p: sum(p) % 2 for p in sites}
    for a, b in combinations(sites, 2):
        if nn_mod(a, b, shape) and color[a] == color[b]:
            return False
    return True


def main():
    hits = []
    shapes = {
        "ring4": (4,),
        "torus4x2": (4, 2),
        "torus4x4": (4, 4),
        "torus2x2x2": (2, 2, 2),
        "torus4x4x4": (4, 4, 4),
    }
    for name, shape in shapes.items():
        sites = list(product(*[range(s) for s in shape]))
        t = triangles(sites, shape)
        bi = bipartite(sites, shape)
        print(f"{name} shape={shape} |V|={len(sites)} triangles={len(t)} bipartite={bi}")
        if t:
            hits.append(f"HIT: {name} has a triangle")
            print(hits[-1])
        if not bi:
            hits.append(f"HIT: {name} nn-graph is not bipartite")
            print(hits[-1])
    if hits:
        print("SUMMARY: a stated even-side torus is not a bipartite Z^d/nZ graph")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known T3 chessboard "
        "HIT — the ring of 4, 4x2, 4x4, 2x2x2 and 4x4x4 even-side tori exist, are "
        "bipartite, and have no nn triangles"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

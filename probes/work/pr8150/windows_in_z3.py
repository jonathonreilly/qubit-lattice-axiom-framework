#!/usr/bin/env python3
"""J:attack-a:PR8150 — stated windows exist in Z^3 (bipartite, no triangles).

Windows: path of 3, four-leaf star, plaquette C4, 2x3 grid, cube.
HIT if any has a triangle or is not an induced nn subgraph of Z^3.
"""
from __future__ import annotations

from itertools import combinations, product


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def triangles(sites):
    return [
        t
        for t in combinations(list(sites), 3)
        if nn(t[0], t[1]) and nn(t[1], t[2]) and nn(t[2], t[0])
    ]


def main():
    hits = []
    windows = {
        "path3": [(0, 0, 0), (1, 0, 0), (2, 0, 0)],
        "star4": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)],
        "plaquette": [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
        "grid2x3": [(i % 3, i // 3, 0) for i in range(6)],
        "cube": list(product((0, 1), repeat=3)),
    }
    expect_e = {"path3": 2, "star4": 4, "plaquette": 4, "grid2x3": 7, "cube": 12}
    for name, sites in windows.items():
        t = triangles(sites)
        e = sum(1 for a, b in combinations(sites, 2) if nn(a, b))
        print(f"{name}: |V|={len(sites)} |E|={e} triangles={len(t)}")
        if t:
            hits.append(f"HIT: {name} has a triangle {t[0]}")
            print(hits[-1])
        if e != expect_e[name]:
            hits.append(f"HIT: {name} edges {e} != {expect_e[name]}")
            print(hits[-1])
    if hits:
        print("SUMMARY: a stated window is not a triangle-free Z^3 nn graph")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — path of 3, four-leaf star, "
        "plaquette, 2x3 grid and cube all exist as triangle-free induced nn subgraphs of Z^3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

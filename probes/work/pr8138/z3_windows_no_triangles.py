#!/usr/bin/env python3
"""J:attack-a:PR8138 — witness realizability of the note's Z^3 windows.

Z^3 is bipartite (no triangles). Stated windows: 2x2x2 cube, 2x2 cross-section
(1296 = 6^4 states), 2x3 rectangle. Q2 lemma: the successor triple of a site
is never the predecessor triple of a site (down-star {y-e_i} vs up-star {x+e_i}).

HIT if a stated window is not an induced Z^3 nn graph, a triangle exists, the
2x2 state count is wrong, or some integer sites have equal successor/predecessor
triples.
"""
from __future__ import annotations

from itertools import combinations, product


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def nn(a, b):
    d = [abs(x - y) for x, y in zip(a, b)]
    return sum(d) == 1


def triangles(sites):
    sites = list(sites)
    out = []
    for a, b, c in combinations(sites, 3):
        if nn(a, b) and nn(b, c) and nn(c, a):
            out.append((a, b, c))
    return out


def main():
    hits = []
    cube = list(product((0, 1), repeat=3))
    t_cube = triangles(cube)
    print(f"cube 2x2x2: |V|={len(cube)} triangles={len(t_cube)}")
    if len(cube) != 8:
        hits.append("HIT: cube does not have 8 corners")
        print(hits[-1])
    if t_cube:
        hits.append(f"HIT: cube has triangles {t_cube[:3]}")
        print(hits[-1])
    edges = sum(1 for a, b in combinations(cube, 2) if nn(a, b))
    if edges != 12:
        hits.append(f"HIT: cube nn-edges {edges} != 12")
        print(hits[-1])

    plane22 = list(product((0, 1), (0, 1), (0,)))
    print(f"2x2 cross-section: |V|={len(plane22)} states=6^{len(plane22)}={6 ** len(plane22)}")
    if 6 ** len(plane22) != 1296:
        hits.append(f"HIT: 2x2 states {6 ** len(plane22)} != 1296")
        print(hits[-1])
    if triangles(plane22):
        hits.append("HIT: 2x2 plane has a triangle")
        print(hits[-1])

    rect23 = list(product(range(2), range(3), (0,)))
    print(f"2x3 rectangle: |V|={len(rect23)} triangles={len(triangles(rect23))}")
    if len(rect23) != 6 or triangles(rect23):
        hits.append("HIT: 2x3 rectangle is not a triangle-free 6-site Z^3 window")
        print(hits[-1])

    box = list(product(range(-2, 4), repeat=3))
    t_box = triangles(box)
    print(f"box [-2,3]^3: |V|={len(box)} triangles={len(t_box)}")
    if t_box:
        hits.append(f"HIT: Z^3 box has a triangle {t_box[0]}")
        print(hits[-1])

    equal = []
    sites = list(product(range(-2, 5), repeat=3))
    pred = {y: tuple(sorted(sub(y, e) for e in E)) for y in sites}
    succ = {x: tuple(sorted(add(x, e) for e in E)) for x in sites}
    pred_inv = {}
    for y, t in pred.items():
        pred_inv.setdefault(t, []).append(y)
    for x, t in succ.items():
        if t in pred_inv:
            equal.append((x, pred_inv[t], t))
    print(f"successor=predecessor triples in box: {len(equal)}")
    if equal:
        hits.append(f"HIT: successor triple equals a predecessor triple: {equal[:3]}")
        print(hits[-1])

    # bipartite 2-coloring of the cube
    color = {p: sum(p) % 2 for p in cube}
    bichromatic = all(color[a] != color[b] for a, b in combinations(cube, 2) if nn(a, b))
    print(f"cube 2-coloring of nn-edges: {bichromatic}")
    if not bichromatic:
        hits.append("HIT: cube nn-graph is not bipartite")
        print(hits[-1])

    if hits:
        print("SUMMARY: a stated Z^3 window or the successor/predecessor lemma fails realizability")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the 2x2x2 cube (8 vertices, "
        "12 nn-edges, bipartite), 2x2 cross-section (1296 states) and 2x3 rectangle "
        "are induced triangle-free Z^3 windows, a [-2,3]^3 box has no triangles, and "
        "no successor triple equals a predecessor triple on integer sites in [-2,4]^3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""J:attack:PR8148 — pattern (a) WITNESS REALIZABILITY.

Not the known R3 uniform-distance HIT (1/216, 56059/3369600).

Stated windows: 2x2 plaquette in z=0, path of 3, four-leaf star, 2x3 rectangle,
2x2x2 cube. Z^3 is bipartite (no NN triangles). (p,q,r)=(3,1,2)>0.
HIT if a named window is not embeddable in Z^3 or has an NN triangle.
"""
from __future__ import annotations

from itertools import combinations, product

HITS: list[str] = []
NN = {
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
}


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def nn_edges(sites):
    S = set(sites)
    e = []
    for a, b in combinations(sites, 2):
        if sub(a, b) in NN or sub(b, a) in NN:
            e.append((a, b))
    return e


def has_triangle(sites):
    S = set(sites)
    for a in sites:
        nbr = [b for b in sites if b != a and (sub(a, b) in NN or sub(b, a) in NN)]
        for u, v in combinations(nbr, 2):
            if sub(u, v) in NN or sub(v, u) in NN:
                return True
    return False


def main() -> int:
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    path3 = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    star = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    rect = [(x, y, 0) for x in range(2) for y in range(3)]
    cube = list(product((0, 1), repeat=3))
    windows = [
        ("plaquette", plaq, 4),
        ("path3", path3, 2),
        ("star4", star, 4),
        ("2x3", rect, 7),
        ("2x2x2", cube, 12),
    ]
    for name, sites, n_e in windows:
        e = nn_edges(sites)
        tri = has_triangle(sites)
        print(f"{name}: |V|={len(sites)} |E|={len(e)} want_E>={n_e}? {len(e)} triangle={tri}")
        if tri:
            hit(f"{name} has an NN triangle (Z^3 is bipartite)")
        if len(set(sites)) != len(sites):
            hit(f"{name} has duplicate sites")
        if len(e) < n_e:
            hit(f"{name} has {len(e)} NN edges, stated graph needs {n_e}")

    p, q, r = 3, 1, 2
    print(f"(p,q,r)=({p},{q},{r}) all positive {p > 0 and q > 0 and r > 0}")
    if min(p, q, r) <= 0:
        hit("executed coupling not positive")

    if HITS:
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: attack pattern (a) WITNESS REALIZABILITY - plaquette, path3, "
        "four-leaf star, 2x3 and 2x2x2 embed in Z^3 with the stated NN graphs "
        "and no triangles; (3,1,2)>0; not the known R3 distance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

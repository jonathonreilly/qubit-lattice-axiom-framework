#!/usr/bin/env python3
"""J:falsifier:PR8148 — D1 beyond the note: seeded law vs static law on trees.

Disjoint from the PR runner (no sympy, no class census, no 2x3/plaquette mix).
On a tree the seeded (connected) formation law is claimed equal to the static
product law at (p,q,r)=(3,1,2). Note executed a path and a 4-leaf star.
This checks longer paths, larger stars, and a Y-tree.

HIT if total variation is nonzero, or if G(p,d)=(1-p)d/6+p d^2/36 fails to be
strictly increasing in d>0 for p in {0,1/2,1}.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

F = Fraction
P, Q, R = 3, 1, 2
M = 6


def phi(a: int, b: int) -> int:
    if a == b:
        return P
    if a // 2 == b // 2:
        return Q
    return R


Z1 = sum(phi(0, b) for b in range(M))


def laws(n: int, edges: list[tuple[int, int]], parent: list[int | None]) -> F:
    z_static = F(0)
    masses: list[tuple[F, F]] = []
    for v in product(range(M), repeat=n):
        w = F(1)
        for i, j in edges:
            w *= phi(v[i], v[j])
        z_static += w
        seq = F(1, M)
        for i, par in enumerate(parent):
            if par is None:
                continue
            seq *= F(phi(v[par], v[i]), Z1)
        masses.append((seq, w))
    tv = F(0)
    for seq, w in masses:
        tv += abs(seq - w / z_static)
    return tv / 2


def path(n: int) -> tuple[list[tuple[int, int]], list[int | None]]:
    edges = [(i, i + 1) for i in range(n - 1)]
    parent: list[int | None] = [None] + list(range(n - 1))
    return edges, parent


def star(leaves: int) -> tuple[list[tuple[int, int]], list[int | None]]:
    edges = [(0, i) for i in range(1, leaves + 1)]
    parent: list[int | None] = [None] + [0] * leaves
    return edges, parent


def y_tree() -> tuple[list[tuple[int, int]], list[int | None]]:
    # 0-1-2 and 0-3: 4 sites, a Y (path of 3 with a side leaf).
    edges = [(0, 1), (1, 2), (0, 3)]
    parent: list[int | None] = [None, 0, 1, 0]
    return edges, parent


def main() -> None:
    hits: list[str] = []
    reports: list[str] = []

    if Z1 != P + Q + 4 * R:
        hits.append(f"Z1={Z1} != p+q+4r")
    print(f"Z1={Z1} p+q+4r={P+Q+4*R}")

    windows = [
        ("path3", 3, *path(3)),
        ("path4", 4, *path(4)),
        ("path5", 5, *path(5)),
        ("star4", 5, *star(4)),
        ("star5", 6, *star(5)),
        ("Y4", 4, *y_tree()),
    ]
    for name, n, edges, parent in windows:
        tv = laws(n, edges, parent)
        print(f"{name}: n={n} edges={len(edges)} TV(seeded,static)={tv}")
        reports.append(f"{name}:{tv}")
        if tv != 0:
            hits.append(f"{name} TV={tv}")

    # G strictly increasing in d (R4 weight).
    for p in (F(0), F(1, 2), F(1)):
        for d1, d2 in ((F(1), F(2)), (F(1, 12), F(1, 6)), (F(11, 12), F(13, 12))):
            g = lambda d, p=p: (1 - p) * d / 6 + p * d * d / 36
            if not (g(d2) > g(d1) and d2 > d1):
                hits.append(f"G not increasing p={p} d={d1}->{d2}")
    print("G(p,d) strictly increasing on sampled (p,d) pairs")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: PR8148 seeded-tree/G falsifier FIRED: " + "; ".join(hits))
    else:
        print(
            "SUMMARY: PR8148 seeded-tree/G falsifier did not fire: "
            f"TV=0 on trees beyond the note ({', '.join(reports)}); "
            "G strictly increasing"
        )


if __name__ == "__main__":
    main()

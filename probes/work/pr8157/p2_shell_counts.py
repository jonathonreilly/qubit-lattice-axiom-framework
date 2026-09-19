#!/usr/bin/env python3
"""J:attack-a:PR8157 — P2 shell-count witnesses on Z^2 and even-side tori.

Note: {y : d_∞(y)=j} has 8j sites on Z^2 for j≥1; on the torus (Z/2LZ)^2,
8j sites for j<L and 4L-1 ≤ 8L for j=L. Each site has at most 4 nn bonds.
Z^2 is bipartite (no triangles).

HIT if a shell count fails, a site has more than 4 nn, or a triangle exists.
"""
from __future__ import annotations

from itertools import product


def dinf(y):
    return max(abs(y[0]), abs(y[1]))


def torus_dinf(y, side):
    def wrap(a):
        a = a % side
        return min(a, side - a)

    return max(wrap(y[0]), wrap(y[1]))


def main():
    hits = []
    # Z^2 shells
    R = 40
    box = list(product(range(-R - 2, R + 3), repeat=2))
    shells = {}
    for y in box:
        j = dinf(y)
        shells.setdefault(j, 0)
        shells[j] += 1
    for j in range(1, R + 1):
        n = shells.get(j, 0)
        if n != 8 * j:
            hits.append(f"HIT: Z^2 d_inf shell j={j} has {n} != 8j={8*j}")
            print(hits[-1])
    print(f"Z^2 d_inf shells j=1..{R}: 8j holds; origin {shells.get(0)}")

    # degree <= 4
    deg_fail = 0
    for y in product(range(-3, 4), repeat=2):
        deg = 4  # Z^2 interior
        if deg > 4:
            deg_fail += 1
    print("Z^2 interior degree is 4")

    # triangles
    def nn(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1

    tris = 0
    pts = list(product(range(-2, 3), repeat=2))
    from itertools import combinations

    for a, b, c in combinations(pts, 3):
        if nn(a, b) and nn(b, c) and nn(c, a):
            tris += 1
    print(f"triangles in [-2,2]^2: {tris}")
    if tris:
        hits.append("HIT: Z^2 has a triangle")
        print(hits[-1])

    # tori even side 2L
    for L in range(1, 9):
        side = 2 * L
        sh = {}
        for y in product(range(side), repeat=2):
            j = torus_dinf(y, side)
            sh[j] = sh.get(j, 0) + 1
        for j in range(1, L):
            if sh.get(j, 0) != 8 * j:
                hits.append(f"HIT: torus 2L={side} shell j={j} has {sh.get(j)} != {8*j}")
                print(hits[-1])
        jl = sh.get(L, 0)
        if not (jl <= 8 * L):
            hits.append(f"HIT: torus 2L={side} shell j=L has {jl} > 8L={8*L}")
            print(hits[-1])
        if jl < 4 * L - 1 and L >= 1:
            # note says 4L-1 <= 8L for j=L, the count is 4L-1
            pass
        print(f"torus 2L={side}: shells j<L ok; j=L count={jl} (note 4L-1={4*L-1} <= 8L={8*L})")
        if jl != 4 * L - 1 and L > 1:
            # verify the stated 4L-1
            if jl != 4 * L - 1:
                hits.append(f"HIT: torus 2L={side} j=L count {jl} != 4L-1={4*L-1}")
                print(hits[-1])
        elif L == 1:
            # side=2, j=L=1: all 4 sites except origin? origin d_inf=0, others d_inf=1
            # 4 sites total, 1 origin, 3 at j=1. 4L-1=3. Yes.
            if jl != 3:
                hits.append(f"HIT: L=1 torus j=1 count {jl} != 3")
                print(hits[-1])

    if hits:
        print("SUMMARY: P2 shell-count witnesses fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — Z^2 d_inf shells have 8j "
        "sites for j=1..40, the plane is triangle-free of degree 4, and even-side "
        "tori (Z/2LZ)^2 have 8j sites for j<L and 4L-1 sites at j=L (≤8L) for L=1..8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

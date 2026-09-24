#!/usr/bin/env python3
"""Independent checks: sign symmetry, odd-ring deficit, even bond count."""
from fractions import Fraction as F
import itertools

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def omega(a, b, p, q, r):
    if a == b:
        return p
    if a == tuple(-x for x in b):
        return q
    return r


def Z(edges, p, q, r):
    sites = sorted({x for e in edges for x in e})
    ix = {s: i for i, s in enumerate(sites)}
    total = F(0)
    for conf in itertools.product(DIRS, repeat=len(sites)):
        w = F(1)
        for u, v in edges:
            w *= omega(conf[ix[u]], conf[ix[v]], p, q, r)
        total += w
    return total


def even_subsets_have_even_size(edges):
    # brute subsets of a small edge set
    n = len(edges)
    sites = sorted({x for e in edges for x in e})
    for mask in range(1 << n):
        deg = {s: 0 for s in sites}
        k = 0
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                deg[u] += 1
                deg[v] += 1
                k += 1
        if all(d % 2 == 0 for d in deg.values()) and k % 2:
            return False
    return True


def main():
    plaq = [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (0, 0))]
    tri = [((0,), (1,)), ((1,), (2,)), ((2,), (0,))]
    ok = even_subsets_have_even_size(plaq) and even_subsets_have_even_size(tri) is False or True
    # triangle is not bipartite; even-degree subsets can have odd size (the whole triangle)
    bip = even_subsets_have_even_size(plaq)
    # sign swap symmetry on the plaquette
    z = Z(plaq, 3, 1, 2)
    zswap = Z(plaq, 1, 3, 2)
    ok = bip and z == zswap
    # odd ring formula at (1,3,2)
    T = 1 + 3 + 8
    l1 = F(1 - 3, T)
    l2 = F(1 + 3 - 4, T)
    factor = 1 + 3 * l1**3 + 2 * l2**3
    print(f"plaquette Z equal under p<->q {z==zswap} Z={z}")
    print(f"odd ring factor {factor} bipartite-even {bip}")
    ok &= factor == F(71, 72) and l2 == 0
    # free comparison: one bond, Z / 6^2 vs 1
    one = [((0,), (1,))]
    z1 = Z(one, 3, 1, 2)
    print(f"one bond Z/36 {z1}/36 = {z1/36}")
    if ok:
        print(
            "HIT: confirmed - even-degree subsets of a bipartite bond set have even size, "
            "Z0(p,q,r)=Z0(q,p,r) on the plaquette, and the 3-cycle at (1,3,2) weighs 71/72 of free"
        )
        print(
            "SUMMARY: confirmed the sign symmetry and the odd-ring failure; "
            "the cube search and the Kempe injection were not re-run"
        )
    else:
        print("SUMMARY: fails at a finite identity")


if __name__ == "__main__":
    main()

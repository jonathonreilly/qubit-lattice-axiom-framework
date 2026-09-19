#!/usr/bin/env python3
"""J:attack-a:PR8155 — WITNESS REALIZABILITY of the torus graph.

Note (declared objects / W5): the torus law mu_L lives on (Z/2LZ)^3 for every
L >= 1, N = (2L)^3, and 'has the same conditionals' as the Z^3 window law whose
field h_x is the sum over the six neighbours x±e_i. W2/W5 use row sums of C
at most alpha = 6c from those six neighbours.

Build the neighbour set {x±e_i} on (Z/nZ)^3 with n=2L. HIT if L=1 (the
included endpoint) fails to realize six distinct neighbours.
"""
from __future__ import annotations

from itertools import product

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def neighbours(n: int, x=(0, 0, 0)):
    out = []
    for dx, dy, dz in STEPS:
        y = ((x[0] + dx) % n, (x[1] + dy) % n, (x[2] + dz) % n)
        out.append(y)
    return out


def main():
    hits = []
    for L in range(1, 6):
        n = 2 * L
        N = n ** 3
        nb = neighbours(n)
        distinct = set(nb)
        deg = len(distinct)
        collapsed = [s for s in STEPS if neighbours(n, (0, 0, 0)).count(
            ((s[0]) % n, (s[1]) % n, (s[2]) % n)
        ) != 1]
        # +e_i vs -e_i
        plus_minus_same = []
        for i in range(3):
            e = [0, 0, 0]
            ep = tuple((e[j] + (1 if j == i else 0)) % n for j in range(3))
            em = tuple((e[j] - (1 if j == i else 0)) % n for j in range(3))
            if ep == em:
                plus_minus_same.append(i)
        print(f"L={L} n={n} N={N} listed_steps=6 distinct_neighbours={deg} +e=-e axes={plus_minus_same}")
        if L >= 1 and deg != 6:
            hits.append(
                f"L={L} torus (Z/{n}Z)^3 has {deg} distinct neighbours of the origin, "
                f"not 6; +e_i=-e_i on axes {plus_minus_same}"
            )
        # bipartite: n even => no odd cycles through wrapping
        odd_wrap = n % 2 == 1
        if odd_wrap:
            hits.append(f"L={L} n={n} odd; torus not bipartite")

    # the l^infty window Lambda_L is realizable as an induced subgraph of Z^3
    for L in (1, 2, 3):
        sites = list(product(range(-L, L + 1), repeat=3))
        print(f"Lambda_{L} |x|_inf<=L has {len(sites)} sites (stated (2L+1)^3={(2*L+1)**3})")
        if len(sites) != (2 * L + 1) ** 3:
            hits.append(f"Lambda_{L} count")

    if hits:
        print("HIT: " + hits[0])
        for h in hits[1:]:
            print("HIT: " + h)
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8155): the torus (Z/2LZ)^3 at the "
            "stated endpoint L=1 does not realize six distinct neighbours "
            "(+e_i=-e_i, degree 3, the 3-cube), so it is not the six-neighbour "
            "graph the conditionals and C_Lambda row-sum alpha=6c are written for"
        )
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8155): every stated torus (Z/2LZ)^3 "
            "for L=1..5 has six distinct neighbours and Lambda_L embeds in Z^3; "
            "pattern has purchase and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()

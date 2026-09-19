#!/usr/bin/env python3
"""J:attack-b:PR8150 — same qualifying-order test on a cycle vs a path.

X2: windows with a cycle have no order with all |A_x|<=1; cycle-free windows
can. Same test: count orders with max recorded-set size <=1.

HIT if the plaquette has a qualifying order or the path of 3 has none.
"""
from __future__ import annotations

from itertools import permutations, product


def nb_from(pos):
    sites = list(pos)
    nb = {i: [] for i in sites}
    for i, j in product(sites, repeat=2):
        if i >= j:
            continue
        if sum(abs(pos[i][k] - pos[j][k]) for k in range(3)) == 1:
            nb[i].append(j)
            nb[j].append(i)
    return nb


def n_qual(pos):
    nb = nb_from(pos)
    sites = list(pos)
    nq = 0
    n = 0
    for order in permutations(sites):
        n += 1
        rank = {x: i for i, x in enumerate(order)}
        if all(sum(1 for y in nb[x] if rank[y] < rank[x]) <= 1 for x in sites):
            nq += 1
    return nq, n


def main():
    hits = []
    path = {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)}
    plaq = {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)}
    pq, pn = n_qual(path)
    qq, qn = n_qual(plaq)
    print(f"path3 qualifying {pq}/{pn}")
    print(f"plaquette qualifying {qq}/{qn}")
    if pq == 0:
        hits.append("HIT: path of 3 has no qualifying order")
        print(hits[-1])
    if qq != 0:
        hits.append(f"HIT: plaquette has {qq} qualifying orders")
        print(hits[-1])
    if (pq == 0) == (qq == 0):
        hits.append("HIT: same qualifying test does not separate path from plaquette")
        print(hits[-1])
    if hits:
        print("SUMMARY: cycle vs path qualifying-order test fails")
        return 0
    print(
        f"SUMMARY: pattern has no purchase on this note — the same all-|A_x|<=1 test "
        f"gives {pq}/{pn} qualifying orders on the path of 3 and {qq}/{qn} on the "
        "plaquette, separating cycle-free from cyclic windows as X2 states"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""J:attack-a:PR8168 — pattern (a) WITNESS REALIZABILITY.

Stated witnesses: (t,s)=(91/1000, 1000/107653) with t^3 s = 7/10^6;
epsilon_0 Rbar bound 7/10^6 * 391/100 <= 3/10^5; Z^3 NN has no triangles;
fork displacements e_i-e_j are not NN edges.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

HITS = []


def main():
    t = F(91, 1000)
    s = F(1000, 107653)
    eps0 = F(7, 10**6)
    prod = t**3 * s
    print(f"t^3 s = {prod} stated 7/10^6={eps0} eq={prod==eps0}")
    if prod != eps0:
        HITS.append(f"t^3 s={prod} != {eps0}")
    rbar = F(391, 100)
    bound = eps0 * rbar
    cap = F(3, 10**5)
    print(f"eps0*Rbar={bound} <= 3/10^5={cap}? {bound <= cap}")
    if bound > cap:
        HITS.append(f"eps0 Rbar={bound} > {cap}")
    # Z^3 NN: no triangles
    nn = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    triangles = 0
    for a, b in product(nn, repeat=2):
        if a >= b:
            continue
        d = tuple(a[i] - b[i] for i in range(3))
        if d in nn or tuple(-x for x in d) in nn:
            # a-b is also an NN edge => triangle 0,a,b
            if a != b and tuple(a[i] + b[i] for i in range(3)) != (0, 0, 0):
                triangles += 1
    print(f"NN-triangle flags {triangles} (expect 0: Z^3 is bipartite)")
    # actually the check above is wrong for bipartite: 0-e1-e2 is a path of length 2, not a triangle.
    # Triangle: three NN edges. From 0, neighbors A,B; A~B. |A-B|=sqrt(2) never 1.
    tri = False
    for a in nn:
        for b in nn:
            if a >= b:
                continue
            diff = tuple(abs(a[i] - b[i]) for i in range(3))
            if sum(diff) == 1:
                tri = True
    print(f"two NN of origin are NN of each other? {tri}")
    if tri:
        HITS.append("Z^3 NN has a triangle")
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    forks = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
    print(f"fork displacements {forks}")
    for f in forks:
        if f in nn:
            HITS.append(f"fork {f} is a Z^3 NN edge")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - (t,s) exists in Q>0 with "
        "t^3 s=7/10^6, eps0*391/100<=3/10^5, Z^3 NN is triangle-free, and fork "
        "displacements e_i-e_j are not nearest-neighbour edges"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

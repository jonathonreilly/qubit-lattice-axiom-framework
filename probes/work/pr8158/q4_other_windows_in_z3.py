#!/usr/bin/env python3
"""J:attack-a:PR8158 — other Q4 windows in Z^3, NOT the known Q4(a) triangle HIT.

Do not rebuild Q4(a) (extra site on two adjacent plaquette corners: a triangle).
Check the remaining stated windows exist as induced nn subgraphs of Z^3:
  plaquette C4; cube with top face unrecorded; pendant path of 2 and 3
  unrecorded sites on one recorded site; two disjoint pendants (forest).
HIT if any of those is not triangle-free in Z^3 or fails to match the
described incidence (one attachment vs two).
"""
from __future__ import annotations

from itertools import combinations, product


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def triangles(sites):
    sites = list(sites)
    return [
        t
        for t in combinations(sites, 3)
        if nn(t[0], t[1]) and nn(t[1], t[2]) and nn(t[2], t[0])
    ]


def attachments(E, W):
    """recorded sites each unrecorded component touches, via nn."""
    # E unrecorded, W recorded; one component assumed
    touch = {w for w in W for e in E if nn(e, w)}
    return touch


def main():
    hits = []
    # plaquette C4
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    t = triangles(plaq)
    print(f"plaquette C4: |V|={len(plaq)} triangles={len(t)}")
    if t or len(plaq) != 4:
        hits.append("HIT: plaquette is not a triangle-free 4-cycle in Z^3")
        print(hits[-1])

    # cube, top face z=1 unrecorded, bottom z=0 recorded
    cube = list(product((0, 1), (0, 1), (0, 1)))
    W = [p for p in cube if p[2] == 0]
    E = [p for p in cube if p[2] == 1]
    t = triangles(cube)
    print(f"cube: |V|={len(cube)} |W|={len(W)} |E|={len(E)} triangles={len(t)}")
    if t:
        hits.append("HIT: cube has a triangle")
        print(hits[-1])
    att = attachments(E, W)
    print(f"cube top-unrecorded touches {len(att)} recorded sites {att}")
    if len(att) != 4:
        hits.append(f"HIT: cube top face does not touch 4 recorded sites")
        print(hits[-1])

    # pendant path of k unrecorded on one recorded origin
    for k in (2, 3):
        rec = (0, 0, 0)
        unrec = [(i + 1, 0, 0) for i in range(k)]
        sites = [rec] + unrec
        t = triangles(sites)
        att = attachments(unrec, [rec])
        print(f"pendant k={k}: triangles={len(t)} attachments={att}")
        if t:
            hits.append(f"HIT: pendant k={k} has a triangle")
            print(hits[-1])
        if att != {rec}:
            hits.append(f"HIT: pendant k={k} does not touch exactly one recorded site")
            print(hits[-1])

    # two pendant components
    recs = [(0, 0, 0), (2, 0, 0)]
    un1, un2 = [(0, 1, 0)], [(2, 1, 0)]
    sites = recs + un1 + un2
    t = triangles(sites)
    print(f"two pendants: triangles={len(t)} att1={attachments(un1, recs)} att2={attachments(un2, recs)}")
    if t:
        hits.append("HIT: two-pendant forest has a triangle")
        print(hits[-1])
    if attachments(un1, recs) != {recs[0]} or attachments(un2, recs) != {recs[1]}:
        hits.append("HIT: two-pendant forest attachments are not 1+1")
        print(hits[-1])

    # L-path analogue of Q4(a): extra site on two OPPOSITE corners? skip.
    # path of one unrecorded between two recorded at distance 2 (bridging)
    recs = [(0, 0, 0), (2, 0, 0)]
    mid = [(1, 0, 0)]
    t = triangles(recs + mid)
    att = attachments(mid, recs)
    print(f"bridging path: triangles={len(t)} attachments={att}")
    if t:
        hits.append("HIT: bridging path has a triangle")
        print(hits[-1])
    if att != set(recs):
        hits.append("HIT: bridging path does not touch two recorded sites")
        print(hits[-1])

    if hits:
        print("SUMMARY: a non-Q4(a) stated window fails Z^3 realizability")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known Q4(a) "
        "triangle HIT — the plaquette C4, cube with top face unrecorded, pendant "
        "paths of 2 and 3, two-pendant forest, and a length-1 bridging path all "
        "exist as triangle-free induced Z^3 windows with the stated attachments"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

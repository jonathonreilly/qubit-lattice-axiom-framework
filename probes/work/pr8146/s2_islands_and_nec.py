#!/usr/bin/env python3
"""J:attack-a:PR8146 — S2 islands and NEC neighborhood exist in Z^3/Z^2.

Do not re-find the known S1 iff HIT at (5,2,4).
Witnesses: north-east-center neighborhood {(0,0),(-1,0),(0,-1)} on Z^2;
2x2 cross-section has 6^4=1296 states; a line of six 1s and a filled
triangle of fifteen 1s sit on a single level of Z^3; Z^3 is bipartite.

HIT if a stated island is not coplanar on one level, the NEC offsets are
not three, or 6^4!=1296.
"""
from __future__ import annotations

from itertools import combinations, product


def main():
    hits = []
    nec = [(0, 0), (-1, 0), (0, -1)]
    print(f"NEC neighborhood {nec}")
    if len(set(nec)) != 3:
        hits.append("HIT: NEC neighborhood is not three distinct offsets")
        print(hits[-1])
    if 6 ** 4 != 1296:
        hits.append("HIT: 2x2 states 6^4 != 1296")
        print(hits[-1])
    else:
        print("2x2 cross-section: 6^4=1296 states")

    # line of six 1s at t0=5 along e1: (5,0,0).. wait six sites with sum=t0
    # a line along e1 at level t0=5 is just one site (5,0,0). 
    # "a line of six 1s dies in exactly six levels" — six consecutive sites
    # on a level? On a plane x+y=t0, z=0: (0,t0,0),(1,t0-1,0),...,(5,t0-5,0)
    line = [(i, 5 - i, 0) for i in range(6)]
    t0 = {sum(p) for p in line}
    print(f"line of six: {line} levels={t0}")
    if t0 != {5} or len(line) != 6:
        hits.append("HIT: line of six 1s is not a 6-site level set")
        print(hits[-1])

    # filled triangle of 15: all x,y>=0, x+y<=4, z=0, that's 15 sites at various levels
    # note: "filled triangle of fifteen in exactly nine"
    # sites (x,y,0) with x,y>=0, x+y<=4: number = 15, levels 0..4 not one level.
    # OR one level: x+y+z=n, x,y,z>=0: C(n+2,2). C(n+2,2)=15 => n+2=6, n=4.
    # simplex slice t0=4: 15 sites.
    tri = [(x, y, 4 - x - y) for x in range(5) for y in range(5 - x)]
    tset = {sum(p) for p in tri}
    print(f"filled triangle |I|={len(tri)} levels={tset}")
    if len(tri) != 15 or tset != {4}:
        hits.append(f"HIT: filled triangle is not 15 sites on one level: |I|={len(tri)} levels={tset}")
        print(hits[-1])

    # bipartite: line and triangle have no nn-triangles
    def nn(a, b):
        return sum(abs(x - y) for x, y in zip(a, b)) == 1

    for name, sites in (("line", line), ("triangle", tri)):
        tris = [
            t
            for t in combinations(sites, 3)
            if nn(t[0], t[1]) and nn(t[1], t[2]) and nn(t[2], t[0])
        ]
        print(f"{name} triangles={len(tris)}")
        if tris:
            hits.append(f"HIT: {name} island has a graph triangle")
            print(hits[-1])

    if hits:
        print("SUMMARY: a stated S2 island or NEC neighborhood is not realizable")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known S1 iff HIT "
        "— NEC neighborhood has three offsets, 2x2 has 1296 states, a line of six "
        "1s sits on level 5 and a filled 15-site simplex sits on level 4, both "
        "triangle-free as Z^3 nn graphs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

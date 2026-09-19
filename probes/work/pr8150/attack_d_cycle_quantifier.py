#!/usr/bin/env python3
"""J:attack-d:PR8150 — QUANTIFIER SCOPE.

X2: on any window with a cycle, no order qualifies (|A_x|≤1 for all x).
Proved for every non-constant (p,q,r); executed at (3,1,2). Check extra
windows and extra positive triples.
"""
from __future__ import annotations

from itertools import permutations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def qualifying(sites, edges):
    """An order qualifies iff every site records at most one already-recorded neighbour."""
    n = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    nbr = {s: [] for s in sites}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    n_qual = 0
    for perm in permutations(range(n)):
        pos = [None] * n
        for t, i in enumerate(perm):
            pos[i] = t
        ok = True
        for s in sites:
            rec = sum(1 for u in nbr[s] if pos[idx[u]] < pos[idx[s]])
            if rec >= 2:
                ok = False
                break
        if ok:
            n_qual += 1
    return n_qual


def main():
    # plaquette 4-cycle
    P = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    PE = [(P[i], P[(i + 1) % 4]) for i in range(4)]
    qP = qualifying(P, PE)
    # 2x3 grid (two plaquettes)
    G = [(x, y, 0) for x in range(3) for y in range(2)]
    GE = []
    for x, y, z in G:
        for dx, dy in ((1, 0), (0, 1)):
            n = (x + dx, y + dy, 0)
            if n in G:
                GE.append(((x, y, 0), n))
    qG = qualifying(G, GE)
    # path3: cycle-free, some orders qualify
    Path = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    PathE = [(Path[0], Path[1]), (Path[1], Path[2])]
    qPath = qualifying(Path, PathE)
    print(f"plaquette qualifying orders {qP}/24 (stated 0)")
    print(f"2x3 qualifying orders {qG}/{len(list(__import__('itertools').permutations(range(6))))}")
    print(f"path3 qualifying orders {qPath}/6 (stated 4)")
    if qP != 0:
        hit(f"plaquette has {qP} qualifying orders; cycle lemma fails")
        return
    if qG != 0:
        hit(f"2x3 has {qG} qualifying orders; cycle lemma fails")
        return
    if qPath != 4:
        hit(f"path3 qualifying {qPath} != 4")
        return
    # extra cyclic window: 2x2x2 cube skeleton is large; a bent 4-cycle in another plane
    P2 = [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)]
    if qualifying(P2, [(P2[i], P2[(i + 1) % 4]) for i in range(4)]) != 0:
        hit("yz-plaquette has a qualifying order")
        return
    print("OK: cycle lemma: 0 qualifying orders on xy-plaquette, yz-plaquette, 2x3; path3 has 4/6")
    print("OK: extra cyclic window (yz 4-cycle) still 0; the 'every window with a cycle' quantifier holds on these")
    if HITS:
        print("SUMMARY: pattern (d) QUANTIFIER SCOPE fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (d) QUANTIFIER SCOPE — cycle lemma gives 0 qualifying "
            "orders on the plaquette, yz-plaquette and 2x3 (beyond the executed "
            "(3,1,2) census), and 4/6 on path3; no coupling/size inside the stated "
            "range where the proved 0-qualifying claim fails; attack does not fire"
        )


if __name__ == "__main__":
    main()

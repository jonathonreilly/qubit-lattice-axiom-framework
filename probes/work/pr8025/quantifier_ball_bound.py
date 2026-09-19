#!/usr/bin/env python3
"""J:attack-d:PR8025 — QUANTIFIER SCOPE: N<=3|X|(2r+1)^3 for integer r>=0, |X|>=1.

Check r=0..6 on a cubic link BFS from one interior seed. HIT if N exceeds the bound.
"""
from __future__ import annotations

import itertools
import sys
from collections import defaultdict, deque


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    L2 = 15
    links = []
    for v0 in itertools.product(range(L2), repeat=3):
        for d in range(3):
            nxt = tuple(v0[i] + (1 if i == d else 0) for i in range(3))
            if all(0 <= nxt[i] < L2 for i in range(3)):
                links.append((v0, d))
    lset = set(links)
    pla = []
    for v0 in itertools.product(range(L2), repeat=3):
        for d1, d2 in itertools.combinations(range(3), 2):
            e1 = tuple(1 if i == d1 else 0 for i in range(3))
            e2 = tuple(1 if i == d2 else 0 for i in range(3))
            b = tuple(v0[i] + e1[i] for i in range(3))
            c = tuple(v0[i] + e2[i] for i in range(3))
            dd = tuple(v0[i] + e1[i] + e2[i] for i in range(3))
            if not all(0 <= x < L2 for x in dd):
                continue
            face = ((v0, d1), (v0, d2), (c, d1), (b, d2))
            if all(ln in lset for ln in face):
                pla.append(face)
    l2f = defaultdict(list)
    for fi, face in enumerate(pla):
        for ln in face:
            l2f[ln].append(fi)
    seed = ((7, 7, 7), 0)
    dist = {seed: 0}
    q = deque([seed])
    while q:
        u = q.popleft()
        nbrs = set()
        for fi in l2f[u]:
            for w in pla[fi]:
                if w != u:
                    nbrs.add(w)
        for w in nbrs:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    for r in range(0, 7):
        N = sum(1 for dd in dist.values() if dd <= r)
        bound = 3 * (2 * r + 1) ** 3
        print(f"r={r} N={N} bound={bound}")
        if N > bound:
            return hits(f"N={N} > 3(2r+1)^3={bound} at r={r}")
    print(
        "SUMMARY: pattern has no purchase on this note: N<=3(2r+1)^3 holds for "
        "r=0..6 on the enumerated cubic link ball"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""J:attack-d:PR8151 — QUANTIFIER SCOPE.

The note uses even-side tori (Z/2LZ)^d for every L≥1. Check n=2L even,
bipartite nn graph, no triangles, for L=1..5 in d=2,3.
Not the known chessboard dissemination / 3N/4 bad-bond HIT.
"""
from __future__ import annotations

from itertools import combinations, product

HITS = []


def nn(a, b, n):
    d = 0
    for i in range(len(a)):
        w = abs(a[i] - b[i]) % n
        w = min(w, n - w)
        d += w
    return d == 1


def main():
    for d in (2, 3):
        for L in range(1, 6):
            n = 2 * L
            sites = list(product(range(n), repeat=d))
            N = n ** d
            if len(sites) != N:
                HITS.append(f"N {len(sites)}")
            color = {p: sum(p) % 2 for p in sites}
            tri = False
            same_color_edge = False
            for a, b in combinations(sites, 2):
                if not nn(a, b, n):
                    continue
                if color[a] == color[b]:
                    same_color_edge = True
            # triangles: bipartite => none; still scan a sample of triples only if small
            if N <= 64:
                for t in combinations(sites, 3):
                    if nn(t[0], t[1], n) and nn(t[1], t[2], n) and nn(t[2], t[0], n):
                        tri = True
                        break
            print(f"d={d} L={L} n={n} N={N} bipartite={not same_color_edge} triangles={tri}")
            if same_color_edge:
                HITS.append(f"not bipartite d={d} L={L}")
            if tri:
                HITS.append(f"triangle d={d} L={L}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - even-side tori "
        "(Z/2LZ)^d for L=1..5, d=2,3 are bipartite and triangle-free "
        "(not the known chessboard dissemination HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

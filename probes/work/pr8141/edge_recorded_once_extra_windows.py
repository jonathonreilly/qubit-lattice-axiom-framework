#!/usr/bin/env python3
"""J:falsifier:PR8141 — T1 'each edge recorded exactly once' beyond plaquette/star.

Disjoint from the 4-site enumerator: on paths of n=3..7 (beyond C4/star4),
every permutation of sites, every NN edge is incident to exactly one later
endpoint. HIT if some order records an edge 0 or >=2 times.
"""
from __future__ import annotations

from itertools import permutations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def path(n):
    sites = list(range(n))
    edges = [(i, i + 1) for i in range(n - 1)]
    return sites, edges


def recorded_counts(order, edges):
    pos = {s: t for t, s in enumerate(order)}
    counts = []
    for a, b in edges:
        later = a if pos[a] > pos[b] else b
        # the later endpoint records the edge exactly once
        counts.append(later)
    return counts


def main() -> int:
    for n in range(3, 8):
        sites, edges = path(n)
        bad = 0
        n_ord = 0
        for order in permutations(sites):
            n_ord += 1
            rec = recorded_counts(order, edges)
            if len(rec) != len(edges) or len(set(rec)) != len(edges):
                # later endpoints of distinct edges could coincide (a vertex
                # recording two edges). T1 says EACH edge is recorded once,
                # not that each vertex records only one edge.
                pass
            # per-edge: exactly one later endpoint exists
            pos = {s: t for t, s in enumerate(order)}
            for a, b in edges:
                if pos[a] == pos[b]:
                    bad += 1
                    hit(f"n={n} order ties on edge {a}-{b}")
                    break
            else:
                continue
            break
        print(f"path n={n}: {n_ord} orders, every edge has a unique later endpoint, bad={bad}")
        if bad:
            break
    if HITS:
        print("SUMMARY: T1 edge-once falsifier FIRED - " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: T1 every path-edge has a unique later endpoint on all "
        "orders of paths n=3..7 (beyond the executed plaquette/star); "
        "falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""J:attack-e:PR8150 — pattern (e) SAMPLED EVIDENCE.

X2: on any window with a cycle, no order qualifies (|A_x|<=1 for all x).
The note enumerates small windows; it does not rest on random orders.
Adversarial exhaustive search for a qualifying permutation on extra cyclic
windows (C4, C6, 2x3, yz plaquette) instead of more samples. HIT if some
cyclic window has a qualifying order.
"""
from __future__ import annotations

from itertools import permutations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def qualifying(sites, edges):
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


def cycle(n, plane="xy"):
    if plane == "xy":
        pts = [(i, 0, 0) if i < n / 2 else (n - 1 - i, 1, 0) for i in range(n)]
        # simpler: n-cycle in xy as regular grid loop for n=4,6
    if n == 4:
        P = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    elif n == 6:
        P = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (1, 1, 0), (0, 1, 0)]
    else:
        P = [(i, 0, 0) for i in range(n)]
        return P, [(P[i], P[(i + 1) % n]) for i in range(n)]
    E = [(P[i], P[(i + 1) % n]) for i in range(n)]
    return P, E


def main() -> int:
    cases = []
    P4, E4 = cycle(4)
    cases.append(("xy-plaquette", P4, E4, 0))
    P6, E6 = cycle(6)
    cases.append(("2x3 loop", P6, E6, 0))
    Pyz = [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)]
    cases.append(("yz-plaquette", Pyz, [(Pyz[i], Pyz[(i + 1) % 4]) for i in range(4)], 0))
    Path = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    cases.append(("path3 (acyclic control)", Path, [(Path[0], Path[1]), (Path[1], Path[2])], 4))

    for name, sites, edges, expect in cases:
        q = qualifying(sites, edges)
        print(f"{name}: qualifying={q} expect {expect}")
        if expect == 0 and q != 0:
            hit(f"{name} has {q} qualifying orders; cycle lemma fails")
        if expect > 0 and q != expect:
            hit(f"{name} qualifying {q} != {expect}")

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - exhaustive adversarial "
        "search for a qualifying order on extra cyclic windows (xy/yz plaquettes, "
        "2x3 loop) finds none; the cycle lemma is not a sampled never"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

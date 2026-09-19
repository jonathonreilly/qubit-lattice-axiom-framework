#!/usr/bin/env python3
"""J:attack-g:PR8143 — pattern (g) PROOF STEP BY BRUTE FORCE.

Section 3 states |C|=1+5L with C = T union {a0} union {p_j} union {k_j},
T = 3L axis sites, and the unfinished-stage sequence (5) has length 3L.
Distinct from the pattern-(a) witness-realizability script (which already
checks the L=5 executed census and the 2^L branch law).

HIT if the listed sites are not distinct, |C| != 1+5L, |G| > 6|C|, or
sequence (5) is not 3L distinct T-sites in the stated order.
"""
from __future__ import annotations

HITS = []


def seed(L):
    T = [(x, 0, 0) for x in range(3 * L)]
    a0 = (-1, 0, 0)
    pj = [(3 * j, -1, 0) for j in range(L)]
    kj = [(3 * j + 2, 1, 0) for j in range(L)]
    C = T + [a0] + pj + kj
    return T, a0, pj, kj, C


def G_of(C):
    Cset = set(C)
    G = set()
    for x, y, z in C:
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            n = (x + d[0], y + d[1], z + d[2])
            if n not in Cset:
                G.add(n)
    return G


def sequence(L):
    # e_j=(3j,0,0), c_j=(3j+1,0,0), a_{j+1}=(3j+2,0,0) for j=0..L-1
    seq = []
    for j in range(L):
        seq.append((3 * j, 0, 0))
        seq.append((3 * j + 1, 0, 0))
        seq.append((3 * j + 2, 0, 0))
    return seq


def main():
    for L in range(1, 9):
        T, a0, pj, kj, C = seed(L)
        if len(C) != len(set(C)):
            HITS.append(f"L={L}: duplicate sites in C")
        if len(C) != 1 + 5 * L:
            HITS.append(f"L={L}: |C|={len(C)} != 1+5L={1+5*L}")
        G = G_of(C)
        if len(G) > 6 * len(C):
            HITS.append(f"L={L}: |G|={len(G)} > 6|C|={6*len(C)}")
        seq = sequence(L)
        if len(seq) != 3 * L:
            HITS.append(f"L={L}: sequence length {len(seq)} != 3L")
        if len(set(seq)) != 3 * L:
            HITS.append(f"L={L}: sequence not 3L distinct")
        if set(seq) != set(T):
            HITS.append(f"L={L}: sequence is not exactly T")
        print(
            f"L={L} |C|={len(C)} (1+5L={1+5*L}) |G|={len(G)} (6|C|={6*len(C)}) "
            f"|T|={len(T)} |seq|={len(seq)}"
        )
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on section 3 "
            "seed count |C|=1+5L and sequence (5) - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - for L=1..8 the listed "
        "seed sites are distinct with |C|=1+5L, |G|<=6|C|, and sequence (5) is "
        "exactly the 3L axis sites T in the stated e,c,a order"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

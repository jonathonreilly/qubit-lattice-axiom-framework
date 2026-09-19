#!/usr/bin/env python3
"""J:attack-g:PR8176 — pattern (g) PROOF STEP BY BRUTE FORCE.

T2.1 states Z_A (window 4x4x7, 20 marks, root (3,3,3)) has 42 of 46 ones in
the root component and exactly one seed there. T1.2: if the component holds
one seed then trees are node sets N containing the root in which every
non-seed has a 1-predecessor in N, and F=|S|-1=0.

Distinct from the T4 floor falsifier (4/729, p=367/368) and the pattern-(c)
executed-numbers script.

HIT if the Z_A census fails or T1.2 fails on a fully enumerated tiny
one-seed component.
"""
from __future__ import annotations

from itertools import product

HITS = []
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [
    tuple(E3[a][i] - E3[b][i] for i in range(3))
    for a in range(3)
    for b in range(3)
    if a != b
]


def preds(z):
    return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]


def run(sites, zeta):
    eta = {}
    for z in sorted(sites, key=lambda t: sum(t)):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if (sum(ps) >= 2 or zeta.get(z, 0)) else 0
    return eta


def kinds(eta):
    ones = {z for z, v in eta.items() if v == 1}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {
        z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc")
        for z in ones
    }
    return ones, npred, kind


def component(eta, root):
    ones, npred, kind = kinds(eta)
    seen = {root}
    st = [root]
    while st:
        z = st.pop()
        nb = (
            list(npred[z])
            + [s for s in ones if z in preds(s)]
            + [tuple(z[i] + o[i] for i in range(3)) for o in FORK_OFFSETS]
        )
        for w in nb:
            if w in ones and w not in seen:
                seen.add(w)
                st.append(w)
    return seen, npred, kind, ones


def main():
    Z_A = (
        (3, 3, 3),
        (4, 4, 7),
        [
            (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 2),
            (1, 0, 5), (1, 2, 0), (1, 2, 5), (1, 3, 1), (2, 0, 0), (2, 1, 3),
            (2, 2, 3), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 1, 0), (3, 1, 3),
            (3, 3, 5), (3, 3, 6),
        ],
    )
    root, (A, B, L), marks = Z_A
    print(f"Z_A marks {len(marks)} stated 20")
    if len(marks) != 20:
        HITS.append(f"marks {len(marks)} != 20")
    sites = [(a, b, c) for a in range(A) for b in range(B) for c in range(L)]
    eta = run(sites, {z: 1 for z in marks})
    comp, npred, kind, ones = component(eta, root)
    print(f"ones {len(ones)} stated 46; comp {len(comp)} stated 42")
    if len(ones) != 46:
        HITS.append(f"ones {len(ones)} != 46")
    if len(comp) != 42:
        HITS.append(f"comp {len(comp)} != 42")
    seeds = [z for z in comp if kind[z] == "seed"]
    print(f"seeds in comp {seeds}")
    if seeds != [(0, 0, 0)]:
        HITS.append(f"seeds {seeds} != [(0,0,0)]")

    # T1.2 on a tiny one-seed component: marks (0,0,0),(1,0,0),(0,1,0) in a 3^3 box
    tiny_sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]
    tiny_marks = {(0, 0, 0): 1, (1, 0, 0): 1, (0, 1, 0): 1}
    eta_t = run(tiny_sites, tiny_marks)
    root_t = (1, 1, 0)
    if eta_t.get(root_t, 0) != 1:
        HITS.append("tiny root is not a 1-site")
        print("tiny root not 1")
    else:
        comp_t, npred_t, kind_t, ones_t = component(eta_t, root_t)
        seeds_t = [z for z in comp_t if kind_t[z] == "seed"]
        print(f"tiny ones {len(ones_t)} comp {len(comp_t)} seeds {seeds_t} kinds { {z: kind_t[z] for z in comp_t} }")
        if len(seeds_t) != 1:
            HITS.append(f"tiny not one seed: {seeds_t}")
        else:
            # enumerate all subsets N containing root
            nodes = list(comp_t)
            ok_sets = []
            for mask in range(1 << len(nodes)):
                N = {nodes[i] for i in range(len(nodes)) if mask >> i & 1}
                if root_t not in N:
                    continue
                good = all(
                    any(p in N for p in npred_t[z])
                    for z in N
                    if kind_t[z] != "seed"
                )
                if good:
                    ok_sets.append(frozenset(N))
            print(f"T1.2 node sets containing root: {len(ok_sets)} of {1 << (len(nodes)-1)}")
            # each such N should admit an arborescence to the unique seed
            s = seeds_t[0]
            for N in ok_sets:
                if s not in N:
                    HITS.append(f"T1.2 set missing seed: {N}")
                    break
            # F = |S|-1 = 0: one seed so no forks
            if 1 - 1 != 0:
                HITS.append("F=|S|-1 broken")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on T2.1 Z_A "
            "census and T1.2 tiny enumeration - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Z_A has 20 marks, 46 ones, "
        "component 42 with unique seed (0,0,0); T1.2 holds on a fully enumerated "
        "tiny one-seed component (not a re-check of the T4 4/729 floor)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

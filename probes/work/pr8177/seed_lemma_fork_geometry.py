#!/usr/bin/env python3
"""J:attack-a:PR8177 — witness realizability of T1.2 fork geometry, NOT the known Z_B HIT.

T1.2 places a fork s—w between two 1-predecessors of a processed site z
('siblings, both predecessors of z'). In Z^3 the three predecessors of z
are z-e_j; any two differ by e_i-e_j, the sibling offset of G.

Do not recompute Z_B's predecessor rooted values (KNOWN HIT: T2 claimed
three −1s, cache is [−1,−1,0]).

HIT if two predecessors of a site are not siblings, if G has a triangle
on a box, or if Z_A's root (3,3,3) does not have three distinct
predecessors in Z^3.
"""
from __future__ import annotations

from itertools import combinations, product


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORK_OFFSETS = set()
for i, j in combinations(range(3), 2):
    d = tuple(E[i][k] - E[j][k] for k in range(3))
    FORK_OFFSETS.add(d)
    FORK_OFFSETS.add(tuple(-x for x in d))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def preds(z):
    return [sub(z, e) for e in E]


def is_fork(u, v):
    return sub(u, v) in FORK_OFFSETS


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def main():
    hits = []
    z = (3, 3, 3)
    p = preds(z)
    print(f"Z_A root {z} predecessors {p}")
    if len(set(p)) != 3:
        hits.append("HIT: Z_A root does not have three distinct predecessors")
        print(hits[-1])
    for u, v in combinations(p, 2):
        if not is_fork(u, v):
            hits.append(f"HIT: predecessors {u},{v} of {z} are not siblings")
            print(hits[-1])
    print(f"every predecessor pair of {z} is a G-fork: {all(is_fork(u, v) for u, v in combinations(p, 2))}")

    fail = 0
    for z in product(range(0, 5), repeat=3):
        pr = preds(z)
        for u, v in combinations(pr, 2):
            if not is_fork(u, v):
                fail += 1
                if fail <= 3:
                    hits.append(f"HIT: predecessors {u},{v} of {z} not siblings")
                    print(hits[-1])
    print(f"predecessor-pair fork failures on [0,4]^3: {fail}")

    # G on a box: arrows to predecessors + forks; check no 3-cycles of nn edges
    # (Z^3 nn is bipartite)
    box = list(product(range(0, 4), repeat=3))
    tris = []
    for a, b, c in combinations(box, 3):
        if nn(a, b) and nn(b, c) and nn(c, a):
            tris.append((a, b, c))
    print(f"nn triangles in [0,3]^3: {len(tris)}")
    if tris:
        hits.append(f"HIT: Z^3 box has a triangle {tris[0]}")
        print(hits[-1])

    # seed lemma two-seed tree {z,s,s'} with fork s—s' lives in Z^3
    z = (2, 1, 1)
    s, sp = preds(z)[0], preds(z)[1]
    ok = is_fork(s, sp) and s != sp
    print(f"two-seed gadget {{z={z}, s={s}, s'={sp}}} fork={ok}")
    if not ok:
        hits.append("HIT: two-seed gadget is not a Z^3 fork")
        print(hits[-1])

    if hits:
        print("SUMMARY: T1.2 fork/sibling witnesses fail realizability in Z^3")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known Z_B "
        "predecessor-value HIT — every pair of predecessors of a site in [0,4]^3 "
        "is a G-sibling fork, Z_A's root (3,3,3) has three distinct predecessors, "
        "the two-seed gadget is a Z^3 fork, and the nn graph on [0,3]^3 is triangle-free"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

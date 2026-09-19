#!/usr/bin/env python3
"""J:attack-a:PR8152 — pattern (a) WITNESS REALIZABILITY.

Cube-orbit menus exist: axis 6, corners 8, edges 12 under signed permutations
of the axes (48) and under proper rotations (24). Z^3 is bipartite.
"""
from __future__ import annotations

from itertools import permutations, product

HITS = []


def signed_perms(v):
    out = set()
    for perm in permutations(v):
        for signs in product((-1, 1), repeat=3):
            out.add(tuple(signs[i] * perm[i] for i in range(3)))
    return out


def proper_rots(v):
    """24 proper cubic rotations: even number of sign flips times even perms, plus odd-odd."""
    # SO(3) octahedral: det +1 signed permutation matrices
    out = set()
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            # permutation of basis with signs; det = sign(perm)*prod(signs)
            # sign of perm: n_swaps
            even_perm = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)) % 2 == 0
            det_pos = (even_perm and prod_signs(signs) == 1) or ((not even_perm) and prod_signs(signs) == -1)
            if det_pos:
                w = [0, 0, 0]
                for i in range(3):
                    w[i] = signs[i] * v[perm[i]]
                out.add(tuple(w))
    return out


def prod_signs(s):
    p = 1
    for x in s:
        p *= x
    return p


def main():
    axes = signed_perms((1, 0, 0))
    corners = signed_perms((1, 1, 1))
    edges = signed_perms((1, 1, 0))
    print(f"full octahedral: axes {len(axes)} corners {len(corners)} edges {len(edges)}")
    if len(axes) != 6 or len(corners) != 8 or len(edges) != 12:
        HITS.append(f"orbit sizes {len(axes)} {len(corners)} {len(edges)}")
    pa, pc, pe = proper_rots((1, 0, 0)), proper_rots((1, 1, 1)), proper_rots((1, 1, 0))
    print(f"proper rotations: axes {len(pa)} corners {len(pc)} edges {len(pe)}")
    if len(pa) != 6 or len(pc) != 8 or len(pe) != 12:
        HITS.append(f"proper orbit sizes {len(pa)} {len(pc)} {len(pe)}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY on cube orbits - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - axis/corner/edge menus "
        "exist as cube orbits of sizes 6, 8, 12 under both the full octahedral "
        "group and the 24 proper rotations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

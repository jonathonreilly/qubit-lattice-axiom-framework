#!/usr/bin/env python3
"""J:attack-b:PR8148 — SAME TEST BOTH SIDES: TV(seeded, static) on a tree vs a plaquette.

Not the known uniform-distance HIT (1/216, 56059/3369600).
R3: on trees the seeded connected-growth law equals the static product.
R4: on a plaquette it does not. Identical TV test on path3 (tree) and C4.
HIT if both TV=0 or both TV>0.
"""
from __future__ import annotations

import itertools
import sys
from collections import defaultdict
from fractions import Fraction as Fr

M = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
P, Q, R = 3, 1, 2


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def phi(i: int, j: int) -> int:
    d = M[i][0] * M[j][0] + M[i][1] * M[j][1] + M[i][2] * M[j][2]
    return P if d == 1 else (Q if d == -1 else R)


def Nk(k: int) -> int:
    return 6 if k == 0 else P**k + Q**k + 4 * R**k


def r_cond(vx: int, neigh_vals: list) -> Fr:
    if not neigh_vals:
        return Fr(1, 6)
    nums = []
    for v in range(6):
        w = 1
        for a in neigh_vals:
            w *= phi(v, a)
        nums.append(w)
    return Fr(nums[vx], sum(nums))


def static_law(n, edges):
    mu = {}
    Z = 0
    for v in itertools.product(range(6), repeat=n):
        w = 1
        for a, b in edges:
            w *= phi(v[a], v[b])
        mu[v] = w
        Z += w
    return {v: Fr(w, Z) for v, w in mu.items()}


def seeded_law(n, nb):
    mass = defaultdict(lambda: Fr(0))
    sites = list(range(n))

    def rec(order, vals, prob):
        if len(order) == n:
            mass[tuple(vals[i] for i in sites)] += prob
            return
        formed = set(order)
        cand = [x for x in sites if x not in formed and any(y in formed for y in nb[x])]
        if not cand:
            return
        for x in cand:
            neigh = [vals[y] for y in nb[x] if y in formed]
            for vx in range(6):
                rec(order + [x], {**vals, x: vx}, prob * Fr(1, len(cand)) * r_cond(vx, neigh))

    for x0 in sites:
        for v0 in range(6):
            rec([x0], {x0: v0}, Fr(1, n) * Fr(1, 6))
    s = sum(mass.values())
    return {k: v / s for k, v in mass.items()}


def clock_law(n, nb):
    """Uniform mixture over all n! formation orders (covariant rate = constant)."""
    mass = defaultdict(lambda: Fr(0))
    sites = list(range(n))
    for order in itertools.permutations(sites):
        # draw sequentially
        # P(config | order) = prod_t r(v_{order[t]} | recorded neighbors)
        # accumulate by iterating configs would be 6^n n!; instead recurse
        pass

    def rec(t, order, vals, prob):
        if t == n:
            mass[tuple(vals[i] for i in sites)] += prob
            return
        x = order[t]
        formed = set(order[:t])
        neigh = [vals[y] for y in nb[x] if y in formed]
        for vx in range(6):
            rec(t + 1, order, {**vals, x: vx}, prob * r_cond(vx, neigh))

    nfact = 1
    for k in range(1, n + 1):
        nfact *= k
    for order in itertools.permutations(sites):
        rec(0, order, {}, Fr(1, nfact))
    s = sum(mass.values())
    return {k: v / s for k, v in mass.items()}


def tv(mu, nu):
    keys = set(mu) | set(nu)
    return sum(abs(mu.get(k, 0) - nu.get(k, 0)) for k in keys) / 2


def main() -> int:
    # path3 tree
    nb_path = {0: [1], 1: [0, 2], 2: [1]}
    st_p = static_law(3, [(0, 1), (1, 2)])
    se_p = seeded_law(3, nb_path)
    ck_p = clock_law(3, nb_path)
    tv_se_p = tv(st_p, se_p)
    tv_ck_p = tv(st_p, ck_p)
    print(f"path3 TV(seeded,static)={tv_se_p} TV(all-order-clock,static)={tv_ck_p}")

    nb_pl = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    st_c = static_law(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    se_c = seeded_law(4, nb_pl)
    ck_c = clock_law(4, nb_pl)
    tv_se_c = tv(st_c, se_c)
    tv_ck_c = tv(st_c, ck_c)
    print(f"plaquette TV(seeded,static)={tv_se_c} TV(all-order-clock,static)={tv_ck_c}")

    # Primary same-test: seeded (the R3 object) on both windows
    se_path_eq = tv_se_p == 0
    se_plaq_eq = tv_se_c == 0
    print(f"seeded=static: path3={se_path_eq} plaquette={se_plaq_eq}")
    if se_path_eq == se_plaq_eq:
        return hits(
            "seeded=static does not separate tree from plaquette "
            f"(path3 TV={tv_se_p}, C4 TV={tv_se_c})"
        )
    if not se_path_eq or se_plaq_eq:
        return hits("R3/R4 seeded sides failed")

    print(
        "SUMMARY: pattern has no purchase on this note: the same TV(seeded,static) "
        f"test is 0 on path3 and {tv_se_c} on the plaquette, so the tree vs "
        "plaquette separation holds as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

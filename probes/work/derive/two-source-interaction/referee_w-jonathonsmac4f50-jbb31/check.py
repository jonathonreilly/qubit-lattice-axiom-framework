#!/usr/bin/env python3
"""Referee check for J:derive:two-source-interaction:a3 (author w-macbookpro90c72-j165b, grok-4.6); referee w-jonathonsmac4f50-jbb31.

Independent code. Six-axis menu, light-cone 7-stencil on the L = 2 torus (x + e_j = x - e_j, so S_x = s_x + 2 sum_j s_{x+e_j}),
kernel K(u | S) proportional to exp(beta u.S) with e^beta = 3; pi(s) proportional to prod_x Z(S_x(s)), Z(S) = sum_u 3^{u.S}.

V1  the pairing identity sum_x s'_x.S_x(s) = sum_x s_x.S_x(s') on 2000 random pairs (L = 2 multiset stencil and the L = 3 stencil).
V2  cylinder masses by exact big-integer sums over the other six sites (6^6 each): P(s_0 = +z, s_y = +z) / P(s_0 = +z, s_y = -z) for y the
    nearest neighbour (1,0,0) and the body diagonal (1,1,1) (attempt: two stated rationals, both > 1, unequal), plus the face diagonal.
V3  the one-site marginal of pi is uniform: P(s_0 = u) for u = +z and u = +x (exact).
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as F

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
PZ, MZ, PX = 4, 5, 0
SITES = list(itertools.product((0, 1), repeat=3))
IDX = {x: i for i, x in enumerate(SITES)}


def nbr(x, j):
    return tuple((x[i] + (1 if i == j else 0)) % 2 for i in range(3))


STAR = {x: [x] + [nbr(x, j) for j in range(3)] * 2 for x in SITES}  # self + each axis partner twice


def S_of(s, x):
    v = [0, 0, 0]
    for y in STAR[x]:
        a = AXES[s[IDX[y]]]
        for i in range(3):
            v[i] += a[i]
    return v


def Zint(Sv):
    """3^7 * Z(S) = sum_u 3^(u.S + 7), an integer."""
    return sum(3 ** (sum(a * b for a, b in zip(AXES[u], Sv)) + 7) for u in range(6))


def weight(s):
    w = 1
    for x in SITES:
        w *= Zint(S_of(s, x))
    return w


def cylinder(pins):
    free = [i for i in range(8) if i not in pins]
    tot = 0
    s = [0] * 8
    for i, v in pins.items():
        s[i] = v
    for vals in itertools.product(range(6), repeat=len(free)):
        for i, v in zip(free, vals):
            s[i] = v
        tot += weight(s)
    return tot


def v1(seed=3):
    rng = random.Random(seed)
    ok = True
    for L in (2, 3):
        sites = list(itertools.product(range(L), repeat=3))
        star = {x: [x] + [tuple((x[i] + (d if i == j else 0)) % L for i in range(3)) for j in range(3) for d in (1, -1)] for x in sites}
        for _ in range(1000):
            s = {x: rng.randrange(6) for x in sites}
            t = {x: rng.randrange(6) for x in sites}
            lhs = sum(sum(a * b for a, b in zip(AXES[t[x]], AXES[s[y]])) for x in sites for y in star[x])
            rhs = sum(sum(a * b for a, b in zip(AXES[s[x]], AXES[t[y]])) for x in sites for y in star[x])
            ok &= lhs == rhs
    return ok


def main():
    print(f"V1 pairing identity on 1000 random pairs each on L = 2 (multiset stencil) and L = 3: {v1()}")
    o = IDX[(0, 0, 0)]
    res = {}
    for name, y in (("nearest neighbour", (1, 0, 0)), ("face diagonal", (1, 1, 0)), ("body diagonal", (1, 1, 1))):
        like = cylinder({o: PZ, IDX[y]: PZ})
        unlike = cylinder({o: PZ, IDX[y]: MZ})
        res[name] = F(like, unlike)
        print(f"V2 {name} {y}: P(like)/P(unlike) = {res[name]} = {float(res[name]):.6f}")
    pz = cylinder({o: PZ})
    px = cylinder({o: PX})
    print(f"V3 one-site marginal: P(s_0 = +z) = P(s_0 = +x): {pz == px}")
    stated_nn = F(17179558853813045157374427641784866348978652410041, 47238316419587431650245082317077879359070521)
    stated_diag = F(17179504273441154976879226752962922871304575139833, 46811863452737032502816928474601790785699833)
    ok = (res["nearest neighbour"] == stated_nn and res["body diagonal"] == stated_diag and stated_nn > 1 and stated_diag > 1
          and stated_nn != stated_diag and pz == px)
    if ok:
        print(f"HIT: confirmed - on the L = 2 six-axis torus at e^beta = 3, pi proportional to prod Z(S_x) gives like/unlike two-site cylinder ratios "
              f"{float(stated_nn):.1f} (nearest neighbour) and {float(stated_diag):.1f} (body diagonal), exactly the stated rationals, both > 1 "
              f"and unequal (face diagonal {float(res['face diagonal']):.1f}); the pairing identity holds and the one-site marginal is uniform; "
              "recomputed by independent big-integer cylinder sums")
        print("SUMMARY: confirmed - the finite L = 2 partial survives; scope: these are equal-time two-site marginals of pi (a snapshot, not "
              "sources pinned at every level), on a torus too small for any 1/r statement, as the attempt says")
    else:
        print(f"SUMMARY: fails at step 3 - the cylinder ratios differ: nn {res['nearest neighbour']} vs {stated_nn}; diag {res['body diagonal']} "
              f"vs {stated_diag}; uniform {pz == px}")


if __name__ == "__main__":
    main()

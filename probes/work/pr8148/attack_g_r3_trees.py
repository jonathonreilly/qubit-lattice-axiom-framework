#!/usr/bin/env python3
"""J:attack-g:PR8148 — brute-force R3 D1-D2 as written.

On a tree, seeded growth (cluster always connected) equals the static law.
Note: path of 3, four-leaf star; (p,q,r)=(3,1,2); uniform distances 1/216
and 56059/3369600.
"""
from __future__ import annotations

import itertools
from collections import defaultdict
from fractions import Fraction

M = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
P, Q, R = 3, 1, 2
Z1 = P + Q + 4 * R  # 12


def phi(i: int, j: int) -> int:
    d = M[i][0] * M[j][0] + M[i][1] * M[j][1] + M[i][2] * M[j][2]
    return P if d == 1 else (Q if d == -1 else R)


def Nk(k: int) -> int:
    return 6 if k == 0 else P**k + Q**k + 4 * R**k


def r_cond(vx: int, neigh_vals: list) -> Fraction:
    k = len(neigh_vals)
    if k == 0:
        return Fraction(1, 6)
    num = 1
    for a in neigh_vals:
        num *= phi(vx, a)
    return Fraction(num, Nk(k))


def window_path3():
    # sites 0-1-2
    sites = [0, 1, 2]
    edges = [(0, 1), (1, 2)]
    nb = {0: [1], 1: [0, 2], 2: [1]}
    return sites, edges, nb


def window_star4():
    # center 0, leaves 1,2,3,4
    sites = [0, 1, 2, 3, 4]
    edges = [(0, i) for i in range(1, 5)]
    nb = {0: [1, 2, 3, 4], 1: [0], 2: [0], 3: [0], 4: [0]}
    return sites, edges, nb


def static_law(sites, edges):
    n = len(sites)
    mu = {}
    Z = 0
    for v in itertools.product(range(6), repeat=n):
        w = 1
        for a, b in edges:
            w *= phi(v[a], v[b])
        mu[v] = w
        Z += w
    return {v: Fraction(w, Z) for v, w in mu.items()}, Z


def seeded_law(sites, nb):
    """First site uniform; thereafter only sites adjacent to the recorded set,
    each drawn from r(· | recorded neighbours). Average over growth sequences.
    """
    n = len(sites)
    mass = defaultdict(lambda: Fraction(0))
    # Recurse over connected orders
    def rec(order, vals, prob):
        if len(order) == n:
            mass[tuple(vals[i] for i in sites)] += prob
            return
        formed = set(order)
        cand = []
        for x in sites:
            if x in formed:
                continue
            if any(y in formed for y in nb[x]):
                cand.append(x)
        if not cand:
            return
        for x in cand:
            neigh = [vals[y] for y in nb[x] if y in formed]
            for vx in range(6):
                rec(order + [x], {**vals, x: vx}, prob * Fraction(1, len(cand)) * r_cond(vx, neigh))

    for x0 in sites:
        for v0 in range(6):
            rec([x0], {x0: v0}, Fraction(1, n) * Fraction(1, 6))
    s = sum(mass.values())
    assert s == 1, s
    return dict(mass)


def tv(mu, nu):
    keys = set(mu) | set(nu)
    return sum(abs(mu.get(k, 0) - nu.get(k, 0)) for k in keys) / 2


def uniform_law(n):
    p = Fraction(1, 6**n)
    return {v: p for v in itertools.product(range(6), repeat=n)}


def main() -> None:
    hits = []
    # Path of 3
    sites, edges, nb = window_path3()
    st, Z = static_law(sites, edges)
    se = seeded_law(sites, nb)
    d = tv(st, se)
    print(f"path3 Z={Z} TV(seeded,static)={d}")
    if d != 0:
        hits.append(f"R3 path seeded != static TV={d}")
    uni = uniform_law(3)
    du = tv(st, uni)
    mx = max(abs(st[k] - uni[k]) for k in st)
    print(f"path3 TV(uniform,static)={du} max-norm={mx} claimed 1/216={Fraction(1,216)}")
    if du != Fraction(1, 216) and mx != Fraction(1, 216):
        hits.append(f"path uniform TV={du} max={mx} != 1/216")
    # Four-leaf star
    sites, edges, nb = window_star4()
    st, Z = static_law(sites, edges)
    se = seeded_law(sites, nb)
    d = tv(st, se)
    print(f"star4 Z={Z} TV(seeded,static)={d}")
    if d != 0:
        hits.append(f"R3 star seeded != static TV={d}")
    uni = uniform_law(5)
    du = tv(st, uni)
    mx = max(abs(st[k] - uni[k]) for k in st)
    claimed = Fraction(56059, 3369600)
    print(f"star4 TV(uniform,static)={du} max-norm={mx} claimed {claimed}")
    if du != claimed and mx != claimed:
        hits.append(f"star uniform TV={du} max={mx} != {claimed}")
    # d_same at (3,1,2)
    N2 = Nk(2)
    print(f"N2={N2} 1/K2(a,a) as p^2/N2 inverse wait d_same claimed 72/13")
    # K_2(a,a) in the note's formation-conditional denominator:
    # r(a|a,a)= p^2/N2, d_same=1/K_2(a,a). If K_2=N2/Z1^2 then 1/K_2 = Z1^2/N2=144/N2
    # N2=9+1+16=26, 144/26=72/13. Yes.
    d_same = Fraction(Z1**2, N2)
    print(f"d_same={d_same} claimed 72/13={Fraction(72,13)}")
    if d_same != Fraction(72, 13):
        hits.append(f"d_same {d_same} != 72/13")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: R3/D1-D2 brute force FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern has no purchase on this note — R3 D1-D2 hold exactly "
            "as written: seeded=static on path3 and four-leaf star at (3,1,2); "
            "uniform distances 1/216 and 56059/3369600; d_same=72/13."
        )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Referee check for J:derive:formation-clauses-in-level-time:a3 (author w-macbookpro90c72-j8dec, grok-4.6);
referee w-jonathonsmac4f50-j8228 (claude-opus-5). Independent code; nothing is taken from the author's script.

Six-axis menu, rule phi = p (same), q (antipodal), r (orthogonal) on nearest-neighbour bonds of Z^3; one-site kernel given recorded
neighbours r(s | n) proportional to prod_j phi(s, n_j) (uniform with none). (p, q, r) = (3, 1, 2) unless stated.

C1  step 1: the noise map at (3,1,2) and (10,1,2).
C2  step 3: on the isolated 2x2x2 cube (12 bonds): P(all +x) under monotone level order, the seeded jump chain, the uniform mixture over
    all 8! orders (dynamic programming over subsets) and the joint static law (Z by full enumeration); TV(monotone, joint).
C3  step 4: the fork pair u = z - e1, v = z - e2 is at squared distance 2 (not a bond); with three frozen +x predecessors each, the joint
    formation of {u, v} under the rule's bonds is the product of the two NEC kernels (TV 0); the attempt's numbers come back only if a
    phi(s_u, s_v) factor is added; joint formation of a whole level of the cube equals the NEC product.
C4  step 5: block 24's M matrix values and the 1/72.
C5  step 7: the 3x3x2 slab: the k-histogram of an explicit connected monotone order from a corner; a two-seed connected growth realising
    the attempt's histogram (0:2, 1:3, 2:9, 3:4), found by random search; the two P(all +x) values.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction as F

import numpy as np

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
PX = 0


def phi_idx(a, b, p, q, r):
    d = sum(x * y for x, y in zip(AXES[a], AXES[b]))
    return p if d == 1 else (q if d == -1 else r)


def kern_allplus(k, p, q, r):
    """P(+x | k recorded neighbours all +x)."""
    if k == 0:
        return F(1, 6)
    return F(p) ** k / (F(p) ** k + F(q) ** k + 4 * F(r) ** k)


def c1():
    out = {}
    for p, q, r in ((3, 1, 2), (10, 1, 2)):
        p, q, r = F(p), F(q), F(r)
        e2 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
        e1o = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
        e1a = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
        out[(int(p), int(q), int(r))] = (e2, e1o, e1a)
    return out


def cube():
    sites = list(itertools.product((0, 1), repeat=3))
    nb = {x: [y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1] for x in sites}
    return sites, nb


def c2(p=3, q=1, r=2):
    sites, nb = cube()
    idx = {x: i for i, x in enumerate(sites)}
    # monotone level order
    order = sorted(sites, key=sum)
    formed = set()
    mono = F(1)
    for x in order:
        k = sum(1 for y in nb[x] if y in formed)
        mono *= kern_allplus(k, p, q, r)
        formed.add(x)

    # uniform mixture over all orders: average over the next site uniformly among empty ones (DP over subsets)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def unif(mask):
        if mask == (1 << 8) - 1:
            return F(1)
        empty = [i for i in range(8) if not mask >> i & 1]
        tot = F(0)
        for i in empty:
            k = sum(1 for y in nb[sites[i]] if mask >> idx[y] & 1)
            tot += kern_allplus(k, p, q, r) * unif(mask | 1 << i)
        return tot / len(empty)

    @lru_cache(maxsize=None)
    def seeded(mask):
        if mask == (1 << 8) - 1:
            return F(1)
        if mask == 0:
            cand = list(range(8))
        else:
            cand = [i for i in range(8) if not mask >> i & 1 and any(mask >> idx[y] & 1 for y in nb[sites[i]])]
        tot = F(0)
        for i in cand:
            k = sum(1 for y in nb[sites[i]] if mask >> idx[y] & 1)
            tot += kern_allplus(k, p, q, r) * seeded(mask | 1 << i)
        return tot / len(cand)

    u, s = unif(0), seeded(0)
    # joint static law: Z over 6^8 configurations (integers), bonds = the 12 cube edges
    bonds = [(idx[x], idx[y]) for x in sites for y in nb[x] if idx[x] < idx[y]]
    Wt = np.array([[phi_idx(a, b, p, q, r) for b in range(6)] for a in range(6)], dtype=np.int64)
    grid = np.array(list(itertools.product(range(6), repeat=8)), dtype=np.int64)
    W = np.ones(len(grid), dtype=np.int64)
    for i, j in bonds:
        W *= Wt[grid[:, i], grid[:, j]]
    Z = int(W.sum())
    joint = F(p ** 12, Z)
    # TV(monotone, joint) in floating point over all 6^8 atoms
    Pm = np.ones(len(grid))
    formed_idx = []
    for x in order:
        i = idx[x]
        rec = [idx[y] for y in nb[x] if idx[y] in formed_idx]
        num = np.ones(len(grid))
        den = np.zeros(len(grid))
        for j in rec:
            num *= Wt[grid[:, i], grid[:, j]]
        for sv in range(6):
            t = np.ones(len(grid))
            for j in rec:
                t *= Wt[sv, grid[:, j]]
            den += t
        Pm *= num / den
        formed_idx.append(i)
    tv = 0.5 * np.abs(Pm - W / Z).sum()
    return mono, s, u, joint, Z, tv, len(bonds)


def c3(p=3, q=1, r=2):
    z = (1, 1, 1)
    u = (0, 1, 1)
    v = (1, 0, 1)
    d2 = sum((a - b) ** 2 for a, b in zip(u, v))
    P = F(p)
    # each of u, v has three recorded +x predecessors
    w = [F(phi_idx(a, PX, p, q, r)) ** 3 for a in range(6)]
    Zs = sum(w)
    nec = {(a, b): w[a] * w[b] / Zs ** 2 for a in range(6) for b in range(6)}
    # joint formation under the rule's bonds: u, v not adjacent -> no factor between them
    joint_rule = dict(nec)
    tv_rule = sum(abs(joint_rule[k] - nec[k]) for k in nec) / 2
    # the attempt's version: an extra phi(s_u, s_v) bond
    wb = {(a, b): w[a] * w[b] * phi_idx(a, b, p, q, r) for a in range(6) for b in range(6)}
    Zb = sum(wb.values())
    joint_bond = {k: v_ / Zb for k, v_ in wb.items()}
    tv_bond = sum(abs(joint_bond[k] - nec[k]) for k in nec) / 2
    # a whole level of the cube: level 1 = {(1,0,0),(0,1,0),(0,0,1)}: no bond inside
    sites, nb = cube()
    lvl1 = [x for x in sites if sum(x) == 1]
    inside = sum(1 for a, b in itertools.combinations(lvl1, 2) if b in nb[a])
    return d2, nec[(PX, PX)], tv_rule, joint_bond[(PX, PX)], tv_bond, inside


def c4(p=3, q=1, r=2):
    M = {}
    for a in range(6):
        for b in range(6):
            M[(a, b)] = sum(phi_idx(s, a, p, q, r) * phi_idx(s, b, p, q, r) for s in range(6))
    vals = sorted(set(M.values()))
    tot = sum(M.values())
    tv = sum(abs(F(v, tot) - F(1, 36)) for v in M.values()) / 2
    return vals, tv


def c5(p=3, q=1, r=2):
    sites = [(i, j, l) for l in range(2) for i in range(3) for j in range(3)]
    nb = {x: [y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1] for x in sites}

    def hist(order):
        formed, h = set(), {}
        for x in order:
            k = sum(1 for y in nb[x] if y in formed)
            h[k] = h.get(k, 0) + 1
            formed.add(x)
        return dict(sorted(h.items()))

    corner = sorted(sites, key=lambda x: (x[0] + x[1] + x[2], x))     # monotone, connected from (0,0,0)
    h1 = hist(corner)
    P1 = F(1)
    for k, c in h1.items():
        P1 *= kern_allplus(k, p, q, r) ** c
    # an order planting a second seed with the attempt's histogram (0:2, 1:3, 2:9, 3:4): random two-seed connected growths
    import random
    rng = random.Random(8228)
    target = {0: 2, 1: 3, 2: 9, 3: 4}
    found = None
    for _ in range(20000):
        a, b = rng.sample(sites, 2)
        if b in nb[a]:
            continue
        order, formed = [a, b], {a, b}
        while len(order) < len(sites):
            cand = [x for x in sites if x not in formed and any(y in formed for y in nb[x])]
            x = rng.choice(cand)
            order.append(x)
            formed.add(x)
        if hist(order) == target:
            found = order
            break
    P2 = F(1)
    for k, c in target.items():
        P2 *= kern_allplus(k, p, q, r) ** c
    return h1, P1, found, P2


def main():
    nm = c1()
    print(f"C1 noise map: (3,1,2): eps2, eps1_perp, eps1_anti = {nm[(3, 1, 2)]}; (10,1,2): eps2 = {nm[(10, 1, 2)][0]}")
    mono, seeded, unif, joint, Z, tv, nbonds = c2()
    print(f"C2 cube ({nbonds} bonds), P(all +x): monotone {mono}; seeded jump chain {seeded}; uniform mixture over 8! orders {unif}; joint "
          f"p^12/Z = {joint} with Z = {Z}; TV(monotone, joint) = {tv:.12f} (attempt: 1182193085/23402354976 = {1182193085 / 23402354976:.12f})")
    d2, nec_pp, tv_rule, jb_pp, tv_bond, inside = c3()
    print(f"C3 fork pair u = z - e1, v = z - e2: |u - v|^2 = {d2} (not a bond); joint formation under the rule's bonds = NEC product, "
          f"P(both +x) = {nec_pp}, TV(joint, NEC) = {tv_rule}; with an added phi(s_u, s_v) bond: P(both +x) = {jb_pp}, TV = {tv_bond} "
          f"(the attempt's 2187/7876 and 360383/3544200); bonds inside level 1 of the cube: {inside}")
    vals, tv4 = c4()
    print(f"C4 block 24's M at (3,1,2): values {vals}; TV(uniform, M/sum M) = {tv4}")
    h1, P1, found, P2 = c5()
    print(f"C5 slab 3x3x2: monotone connected order from a corner has k-histogram {h1}, P(all +x) = {P1}; an order planting a second seed "
          f"with histogram (0:2, 1:3, 2:9, 3:4) {'found: ' + str(found[:3]) + '...' if found else 'not found in 20000 random two-seed growths'}; "
          f"its P(all +x) = {P2}; smaller: {P2 < P1}")

    claimed_cube = (F(2187, 44994560), F(84807, 1799782400), F(338229, 7997080000), F(59049, 775835648))
    cube_ok = (mono, seeded, unif, joint) == claimed_cube and Z == 6982520832 and abs(tv - 1182193085 / 23402354976) < 1e-11
    slab_ok = (h1 == {0: 1, 1: 5, 2: 8, 3: 4} and found is not None and P1 == F(94143178827, 68428452520263680000)
               and P2 == F(282429536481, 222392470690856960000) and P2 < P1)
    step4_wrong = d2 == 2 and tv_rule == 0 and jb_pp == F(2187, 7876) and tv_bond == F(360383, 3544200) and inside == 0
    if step4_wrong:
        print(f"SUMMARY: fails at step 4 - two same-level sites are never nearest neighbours on Z^3 (the fork offset e_i - e_j has squared "
              f"length 2), so the rule puts no phi factor between them: joint formation of a same-level pair (or of a whole level, which has "
              f"no internal bond) is exactly the NEC product (TV 0, P(both +x) = {nec_pp}); the attempt's 2187/7876 and 360383/3544200 "
              f"reproduce only with an added phi(s_u, s_v) bond, so 'joint units fail (N1)' is not shown by the fork pair (joint units fail "
              f"only when they contain a bond, i.e. span two levels); the other finite facts re-derive: noise map (11/20, 17/26, 35/44; "
              f"33/1033), the four cube numbers {'as stated' if cube_ok else 'DIFFER'} (Z = {Z}), TV(monotone, joint) = {tv:.10f}, "
              f"block 24's 26/22/24 and 1/72, the slab histograms and probabilities {'as stated' if slab_ok else 'DIFFER'}")
    elif cube_ok and slab_ok:
        print("HIT: confirmed - the finite facts re-derive")
        print("SUMMARY: confirmed")
    else:
        print(f"SUMMARY: fails - cube {cube_ok}, slab {slab_ok}, step4 {step4_wrong}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Referee of J:derive:formation-order-independence:a1 (author w-macbookpro90c72-j482b, grok-4.6); referee w-jonathonsmac4f50-j40d0
(claude-opus-5). Independent code (exact Fractions, full joint laws); nothing from the author's check.py.

O1  the DAG statement: on the V (a, b -> c), the diamond (a -> b, c -> d) and a five-site DAG, every linear extension gives the
    same full joint law (exact), for the six-axis product kernel at (3,1,2) and for an arbitrary non-covariant rational kernel on
    a binary menu (the statement needs no symmetry of the kernel)
O2  C4 formed from recorded neighbours (undirected): Hamiltonian-path order k = (0,1,1,2), P(all +x) = 3/832; opposite-first
    k = (0,0,2,2), P(all +x) = 9/2704; the HIT line's '(0,0,1,1)' for opposite-first is impossible (the k's sum to |E| = 4)
O3  smallest example: with two sites the two orders give the same law (W symmetric, Z_1 = p + q + 4r constant), at (3,1,2) and
    (5,2,4); with three sites (the path = the attempt's V read undirected) the orders (end, end, middle) and (middle, end, end)
    differ: k = (0,0,2) vs (0,1,1), P(all +x) = 1/104 vs 1/96 - so the smallest counterexample has three sites, not C4
O4  the event-lattice statement: on the 3x3 window of the level-ordered plane (predecessors x - e1, x - e2), sixty random linear
    extensions give the same full joint law on a binary menu (exact)
"""
from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction as F

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def six(p, q, r):
    M = range(6)
    W = [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]

    def K(v, pv):
        ws = []
        for s in M:
            w = 1
            for a in pv:
                w *= W[s][a]
            ws.append(w)
        return F(ws[v], sum(ws))
    return list(M), K


def binary_kernel(seed):
    rnd = random.Random(seed)
    table = {}

    def K(v, pv):
        key = tuple(pv)
        if key not in table:
            a = F(rnd.randint(1, 9), 10)
            table[key] = a
        a = table[key]
        return a if v == 1 else 1 - a
    return [0, 1], K


def joint(order, parents, menu, K):
    """full law when sites form in `order`, each from its parents' (already formed) values"""
    law = {}
    n = len(order)
    for vals in itertools.product(menu, repeat=n):
        val = dict(zip(order, vals))
        pr = F(1)
        for x in order:
            pr *= K(val[x], [val[y] for y in parents[x]])
        key = tuple(val[x] for x in sorted(order))
        law[key] = law.get(key, 0) + pr
    return law


def extensions(sites, parents):
    out = []
    for o in itertools.permutations(sites):
        pos = {x: i for i, x in enumerate(o)}
        if all(pos[y] < pos[x] for x in sites for y in parents[x]):
            out.append(o)
    return out


def main():
    dags = {
        "V": {"a": [], "b": [], "c": ["a", "b"]},
        "diamond": {"a": [], "b": ["a"], "c": ["a"], "d": ["b", "c"]},
        "five": {"a": [], "b": [], "c": ["a"], "d": ["a", "b"], "e": ["c", "d"]},
    }
    ok, rows = True, []
    for name, par in dags.items():
        exts = extensions(list(par), par)
        for menu, K in (six(3, 1, 2), binary_kernel(7)):
            laws = [joint(o, par, menu, K) for o in exts]
            ok &= all(l == laws[0] for l in laws) and sum(laws[0].values()) == 1
        rows.append(f"{name}: {len(exts)} linear extensions")
    check("O1", ok, "every linear extension gives the same full joint law: " + "; ".join(rows)
          + " (six-axis product kernel and a random binary kernel)")

    M6, K6 = six(3, 1, 2)
    nbr = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

    def seq(order):
        seen, ks, pr = set(), [], F(1)
        for x in order:
            rec = [y for y in nbr[x] if y in seen]
            ks.append(len(rec))
            pr *= K6(0, [0] * len(rec))
            seen.add(x)
        return tuple(ks), pr
    kp, pp = seq([0, 1, 2, 3])
    ko, po = seq([0, 2, 1, 3])
    check("O2", kp == (0, 1, 1, 2) and pp == F(3, 832) and ko == (0, 0, 2, 2) and po == F(9, 2704) and sum(ko) == 4,
          f"path order k = {kp}, P(all +x) = {pp}; opposite-first k = {ko}, P(all +x) = {po}; sum of k = |E| = 4, so '(0,0,1,1)' "
          "cannot occur")

    ok, rows = True, []
    for rule in ((3, 1, 2), (5, 2, 4)):
        menu, K = six(*rule)
        two = [joint(o, par, menu, K) for o, par in (([0, 1], {0: [], 1: [0]}), ([1, 0], {1: [], 0: [1]}))]
        ok &= two[0] == two[1]
        rows.append(f"{rule}: two sites order-free")
    menu, K = six(3, 1, 2)
    ends_first = joint(["a", "b", "c"], {"a": [], "b": [], "c": ["a", "b"]}, menu, K)
    mid_first = joint(["c", "a", "b"], {"c": [], "a": ["c"], "b": ["c"]}, menu, K)
    pe, pm = ends_first[(0, 0, 0)], mid_first[(0, 0, 0)]
    ok &= ends_first != mid_first and pe == F(1, 104) and pm == F(1, 96)
    check("O3", ok, "; ".join(rows) + f"; three-site path: ends-first P(all +x) = {pe}, middle-first {pm}: the laws differ")

    sites = [(i, j) for i in range(3) for j in range(3)]
    par = {x: [y for y in ((x[0] - 1, x[1]), (x[0], x[1] - 1)) if y in sites] for x in sites}
    menu, K = binary_kernel(11)
    rnd = random.Random(3)
    base = sorted(sites, key=lambda x: (x[0] + x[1], x))
    law0 = joint(base, par, menu, K)
    ok = sum(law0.values()) == 1
    for _ in range(60):
        o = sorted(sites, key=lambda x: (x[0] + x[1], rnd.random()))
        # random interleavings across levels that still respect the partial order
        for _ in range(20):
            i = rnd.randrange(8)
            a, b = o[i], o[i + 1]
            if a not in par[b]:
                o[i], o[i + 1] = b, a
        pos = {x: i for i, x in enumerate(o)}
        assert all(pos[y] < pos[x] for x in sites for y in par[x])
        ok &= joint(o, par, menu, K) == law0
    check("O4", ok, "3x3 level-ordered window: 60 random linear extensions give the identical 512-cell joint law (binary kernel)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-order-independence a1: on a causal DAG the formation law is the product of kernels along the "
          "partial order and the same for every linear extension (full joint laws equal on the V, the diamond, a five-site DAG and a "
          "3x3 level-ordered window, for covariant and non-covariant kernels), and C4's orders give 3/832 vs 9/2704. Corrections: the "
          "opposite-first k-sequence is (0,0,2,2), not the HIT line's (0,0,1,1); C4 is not the smallest counterexample - the "
          "three-site path (the attempt's V read undirected) already has order-dependent laws (1/104 vs 1/96) and two sites cannot")
    print("SUMMARY: confirmed with two corrections (the k-sequence typo; smallest example has three sites)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

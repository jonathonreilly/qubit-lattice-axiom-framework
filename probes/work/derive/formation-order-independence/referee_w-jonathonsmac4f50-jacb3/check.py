#!/usr/bin/env python3
"""Referee of J:derive:formation-order-independence:a4 (author w-macbookpro90c72-jaf09, grok-4.6); referee w-jonathonsmac4f50-jacb3
(claude-opus-5). Independent code (exact Fractions over full joint laws); nothing from the author's check.py. Disclosure: this referee's
model family refereed attempt a1 of this problem (grok; referee_w-jonathonsmac4f50-j40d0), where the three-site example was found.

P1  step 1: on the V, the diamond and a five-site DAG, every linear extension gives the same full joint law (six-axis product kernel at
    (3,1,2) and a random non-covariant binary kernel)
P2  step 4: the 2-site edge is order-free for the symmetric six-axis rule (TV = 0; P(equal) = 1/4); the V formed child-first differs from
    the causal V: TV = 1/72 exactly, P(all +x) = 1/104 (causal) vs 1/96 (child-first)
P3  step 5's reading: on a level-ordered 3x3 window (predecessors x - e1, x - e2), sixty random linear extensions give the same law
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


def binary(seed):
    rnd = random.Random(seed)
    table = {}

    def K(v, pv):
        key = tuple(pv)
        if key not in table:
            table[key] = F(rnd.randint(1, 9), 10)
        return table[key] if v == 1 else 1 - table[key]
    return [0, 1], K


def joint(order, parents, menu, K):
    law = {}
    for vals in itertools.product(menu, repeat=len(order)):
        val = dict(zip(order, vals))
        pr = F(1)
        for x in order:
            pr *= K(val[x], [val[y] for y in parents[x]])
        key = tuple(val[x] for x in sorted(order))
        law[key] = law.get(key, 0) + pr
    return law


def extensions(parents):
    sites = list(parents)
    out = []
    for o in itertools.permutations(sites):
        pos = {x: i for i, x in enumerate(o)}
        if all(pos[y] < pos[x] for x in sites for y in parents[x]):
            out.append(o)
    return out


def main():
    dags = {"V": {"a": [], "b": [], "c": ["a", "b"]}, "diamond": {"a": [], "b": ["a"], "c": ["a"], "d": ["b", "c"]},
            "five": {"a": [], "b": [], "c": ["a"], "d": ["a", "b"], "e": ["c", "d"]}}
    ok, rows = True, []
    for name, par in dags.items():
        ex = extensions(par)
        for menu, K in (six(3, 1, 2), binary(5)):
            laws = [joint(o, par, menu, K) for o in ex]
            ok &= all(l == laws[0] for l in laws) and sum(laws[0].values()) == 1
        rows.append(f"{name}: {len(ex)} extensions")
    check("P1", ok, "; ".join(rows) + " - identical full joint laws")

    menu, K = six(3, 1, 2)
    e1 = joint([0, 1], {0: [], 1: [0]}, menu, K)
    e2 = joint([1, 0], {1: [], 0: [1]}, menu, K)
    tv2 = sum(abs(e1[k] - e2[k]) for k in e1) / 2
    peq = sum(v for k, v in e1.items() if k[0] == k[1])
    causal = joint(["a", "b", "c"], {"a": [], "b": [], "c": ["a", "b"]}, menu, K)
    child = joint(["c", "a", "b"], {"c": [], "a": ["c"], "b": ["c"]}, menu, K)
    tv3 = sum(abs(causal[k] - child[k]) for k in causal) / 2
    ok = tv2 == 0 and peq == F(1, 4) and tv3 == F(1, 72) and causal[(0, 0, 0)] == F(1, 104) and child[(0, 0, 0)] == F(1, 96)
    check("P2", ok, f"2-site edge: TV = {tv2}, P(equal) = {peq}; V causal vs child-first: TV = {tv3}, P(all +x) {causal[(0, 0, 0)]} vs "
          f"{child[(0, 0, 0)]}")

    sites = [(i, j) for i in range(3) for j in range(3)]
    par = {x: [y for y in ((x[0] - 1, x[1]), (x[0], x[1] - 1)) if y in sites] for x in sites}
    menu, K = binary(9)
    rnd = random.Random(4)
    law0 = joint(sorted(sites, key=lambda x: (x[0] + x[1], x)), par, menu, K)
    ok = sum(law0.values()) == 1
    for _ in range(60):
        o = sorted(sites, key=lambda x: (x[0] + x[1], rnd.random()))
        for _ in range(20):
            i = rnd.randrange(8)
            if o[i] not in par[o[i + 1]]:
                o[i], o[i + 1] = o[i + 1], o[i]
        ok &= joint(o, par, menu, K) == law0
    check("P3", ok, "3x3 level-ordered window: 60 random linear extensions give the identical 512-cell law")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-order-independence a4: on a finite predecessor DAG every linear extension gives the same joint law "
          "prod_v r(s_v | s_parents) (full laws on the V, the diamond, a five-site DAG and a 3x3 level window, covariant and non-covariant "
          "kernels); the 2-site edge is order-free for the symmetric rule (TV 0, P(equal) = 1/4) and the smallest violation is the 3-site V "
          "formed child-first, TV = 1/72 at (3,1,2) (P(all +x) 1/104 vs 1/96); recomputed independently")
    print("SUMMARY: confirmed - no failing step; the smallest example and the event-lattice reading are stated correctly")
    return 0


if __name__ == "__main__":
    sys.exit(main())

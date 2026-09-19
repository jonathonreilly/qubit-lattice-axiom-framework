#!/usr/bin/env python3
"""J:attack-e:PR8176 — SAMPLED EVIDENCE.

The note's conjecture that c*=1 (executed hill-climbs on ~10^4 realizations
never exceed 1) is sampled. Adversarial construction: T1.3 DP of
min (E-3(|S|-1)-|A|) over single-seed marked trees on a 3x3x6 window,
greedy one-site flips, seeking a realization with min > 0 (i.e. c*>1).
Not the T4 4/729 floor.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORKS = tuple(
    tuple(E[i][a] - E[j][a] for a in range(3))
    for i in range(3)
    for j in range(3)
    if i != j
)
HITS = []
A = B = 3
L = 6
BOX = set(product(range(A), range(B), range(L)))
ROOT = (2, 2, 5)


def add(u, v):
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return tuple(sub(z, e) for e in E)


def classify(ones):
    seed, amp, proc = set(), set(), set()
    npred = {}
    for z in ones:
        n = sum(p in ones for p in preds(z))
        npred[z] = n
        if n == 0:
            seed.add(z)
        elif n == 1:
            amp.add(z)
        else:
            proc.add(z)
    return seed, amp, proc, npred


def component(ones, root):
    if root not in ones:
        return set()
    parent = {z: z for z in ones}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for z in ones:
        for p in preds(z):
            if p in ones:
                union(z, p)
        for d in FORKS:
            w = add(z, d)
            if w in ones:
                union(z, w)
    r = find(root)
    return {z for z in ones if find(z) == r}


def min_cost(ones, root):
    """min_N Σ cost at c=1 on a single-seed component, or None if not applicable."""
    seed, amp, proc, npred = classify(ones)
    comp = component(ones, root)
    if root not in comp:
        return None
    seeds = seed & comp
    if len(seeds) != 1:
        return None
    s = next(iter(seeds))
    if level(s) >= level(root):
        return None
    by_lv = defaultdict(list)
    for z in comp:
        by_lv[level(z)].append(z)
    levels = list(range(level(root), level(s) - 1, -1))
    # DP[lv][frozenset of chosen sites at lv] = min cost from lv down
    sites_at = {lv: tuple(by_lv[lv]) for lv in levels}
    if any(len(v) > 12 for v in sites_at.values()):
        return None

    def ok_trans(chosen, below):
        below = set(below)
        for z in chosen:
            if z in seed:
                continue
            if not any(p in below for p in preds(z) if p in comp):
                return False
            if z in amp:
                only = [p for p in preds(z) if p in ones]
                if len(only) != 1 or only[0] not in below:
                    return False
        return True

    def cost_set(chosen):
        c = 0
        for z in chosen:
            if z in proc:
                c += 1
            elif z in amp:
                c -= 1
        return c

    # iterate levels root -> seed
    states = {frozenset([root]): cost_set([root])}
    for i, lv in enumerate(levels[:-1]):
        nxt_lv = levels[i + 1]
        cand = sites_at[nxt_lv]
        new = {}
        for ch, csofar in states.items():
            n = len(cand)
            for mask in range(1 << n):
                below = frozenset(cand[j] for j in range(n) if mask >> j & 1)
                if lv == levels[-2]:
                    # next is seed level: must be {s} or include s
                    if s not in below:
                        continue
                if not ok_trans(ch, below):
                    continue
                tot = csofar + cost_set(below)
                if below not in new or tot < new[below]:
                    new[below] = tot
        states = new
        if not states:
            return None
    # last level must be {s} (seed cost 0)
    best = None
    for ch, tot in states.items():
        if s in ch:
            if best is None or tot < best:
                best = tot
    return best


def greedy():
    # single-seed chain from (0,0,0) to ROOT, then greedy add/remove
    chain = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
        (2, 2, 5),
    ]
    ones = set(chain)
    seed, amp, proc, _ = classify(ones)
    print(
        f"chain |ones|={len(ones)} seeds={len(seed)} A={len(amp)} P={len(proc)} "
        f"comp={len(component(ones, ROOT))} min_cost={min_cost(ones, ROOT)}"
    )
    best_ones = set(ones)
    best = min_cost(ones, ROOT)
    improved = True
    rounds = 0
    while improved and rounds < 40:
        improved = False
        rounds += 1
        order = sorted(BOX, key=level)
        for z in order:
            if z == ROOT:
                continue
            trial = set(best_ones)
            if z in trial:
                trial.remove(z)
            else:
                trial.add(z)
            if ROOT not in trial:
                continue
            mc = min_cost(trial, ROOT)
            if mc is None:
                continue
            if best is None or mc > best:
                best, best_ones = mc, trial
                improved = True
                print(f"  round {rounds} |ones|={len(trial)} min_cost={mc}")
    # pairwise adds from the original chain (shrinking discards processed candidates)
    sites = [z for z in sorted(BOX, key=level) if z not in chain]
    for i, u in enumerate(sites):
        for v in sites[i + 1 :]:
            trial = set(chain) | {u, v}
            mc = min_cost(trial, ROOT)
            if mc is None:
                continue
            if best is None or mc > best:
                best, best_ones = mc, trial
                print(f"  pair add {u},{v} |ones|={len(trial)} min_cost={mc}")
    return best, best_ones


def main():
    best, ones = greedy()
    print(f"adversarial best min_cost(c=1)={best} |ones|={len(ones)}")
    if best is not None and best > 0:
        seed, amp, proc, _ = classify(ones)
        comp = component(ones, ROOT)
        HITS.append(
            f"c*>1: min(E-|A|)={best} on |comp|={len(comp)} seeds={len(seed&comp)} "
            f"A={len(amp&comp)} P={len(proc&comp)}"
        )
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (e) SAMPLED EVIDENCE - "
            + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - greedy adversarial "
        "flips on a 3x3x6 window never produced a single-seed component with "
        "min(E-|A|)>0, so they do not refute the sampled c*=1 conjecture"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

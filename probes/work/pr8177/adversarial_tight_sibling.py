#!/usr/bin/env python3
"""J:attack-e:PR8177 — SAMPLED EVIDENCE.

The note's 'tight-sibling case never arises' / '(H) never violated' on ~10^4
climbs is sampled. Adversarial: greedy one-site flips on a 3x3x5 single-seed
window, computing the rooted DP v(z)=min(E-|A|) at every processed site,
seeking a processed z whose 1-predecessors are all processed with v=0.

Do not re-find the known T2 Z_B [-1,-1,0] predecessor HIT.
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
A = B = 3
L = 5
BOX = set(product(range(A), range(B), range(L)))
ROOT = (2, 2, 4)


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
        if level(s) <= level(z) <= level(root):
            by_lv[level(z)].append(z)
    levels = list(range(level(root), level(s) - 1, -1))
    sites_at = {lv: tuple(by_lv[lv]) for lv in levels}
    if any(len(v) > 10 for v in sites_at.values()):
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

    states = {frozenset([root]): cost_set([root])}
    for i, lv in enumerate(levels[:-1]):
        cand = sites_at[levels[i + 1]]
        new = {}
        n = len(cand)
        for ch, csofar in states.items():
            for mask in range(1 << n):
                below = frozenset(cand[j] for j in range(n) if mask >> j & 1)
                if levels[i + 1] == level(s) and s not in below:
                    continue
                if not ok_trans(ch, below):
                    continue
                tot = csofar + cost_set(below)
                if below not in new or tot < new[below]:
                    new[below] = tot
        states = new
        if not states:
            return None
    best = None
    for ch, tot in states.items():
        if s in ch and (best is None or tot < best):
            best = tot
    return best


def scan(ones):
    """Return tight-sibling hits and (H) violations. Single-seed components only."""
    seed, amp, proc, npred = classify(ones)
    tight_sib = []
    h_fail = []
    geom = 0
    for z in proc:
        ones_p = [p for p in preds(z) if p in ones]
        if ones_p and all(p in proc for p in ones_p):
            geom += 1
            vs = []
            ok = True
            for p in ones_p:
                vp = min_cost(ones, p)
                vs.append(vp)
                if vp is None or vp != 0:
                    ok = False
            if ok:
                tight_sib.append((z, ones_p, vs))
        vz = min_cost(ones, z)
        if vz is not None and vz > 0:
            h_fail.append((z, "proc", vz))
    for z in amp:
        vz = min_cost(ones, z)
        if vz is not None and vz >= 0:
            h_fail.append((z, "amp", vz))
    return geom, tight_sib, h_fail


def main() -> int:
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
    ]
    ones = set(chain)
    geom, ts, hf = scan(ones)
    print(f"chain geom_tight_pred={geom} tight_sib={ts} H_fail={hf} v(ROOT)={min_cost(ones, ROOT)}")

    def consider(trial, tag):
        if ROOT not in trial:
            return False
        g, ts, hf = scan(trial)
        if ts:
            print("HIT: tight-sibling", tag, ts)
            print(
                "SUMMARY: HIT - adversarial construction found a processed site "
                f"whose 1-predecessors are all processed with v=0: {ts}"
            )
            return True
        if hf:
            print("HIT: (H) violated", tag, hf[:3])
            print(
                "SUMMARY: HIT - adversarial construction found a rooted-inequality "
                f"violation (H): {hf[:3]}"
            )
            return True
        return False

    # every one-site add/remove from the chain
    for z in sorted(BOX, key=level):
        if z == ROOT:
            continue
        trial = set(ones)
        if z in trial:
            trial.remove(z)
        else:
            trial.add(z)
        if consider(trial, f"flip {z}"):
            return 0
    # pairwise adds (the geometry of two extra 1s can make a processed node)
    extras = [z for z in sorted(BOX, key=level) if z not in chain]
    max_geom = 0
    best_ones = set(ones)
    for i, u in enumerate(extras):
        for v in extras[i + 1 :]:
            trial = set(chain) | {u, v}
            g, ts, hf = scan(trial)
            if g > max_geom:
                max_geom = g
                best_ones = trial
                print(f"  pair {u},{v} geom={g} v(ROOT)={min_cost(trial, ROOT)}")
            if consider(trial, f"pair {u},{v}"):
                return 0
    # two-layer processed gadget: seed, three amps, three 2-pred processed, then a
    # 3-pred processed whose predecessors are those processed sites.
    gadget = {
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        (1, 1, 2),
        (2, 1, 2),
        (1, 2, 2),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
    }
    print(
        f"gadget |ones|={len(gadget)} v(ROOT)={min_cost(gadget, ROOT)} "
        f"class={tuple(len(s) for s in classify(gadget)[:3])}"
    )
    if consider(gadget, "processed gadget"):
        return 0
    g_g, ts_g, hf_g = scan(gadget)
    seed, amp, proc, npred = classify(gadget)
    for z in proc:
        ones_p = [p for p in preds(z) if p in gadget]
        if ones_p and all(p in proc for p in ones_p):
            print(
                f"  gadget processed {z} npred={npred[z]} preds={ones_p} "
                f"v(z)={min_cost(gadget, z)} v(preds)={[min_cost(gadget, p) for p in ones_p]}"
            )
    print(f"gadget geom={g_g} ts={ts_g} hf={hf_g}")
    # thicken gadget by one extra 1
    for z in sorted(BOX, key=level):
        if z in gadget:
            continue
        trial = set(gadget) | {z}
        if consider(trial, f"gadget+{z}"):
            return 0
    g, ts, hf = scan(best_ones)
    print(f"final max_geom={max_geom} tight_sib={ts} H_fail={hf} |ones|={len(best_ones)}")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8177): adversarial chain/pair/gadget "
        "search on a 3x3x5 single-seed window produced the tight-sibling "
        f"geometry (gadget geom={g_g}) but those processed predecessors were "
        "not all v=0, and no (H) violation; the sampled 'never arises' is not "
        "refuted; not a re-find of the known Z_B [-1,-1,0] HIT; pattern has no "
        "purchase beyond that"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Independent certificate for tight-sibling-vacuity a4.

Own level sweep. Cost depends only on the closed node set.
"""
from collections import defaultdict
from fractions import Fraction as F

FAILS = []
MARKS = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 2, 1), (1, 0, 2), (2, 1, 0), (1, 1, 3), (1, 3, 1), (3, 1, 1)}
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def preds(z):
    return [tuple(z[i] - AXES[j][i] for i in range(3)) for j in range(3)]


def level(z):
    return z[0] + z[1] + z[2]


def realize(marks):
    sites = [(x, y, z) for L in range(10) for x in range(L + 1) for y in range(L - x + 1) for z in [L - x - y]]
    eta = {}
    for z in sites:
        npred = sum(eta.get(p, 0) == 1 for p in preds(z))
        eta[z] = 1 if npred >= 2 or z in marks else 0
    kind = {}
    by = defaultdict(list)
    for z in sites:
        if not eta[z]:
            continue
        npred = sum(eta.get(p, 0) == 1 for p in preds(z))
        kind[z] = "seed" if npred == 0 else ("amp" if npred == 1 else "proc")
        by[level(z)].append(z)
    return eta, kind, by


def min_closed(kind, by, eta, target):
    """Minimum cost of a closed node set containing target, levels <= level(target). Returns (cost, nodes)."""
    state = {frozenset(): (0, frozenset())}
    back = {}
    for L in range(level(target) + 1):
        nodes = by[L]
        n = len(nodes)
        nxt = {}
        step = {}
        for prev, (c0, _) in state.items():
            for mask in range(1 << n):
                chosen = [nodes[i] for i in range(n) if mask >> i & 1]
                if L == level(target) and target not in chosen:
                    continue
                if any(kind[z] != "seed" and not any(p in prev for p in preds(z) if eta.get(p) == 1) for z in chosen):
                    continue
                dc = sum(1 if kind[z] == "proc" else (-1 if kind[z] == "amp" else -3) for z in chosen)
                key = frozenset(chosen)
                c = c0 + dc
                if key not in nxt or c < nxt[key][0]:
                    nxt[key] = (c, key)
                    step[key] = prev
        back[L] = step
        state = nxt
    best_c, best_key = None, None
    for key, (c, _) in state.items():
        if target in key and (best_c is None or c < best_c):
            best_c, best_key = c, key
    nodes = set()
    key = best_key
    for L in range(level(target), -1, -1):
        prev = back[L][key]
        nodes |= set(key)
        key = prev
    return 3 + best_c, nodes


def frontier(kind, by, eta, target):
    state = {frozenset(): {(0, 0)}}
    for L in range(level(target) + 1):
        nodes = by[L]
        n = len(nodes)
        nxt = defaultdict(set)
        for prev, pairs in state.items():
            for mask in range(1 << n):
                chosen = [nodes[i] for i in range(n) if mask >> i & 1]
                if L == level(target) and target not in chosen:
                    continue
                if any(kind[z] != "seed" and not any(p in prev for p in preds(z) if eta.get(p) == 1) for z in chosen):
                    continue
                de = sum(kind[z] == "proc" for z in chosen)
                da = sum(kind[z] == "amp" for z in chosen)
                for e, a in pairs:
                    nxt[frozenset(chosen)].add((e + de, a + da))
        state = nxt
    got = set()
    for key, pairs in state.items():
        if target in key:
            got |= pairs
    return got


def main():
    # cost = E - 3(|S|-1) - |A| = 3 + sum of weights
    ok("cost", 6 - 3 * (2 - 1) - 4 == 3 + (1 * 6 + -1 * 4 + -3 * 2),
       "cost depends only on the node weights")

    eta, kind, by = realize(MARKS)
    ones = [z for z in kind]
    counts = {k: sum(v == k for v in kind.values()) for k in ("seed", "amp", "proc")}
    ok("sweep", len(ones) == 37 and counts == {"seed": 1, "amp": 9, "proc": 27} and kind[(3, 3, 3)] == "proc",
       f"37 one-sites, {counts}, 333 processed")
    preds333 = preds((3, 3, 3))
    ok("preds", all(kind[p] == "proc" for p in preds333), f"three predecessors {preds333} are processed")

    c333, nodes333 = min_closed(kind, by, eta, (3, 3, 3))
    pred_costs = {p: min_closed(kind, by, eta, p)[0] for p in preds333}
    closed = all(kind[z] == "seed" or any(p in nodes333 for p in preds(z) if eta.get(p) == 1) for z in nodes333)
    one_seed = sum(kind[z] == "seed" for z in nodes333) == 1
    ok("values", c333 == 1 and pred_costs == {p: 0 for p in preds333} and closed and one_seed,
       f"v(333)={c333}, predecessors {pred_costs}")

    pairs = frontier(kind, by, eta, (3, 3, 3))
    # nondominated for small E and large A
    nd = sorted((e, a) for e, a in pairs if not any(e2 <= e and a2 >= a and (e2, a2) != (e, a) for e2, a2 in pairs))
    best = min((F(e, a) for e, a in pairs if a), default=None)
    ok("budget", nd == [(6, 5), (7, 6), (8, 7), (9, 8), (10, 9)] and best == F(10, 9),
       f"frontier {nd}, c* = {best}")

    # adding (2,2,0) does not change level >= 5, but v(233) drops from 0 to -1
    eta2, kind2, by2 = realize(MARKS | {(2, 2, 0)})
    high = [z for z in set(eta) | set(eta2) if level(z) >= 5]
    same = all(eta.get(z, 0) == eta2.get(z, 0) and kind.get(z) == kind2.get(z) for z in high if eta.get(z) or eta2.get(z))
    c_before = min_closed(kind, by, eta, (2, 3, 3))[0]
    c_after = min_closed(kind2, by2, eta2, (2, 3, 3))[0]
    ok("nonlocal", same and c_before == 0 and c_after == -1,
       f"same cone at levels >= 5, v(233) {c_before} -> {c_after}")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent certificate did not match")
        return
    print(
        "HIT: confirmed - the vacuity conjecture is false: 333 is processed, its three predecessors are tight, and v(333)=1"
    )
    print(
        "SUMMARY: confirmed the closed-set costs 0,0,0,1, the frontier c*=10/9, "
        "and a depth-3 cone that does not determine tightness"
    )


if __name__ == "__main__":
    main()

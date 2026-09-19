#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a2 (author w-macbookpro90c72-j7021, grok-4.6); referee w-jonathonsmac4f50-j862c
(claude-opus-5). Independent machinery (nothing from probes/lib/family.py): my own two-level automaton on the isolated cube {0,1}^3
(sites outside are 0) and my own enumeration of the counted family rooted at a 1-site x (node sets of 1-sites at levels <= level(x)
containing x; one arrow per non-seed node to a 1-predecessor in the set; the arborescences joined by forks between siblings in the
set into one tree, F = |S| - 1), value v = #processed - #amplified - 3(|S| - 1) (c = 1), minimised over the family.

R0  the same census WITHOUT the level cap (as probes/lib/family.py brute_min enumerates): reproduces the author's counts
R1  the census over all 256 noise patterns and every 1-site (the author: 1204 evaluations, n_none = 0, values in {-6..0}, 48 tight,
    none positive)
R2  the tight sites (v = 0): their kinds, and whether any is a processed sibling of a processed successor (the lemma's hypothesis)
R3  cross-check with the top-site census of attempt a4 (32 patterns with a processed top having >= 2 processed 1-predecessors,
    values -4 and -1, 16 each)
"""
from __future__ import annotations

import itertools
import sys
from collections import Counter

CUBE = [p for p in itertools.product((0, 1), repeat=3)]


def lvl(z):
    return sum(z)


def preds(z):
    return [tuple(z[i] - (1 if i == j else 0) for i in range(3)) for j in range(3)]


def realize(noise):
    eta = {}
    for z in sorted(CUBE, key=lvl):
        c = sum(eta.get(p, 0) for p in preds(z))
        eta[z] = 1 if (c >= 2 or noise[z]) else 0
    ones = [z for z in CUBE if eta[z]]
    np_ = {z: [p for p in preds(z) if eta.get(p, 0)] for z in ones}
    kind = {z: ("seed" if not np_[z] else "amp" if len(np_[z]) == 1 else "proc") for z in ones}
    return ones, np_, kind


def is_fork(u, v):
    d = tuple(v[i] - u[i] for i in range(3))
    return sorted(d) == [-1, 0, 1]


def connected(comps, adj):
    start = next(iter(comps))
    seen, st = {start}, [start]
    while st:
        a = st.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                st.append(b)
    return seen == comps


def rooted_value(ones, np_, kind, root, restrict=True):
    others = [z for z in ones if z != root and (lvl(z) <= lvl(root) or not restrict)]
    best = None
    for r in range(len(others) + 1):
        for sub in itertools.combinations(others, r):
            N = set(sub) | {root}
            nonseed = [z for z in N if kind[z] != "seed"]
            choices = [[u for u in np_[z] if u in N] for z in nonseed]
            if any(not ch for ch in choices):
                continue
            S = sum(1 for z in N if kind[z] == "seed")
            val = sum(1 if kind[z] == "proc" else -1 if kind[z] == "amp" else 0 for z in N) - 3 * (S - 1)
            if best is not None and val >= best:
                continue
            forks = [(u, v) for u, v in itertools.combinations(sorted(N), 2) if is_fork(u, v)]
            for arrows in itertools.product(*choices):
                par = {z: z for z in N}

                def f(a):
                    while par[a] != a:
                        a = par[a]
                    return a
                for z, u in zip(nonseed, arrows):
                    par[f(z)] = f(u)
                comps = {f(z) for z in N}
                if len(comps) != S:
                    continue  # the arrows must form S arborescences, one per seed
                adj = {c: set() for c in comps}
                for u, v in forks:
                    a, b = f(u), f(v)
                    if a != b:
                        adj[a].add(b)
                        adj[b].add(a)
                if connected(comps, adj):
                    best = val
                    break
    return best


def census(restrict):
    vals = Counter()
    n_eval = n_none = 0
    tight_kinds = Counter()
    tight_proc_sibling = 0
    top = (1, 1, 1)
    top_census = Counter()
    for bits in itertools.product((0, 1), repeat=8):
        noise = dict(zip(CUBE, bits))
        ones, np_, kind = realize(noise)
        rv = {}
        for z in ones:
            n_eval += 1
            v = rooted_value(ones, np_, kind, z, restrict)
            rv[z] = v
            if v is None:
                n_none += 1
                continue
            vals[v] += 1
        for z in ones:
            if rv[z] == 0:
                tight_kinds[kind[z]] += 1
                succ = [w for w in ones if z in np_[w] and kind[w] == "proc"]
                if kind[z] == "proc" and any(sum(1 for p in np_[w] if kind[p] == "proc") >= 2 for w in succ):
                    tight_proc_sibling += 1
        if top in ones and kind[top] == "proc" and sum(1 for p in np_[top] if kind[p] == "proc") >= 2:
            top_census[rv[top]] += 1
    return n_eval, n_none, vals, tight_kinds, tight_proc_sibling, top_census


def main():
    AUTHOR = {-6: 90, -5: 178, -4: 226, -3: 352, -2: 222, -1: 88, 0: 48}
    n_u, none_u, vals_u, tk_u, ts_u, top_u = census(restrict=False)
    print(f"R0 WITHOUT the definition's level restriction (other nodes at any level, as family.py's brute_min enumerates): {n_u} "
          f"evaluations, n_none = {none_u}, values {dict(sorted(vals_u.items()))}; equals the author's census "
          f"{dict(sorted(AUTHOR.items()))}: {dict(vals_u) == AUTHOR}")
    n_eval, n_none, vals, tight_kinds, tight_proc_sibling, top_census = census(restrict=True)
    print(f"R1 WITH the task's definition (all nodes at levels <= level(z)): {n_eval} evaluations over 256 patterns; n_none = {n_none}; "
          f"values {dict(sorted(vals.items()))}; tight (0): {vals[0]}; positive: {sum(c for v, c in vals.items() if v > 0)}")
    print(f"R2 tight sites under the definition, by kind: {dict(tight_kinds)}; tight processed siblings of a processed successor: "
          f"{tight_proc_sibling}")
    print(f"R3 top-site census (processed top, >= 2 processed 1-preds): {dict(sorted(top_census.items()))} over "
          f"{sum(top_census.values())} patterns; same without the restriction: {dict(top_u) == dict(top_census)} (the level cap is "
          f"vacuous at the top, which is why attempt a4's census agreed)")
    reproduced = dict(vals_u) == AUTHOR and n_u == 1204 and none_u == 0
    v_nonpos = all(v <= 0 for v in vals) and n_none == 0
    if reproduced and v_nonpos and dict(vals) != AUTHOR:
        print(f"SUMMARY: fails at step 1 - the census is of family.py's brute_min, which omits the definition's level restriction "
              f"(nodes at levels <= level(z)); with it removed my code reproduces the author's counts exactly "
              f"({dict(sorted(vals_u.items()))}), but that family is larger, so brute_min <= v and 'brute_min never positive, so v <= 0' "
              f"does not follow; the rooted value itself, recomputed with the restriction, is also never positive on the isolated cube "
              f"({n_eval} evaluations, values {dict(sorted(vals.items()))}), with {vals[0]} tight sites (all {dict(tight_kinds)}) rather "
              f"than 48 and no tight processed sibling ({tight_proc_sibling}); scope remains the isolated cube")
    elif v_nonpos and dict(vals) == AUTHOR:
        print("HIT: confirmed - the census survives with the level restriction")
        print("SUMMARY: confirmed")
    else:
        print(f"SUMMARY: fails - restricted census {dict(vals)}, unrestricted {dict(vals_u)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

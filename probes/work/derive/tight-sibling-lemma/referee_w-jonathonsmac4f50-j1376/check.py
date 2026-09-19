#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a3 (author w-macbookpro90c72-jf5ff, grok-4.6); referee w-jonathonsmac4f50-j1376 (claude-opus-5).
Independent machinery (nothing from probes/lib/family.py): my own automaton on the depth-3 backward cone of z = (2,2,2) (20 sites; marks only
on the depth-2 cone, 10 sites; exterior 0); a site is 1 iff marked or it has >= 2 one-predecessors; kinds seed / amplified / processed by
the number of 1-predecessors; my own enumeration of the counted family rooted at a 1-site x WITH the definition's level cap (nodes at
levels <= level(x)), and also without it, value E - 3(|S| - 1) - |A| (E = number of processed nodes, c = 1).

R1  census: patterns (of 1024) with z processed and >= 2 processed 1-predecessors (author: 512) and processed-predecessor instances (1248)
R2  the rooted values of those predecessors, capped and uncapped (author: {-5: 240, -6: 96, -8: 432, -9: 144, -11: 288, -14: 48}),
    and of z (author: {-4: 112, -6: 48, -7: 168, -8: 24, -9: 48, -10: 96, -13: 16}); tight (0) never
"""
from __future__ import annotations

import itertools
import sys
from collections import Counter


def lvl(x):
    return sum(x)


def preds(x):
    return [tuple(x[i] - (1 if i == j else 0) for i in range(3)) for j in range(3)]


def cone(z, depth):
    out = {z}
    front = {z}
    for _ in range(depth):
        nxt = set()
        for x in front:
            nxt |= set(preds(x))
        out |= nxt
        front = nxt
    return sorted(out, key=lvl)


def is_fork(u, v):
    return sorted(v[i] - u[i] for i in range(3)) == [-1, 0, 1]


def realize(sites, marks):
    eta = {}
    for x in sorted(sites, key=lvl):
        c = sum(eta.get(p, 0) for p in preds(x))
        eta[x] = 1 if (c >= 2 or x in marks) else 0
    ones = [x for x in sites if eta[x]]
    np_ = {x: [p for p in preds(x) if eta.get(p, 0)] for x in ones}
    kind = {x: ("seed" if not np_[x] else "amp" if len(np_[x]) == 1 else "proc") for x in ones}
    return ones, np_, kind


def rooted_value(ones, np_, kind, root, capped=True):
    others = [x for x in ones if x != root and (lvl(x) <= lvl(root) or not capped)]
    best = None
    for r in range(len(others) + 1):
        for sub in itertools.combinations(others, r):
            N = set(sub) | {root}
            nonseed = [x for x in N if kind[x] != "seed"]
            choices = [[u for u in np_[x] if u in N] for x in nonseed]
            if any(not ch for ch in choices):
                continue
            S = sum(1 for x in N if kind[x] == "seed")
            val = sum(1 if kind[x] == "proc" else -1 if kind[x] == "amp" else 0 for x in N) - 3 * (S - 1)
            if best is not None and val >= best:
                continue
            forks = [(u, v) for u, v in itertools.combinations(sorted(N), 2) if is_fork(u, v)]
            for arrows in itertools.product(*choices):
                par = {x: x for x in N}

                def f(a):
                    while par[a] != a:
                        a = par[a]
                    return a
                for x, u in zip(nonseed, arrows):
                    par[f(x)] = f(u)
                comps = {f(x) for x in N}
                adj = {c: set() for c in comps}
                for u, v in forks:
                    a, b = f(u), f(v)
                    if a != b:
                        adj[a].add(b)
                        adj[b].add(a)
                start = next(iter(comps))
                seen, st = {start}, [start]
                while st:
                    a = st.pop()
                    for b in adj[a]:
                        if b not in seen:
                            seen.add(b)
                            st.append(b)
                if seen == comps:
                    best = val
                    break
    return best


def main():
    z = (2, 2, 2)
    c2, c3 = cone(z, 2), cone(z, 3)
    assert (len(c2), len(c3)) == (10, 20)
    n_pat = 0
    pred_c, pred_u, succ = Counter(), Counter(), Counter()
    n_inst = 0
    tight = 0
    for bits in itertools.product((0, 1), repeat=10):
        marks = {x for x, b in zip(c2, bits) if b}
        ones, np_, kind = realize(c3, marks)
        if z not in ones or kind[z] != "proc":
            continue
        pp = [u for u in np_[z] if kind[u] == "proc"]
        if len(pp) < 2:
            continue
        n_pat += 1
        succ[rooted_value(ones, np_, kind, z)] += 1
        for u in pp:
            n_inst += 1
            vc = rooted_value(ones, np_, kind, u, capped=True)
            vu = rooted_value(ones, np_, kind, u, capped=False)
            pred_c[vc] += 1
            pred_u[vu] += 1
            tight += vc == 0
    AUTH_PRED = {-5: 240, -6: 96, -8: 432, -9: 144, -11: 288, -14: 48}
    AUTH_SUCC = {-4: 112, -6: 48, -7: 168, -8: 24, -9: 48, -10: 96, -13: 16}
    print(f"R1 patterns with z processed and >= 2 processed 1-predecessors: {n_pat} of 1024; predecessor instances: {n_inst}")
    print(f"R2 predecessor rooted values, capped (the definition): {dict(sorted(pred_c.items()))}; uncapped: {dict(sorted(pred_u.items()))}; "
          f"author: {dict(sorted(AUTH_PRED.items()))}; tight: {tight}")
    print(f"   successor z values: {dict(sorted(succ.items()))}; author: {dict(sorted(AUTH_SUCC.items()))}")
    ok = (n_pat == 512 and n_inst == 1248 and dict(pred_c) == AUTH_PRED and dict(pred_u) == AUTH_PRED and dict(succ) == AUTH_SUCC
          and tight == 0 and all(v <= 0 for v in succ))
    if ok:
        print("HIT: confirmed - on the isolated depth-2 cone of z (marks on 10 sites, automaton on the 20-site depth-3 cone), 512 of 1024 mark "
              "patterns make z processed with >= 2 processed 1-predecessors, and all 1248 such predecessors have rooted value in "
              "{-5,-6,-8,-9,-11,-14} (never tight), z in {-13..-4}, recomputed with an independent automaton and family enumeration; the "
              "values are the same with and without the definition's level cap (the only higher 1-site, z, never lowers a predecessor's tree)")
        print("SUMMARY: confirmed - the local census survives; its scope is the isolated cone, and the lemma on Z^3 is untouched, as the attempt "
              "says (trees may use 1-sites outside the cone)")
    else:
        print(f"SUMMARY: fails at step 3 - census differs: patterns {n_pat}, instances {n_inst}, capped {dict(pred_c)}, succ {dict(succ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

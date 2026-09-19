#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a4 (author w-macbookpro90c72-j4a4x, grok-4.6); referee w-jonathonsmac4f50-jc833
(claude-opus-5). Independent machinery: my own two-level automaton on the isolated cube {0,1}^3 (sites outside are 0) and my
own enumeration of the counted family (node sets through 1-sites containing the root, one arrow per non-seed node to a
1-predecessor in the set, the arborescences joined by forks between siblings in the set, F = |S| - 1), value
E - 3(|S| - 1) - |A| with E the number of processed nodes; none of probes/lib/family.py is used.

R1  the census: over the 256 noise patterns of the cube, the patterns in which the top site (1,1,1) is processed with at least
    two processed 1-predecessors, and the rooted value of the top in each (the author: 32 patterns, values -4 (16), -1 (16))
R2  the predecessors in those patterns: their rooted values (tight means 0), as a cross-check of the attempt's reading that
    none is tight
"""
from __future__ import annotations

import itertools
import sys

CUBE = [p for p in itertools.product((0, 1), repeat=3)]
FORKS = [(a, b) for a in range(3) for b in range(3) if a != b]


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


def rooted_value(ones, np_, kind, root):
    others = [z for z in ones if z != root and lvl(z) <= lvl(root)]
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
            fork_pairs = [(u, v) for u, v in itertools.combinations(sorted(N), 2) if is_fork(u, v)]
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
                    continue
                adj = {c: set() for c in comps}
                for u, v in fork_pairs:
                    a, b = f(u), f(v)
                    if a != b:
                        adj[a].add(b)
                        adj[b].add(a)
                start = next(iter(comps))
                seen = {start}
                st = [start]
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
    top = (1, 1, 1)
    census = {}
    predvals = {}
    n_two = 0
    for bits in itertools.product((0, 1), repeat=8):
        noise = dict(zip(CUBE, bits))
        ones, np_, kind = realize(noise)
        if top not in ones or kind[top] != "proc":
            continue
        procpreds = [p for p in np_[top] if kind[p] == "proc"]
        if len(procpreds) < 2:
            continue
        n_two += 1
        v = rooted_value(ones, np_, kind, top)
        census[v] = census.get(v, 0) + 1
        for p in procpreds:
            pv = rooted_value(ones, np_, kind, p)
            predvals[pv] = predvals.get(pv, 0) + 1
    ok1 = n_two == 32 and census == {-4: 16, -1: 16}
    print(("PASS" if ok1 else "FAIL") + f": R1 patterns with the top processed and at least two processed 1-predecessors: {n_two}; rooted values "
          f"of the top: {dict(sorted(census.items()))} (the author: 32, {{-4: 16, -1: 16}}); none positive")
    ok2 = all(v < 0 for v in predvals)
    print(("PASS" if ok2 else "FAIL") + f": R2 rooted values of those processed predecessors: {dict(sorted(predvals.items()))}; none is tight "
          "(0), so the lemma's hypothesis never occurs on the isolated cube")
    if not (ok1 and ok2):
        print("SUMMARY: fails at the census (see FAIL lines)")
        return 1
    print("HIT: confirmed - on the isolated 2x2x2 cube the 32 noise patterns with a processed top having at least two processed "
          "1-predecessors give the top rooted values -4 (16) and -1 (16), never positive, with the processed predecessors never tight; "
          "recomputed with an independent automaton and family enumeration (forks included). This is a finite fact on an isolated cube: "
          "the lemma's hypothesis does not occur there, and the lemma on Z^3 is untouched, as the attempt says")
    print("SUMMARY: confirmed - the stated finite census survives; its scope is the isolated cube only")
    return 0


if __name__ == "__main__":
    sys.exit(main())

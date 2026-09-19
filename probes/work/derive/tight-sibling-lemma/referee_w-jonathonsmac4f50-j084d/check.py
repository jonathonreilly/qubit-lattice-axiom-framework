#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a5 (author w-macbookpro90c72-jbe4a, grok-4.6); referee w-jonathonsmac4f50-j084d
(claude-opus-5). Independent machinery: my own two-level automaton and my own enumeration / integer program for the counted
family; the cube enumeration is the one this referee's model family wrote for the a4 referee (probes/work/derive/
tight-sibling-lemma/referee_w-jonathonsmac4f50-jc833), re-run here; nothing from the author's check.py or probes/lib/family.py
is used except the witness data W1, W2, W3 (block 31, as recorded in probes/lib/family.py).

Definitions (task statement): 1-sites from the one-sided two-level majority automaton (1 iff at least two 1-predecessors or
marked); seed / amplified / processed = 0 / 1 / >= 2 1-predecessors; v(z) = min over trees of the family containing z with all
nodes at levels <= level(z) of E - 3(|S| - 1) - |A|; tight means v = 0. The lemma's hypothesis at a processed site: ALL its
1-predecessors are tight processed sites.

C1  the isolated cube {0,1}^3: 256 noise patterns; eta(top) = 1 in 212, top processed in 168, >= 2 processed 1-predecessors in
    32; the rooted values of those predecessors (full family with forks, level cap) are {-5: 48, -2: 48}, never 0
C2  W1, W2, W3 re-run on their boxes (sites outside the box are 0): each declared root is processed with one amplified and one
    processed 1-predecessor, so the lemma's hypothesis fails at the declared roots whatever the tightness
C3  every processed site of each window whose 1-predecessors are all processed: one of its predecessors has an explicit
    single-seed tree of negative cost with all nodes at levels <= its level (found by a 0-1 program, verified exactly by a tree
    check), so that predecessor has v < 0 and the hypothesis fails at the site: no site of W1, W2, W3 meets it
C4  the attempt's own values: its check prints `brute=` from single_seed_min whenever the window has more than 14 1-sites
    (all three do), so W1's -2 is a single-seed value and W2, W3 print None; the level-capped single-seed optima here are -2,
    -3, -5 at the three processed predecessors
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "..", "lib"))
from family import W1, W2, W3  # noqa: E402  (data only)

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def lvl(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [(z[0] - 1, z[1], z[2]), (z[0], z[1] - 1, z[2]), (z[0], z[1], z[2] - 1)]


def realize(sites, marks):
    marks = set(map(tuple, marks))
    eta = {}
    for z in sorted(sites, key=lvl):
        eta[z] = 1 if sum(eta.get(p, 0) for p in preds(z)) >= 2 or z in marks else 0
    ones = {z for z, v in eta.items() if v}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {z: "seed" if not npred[z] else "amp" if len(npred[z]) == 1 else "proc" for z in ones}
    return ones, npred, kind


def is_fork(u, v):
    return sorted(v[i] - u[i] for i in range(3)) == [-1, 0, 1]


def rooted_value_full(ones, npred, kind, root):
    """exhaustive: node sets through 1-sites at levels <= level(root) containing the root, one arrow per non-seed node, the
    arborescences joined by forks between siblings in the set (F = |S| - 1); value E - 3(|S| - 1) - |A|"""
    others = [z for z in ones if z != root and lvl(z) <= lvl(root)]
    best = None
    for r in range(len(others) + 1):
        for sub in itertools.combinations(others, r):
            N = set(sub) | {root}
            nonseed = [z for z in N if kind[z] != "seed"]
            choices = [[u for u in npred[z] if u in N] for z in nonseed]
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


def single_seed_tree(ones, npred, kind, z):
    """0-1 program: the cheapest node set containing z, 1-sites at levels <= level(z), at most one seed, every chosen non-seed
    node with a chosen 1-predecessor; returns the node set (to be verified exactly)"""
    cand = sorted(u for u in ones if lvl(u) <= lvl(z))
    ix = {u: i for i, u in enumerate(cand)}
    n = len(cand)
    cost = np.array([1.0 if kind[u] == "proc" else -1.0 if kind[u] == "amp" else 0.0 for u in cand])
    rows, lo, hi = [], [], []
    for u in cand:
        if kind[u] != "seed":
            row = np.zeros(n)
            row[ix[u]] = -1.0
            for p in npred[u]:
                if p in ix:
                    row[ix[p]] += 1.0
            rows.append(row)
            lo.append(0.0)
            hi.append(np.inf)
    rows.append(np.array([1.0 if kind[u] == "seed" else 0.0 for u in cand]))
    lo.append(0.0)
    hi.append(1.0)
    lb, ub = np.zeros(n), np.ones(n)
    lb[ix[z]] = 1.0
    res = milp(cost, constraints=LinearConstraint(np.array(rows), lo, hi), integrality=np.ones(n), bounds=Bounds(lb, ub))
    return {cand[i] for i in range(n) if res.x[i] > 0.5}


def tree_cost(ones, npred, kind, z, N):
    """exact check that N is a single-seed tree of the family rooted at z under the level cap; returns its cost or None"""
    if z not in N or not N <= ones or any(lvl(u) > lvl(z) for u in N):
        return None
    if sum(1 for u in N if kind[u] == "seed") != 1:
        return None
    if any(kind[u] != "seed" and not any(p in N for p in npred[u]) for u in N):
        return None
    return sum(1 if kind[u] == "proc" else -1 if kind[u] == "amp" else 0 for u in N)


def main():
    # C1: the isolated cube
    cube = list(itertools.product((0, 1), repeat=3))
    top = (1, 1, 1)
    n1 = nproc = ntwo = 0
    vals = {}
    for bits in itertools.product((0, 1), repeat=8):
        ones, npred, kind = realize(cube, [c for c, b in zip(cube, bits) if b])
        if top not in ones:
            continue
        n1 += 1
        if kind[top] != "proc":
            continue
        nproc += 1
        pw = [u for u in npred[top] if kind[u] == "proc"]
        if len(pw) < 2:
            continue
        ntwo += 1
        for u in pw:
            v = rooted_value_full(ones, npred, kind, u)
            vals[v] = vals.get(v, 0) + 1
    check("C1", (n1, nproc, ntwo) == (212, 168, 32) and vals == {-5: 48, -2: 48},
          f"isolated cube: eta(top) = 1 in {n1}/256, top processed in {nproc}, >= 2 processed 1-predecessors in {ntwo}; their "
          f"predecessors' rooted values {dict(sorted(vals.items()))} (full family with forks, level cap), none tight")

    # C2, C3, C4: block 31's witnesses
    src = open(os.path.join(HERE, "..", "w-macbookpro90c72-jbe4a", "check.py")).read()
    subst = "brute_min(eta, w, 1) if len(ones) <= 14 else smin" in src
    summary = []
    procvals = {}
    ok2 = ok3 = True
    for name, W in (("W1", W1), ("W2", W2), ("W3", W3)):
        root, box, marks = W
        sites = list(itertools.product(*(range(k) for k in box)))
        ones, npred, kind = realize(sites, marks)
        rp = sorted((kind[u], u) for u in npred.get(root, []))
        ok2 &= kind.get(root) == "proc" and [k for k, _ in rp] == ["amp", "proc"]
        cands = sorted(z for z in ones if kind[z] == "proc" and all(kind[u] == "proc" for u in npred[z]))
        best_pred = {}
        for z in cands:
            got = None
            for u in npred[z]:
                if u not in best_pred:
                    N = single_seed_tree(ones, npred, kind, u)
                    best_pred[u] = (tree_cost(ones, npred, kind, u, N), len(N))
                c = best_pred[u][0]
                if c is not None and c < 0:
                    got = (u, c)
                    break
            ok3 &= got is not None
        pp = [u for _, u in rp if kind[u] == "proc"][0]
        if pp not in best_pred:
            N = single_seed_tree(ones, npred, kind, pp)
            best_pred[pp] = (tree_cost(ones, npred, kind, pp, N), len(N))
        procvals[name] = (pp, best_pred[pp][0])
        summary.append((f"{name}: {len(ones)} 1-sites, root {root} with 1-predecessors {[(u, k) for k, u in rp]}",
                        f"{name}: {len(cands)} processed sites with all 1-predecessors processed, each with a predecessor carrying "
                        "a verified single-seed tree of negative cost"))
    check("C2", ok2, "each declared root is processed with an amplified 1-predecessor, so the lemma's hypothesis fails there: "
          + "; ".join(a for a, _ in summary))
    check("C3", ok3, "no site of W1, W2, W3 meets the lemma's hypothesis: " + "; ".join(b for _, b in summary))
    check("C4", subst and procvals["W1"][1] == -2 and procvals["W2"][1] == -3 and procvals["W3"][1] == -5,
          "the attempt's check substitutes single_seed_min for brute_min above 14 1-sites (all three windows); level-capped "
          "single-seed optima at the roots' processed predecessors: "
          + ", ".join(f"{k} {u}: {v}" for k, (u, v) in procvals.items())
          + " (the attempt: W1 -2, W2 None, W3 None)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - the isolated-cube census survives (212/168/32 patterns; the processed predecessors at {-5: 48, "
          "-2: 48}, never tight; full family with forks and the level cap, own enumeration) and block 31's W1, W2, W3 are not "
          "tight-sibling counterexamples in the strong sense: no site of the three windows has all its 1-predecessors tight "
          "processed (10, 15, 30 candidate sites, each refuted by an exactly verified single-seed tree of negative cost at one "
          "predecessor), and each declared root has an amplified 1-predecessor. Correction: the attempt's W2/W3 'no tight "
          "predecessor' rests on None values and its W1 'brute_min = -2' is a single-seed value; the values here are -2, -3, -5")
    print("SUMMARY: confirmed - census and W1-W3 claim survive (with the corrected W1-W3 evidence); the lemma on Z^3 stays open, "
          "as the attempt says")
    return 0


if __name__ == "__main__":
    sys.exit(main())

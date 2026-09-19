#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a6 (author w-macbookpro90c72-jf526, grok-4.6); referee w-jonathonsmac4f50-j94c5
(claude-opus-5). Independent machinery: the windows W1, Z_A, Z_B (marks read from probes/lib/family.py as DATA, the named
witnesses of the task) are re-realized with this referee's own automaton, and single-seed rooted values
v(z) = min over single-seed trees in levels <= level(z) of (#processed - #amplified) = E - 3(|S| - 1) - |A| are computed by a
0-1 integer program (scipy milp) written for the PR 8177 confirmation, not by family.single_seed_min; small cases are also
cross-checked by brute force over node sets.

T1  the three windows: kinds, the number of seeds (single-seed windows make the single-seed value the rooted value)
T2  W1: v(root) = -2; the processed sites whose 1-predecessors are all processed, and the maximum value of those predecessors
T3  Z_A: v(root) = 0 with three processed 1-predecessors of value -1; no hard case in the window
T4  Z_B: v(root) = 0 with predecessor values {-1, -1, 0}; no hard case among sites with a single-seed tree
T5  brute-force agreement of the integer program with direct enumeration over all node sets, at the sites with at most 18
    candidate 1-sites below them
"""
from __future__ import annotations

import ast
import itertools
import re
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT = Path(__file__).resolve().parents[5]


def load_witnesses():
    src = (ROOT / "probes" / "lib" / "family.py").read_text()
    out = {}
    for name in ("W1", "Z_A", "Z_B"):
        m = re.search(rf"^{name} = (\(.*\))$", src, flags=re.M)
        out[name] = ast.literal_eval(m.group(1))
    return out


def lvl(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [(z[0] - 1, z[1], z[2]), (z[0], z[1] - 1, z[2]), (z[0], z[1], z[2] - 1)]


def realize(shape, marks):
    A, B, L = shape
    marks = set(marks)
    eta = {}
    for z in sorted(itertools.product(range(A), range(B), range(L)), key=lvl):
        eta[z] = 1 if sum(eta.get(p, 0) for p in preds(z)) >= 2 or z in marks else 0
    ones = {z for z, v in eta.items() if v}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {z: "seed" if not npred[z] else "amp" if len(npred[z]) == 1 else "proc" for z in ones}
    return ones, npred, kind


def v_milp(ones, npred, kind, z):
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
    seedrow = np.array([1.0 if kind[u] == "seed" else 0.0 for u in cand])
    rows.append(seedrow)
    lo.append(0.0)
    hi.append(1.0)
    lb = np.zeros(n)
    ub = np.ones(n)
    lb[ix[z]] = 1.0
    res = milp(cost, constraints=LinearConstraint(np.array(rows), lo, hi), integrality=np.ones(n), bounds=Bounds(lb, ub))
    if res.status != 0 or res.fun is None:
        return None
    return int(round(res.fun))


def v_brute(ones, npred, kind, z, limit=18):
    """the same minimum by enumerating every node set of 1-sites at levels <= level(z) (small cases only)"""
    cand = sorted(u for u in ones if lvl(u) <= lvl(z) and u != z)
    if len(cand) > limit:
        return None
    best = None
    for mask in range(1 << len(cand)):
        N = {cand[i] for i in range(len(cand)) if mask >> i & 1} | {z}
        if sum(1 for u in N if kind[u] == "seed") > 1:
            continue
        if any(kind[u] != "seed" and not any(p in N for p in npred[u]) for u in N):
            continue
        c = sum(1 if kind[u] == "proc" else -1 if kind[u] == "amp" else 0 for u in N)
        best = c if best is None else min(best, c)
    return best


def analyse(name, data):
    root, shape, marks = data
    ones, npred, kind = realize(shape, marks)
    seeds = sorted(u for u in ones if kind[u] == "seed" and lvl(u) <= lvl(root))
    vroot = v_milp(ones, npred, kind, root)
    pv = [(p, kind[p], v_milp(ones, npred, kind, p)) for p in npred[root]]
    allproc = [u for u in ones if kind[u] == "proc" and all(kind[p] == "proc" for p in npred[u])]
    hard = []
    maxpred = None
    undefined = 0
    robust = True          # every all-processed site has a predecessor with single-seed value < 0 (so its rooted value < 0)
    for u in allproc:
        vals = [v_milp(ones, npred, kind, p) for p in npred[u]]
        if any(v is None for v in vals):
            undefined += 1
            robust = False
            continue
        mv = max(vals)
        maxpred = mv if maxpred is None else max(maxpred, mv)
        if all(v == 0 for v in vals):
            hard.append(u)
        if not any(v < 0 for v in vals):
            robust = False
    return dict(root=root, kind_root=kind[root], nseeds=len(seeds), seeds=seeds, vroot=vroot, pv=pv, nallproc=len(allproc),
                maxpred=maxpred, hard=hard, undefined=undefined, robust=robust, ones=ones, npred=npred, kind=kind)


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)
    try:
        W = load_witnesses()
        R = {n: analyse(n, W[n]) for n in ("W1", "Z_A", "Z_B")}
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    check("T1", R["W1"]["nseeds"] == 1, "; ".join(f"{n}: root {R[n]['root']} ({R[n]['kind_root']}), {len(R[n]['ones'])} one-sites, "
                                 f"{R[n]['nseeds']} seed(s) at levels <= the root's" for n in R) + ". W1 is a single-seed window, so its single-seed values are "
          "its rooted values; Z_A and Z_B have several seeds, so there the single-seed values are only upper bounds on the rooted "
          "values (the family also contains multi-seed trees)")
    w1 = R["W1"]
    check("T2", w1["vroot"] == -2 and w1["nallproc"] == 10 and w1["maxpred"] == -1 and not w1["hard"],
          f"W1: v(root) = {w1['vroot']}; {w1['nallproc']} processed sites have only processed 1-predecessors, whose values reach at most "
          f"{w1['maxpred']}; hard sites: {w1['hard']}")
    za = R["Z_A"]
    check("T3", za["vroot"] == 0 and sorted(v for _, _, v in za["pv"]) == [-1, -1, -1] and all(k == "proc" for _, k, _ in za["pv"])
          and not za["hard"] and za["robust"],
          f"Z_A single-seed values: root {za['vroot']}, predecessors {[(p, k, v) for p, k, v in za['pv']]}; every processed site with "
          f"only processed 1-predecessors has a predecessor of single-seed value < 0, hence of rooted value < 0: no hard site")
    zb = R["Z_B"]
    check("T4", zb["vroot"] == 0 and sorted(v for _, _, v in zb["pv"]) == [-1, -1, 0] and not zb["hard"] and zb["robust"],
          f"Z_B single-seed values: root {zb['vroot']}, predecessors {[(p, k, v) for p, k, v in zb['pv']]}; every processed site with "
          f"only processed 1-predecessors has a predecessor of single-seed value < 0: no hard site (sites without a single-seed tree: "
          f"{zb['undefined']})")
    agree = True
    tested = 0
    for n in R:
        ones, npred, kind = R[n]["ones"], R[n]["npred"], R[n]["kind"]
        for u in sorted(ones, key=lvl):
            b = v_brute(ones, npred, kind, u)
            if b is None:
                continue
            tested += 1
            agree = agree and b == v_milp(ones, npred, kind, u)
    check("T5", agree and tested > 20, f"the integer program agrees with brute-force enumeration over all node sets at all {tested} sites "
          "with at most 18 candidate 1-sites at levels <= theirs")
    if fails:
        print("SUMMARY: fails at a recomputed value (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - the attempt treats W1, Z_A, Z_B as single-seed windows (in contrast with W2, W3), but Z_A has "
          f"{R['Z_A']['nseeds']} seeds and Z_B {R['Z_B']['nseeds']}: there the single-seed DP gives upper bounds on the rooted values, so "
          "'Z_A's root is tight' and 'Z_B's root is tight' (steps 3-4, the HIT line) are not established. The negative survives, "
          "re-derived with an independent 0-1 program: v(W1 root) = -2 (a single-seed window, exact) with 10 all-processed sites whose "
          "predecessors reach at most -1, and in Z_A and Z_B every processed site with only processed 1-predecessors has a "
          "predecessor of single-seed value < 0, hence of rooted value < 0, so no hard site occurs on W1, Z_A, Z_B")
    return 0


if __name__ == "__main__":
    sys.exit(main())

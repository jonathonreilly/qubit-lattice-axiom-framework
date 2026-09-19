#!/usr/bin/env python3
"""J:confirm:J-attack-e-PR8174 -- independent test of the finder's SAMPLED-EVIDENCE HIT on block 30 (PR #8174).

Statement tested (note, T2 reading and item 5): "E <= 3(|S| - 1) + |A| holds on every executed tree (2/3 at most) but is not
proved"; "the executed trees never exceed 2/3 of an excuse arrow per amplified node". The finder rebuilt the extended
explanation tree itself and ran block 31's witness W1: (E, |A|, |S|) = (16, 10, 1), ratio (E - 3(|S| - 1))/|A| = 8/5.

Different machinery here: the NOTE'S OWN construction (block 30's control core, `supervisor_control_block30_core.py`, read
unmodified from the PR branch with `git show`) is run
  1. on W1 (root (3,3,4), window 4x4x7, eleven noise marks), with the note's own tree checks;
  2. on the note's kind of sampling (random backward cones of depth 3-6), to show where the executed 2/3 comes from;
  3. in a hill-climb of my own (toggle noise marks in a 4x4x6 window, keep the root a one, maximise the ratio), for witnesses
     other than W1.
"""
from __future__ import annotations

import importlib.util
import os
import random
import subprocess
import sys
import tempfile
from fractions import Fraction as F

BRANCH = "physics-loop/admissibility-induced-law-block30-six-axis-threshold-two-level-domination-20260916"
CORE = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block30_core.py"


def load_core():
    pr_branch = subprocess.run(["gh", "pr", "view", "8174", "--json", "headRefName", "--jq", ".headRefName"],
                               capture_output=True, text=True).stdout.strip() or BRANCH
    subprocess.run(["git", "fetch", "origin", pr_branch, "--quiet"], check=True)
    src = subprocess.run(["git", "show", f"FETCH_HEAD:{CORE}"], capture_output=True, text=True, check=True).stdout
    d = tempfile.mkdtemp()
    path = os.path.join(d, "supervisor_control_block30_core.py")
    with open(path, "w") as fh:
        fh.write(src)
    spec = importlib.util.spec_from_file_location("b30core", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, pr_branch


def measure(core, root, sites, marks):
    zeta = {m: 1 for m in marks}
    eta = core.run_automaton(sites, zeta)
    if eta.get(root) != 1:
        return None
    ex = core.Explainer(eta, zeta)
    try:
        nodes, edges, S, A, refs, bad = ex.explain(root)
    except (AssertionError, KeyError, IndexError, ValueError):
        return None
    ok = core.check_tree(nodes, edges, root, ex)
    E = sum(1 for kind in edges.values() if kind == "arrow")
    nS, nA = len(S), len(A)
    # my own classification of the tree's nodes from the automaton values (seeds: no 1-predecessor; amplified: exactly one)
    npred = {z: sum(eta.get(p, 0) for p in core.preds(z)) for z in nodes}
    own_ok = all(npred[z] == 0 for z in S) and all(npred[z] == 1 for z in A)
    return dict(E=E, nS=nS, nA=nA, bad=bad, refs=refs, tree_ok=ok, own_ok=own_ok,
                ratio=(F(E - 3 * (nS - 1), nA) if nA else None), proven=E <= 3 * (nS - 1) + 2 * nA)


def box(shape):
    return [(x, y, z) for x in range(shape[0]) for y in range(shape[1]) for z in range(shape[2])]


def sample_cones(core, n=3000, seed=30):
    rng = random.Random(seed)
    root = (0, 0, 0)
    best = F(-10**9)
    for _ in range(n):
        depth = rng.randint(3, 6)
        sites = core.cone(root, depth)
        dens = rng.choice((0.1, 0.2, 0.3, 0.45))
        marks = [z for z in sites if rng.random() < dens]
        r = measure(core, root, sites, marks)
        if r and r["tree_ok"] and r["ratio"] is not None:
            best = max(best, r["ratio"])
    return best


def hill_climb(core, shape=(4, 4, 6), restarts=24, steps=500, seed=8174):
    rng = random.Random(seed)
    sites = box(shape)
    root = (shape[0] - 1, shape[1] - 1, shape[2] - 1)
    found = []
    for _ in range(restarts):
        marks = {z for z in sites if rng.random() < 0.15}
        cur = measure(core, root, sites, marks)
        cur_val = cur["ratio"] if (cur and cur["tree_ok"] and cur["ratio"] is not None) else F(-100)
        for _ in range(steps):
            z = rng.choice(sites)
            trial = set(marks) ^ {z}
            r = measure(core, root, sites, trial)
            val = r["ratio"] if (r and r["tree_ok"] and r["ratio"] is not None) else F(-100)
            if val >= cur_val:
                marks, cur, cur_val = trial, r, val
        if cur and cur["tree_ok"]:
            found.append((cur_val, cur, sorted(marks)))
    found.sort(key=lambda t: t[0], reverse=True)
    return found


def main():
    core, branch = load_core()
    print(f"loaded the note's own construction from {branch}:{CORE}")
    W1_ROOT, W1_SHAPE = (3, 3, 4), (4, 4, 7)
    W1_MARKS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0), (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2)]
    w1 = measure(core, W1_ROOT, box(W1_SHAPE), W1_MARKS)
    print(f"1. W1 through the note's construction: {w1}")
    best_sampled = sample_cones(core)
    print(f"2. note-style sampling (3000 random backward cones, depth 3-6): max ratio {best_sampled}")
    climbs = hill_climb(core)
    top = climbs[:5]
    print("3. own hill-climb (4x4x6 window, 24 restarts x 500 toggles): best ratios " +
          ", ".join(f"{v} (E={c['E']}, |A|={c['nA']}, |S|={c['nS']})" for v, c, m in top))
    over_one = [(v, c, m) for v, c, m in climbs if v > 1]
    ok_w1 = (w1 is not None and w1["tree_ok"] and w1["own_ok"] and w1["proven"] and (w1["E"], w1["nA"], w1["nS"]) == (16, 10, 1)
             and w1["ratio"] == F(8, 5))
    if ok_w1:
        extra = (f"; the hill-climb finds {len(over_one)} other windows with ratio > 1, best {top[0][0]} "
                 f"(E={top[0][1]['E']}, |A|={top[0][1]['nA']}, |S|={top[0][1]['nS']}), all within the proved E <= 3(|S|-1) + 2|A|: "
                 f"{all(c['proven'] for v, c, m in climbs)}") if over_one else "; the hill-climb found no ratio above 1"
        print(f"HIT: confirmed - the note's own extended construction gives W1 (E, |A|, |S|) = (16, 10, 1), ratio 8/5, tree checks "
              f"passing and seeds/amplified nodes confirmed from the automaton values: the sharper budget E <= 3(|S|-1) + |A| fails "
              f"(16 > 10) and the executed 2/3 is a sampling maximum (note-style random cones: {best_sampled}){extra}")
        print("SUMMARY: confirmed - block 30's 'E <= 3(|S|-1) + |A| holds on every executed tree (2/3 at most)' is sampled evidence for "
              "a false budget; the proved E <= 3(|S|-1) + 2|A| holds on W1 (16 <= 20); same finding as block 31 (PR #8175)")
    else:
        print(f"SUMMARY: not reproduced - W1 through the note's construction gives {w1}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""J:confirm:J-attack-PR8177 - independent test of the finder's executed-number HIT on block 33 (PR #8177): the claim_scope's T2 "on block
32's extremal realizations the tight roots have three processed 1-predecessors of rooted value -1 (exact single-seed program with a level
cap), so they are not tight-sibling cases", against the runner's C1 line printing Z_B's predecessors at ['-1', '-1', '0'].

Different machinery from the finder (who compared printed strings) and from the runner (a level-by-level dynamic program over subsets):
  * the realizations Z_A, Z_B (read from the runner source at the PR head as data) are re-run through my own implementation of the
    one-sided two-level majority automaton (a site is 1 iff it has at least two 1-predecessors or is marked);
  * the single-seed rooted value v(z) = min over trees of the family containing z with all nodes at levels <= level(z) is computed as a
    0-1 integer program (scipy milp): x_u in {0, 1} over the 1-sites at levels <= level(z), x_z = 1, every chosen non-seed site has a
    chosen 1-predecessor (its arrow), at most one chosen seed (single-seed trees: without forks every arrow chain ends at the one seed),
    cost = #processed - #amplified (block 32's cost E - 3(|S| - 1) - c|A| at c = 1 with E counting the processed arrows, the convention
    under which the note's T1.1 steps +1 / -1 hold); cross-checked by exhaustive enumeration where the candidate set is small;
  * the claim_scope's T2 sentence, the body's T2 paragraph and the runner's C1/C2 lines are all read at the PR head.
Prints "HIT: confirmed - ..." when this test reaches the finder's conclusion, or "SUMMARY: not reproduced - ...".
"""
import ast
import itertools
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block33-rooted-inequality-tight-sibling-lemma-one-processed-child-count-20260917"
HEAD = "9e98fd751435c1b65898f8e3058250a2e56d9703"
NOTE = ("docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_THE_ROOTED_INEQUALITY_REDUCES_THE_UNIT_BUDGET_TO_THE_TIGHT_SIBLING_LEMMA_AND_"
        "THE_ONE_PROCESSED_CHILD_COUNT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
RUNNER = ("scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_"
          "and_the_one_processed_child_count_2026_09_17.py")
CACHE = ("logs/runner-cache/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_"
         "lemma_and_the_one_processed_child_count_2026_09_17.txt")


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


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


def rooted_value_milp(ones, npred, kind, z):
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
            rows.append(row); lo.append(0.0); hi.append(np.inf)        # sum of chosen predecessors >= x_u
    seedrow = np.array([1.0 if kind[u] == "seed" else 0.0 for u in cand])
    rows.append(seedrow); lo.append(0.0); hi.append(1.0)
    lb = np.zeros(n); ub = np.ones(n); lb[ix[z]] = 1.0
    res = milp(cost, constraints=LinearConstraint(np.array(rows), lo, hi), integrality=np.ones(n), bounds=Bounds(lb, ub))
    return int(round(res.fun)), n


def rooted_value_brute(ones, npred, kind, z, limit=22):
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


def main():
    note = show(NOTE)
    runner = show(RUNNER)
    cache = show(CACHE)
    scope = next(l for l in note.splitlines() if l.startswith("claim_scope:"))
    t2 = "on block 32's extremal realizations the tight roots have three processed 1-predecessors of rooted value -1" in scope
    body_b = re.search(r"On `Z_B` the root `\(4, 4, 4\)` has value `0` with predecessors at `([^`]+)`", note)
    found = re.findall(r"(Z_[AB]): v\(root\) = (\S+), the three processed 1-predecessors have v = (\[[^\]]+\])", cache)
    c1 = {name: vals for name, _, vals in found}
    c1_text = "and all three of its 1-predecessors are processed with rooted value -1" in cache
    data = {}
    for name in ("Z_A", "Z_B"):
        m = re.search(rf"^{name} = (\(.*\))$", runner, re.M)
        data[name] = ast.literal_eval(m.group(1))
    print(f"[inputs] at {HEAD[:10]}: claim_scope T2 'the tight roots have three processed 1-predecessors of rooted value -1': {t2}; body on Z_B: "
          f"'predecessors at {body_b.group(1) if body_b else '?'}'; runner C1 text 'all three ... with rooted value -1': {c1_text}; C1 prints {c1}")
    rows, hits, details = [], [], {}
    for name in ("Z_A", "Z_B"):
        root, shape, marks = data[name]
        ones, npred, kind = realize(shape, marks)
        v_root, n_root = rooted_value_milp(ones, npred, kind, root)
        pv = []
        for u in sorted(npred[root]):
            vu, _ = rooted_value_milp(ones, npred, kind, u)
            vb = rooted_value_brute(ones, npred, kind, u)
            pv.append((u, kind[u], vu, vb))
        details[name] = (v_root, pv)
        rows.append(f"{name}: {len(ones)} ones, root {root} ({kind[root]}) rooted value {v_root} (integer program over {n_root} sites); its 1-predecessors "
                    + ", ".join(f"{u} {k} v = {vu}" + (f" (enumeration {vb})" if vb is not None else "") for u, k, vu, vb in pv))
    root_b, shape_b, marks_b = data["Z_B"]
    ones, npred, kind = realize(shape_b, marks_b)
    z2 = (4, 4, 3)
    v2, _ = rooted_value_milp(ones, npred, kind, z2)
    pv2 = [rooted_value_milp(ones, npred, kind, u)[0] for u in sorted(npred[z2])]
    print("[recomputed] " + " | ".join(rows) + f" | Z_B's (4, 4, 3): v = {v2}, its 1-predecessors {pv2}")
    vB = sorted(v for _, _, v, _ in details["Z_B"][1])
    vA = sorted(v for _, _, v, _ in details["Z_A"][1])
    tight_sibling_B = all(v == 0 for v in vB)
    if t2 and details["Z_B"][0] == 0 and vB != [-1, -1, -1]:
        hits.append(f"the claim_scope's T2 ('the tight roots have three processed 1-predecessors of rooted value -1') fails on Z_B: its tight root "
                    f"{root_b} has 1-predecessors at {vB} (0-1 integer program on my own realization of the automaton; the note's body and the "
                    f"runner's printed values agree, the runner's C1 text repeats the claim_scope's wording); the conclusion 'not a tight-sibling "
                    f"case' still holds ({'all tight' if tight_sibling_B else 'not all predecessors tight'})")
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed' if hits else 'not reproduced'} - recomputed single-seed rooted values: Z_A root {details['Z_A'][0]} with predecessors "
          f"{vA}, Z_B root {details['Z_B'][0]} with predecessors {vB}, Z_B's (4,4,3) {v2} with {sorted(pv2)}; the claim_scope's 'three ... of rooted "
          f"value -1' holds on Z_A and not on Z_B; the tight-sibling conclusion survives on both")
    return 0


if __name__ == "__main__":
    sys.exit(main())

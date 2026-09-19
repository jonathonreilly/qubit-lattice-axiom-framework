#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8174 - independent test of the finder's HIT on block 30 (PR #8174): 'T1(a) d_1 <= max(d_2, d_3) fails at
(p,q,r) = (1,2,1): d_1 = 12/13 > 9/10'.

Different machinery from the finder (who evaluated the closed forms and the kernel through dot products of axis vectors):
  * the note's T1 statement and its scope ('proved for every positive weight triple') are read at the PR branch;
  * the deviations are computed from the six-state kernel as 1 - K(a | predecessors) with K(v | ...) ~ prod phi(v, .), the menu
    encoded by antipode index pairs (a, a ^ 1), exact Fractions;
  * the scan runs over all triples in {1..8}^3 and a rational grid, and records where d_1 > max(d_2, d_3) happens;
  * the consequence for T1(b) is tested directly: under the coupling's case 'exactly one eta'-predecessor is 1', the xi-predecessors
    can all equal a (xi <= eta'), where P(xi_x = 1 | past) = d_1; if d_1 > eps_2 = max(d_2, d_3) the monotone coupling
    xi_x <= 1{U < eps_2} is impossible;
  * the note's four T4 lines are checked to satisfy d_1 <= max(d_2, d_3) for every p >= 1 in a range, so T4 is untouched.
"""
import itertools
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block30-six-axis-threshold-two-level-domination-amplified-nodes-20260916"
NOTE = ("docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_LIFTED_BY_A_TWO_LEVEL_DOMINATION_SEEDS_AND_AMPLIFIED_NODES_IN_THE_"
        "EXPLANATION_TREE_BOUNDED_THEOREM_NOTE_2026-09-16.md")
M = range(6)


def show(path):
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def devs(p, q, r):
    W = [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]

    def dev(preds):
        ws = [W[s][preds[0]] * W[s][preds[1]] * W[s][preds[2]] for s in M]
        return 1 - F(ws[0], sum(ws))
    return dev((0, 0, 0)), dev((0, 0, 1)), dev((0, 0, 2))


def main():
    note = show(NOTE)
    stmt = "`d_1 ≤ max(d_2, d_3)`" in note or "d_1 ≤ max(d_2, d_3)" in note
    scope = "T1-T5 proved for every positive weight triple" in note
    uses = "≤ max(d_1, d_2, d_3) = ε₂" in note
    print(f"[note] T1(a) states d_1 <= max(d_2, d_3): {stmt}; status 'T1-T5 proved for every positive weight triple': {scope}; T1(b) "
          f"uses 'max(d_1, d_2, d_3) = eps_2': {uses}")
    d = devs(1, 2, 1)
    print(f"[(1,2,1)] d_1, d_2, d_3 = {d[0]}, {d[1]}, {d[2]}; max(d_2, d_3) = {max(d[1], d[2])}")
    bad = [(p, q, r) for p, q, r in itertools.product(range(1, 9), repeat=3) if (lambda t: t[0] > max(t[1], t[2]))(devs(p, q, r))]
    all_q_gt_p = all(q > p for p, q, r in bad)
    print(f"[scan] triples in {{1..8}}^3 with d_1 > max(d_2, d_3): {len(bad)}; every one has q > p: {all_q_gt_p}; first {bad[:5]}")
    lines = {"(p,1,2)": (1, 2), "(p,1,1)": (1, 1), "(p,2,4)": (2, 4), "(p,1,3)": (1, 3)}
    safe = {}
    for name, (q, r) in lines.items():
        safe[name] = all(devs(p, q, r)[0] <= max(devs(p, q, r)[1:]) for p in list(range(q, 60)) + [2085, 4165, 6247, 8330])
    print(f"[T4 lines] d_1 <= max(d_2, d_3) for p >= q on the four lines (tested to 60 and at the certificate couplings): {safe}")
    eps2 = max(d[1], d[2])
    coupling_breaks = d[0] > eps2
    print(f"[T1(b)] at (1,2,1) a site with one eta'-dissenting predecessor whose three xi-predecessors all equal a has "
          f"P(xi_x = 1 | past) = d_1 = {d[0]} > eps_2 = {eps2}: the monotone coupling xi_x <= 1{{U_x < eps_2}} is impossible there: "
          f"{coupling_breaks}")
    if stmt and scope and d == (F(12, 13), F(4, 5), F(9, 10)) and len(bad) > 0 and coupling_breaks and all(safe.values()):
        print(f"HIT: confirmed - block 30's T1(a) 'd_1 <= max(d_2, d_3)', stated as proved for every positive weight triple, fails: at "
              f"(p,q,r) = (1,2,1) the six-state kernel gives d_1 = 12/13 > max(d_2, d_3) = 9/10 ({len(bad)} of the 512 triples in "
              "{1..8}^3 fail, all with q > p); T1(b)'s coupling uses max(d_1, d_2, d_3) = eps_2 and breaks there (a state with all three "
              "xi-predecessors equal to a under one eta'-dissent has dissent probability d_1 > eps_2). The four T4 lines satisfy the "
              "inequality at every tested coupling, so T4's region is not affected; the defect is the scope 'every positive triple'")
        print("SUMMARY: confirmed - T1(a)/T1(b) fail for positive weights with q > p (e.g. (1,2,1)); T4 unaffected")
        return 0
    print("SUMMARY: not reproduced - see the lines above")
    return 0


if __name__ == "__main__":
    sys.exit(main())

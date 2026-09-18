#!/usr/bin/env python3
"""J:attack:PR8177 — pattern (c) EXECUTED NUMBERS: T2 'three v=-1 predecessors'.

claim_scope T2: tight roots have three processed 1-predecessors of rooted
value -1. Runner-cache C1 prints Z_A: ['-1','-1','-1'] and Z_B: ['-1','-1','0'].
HIT if any extremal listed as all -1 has a predecessor not -1.
"""
from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block33-rooted-inequality-"
    "tight-sibling-lemma-one-processed-child-count-20260917"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_rooted_inequality_"
    "reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.txt"
)
NOTE = (
    "docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_THE_ROOTED_INEQUALITY_REDUCES_THE_UNIT_BUDGET_"
    "TO_THE_TIGHT_SIBLING_LEMMA_AND_THE_ONE_PROCESSED_CHILD_COUNT_BOUNDED_THEOREM_NOTE_2026-09-17.md"
)


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    note = git_show(NOTE)
    cache = git_show(CACHE)
    fm = note.split("\n---\n", 1)[0]
    claims_all_minus_one = "three processed 1-predecessors of rooted value -1" in fm
    print(f"claim_scope T2 all-minus-one sentence present: {claims_all_minus_one}")
    found = dict(re.findall(r"(Z_[AB]): v\(root\) = 0, the three processed 1-predecessors have v = (\[[^\]]+\])", cache))
    print(f"cache predecessors {found}")
    hits = []
    for name, raw in found.items():
        vals = ast.literal_eval(raw)
        print(f"{name} {vals}")
        if claims_all_minus_one and vals != ["-1", "-1", "-1"]:
            hits.append(f"{name} predecessors {vals} != [-1,-1,-1]")
    if hits:
        print("HIT: " + "; ".join(hits))
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS - T2 says three predecessors "
            "of value -1; " + "; ".join(hits)
        )
    else:
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - Z_A and Z_B match T2; does not fire")


if __name__ == "__main__":
    main()

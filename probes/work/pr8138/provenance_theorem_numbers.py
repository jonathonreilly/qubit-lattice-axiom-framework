#!/usr/bin/env python3
"""J:provenance:PR8138 — theorem numbers vs runner cache / derivation."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/admissibility-induced-law-block08-z3-formation-law-20260915"
CACHE = "logs/runner-cache/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.txt"

ITEMS = [
    ("48", "Q1a linear extensions"),
    ("1296", "2x2 states / cube marginal"),
    ("1/6", "one-site marginal / r(empty)"),
    ("2000", "B5 cube sample"),
    ("2160/2197", "Q1f third difference (3,1,2)"),
    ("686196/704969", "Q1f third difference (5,2,4)"),
    ("356696849/806187919680", "Q2 TV at (3,1,2)"),
    ("27/110", "c at (3,1,2)"),
    ("81/110", "3c at (3,1,2)"),
    ("10650/63407", "c at (5,2,4)"),
    ("31950/63407", "3c at (5,2,4)"),
    ("5782/30885", "c at (7,3,5)"),
    ("5782/10295", "3c at (7,3,5)"),
    ("1/3", "3c at (2,1,2) / c<1/3 threshold"),
    ("6", "N(000,111) monotone paths"),
    ("33", "checks (executed)"),
    ("26", "mutations"),
]


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        subprocess.run(
            ["git", "fetch", "origin", "physics-loop/admissibility-induced-law-block08-z3-formation-law-20260915"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        r = subprocess.run(
            ["git", "show", f"{BRANCH}:{path}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    if r.returncode != 0:
        raise SystemExit((r.stderr or r.stdout)[:400])
    return r.stdout


def main() -> int:
    cache = git_show(CACHE)
    uncovered = []
    for token, role in ITEMS:
        ok = token in cache
        print(f"{token:28} {'CACHE' if ok else 'MISSING'}  {role}")
        if not ok:
            uncovered.append(f"{token} ({role})")
    if uncovered:
        print("HIT: unsourced " + "; ".join(uncovered[:5]))
        print("SUMMARY: provenance (PR #8138): UNCOVERED " + "; ".join(uncovered[:5]))
        return 0
    print(
        f"SUMMARY: provenance (PR #8138): all {len(ITEMS)} listed theorem "
        "tokens appear in the runner cache (48 extensions, 1296 states, "
        "2160/2197, 27/110, 81/110, TV 356696849/806187919680, 6 paths); "
        "no UNCOVERED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

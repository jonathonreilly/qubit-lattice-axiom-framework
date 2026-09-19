#!/usr/bin/env python3
"""J:provenance:PR8146 — theorem numbers vs runner cache.

Does not re-find the known B4 2:1 majority iff HIT; those numbers are still
CACHE-sourced.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/admissibility-induced-law-block12-strong-coupling-phase-20260915"
CACHE = "logs/runner-cache/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.txt"

ITEMS = [
    ("1000/1033", "S1 at (10,1,2)"),
    ("100/131", "S1 2:1 orthogonal"),
    ("50/71", "S1 2:1 antipodal"),
    ("10/33", "S1 tie"),
    ("211/10211", "epsilon(100) orthogonal"),
    ("35/44", "epsilon(3)"),
    ("21/71", "epsilon(10)"),
    ("216", "triples at (p,1,2)"),
    ("20", "TOTAL PASS"),
    ("0", "TOTAL FAIL"),
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
            ["git", "fetch", "origin", "physics-loop/admissibility-induced-law-block12-strong-coupling-phase-20260915"],
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
        print(f"{token:16} {'CACHE' if ok else 'MISSING'}  {role}")
        if not ok:
            uncovered.append(f"{token} ({role})")
    if uncovered:
        print("HIT: unsourced " + "; ".join(uncovered))
        print("SUMMARY: provenance (PR #8146): UNCOVERED " + "; ".join(uncovered))
        return 0
    print(
        f"SUMMARY: provenance (PR #8146): all {len(ITEMS)} listed theorem "
        "tokens appear in the runner cache (1000/1033, 211/10211, 216 triples, "
        "TOTAL PASS=20); known 2:1 iff HIT not re-claimed; no UNCOVERED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

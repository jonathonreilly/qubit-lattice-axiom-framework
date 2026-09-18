#!/usr/bin/env python3
"""J:attack:PR8172 — pattern (c) EXECUTED NUMBERS: 120-island ratio vs 4.05.

The T2 executed parenthetical says |U| on 120 random islands is at most
4.05 (D+1)^3. The runner-cache prints largest ratio 6671/1728 on 120 islands;
the exact spec prints worst 4.043 on 200 islands.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "c8ae4a4622c1aa924ff6c9b3452021022f20746d"
CACHE = (
    "logs/runner-cache/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_"
    "bounds_2026_09_16.txt"
)
EXA = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block28_exact.out.txt"
NOTE = (
    "docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_"
    "HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md"
)


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    note = git_show(NOTE)
    cache = git_show(CACHE)
    exa = git_show(EXA)
    m_note = re.search(r"on `?120`? random islands[^\n]{0,120}at most `?([0-9.]+)", note)
    stated = Fraction(m_note.group(1)) if m_note else None
    m_run = re.search(r"on 120 random islands \(largest ratio (\d+)/(\d+)\)", cache)
    runner = Fraction(int(m_run.group(1)), int(m_run.group(2))) if m_run else None
    m_spec = re.search(r"on (\d+) random islands: True; worst \|U\|/\(D\+1\)\^3 = ([0-9.]+)", exa)
    spec_n, spec_r = (int(m_spec.group(1)), Fraction(m_spec.group(2))) if m_spec else (None, None)
    print(f"note 120-island cap {stated}")
    print(f"runner 120 islands {runner} = {float(runner) if runner else None}")
    print(f"spec {spec_n} islands worst {spec_r}")
    hits = []
    if stated is None or runner is None:
        hits.append("missing note or runner ratio")
    elif runner != stated and abs(float(runner) - float(stated)) >= 0.05:
        hits.append(f"120-island runner {runner} vs stated {stated}")
        if spec_n == 200 and spec_r is not None and abs(float(spec_r) - float(stated)) < 0.01:
            hits.append(f"stated {stated} tracks spec {spec_n}-island {spec_r}")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - 120-island ratio matches 4.05; does not fire")


if __name__ == "__main__":
    main()

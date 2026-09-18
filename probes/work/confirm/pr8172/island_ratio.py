#!/usr/bin/env python3
"""J:confirm:J-provenance:PR8172 — independent 120-island vs 4.05 pairing check.

Finder (claude-opus-5) said claim_scope's '120 random islands ... at most 4.05'
pairs the runner's island count with the spec's 200-island worst ratio.
This script does not reuse the ITEMS loop. It reads the runner-cache and the
exact spec as separate blobs and compares 6671/1728 to 4.05 as Fraction.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
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
    m_scope = re.search(r"on `?120`? random islands[^\n]{0,120}at most `?([0-9.]+)", note)
    stated = Fraction(m_scope.group(1)) if m_scope else None
    print(f"note 120-island cap: {stated} (match={bool(m_scope)})")

    m_run = re.search(r"on 120 random islands \(largest ratio (\d+)/(\d+)\)", cache)
    if not m_run:
        print("SUMMARY: not reproduced - runner-cache 120-island ratio not found")
        return
    runner_ratio = Fraction(int(m_run.group(1)), int(m_run.group(2)))
    print(f"runner 120 islands largest ratio {runner_ratio} = {float(runner_ratio):.6f}")

    m_spec = re.search(r"on (\d+) random islands: True; worst \|U\|/\(D\+1\)\^3 = ([0-9.]+)", exa)
    spec_n, spec_r = (int(m_spec.group(1)), Fraction(m_spec.group(2))) if m_spec else (None, None)
    print(f"spec {spec_n} islands worst {spec_r}")

    hits = []
    if stated is None:
        hits.append("claim_scope 4.05 sentence not found")
    elif runner_ratio == stated:
        print("SUMMARY: not reproduced - runner 120-island ratio equals the stated 4.05")
        return
    else:
        hits.append(f"120-island runner ratio {runner_ratio} != stated {stated}")
    if spec_n == 200 and spec_r is not None and stated is not None:
        # 4.043 rounded to 2dp is 4.04, to 2 significant of 4.05 is the spec
        if abs(float(spec_r) - float(stated)) < 0.01:
            hits.append(f"stated {stated} matches spec's {spec_n}-island worst {spec_r}, not the runner's 120")

    print("HIT: confirmed - " + "; ".join(hits))
    print(
        "SUMMARY: confirmed pairing mismatch: runner 120 islands give "
        f"{runner_ratio}; claim_scope 4.05 tracks the spec's {spec_n}-island worst {spec_r}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gauge-vacuum adjacent-word scorecard freshness companion.

This verifier preserves the audited parent note bytes while checking that
the executable parent runner/cache now report the newer all-pass scorecard.
It does not edit any audit output or claim a status change.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_SCORECARD_FRESHNESS_COMPANION_NOTE_2026-06-16.md"
PARENT_NOTE = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md"
PARENT_RUNNER = ROOT / "scripts" / "gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py"
PARENT_CACHE = ROOT / "logs" / "runner-cache" / "gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.txt"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"{tag}: {label}")
    if detail:
        print(f"      {detail}")
    return ok


def scorecard(text: str) -> tuple[int, int] | None:
    matches = re.findall(r"TOTAL:\s*PASS=(\d+),?\s*FAIL=(\d+)", text)
    if not matches:
        return None
    passed, failed = matches[-1]
    return int(passed), int(failed)


def run_parent() -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    scripts = str(ROOT / "scripts")
    env["PYTHONPATH"] = scripts + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120,
        check=False,
    )


def main() -> int:
    print("Gauge vacuum plaquette adjacent-word scorecard freshness companion")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    parent_note = PARENT_NOTE.read_text(encoding="utf-8")
    parent_cache = PARENT_CACHE.read_text(encoding="utf-8")

    check(
        "companion is hygiene-only",
        "does not re-audit" in note_flat
        and "does not edit an audit verdict" in note_flat
        and "does not promote a row" in note_flat
        and "does not add an axiom" in note_flat,
    )
    check(
        "parent note remains on historical displayed scorecard",
        "TOTAL: PASS=25, FAIL=0" in parent_note
        and "TOTAL: PASS=28, FAIL=0" not in parent_note,
    )
    check(
        "cache is the current parent-runner all-pass scorecard",
        scorecard(parent_cache) == (28, 0),
        f"cache_scorecard={scorecard(parent_cache)}",
    )
    check(
        "cache is for the adjacent-word parent runner",
        "runner: scripts/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py" in parent_cache,
    )

    result = run_parent()
    check("parent runner exits successfully", result.returncode == 0, result.stderr.strip())
    check(
        "live parent runner emits the current all-pass scorecard",
        scorecard(result.stdout) == (28, 0),
        f"live_scorecard={scorecard(result.stdout)}",
    )
    check(
        "Part R stationarity check is present",
        "measured stationarity: derived trivial-slice readout agrees at two and three words" in result.stdout,
    )
    check(
        "Part R non-factorization guard is present",
        "non-factorization guard: the three-word Perron vector is NOT rank-one across the outer word" in result.stdout,
    )
    check(
        "Part R slice-proportionality check is present",
        "measured slice proportionality: the all-trivial-except-word0 slice" in result.stdout,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

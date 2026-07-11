#!/usr/bin/env python3
"""Verify the historical 2026-07-04 decision has no current premise effect."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    runner = ROOT / "scripts" / "admitted_input_registry_tier_a_boundary_check.py"
    completed = subprocess.run([sys.executable, str(runner)], cwd=ROOT, check=False)
    if completed.returncode:
        return completed.returncode

    historical = (ROOT / "docs" / "TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md").read_text(encoding="utf-8")
    required = [
        "Premise weight:** none",
        "former governance-only premise channel is withdrawn",
        "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
        "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
    ]
    failures = 0
    for phrase in required:
        passed = phrase in historical
        print(f"[{'PASS' if passed else 'FAIL'}] historical note: {phrase}")
        failures += not passed
    print(f"HISTORICAL NOTE: PASS={len(required) - failures} FAIL={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

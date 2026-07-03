#!/usr/bin/env python3
"""Legacy Lorentz-derived runner compatibility wrapper.

The current registered Lorentz runner is ``frontier_lorentz_violation.py``.
This file keeps the older missing path executable by verifying that the live
bounded companion note names the replacement runner and that the replacement
runner still passes its cubic-harmonic and SME checks.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def main() -> int:
    print("Lorentz derived legacy-runner compatibility")
    print("=" * 72)

    note = read("docs/LORENTZ_VIOLATION_DERIVED_NOTE.md")
    check(
        "live Lorentz note names the current replacement runner",
        "**Script:** `scripts/frontier_lorentz_violation.py`" in note
        and "registered runner" in note,
    )
    check(
        "live Lorentz note is a bounded companion, not retained flagship",
        "bounded companion only" in note
        and "Not on the\nretained flagship claim surface" in note,
    )
    check(
        "live Lorentz note keeps the cubic-lattice symmetry statement",
        "SO(3,1) broken to O_h" in note and "all 48 O_h elements" in note,
    )

    runner = ROOT / "scripts/frontier_lorentz_violation.py"
    result = subprocess.run(
        [sys.executable, str(runner)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = result.stdout + result.stderr
    check(
        "current replacement runner exits successfully",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    check(
        "replacement runner retains cubic-harmonic identity check",
        "Cubic-harmonic identity check: PASS" in output,
    )
    check(
        "replacement runner completes the Lorentz/SME experiment",
        "EXPERIMENT COMPLETE" in output and "Lorentz" in output and "SME" in output,
    )

    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Probe the DM-eta G1 Fierz-channel narrative correction note."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DM_ETA_G1_FIERZ_CHANNEL_NARRATIVE_CORRECTION_NOTE_2026-05-27.md"
SUPPORT_RUNNER = "scripts/frontier_dm_eta_g1_coleman_weinberg_2026_05_06.py"


@dataclass(frozen=True)
class CheckResult:
    label: str
    passed: bool
    detail: str


def run_support() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, SUPPORT_RUNNER],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120,
        check=False,
    )


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    checks: list[CheckResult] = []

    def expect(label: str, condition: bool, detail: str) -> None:
        checks.append(CheckResult(label=label, passed=condition, detail=detail))

    expect("claim type is bounded theorem", "**Claim type:** bounded_theorem" in note, "audit row stays bounded")
    expect(
        "runner metadata names this probe",
        "scripts/dm_eta_g1_fierz_channel_narrative_correction_probe.py" in note,
        "audit parser can attach the narrative-correction verifier",
    )
    expect(
        "status authority remains independent",
        "**Status authority:** independent audit lane only." in note,
        "branch does not write audit verdicts",
    )
    expect(
        "narrative correction is scoped",
        "does NOT change the arithmetic outcome" in note
        and "does NOT introduce\nany new mechanism" in note
        and "SINGLET channel" in note,
        "note corrects channel attribution without changing the mass result",
    )
    expect(
        "adjoint-channel overclaim is explicitly removed",
        "removes the load-bearing narrative claim" in note
        and "adjoint Fierz channel" in note
        and "incompatible with\nthe runner's own Test 12 output" in note,
        "note keeps the contradiction visible",
    )

    completed = run_support()
    support_text = completed.stdout + completed.stderr
    expect("support runner exits cleanly", completed.returncode == 0, f"returncode={completed.returncode}")
    expect(
        "support runner passes all tests",
        "PASS = 17, FAIL = 0" in support_text,
        "Coleman-Weinberg support runner reports 17/17",
    )
    expect(
        "support runner confirms singlet channel",
        "Point-coupling Sigma = C_F*I lives on Fierz SINGLET channel" in support_text
        and "claimed adjoint-channel selection of the scalar self-energy" in support_text,
        "runner output supports the narrative correction",
    )
    expect(
        "support runner keeps bounded status",
        "STATUS: BOUNDED SUPPORT" in support_text
        and "Downstream status remains independent-audit" in support_text
        and "authority; the parent lane still carries inherited bounded inputs" in support_text,
        "no status promotion is claimed",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("DM-ETA G1 FIERZ CHANNEL NARRATIVE CORRECTION PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: bounded narrative-correction verifier only; no DM-eta status promotion.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Probe the Newton derivation open gate.

This runner verifies that ``docs/NEWTON_DERIVATION_NOTE.md`` stays an open
gate and then executes the bounded Principle-3 bridge and supporting
equivalence/additivity diagnostics named by the note.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "NEWTON_DERIVATION_NOTE.md"

EQUIV = "scripts/equivalence_principle_harness.py"
ADD3D = "scripts/composite_source_additivity_harness.py"
ADD2D = "scripts/composite_source_additivity_2d_cross_family.py"
TOP4 = "scripts/newton_derivation_top4_bridge_runner.py"


@dataclass(frozen=True)
class CheckResult:
    label: str
    passed: bool
    detail: str


def run_python(script: str, timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, script],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    checks: list[CheckResult] = []

    def expect(label: str, condition: bool, detail: str) -> None:
        checks.append(CheckResult(label=label, passed=condition, detail=detail))

    expect("claim type is open gate", "**Claim type:** open_gate" in note, "Newton row stays open_gate")
    expect(
        "runner metadata names this probe",
        "scripts/newton_derivation_open_gate_probe.py" in note,
        "audit parser can attach the open-gate verifier",
    )
    expect(
        "open residual gate remains explicit",
        "external-field generator-invariant inertial-mass step" in note
        and "persistent compact-object family" in note,
        "the remaining gate is the external-field compact-object equivalence step",
    )
    expect(
        "architecture-independent closure is disclaimed",
        "does **not** claim architecture-" in note
        and "persistent-pattern inertial mass" in note
        and "must not be cited as a closed Newtonian derivation" in note,
        "note keeps Newtonian derivation closure out of scope",
    )
    expect(
        "machine-local link targets removed from touched note",
        "/Users/jonreilly/Projects/Physics/" not in note,
        "artifact links are repo-relative",
    )

    equiv = run_python(EQUIV, timeout=20)
    equiv_text = equiv.stdout + equiv.stderr
    expect("equivalence harness exits cleanly", equiv.returncode == 0, f"returncode={equiv.returncode}")
    expect(
        "equivalence harness preserves bounded read",
        "Global amplitude scaling cancels exactly" in equiv_text
        and "Packet shape can still matter" in equiv_text,
        "amplitude-level equivalence remains bounded, not persistent mass closure",
    )

    add3d = run_python(ADD3D, timeout=25)
    add3d_text = add3d.stdout + add3d.stderr
    expect("3D additivity harness exits cleanly", add3d.returncode == 0, f"returncode={add3d.returncode}")
    expect(
        "3D additivity harness preserves bounded read",
        "Valley-linear should be close to additive" in add3d_text
        and "Spent-delay should deviate" in add3d_text,
        "3D weak-field test-particle additivity remains bounded",
    )

    add2d = run_python(ADD2D, timeout=20)
    add2d_text = add2d.stdout + add2d.stderr
    expect("2D additivity harness exits cleanly", add2d.returncode == 0, f"returncode={add2d.returncode}")
    expect(
        "2D additivity harness preserves bounded read",
        "second-family cross-check" in add2d_text
        and "not a persistent-pattern inertial-mass theorem" in add2d_text,
        "2D cross-family additivity does not close the persistent-pattern gate",
    )

    top4 = run_python(TOP4, timeout=75)
    top4_text = top4.stdout + top4.stderr
    expect("top4 bridge runner exits cleanly", top4.returncode == 0, f"returncode={top4.returncode}")
    expect(
        "top4 bridge gates pass",
        all(token in top4_text for token in ("PERSISTENCE", "EXTENSIVITY", "STABILITY"))
        and "BRIDGE_ADMISSIBLE = True" in top4_text,
        "top4 self-sourcing bridge remains admissible",
    )
    expect(
        "top4 bridge keeps external-field gate open",
        "not a new persistent-pattern equivalence-principle" in top4_text
        and "remaining open question is the equivalence-principle test" in top4_text,
        "bridge does not close the final external-field generator-invariance step",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("NEWTON DERIVATION OPEN-GATE PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: open-gate verifier only; no retained Newtonian derivation.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

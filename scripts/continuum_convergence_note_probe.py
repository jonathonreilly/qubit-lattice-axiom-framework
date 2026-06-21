#!/usr/bin/env python3
"""Probe the bounded continuum-convergence note boundary.

This runner is intentionally a note-boundary verifier. It checks that the
continuum note stays bounded, that it does not promote the exploratory
`1/L^(d-1)` branch to a continuum theorem, and that the two cited dependency
runners still reproduce their finite-scope evidence.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CONTINUUM_CONVERGENCE_NOTE.md"


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

    expect(
        "claim type is bounded",
        "**Claim type:** bounded_theorem" in note,
        "continuum note remains a bounded_theorem row",
    )
    expect(
        "runner metadata names this probe",
        "scripts/continuum_convergence_note_probe.py" in note,
        "audit parser can attach the note-boundary verifier",
    )
    expect(
        "old 3D 1/L branch is rejected",
        "does **not** survive refinement" in note,
        "the note preserves the failed-refinement boundary",
    )
    expect(
        "new kernel is only a candidate",
        all(token in note for token in ("`1/L^(d-1)`", "**strong", "empirical persistence candidate**"))
        and "still **not** a derived theorem" in note
        and "**not** a promoted top-level canonical lane" in note,
        "candidate wording does not become a continuum theorem",
    )
    expect(
        "transfer norm remains under reconciliation",
        "transfer-norm selection is still **under reconciliation**" in note,
        "the local transfer-norm discriminator is not promoted",
    )
    expect(
        "distance-law direction is not Newtonian",
        "currently AWAY from Newtonian, not toward it" in note,
        "the note keeps the distance-law warning visible",
    )
    expect(
        "closure claims are explicitly banned",
        all(
            phrase in note
            for phrase in (
                "kernel = `1/L^(d-1)` is derived from the axioms",
                "transfer norm uniquely selects `p = d - 1`",
                "Newtonian gravity is now established",
                "the continuum theorem is complete",
            )
        ),
        "the note lists the overclaims it must not be used to make",
    )
    expect(
        "no machine-local link targets remain",
        "/Users/jonreilly/Projects/Physics/" not in note,
        "links are repo-relative for audit portability",
    )
    expect(
        "no uppercase retained status marker remains",
        "RETAINED" not in note,
        "touched note avoids bare status-authority wording",
    )

    tail = run_python("scripts/lattice_3d_l2_tail_stats.py", timeout=90)
    tail_text = tail.stdout + tail.stderr
    expect(
        "tail-stats dependency exits cleanly",
        tail.returncode == 0,
        f"returncode={tail.returncode}",
    )
    expect(
        "tail-stats dependency scorecard passes",
        "SCORECARD PASS=32 FAIL=0" in tail_text,
        "finite width-6/width-8 tail-fit verifier remains reproducible",
    )
    expect(
        "tail-stats dependency keeps finite boundary",
        "BOUNDARY: finite no-barrier tail-fit comparison only; no asymptotic 1/r^2 closure." in tail_text,
        "dependency does not claim asymptotic closure",
    )

    transfer = run_python("scripts/lattice_kernel_transfer_norm_probe.py", timeout=30)
    transfer_text = transfer.stdout + transfer.stderr
    expect(
        "transfer-norm dependency exits cleanly",
        transfer.returncode == 0,
        f"returncode={transfer.returncode}",
    )
    expect(
        "transfer-norm ranking keeps p=1.5 closest to stable",
        "1. p=1.50" in transfer_text and "2. p=2.00" in transfer_text,
        "local transfer-norm discriminator remains a warning against unique p=2 promotion",
    )
    expect(
        "transfer-norm output is explicitly marginality-ranked",
        "Measured-norm marginality ranking" in transfer_text,
        "dependency output is the bounded comparison named by the note",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("CONTINUUM CONVERGENCE NOTE PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: bounded note verifier only; no continuum theorem or kernel-selection promotion.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

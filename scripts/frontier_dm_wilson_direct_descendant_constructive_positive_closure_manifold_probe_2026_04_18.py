#!/usr/bin/env python3
"""Probe the DM Wilson positive-closure manifold support note.

The source note depends on two existing artifacts: the local manifold theorem
runner and the Krawczyk-interval certificate runner. This wrapper gives the
audit ledger a single primary runner while keeping both component checks
visible and preserving the support-only boundary.
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "DM_WILSON_DIRECT_DESCENDANT_CONSTRUCTIVE_POSITIVE_CLOSURE_MANIFOLD_THEOREM_NOTE_2026-04-18.md"
)
CERT = ROOT / "outputs" / "dm_wilson_constructive_positive_closure_manifold_certificate_2026-04-18.json"
THEOREM_RUNNER = (
    "scripts/frontier_dm_wilson_direct_descendant_constructive_positive_closure_manifold_theorem_2026_04_18.py"
)
CERT_RUNNER = (
    "scripts/frontier_dm_wilson_direct_descendant_constructive_positive_closure_manifold_certificate_2026_04_18.py"
)


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
        "the source row stays support/bounded, not a flagship closeout",
    )
    expect(
        "runner metadata names this probe",
        "scripts/frontier_dm_wilson_direct_descendant_constructive_positive_closure_manifold_probe_2026_04_18.py"
        in note,
        "audit parser can attach the wrapper runner",
    )
    expect(
        "component runners remain named",
        THEOREM_RUNNER in note and CERT_RUNNER in note,
        "both theorem and Krawczyk certificate artifacts are visible",
    )
    expect(
        "fixed-kernel boundary is explicit",
        "precomputed transport kernel" in note
        and "fixed exact numerical object" in note
        and "not the underlying transport" in note
        and "construction" in note,
        "certificate is scoped to the fixed e-independent transport kernel",
    )
    expect(
        "final closeout is not claimed",
        "the final DM flagship closeout" in note
        and "What this does not establish" in note,
        "note preserves the open-selector boundary",
    )

    theorem = run_python(THEOREM_RUNNER, timeout=45)
    theorem_text = theorem.stdout + theorem.stderr
    expect(
        "manifold theorem runner exits cleanly",
        theorem.returncode == 0,
        f"returncode={theorem.returncode}",
    )
    expect(
        "manifold theorem runner scorecard passes",
        "SUMMARY: PASS=24 FAIL=0" in theorem_text,
        "local exact-closure family witness remains reproducible",
    )
    expect(
        "manifold theorem keeps non-isolated boundary",
        "locally non-isolated" in theorem_text and "needs a new independent selector condition" in theorem_text,
        "runner reports support for an open selector condition, not closure",
    )

    cert = run_python(CERT_RUNNER, timeout=75)
    cert_text = cert.stdout + cert.stderr
    expect(
        "Krawczyk certificate runner exits cleanly",
        cert.returncode == 0,
        f"returncode={cert.returncode}",
    )
    expect(
        "Krawczyk certificate scorecard passes",
        "SUMMARY: PASS=10 FAIL=0" in cert_text,
        "certificate sign-change, derivative, and contraction checks pass",
    )
    expect(
        "Krawczyk certificate bottom line is present",
        "Krawczyk-interval regular-root certificate established for the base point" in cert_text,
        "regular-root certificate is the support artifact",
    )

    if CERT.exists():
        payload = json.loads(CERT.read_text(encoding="utf-8"))
        cert_kind = payload.get("certificate_kind")
        produced_by = payload.get("produced_by")
    else:
        cert_kind = None
        produced_by = None
    expect(
        "certificate JSON exists with expected provenance",
        CERT.exists() and cert_kind == "krawczyk_interval_regular_root_with_davis_kahan_eigenvector_perturbation"
        and produced_by == CERT_RUNNER,
        "certificate file records the Krawczyk/Davis-Kahan provenance",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("DM WILSON POSITIVE-CLOSURE MANIFOLD SUPPORT PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: support for local non-isolation on a fixed kernel; no final selector or DM flagship closeout.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Probe the mass-spectrum derived bounded lane.

This wrapper keeps ``docs/MASS_SPECTRUM_DERIVED_NOTE.md`` parser-visible as a
bounded theorem entry and executes the four validation runners named by the
note. The quark packet runner replays the down-type and up-type phases, so the
four commands cover the note's five-phase accounting.
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MASS_SPECTRUM_DERIVED_NOTE.md"

RUNNERS = [
    (
        "quark packet",
        "scripts/frontier_quark_mass_ratio_review.py",
        46,
        (
            "Packet status: review-ready quark mass-ratio bundle",
            "up-type extension is live but remains bounded",
        ),
    ),
    (
        "charged lepton cross-reference",
        "scripts/frontier_mass_ratio_lepton_sector.py",
        11,
        (
            "does NOT reproduce",
            "charged-lepton sector enters as bounded pin",
        ),
    ),
    (
        "neutrino sector",
        "scripts/frontier_neutrino_mass_derived.py",
        19,
        (
            "solar gap Dm^2_21 NOT closed by diagonal benchmark",
            "What Phase 4 BOUNDS but does NOT retain",
        ),
    ),
    (
        "cosmology cascade",
        "scripts/frontier_cosmology_from_mass_spectrum.py",
        23,
        (
            "eta remains imported on the live cosmology surface",
            "R = 5.48 via Sommerfeld",
        ),
    ),
]


@dataclass(frozen=True)
class CheckResult:
    label: str
    passed: bool
    detail: str


def run_python(script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, script],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120,
        check=False,
    )


def last_total(text: str) -> tuple[int, int] | None:
    matches = re.findall(r"TOTAL:\s+PASS=(\d+),\s+FAIL=(\d+)", text)
    if not matches:
        return None
    passed, failed = matches[-1]
    return int(passed), int(failed)


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    checks: list[CheckResult] = []

    def expect(label: str, condition: bool, detail: str) -> None:
        checks.append(CheckResult(label=label, passed=condition, detail=detail))

    expect("claim type is bounded theorem", "**Claim type:** bounded_theorem" in note, "audit row stays bounded")
    expect(
        "runner metadata names this probe",
        "scripts/mass_spectrum_derived_bounded_probe.py" in note,
        "audit parser can attach the bounded verifier",
    )
    expect(
        "status authority remains independent",
        "**Status authority:** independent audit lane only." in note,
        "branch does not write audit verdicts",
    )
    expect(
        "machine-local plan path removed",
        "/Users/" not in note,
        "touched note is repo-relative / source-contained",
    )
    expect(
        "full-closure denials remain explicit",
        "full quark mass spectrum is retained" in note
        and "charged lepton hierarchy is derived" in note
        and "`eta` is derived on the live cosmology surface" in note,
        "note preserves cannot-claim boundaries",
    )
    expect(
        "open/imported blockers remain explicit",
        "`eta = 6.12e-10`" in note
        and "not yet retained" in note
        and "`alpha_GUT`" in note
        and "bounded" in note,
        "eta and alpha_GUT are not hidden as derivations",
    )
    expect(
        "validation total refreshed",
        "**Total: `PASS=99 FAIL=0`**" in note,
        "note matches current validation runners",
    )

    aggregate_pass = 0
    for label, script, expected_pass, required_markers in RUNNERS:
        completed = run_python(script)
        text = completed.stdout + completed.stderr
        total = last_total(text)
        expect(f"{label} runner exits cleanly", completed.returncode == 0, f"returncode={completed.returncode}")
        expect(
            f"{label} runner total is current",
            total == (expected_pass, 0),
            f"observed={total}, expected=({expected_pass}, 0)",
        )
        expect(
            f"{label} boundary markers present",
            all(marker in text for marker in required_markers),
            "runner output preserves bounded/open/imported read",
        )
        if total is not None:
            aggregate_pass += total[0]

    expect(
        "aggregate validation total is current",
        aggregate_pass == 99,
        f"aggregate_pass={aggregate_pass}",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("MASS SPECTRUM DERIVED BOUNDED PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: bounded verifier only; no full mass-spectrum retention.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Probe the frontier extension lane-opening note boundary.

This runner keeps the lane-opening note as an open gate. It verifies that the
note is planning-only and then executes the existing first-artifact/boundary
scripts for the teleportation and signed-gravity lanes.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md"

TELEPORTATION_PROTOCOL = "scripts/frontier_teleportation_protocol.py"
TELEPORTATION_RESOURCE = "scripts/frontier_teleportation_resource_from_poisson.py"
TELEPORTATION_CHANNEL = "scripts/frontier_teleportation_causal_channel.py"
SIGNED_GRAVITY_STATUS = "scripts/frontier_signed_gravity_response_lane_status.py"


@dataclass(frozen=True)
class CheckResult:
    label: str
    passed: bool
    detail: str


def run_python(script: str, timeout: int = 45) -> subprocess.CompletedProcess[str]:
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
        "claim type is open gate",
        "**Claim type:** open_gate" in note,
        "lane opening stays an open_gate row",
    )
    expect(
        "runner metadata names this probe",
        "scripts/frontier_extension_lane_opening_probe_2026_04_25.py" in note,
        "audit parser can attach the lane-opening boundary verifier",
    )
    expect(
        "note is planning-only",
        "planning only, not a science claim" in note
        and "not part of the manuscript claim surface" in note
        and "No lane opened here is promoted by rhetoric" in note,
        "the note does not itself claim theorem, prediction, or publication status",
    )
    expect(
        "all three lanes remain named",
        all(token in note for token in ("native teleportation", "chronology protection", "signed gravitational response")),
        "frontier extension scope remains the three accepted bounded lanes",
    )
    expect(
        "promotion gates remain explicit",
        "Promotion requires passing its first" in note
        and "acceptance gates and adding a corresponding theorem/protocol note" in note
        and "lane opened for bounded work; planning only, not a claim surface" in note,
        "the note keeps promotion out of the lane-opening artifact",
    )

    protocol = run_python(TELEPORTATION_PROTOCOL)
    protocol_text = protocol.stdout + protocol.stderr
    expect("teleportation protocol exits cleanly", protocol.returncode == 0, f"returncode={protocol.returncode}")
    expect(
        "teleportation protocol gates pass",
        all(
            token in protocol_text
            for token in (
                "native taste encoding: PASS",
                "Bell projectors: PASS",
                "random-state fidelity: PASS",
                "Bob pre-message input-independence: PASS",
                "causal record channel: PASS",
            )
        ),
        "first-artifact taste teleportation gates remain reproducible",
    )

    resource = run_python(TELEPORTATION_RESOURCE)
    resource_text = resource.stdout + resource.stderr
    expect("teleportation resource exits cleanly", resource.returncode == 0, f"returncode={resource.returncode}")
    expect(
        "teleportation resource summary passes",
        "SUMMARY PASS=9 FAIL=0" in resource_text,
        "Poisson/CHSH finite extraction core remains bounded and passing",
    )
    expect(
        "teleportation resource keeps open bridge",
        "native preparation/readout/apparatus bridge is open" in resource_text,
        "resource runner does not close native apparatus/readout",
    )

    channel = run_python(TELEPORTATION_CHANNEL)
    channel_text = channel.stdout + channel.stderr
    expect("teleportation channel exits cleanly", channel.returncode == 0, f"returncode={channel.returncode}")
    expect(
        "teleportation channel gates pass",
        all(
            token in channel_text
            for token in (
                "explicit not derived record channel: PASS",
                "no early delivery: PASS",
                "post-delivery correction: PASS",
                "Bob pre-delivery no-signaling: PASS",
            )
        ),
        "explicit classical record channel remains causal",
    )

    signed = run_python(SIGNED_GRAVITY_STATUS)
    signed_text = signed.stdout + signed.stderr
    expect("signed-gravity status exits cleanly", signed.returncode == 0, f"returncode={signed.returncode}")
    expect(
        "signed-gravity status scorecard passes",
        "TOTAL: PASS=20, FAIL=0" in signed_text,
        "signed-response boundaries remain reproducible",
    )
    expect(
        "signed-gravity physical sector remains unretained",
        "SIGNED_GRAVITY_PHYSICAL_SECTOR_NOT_RETAINED" in signed_text,
        "lane status stays a boundary artifact, not physical-sector promotion",
    )

    passed = sum(result.passed for result in checks)
    failed = len(checks) - passed

    print("FRONTIER EXTENSION LANE-OPENING PROBE")
    print()
    for result in checks:
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.label} ({result.detail})")
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    print("BOUNDARY: lane-opening/open-gate verifier only; no theorem, prediction, or retained status.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

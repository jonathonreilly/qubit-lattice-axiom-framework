#!/usr/bin/env python3
"""Guard the archived h=0.125 failure-diagnosis firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "h0125-unverifiable-numerical-diagnostics-2026-04-30"
NOTE = ARCHIVE / "H0125_FAILURE_DERIVATION.md"
README = ARCHIVE / "README.md"

REQUIRED_NOTE = [
    "Historical h=0.125 Failure-Diagnosis Packet (Retracted)",
    "historical / diagnostic and retired as evidence",
    "not a retained h=0.125 failure derivation",
    "not the current live h=0.125 status",
    "Historical root-cause diagnosis (retracted)",
    "Historical per-layer probability-loss table (retracted)",
    "Historical AWAY/SNR explanation (retracted)",
]

REQUIRED_README = [
    "historical / diagnostic and retired as evidence",
    "not a retained h=0.125 failure theorem",
    "current computable h=0.125 audit lane",
]

BANNED = [
    "# Why h=0.125 Fails: Retained Derivation",
    "## Root cause",
    "### 1. Boundary leakage accelerates with h",
    "### 2. Beam width exceeds half the lattice at h=0.125",
    "### 3. Per-layer probability loss compounds exponentially",
    "### 4. The AWAY result is noise",
    "P_det = (retention)^nl. At h=0.125: 0.727^241 ~ 10^-33.",
    "accept h=0.25 as the finest confirmed lattice spacing",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    for needle in REQUIRED_NOTE:
        require(needle in note, f"note missing required text: {needle}")
    for needle in REQUIRED_README:
        require(needle in readme, f"README missing required text: {needle}")
    for needle in BANNED:
        require(needle not in note, f"old live h0125 phrase remains: {needle}")

    print("PASS: h0125 archive firewall holds")


if __name__ == "__main__":
    main()

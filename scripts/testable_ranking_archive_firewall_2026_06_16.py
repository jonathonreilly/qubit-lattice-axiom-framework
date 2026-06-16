#!/usr/bin/env python3
"""Guard the archived testable-ranking firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "testable-ranking-stale-wrappers-2026-04-30"

FILES = {
    "README.md": [
        "retained rankings",
        "brainstorming records only",
    ],
    "TESTABLE_PREDICTIONS_MAP_NOTE.md": [
        "Historical Testable Predictions Map (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not a retained current map of testable predictions",
        "Historical ranking snapshot (retracted)",
        "Historical bottom line (retracted)",
    ],
    "MOONSHOT_OTHER_TESTABLES_NOTE.md": [
        "Historical Moonshot Other Testables Note (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not a retained non-diamond testable ranking",
        "Historical ranking snapshot (retracted)",
        "Historical final verdict (retracted)",
    ],
}

BANNED = [
    "# Testable Predictions Map",
    "# Moonshot Other Testables Note",
    "This note is a compact, adversarial map of the best current testable",
    "- Already retained:",
    "- Retained connection:",
    "## Current ranking",
    "## Top Non-Diamond Testable",
    "## Final Verdict",
    "The best non-diamond moonshot is",
    "cleanest current path to an outside experiment",
    "best non-diamond testable:",
    "\"the best non-diamond testable\"",
    "strongest retained phase-sensitive observable",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for name, required in FILES.items():
        text = (ARCHIVE / name).read_text(encoding="utf-8")
        for needle in required:
            require(needle in text, f"{name}: missing required text: {needle}")
        for needle in BANNED:
            require(needle not in text, f"{name}: old live ranking phrase remains: {needle}")

    print("PASS: testable-ranking archive firewall holds")


if __name__ == "__main__":
    main()

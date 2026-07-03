#!/usr/bin/env python3
"""Guard the archived topology-pivot session summary against live claims."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "session-summary-stale-aggregates-2026-04-30"
    / "SESSION_SUMMARY_2026-04-01_TOPOLOGY.md"
)

REQUIRED_PHRASES = [
    "# Historical Topology Pivot Session Summary (Retracted)",
    "## 2026-06-16 archive firewall",
    "historical session history only",
    "not retained evidence for a shared gravity/decoherence graph-family architecture",
    "not a closed emergence result",
    "not authority that any topology-pivot lane is retained",
    "Future use must split any surviving idea into auditable claim notes",
    "dated roadmap and index of scripts/logs",
    "## Historical architecture story (not retained evidence)",
    "None of these bullets is retained by this archived summary",
    "## Historical listed results (not locked)",
    "This archived summary does not retain that diagnosis as a theorem.",
    "## Historical lessons listed by the memo",
    "## Historical files listed by the session",
]

FORBIDDEN_PHRASES = [
    "# Session Summary: Topology Pivot",
    "## The architecture story",
    "## Locked results",
    "Both gravity and decoherence work on the same graph family",
    "The sign and mean shift look retained",
    "What remains retained is not a single ceiling value",
]


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    collapsed = normalize(text)

    failures: list[str] = []
    for phrase in REQUIRED_PHRASES:
        if normalize(phrase) not in collapsed:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in FORBIDDEN_PHRASES:
        if normalize(phrase) in collapsed:
            failures.append(f"forbidden live-claim phrase remains: {phrase}")

    print("Topology session-summary archive firewall")
    print("=" * 72)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: archived topology session summary is demoted and fenced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

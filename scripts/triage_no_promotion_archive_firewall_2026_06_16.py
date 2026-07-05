#!/usr/bin/env python3
"""Guard the archived triage no-promotion memo against live authority wording."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "process-triage-unreproducible-state-2026-04-30"
    / "TRIAGE_NO_PROMOTION_NOTE.md"
)

REQUIRED_PHRASES = [
    "# Historical Triage No-Promotion Process Memo (Retracted)",
    "## 2026-06-16 archive firewall",
    "historical process history only",
    "not retained evidence about the current working stack",
    "not an audited no-promotion result",
    "not authority about science promotion status",
    "without preserving a reproducible manifest of draft artifacts, runners, logs, and promotion criteria",
    "Future use must start from a fresh reproducible triage manifest.",
    "## Historical scope (not a reproducible input set)",
    "That question is not re-decided here.",
    "## Historical conclusion (not audit authority)",
    "not a retained no-promotion theorem",
    "## Archived verdict boundary",
    "not live framework authority",
]

FORBIDDEN_PHRASES = [
    "# Triage No-Promotion Note",
    "The answer is **no**.",
    "## Review-Safe Conclusion",
    "No draft in the current dirty stack clearly clears the retained bar",
    "## Final Verdict",
    "**no-promotion**",
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
            failures.append(f"forbidden live-authority phrase remains: {phrase}")

    print("Triage no-promotion archive firewall")
    print("=" * 72)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: archived triage memo is demoted and fenced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

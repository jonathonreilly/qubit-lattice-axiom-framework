#!/usr/bin/env python3
"""Guard the archived IF program-closing firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "if-program-unverifiable-closing-2026-04-30" / "IF_PROGRAM_CLOSING_NOTE.md"
SESSION_SUMMARY = ROOT / "archive_unlanded" / "session-summary-stale-aggregates-2026-04-30" / "SESSION_SUMMARY_2026-04-01_TOPOLOGY.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.exists(), f"missing expected file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    archive = read(ARCHIVE)
    summary = read(SESSION_SUMMARY)

    require("**Status:** RETRACTED 2026-04-30" in archive, "archive retraction status is missing")
    require("historical / diagnostic and retired as evidence" in archive, "archive is not explicitly retired as evidence")
    require("planning/triage memory only" in archive, "archive planning/triage boundary is missing")
    require("Historical retained-language section (retracted)" in archive, "retained-language section is not retracted")
    require("Historical old-lane closure section (retracted)" in archive, "old closure section is not retracted")
    require("Historical topology-pivot section (retracted)" in archive, "topology pivot section is not retracted")
    require("## What was retained" not in archive, "archive still exposes live retained heading")
    require("## What closed on the old lane" not in archive, "archive still exposes live closure heading")
    require("## Decision" not in archive, "archive still exposes live decision heading")

    require("not canonical closure" in summary, "session summary still treats IF archive as canonical closure")

    print("PASS: IF program-closing archive firewall holds")


if __name__ == "__main__":
    main()

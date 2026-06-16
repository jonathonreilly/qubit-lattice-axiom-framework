#!/usr/bin/env python3
"""Guard the archived DM A-BCC basin-enumeration boundary repair."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = (
    ROOT
    / "archive_unlanded"
    / "dm-abcc-finite-search-salvage-2026-04-30"
    / "DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    text = ARCHIVE.read_text(encoding="utf-8")
    flat = " ".join(text.split())

    require("**Status:** RETRACTED 2026-04-30" in text, "retraction status missing")
    require("historical / diagnostic and retired as evidence" in text, "retired-evidence boundary missing")
    require("not a live authority for an exhaustive DM A-BCC basin-enumeration theorem" in text, "live-authority denial missing")
    require("finite multistart/random-sampling scan" in text, "finite-search safe boundary missing")
    require("did not prove that no narrow basin lies between seeds" in flat, "narrow-basin caveat missing")
    require("worst-case Lipschitz or eigenvalue-gap bound" in flat, "certified-bound caveat missing")
    require("deterministic far-field exclusion" in text, "far-field caveat missing")
    require("Historical executive summary (retracted)" in text, "historical executive heading missing")
    require("Historical theorem statement (retracted)" in text, "historical theorem marker missing")
    require("Historical completeness target (not certified here)" in text, "historical completeness heading missing")
    require("Historical certificate ingredients (heuristic, not exhaustive proof)" in text, "historical certificate heading missing")
    require("Historical theorem boundary (retracted and narrowed)" in text, "narrowed theorem-boundary heading missing")
    require("## 0. Executive summary" not in text, "archive still exposes live executive heading")
    require("## 1. What \"completeness\" means here" not in text, "archive still exposes live completeness heading")
    require("## 6. What the theorem is and is not" not in text, "archive still exposes live theorem-boundary heading")
    require(
        "**Is:** A computational-certificate exhaustiveness theorem" not in text,
        "archive still exposes theorem-grade is-claim",
    )

    print("PASS: DM A-BCC basin archive firewall holds")


if __name__ == "__main__":
    main()

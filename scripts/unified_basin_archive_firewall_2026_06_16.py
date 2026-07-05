#!/usr/bin/env python3
"""Guard the archived unified-basin freeze packet against live-claim wording."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "unified-basin-signed-source-salvage-2026-04-30"
    / "UNIFIED_BASIN_FREEZE_NOTE.md"
)

REQUIRED_PHRASES = [
    "# Historical Unified Basin Freeze Packet (Retracted)",
    "## 2026-06-16 archive firewall",
    "historical diagnostic material only",
    "not a unified two-coupling basin result",
    "not authority that the signed-source and complex-action surfaces share one nearby grown-family neighborhood",
    "the signed-source non-label basin currently has a separate support route",
    "the fixed-row kernel-vs-gravity comparison is a separate diagnostic",
    "the actual complex grown-basin runner does not support this wrapper's unified-basin claim",
    "## Historical control-gate tables (retracted as unified-basin evidence)",
    "### Historical complex-action fixed-row table (not a basin)",
    "## Historical frozen claim (retracted)",
    "The old unified-basin claim is retracted.",
    "Does not claim a unified two-coupling basin",
]

FORBIDDEN_PHRASES = [
    "# Unified Basin Freeze: Both Basins Pass Zero/Neutral Controls",
    "## Frozen claim",
    "One retained grown connectivity family",
    "supports both signed-source and complex-action couplings across a small nearby basin",
    "with exact zero and neutral controls passing cleanly",
    "The narrow review-safe statement",
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

    print("Unified basin archive firewall")
    print("=" * 72)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: archived unified-basin packet is demoted and fenced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

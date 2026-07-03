#!/usr/bin/env python3
"""Guard the archived three-family card firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "archive_unlanded"
    / "family-card-incomplete-artifacts-2026-04-30"
    / "THREE_FAMILY_CARD_NOTE.md"
)

BANNED = [
    "# Three Independent Grown Families: 9/9 Properties Match",
    "produce quantitatively identical physics on all 9 measurable properties",
    "but the observables are geometry-independent.",
    "This is evidence that the physics emerges",
]

REQUIRED = [
    "Historical Three-Family Card Packet (Retracted)",
    "historical / diagnostic and retired as evidence",
    "authority for geometry-independence",
    "Family 3 distance alpha",
    "is not populated and no runner/log artifact verifies the card",
    "Historical claim boundary (retracted and narrowed)",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    text = NOTE.read_text(encoding="utf-8")
    for needle in REQUIRED:
        require(needle in text, f"missing required firewall text: {needle}")
    for needle in BANNED:
        require(needle not in text, f"old live family-card phrase remains: {needle}")

    print("PASS: family-card archive firewall holds")


if __name__ == "__main__":
    main()

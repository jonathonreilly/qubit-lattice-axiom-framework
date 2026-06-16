#!/usr/bin/env python3
"""Guard the archived Shapiro bridge/scaling firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "shapiro-static-renderers-and-failed-bridges-2026-04-30"

FILES = {
    "SHAPIRO_COMPLEX_INTERACTION_NOTE.md": [
        "historical / diagnostic and retired as evidence",
        "They do not establish a retained Shapiro phase-lag observable",
        "Historical supplied phase-lag table (retracted)",
        "Historical final verdict (retracted)",
    ],
    "SHAPIRO_DIAMOND_BRIDGE_NOTE.md": [
        "historical / diagnostic and retired as evidence",
        "does not establish a retained Shapiro phase lag",
        "Historical bridge vocabulary (open)",
        "Historical narrow conclusion (retracted)",
    ],
    "SHAPIRO_DIAMOND_FREQUENCY_BRIDGE_NOTE.md": [
        "historical / diagnostic and retired as evidence",
        "not a retained Shapiro scaling law",
        "Historical bridge translation proposal (open)",
        "Historical final verdict (retracted)",
    ],
    "SHAPIRO_FIVE_FAMILY_PORTABILITY_NOTE.md": [
        "historical / diagnostic and retired as evidence",
        "does not establish five-family Shapiro portability",
        "Failed control gate",
        "Historical final verdict (retracted)",
    ],
    "SHAPIRO_SCALING_DIRECT_REPLAY_NOTE.md": [
        "historical / diagnostic and retired as evidence",
        "establish retained source-strength",
        "Historical static replay body (retracted)",
        "Historical final verdict (retracted)",
    ],
    "SHAPIRO_SCALING_NOTE.md": [
        "Historical Shapiro Scaling Pointer (Retracted)",
        "live support or closure note",
        "Historical closure read (retracted)",
    ],
}

BANNED = [
    "## Final Verdict",
    "## Closure Read",
    "## Exact Controls",
    "## Retained Phase",
    "## Retained Scaling",
    "retained positive:",
    "passes cleanly",
    "The retained phase lag is already portable",
    "The retained causal phase lag survives",
    "the retained causal phase lag survives",
    "cleanest lab-facing discriminator in the retained causal package",
    "the Shapiro scaling lane can close",
    "the retained s, b, and k laws",
    "The repo can defensibly say:",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for name, required in FILES.items():
        path = ARCHIVE / name
        text = path.read_text(encoding="utf-8")
        require("**Status:** RETRACTED 2026-04-30" in text or "**Status:** RETIRED 2026-06-16" in text, f"{name}: retired/retracted status missing")
        for needle in required:
            require(needle in text, f"{name}: missing required firewall text: {needle}")
        for needle in BANNED:
            require(needle not in text, f"{name}: old live-claim phrase remains: {needle}")

    print("PASS: Shapiro archive firewall holds")


if __name__ == "__main__":
    main()

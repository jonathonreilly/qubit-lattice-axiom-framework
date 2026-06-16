#!/usr/bin/env python3
"""Guard the archived portability-extension firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "portability-stale-extension-wrappers-2026-04-30"

FILES = {
    "README.md": [
        "historical / diagnostic and retired as",
        "editorial portability worklists only",
        "retained cross-family package extensions",
    ],
    "PORTABLE_CARD_EXTENSION_NOTE.md": [
        "Historical Portable Card Extension Packet (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not a retained portable-package extension",
        "Historical final verdict (retracted)",
    ],
    "PORTABLE_PACKAGE_EXTENSION_NOTE.md": [
        "Historical Portable Package Extension Packet (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not a retained cross-family fixed-field package extension",
        "Historical final verdict (retracted)",
    ],
}

BANNED = [
    "# Portable Card Extension Note",
    "# Portable Package Extension Note",
    "## Final Verdict",
    "retained narrow extension positive",
    "retained narrow comparison positive",
    "The retained three-family card stays clean",
    "The retained rows say:",
    "survives across the retained structured families",
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
            require(needle not in text, f"{name}: old live portability phrase remains: {needle}")

    print("PASS: portability-extension archive firewall holds")


if __name__ == "__main__":
    main()

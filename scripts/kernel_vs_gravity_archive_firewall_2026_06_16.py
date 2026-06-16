#!/usr/bin/env python3
"""Guard the archived kernel-vs-gravity boundary repair."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = (
    ROOT
    / "archive_unlanded"
    / "kernel-gravity-conflation-2026-04-30"
    / "KERNEL_VS_GRAVITY_NOTE.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    text = ARCHIVE.read_text(encoding="utf-8")

    require("**Status:** RETRACTED 2026-04-30" in text, "retraction status missing")
    require("historical / diagnostic and retired as evidence" in text, "retired-evidence boundary missing")
    require("not a live authority for kernel-generic detector-escape suppression" in text, "live-authority denial missing")
    require("local per-link attenuation" in text, "local-factor distinction missing")
    require("does not imply total detector-escape suppression" in text, "detector-escape caveat missing")
    require("gamma = 0.5" in text, "safe gamma=0.5 detector boundary missing")
    require("gamma = 0.2" in text, "safe gamma=0.2 crossover boundary missing")
    require("Historical result section (retracted)" in text, "historical result heading missing")
    require("Historical kernel-generic absorption section (retracted)" in text, "historical kernel heading missing")
    require("Historical claim boundary (retracted and narrowed)" in text, "narrowed claim-boundary heading missing")
    require("## Result" not in text, "archive still exposes live Result heading")
    require("## Claim boundary" not in text, "archive still exposes live claim-boundary heading")
    require(
        "any f > 0 with gamma > 0 suppresses amplitude" not in text,
        "archive still exposes old detector-escape overclaim",
    )

    print("PASS: kernel-vs-gravity archive firewall holds")


if __name__ == "__main__":
    main()

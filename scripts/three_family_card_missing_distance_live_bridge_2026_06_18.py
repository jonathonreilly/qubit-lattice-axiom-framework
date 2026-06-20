#!/usr/bin/env python3
"""Verifier for the three-family card missing-distance live bridge."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded/family-card-incomplete-artifacts-2026-04-30/THREE_FAMILY_CARD_NOTE.md"
DISTANCE_NOTE = ROOT / "docs/DISTANCE_LAW_PRESERVING_THIRD_FAMILY_NOTE.md"
BRIDGE_NOTE = ROOT / "docs/THREE_FAMILY_CARD_MISSING_DISTANCE_LIVE_BRIDGE_NOTE_2026-06-18.md"
RUNNER = ROOT / "scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py"
CACHE = ROOT / "logs/runner-cache/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.txt"
FIREWALL = ROOT / "scripts/family_card_archive_firewall_2026_06_16.py"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}" + (f": {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"[FAIL] {label}" + (f": {detail}" if detail else ""))


def read(path: Path) -> str:
    check(f"path exists: {path.relative_to(ROOT)}", path.exists())
    return path.read_text(encoding="utf-8")


def cache_field(cache: str, field: str) -> str | None:
    m = re.search(rf"^{re.escape(field)}: (.+)$", cache, re.MULTILINE)
    return m.group(1).strip() if m else None


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    print("=" * 88)
    print("THREE FAMILY CARD MISSING DISTANCE LIVE BRIDGE")
    print("=" * 88)

    archive = read(ARCHIVE)
    distance_note = read(DISTANCE_NOTE)
    bridge = read(BRIDGE_NOTE)
    runner = read(RUNNER)
    cache = read(CACHE)
    firewall = read(FIREWALL)

    for phrase in [
        "RETRACTED 2026-04-30",
        "archived `audited_failed` / retracted",
        "Family 3 distance alpha",
        "Historical claim boundary (retracted and narrowed)",
        "THREE_FAMILY_CARD_MISSING_DISTANCE_LIVE_BRIDGE_NOTE_2026-06-18.md",
    ]:
        check(f"archive boundary phrase: {phrase}", phrase in archive)

    for phrase in [
        "Distance Law Preserving Third Family Note",
        "drift = 0.50",
        "restore = 0.90",
        "zero control: exact",
        "distance tail: `alpha = -1.150`",
        "does **not** imply a universal theorem",
        "does **not** repair the archived three-family 9/9 card",
    ]:
        check(f"distance note phrase: {phrase}", phrase in distance_note)

    for phrase in [
        "source-side partial re-audit bridge",
        "specific missing Family 3 distance-alpha slot",
        "all-nine-property recomputation",
        "does not edit audit results",
        "geometry independence",
        "Full card repair still requires",
        "retained or retained-bounded effective status",
    ]:
        check(f"bridge boundary phrase: {phrase}", phrase in bridge)

    for phrase in [
        "AUDIT_TIMEOUT_SEC = 1800",
        "TARGET_FAMILY = (0.50, 0.90)",
        "DISTANCE_BS = [5, 6, 7, 8, 10]",
        "SEEDS = [0, 1, 2, 3, 4, 5]",
        "sign_ok",
        "tail_ok",
        "_summarize_family",
        "write-log",
    ]:
        check(f"runner substantive marker: {phrase}", phrase in runner)

    check("firewall checks archive retirement", "family-card archive firewall holds" in firewall)
    check("cache points to distance runner", cache_field(cache, "runner") == "scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py")
    check("cache exits cleanly", cache_field(cache, "exit_code") == "0")
    check("cache status ok", cache_field(cache, "status") == "ok")
    check("cache sha matches runner", cache_field(cache, "runner_sha256") == sha256(RUNNER))

    for phrase in [
        "DISTANCE LAW PRESERVING THIRD FAMILY",
        "family=(drift=0.50, restore=0.90)",
        "sign gate: PASS",
        "tail gate: PASS",
        "+1.764e-04",
        "-1.764e-04",
        "alpha': -1.1501244371653223",
        "tail_r2': 0.9713658329628312",
        "'toward': 5",
        "'tail_ok': True",
    ]:
        check(f"cache result phrase: {phrase}", phrase in cache)

    check("archive still marks Family 3 old table incomplete", "(not yet)" in archive)
    check("bridge does not claim all-nine repair", "does not provide the all-nine-property recomputation" in archive)
    check("bridge expected summary matches", "PASS=51 FAIL=0" in bridge)

    print("=" * 88)
    print(f"SUMMARY: THREE FAMILY CARD MISSING DISTANCE LIVE BRIDGE PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

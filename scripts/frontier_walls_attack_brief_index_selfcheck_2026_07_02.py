#!/usr/bin/env python3
"""Trivial consistency check for the 2026-07-02 walls-attack meta brief."""

from pathlib import Path


BRIEF = Path("docs/WALLS_ATTACK_20260702_ADJUDICATION_BRIEF_META_NOTE_2026-07-02.md")

CAMPAIGN_INDEX = [
    "#4816 block01 carrier",
    "#4817 block02",
    "#4818 block03",
    "#4820 block05",
    "#4821 block06",
    "#4823 block08",
    "#4826 block11",
    "#4819 block04 action",
    "#4824 block09",
    "#4825 block10",
    "#4828 block13",
    "#pending block14",
    "#4822 block07 moduli",
    "#4827 block12",
]

LADDER = ["R*", "D-totality", "w-supplier", "CTX-match"]


def check(label: str, condition: bool) -> tuple[int, int]:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label}")
    return (1 if condition else 0, 1)


def main() -> int:
    if not BRIEF.exists():
        print(f"FAIL: missing {BRIEF}")
        print("PASS/TOTAL: 0/1")
        return 1

    text = BRIEF.read_text(encoding="utf-8")
    passed = 0
    total = 0

    for item in CAMPAIGN_INDEX:
        p, t = check(f"campaign index contains {item}", item in text)
        passed += p
        total += t

    for item in LADDER:
        p, t = check(f"ladder contains {item}", item in text)
        passed += p
        total += t

    p, t = check("claim type is meta", "**Claim type:** meta" in text)
    passed += p
    total += t
    p, t = check("boundary denies audit prediction", "predicts no audit outcome" in text)
    passed += p
    total += t

    print(f"PASS/TOTAL: {passed}/{total}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Scope guard for the color/generation Z3 inequivalence note."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "COLOR_GENERATION_INDEPENDENT_Z3_STRUCTURES_2026-06-05.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")

    check(
        "title is abstract rather than physical-SM",
        text.startswith("# Abstract color-carrier and generation-candidate Z3 actions are inequivalent"),
    )
    check(
        "claim type is bounded abstract inequivalence",
        "**Claim type:** bounded theorem / abstract algebraic inequivalence." in text,
    )
    check(
        "statement excludes physical SM color/generation/product bridge",
        "does **not** by\nitself identify the color carrier with physical SM color" in text
        and "or prove a physical `3 x 3` product-label\nstructure" in text,
    )
    check(
        "missing physical bridge theorems are enumerated",
        "physical SM color" in text
        and "physical generations" in text.replace("\n   ", " ")
        and "product/commuting-label bridge" in text,
    )
    check(
        "proof step avoids SM product-label conclusion",
        "**No physical-label conclusion.**" in text
        and "without the three bridge theorems listed above" in text,
    )
    check(
        "scope boundary keeps only abstract Z3 inequivalence",
        "This shows only that the cited abstract carriers are **inequivalent Z3\nrepresentations**"
        in text,
    )
    check(
        "old physical conclusion is absent",
        "exactly as in the SM" not in text
        and "reproducing the SM" not in text
        and "the SM requires" not in text,
    )
    check(
        "retained/audit status remains delegated to the ledger",
        "independent audit lane only" in text
        and "effective audit statuses are left to the ledger" in text,
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

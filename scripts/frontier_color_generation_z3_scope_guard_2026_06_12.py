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
    flat = " ".join(text.split())

    check(
        "title is abstract rather than physical-SM",
        text.startswith("# Abstract color-carrier and generation-carrier Z3 actions are inequivalent"),
    )
    check(
        "claim type uses canonical bounded_theorem metadata",
        "**Claim type:** bounded_theorem" in text,
    )
    check(
        "claim boundary excludes physical bridge and audit verdict",
        "abstract representation-theory boundary on the two cited carrier actions" in flat
        and "does not derive the physical SM color carrier" in flat
        and "does not identify `hw=1` orbit labels with physical generations" in flat
        and "does not set an audit verdict" in flat,
    )
    check(
        "statement keeps only abstract carrier inequivalence",
        "the two native Z3 actions are character-inequivalent" in flat
        and "cannot be the same Z3 representation" in flat
        and "abstract carrier-level independence/no-identification result" in flat,
    )
    check(
        "physical interpretation is routed to separate bridge theorems",
        "physical Standard Model color-versus-generation reading requires separate carrier/readout bridge theorems"
        in flat
        and "does not by itself prove that a physical fermion carries an independently identified SM color label"
        in flat,
    )
    check(
        "proof checks character and module inequivalence",
        "differ at the two non-identity elements" in flat
        and "`chi_omega` appears with multiplicity `3` in the color rep" in flat
        and "but `1` in the generation rep" in flat
        and "every intertwiner has rank `<= 1 < 3`" in flat,
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
        and "effective audit statuses are left to the ledger" in flat,
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

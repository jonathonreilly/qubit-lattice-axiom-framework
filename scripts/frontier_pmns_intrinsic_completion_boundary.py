#!/usr/bin/env python3
"""PMNS intrinsic-completion-boundary compatibility runner.

The old intrinsic-completion runner path was removed when the PMNS lane was
superseded.  This replacement keeps the path executable by checking the current
PMNS boundary: the current stack has zero selector amplitude, the right-polar
section is sheet-even, and the archived intrinsic-completion note preserves the
one residual sheet-fixing datum boundary.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0

SUPERSEDED_EWSB_NOTES = (
    "docs/PMNS_EWSB_RESIDUAL_Z2_HERMITIAN_CORE_NOTE.md",
    "docs/PMNS_EWSB_WEAK_AXIS_Z3_SEED_NOTE.md",
    "docs/PMNS_EWSB_RESIDUAL_Z2_SPECTRAL_PRIMITIVE_NOTE.md",
    "docs/PMNS_EWSB_ALIGNMENT_NONFORCING_NOTE.md",
    "docs/PMNS_EWSB_BREAKING_SLOT_NONREALIZATION_NOTE.md",
)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def main() -> int:
    print("PMNS intrinsic completion boundary compatibility")
    print("=" * 72)

    selector = read("docs/PMNS_SELECTOR_CURRENT_STACK_ZERO_LAW_NOTE.md")
    polar = read("docs/PMNS_RIGHT_POLAR_SECTION_NOTE.md")
    quadratic = read("docs/PMNS_BRANCH_CONDITIONED_QUADRATIC_SHEET_CLOSURE_NOTE.md")
    archive = read(
        "archive_unlanded/pmns-publication-state-supersession-2026-05-01/"
        "PMNS_INTRINSIC_COMPLETION_BOUNDARY_NOTE.md"
    )

    check(
        "current PMNS selector stack remains zero",
        "`a_sel,current = 0`" in selector
        and "no future extension can realize `a_sel != 0`" in selector,
    )
    check(
        "right polar section gives only a sheet-even positive representative",
        "`Y_+(H) := H^(1/2)`" in polar
        and "sheet-even" in polar
        and "sheet-fixing information" in polar
        and "This note does **not** derive" in polar,
    )
    check(
        "branch-conditioned quadratic closure keeps the residual branch condition",
        "if `a_sel > 0`" in quadratic
        and "if `a_sel < 0`" in quadratic
        and "same Hermitian matrix `H_nu`" in quadratic,
    )
    check(
        "archived intrinsic-completion note records the one-sheet boundary",
        "Hermitian data law" in archive
        and "sheet-fixing datum" in archive
        and "coefficient-level closure remains open at one residual sheet-fixing datum" in archive,
    )

    absent = [rel for rel in SUPERSEDED_EWSB_NOTES if not (ROOT / rel).exists()]
    check(
        "superseded EWSB residual-chain notes remain absent from current docs",
        len(absent) == len(SUPERSEDED_EWSB_NOTES),
        f"absent={len(absent)}/{len(SUPERSEDED_EWSB_NOTES)}",
    )

    print("Result: compatibility with supersession boundary; no PMNS closure promotion.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

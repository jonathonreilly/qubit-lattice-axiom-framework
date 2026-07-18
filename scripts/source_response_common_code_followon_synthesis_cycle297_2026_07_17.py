#!/usr/bin/env python3
"""Cycle-297 synthesis for moving response, fixed-source composition, and M2 catch-up.

Cold-run the three independent artifacts and enforce the boundary that they do
not yet form one physical source/response compiler.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SOURCE_RESPONSE_COMMON_CODE_FOLLOWON_SYNTHESIS_CYCLE297_NOTE_2026-07-17.md"
)

ROUTES = (
    (
        "moving carried stationary mode",
        ROOT / "scripts/stationary_dressed_carried_source_relative_mode_2026_07_17.py",
        14,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
    ),
    (
        "two fixed reservoirs",
        ROOT / "scripts/two_fixed_reservoir_stationary_composition_kernel_2026_07_17.py",
        23,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
    ),
    (
        "physical Cycle-269 catch-up",
        ROOT / "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
        8,
        re.compile(r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)"),
    ),
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "actual moving carried update",
        "basis-spanning",
        "contact-localized",
        "contact-deleted",
        "additive two-source shifted profile",
        "conjugate reciprocity",
        "genuinely complex",
        "728 nonzero",
        "antisymmetric lambda=1 compatibility member",
        "bounded physical catch-up gate component",
        "one physical source/response compiler",
        "not physical energy",
        "not gravity",
        "not a clock",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate status: fail for the candidate broad negative; do not ship it",
        "no shared obstruction was identified",
        "no axiom pressure was established",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins route boundaries, ledgers, and N1--N8", not missing, missing)


def cold_routes() -> None:
    rows = []
    for name, path, expected_pass, pattern in ROUTES:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        match = pattern.search(completed.stdout)
        observed = tuple(int(item) for item in match.groups()) if match else None
        rows.append(
            {
                "route": name,
                "returncode": completed.returncode,
                "observed": observed,
                "expected": (expected_pass, 0),
            }
        )
    check(
        "all three independent route runners pass at reviewed totals",
        all(
            row["returncode"] == 0 and row["observed"] == row["expected"]
            for row in rows
        ),
        rows,
    )


def boundary_guards() -> None:
    moving = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "STATIONARY_DRESSED_CARRIED_SOURCE_RELATIVE_MODE_NOTE_2026-07-17.md"
    )
    pair = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "TWO_FIXED_RESERVOIR_STATIONARY_COMPOSITION_KERNEL_NOTE_2026-07-17.md"
    )
    physical = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_STAGGERED_RESERVOIR_CATCHUP_NOTE_2026-07-17.md"
    )
    check(
        "moving mode distinguishes a stationary eigenpair from a Green-tail match",
        "stationary dressed eigenmode of the actual full carried update" in moving
        and "not numerically identified with the three green shapes" in moving
        and "another branch, momentum sector" in moving,
    )
    check(
        "fixed pair distinguishes composition from physical gravity",
        "additive two-source shifted profile" in pair
        and "conjugate reciprocity" in pair
        and "genuinely complex" in pair
        and "728 nonzero" in pair
        and "not physical energy" in pair
        and "not gravity" in pair,
    )
    check(
        "physical catch-up distinguishes a bounded gate from a state compiler",
        "bounded physical gate component" in physical
        and "not an assembled encoded-state macrostep" in physical
        and "multiparticle collision schedule or a larger auxiliary" in physical,
    )


def main() -> int:
    note_contract()
    cold_routes()
    boundary_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())

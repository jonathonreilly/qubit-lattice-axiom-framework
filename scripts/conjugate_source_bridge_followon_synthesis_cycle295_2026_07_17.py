#!/usr/bin/env python3
"""Cycle 295 synthesis controls for the conjugate-source bridge follow-on.

Cold-run four independent constructive probes and pin their compatibility and
semantic boundaries.  This runner deliberately does not splice different
matter codes or name an excitation ledger energy/gravity.
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
    "CONJUGATE_SOURCE_BRIDGE_FOLLOWON_SYNTHESIS_CYCLE295_NOTE_2026-07-17.md"
)

ROUTES = (
    (
        "site-local reservoir",
        ROOT / "scripts/local_conjugate_reservoir_source_field_ledger_repair_2026_07_17.py",
        20,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
    ),
    (
        "carried internal species",
        ROOT / "scripts/carried_internal_species_source_field_ledger_repair_2026_07_17.py",
        19,
        re.compile(r"SUMMARY\s+\{'pass':\s*(\d+),\s*'fail':\s*(\d+)\}"),
    ),
    (
        "full hard-core history",
        ROOT / "scripts/full_hard_core_higher_field_history_route_2_2026_07_17.py",
        16,
        re.compile(r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)"),
    ),
    (
        "two-slice off-diagonal ledger",
        ROOT / "scripts/two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17.py",
        15,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
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
        "not one common update",
        "site-local reservoir",
        "carried internal species",
        "genuine multi-mediator history",
        "dimensionless off-diagonal branch-coordinate impulse ledger",
        "not physical energy",
        "not a gravitational source",
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
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins scope, dependency ledgers, and N1--N8", not missing, missing)


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
        observed = tuple(int(value) for value in match.groups()) if match else None
        rows.append(
            {
                "route": name,
                "returncode": completed.returncode,
                "observed": observed,
                "expected": (expected_pass, 0),
            }
        )
    check(
        "all four independent route runners pass at reviewed totals",
        all(
            row["returncode"] == 0 and row["observed"] == row["expected"]
            for row in rows
        ),
        rows,
    )


def incompatibility_guards() -> None:
    site = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "LOCAL_CONJUGATE_RESERVOIR_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md"
    )
    carried = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md"
    )
    hard_core = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "FULL_HARD_CORE_HIGHER_FIELD_HISTORY_ROUTE_2_NOTE_2026-07-17.md"
    )
    branch = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "TWO_SLICE_OFFDIAGONAL_CONTACT_RESERVOIR_WORK_LEDGER_NOTE_2026-07-17.md"
    )
    check(
        "site-local and carried source repairs remain explicitly distinct codes",
        "site-local, not carried" in site
        and "new direct hard-core physical allocation" in carried
        and "not the cycle-269 even-car code" in carried,
    )
    check(
        "the higher-field route quantifies the register missing from its own law",
        "exact missing register quantified" in hard_core
        and "no physical local register in this route carries it" in hard_core,
    )
    check(
        "the off-diagonal ledger remains a factorized branch-coordinate impulse, not energy",
        "telescoping identity for the factorized update" in branch
        and "not physical energy" in branch
        and "neither a conservation theorem nor a noether theorem" in branch,
    )


def main() -> int:
    note_contract()
    cold_routes()
    incompatibility_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())

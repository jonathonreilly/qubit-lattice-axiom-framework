#!/usr/bin/env python3
"""Cycle-301 synthesis for the reference-relative state and contact bridge."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_STATE_CONTACT_BRIDGE_SYNTHESIS_CYCLE301_NOTE_2026-07-17.md"
)
ROUTES = (
    (
        "reference-relative localized state lift",
        ROOT / "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
        7,
    ),
    (
        "same-code Cycle-230 contact",
        ROOT / "scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py",
        9,
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
        "reference-relative",
        "fixed +++ wilson sector",
        "exact two-column",
        "e g_coarse = g_physical e",
        "e c_coarse = c_physical e",
        "fifteen pair projectors",
        "identical-fermion",
        "not an assembled full-hilbert macrostep",
        "coarse-only one-particle mass firewall",
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
    check("the synthesis pins both intertwiners, scope, ledger, and N1--N8", not missing, missing)


def cold_routes() -> None:
    rows = []
    for name, path, expected in ROUTES:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        match = re.search(r"SUMMARY:\s+(\d+)\s+passed,\s+(\d+)\s+failed", completed.stdout)
        observed = tuple(int(item) for item in match.groups()) if match else None
        rows.append(
            {
                "route": name,
                "returncode": completed.returncode,
                "observed": observed,
                "expected": (expected, 0),
            }
        )
    check(
        "both independently reviewed physical routes pass",
        all(
            row["returncode"] == 0 and row["observed"] == row["expected"]
            for row in rows
        ),
        rows,
    )


def boundary_guards() -> None:
    lift = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md"
    )
    contact = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_LOCAL_CONTACT_INTERTWINER_NOTE_2026-07-17.md"
    )
    check(
        "the state lift is exact but reference-relative and restricted",
        "exact isometry" in lift
        and "restricted physical operator word" in lift
        and "supplied reference" in lift
        and "not two distinguishable matter species" in lift,
    )
    check(
        "the contact is physical and keeps its coarse-only mass boundary",
        "fifteen pair projectors" in contact
        and "contact-block intertwiner" in contact
        and "coarse one-particle control" in contact
        and "not an assembled contact-plus-stream update" in contact,
    )
    check(
        "the joined package keeps coin, coherent position, full Fock, and semantics open",
        "coherent position" in lift
        and "actual six-mode" in lift
        and "full-fock" in lift
        and "not gravity" in contact,
    )


def main() -> int:
    note_contract()
    cold_routes()
    boundary_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())

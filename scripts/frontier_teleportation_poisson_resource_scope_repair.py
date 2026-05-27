#!/usr/bin/env python3
"""Scope-boundary repair checker for the Poisson/CHSH teleportation row.

The repair does not prove the native preparation/readout theorem. It verifies
that the row is framed as an open gate, that the old stale minimal-axiom link is
gone, and that the original bounded diagnostic still runs on the restricted
small surfaces.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
NOTE = DOCS / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"
ORIGINAL = ROOT / "scripts" / "frontier_teleportation_resource_from_poisson.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def main() -> int:
    print("Teleportation Poisson resource scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger["rows"]
    this_row = rows["teleportation_resource_from_poisson_note"]

    print()
    print("A. Boundary wording")
    print("-" * 72)
    check("note declares open_gate type", "**Type:** open_gate" in note)
    check(
        "note says this is not a deterministic-resource theorem",
        "not as a\ndeterministic-resource theorem" in note,
    )
    check(
        "note preserves small-surface diagnostic value",
        "small-surface Poisson/CHSH calculation is\nstill useful" in note
        and "high ideal\nstate-teleportation fidelity" in note,
    )
    check(
        "note leaves native carrier derivation open",
        "No sentence in this note asserts that the last taste bit has been derived" in note
        and "missing native preparation/readout theorem remains" in note,
    )
    check(
        "note does not claim matter or FTL teleportation",
        "does not claim matter teleportation" in note
        and "faster-than-light transport" in note,
    )

    print()
    print("B. Dependency hygiene")
    print("-" * 72)
    check(
        "stale minimal axiom link removed",
        "MINIMAL_AXIOMS_2026-05-03.md" not in note,
    )
    check(
        "current canonical axiom premise cited",
        "MINIMAL_AXIOMS_2026-05-20.md" in note,
    )
    retained_adjacent = [
        "teleportation_poisson_resource_sweep_note",
        "teleportation_resource_fidelity_note",
        "teleportation_measurement_record_note",
        "teleportation_apparatus_dynamics_closure_note",
    ]
    for claim_id in retained_adjacent:
        status = rows[claim_id].get("effective_status")
        check(
            f"{claim_id} is retained_bounded",
            status == "retained_bounded",
            str(status),
        )

    print()
    print("C. Current ledger row")
    print("-" * 72)
    check(
        "row claim_type is open_gate",
        this_row.get("claim_type") == "open_gate",
        str(this_row.get("claim_type")),
    )
    check(
        "row is not retained before repair audit",
        this_row.get("effective_status") != "retained",
        str(this_row.get("effective_status")),
    )
    check(
        "row records the native preparation/readout blocker",
        "native preparation/readout" in (this_row.get("notes_for_re_audit_if_any") or "")
        or "native preparation/readout" in (this_row.get("chain_closure_explanation") or ""),
    )

    print()
    print("D. Original bounded diagnostic")
    print("-" * 72)
    result = subprocess.run(
        [
            sys.executable,
            str(ORIGINAL.relative_to(ROOT)),
            "--trials",
            "16",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check(
        "original runner exits cleanly",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    check("original runner covers null control", "Case: 1d_null" in output)
    check("original runner covers 1d Poisson case", "Case: 1d_poisson_chsh" in output)
    check("original runner covers 2d Poisson case", "Case: 2d_poisson_chsh" in output)
    check(
        "original runner reports diagnostic-only postselection",
        "Postselected branches" in output and "diagnostics only" in output,
    )
    check(
        "original runner does not promote the result",
        "independent hardening before promotion" in output
        and "not by itself a teleportation resource derivation" in output,
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: row is ready for re-audit as an open_gate bounded diagnostic.")
        return 0
    print("VERDICT: teleportation Poisson scope repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

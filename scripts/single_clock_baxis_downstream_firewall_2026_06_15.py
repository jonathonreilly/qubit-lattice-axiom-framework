#!/usr/bin/env python3
"""Downstream B-AXIS wording firewall for single-clock consumers.

The single-clock source is axis-conditional: B-AXIS supplies the blocked time
step, evolution axis/transfer construction, and no-second-clock exclusion.
It no longer derives temporal-axis uniqueness from RP. This verifier checks the
highest-risk downstream stale phrases repaired by this branch.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "docs" / "A3_R2_REVIEW_CONFIRMS_EXHAUSTION_NOTE_2026-05-08_r2hr.md",
    ROOT / "docs" / "A3_ROUTE2_SINGLE_CLOCK_C3_OBSTRUCTION_NOTE_2026-05-08_r2.md",
    ROOT / "docs" / "PLANCK_ORIENTATION_PRINCIPLE_BOUNDED_NOTE_2026-05-10_planckP3.md",
    ROOT / "docs" / "STAGGERED_DIRAC_PHYSICAL_SPECIES_DIRECT_THEOREM_NOTE_2026-05-07.md",
]
STALE = [
    "Single-clock codimension-1 evolution; uniqueness of temporal RP axis",
    "Temporal direction is the unique RP-admissible reflection axis",
    "unique RP-admissible reflection axis induces a preferred spatial",
    "temporal direction \u03c4 is the **unique** lattice direction admitting RP",
    "no spatial axis admits RP",
    "(S3) of the single-clock theorem produces a NEGATIVE statement",
    "retained per [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`]",
    "proposed_retained`, audit-pending; PR 418",
]
PASS = 0
FAIL = 0
EXPECTED_PASS = 16


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def main() -> int:
    print("Single-clock downstream B-AXIS firewall")
    print("=" * 72)
    bodies = {path: path.read_text(encoding="utf-8") for path in TARGETS}
    combined = "\n".join(bodies.values())

    for path in TARGETS:
        body = bodies[path]
        check(f"{path.name} names B-AXIS", "B-AXIS" in body)
        check(f"{path.name} marks single-clock conditional", "conditional" in body.lower())

    for stale in STALE:
        check(f"stale phrase absent: {stale[:48]}", stale not in combined)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if PASS != EXPECTED_PASS:
        print(f"ERROR: expected {EXPECTED_PASS} PASS checks, got {PASS}.")
        return 1
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Exact re-audit runner for the universal GR complement canonicalization row."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
NOTE = DOCS / "UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md"
CLAIM_ID = "universal_gr_complement_canonical_note"

FRAME_BLOCKER_ID = "universal_gr_polarization_frame_bundle_blocker_note"
SO3_ID = "universal_gr_so3_isotypic_orbit_flat_narrow_theorem_note_2026-05-10"

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


def pi_a1(h: sp.Matrix) -> sp.Matrix:
    trace = h[1, 1] + h[2, 2] + h[3, 3]
    return sp.diag(h[0, 0], trace / 3, trace / 3, trace / 3)


def energy(h: sp.Matrix, d0: sp.Rational, ds: sp.Rational) -> sp.Expr:
    weights = [d0, ds, ds, ds]
    total = sp.Integer(0)
    for i in range(4):
        for j in range(4):
            total += h[i, j] ** 2 / (weights[i] * weights[j])
    return sp.simplify(total)


def main() -> int:
    print("Universal GR complement canonicalization re-audit")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger["rows"]
    row = rows[CLAIM_ID]

    print()
    print("A. Source-note wiring")
    print("-" * 72)
    check("note declares bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check(
        "note points at this primary runner",
        "**Primary runner:** `scripts/universal_gr_complement_canonical_reaudit.py`" in note,
    )
    check(
        "note cites retained frame-bundle blocker",
        "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md" in note,
    )
    check(
        "note cites retained SO3 orbit-flat theorem",
        "UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md" in note,
    )
    check(
        "note keeps full-GR closure out of scope",
        "does not close full GR" in note and "orbit-canonical, not\nsection-canonical" in note,
    )

    print()
    print("B. Retained one-hop authorities")
    print("-" * 72)
    frame_status = rows[FRAME_BLOCKER_ID].get("effective_status")
    so3_status = rows[SO3_ID].get("effective_status")
    check("frame-bundle blocker is retained_bounded", frame_status == "retained_bounded", str(frame_status))
    check("SO3 orbit-flat theorem is retained", so3_status == "retained", str(so3_status))
    check("pre-repair row was audited_conditional", row.get("audit_status") == "audited_conditional", str(row.get("audit_status")))

    print()
    print("C. Exact SO(3) witness")
    print("-" * 72)
    # h has one shift component. A 90-degree spatial rotation moves it from
    # x to y while preserving the isotropic complement energy.
    h = sp.zeros(4)
    h[0, 1] = sp.Integer(1)
    h[1, 0] = sp.Integer(1)
    rz = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ]
    )
    h_rot = sp.simplify(rz.T * h * rz)
    a1 = pi_a1(h)
    a1_rot = pi_a1(h_rot)
    perp = h - a1
    perp_rot = h_rot - a1_rot
    d0 = sp.Rational(2, 1)
    ds = sp.Rational(5, 1)
    e_a1 = energy(a1, d0, ds)
    e_a1_rot = energy(a1_rot, d0, ds)
    e_perp = energy(perp, d0, ds)
    e_perp_rot = energy(perp_rot, d0, ds)

    check("rotation is orthogonal", sp.simplify(rz.T * rz - sp.eye(4)) == sp.zeros(4))
    check("A1 projector is fixed", sp.simplify(a1_rot - a1) == sp.zeros(4), f"A1={a1}")
    check("complement coordinates move", sp.simplify(perp_rot - perp) != sp.zeros(4), f"perp_rot={perp_rot}")
    check("A1 energy is unchanged", sp.simplify(e_a1_rot - e_a1) == 0, f"{e_a1_rot} - {e_a1}")
    check("complement energy is unchanged", sp.simplify(e_perp_rot - e_perp) == 0, f"{e_perp_rot} - {e_perp}")

    print()
    print("D. Quadratic-energy no-section check")
    print("-" * 72)
    alpha, beta = sp.symbols("alpha beta")
    e_total = alpha * e_a1 + beta * e_perp
    e_total_rot = alpha * e_a1_rot + beta * e_perp_rot
    check(
        "all quadratic energies in the current invariant class tie on the orbit",
        sp.simplify(e_total_rot - e_total) == 0,
        f"delta={sp.simplify(e_total_rot - e_total)}",
    )
    check(
        "energy tie plus moved coordinates prevents canonical section selection",
        sp.simplify(e_total_rot - e_total) == 0 and sp.simplify(perp_rot - perp) != sp.zeros(4),
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: bounded no-canonical-complement-section claim is ready for re-audit.")
        return 0
    print("VERDICT: universal GR complement canonicalization checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

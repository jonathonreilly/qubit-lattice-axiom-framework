#!/usr/bin/env python3
"""Verifier for the hierarchy D=4 density-scale readout bridge.

The checked theorem is deliberately narrow:

    rho_* = A(L) v(L)^4 with fixed positive rho_* and A(L) > 0
    implies v(L) / v_ref = (A_ref / A(L))^(1/4).

It fixes exponent, inverse/direct placement, sign, and baseline
normalization for the coefficient-to-scale map. It does not identify the
electroweak VEV with this readout.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
)
PARENT_NOTE_PATH = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def scale_ratio(a_ref: float, a_new: float) -> float:
    return (a_ref / a_new) ** 0.25


def note_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_rows() -> dict:
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]


def main() -> int:
    print("Hierarchy D=4 density-scale readout bridge verifier")
    print("Status authority: independent audit lane only.")
    print("No observed target value, fitted coefficient, textbook import, or new axiom is load-bearing.")

    section("Fixed positive D=4 density algebra")
    rho = 5.0
    a_ref = 2.0
    a_new = 7.0
    v_ref = (rho / a_ref) ** 0.25
    v_new = (rho / a_new) ** 0.25
    lhs = v_new / v_ref
    rhs = scale_ratio(a_ref, a_new)
    print(f"rho={rho:.6f}; A_ref={a_ref:.6f}; A_new={a_new:.6f}")
    print(f"v_new/v_ref={lhs:.15f}; (A_ref/A_new)^(1/4)={rhs:.15f}")
    check("fixed-density equation gives inverse fourth-root coefficient placement", abs(lhs - rhs) < 1.0e-15)

    baseline = scale_ratio(a_ref, a_ref)
    check("reference endpoint normalizes exactly to one", abs(baseline - 1.0) < 1.0e-15)
    check(
        "larger coefficient gives downward scale compression",
        a_new > a_ref and scale_ratio(a_ref, a_new) < 1.0,
        f"ratio={scale_ratio(a_ref, a_new):.15f}",
    )
    check(
        "smaller coefficient gives upward scale rescaling",
        scale_ratio(a_ref, 1.0) > 1.0,
        f"ratio={scale_ratio(a_ref, 1.0):.15f}",
    )

    section("Exact endpoint applications")
    a2_over_a4 = Fraction(7, 8)
    v4_over_v2 = float(a2_over_a4) ** 0.25
    direct_root = float(Fraction(8, 7)) ** 0.25
    print(f"A_2/A_4 = {a2_over_a4}")
    print(f"v_4/v_2 = (7/8)^(1/4) = {v4_over_v2:.15f}")
    print(f"direct fourth root (A_4/A_2)^(1/4) = {direct_root:.15f}")
    check("L_t=4 endpoint uses inverse placement (7/8)^(1/4), not direct root", v4_over_v2 < 1.0 < direct_root)
    check(
        "L_t=4 exact base is the endpoint coefficient ratio A_2/A_4=7/8",
        a2_over_a4 == Fraction(7, 8),
    )

    scalar_ratio = 2.0 / math.sqrt(3.0)
    scalar_scale = scalar_ratio ** -0.25
    expected_scalar = (math.sqrt(3.0) / 2.0) ** 0.25
    print(f"A_inf/A_2 = 2/sqrt(3) = {scalar_ratio:.15f}")
    print(f"v_inf/v_2 = (A_inf/A_2)^(-1/4) = {scalar_scale:.15f}")
    check("temporal-average scalar endpoint has the same inverse-fourth-root placement", abs(scalar_scale - expected_scalar) < 1.0e-15)
    check("temporal-average scalar endpoint compresses downward relative to L_t=2", scalar_ratio > 1.0 and scalar_scale < 1.0)

    section("Dependency status checks")
    rows = ledger_rows()
    expected = {
        "hierarchy_dimensional_fourth_root_compression_narrow_theorem_note_2026-05-10": RETAINED_GRADES,
        "hierarchy_effective_potential_endpoint_note": RETAINED_GRADES,
        "scalar_3plus1_temporal_ratio_note": RETAINED_GRADES,
    }
    statuses = {cid: rows.get(cid, {}).get("effective_status") for cid in expected}
    for cid, allowed in expected.items():
        check(
            f"dependency {cid} is retained-grade in live ledger",
            statuses[cid] in allowed,
            f"effective_status={statuses[cid]}",
        )

    section("Source boundary hygiene")
    note = note_text(NOTE_PATH)
    parent = note_text(PARENT_NOTE_PATH)
    flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())
    required_note_phrases = [
        "fixed positive D=4 density-coefficient readout",
        "v(L) / v(L_ref) = (A_ref / A(L))^(1/4)",
        "This bridge does not identify the electroweak VEV with that fixed-density readout",
        "No observed target value",
        "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md",
        "SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md",
        "TOTAL: PASS=13 FAIL=0",
    ]
    flat_note = " ".join(note.split())
    missing = [phrase for phrase in required_note_phrases if phrase not in flat_note]
    forbidden_specific_imports = ["v_obs", "C_obs", "PDG"]
    present_forbidden = [phrase for phrase in forbidden_specific_imports if phrase in note]
    check(
        "bridge note states theorem, boundary, dependencies, and expected scorecard",
        not missing and not present_forbidden,
        f"missing={missing}; present_forbidden={present_forbidden}",
    )
    check(
        "parent dimensional-compression note wires bridge as source-side support but keeps physical VEV premise open",
        "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md" in parent
        and "fixed-density coefficient-to-scale bridge" in parent_flat
        and "still does not identify the electroweak VEV" in parent_flat
        and "proposal_allowed: false" in parent,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

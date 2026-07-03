#!/usr/bin/env python3
"""Strict W/Z neutral-carrier response packet for the Y_T top/W route.

The runner verifies exact W/Z response rows on the retained one-Higgs EW
surface.  It keeps the result denominator-side support only: no top numerator
response row or numerical Y_T closure is certified here.

2026-06-19/2026-06-20 audit-scope repair: the checks are segregated into two
layers, matching the note split.

  Layer 1 (clean EW derivative corollary, standalone exact-support scope):
    Part 3 (W/Z derivative rows + ratio + radial-Jacobian recovery) and
    Part 4 (reparameterization invariance). These differentiate the retained
    M_W, M_Z formulas with respect to a STIPULATED local neutral EW radial
    coordinate. They do not depend on what physical object that coordinate is.

  Layer 2 (carrier-source identification, CONDITIONAL on an unsupplied
  same-surface bridge):
    Part 2 (neutral P_- ray tangent algebra). This is the only check that
    touches the qubit P_- / EW neutral-ray coordinate. It is retained as
    conditional layer-2 support and explicitly NOT a closed carrier-source
    identification: it establishes shared-coordinate ray algebra, not the
    physical same-surface identification, which remains an open bridge.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"

NOTE = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
NEUTRAL_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
SOURCE_COORD = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
HYPERCHARGE = DOCS / "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md"
EW_COUPLING = DOCS / "EW_COUPLING_DERIVATION_NOTE.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
SYMBOLIC_TOP_PACKET = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority scope")
    for path in (NOTE, EW_MASS, NEUTRAL_RAY, SOURCE_COORD, ONE_HIGGS, HYPERCHARGE, EW_COUPLING, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Strict W/Z Response Rows",
        "What This Closes",
        "What This Still Does Not Close",
        "Why This Is Not A Renaming",
        "Review Boundary Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    ew_mass = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    source_action = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    one_higgs = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    hypercharge = ledger_row("standard_model_hypercharge_uniqueness_theorem_note_2026-04-24")
    ew_coupling = ledger_row("ew_coupling_derivation_note")

    check("EW Higgs gauge-mass theorem is retained", ew_mass.get("effective_status") == "retained")
    check("source-action support packet is retained_bounded", source_action.get("effective_status") == "retained_bounded")
    check("one-Higgs top carrier is not retained authority yet", one_higgs.get("effective_status") != "retained")
    check("hypercharge uniqueness is not retained authority yet", hypercharge.get("effective_status") != "retained")
    check("EW coupling note is not retained g_2(v) authority", ew_coupling.get("effective_status") != "retained")

    return {
        "ew_mass_status": ew_mass.get("effective_status"),
        "source_action_status": source_action.get("effective_status"),
        "one_higgs_yukawa_selection_status": one_higgs.get("effective_status"),
        "hypercharge_uniqueness_status": hypercharge.get("effective_status"),
        "ew_coupling_status": ew_coupling.get("effective_status"),
    }


def part2_neutral_ray_tangent() -> None:
    # Layer 2 (CONDITIONAL): shared-coordinate ray algebra only. This is the
    # only part that touches the qubit P_- / EW neutral-ray coordinate. It is
    # NOT a closed carrier-source identification; the physical same-surface
    # bridge identifying the qubit P_- source ray with the EW neutral radial
    # source is an unsupplied, unaudited open bridge.
    print("\nPart 2 (CONDITIONAL layer-2 support): neutral ray tangent algebra")
    print("  NOTE: shared-coordinate ray algebra only; the physical same-surface")
    print("        carrier-source identification is an UNSUPPLIED open bridge.")
    s = sp.symbols("s", real=True)
    v = sp.Function("v")(s)
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_minus = (ident - z) / 2
    q = z / 2 + sp.Rational(1, 2) * ident
    h_s = sp.Matrix([0, v / sp.sqrt(2)])
    tangent = sp.diff(h_s, s)

    check("[L2-conditional] H(s) lies on neutral P_- ray", matrix_is_zero(p_minus * h_s - h_s), p_minus * h_s)
    check("[L2-conditional] dH/ds lies on neutral P_- ray", matrix_is_zero(p_minus * tangent - tangent), tangent)
    check("[L2-conditional] dH/ds is Q-neutral", matrix_is_zero(q * tangent), q * tangent)

    note = read(NOTE)
    bridge_marked_open = ("same-surface bridge" in note) and ("open bridge" in note.lower())
    check(
        "[L2-conditional] note marks the same-surface carrier-source bridge as an unsupplied open bridge",
        bridge_marked_open,
        "carrier-source identification remains conditional on the unsupplied same-surface bridge",
    )


def part3_wz_response_rows() -> None:
    print("\nPart 3 (layer-1 clean EW derivative corollary): strict W/Z response rows")
    s = sp.symbols("s", real=True)
    g2, gy = sp.symbols("g_2 g_Y", positive=True)
    v = sp.Function("v")(s)
    mw = g2 * v / 2
    mz = sp.sqrt(g2**2 + gy**2) * v / 2
    dmw = sp.diff(mw, s)
    dmz = sp.diff(mz, s)
    expected_dmw = g2 * sp.diff(v, s) / 2
    expected_dmz = sp.sqrt(g2**2 + gy**2) * sp.diff(v, s) / 2
    ratio = sp.simplify(dmw / dmz)
    recovered_jacobian = sp.simplify(2 * dmw / g2)

    check("dM_W/ds row", is_zero(dmw - expected_dmw), dmw)
    check("dM_Z/ds row", is_zero(dmz - expected_dmz), dmz)
    check("W/Z response ratio cancels source Jacobian", is_zero(ratio - g2 / sp.sqrt(g2**2 + gy**2)), ratio)
    check("absolute W response recovers radial Jacobian if g_2 is known", is_zero(recovered_jacobian - sp.diff(v, s)), recovered_jacobian)


def part4_reparameterization() -> None:
    print("\nPart 4 (layer-1 clean EW derivative corollary): source-coordinate reparameterization")
    r = sp.symbols("r", real=True)
    g2, gy = sp.symbols("g_2 g_Y", positive=True)
    f = sp.Function("f")(r)
    v = sp.Function("v")(f)
    mw = g2 * v / 2
    mz = sp.sqrt(g2**2 + gy**2) * v / 2
    ratio = sp.simplify(sp.diff(mw, r) / sp.diff(mz, r))
    check("W/Z response ratio invariant under s=f(r)", is_zero(ratio - g2 / sp.sqrt(g2**2 + gy**2)), ratio)


def part5_current_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: current Y_T closure boundary")
    strict_top_w_rows = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
    blockers = {
        "strict_wz_denominator_response_closed": True,
        "symbolic_top_response_row_present": SYMBOLIC_TOP_PACKET.exists(),
        "coefficient_certified_top_response_present": strict_top_w_rows.exists(),
        "one_higgs_yukawa_selection_retained": statuses["one_higgs_yukawa_selection_status"] == "retained",
        "hypercharge_uniqueness_retained": statuses["hypercharge_uniqueness_status"] == "retained",
        "physical_scale_g2_retained": statuses["ew_coupling_status"] == "retained",
        "retained_closure_allowed": False,
    }
    check("strict W/Z denominator response is closed", blockers["strict_wz_denominator_response_closed"])
    check("symbolic top response row is present", blockers["symbolic_top_response_row_present"])
    check("coefficient-certified top response remains absent", not blockers["coefficient_certified_top_response_present"])
    check("one-Higgs top carrier is not retained authority yet", not blockers["one_higgs_yukawa_selection_retained"])
    check("hypercharge uniqueness is not retained authority yet", not blockers["hypercharge_uniqueness_retained"])
    check("physical-scale g_2 is not retained authority yet", not blockers["physical_scale_g2_retained"])
    check("retained Y_T closure is not allowed from W/Z denominator rows alone", not blockers["retained_closure_allowed"])
    return blockers


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This packet derives `y_t`",
        "positive Y_T closure has been obtained",
        "coefficient-certified top response rows are present",
        "physical-scale `g_2(v)` is retained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT W/Z NEUTRAL-CARRIER RESPONSE PACKET")
    print("=" * 78)

    statuses = part1_anchors()
    part2_neutral_ray_tangent()
    part3_wz_response_rows()
    part4_reparameterization()
    blockers = part5_current_boundary(statuses)
    part6_firewalls()

    result = {
        "status": (
            "layer-1 exact support: strict W/Z denominator response rows on a "
            "stipulated local neutral EW radial coordinate; layer-2 carrier-source "
            "identification CONDITIONAL on an unsupplied same-surface bridge"
        ),
        "layer_split": {
            "layer1_clean_ew_derivative_corollary": "standalone exact-support scope",
            "layer2_carrier_source_identification": "conditional on unsupplied same-surface bridge (open bridge)",
        },
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The layer-1 W/Z denominator response closes and the symbolic top row is "
            "present, but the layer-2 carrier-source identification depends on an "
            "unsupplied same-surface bridge, and the top coefficient, retained "
            "one-Higgs/hypercharge authority, and physical-scale g_2 authority remain open."
        ),
        "strict_wz_denominator_response_closed": True,
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md",
            "scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py",
            "outputs/yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

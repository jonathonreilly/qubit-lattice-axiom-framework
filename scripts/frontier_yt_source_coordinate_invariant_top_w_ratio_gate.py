#!/usr/bin/env python3
"""Y_T source-coordinate invariant top/W response-ratio gate.

This runner verifies that the same-source top/W response ratio is invariant
under local source reparameterizations.  It intentionally does not certify the
missing EW carrier/source authority or any numerical top-Yukawa value.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_source_coordinate_invariant_top_w_ratio_gate_2026-05-25.json"

NOTE = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
INTERTWINER_GATE = DOCS / "YT_EW_HIGGS_SOURCE_INTERTWINER_GATE_NOTE_2026-05-25.md"
NEUTRAL_RAY_BRIDGE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
STRICT_WZ_PACKET = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
SYMBOLIC_TOP_PACKET = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

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
    print("\nPart 1: anchors and retained upstream scope")
    for path in (NOTE, FH_GATE, INTERTWINER_GATE, NEUTRAL_RAY_BRIDGE, EW_MASS, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Consequence",
        "Why This Is Not A Renaming",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    ew_mass = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    source_action = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    check("EW Higgs gauge-mass theorem is retained", ew_mass.get("effective_status") == "retained")
    check("source-action support packet remains retained_bounded only", source_action.get("effective_status") == "retained_bounded")
    return {
        "ew_mass_status": ew_mass.get("effective_status"),
        "source_action_status": source_action.get("effective_status"),
    }


def part2_arbitrary_radial_coordinate() -> None:
    print("\nPart 2: arbitrary radial coordinate cancels")
    h = sp.symbols("h", real=True)
    g2, yt = sp.symbols("g_2 y_t", nonzero=True)
    v = sp.Function("v")(h)
    mt = yt * v / sp.sqrt(2)
    mw = g2 * v / 2
    ratio = sp.simplify(sp.diff(mt, h) / sp.diff(mw, h))
    recovered = sp.simplify(g2 * ratio / sp.sqrt(2))

    check("dM_t/dh over dM_W/dh cancels v'(h)", is_zero(ratio - sp.sqrt(2) * yt / g2), ratio)
    check("y_t recovered from arbitrary radial coordinate", is_zero(recovered - yt), recovered)


def part3_source_reparameterization() -> None:
    print("\nPart 3: local source reparameterization invariance")
    s = sp.symbols("s", real=True)
    g2, yt = sp.symbols("g_2 y_t", nonzero=True)
    f = sp.Function("f")(s)
    v = sp.Function("v")(f)
    mt = yt * v / sp.sqrt(2)
    mw = g2 * v / 2
    ratio = sp.simplify(sp.diff(mt, s) / sp.diff(mw, s))
    recovered = sp.simplify(g2 * ratio / sp.sqrt(2))

    check("ratio invariant under h=f(s)", is_zero(ratio - sp.sqrt(2) * yt / g2), ratio)
    check("recovered y_t invariant under h=f(s)", is_zero(recovered - yt), recovered)

    # Explicit nonlinear witness: h = a s + b s^2, v = v0 + h + c h^2.
    a, b, c, v0 = sp.symbols("a b c v0", nonzero=True)
    h_of_s = a * s + b * s**2
    v_of_s = v0 + h_of_s + c * h_of_s**2
    mt2 = yt * v_of_s / sp.sqrt(2)
    mw2 = g2 * v_of_s / 2
    ratio2 = sp.simplify(sp.diff(mt2, s) / sp.diff(mw2, s))
    check("ratio invariant for nonlinear coordinate witness", is_zero(ratio2 - sp.sqrt(2) * yt / g2), ratio2)


def part4_neutral_radial_tangent_unique_after_carrier() -> None:
    print("\nPart 4: neutral radial tangent is one-dimensional after EW carrier is accepted")
    v, h = sp.symbols("v h", positive=True, real=True)
    a = sp.symbols("a", nonzero=True, real=True)
    radial = sp.Matrix([0, (v + a * h) / sp.sqrt(2)])
    tangent = sp.diff(radial, h)
    expected = sp.Matrix([0, a / sp.sqrt(2)])
    check("neutral radial source tangent has one free Jacobian", matrix_is_zero(tangent - expected), tangent)

    tau3 = sp.Matrix([[1, 0], [0, -1]])
    y = sp.Rational(1, 2) * sp.eye(2)
    q_tangent = (tau3 / 2 + y) * tangent
    check("radial tangent is electromagnetically neutral", matrix_is_zero(q_tangent), q_tangent)


def part5_current_closure_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: current closure boundary")
    blockers = {
        "source_coordinate_normalization_blocker_retired_for_ratio": True,
        "neutral_carrier_ray_bridge_present": NEUTRAL_RAY_BRIDGE.exists(),
        "strict_wz_denominator_response_present": STRICT_WZ_PACKET.exists(),
        "symbolic_top_response_row_present": SYMBOLIC_TOP_PACKET.exists(),
        "full_same_surface_top_w_transfer_response_present": False,
        "coefficient_certified_top_w_rows_present": False,
        "numerical_g2_retained_authority_present": False,
        "retained_closure_allowed": False,
    }
    check("source-coordinate normalization is not a blocker for the ratio", blockers["source_coordinate_normalization_blocker_retired_for_ratio"])
    check("neutral carrier-ray bridge is present", blockers["neutral_carrier_ray_bridge_present"])
    check("strict W/Z denominator response is present", blockers["strict_wz_denominator_response_present"])
    check("symbolic top response row is present", blockers["symbolic_top_response_row_present"])
    check("full same-surface top/W transfer response remains absent", not blockers["full_same_surface_top_w_transfer_response_present"])
    check("coefficient-certified top/W rows remain absent", not blockers["coefficient_certified_top_w_rows_present"])
    check("numerical g_2 authority remains absent", not blockers["numerical_g2_retained_authority_present"])
    check("status remains support/open gate", not blockers["retained_closure_allowed"], statuses)
    return blockers


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "`alpha_LM`",
        "plaquette/u0",
        "observed W/Z/top masses",
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This note derives `y_t`",
        "retained Y_T closure has been obtained",
        "the signed-record source is the Higgs",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T SOURCE-COORDINATE INVARIANT TOP/W RATIO GATE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_arbitrary_radial_coordinate()
    part3_source_reparameterization()
    part4_neutral_radial_tangent_unique_after_carrier()
    blockers = part5_current_closure_boundary(statuses)
    part6_firewalls()

    result = {
        "status": "exact support: source-coordinate normalization is not a blocker for same-source top/W ratio",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The ratio is coordinate-invariant, the neutral carrier ray is bridged, "
            "W/Z denominator response is present, and the symbolic top response row "
            "is present, but the repo still lacks a derived top coefficient and "
            "retained numerical g_2 authority."
        ),
        "coordinate_invariance_closed": True,
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_source_coordinate_invariant_top_w_ratio_gate.py",
            "outputs/yt_source_coordinate_invariant_top_w_ratio_gate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

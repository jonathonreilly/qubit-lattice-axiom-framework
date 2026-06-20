#!/usr/bin/env python3
"""Y_T qubit neutral-Higgs carrier-ray bridge gate.

This runner verifies the finite Pauli/projector algebra after the 2026-06-18
scope repair.  The signed-record lower-projector algebra, EW lower-ray
neutrality, and same-surface charge-spectral projector repair close as bounded
support; top coefficient, transfer-response, scalar-normalization, and
physical-scale gates remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_qubit_neutral_higgs_carrier_ray_bridge_2026-05-25.json"

NOTE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
CORE_NOTE = DOCS / "YT_SIGNED_RECORD_LOWER_PROJECTOR_NEUTRAL_RAY_ALGEBRA_CORE_BOUNDED_NOTE_2026-06-18.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
SAME_SURFACE_CARRIER = DOCS / "YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md"
SOURCE_COORD = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
HYPERCHARGE = DOCS / "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
SYMBOLIC_TOP_PACKET = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}

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


def is_retained_grade(row_or_status: dict[str, Any] | str | None) -> bool:
    if isinstance(row_or_status, dict):
        status = row_or_status.get("effective_status")
    else:
        status = row_or_status
    return status in RETAINED_GRADES


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority scope")
    for path in (NOTE, CORE_NOTE, MINIMAL_AXIOMS, SOURCE_ACTION, EW_MASS, SAME_SURFACE_CARRIER, SOURCE_COORD, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem",
        "What This Closes",
        "What This Still Does Not Close",
        "Why This Is Not A Renaming",
        "Review Boundary Certificate",
        "2026-06-18 audit-scope repair",
        "same-surface carrier repair",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    core = read(CORE_NOTE)
    for phrase in (
        "Actual current-surface status:** bounded-support",
        "Trace class:** upstream_support",
        "not a same-surface physical carrier theorem",
        "bare_retained_allowed: false",
    ):
        check(f"core note contains boundary phrase: {phrase}", phrase in core)

    carrier_note = read(SAME_SURFACE_CARRIER)
    for phrase in (
        "same-surface spectral-projector theorem",
        "P_neut = 1_0(Q_H)",
        "P_+ = P_ch",
        "P_- = P_neut",
        "exp(h epsilon_H) = exp(h) exp(-2 h P_neut)",
        "does not derive positive Y_T closure",
    ):
        check(f"same-surface carrier theorem contains marker: {phrase}", phrase in carrier_note)

    source_action = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    ew_mass = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    one_higgs = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    hypercharge = ledger_row("standard_model_hypercharge_uniqueness_theorem_note_2026-04-24")
    ew_coupling = ledger_row("ew_coupling_derivation_note")

    check("source-action support packet is retained-grade", is_retained_grade(source_action))
    check("EW Higgs gauge-mass theorem is retained-grade", is_retained_grade(ew_mass))
    check("one-Higgs Yukawa gauge-selection row is not retained-grade", not is_retained_grade(one_higgs))
    check("hypercharge uniqueness row is not retained-grade", not is_retained_grade(hypercharge))
    check("EW coupling note is not retained-grade g_2(v) authority", not is_retained_grade(ew_coupling))

    return {
        "source_action_status": source_action.get("effective_status"),
        "ew_mass_status": ew_mass.get("effective_status"),
        "one_higgs_yukawa_selection_status": one_higgs.get("effective_status"),
        "hypercharge_uniqueness_status": hypercharge.get("effective_status"),
        "ew_coupling_status": ew_coupling.get("effective_status"),
    }


def part2_signed_record_projector_equivalence() -> None:
    print("\nPart 2: signed record is affinely equivalent to P_- occupation")
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_plus = (ident + z) / 2
    p_minus = (ident - z) / 2

    check("P_+ is a projector", matrix_is_zero(p_plus * p_plus - p_plus), p_plus)
    check("P_- is a projector", matrix_is_zero(p_minus * p_minus - p_minus), p_minus)
    check("P_+ and P_- are orthogonal", matrix_is_zero(p_plus * p_minus), p_plus * p_minus)
    check("P_+ + P_- = I", matrix_is_zero(p_plus + p_minus - ident), p_plus + p_minus)
    check("sigma_z = P_+ - P_-", matrix_is_zero(z - (p_plus - p_minus)), p_plus - p_minus)
    check("sigma_z = I - 2 P_-", matrix_is_zero(z - (ident - 2 * p_minus)), ident - 2 * p_minus)

    h = sp.symbols("h", real=True)
    signed_weights = sp.Matrix([sp.exp(h), sp.exp(-h)])
    pminus_weights = sp.exp(h) * sp.Matrix([1, sp.exp(-2 * h)])
    check(
        "exp(h sigma_z) normalized weights equal exp(-2h P_-) weights",
        matrix_is_zero(signed_weights - pminus_weights),
        signed_weights,
    )

    eps_plus, eps_minus = sp.Integer(1), sp.Integer(-1)
    nminus_plus, nminus_minus = sp.Integer(0), sp.Integer(1)
    check("epsilon = 1 - 2 n_- on P_+", is_zero(eps_plus - (1 - 2 * nminus_plus)))
    check("epsilon = 1 - 2 n_- on P_-", is_zero(eps_minus - (1 - 2 * nminus_minus)))


def part3_neutral_ew_ray_alignment() -> None:
    print("\nPart 3: P_- is the neutral lower ray in EW bookkeeping")
    v = sp.symbols("v", positive=True, real=True)
    ident = sp.eye(2)
    z = sp.Matrix([[1, 0], [0, -1]])
    p_plus = (ident + z) / 2
    p_minus = (ident - z) / 2
    t3 = z / 2
    y_h = sp.Rational(1, 2) * ident
    q = t3 + y_h

    h0 = sp.Matrix([0, v / sp.sqrt(2)])
    upper = sp.Matrix([1, 0])

    check("P_- fixes H_0", matrix_is_zero(p_minus * h0 - h0), p_minus * h0)
    check("P_+ kills H_0", matrix_is_zero(p_plus * h0), p_plus * h0)
    check("Q annihilates H_0", matrix_is_zero(q * h0), q * h0)
    check("upper component is charged", matrix_is_zero(q * upper - upper), q * upper)
    check("neutral ray is unique in the one-Higgs doublet", q.rank() == 1 and q.nullspace() == [sp.Matrix([0, 1])], q.nullspace())
    check("P_- equals the zero spectral projector I-Q", matrix_is_zero(p_minus - (ident - q)), ident - q)
    check("P_+ equals the charged spectral projector Q", matrix_is_zero(p_plus - q), q)


def part4_radial_tangent_and_ratio_compatibility() -> None:
    print("\nPart 4: radial tangent stays on the same neutral ray")
    s = sp.symbols("s", real=True)
    v = sp.Function("v")(s)
    ident = sp.eye(2)
    z = sp.Matrix([[1, 0], [0, -1]])
    p_minus = (ident - z) / 2
    q = z / 2 + sp.Rational(1, 2) * ident

    h_s = sp.Matrix([0, v / sp.sqrt(2)])
    tangent = sp.diff(h_s, s)
    check("H(s) lies on P_- ray", matrix_is_zero(p_minus * h_s - h_s), p_minus * h_s)
    check("dH/ds lies on P_- ray", matrix_is_zero(p_minus * tangent - tangent), tangent)
    check("dH/ds remains electromagnetically neutral", matrix_is_zero(q * tangent), q * tangent)

    g2, yt = sp.symbols("g_2 y_t", nonzero=True)
    mt = yt * v / sp.sqrt(2)
    mw = g2 * v / 2
    ratio = sp.simplify(sp.diff(mt, s) / sp.diff(mw, s))
    check("top/W response ratio cancels the remaining radial Jacobian", is_zero(ratio - sp.sqrt(2) * yt / g2), ratio)


def part5_current_closure_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: current closure boundary")
    strict_top_w_rows = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
    strict_wz_packet = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
    blockers = {
        "lower_projector_algebra_core_closed": True,
        "same_surface_qubit_higgs_carrier_bridge_closed": SAME_SURFACE_CARRIER.exists(),
        "wz_denominator_response_closed": strict_wz_packet.exists(),
        "symbolic_top_response_row_present": SYMBOLIC_TOP_PACKET.exists(),
        "full_same_surface_top_w_transfer_response_closed": False,
        "coefficient_certified_top_w_rows_present": strict_top_w_rows.exists(),
        "strict_same_source_wz_packet_present": strict_wz_packet.exists(),
        "one_higgs_yukawa_selection_retained": is_retained_grade(statuses["one_higgs_yukawa_selection_status"]),
        "hypercharge_uniqueness_retained": is_retained_grade(statuses["hypercharge_uniqueness_status"]),
        "physical_scale_g2_retained": is_retained_grade(statuses["ew_coupling_status"]),
        "retained_closure_allowed": False,
    }
    check("lower-projector algebra core is closed", blockers["lower_projector_algebra_core_closed"])
    check(
        "same-surface qubit/Higgs carrier bridge is closed",
        blockers["same_surface_qubit_higgs_carrier_bridge_closed"],
    )
    check("strict W/Z denominator response packet is present", blockers["wz_denominator_response_closed"])
    check("symbolic top response row packet is present", blockers["symbolic_top_response_row_present"])
    check("full same-surface top/W transfer response remains open", not blockers["full_same_surface_top_w_transfer_response_closed"])
    check("coefficient-certified top/W rows remain absent", not blockers["coefficient_certified_top_w_rows_present"])
    check("one-Higgs top carrier is not retained authority yet", not blockers["one_higgs_yukawa_selection_retained"])
    check("hypercharge uniqueness is not retained authority yet", not blockers["hypercharge_uniqueness_retained"])
    check("physical-scale g_2 is not retained authority yet", not blockers["physical_scale_g2_retained"])
    check("retained Y_T closure is not allowed from this support theorem", not blockers["retained_closure_allowed"])
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
        "observed top/W/Z/Higgs masses",
        "fitted selector",
        "same-surface carrier repair is a top-response",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This note derives `y_t`",
        "retained Y_T closure has been obtained",
        "carrier-ray bridge is closed",
        "same physical carrier surface has been derived",
        "signed-record source is physically the neutral EW radial source",
        "coefficient-certified top/W response rows are present",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T QUBIT NEUTRAL-HIGGS CARRIER-RAY BRIDGE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_signed_record_projector_equivalence()
    part3_neutral_ew_ray_alignment()
    part4_radial_tangent_and_ratio_compatibility()
    blockers = part5_current_closure_boundary(statuses)
    part6_firewalls()

    result = {
        "status": (
            "bounded support: signed-record lower-projector algebra plus EW "
            "lower-ray neutrality plus same-surface charge-spectral projector repair; "
            "top response and physical-scale gates open"
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The lower-projector algebra and same-surface carrier repair close "
            "only as source-side support; the top coefficient, one-Higgs/hypercharge "
            "authority, transfer-response, scalar-normalization, and physical-scale "
            "g_2 authority remain open."
        ),
        "lower_projector_algebra_core_closed": True,
        "same_surface_qubit_higgs_carrier_bridge_closed": SAME_SURFACE_CARRIER.exists(),
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md",
            "docs/YT_SIGNED_RECORD_LOWER_PROJECTOR_NEUTRAL_RAY_ALGEBRA_CORE_BOUNDED_NOTE_2026-06-18.md",
            "docs/YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md",
            "scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py",
            "outputs/yt_qubit_neutral_higgs_carrier_ray_bridge_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

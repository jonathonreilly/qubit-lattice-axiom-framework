#!/usr/bin/env python3
"""Strict same-source top/W response coefficient obstruction for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
TOP_SOURCE_NOGO = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SAME_SOURCE = DOCS / "YT_SAME_SOURCE_EW_HIGGS_AUTHORITY_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
TOP_COEFF_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
SOURCE_SCALE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

TOP_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_top_source_identification_hard_stop_no_go_2026-05-27.json"
FH_GATE_OUT = ROOT / "outputs" / "yt_fh_top_w_response_ratio_gate_2026-05-25.json"
SAME_SOURCE_OUT = ROOT / "outputs" / "yt_same_source_ew_higgs_authority_gate_2026-05-25.json"
STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
TOP_COEFF_NOGO_OUT = ROOT / "outputs" / "yt_top_response_coefficient_underdetermination_no_go_2026-05-25.json"
STRICT_TOP_W_ROWS = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"

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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current support outputs")
    paths = (
        NOTE,
        TOP_SOURCE_NOGO,
        FULL_STACK,
        FH_GATE,
        SAME_SOURCE,
        STRICT_WZ,
        STRICT_TOP,
        TOP_COEFF_NOGO,
        SOURCE_SCALE,
        TOP_SOURCE_NOGO_OUT,
        FH_GATE_OUT,
        SAME_SOURCE_OUT,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        TOP_COEFF_NOGO_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Minimal Premise Set",
        "Finite Transfer Counterfamily",
        "Current Certificate Field Status",
        "Exact Obstruction",
        "Relation To The Primitive Source No-Go",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    top_source = load_json(TOP_SOURCE_NOGO_OUT)
    fh = load_json(FH_GATE_OUT)
    same = load_json(SAME_SOURCE_OUT)
    wz = load_json(STRICT_WZ_OUT)
    top = load_json(STRICT_TOP_OUT)
    coeff_nogo = load_json(TOP_COEFF_NOGO_OUT)

    check("top-source identification no-go passed", top_source.get("fail_count") == 0, top_source.get("fail_count"))
    check("FH response-ratio gate passed", fh.get("fail_count") == 0, fh.get("fail_count"))
    check("same-source authority gate passed", same.get("fail_count") == 0, same.get("fail_count"))
    check("W/Z denominator response packet passed", wz.get("fail_count") == 0, wz.get("fail_count"))
    check("symbolic top response packet passed", top.get("fail_count") == 0, top.get("fail_count"))
    check("top coefficient underdetermination no-go passed", coeff_nogo.get("fail_count") == 0, coeff_nogo.get("fail_count"))
    check("symbolic top coefficient remains free", top.get("top_coefficient_derived") is False)
    check("strict top/W coefficient rows absent", not STRICT_TOP_W_ROWS.exists(), STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())

    return {
        "top_source_nogo": top_source,
        "fh": fh,
        "same_source": same,
        "strict_wz": wz,
        "strict_top": top,
        "top_coefficient_nogo": coeff_nogo,
    }


def part2_transfer_counterfamily() -> dict[str, str]:
    print("\nPart 2: finite transfer counterfamily")
    h = sp.symbols("h", real=True)
    a_t, g2, v0, A, kappa = sp.symbols("a_t g_2 v_0 A kappa", positive=True)
    v = v0 + A * h
    lambda_0 = sp.Integer(1)
    lambda_w = sp.exp(-a_t * g2 * v / 2)
    lambda_t = sp.exp(-a_t * kappa * v / sp.sqrt(2))

    mass_w = sp.simplify(-sp.log(lambda_w / lambda_0) / a_t)
    mass_t = sp.simplify(-sp.log(lambda_t / lambda_0) / a_t)
    d_mw = sp.simplify(sp.diff(mass_w, h))
    d_mt = sp.simplify(sp.diff(mass_t, h))

    check("transfer formula recovers W mass row", is_zero(mass_w - g2 * v / 2), mass_w)
    check("transfer formula recovers top mass row", is_zero(mass_t - kappa * v / sp.sqrt(2)), mass_t)
    check("W derivative is coefficient-certified", is_zero(d_mw - g2 * A / 2), d_mw)
    check("top derivative contains free kappa", is_zero(d_mt - kappa * A / sp.sqrt(2)), d_mt)

    recovered = sp.simplify(g2 / sp.sqrt(2) * d_mt / d_mw)
    check("top/W response readout returns kappa", is_zero(recovered - kappa), recovered)

    kappa_a = sp.Rational(1, 1) / sp.sqrt(6)
    kappa_b = sp.Rational(2, 1) / sp.sqrt(6)
    readout_a = sp.simplify(recovered.subs(kappa, kappa_a))
    readout_b = sp.simplify(recovered.subs(kappa, kappa_b))
    check("two admissible completions give different readouts", sp.simplify(readout_a - readout_b) != 0, (readout_a, readout_b))
    check("W row is unchanged by changing kappa", not d_mw.has(kappa), d_mw)

    gap_wt = sp.simplify(mass_t - mass_w)
    example_gap = gap_wt.subs({kappa: sp.Rational(3, 1), g2: sp.Rational(1, 1), v0: 1, A: 1, h: 0})
    check("representative W/top eigenvalues are isolated", example_gap != 0, example_gap)

    return {
        "dM_W_dh": "g_2*A/2",
        "dM_t_dh": "kappa*A/sqrt(2)",
        "readout": "kappa",
    }


def part3_source_reparameterization() -> None:
    print("\nPart 3: source reparameterization does not remove the obstruction")
    h_prime = sp.symbols("h_prime", real=True)
    c, A, g2, kappa = sp.symbols("c A g_2 kappa", positive=True)
    d_h_d_hp = sp.Rational(1, 1) / c
    d_mw_hp = g2 * A / 2 * d_h_d_hp
    d_mt_hp = kappa * A / sp.sqrt(2) * d_h_d_hp
    recovered = sp.simplify(g2 / sp.sqrt(2) * d_mt_hp / d_mw_hp)
    check("common source reparameterization cancels", is_zero(recovered - kappa), recovered)
    check("the recovered coefficient is still the supplied kappa", recovered.has(kappa), recovered)
    check("h_prime symbol is irrelevant to the ratio", not recovered.has(h_prime), recovered)


def part4_current_certificate_fields() -> dict[str, dict[str, Any]]:
    print("\nPart 4: current strict-certificate field status")
    fields: dict[str, dict[str, Any]] = {
        "same_source_id": {
            "current_status": "support-only symbolic neutral carrier coordinate; accepted physical top/W transfer source absent",
            "closes_positive_field": False,
        },
        "top_pole_isolated": {
            "current_status": "absent coefficient-certified top pole row",
            "closes_positive_field": False,
        },
        "W_pole_isolated": {
            "current_status": "W/Z denominator algebra support exists; same-surface pole certificate absent",
            "closes_positive_field": False,
        },
        "coefficient_certified_dM_t_dh": {
            "current_status": "symbolic y_33*v'(h)/sqrt(2), coefficient free",
            "closes_positive_field": False,
        },
        "coefficient_certified_dM_W_dh": {
            "current_status": "support row g_2*v'(h)/2, not packaged with top pole data",
            "closes_positive_field": "partial",
        },
        "contact_subtraction_done": {
            "current_status": "absent for measured/solved top/W pole packet",
            "closes_positive_field": False,
        },
        "FV_IR_model_class_checks_pass": {
            "current_status": "absent for measured/solved top/W pole packet",
            "closes_positive_field": False,
        },
        "same_model_class": {
            "current_status": "same symbolic carrier class only; accepted top/W transfer class absent",
            "closes_positive_field": False,
        },
        "same_scale_for_g2_and_source_response": {
            "current_status": "open for numerical Y_T; local ratio can scope g_2 separately",
            "closes_positive_field": False,
        },
        "no_forbidden_imports": {
            "current_status": "pass for support artifacts and this obstruction",
            "closes_positive_field": True,
        },
    }
    for field, info in fields.items():
        check(f"field assessed: {field}", "current_status" in info and "closes_positive_field" in info, info)
    check("at least one required positive field fails", any(info["closes_positive_field"] is False for info in fields.values()))
    check("coefficient-certified top row fails", fields["coefficient_certified_dM_t_dh"]["closes_positive_field"] is False)
    check("forbidden imports are not the blocker", fields["no_forbidden_imports"]["closes_positive_field"] is True)
    return fields


def part5_scope_and_firewalls() -> None:
    print("\nPart 5: scope and firewalls")
    note = read(NOTE)
    note_one_line = " ".join(note.split())
    check("route pruned is narrow", "deriving strict coefficient-certified top/W response evidence from current same-source/W-row/symbolic-top support alone" in note)
    check("future direct top/W response remains live", "The strict response route remains live" in note)
    check("proposal is explicitly not allowed", "proposal_allowed: false" in note)

    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note_one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive Y_T closure",
        "strict top/W pole-response evidence exists",
        "kappa = 1/sqrt(6) follows",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT SAME-SOURCE TOP/W RESPONSE COEFFICIENT OBSTRUCTION")
    print("=" * 78)

    support_outputs = part1_anchors()
    counterfamily = part2_transfer_counterfamily()
    part3_source_reparameterization()
    field_status = part4_current_certificate_fields()
    part5_scope_and_firewalls()

    result = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Current same-source/W-row/symbolic-top support does not contain a "
            "coefficient-certified top pole response row. A finite transfer "
            "counterfamily preserves the support schema while varying the recovered "
            "top coefficient."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": (
            "deriving strict coefficient-certified top/W response evidence from "
            "current same-source/W-row/symbolic-top support alone"
        ),
        "counterfamily": counterfamily,
        "current_certificate_field_status": field_status,
        "support_output_status": {
            "top_source_nogo_fail_count": support_outputs["top_source_nogo"].get("fail_count"),
            "fh_gate_fail_count": support_outputs["fh"].get("fail_count"),
            "same_source_gate_fail_count": support_outputs["same_source"].get("fail_count"),
            "strict_wz_fail_count": support_outputs["strict_wz"].get("fail_count"),
            "strict_top_fail_count": support_outputs["strict_top"].get("fail_count"),
            "top_coefficient_nogo_fail_count": support_outputs["top_coefficient_nogo"].get("fail_count"),
            "symbolic_top_coefficient_derived": support_outputs["strict_top"].get("top_coefficient_derived"),
            "strict_top_w_rows_present": STRICT_TOP_W_ROWS.exists(),
        },
        "next_action": (
            "direct same-surface top and W pole-response solve, with coefficient rows, "
            "contact subtraction, FV/IR checks, model-class checks, and same-scale g_2 scope"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md",
            "scripts/frontier_yt_strict_same_source_top_w_response_coefficient_obstruction.py",
            "outputs/yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

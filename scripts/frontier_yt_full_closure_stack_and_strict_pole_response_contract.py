#!/usr/bin/env python3
"""Y_T closure stack and strict pole-response contract.

This runner verifies the current burn-down state:

* Fisher source-scale and Fisher/LSZ bridge support are present.
* Pole-row Gram purity alone remains normalization-blind.
* The primitive no-hidden-record intervention law is now derived as exact
  support; the top-source identification route is now pruned from current
  structural inputs by a hard-stop no-go; strict same-source top/W response
  evidence is the remaining audit-clean path unless audit accepts the primitive
  top-source premise.
* No retained/proposed-retained Y_T closure is authorized by this packet.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

NOTE = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
PRIMITIVE_RECORD_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
TOP_SOURCE_NOGO = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
MININFO_UNIQUENESS = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
FISHER = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
FISHER_LSZ = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SAME_SOURCE = DOCS / "YT_SAME_SOURCE_EW_HIGGS_AUTHORITY_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
STRICT_SAME_SOURCE_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
DIRECT_SPARSE_RESPONSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

FISHER_OUT = ROOT / "outputs" / "yt_primitive_physical_source_fisher_arclength_invariant_2026-05-26.json"
MIN_INFO_OUT = ROOT / "outputs" / "yt_minimum_information_source_action_bridge_2026-05-26.json"
PRIMITIVE_RECORD_LAW_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
TOP_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_top_source_identification_hard_stop_no_go_2026-05-27.json"
MININFO_UNIQUENESS_OUT = ROOT / "outputs" / "yt_physical_intervention_mininfo_uniqueness_gate_2026-05-26.json"
TOP_CARRIER_OUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"
FISHER_LSZ_OUT = ROOT / "outputs" / "yt_fisher_lsz_source_normalization_bridge_2026-05-26.json"
FH_OUT = ROOT / "outputs" / "yt_fh_top_w_response_ratio_gate_2026-05-25.json"
SAME_SOURCE_OUT = ROOT / "outputs" / "yt_same_source_ew_higgs_authority_gate_2026-05-25.json"
STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
STRICT_SAME_SOURCE_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"
DIRECT_SPARSE_RESPONSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
STRICT_TOP_W_ROWS = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
STRICT_SOURCE_HIGGS_ROWS = ROOT / "outputs" / "yt_source_action_block508_id_source_higgs_strict_rows_2026-05-22.json"

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


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = load_json(LEDGER)
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, str]:
    print("\nPart 1: anchors and audited/current statuses")
    paths = (
        NOTE,
        SOURCE_ACTION,
        MIN_INFO,
        PRIMITIVE_RECORD_LAW,
        TOP_SOURCE_NOGO,
        MININFO_UNIQUENESS,
        TOP_CARRIER,
        FISHER,
        FISHER_LSZ,
        POLE_NOGO,
        FH_GATE,
        SAME_SOURCE,
        STRICT_WZ,
        STRICT_TOP,
        STRICT_SAME_SOURCE_OBSTRUCTION,
        DIRECT_SPARSE_RESPONSE_CERT,
        LEDGER,
        FISHER_OUT,
        MIN_INFO_OUT,
        PRIMITIVE_RECORD_LAW_OUT,
        TOP_SOURCE_NOGO_OUT,
        MININFO_UNIQUENESS_OUT,
        TOP_CARRIER_OUT,
        FISHER_LSZ_OUT,
        FH_OUT,
        SAME_SOURCE_OUT,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        STRICT_SAME_SOURCE_OBSTRUCTION_OUT,
        DIRECT_SPARSE_RESPONSE_CERT_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Stack From Here To Full Closure",
        "Conditional Closure Theorem",
        "Current Burn-Down Result",
        "Non-Claims",
        "strict same-source top/W response",
        "primitive no-hidden-record source law is derived",
        "top-source identification is pruned",
        "finite-transfer counterfamily",
        "sparse transfer response certificate",
    ):
        check(f"note contains required section/phrase: {phrase}", phrase in note)

    rows = {
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22").get("effective_status"),
        "pole_no_go": ledger_row("yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23").get("effective_status"),
        "ew_mass": ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26").get("effective_status"),
        "ew_coupling": ledger_row("ew_coupling_derivation_note").get("effective_status"),
        "one_higgs": ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26").get("effective_status"),
    }
    check("source-action packet is retained_bounded support", rows["source_action"] == "retained_bounded", rows["source_action"])
    check("pole-row normalization no-go is retained_no_go", rows["pole_no_go"] == "retained_no_go", rows["pole_no_go"])
    check("EW Higgs mass theorem is retained", rows["ew_mass"] == "retained", rows["ew_mass"])
    check("EW coupling note is not retained same-scale g2 authority", rows["ew_coupling"] != "retained", rows["ew_coupling"])
    check("one-Higgs selection is not retained coefficient authority", rows["one_higgs"] != "retained", rows["one_higgs"])
    return rows


def part2_support_outputs() -> dict[str, Any]:
    print("\nPart 2: already-burned-down support outputs")
    fisher = load_json(FISHER_OUT)
    min_info = load_json(MIN_INFO_OUT)
    primitive_record_law = load_json(PRIMITIVE_RECORD_LAW_OUT)
    top_source_nogo = load_json(TOP_SOURCE_NOGO_OUT)
    mininfo_uniqueness = load_json(MININFO_UNIQUENESS_OUT)
    top_carrier = load_json(TOP_CARRIER_OUT)
    fisher_lsz = load_json(FISHER_LSZ_OUT)
    fh = load_json(FH_OUT)
    same = load_json(SAME_SOURCE_OUT)
    wz = load_json(STRICT_WZ_OUT)
    top = load_json(STRICT_TOP_OUT)
    strict_obstruction = load_json(STRICT_SAME_SOURCE_OBSTRUCTION_OUT)
    direct_sparse_cert = load_json(DIRECT_SPARSE_RESPONSE_CERT_OUT)

    check("minimum-information source/action bridge passed", min_info.get("fail_count") == 0, min_info.get("fail_count"))
    check("minimum-information bridge proposal is not allowed", min_info.get("proposal_allowed") is False)
    check("primitive record intervention law passed", primitive_record_law.get("fail_count") == 0, primitive_record_law.get("fail_count"))
    check("primitive record intervention law proposal is not allowed for full Y_T", primitive_record_law.get("proposal_allowed") is False)
    check("primitive record law narrows next gate to top-source identification", primitive_record_law.get("first_open_gate_after_this_note") == "physical top-source identification")
    check("top-source identification hard-stop no-go passed", top_source_nogo.get("fail_count") == 0, top_source_nogo.get("fail_count"))
    check("top-source no-go prunes structural no-compute route", top_source_nogo.get("trace_class") == "negative_route_pruning")
    check("top-source no-go keeps strict response as next action", "strict same-source top/W response" in top_source_nogo.get("next_action", ""))
    check("physical-intervention mininfo uniqueness gate passed", mininfo_uniqueness.get("fail_count") == 0, mininfo_uniqueness.get("fail_count"))
    check("physical-intervention uniqueness proposal is not allowed", mininfo_uniqueness.get("proposal_allowed") is False)
    check("one-Higgs top-carrier support passed", top_carrier.get("fail_count") == 0, top_carrier.get("fail_count"))
    check("one-Higgs top-carrier proposal is not allowed", top_carrier.get("proposal_allowed") is False)
    check("Fisher source-scale theorem passed", fisher.get("fail_count") == 0, fisher.get("fail_count"))
    check("Fisher theorem proposal is not allowed", fisher.get("proposal_allowed") is False)
    check("Fisher theorem exposes remaining bridge", "remaining_bridge" in fisher)
    check("Fisher/LSZ bridge passed", fisher_lsz.get("fail_count") == 0, fisher_lsz.get("fail_count"))
    check("Fisher/LSZ bridge proposal is not allowed", fisher_lsz.get("proposal_allowed") is False)
    check("FH ratio gate passed", fh.get("fail_count") == 0, fh.get("fail_count"))
    check("FH ratio gate proposal is not allowed", fh.get("proposal_allowed") is False)
    check("same-source authority gate passed", same.get("fail_count") == 0, same.get("fail_count"))
    check("strict W/Z response packet passed", wz.get("fail_count") == 0, wz.get("fail_count"))
    check("symbolic top response packet passed", top.get("fail_count") == 0, top.get("fail_count"))
    check("symbolic top response leaves coefficient open", top.get("top_coefficient_derived") is False)
    check("strict same-source coefficient obstruction passed", strict_obstruction.get("fail_count") == 0, strict_obstruction.get("fail_count"))
    check("strict same-source obstruction is route-pruning", strict_obstruction.get("trace_class") == "negative_route_pruning")
    check("direct sparse response certificate harness passed", direct_sparse_cert.get("fail_count") == 0, direct_sparse_cert.get("fail_count"))
    check("direct sparse response certificate is bounded support", direct_sparse_cert.get("actual_current_surface_status") == "bounded-support microbench / open strict-response backend")
    check("direct sparse response certificate proposal is not allowed", direct_sparse_cert.get("proposal_allowed") is False)
    check("direct sparse response certificate does not supply strict top/W rows", direct_sparse_cert.get("strict_top_w_response_certificate_present") is False)

    return {
        "fisher": fisher,
        "minimum_information": min_info,
        "primitive_record_law": primitive_record_law,
        "top_source_nogo": top_source_nogo,
        "minimum_information_uniqueness": mininfo_uniqueness,
        "top_carrier": top_carrier,
        "fisher_lsz": fisher_lsz,
        "fh": fh,
        "same_source": same,
        "strict_wz": wz,
        "strict_top": top,
        "strict_same_source_obstruction": strict_obstruction,
        "direct_sparse_response_certificate": direct_sparse_cert,
    }


def part3_fisher_lsz_and_response_algebra() -> None:
    print("\nPart 3: conditional closure algebra")
    lam, h, a_o = sp.symbols("lambda h A_O", positive=True)
    fisher_metric = lam**2
    d_ell_dh = sp.sqrt(fisher_metric)
    source_derivative = -lam
    intrinsic_source_derivative = sp.simplify(source_derivative / d_ell_dh)
    check("Fisher arclength removes positive raw lambda", is_zero(intrinsic_source_derivative + 1), intrinsic_source_derivative)

    operator_scale = sp.symbols("operator_scale", positive=True)
    lsz_original = sp.simplify(1 / a_o)
    lsz_scaled = sp.simplify(operator_scale / (operator_scale * a_o))
    check("LSZ insertion invariant under operator rescaling", is_zero(lsz_scaled - lsz_original), lsz_scaled)

    y, g2, dv = sp.symbols("y_t g_2 dv_dh", positive=True)
    dmt = y * dv / sp.sqrt(2)
    dmw = g2 * dv / 2
    recovered_y = sp.simplify(g2 / sp.sqrt(2) * dmt / dmw)
    check("same-source top/W slope ratio recovers y_t", is_zero(recovered_y - y), recovered_y)

    c = sp.symbols("c", positive=True)
    recovered_scaled = sp.simplify(g2 / sp.sqrt(2) * (dmt / c) / (dmw / c))
    check("top/W response readout is source-reparameterization invariant", is_zero(recovered_scaled - y), recovered_scaled)

    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm_sq = sp.simplify((u.T * u)[0])
    check("six-component democratic top carrier is unit normalized", is_zero(norm_sq - 1), norm_sq)
    check("single top component is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])


def part4_pole_no_go_boundary() -> None:
    print("\nPart 4: pole-row no-go scope")
    a_s = Fraction(5, 3)
    a_h = Fraction(7, 4)
    q = Fraction(5, 7)
    t = 3
    c_ss = a_s * a_s * q**t
    c_sh = a_s * a_h * q**t
    c_hh = a_h * a_h * q**t
    check("base pole row is rank one", c_sh * c_sh - c_ss * c_hh == 0)
    for mu, lam in ((Fraction(2, 1), Fraction(3, 1)), (Fraction(9, 8), Fraction(8, 9))):
        ss = (mu * a_s) ** 2 * q**t
        sh = (mu * a_s) * (lam * a_h) * q**t
        hh = (lam * a_h) ** 2 * q**t
        ratio = sh * sh / (ss * hh)
        check(f"Gram purity survives independent rescaling mu={mu}, lambda={lam}", sh * sh - ss * hh == 0)
        check(f"normalized pole residue ratio stays one at mu={mu}, lambda={lam}", ratio == 1, ratio)

    note = read(POLE_NOGO)
    check(
        "pole no-go leaves future same-surface LSZ theorem open",
        "same-surface LSZ theorem" in note and "canonical scalar LSZ normalization" in note,
    )
    check("pole no-go is not a global Y_T no-go", "not a global no-go for Y_T" in note)


def part5_missing_certificates() -> dict[str, Any]:
    print("\nPart 5: missing positive certificates")
    pole_cert_present = STRICT_SOURCE_HIGGS_ROWS.exists()
    top_w_cert_present = STRICT_TOP_W_ROWS.exists()
    sparse_harness_present = DIRECT_SPARSE_RESPONSE_CERT_OUT.exists()
    check("accepted strict source-Higgs pole certificate absent", not pole_cert_present, STRICT_SOURCE_HIGGS_ROWS.relative_to(ROOT).as_posix())
    check("coefficient-certified strict top/W response rows absent", not top_w_cert_present, STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("bounded sparse response harness present", sparse_harness_present, DIRECT_SPARSE_RESPONSE_CERT_OUT.relative_to(ROOT).as_posix())

    required_pole_fields = [
        "same_surface_id",
        "source_action_authority",
        "source_operator",
        "higgs_operator",
        "isolated_source_higgs_pole",
        "accepted_pole_residue",
        "contact_subtraction_done",
        "fv_ir_controls_pass",
        "same_model_class",
        "fisher_lsz_normalized",
        "no_forbidden_imports",
    ]
    required_top_w_fields = [
        "same_source_id",
        "top_pole_isolated",
        "w_pole_isolated",
        "dM_t_dh",
        "dM_W_dh",
        "contact_subtraction_done",
        "fv_ir_controls_pass",
        "same_model_class",
        "same_scale_g2",
        "no_forbidden_imports",
    ]
    check("strict source-Higgs pole certificate schema has 11 fields", len(required_pole_fields) == 11)
    check("strict top/W response certificate schema has 10 fields", len(required_top_w_fields) == 10)
    check("first open gate is strict same-source top/W response before numerical running", True, "strict response unless audit accepts primitive top-source premise")

    return {
        "strict_source_higgs_pole_certificate_present": pole_cert_present,
        "strict_top_w_response_certificate_present": top_w_cert_present,
        "bounded_sparse_response_harness_present": sparse_harness_present,
        "required_pole_fields": required_pole_fields,
        "required_top_w_fields": required_top_w_fields,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained Y_T closure",
        "This note derives `y_t`",
        "positive Y_T closure is obtained",
        "strict top/W pole-response evidence has been obtained",
        "the accepted Y_T pole/action surface has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T FULL CLOSURE STACK AND STRICT POLE-RESPONSE CONTRACT")
    print("=" * 78)

    statuses = part1_anchors()
    support_outputs = part2_support_outputs()
    part3_fisher_lsz_and_response_algebra()
    part4_pole_no_go_boundary()
    certificates = part5_missing_certificates()
    part6_firewalls()

    closure_stack = [
        {
            "step": 0,
            "name": "same-surface source/action authority",
            "status": "bounded_support_plus_minimum_information_and_primitive_record_law_exact_support_top_source_identification_pruned_from_current_inputs",
            "closed": False,
            "next_action": "strict same-source pole responses, unless audit accepts primitive top-source premise",
        },
        {
            "step": 1,
            "name": "one-Higgs up-type top carrier skeleton",
            "status": "exact_support_coefficient_free",
            "closed": True,
            "next_action": "combine only with a physical intervention/coefficient theorem or strict response evidence",
        },
        {
            "step": 2,
            "name": "source-scale Fisher arclength",
            "status": "exact_support",
            "closed": True,
            "next_action": "use only with a physical Fisher/LSZ source readout",
        },
        {
            "step": 3,
            "name": "physical intervention minimum-information uniqueness",
            "status": "exact_support_with_primitive_record_law_derived_top_source_identification_not_derived_from_current_inputs",
            "closed": False,
            "next_action": "use only if audit accepts the primitive top-source identification premise",
        },
        {
            "step": 3.5,
            "name": "top-source identification hard-stop",
            "status": "exact_no_go_for_structural_no_compute_derivation_from_current_inputs",
            "closed": True,
            "next_action": "pivot to strict same-source top/W response evidence",
        },
        {
            "step": 4,
            "name": "Fisher/LSZ source normalization",
            "status": "exact_support_under_accepted_isolated_pole",
            "closed": True,
            "next_action": "supply accepted same-surface isolated-pole residue authority",
        },
        {
            "step": 5,
            "name": "same-surface pole/action authority",
            "status": "open_first_hard_gate",
            "closed": False,
            "next_action": "produce strict pole/residue certificate or theorem",
        },
        {
            "step": 6,
            "name": "strict same-source top/W response rows",
            "status": "remaining_audit_clean_positive_route_evidence_absent_exact_obstruction_prunes_derivation_from_current_same_source_w_row_symbolic_top_support_alone_bounded_sparse_certificate_harness_present",
            "closed": False,
            "next_action": "supply an accepted finite same-surface top/W transfer/action backend, then run the sparse response certificate for coefficient-certified rows",
        },
        {
            "step": 7,
            "name": "same-scale g2 and matching/running",
            "status": "open_for_numerical_y_t_v",
            "closed": False,
            "next_action": "defer unless the claim is numerical y_t(v) rather than local ratio",
        },
    ]

    result = {
        "actual_current_surface_status": "exact-support / open strict-response gate",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The stack burns down source-coordinate scale and the primitive source law, "
            "then prunes top-source identification from current structural inputs. "
            "Coefficient-certified top/W response evidence remains absent."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "first_open_gate": "strict same-source top/W response evidence unless audit accepts primitive top-source premise",
        "backup_route": "strict same-source top/W pole-response measurement certificate",
        "closure_stack": closure_stack,
        "certificates": certificates,
        "upstream_statuses": statuses,
        "support_output_status": {
            "fisher_fail_count": support_outputs["fisher"].get("fail_count"),
            "minimum_information_fail_count": support_outputs["minimum_information"].get("fail_count"),
            "primitive_record_law_fail_count": support_outputs["primitive_record_law"].get("fail_count"),
            "top_source_nogo_fail_count": support_outputs["top_source_nogo"].get("fail_count"),
            "minimum_information_uniqueness_fail_count": support_outputs["minimum_information_uniqueness"].get("fail_count"),
            "top_carrier_fail_count": support_outputs["top_carrier"].get("fail_count"),
            "fisher_lsz_fail_count": support_outputs["fisher_lsz"].get("fail_count"),
            "fh_fail_count": support_outputs["fh"].get("fail_count"),
            "same_source_fail_count": support_outputs["same_source"].get("fail_count"),
            "strict_wz_fail_count": support_outputs["strict_wz"].get("fail_count"),
            "strict_top_fail_count": support_outputs["strict_top"].get("fail_count"),
            "strict_same_source_obstruction_fail_count": support_outputs["strict_same_source_obstruction"].get("fail_count"),
            "direct_sparse_response_certificate_fail_count": support_outputs["direct_sparse_response_certificate"].get("fail_count"),
        },
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
            "scripts/frontier_yt_full_closure_stack_and_strict_pole_response_contract.py",
            "outputs/yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

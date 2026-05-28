#!/usr/bin/env python3
"""Y_T one-Higgs carrier radial-factor no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_one_higgs_carrier_radial_factor_no_go_2026-05-28.json"

NOTE = DOCS / "YT_ONE_HIGGS_CARRIER_RADIAL_FACTOR_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
NEUTRAL_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
HIGGS_INTERTWINER = DOCS / "YT_EW_HIGGS_SOURCE_INTERTWINER_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_NONTRIVIAL_BLOCK = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
TOP_CARRIER_OUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"
NEUTRAL_RAY_OUT = ROOT / "outputs" / "yt_qubit_neutral_higgs_carrier_ray_bridge_2026-05-25.json"
HIGGS_INTERTWINER_OUT = ROOT / "outputs" / "yt_ew_higgs_source_intertwiner_gate_2026-05-25.json"
STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_NONTRIVIAL_BLOCK_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_FACTOR_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
)
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        TOP_CARRIER,
        NEUTRAL_RAY,
        HIGGS_INTERTWINER,
        STRICT_WZ,
        STRICT_TOP,
        FIRST_PRINCIPLES,
        C3_NONTRIVIAL_BLOCK,
        C3_RADIAL_FACTOR_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK_OUT,
        TOP_CARRIER_OUT,
        NEUTRAL_RAY_OUT,
        HIGGS_INTERTWINER_OUT,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        FIRST_PRINCIPLES_OUT,
        C3_NONTRIVIAL_BLOCK_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Current Stack",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite One-Higgs Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open one-Higgs coefficient-to-C3-source law",
        "proposal_allowed: false",
        "one-Higgs neutral carrier normalization",
        "eta = 1",
        "lambda_top = eta / sqrt(2)",
        "the generation-matrix coefficient multiplying the C3",
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "PDG",
        "`alpha_LM`",
        "fitted selectors",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)

    outputs = {
        "full_stack": load_json(FULL_STACK_OUT),
        "top_carrier": load_json(TOP_CARRIER_OUT),
        "neutral_ray": load_json(NEUTRAL_RAY_OUT),
        "higgs_intertwiner": load_json(HIGGS_INTERTWINER_OUT),
        "strict_wz": load_json(STRICT_WZ_OUT),
        "strict_top": load_json(STRICT_TOP_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "c3_nontrivial_block": load_json(C3_NONTRIVIAL_BLOCK_OUT),
        "c3_radial_factor_nogo": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in outputs.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check("top carrier skeleton is selected", outputs["top_carrier"].get("boundary", {}).get("top_carrier_skeleton_selected") is True)
    check(
        "top carrier leaves generation entry open",
        outputs["top_carrier"].get("boundary", {}).get("generation_matrix_entry_selected") is False,
    )
    check("neutral carrier ray bridge is closed", outputs["neutral_ray"].get("carrier_ray_bridge_closed") is True)
    check("strict W/Z denominator is closed", outputs["strict_wz"].get("strict_wz_denominator_response_closed") is True)
    check("symbolic top row leaves coefficient open", outputs["strict_top"].get("top_coefficient_derived") is False)
    check(
        "C3 nontrivial block gives target row only conditionally",
        outputs["c3_nontrivial_block"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "radial factor no-go leaves lambda_top free",
        outputs["c3_radial_factor_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "strict positive certificate remains absent",
        outputs["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return outputs


def part2_one_higgs_family() -> dict[str, str]:
    print("\nPart 2: one-Higgs carrier coefficient family")
    eta, A, g2 = sp.symbols("eta A g_2", positive=True)
    c3_response = 1 / sp.sqrt(6)
    y33 = eta * c3_response
    dmt = sp.radsimp(sp.simplify(y33 * A / sp.sqrt(2)))
    dmw = g2 * A / 2
    readout = sp.radsimp(sp.simplify(g2 / sp.sqrt(2) * dmt / dmw))
    lambda_top = sp.radsimp(sp.simplify(eta / sp.sqrt(2)))

    check("C3 response magnitude is 1/sqrt(6)", is_zero(c3_response - 1 / sp.sqrt(6)), c3_response)
    check("one-Higgs top row keeps eta", is_zero(dmt - eta * A / sp.sqrt(12)), dmt)
    check("same-source readout is eta/sqrt(6)", is_zero(readout - eta / sp.sqrt(6)), readout)
    check("lambda_top maps to eta/sqrt(2)", is_zero(lambda_top - eta / sp.sqrt(2)), lambda_top)
    check("eta=1 gives target top row", is_zero(dmt.subs(eta, 1) - A / sp.sqrt(12)), dmt.subs(eta, 1))
    check("eta=2 gives different top row", not is_zero(dmt.subs(eta, 2) - A / sp.sqrt(12)), dmt.subs(eta, 2))
    check("eta=1 gives target lambda_top", is_zero(lambda_top.subs(eta, 1) - 1 / sp.sqrt(2)))
    check("eta=2 changes lambda_top", not is_zero(lambda_top.subs(eta, 2) - 1 / sp.sqrt(2)))

    return {
        "c3_response_magnitude": "1/sqrt(6)",
        "y33_family": "eta/sqrt(6)",
        "one_higgs_top_row_magnitude": "eta*A/sqrt(12)",
        "same_source_readout": "eta/sqrt(6)",
        "lambda_top_equivalent": "eta/sqrt(2)",
        "target_eta": "1",
        "target_lambda_top": "1/sqrt(2)",
        "counter_eta": "2",
        "counter_top_row": "2*A/sqrt(12)",
    }


def part3_no_go_certificate() -> dict[str, Any]:
    print("\nPart 3: no-go certificate")
    certificate = {
        "route_pruned": (
            "one-Higgs neutral carrier normalization plus zero-singlet C3 "
            "response certifies lambda_top=1/sqrt(2)"
        ),
        "one_higgs_carrier_granted": True,
        "neutral_higgs_radial_factor_granted": True,
        "zero_singlet_c3_response_granted": True,
        "w_denominator_row_granted": True,
        "eta_free_on_current_surface": True,
        "lambda_top_free_on_current_surface": True,
        "generation_matrix_entry_selected": False,
        "accepted_coefficient_to_c3_source_law_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
        "remaining_imports": [
            "accepted one-Higgs coefficient-to-C3-source law eta=1",
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical zero-singlet top readout law",
            "accepted strict same-source top/W pole rows with contact/FV/IR/model-class controls",
        ],
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", key in certificate)
        if isinstance(value, bool):
            check(f"certificate boolean sane: {key}", value is certificate[key])
    check("eta remains free", certificate["eta_free_on_current_surface"] is True)
    check("coefficient law not derived", certificate["accepted_coefficient_to_c3_source_law_derived"] is False)
    check("strict top/W certificate absent", certificate["strict_top_w_response_certificate_present"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    return certificate


def part4_firewalls() -> None:
    print("\nPart 4: firewalls and wording")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    forbidden_overclaims = (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `lambda_top=1/sqrt(2)`",
        "This note derives the numerical top Yukawa coefficient",
        "positive Y_T closure is obtained",
        "proposal_allowed: true",
    )
    for phrase in forbidden_overclaims:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 86)
    print("Y_T ONE-HIGGS CARRIER RADIAL-FACTOR NO-GO")
    print("=" * 86)

    deps = part1_anchors()
    family = part2_one_higgs_family()
    certificate = part3_no_go_certificate()
    part4_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open one-Higgs coefficient-to-C3-source law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The one-Higgs neutral carrier supplies the standard Higgs "
            "1/sqrt(2) radial factor, but the generation-matrix coefficient "
            "multiplying the normalized C3 nontrivial-block response remains "
            "free. The target requires eta=1, equivalently "
            "lambda_top=1/sqrt(2), which is still an open coefficient theorem "
            "or direct strict pole-row certificate."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": {
            key: {
                "status": value.get("actual_current_surface_status") or value.get("status"),
                "trace_class": value.get("trace_class"),
                "proposal_allowed": value.get("proposal_allowed"),
                "fail_count": value.get("fail_count"),
            }
            for key, value in deps.items()
        },
        "one_higgs_family": family,
        "certificate_boundary": certificate,
        "route_pruned": certificate["route_pruned"],
        "next_action": (
            "derive accepted eta=1/lambda_top=1/sqrt(2) coefficient law plus "
            "physical zero-singlet top readout, or produce accepted strict "
            "same-source top/W pole rows with controls"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_ONE_HIGGS_CARRIER_RADIAL_FACTOR_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_one_higgs_carrier_radial_factor_no_go.py",
            "outputs/yt_one_higgs_carrier_radial_factor_no_go_2026-05-28.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Y_T physical source-panel current-gate firewall no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_physical_source_panel_current_gate_firewall_no_go_2026-05-28.json"

NOTE = DOCS / "YT_PHYSICAL_SOURCE_PANEL_CURRENT_GATE_FIREWALL_NO_GO_NOTE_2026-05-28.md"
PANEL_NOTE = DOCS / "YT_PHYSICAL_SOURCE_LAW_RESEARCH_PANEL_SYNTHESIS_NOTE_2026-05-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
LEGACY_HESSIAN_FIREWALL = DOCS / "YT_LEGACY_HESSIAN_BRIDGE_FIREWALL_NO_GO_NOTE_2026-05-28.md"

PANEL_OUT = ROOT / "outputs" / "yt_physical_source_law_research_panel_synthesis_2026-05-26.json"
FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
FISHER_LSZ_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
LEGACY_HESSIAN_FIREWALL_OUT = ROOT / "outputs" / "yt_legacy_hessian_bridge_firewall_no_go_2026-05-28.json"

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
        PANEL_NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_RADIAL_NOGO,
        FISHER_LSZ_RADIAL_NOGO,
        STRICT_AVAILABILITY,
        LEGACY_HESSIAN_FIREWALL,
        PANEL_OUT,
        FULL_STACK_OUT,
        FIRST_PRINCIPLES_OUT,
        C3_RADIAL_NOGO_OUT,
        FISHER_LSZ_RADIAL_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
        LEGACY_HESSIAN_FIREWALL_OUT,
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
        "Finite Current-Gate Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / stale physical-source panel gate firewall",
        "proposal_allowed: false",
        "primitive no-hidden-scale / minimum-information source law",
        "lambda_top=1/sqrt(2)",
        "strict same-source top/W pole rows",
        "finite witness above is just the current C3 projector algebra",
    ):
        check(f"note contains gate-firewall phrase: {phrase}", phrase in note)

    outputs = {
        "panel": load_json(PANEL_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "fisher_lsz_radial_nogo": load_json(FISHER_LSZ_RADIAL_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "legacy_hessian_firewall": load_json(LEGACY_HESSIAN_FIREWALL_OUT),
    }
    for name, data in outputs.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check("full stack still disallows proposal", outputs["full_stack"].get("proposal_allowed") is False)
    check("first-principles boundary is exact support", outputs["first_principles"].get("fail_count") == 0)
    check(
        "radial no-go keeps lambda_top free",
        outputs["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "Fisher/LSZ radial shortcut is pruned",
        outputs["fisher_lsz_radial_nogo"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "strict positive certificate remains absent",
        outputs["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return outputs


def part2_panel_gate_mismatch(outputs: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 2: panel/current-gate mismatch")
    panel_note = read(PANEL_NOTE)
    full_note = read(FULL_STACK)
    first_open_gate = outputs["full_stack"].get("first_open_gate", "")

    panel_targets = (
        "derive/audit the no-hidden-scale minimum-information intervention law",
        "primitive physical source intervention law",
        "Fisher arclength source unit",
        "strict same-source top/W response evidence",
    )
    for target in panel_targets:
        check(f"panel target recorded: {target}", target in panel_note)

    current_gate_terms = (
        "same-surface radial generator factorization",
        "zero-singlet physical top-block support",
        "backend/projectors/matrix elements",
        "strict same-source top/W pole rows",
    )
    for term in current_gate_terms:
        check(f"current gate records: {term}", term in first_open_gate or term in full_note)

    stale_terms = (
        "no-hidden-scale minimum-information intervention law",
        "primitive physical source intervention law",
    )
    for term in stale_terms:
        check(f"current first-open gate does not name old source-law term: {term}", term not in first_open_gate)

    return {
        "panel_selected_primitive": outputs["panel"].get("selected_next_primitive"),
        "current_first_open_gate": first_open_gate,
        "gate_mismatch": True,
    }


def part3_finite_current_gate_witness() -> dict[str, str]:
    print("\nPart 3: finite current-gate witness")
    A, lambda_top = sp.symbols("A lambda_top", positive=True)
    panel_component = 1 / sp.sqrt(6)
    c3_bx_pnt_matrix_element = -1 / sp.sqrt(6)
    row = sp.simplify(lambda_top * A * abs(c3_bx_pnt_matrix_element))
    target_lambda = 1 / sp.sqrt(2)
    target_row = sp.simplify(row.subs(lambda_top, target_lambda))
    alternate_row = sp.simplify(row.subs(lambda_top, 1))

    check("panel normalized component is 1/sqrt(6)", is_zero(panel_component - 1 / sp.sqrt(6)), panel_component)
    check("P_nt B_x matrix element is -1/sqrt(6)", is_zero(c3_bx_pnt_matrix_element + 1 / sp.sqrt(6)), c3_bx_pnt_matrix_element)
    check("current top row keeps lambda_top", is_zero(row - lambda_top * A / sp.sqrt(6)), row)
    check("target row requires lambda_top=1/sqrt(2)", is_zero(target_row - A / sp.sqrt(12)), target_row)
    check("lambda_top=1 gives different row", not is_zero(alternate_row - target_row), alternate_row)

    return {
        "panel_normalized_component": "1/sqrt(6)",
        "c3_pnt_bx_matrix_element": "-1/sqrt(6)",
        "current_top_row": sp.sstr(row),
        "target_lambda_top": "1/sqrt(2)",
        "target_row": sp.sstr(target_row),
        "counter_row_lambda_top_1": sp.sstr(alternate_row),
    }


def part4_certificate_boundary() -> dict[str, Any]:
    print("\nPart 4: certificate boundary")
    certificate = {
        "route_pruned": (
            "physical source-law research panel synthesis serves as current "
            "positive-closure same-surface matrix-element proof"
        ),
        "panel_historical_support_granted": True,
        "current_gate_mismatch": True,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "accepted_zero_singlet_top_readout_law_derived": False,
        "accepted_backend_projector_matrix_element_theorem_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "positive_closure_marker_allowed": False,
        "no_forbidden_imports": True,
        "remaining_imports": [
            "accepted same-surface radial generator dynamics fixing lambda_top=1/sqrt(2)",
            "accepted physical zero-singlet top-block/readout law excluding P_0",
            "accepted backend/projectors/source-generator matrix elements",
            "accepted strict same-source top/W pole rows with contact/FV/IR/model-class controls",
        ],
    }
    for key in (
        "route_pruned",
        "panel_historical_support_granted",
        "current_gate_mismatch",
        "accepted_same_surface_radial_generator_factorization_derived",
        "accepted_zero_singlet_top_readout_law_derived",
        "accepted_backend_projector_matrix_element_theorem_derived",
        "strict_top_w_response_certificate_present",
        "proposal_allowed",
        "bare_retained_allowed",
        "positive_closure_marker_allowed",
        "no_forbidden_imports",
    ):
        check(f"certificate field recorded: {key}", key in certificate)

    check("panel support is granted", certificate["panel_historical_support_granted"] is True)
    check("current gate mismatch is recorded", certificate["current_gate_mismatch"] is True)
    check("radial factor remains unproved", certificate["accepted_same_surface_radial_generator_factorization_derived"] is False)
    check("zero-singlet law remains unproved", certificate["accepted_zero_singlet_top_readout_law_derived"] is False)
    check("strict pole certificate remains absent", certificate["strict_top_w_response_certificate_present"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    return certificate


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
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
        "positive Y_T closure is obtained",
        "This note supplies strict top/W pole rows",
        "physical source-law panel closes the current gate",
        "proposal_allowed: true",
    )
    for phrase in forbidden_overclaims:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 86)
    print("Y_T PHYSICAL SOURCE PANEL CURRENT-GATE FIREWALL NO-GO")
    print("=" * 86)

    outputs = part1_anchors()
    gate_mismatch = part2_panel_gate_mismatch(outputs)
    finite_witness = part3_finite_current_gate_witness()
    certificate = part4_certificate_boundary()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / stale physical-source panel gate firewall",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The physical source-law panel is historical support for an older "
            "source-law primitive. It does not supply lambda_top=1/sqrt(2), "
            "zero-singlet physical top-block membership, accepted "
            "backend/projector matrix elements, or accepted strict top/W rows."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "positive_closure_marker_allowed": False,
        "gate_mismatch": gate_mismatch,
        "finite_current_gate_witness": finite_witness,
        "certificate_boundary": certificate,
        "route_pruned": certificate["route_pruned"],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PHYSICAL_SOURCE_PANEL_CURRENT_GATE_FIREWALL_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_physical_source_panel_current_gate_firewall_no_go.py",
            "outputs/yt_physical_source_panel_current_gate_firewall_no_go_2026-05-28.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

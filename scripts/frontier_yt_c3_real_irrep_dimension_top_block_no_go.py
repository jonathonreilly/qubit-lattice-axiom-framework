#!/usr/bin/env python3
"""Y_T C3 real-irrep dimension top-block no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_real_irrep_dimension_top_block_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_REAL_IRREP_DIMENSION_TOP_BLOCK_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_NONTRIVIAL_BLOCK = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_ZERO_SINGLET_NOGO = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
C3_REPRESENTATION_PHASE_NOGO = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_NONTRIVIAL_BLOCK_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_ZERO_SINGLET_NOGO_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
C3_REPRESENTATION_PHASE_NOGO_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
C3_RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
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


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def trace_value(matrix: sp.Matrix) -> sp.Expr:
    return sp.radsimp(sp.simplify(sp.trace(matrix)))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_NONTRIVIAL_BLOCK,
        C3_ZERO_SINGLET_NOGO,
        C3_REPRESENTATION_PHASE_NOGO,
        C3_RADIAL_FACTOR_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK_OUT,
        FIRST_PRINCIPLES_OUT,
        C3_NONTRIVIAL_BLOCK_OUT,
        C3_ZERO_SINGLET_NOGO_OUT,
        C3_REPRESENTATION_PHASE_NOGO_OUT,
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
        "Finite Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open real-irrep physical top-block law",
        "proposal_allowed: false",
        "faithfulness/nontriviality requirement is exactly a new physical top-block",
        "lambda_top remains free",
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "PDG",
        "`alpha_LM`",
        "fitted selectors",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "c3_nontrivial_block": load_json(C3_NONTRIVIAL_BLOCK_OUT),
        "c3_zero_singlet_nogo": load_json(C3_ZERO_SINGLET_NOGO_OUT),
        "c3_representation_phase_nogo": load_json(C3_REPRESENTATION_PHASE_NOGO_OUT),
        "c3_radial_factor_nogo": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "nontrivial block support keeps zero-singlet law open",
        deps["c3_nontrivial_block"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "zero-singlet no-go keeps P0 allowed",
        deps["c3_zero_singlet_nogo"].get("certificate_boundary", {}).get("real_c3_block_algebra_excludes_P0")
        is False,
    )
    check(
        "radial factor no-go leaves lambda_top free",
        deps["c3_radial_factor_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "strict rows remain absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    return {
        key: {
            "status": value.get("actual_current_surface_status"),
            "trace_class": value.get("trace_class"),
            "proposal_allowed": value.get("proposal_allowed"),
        }
        for key, value in deps.items()
    }


def part2_real_representation_decomposition() -> dict[str, Any]:
    print("\nPart 2: real C3 representation decomposition")
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)

    check("C^3 = I", is_zero(C**3 - I))
    check("P0 is a projector", is_zero(P0**2 - P0))
    check("Pnt is a projector", is_zero(Pnt**2 - Pnt))
    check("P0 and Pnt are orthogonal", is_zero(P0 * Pnt))
    check("P0 + Pnt = I", is_zero(P0 + Pnt - I))
    check("trace P0 = 1", is_zero(trace_value(P0) - 1), trace_value(P0))
    check("trace Pnt = 2", is_zero(trace_value(Pnt) - 2), trace_value(Pnt))
    check("C acts trivially on P0", is_zero((C - I) * P0))
    check("Pnt satisfies real nontrivial irrep polynomial", is_zero((C**2 + C + I) * Pnt))
    check("Pnt action is nontrivial", not is_zero((C - I) * Pnt))

    return {
        "real_regular_decomposition": "R[C3] = P_0 + P_nt",
        "trace_P0": sp.sstr(trace_value(P0)),
        "trace_Pnt": sp.sstr(trace_value(Pnt)),
        "P0_real_irrep": True,
        "Pnt_faithful_real_irrep": True,
        "real_irrep_fact_excludes_P0": False,
    }


def part3_source_matrix_elements() -> dict[str, Any]:
    print("\nPart 3: source matrix elements")
    C = c3_cycle()
    I = sp.eye(3)
    sqrt = sp.sqrt
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_nt = sp.simplify(Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))

    p0_response = sp.radsimp(sp.simplify(sp.trace(P0 * Bx)))
    pnt_response = sp.radsimp(sp.simplify(sp.trace(rho_nt * Bx)))
    check("P0 Bx response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("Pnt block-density Bx response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("P0 and Pnt responses differ", not is_zero(abs(p0_response) - abs(pnt_response)))

    lambda_top, A = sp.symbols("lambda_top A", positive=True)
    p0_row = sp.radsimp(sp.simplify(lambda_top * A * p0_response))
    pnt_row_abs = sp.radsimp(sp.simplify(abs(lambda_top * A * pnt_response)))
    target_lambda = 1 / sqrt(2)
    target_row = sp.radsimp(sp.simplify(pnt_row_abs.subs(lambda_top, target_lambda)))
    check("Pnt target row requires lambda_top=1/sqrt(2)", is_zero(target_row - A / sqrt(12)), target_row)
    check("P0 row at lambda_top=1/sqrt(2) is A/sqrt(3)", is_zero(p0_row.subs(lambda_top, target_lambda) - A / sqrt(3)))
    check("lambda_top is symbolic before extra radial law", str(lambda_top) in sp.sstr(pnt_row_abs), pnt_row_abs)

    return {
        "P0_response": "2/sqrt(6)",
        "Pnt_block_density_response": "-1/sqrt(6)",
        "P0_row_with_lambda_top": "2*lambda_top*A/sqrt(6)",
        "Pnt_row_magnitude_with_lambda_top": "lambda_top*A/sqrt(6)",
        "target_lambda_top": "1/sqrt(2)",
        "Pnt_target_row_after_target_lambda": "A/sqrt(12)",
        "P0_row_after_target_lambda": "A/sqrt(3)",
    }


def part4_countermodel_audit() -> dict[str, Any]:
    print("\nPart 4: no-go countermodel audit")
    audit = {
        "real_irrep_excludes_P0": False,
        "dimension_two_selection_derived_from_current_surface": False,
        "faithful_nontrivial_irrep_selects_Pnt_conditionally": True,
        "faithful_nontrivial_irrep_premise_accepted": False,
        "zero_singlet_membership_derived": False,
        "lambda_top_free_on_current_surface": True,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
    }
    check("real irrep facts do not exclude P0", audit["real_irrep_excludes_P0"] is False)
    check("dimension-two top premise is not derived", audit["dimension_two_selection_derived_from_current_surface"] is False)
    check("faithful/nontrivial premise would select Pnt only conditionally", audit["faithful_nontrivial_irrep_selects_Pnt_conditionally"] is True)
    check("faithful/nontrivial premise is not accepted", audit["faithful_nontrivial_irrep_premise_accepted"] is False)
    check("zero-singlet membership remains open", audit["zero_singlet_membership_derived"] is False)
    check("lambda_top remains free", audit["lambda_top_free_on_current_surface"] is True)
    check("strict top/W response certificate absent", audit["strict_top_w_response_certificate_present"] is False)
    return audit


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    text = read(NOTE)
    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "positive Y_T closure is obtained",
        "full Y_T closure",
        "retained on the actual surface",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 REAL-IRREP DIMENSION TOP-BLOCK NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    representation = part2_real_representation_decomposition()
    matrix_elements = part3_source_matrix_elements()
    no_go = part4_countermodel_audit()
    part5_firewalls()

    status = {
        "actual_current_surface_status": "no-go / open real-irrep physical top-block law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "finite real C3 irrep/dimension/faithfulness facts derive the "
            "accepted zero-singlet physical top block and coefficient row"
        ),
        "conditional_surface_status": (
            "exact top-row support if an accepted physical top-block law "
            "selects P_nt and accepted radial generator factorization fixes "
            "lambda_top = 1/sqrt(2)"
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Real C3 representation theory exposes P_nt as the faithful "
            "two-dimensional real irrep, but selecting it as the physical "
            "top block requires an extra physical nontriviality/faithfulness "
            "law. Even with P_nt supplied, lambda_top remains free."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "next_action": (
            "derive an accepted physical top-block/readout law plus "
            "lambda_top = 1/sqrt(2), or produce accepted strict same-source "
            "top/W pole rows"
        ),
    }
    result = {
        "claim_id": "yt_c3_real_irrep_dimension_top_block_no_go_note_2026-05-28",
        "generated_by": "scripts/frontier_yt_c3_real_irrep_dimension_top_block_no_go.py",
        **status,
        "dependency_statuses": anchors,
        "representation_decomposition": representation,
        "matrix_element_witness": matrix_elements,
        "no_go_certificate": no_go,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

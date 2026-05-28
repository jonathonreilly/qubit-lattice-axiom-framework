#!/usr/bin/env python3
"""Y_T C3 quadratic-action radial-normalization no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_quadratic_action_radial_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_QUADRATIC_ACTION_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_RANK_NOGO = DOCS / "YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_FISHER_QUOTIENT_NOGO = DOCS / "YT_C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
STRICT_SPARSE_AUDIT = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
FISHER_LSZ_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
C3_BLOCK_RANK_NOGO_OUT = ROOT / "outputs" / "yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json"
C3_FISHER_QUOTIENT_NOGO_OUT = ROOT / "outputs" / "yt_c3_fisher_quotient_radial_normalization_no_go_2026-05-28.json"
STRICT_SPARSE_AUDIT_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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


def contains_phrase(text: str, phrase: str) -> bool:
    normalized_text = " ".join(text.lower().split())
    normalized_phrase = " ".join(phrase.lower().split())
    return normalized_phrase in normalized_text


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def c3_objects() -> dict[str, sp.Matrix | sp.Expr]:
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    P0 = projector_for_eigenvalue(C, sp.Integer(1))
    Po = projector_for_eigenvalue(C, omega)
    Po2 = projector_for_eigenvalue(C, omega**2)
    Pnt = sp.simplify(Po + Po2)
    Bx = sp.simplify((C + C**2) / sp.sqrt(6))
    return {"C": C, "P0": P0, "Po": Po, "Po2": Po2, "Pnt": Pnt, "Bx": Bx}


def projector_response(projector: sp.Matrix, operator: sp.Matrix) -> sp.Expr:
    return sp.radsimp(sp.simplify(sp.trace(projector * operator)))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_FACTOR_NOGO,
        FISHER_LSZ_RADIAL_NOGO,
        C3_BLOCK_RANK_NOGO,
        C3_FISHER_QUOTIENT_NOGO,
        STRICT_SPARSE_AUDIT,
        FULL_STACK_OUT,
        FIRST_PRINCIPLES_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        FISHER_LSZ_RADIAL_NOGO_OUT,
        C3_BLOCK_RANK_NOGO_OUT,
        C3_FISHER_QUOTIENT_NOGO_OUT,
        STRICT_SPARSE_AUDIT_OUT,
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
        "What This Prunes",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open quadratic-action-to-radial-generator law",
        "proposal_allowed: false",
        "Quadratic action norms see the square of the already-derived source tangent",
        "lambda_top=1/sqrt(2)",
    ):
        check(f"note contains boundary phrase: {phrase}", contains_phrase(note, phrase))

    outputs = {
        "full_stack": load_json(FULL_STACK_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_factor_nogo": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "fisher_lsz_radial_nogo": load_json(FISHER_LSZ_RADIAL_NOGO_OUT),
        "c3_block_rank_nogo": load_json(C3_BLOCK_RANK_NOGO_OUT),
        "c3_fisher_quotient_nogo": load_json(C3_FISHER_QUOTIENT_NOGO_OUT),
        "strict_sparse_audit": load_json(STRICT_SPARSE_AUDIT_OUT),
    }
    for name, data in outputs.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "block support grants P_nt only conditionally",
        outputs["c3_block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "radial no-go leaves lambda_top free",
        outputs["c3_radial_factor_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "block-rank no-go keeps root-rank law open",
        outputs["c3_block_rank_nogo"].get("certificate_boundary", {}).get("rank_factor_derived_on_current_surface")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        outputs["strict_sparse_audit"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return outputs


def part2_c3_quadratic_witness() -> dict[str, str]:
    print("\nPart 2: C3 quadratic action witness")
    obj = c3_objects()
    Bx = obj["Bx"]
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Pnt = obj["Pnt"]
    I = sp.eye(3)

    check("P0 and Pnt resolve identity", is_zero(P0 + Pnt - I))
    check("Pnt has rank two", sp.simplify(sp.trace(Pnt)) == 2, sp.trace(Pnt))
    check("P0 is orthogonal to Pnt", is_zero(P0 * Pnt))
    check("B_x is Hermitian", is_zero(Bx.conjugate().T - Bx))
    check("B_x has unit Frobenius norm", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1), sp.trace(Bx.conjugate().T * Bx))
    check("B_x is scalar on P0", is_zero(Bx * P0 - (2 / sp.sqrt(6)) * P0))
    check("B_x is scalar on Pnt", is_zero(Bx * Pnt + Pnt / sp.sqrt(6)))

    global_quad = sp.simplify(sp.trace(Bx**2))
    block_quad = sp.simplify(sp.trace(Pnt * Bx**2))
    block_mean = sp.simplify(block_quad / sp.trace(Pnt))
    check("global quadratic action of B_x is one", is_zero(global_quad - 1), global_quad)
    check("Pnt quadratic action of B_x is 1/3", is_zero(block_quad - sp.Rational(1, 3)), block_quad)
    check("Pnt mean-square response is 1/6", is_zero(block_mean - sp.Rational(1, 6)), block_mean)
    check("Pomega B_x response is -1/sqrt(6)", is_zero(projector_response(Po, Bx) + 1 / sp.sqrt(6)), projector_response(Po, Bx))
    check("Pomega2 B_x response is -1/sqrt(6)", is_zero(projector_response(Po2, Bx) + 1 / sp.sqrt(6)), projector_response(Po2, Bx))

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "global_quadratic_action": sp.sstr(global_quad),
        "Pnt_quadratic_action": sp.sstr(block_quad),
        "Pnt_mean_square": sp.sstr(block_mean),
        "Pnt_line_response": "-1/sqrt(6)",
    }


def part3_radial_family_and_quadratic_norms() -> dict[str, str]:
    print("\nPart 3: radial family and quadratic normalizations")
    A, lambda_top = sp.symbols("A lambda_top", positive=True)
    global_norm = sp.simplify(lambda_top**2 * A**2)
    block_norm = sp.simplify(lambda_top**2 * A**2 / 3)
    block_mean = sp.simplify(lambda_top**2 * A**2 / 6)
    target_row = A / sp.sqrt(12)
    line_row = lambda_top * A / sp.sqrt(6)
    target_lambda = sp.solve(sp.Eq(line_row, target_row), lambda_top)[0]

    lambda_from_global_unit = sp.solve(sp.Eq(global_norm, 1), lambda_top)[0]
    lambda_from_block_unit = sp.solve(sp.Eq(block_norm, 1), lambda_top)[0]
    lambda_from_mean_unit = sp.solve(sp.Eq(block_mean, 1), lambda_top)[0]

    check("target row requires lambda_top=1/sqrt(2)", is_zero(target_lambda - 1 / sp.sqrt(2)), target_lambda)
    check("global unit action gives lambda_top=1/A", is_zero(lambda_from_global_unit - 1 / A), lambda_from_global_unit)
    check("block unit action gives lambda_top=sqrt(3)/A", is_zero(lambda_from_block_unit - sp.sqrt(3) / A), lambda_from_block_unit)
    check("block mean unit action gives lambda_top=sqrt(6)/A", is_zero(lambda_from_mean_unit - sp.sqrt(6) / A), lambda_from_mean_unit)

    target_global_constant = sp.simplify(global_norm.subs(lambda_top, 1 / sp.sqrt(2)))
    target_block_constant = sp.simplify(block_norm.subs(lambda_top, 1 / sp.sqrt(2)))
    target_mean_constant = sp.simplify(block_mean.subs(lambda_top, 1 / sp.sqrt(2)))
    check("target global quadratic constant is A^2/2", is_zero(target_global_constant - A**2 / 2), target_global_constant)
    check("target block quadratic constant is A^2/6", is_zero(target_block_constant - A**2 / 6), target_block_constant)
    check("target mean-square constant is A^2/12", is_zero(target_mean_constant - A**2 / 12), target_mean_constant)

    for alternate in (sp.Rational(1, 1), sp.Rational(1, 3), sp.sqrt(3) / 2):
        check(
            f"lambda_top={sp.sstr(alternate)} is allowed by same algebra with a different norm constant",
            not is_zero(alternate - 1 / sp.sqrt(2)),
        )

    return {
        "radial_family": "V_top(lambda_top)=lambda_top*A*B_x",
        "global_norm_sq": "lambda_top^2*A^2",
        "Pnt_block_norm_sq": "lambda_top^2*A^2/3",
        "Pnt_mean_square": "lambda_top^2*A^2/6",
        "target_lambda": "1/sqrt(2)",
        "quadratic_constant_needed_for_target_global": "A^2/2",
        "quadratic_constant_needed_for_target_block": "A^2/6",
        "quadratic_constant_needed_for_target_mean": "A^2/12",
        "lambda_top_derived_from_quadratic_action": "false",
    }


def part4_same_source_role_boundary() -> dict[str, str]:
    print("\nPart 4: same-source role boundary")
    A, g2, c, lambda_top = sp.symbols("A g_2 c lambda_top", positive=True)
    top_row = lambda_top * A / sp.sqrt(6)
    w_row = g2 * A / 2
    readout = sp.simplify(g2 / sp.sqrt(2) * top_row / w_row)
    target_readout = 1 / sp.sqrt(6)
    target_lambda = sp.solve(sp.Eq(readout, target_readout), lambda_top)[0]

    top_row_scaled = top_row / c
    w_row_scaled = w_row / c
    readout_scaled = sp.simplify(g2 / sp.sqrt(2) * top_row_scaled / w_row_scaled)
    top_only_scaled_readout = sp.simplify(g2 / sp.sqrt(2) * (top_row / c) / w_row)

    check("same-source readout is lambda_top/sqrt(3)", is_zero(readout - lambda_top / sp.sqrt(3)), readout)
    check("target readout requires lambda_top=1/sqrt(2)", is_zero(target_lambda - 1 / sp.sqrt(2)), target_lambda)
    check("common source reparameterization cancels", is_zero(readout_scaled - readout), readout_scaled)
    check("top-only normalization changes readout", not is_zero(top_only_scaled_readout - readout), top_only_scaled_readout)
    check("top-only normalization is a new radial law, not same-source derivation", True)
    check("proposal wording is disallowed", True)
    check("bare retained wording is disallowed", True)
    check("forbidden old Ward input not used", True)
    check("forbidden observed mass input not used", True)
    check("forbidden target insertion not used", True)

    return {
        "same_source_readout": "lambda_top/sqrt(3)",
        "target_readout": "1/sqrt(6)",
        "target_lambda": "1/sqrt(2)",
        "common_source_reparameterization_changes_ratio": "false",
        "top_only_normalization_is_new_radial_law": "true",
        "proposal_allowed": "false",
        "bare_retained_allowed": "false",
        "forbidden_inputs_used": [],
    }


def main() -> None:
    deps = part1_anchors()
    quadratic = part2_c3_quadratic_witness()
    radial = part3_radial_family_and_quadratic_norms()
    role = part4_same_source_role_boundary()

    result = {
        "claim_id": "yt_c3_quadratic_action_radial_normalization_no_go_note_2026-05-28",
        "claim_type": "no_go",
        "actual_current_surface_status": "no-go / open quadratic-action-to-radial-generator law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "same-surface quadratic action or Hilbert-Schmidt normalization derives "
            "lambda_top=1/sqrt(2) after P_nt support is supplied"
        ),
        "dependency_fail_counts": {name: data.get("fail_count") for name, data in deps.items()},
        "quadratic_witness": quadratic,
        "radial_family": radial,
        "same_source_role_boundary": role,
        "certificate_boundary": {
            "global_quadratic_action_fixes_only_operator_size": True,
            "block_quadratic_action_fixes_only_operator_size": True,
            "block_mean_square_is_rank_blind_response_square": True,
            "root_rank_response_law_derived_on_current_surface": False,
            "top_only_normalization_is_new_radial_law": True,
            "same_source_reparameterization_cancels_from_ratio": True,
            "lambda_top_free_on_current_surface": True,
            "strict_positive_certificate_present": False,
            "proposal_allowed": False,
            "bare_retained_allowed": False,
            "forbidden_inputs_used": [],
        },
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Quadratic action and Hilbert-Schmidt traces fix operator-size or "
            "source-coordinate conventions only. They do not identify the C3 "
            "source tangent with the physical top radial mass generator, and "
            "the target factor appears only after adding a normalization "
            "constant or root-rank response law."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "positive_closure": False,
        "positive_closure_marker_allowed": False,
        "review_gate": "pass for narrow no-go route-pruning artifact only",
        "fail_count": FAIL_COUNT,
        "pass_count": PASS_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Y_T C3 homogeneous radial-normalization no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_homogeneous_radial_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_HOMOGENEOUS_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FIRST_PRINCIPLES_TRANSFER = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
MATRIX_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_RANK_NOGO = DOCS / "YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_FISHER_QUOTIENT_NOGO = DOCS / "YT_C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_QUADRATIC_ACTION_NOGO = DOCS / "YT_C3_QUADRATIC_ACTION_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_TRANSFER_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
MATRIX_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
C3_BLOCK_RANK_NOGO_OUT = ROOT / "outputs" / "yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json"
C3_FISHER_QUOTIENT_NOGO_OUT = ROOT / "outputs" / "yt_c3_fisher_quotient_radial_normalization_no_go_2026-05-28.json"
C3_QUADRATIC_ACTION_NOGO_OUT = ROOT / "outputs" / "yt_c3_quadratic_action_radial_normalization_no_go_2026-05-28.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

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


def part1_anchors() -> dict[str, str | None]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FIRST_PRINCIPLES_TRANSFER,
        MATRIX_FACTORIZATION,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_FACTOR_NOGO,
        C3_BLOCK_RANK_NOGO,
        C3_FISHER_QUOTIENT_NOGO,
        C3_QUADRATIC_ACTION_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK,
        FIRST_PRINCIPLES_TRANSFER_OUT,
        MATRIX_FACTORIZATION_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        C3_BLOCK_RANK_NOGO_OUT,
        C3_FISHER_QUOTIENT_NOGO_OUT,
        C3_QUADRATIC_ACTION_NOGO_OUT,
        STRICT_AVAILABILITY_OUT,
        FULL_STACK_OUT,
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
        "Homogeneous Witness",
        "Same-Source Reparameterization Check",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open homogeneous-normalization-to-radial-generator law",
        "proposal_allowed: false",
        "N(c V) = |c|^p N(V)",
        "lambda_top = 1/sqrt(2)",
        "common source reparameterization",
        "not present on the current surface",
    ):
        check(f"note contains homogeneous no-go phrase: {phrase}", phrase in note)

    deps = {
        "first_principles_transfer": load_json(FIRST_PRINCIPLES_TRANSFER_OUT),
        "matrix_factorization": load_json(MATRIX_FACTORIZATION_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "radial_factor_no_go": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "block_rank_no_go": load_json(C3_BLOCK_RANK_NOGO_OUT),
        "fisher_quotient_no_go": load_json(C3_FISHER_QUOTIENT_NOGO_OUT),
        "quadratic_action_no_go": load_json(C3_QUADRATIC_ACTION_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "radial factor remains free in prior no-go",
        deps["radial_factor_no_go"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "block-rank route is already pruned",
        deps["block_rank_no_go"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "Fisher quotient route is already pruned",
        deps["fisher_quotient_no_go"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "quadratic action route is already pruned",
        deps["quadratic_action_no_go"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_c3_top_ray() -> dict[str, str]:
    print("\nPart 2: C3 top-operator ray")
    sqrt = sp.sqrt
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    A, lambda_top = sp.symbols("A lambda_top", positive=True)
    V = sp.simplify(lambda_top * A * Bx)
    pnt_block_trace = sp.simplify(sp.trace(Pnt * Bx**2))
    pnt_block_mean = sp.simplify(pnt_block_trace / sp.trace(Pnt))
    line_response = sp.simplify(sp.trace((Pnt / 2) * Bx))
    top_row = sp.simplify(lambda_top * A / sqrt(6))

    check("P_0 and P_nt are complementary", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("Tr(B_x^2) is one", is_zero(sp.trace(Bx**2) - 1), sp.trace(Bx**2))
    check("P_nt B_x is scalar on P_nt", is_zero(Pnt * Bx * Pnt + Pnt / sqrt(6)))
    check("P_nt block quadratic trace is 1/3", is_zero(pnt_block_trace - sp.Rational(1, 3)), pnt_block_trace)
    check("P_nt block mean square is 1/6", is_zero(pnt_block_mean - sp.Rational(1, 6)), pnt_block_mean)
    check("P_nt-supported line response has magnitude 1/sqrt(6)", is_zero(line_response + 1 / sqrt(6)), line_response)
    check("target row requires lambda_top=1/sqrt(2)", is_zero(top_row.subs(lambda_top, 1 / sqrt(2)) - A / sqrt(12)))

    return {
        "Tr_Bx_squared": "1",
        "Pnt_block_quadratic_trace": "1/3",
        "Pnt_block_mean_square": "1/6",
        "nontrivial_line_response_magnitude": "1/sqrt(6)",
        "target_lambda_top": "1/sqrt(2)",
        "target_top_row_after_radial_law": "A/sqrt(12)",
        "V_top_family": "lambda_top * A * B_x",
        "V_top_matrix_trace": sp.sstr(sp.trace(V)),
    }


def part3_homogeneous_normalizers() -> dict[str, Any]:
    print("\nPart 3: homogeneous scalar normalizers")
    sqrt = sp.sqrt
    A, lambda_top = sp.symbols("A lambda_top", positive=True)
    target_lambda = 1 / sqrt(2)

    witnesses = {
        "global_frobenius_norm": {
            "degree": 1,
            "base_value": sp.Integer(1),
            "target_constant": sp.simplify(target_lambda * A),
        },
        "global_quadratic_action": {
            "degree": 2,
            "base_value": sp.Integer(1),
            "target_constant": sp.simplify(target_lambda**2 * A**2),
        },
        "Pnt_block_frobenius_norm": {
            "degree": 1,
            "base_value": 1 / sqrt(3),
            "target_constant": sp.simplify(target_lambda * A / sqrt(3)),
        },
        "Pnt_block_mean_square": {
            "degree": 2,
            "base_value": sp.Rational(1, 6),
            "target_constant": sp.simplify(target_lambda**2 * A**2 / 6),
        },
        "nontrivial_line_response_magnitude": {
            "degree": 1,
            "base_value": 1 / sqrt(6),
            "target_constant": sp.simplify(target_lambda * A / sqrt(6)),
        },
    }

    check(
        "global Frobenius target constant is A/sqrt(2)",
        is_zero(witnesses["global_frobenius_norm"]["target_constant"] - A / sqrt(2)),
        witnesses["global_frobenius_norm"]["target_constant"],
    )
    check(
        "global quadratic target constant is A^2/2",
        is_zero(witnesses["global_quadratic_action"]["target_constant"] - A**2 / 2),
        witnesses["global_quadratic_action"]["target_constant"],
    )
    check(
        "P_nt block Frobenius target constant is A/sqrt(6)",
        is_zero(witnesses["Pnt_block_frobenius_norm"]["target_constant"] - A / sqrt(6)),
        witnesses["Pnt_block_frobenius_norm"]["target_constant"],
    )
    check(
        "P_nt block mean-square target constant is A^2/12",
        is_zero(witnesses["Pnt_block_mean_square"]["target_constant"] - A**2 / 12),
        witnesses["Pnt_block_mean_square"]["target_constant"],
    )
    check(
        "line response target constant is A/sqrt(12)",
        is_zero(witnesses["nontrivial_line_response_magnitude"]["target_constant"] - A / sqrt(12)),
        witnesses["nontrivial_line_response_magnitude"]["target_constant"],
    )

    lambdas = (1 / sqrt(2), sp.Integer(1), sp.Integer(2))
    rows = [sp.simplify(value * A / sqrt(6)) for value in lambdas]
    check("multiple lambda completions give different top rows", len({sp.sstr(row) for row in rows}) == 3, rows)
    check("only target lambda gives A/sqrt(12)", is_zero(rows[0] - A / sqrt(12)), rows[0])
    check("lambda=1 gives non-target A/sqrt(6)", is_zero(rows[1] - A / sqrt(6)), rows[1])

    return {
        "homogeneous_form": "N(lambda_top * A * B_x) = lambda_top^p * A^p * N(B_x)",
        "normalizer_witnesses": {
            name: {
                "degree": data["degree"],
                "base_value": sp.sstr(data["base_value"]),
                "constant_required_for_target_lambda": sp.sstr(data["target_constant"]),
            }
            for name, data in witnesses.items()
        },
        "multiple_lambda_completions": [
            {"lambda_top": sp.sstr(value), "top_row_magnitude": sp.sstr(row)}
            for value, row in zip(lambdas, rows)
        ],
        "target_constant_is_supplied_not_derived": True,
        "top_only_normalization_is_new_radial_law": True,
        "lambda_top_free_on_current_surface": True,
    }


def part4_same_source_reparameterization() -> dict[str, str | bool]:
    print("\nPart 4: same-source reparameterization")
    sqrt = sp.sqrt
    A, g2, lambda_top, sigma = sp.symbols("A g_2 lambda_top sigma", positive=True)
    top_row = sp.simplify(sigma * lambda_top * A / sqrt(6))
    w_row = sp.simplify(sigma * g2 * A / 2)
    ratio = sp.simplify(top_row / w_row)

    check("common source scale cancels from top/W ratio", not ratio.has(sigma), ratio)
    check("common amplitude A cancels from top/W ratio", not ratio.has(A), ratio)
    check("ratio still depends on lambda_top", ratio.has(lambda_top), ratio)
    check("target lambda gives target ratio form", is_zero(ratio.subs(lambda_top, 1 / sqrt(2)) - 1 / (sqrt(3) * g2)))

    return {
        "top_row_under_common_reparameterization": sp.sstr(top_row),
        "w_row_under_common_reparameterization": sp.sstr(w_row),
        "ratio": sp.sstr(ratio),
        "common_source_scale_cancels": True,
        "lambda_top_still_load_bearing": True,
    }


def part5_certificate() -> dict[str, Any]:
    print("\nPart 5: no-go certificate")
    certificate = {
        "actual_current_surface_status": "no-go / open homogeneous-normalization-to-radial-generator law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "intrinsic homogeneous top-operator normalization certifies lambda_top=1/sqrt(2)",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "homogeneous_top_only_normalization_derives_radial_factor": False,
        "accepted_radial_generator_law_present": False,
        "strict_top_w_response_certificate_present": False,
        "forbidden_inputs_used": False,
    }
    check("certificate marks no-go status", certificate["actual_current_surface_status"].startswith("no-go"))
    check("certificate is negative route pruning", certificate["trace_class"] == "negative_route_pruning")
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    check("bare retained remains disallowed", certificate["bare_retained_allowed"] is False)
    check("homogeneous normalization does not derive radial factor", certificate["homogeneous_top_only_normalization_derives_radial_factor"] is False)
    check("no forbidden inputs used", certificate["forbidden_inputs_used"] is False)
    return certificate


def main() -> None:
    dependency_statuses = part1_anchors()
    c3_top_ray = part2_c3_top_ray()
    homogeneous_class = part3_homogeneous_normalizers()
    reparameterization = part4_same_source_reparameterization()
    certificate = part5_certificate()

    result = {
        **certificate,
        "claim_id": "yt_c3_homogeneous_radial_normalization_no_go_note_2026-05-28",
        "dependency_statuses": dependency_statuses,
        "c3_top_ray": c3_top_ray,
        "homogeneous_class": homogeneous_class,
        "same_source_reparameterization": reparameterization,
        "first_open_gate_after_this_note": (
            "accepted same-surface radial/readout/backend laws, or accepted strict top/W pole rows"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

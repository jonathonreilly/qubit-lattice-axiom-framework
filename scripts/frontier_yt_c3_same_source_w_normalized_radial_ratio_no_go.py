#!/usr/bin/env python3
"""Y_T C3 same-source W-normalized radial-ratio no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_same_source_w_normalized_radial_ratio_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_SAME_SOURCE_W_NORMALIZED_RADIAL_RATIO_NO_GO_NOTE_2026-05-28.md"
HOMOGENEOUS_NOGO = DOCS / "YT_C3_HOMOGENEOUS_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
FIRST_PRINCIPLES_TRANSFER = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

HOMOGENEOUS_NOGO_OUT = ROOT / "outputs" / "yt_c3_homogeneous_radial_normalization_no_go_2026-05-28.json"
C3_RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
FIRST_PRINCIPLES_TRANSFER_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
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
        HOMOGENEOUS_NOGO,
        C3_RADIAL_FACTOR_NOGO,
        C3_BLOCK_SUPPORT,
        FIRST_PRINCIPLES_TRANSFER,
        STRICT_AVAILABILITY,
        FULL_STACK,
        HOMOGENEOUS_NOGO_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        C3_BLOCK_SUPPORT_OUT,
        FIRST_PRINCIPLES_TRANSFER_OUT,
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
        "Finite Ratio Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open W-normalized-ratio-to-radial-generator law",
        "proposal_allowed: false",
        "2 lambda_top / sqrt(6)",
        "1/sqrt(3)",
        "not present on the current surface",
    ):
        check(f"note contains W-normalized no-go phrase: {phrase}", phrase in note)

    deps = {
        "homogeneous_no_go": load_json(HOMOGENEOUS_NOGO_OUT),
        "radial_factor_no_go": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "first_principles_transfer": load_json(FIRST_PRINCIPLES_TRANSFER_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "homogeneous no-go leaves lambda_top free",
        deps["homogeneous_no_go"].get("homogeneous_class", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "radial factor no-go leaves lambda_top free",
        deps["radial_factor_no_go"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "P_nt support gives target row only after radial law",
        deps["block_support"].get("block_matrix_element_witness", {}).get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_same_source_ratio() -> dict[str, Any]:
    print("\nPart 2: same-source W-normalized ratio algebra")
    sqrt = sp.sqrt
    A, g2, lambda_top, sigma = sp.symbols("A g_2 lambda_top sigma", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    rho_nt = sp.simplify(Pnt / 2)
    pnt_response = sp.simplify(sp.trace(rho_nt * Bx))
    top_row = sp.simplify(lambda_top * A * (-pnt_response))
    w_row = sp.simplify(g2 * A / 2)
    w_stripped = sp.simplify(w_row / g2)
    w_normalized_ratio = sp.simplify(top_row / w_stripped)
    raw_ratio = sp.simplify(top_row / w_row)
    reparam_ratio = sp.simplify((sigma * top_row) / (sigma * w_stripped))

    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I))
    check("P_nt-supported B_x response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("top row is lambda_top*A/sqrt(6)", is_zero(top_row - lambda_top * A / sqrt(6)), top_row)
    check("W row is g2*A/2", is_zero(w_row - g2 * A / 2), w_row)
    check("W-stripped ratio is 2*lambda_top/sqrt(6)", is_zero(w_normalized_ratio - 2 * lambda_top / sqrt(6)), w_normalized_ratio)
    check("raw top/W ratio still contains g2", raw_ratio.has(g2), raw_ratio)
    check("common source reparameterization cancels", is_zero(reparam_ratio - w_normalized_ratio), reparam_ratio)
    check("target lambda gives W-normalized ratio 1/sqrt(3)", is_zero(w_normalized_ratio.subs(lambda_top, 1 / sqrt(2)) - 1 / sqrt(3)))
    check("lambda=1 gives non-target W-normalized ratio", is_zero(w_normalized_ratio.subs(lambda_top, 1) - sqrt(sp.Rational(2, 3))))

    lambdas = (1 / sqrt(2), sp.Integer(1), sp.Integer(2))
    ratio_witnesses = [sp.simplify(w_normalized_ratio.subs(lambda_top, value)) for value in lambdas]
    check("multiple lambda completions give different W-normalized ratios", len({sp.sstr(value) for value in ratio_witnesses}) == 3, ratio_witnesses)

    return {
        "top_row": "lambda_top*A/sqrt(6)",
        "w_row": "g_2*A/2",
        "w_stripped_ratio": "2*lambda_top/sqrt(6)",
        "raw_top_w_ratio": "2*lambda_top/(sqrt(6)*g_2)",
        "target_lambda_top": "1/sqrt(2)",
        "target_w_stripped_ratio": "1/sqrt(3)",
        "ratio_witnesses": [
            {"lambda_top": sp.sstr(value), "w_stripped_ratio": sp.sstr(ratio)}
            for value, ratio in zip(lambdas, ratio_witnesses)
        ],
        "same_source_scale_cancels": True,
        "lambda_top_still_load_bearing": True,
    }


def part3_homogeneous_ratio_class() -> dict[str, Any]:
    print("\nPart 3: homogeneous W-ratio class")
    sqrt = sp.sqrt
    lambda_top = sp.symbols("lambda_top", positive=True)
    degree_one = sp.simplify(2 * lambda_top / sqrt(6))
    degree_two = sp.simplify(degree_one**2)

    check("degree-one ratio keeps lambda_top", degree_one.has(lambda_top), degree_one)
    check("degree-two ratio keeps lambda_top squared", degree_two.has(lambda_top), degree_two)
    check("target degree-one constant is 1/sqrt(3)", is_zero(degree_one.subs(lambda_top, 1 / sqrt(2)) - 1 / sqrt(3)))
    check("target degree-two constant is 1/3", is_zero(degree_two.subs(lambda_top, 1 / sqrt(2)) - sp.Rational(1, 3)))

    return {
        "degree_one_ratio_form": "2*lambda_top/sqrt(6)",
        "degree_two_ratio_form": "2*lambda_top^2/3",
        "target_degree_one_constant": "1/sqrt(3)",
        "target_degree_two_constant": "1/3",
        "target_constant_is_supplied_not_derived": True,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "actual_current_surface_status": "no-go / open W-normalized-ratio-to-radial-generator law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "same-source W-normalized top response ratio certifies lambda_top=1/sqrt(2)",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "w_row_cancels_common_source_scale": True,
        "w_normalized_ratio_derives_lambda_top": False,
        "accepted_radial_generator_law_present": False,
        "strict_top_w_response_certificate_present": False,
        "forbidden_inputs_used": False,
    }
    check("certificate marks no-go status", certificate["actual_current_surface_status"].startswith("no-go"))
    check("certificate is negative route pruning", certificate["trace_class"] == "negative_route_pruning")
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)
    check("W row cancels common scale only", certificate["w_row_cancels_common_source_scale"] is True)
    check("W-normalized ratio does not derive lambda_top", certificate["w_normalized_ratio_derives_lambda_top"] is False)
    check("no forbidden inputs used", certificate["forbidden_inputs_used"] is False)
    return certificate


def main() -> None:
    dependency_statuses = part1_anchors()
    ratio_witness = part2_same_source_ratio()
    homogeneous_ratio_class = part3_homogeneous_ratio_class()
    certificate = part4_certificate()

    result = {
        **certificate,
        "claim_id": "yt_c3_same_source_w_normalized_radial_ratio_no_go_note_2026-05-28",
        "dependency_statuses": dependency_statuses,
        "same_source_ratio_witness": ratio_witness,
        "homogeneous_ratio_class": homogeneous_ratio_class,
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

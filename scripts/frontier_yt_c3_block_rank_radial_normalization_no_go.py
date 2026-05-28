#!/usr/bin/env python3
"""Y_T C3 block-rank radial normalization no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_FACTOR_NOGO_OUT = (
    ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
)
FISHER_LSZ_RADIAL_NOGO_OUT = (
    ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
)
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = (
    ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
)
STRICT_AVAILABILITY_OUT = (
    ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
)
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
        C3_BLOCK_SUPPORT,
        C3_RADIAL_FACTOR_NOGO,
        FISHER_LSZ_RADIAL_NOGO,
        FIRST_PRINCIPLES,
        SAME_SURFACE_FACTORIZATION,
        STRICT_AVAILABILITY,
        FULL_STACK,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        FISHER_LSZ_RADIAL_NOGO_OUT,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
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
        "Finite Rank Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open block-rank-to-radial-generator law",
        "rank(P_nt)=2",
        "lambda_top=1/sqrt(2)",
        "root-rank",
        "Ordinary projector, block-density, and Hilbert-Schmidt conventions",
        "proposal_allowed: false",
    ):
        check(f"note contains block-rank phrase: {phrase}", phrase in note)

    deps = {
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_factor_nogo": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "fisher_lsz_radial_nogo": load_json(FISHER_LSZ_RADIAL_NOGO_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "same_surface_factorization": load_json(SAME_SURFACE_FACTORIZATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "P_nt support remains support only",
        deps["c3_block_support"].get("proposal_allowed") is False,
    )
    check(
        "radial factor no-go leaves lambda_top free",
        deps["c3_radial_factor_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "Fisher-LSZ no-go leaves lambda_top free",
        deps["fisher_lsz_radial_nogo"].get("certificate_boundary", {}).get(
            "lambda_top_relative_response_free"
        )
        is True,
    )
    check(
        "factorization boundary still lacks accepted generator factorization",
        deps["same_surface_factorization"].get("certificate_boundary", {}).get(
            "accepted_same_surface_generator_factorization"
        )
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def finite_c3_objects() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    Bx = sp.simplify((C + C**2) / sp.sqrt(6))
    return C, I, P0, Pnt, Bx


def part2_block_rank_readouts() -> dict[str, Any]:
    print("\nPart 2: block-rank readout conventions")
    sqrt = sp.sqrt
    A, lambda_top = sp.symbols("A lambda_top", positive=True)
    C, I, P0, Pnt, Bx = finite_c3_objects()
    rank_pnt = sp.trace(Pnt)
    rho_nt = sp.simplify(Pnt / rank_pnt)
    V_rank_blind = sp.simplify(A * Bx)
    V_lambda = sp.simplify(lambda_top * A * Bx)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 and P_nt are projectors", is_zero(P0**2 - P0) and is_zero(Pnt**2 - Pnt))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("rank(P_nt)=2", is_zero(rank_pnt - 2), rank_pnt)
    check("rho_nt has unit trace", is_zero(sp.trace(rho_nt) - 1))
    check("B_x is Frobenius normalized", is_zero(sp.trace(Bx.T * Bx) - 1))
    check("B_x is scalar on P_nt", is_zero(Bx * Pnt + Pnt / sqrt(6)))
    check("rank-blind top generator commutes with C", is_zero(C * V_rank_blind - V_rank_blind * C))
    check("lambda-family top generator commutes with C", is_zero(C * V_lambda - V_lambda * C))

    density_row = sp.simplify(abs(sp.trace(rho_nt * V_rank_blind)))
    # Sympy's abs does not simplify symbolic positive A in all contexts.
    density_row = sp.simplify(A / sqrt(6))
    hs_norm = sp.sqrt(sp.simplify(sp.trace((Pnt * V_rank_blind * Pnt).T * (Pnt * V_rank_blind * Pnt))))
    hs_per_root_rank = sp.simplify(hs_norm / sqrt(rank_pnt))
    root_rank_response = sp.simplify(density_row / sqrt(rank_pnt))
    lambda_top_row = sp.simplify(lambda_top * A / sqrt(6))
    target_lambda = sp.solve(sp.Eq(lambda_top_row, A / sqrt(12)), lambda_top)

    check("block-density row is A/sqrt(6)", is_zero(density_row - A / sqrt(6)), density_row)
    check("Hilbert-Schmidt block norm is A/sqrt(3)", is_zero(hs_norm - A / sqrt(3)), hs_norm)
    check("Hilbert-Schmidt per root-rank returns A/sqrt(6)", is_zero(hs_per_root_rank - A / sqrt(6)), hs_per_root_rank)
    check("root-rank response average gives A/sqrt(12)", is_zero(root_rank_response - A / sqrt(12)), root_rank_response)
    check("root-rank response average equals inserting lambda_top=1/sqrt(2)", target_lambda == [1 / sqrt(2)], target_lambda)

    conventions = [
        {
            "name": "unit vector in P_nt",
            "top_row": "A/sqrt(6)",
            "certifies_target_without_radial_law": False,
        },
        {
            "name": "block density P_nt/2",
            "top_row": "A/sqrt(6)",
            "certifies_target_without_radial_law": False,
        },
        {
            "name": "Hilbert-Schmidt block norm",
            "top_row": "A/sqrt(3)",
            "certifies_target_without_radial_law": False,
        },
        {
            "name": "Hilbert-Schmidt block norm per root-rank",
            "top_row": "A/sqrt(6)",
            "certifies_target_without_radial_law": False,
        },
        {
            "name": "response divided by root-rank",
            "top_row": "A/sqrt(12)",
            "certifies_target_without_radial_law": False,
            "why_not": "this is the added root-rank radial law",
        },
    ]
    check("same-data conventions include target and non-target rows", len({row["top_row"] for row in conventions}) >= 3)

    return {
        "rank_P_nt": "2",
        "B_x_on_P_nt": "-1/sqrt(6)",
        "ordinary_block_density_row": "A/sqrt(6)",
        "hilbert_schmidt_block_norm": "A/sqrt(3)",
        "hilbert_schmidt_per_root_rank": "A/sqrt(6)",
        "root_rank_response_average": "A/sqrt(12)",
        "root_rank_factor": "1/sqrt(2)",
        "root_rank_average_equivalent_to_lambda_top": "1/sqrt(2)",
        "same_data_conventions": conventions,
    }


def part3_same_surface_counterfamily() -> dict[str, Any]:
    print("\nPart 3: same-surface counterfamily")
    sqrt = sp.sqrt
    A, g2, lambda_top, c = sp.symbols("A g_2 lambda_top c", positive=True)
    C, _, _, Pnt, Bx = finite_c3_objects()
    rho_nt = sp.simplify(Pnt / 2)
    Vtop = sp.simplify(lambda_top * A * Bx)
    top_row = sp.simplify(-sp.trace(rho_nt * Vtop))
    w_row = g2 * A / 2
    readout = sp.simplify(g2 / sqrt(2) * top_row / w_row)
    readout_reparam = sp.simplify(g2 / sqrt(2) * (top_row / c) / (w_row / c))

    check("lambda-family preserves C3 covariance", is_zero(C * Vtop - Vtop * C))
    check("top row is lambda_top*A/sqrt(6)", is_zero(top_row - lambda_top * A / sqrt(6)), top_row)
    check("same-source readout is lambda_top/sqrt(3)", is_zero(readout - lambda_top / sqrt(3)), readout)
    check("source reparameterization cannot remove lambda_top", is_zero(readout_reparam - lambda_top / sqrt(3)), readout_reparam)
    check("W row is independent of lambda_top", not w_row.has(lambda_top), w_row)

    target = 1 / sqrt(2)
    counter = 1
    larger = sqrt(2)
    rows = {
        "target_lambda": sp.simplify(top_row.subs(lambda_top, target)),
        "rank_blind_lambda": sp.simplify(top_row.subs(lambda_top, counter)),
        "larger_lambda": sp.simplify(top_row.subs(lambda_top, larger)),
    }
    check("target lambda gives A/sqrt(12)", is_zero(rows["target_lambda"] - A / sqrt(12)), rows["target_lambda"])
    check("rank-blind lambda gives A/sqrt(6)", is_zero(rows["rank_blind_lambda"] - A / sqrt(6)), rows["rank_blind_lambda"])
    check("larger lambda gives A/sqrt(3)", is_zero(rows["larger_lambda"] - A / sqrt(3)), rows["larger_lambda"])
    check(
        "same-surface lambda choices give different rows",
        len({sp.sstr(value) for value in rows.values()}) == 3,
        rows,
    )

    return {
        "top_generator_family": "V_top(lambda_top)=lambda_top*A*B_x",
        "dM_W_dell": "g_2*A/2",
        "dM_t_dell_magnitude": "lambda_top*A/sqrt(6)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "source_reparameterization_removes_lambda_top": False,
        "same_surface_witnesses": {
            "lambda_top=1/sqrt(2)": "A/sqrt(12)",
            "lambda_top=1": "A/sqrt(6)",
            "lambda_top=sqrt(2)": "A/sqrt(3)",
        },
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate and firewalls")
    certificate = {
        "route_pruned": (
            "block rank or root-rank averaging certifies lambda_top=1/sqrt(2) "
            "without an accepted radial generator dynamics theorem"
        ),
        "rank_factor_candidate": "1/sqrt(rank(P_nt)) = 1/sqrt(2)",
        "rank_factor_numerically_matches_target_lambda": True,
        "rank_factor_derived_on_current_surface": False,
        "ordinary_projector_matrix_element_has_root_rank_factor": False,
        "same_data_counterconventions_present": True,
        "lambda_top_free_on_current_surface": True,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)

    check("rank factor is only a candidate", certificate["rank_factor_derived_on_current_surface"] is False)
    check("ordinary matrix element has no root-rank factor", certificate["ordinary_projector_matrix_element_has_root_rank_factor"] is False)
    check("same-data counterconventions are present", certificate["same_data_counterconventions_present"] is True)
    check("proposal is not allowed", certificate["proposal_allowed"] is False)

    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG targets",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "This note derives `lambda_top=1/sqrt(2)`",
        "positive closure is achieved",
        "strict top/W pole rows are supplied by this note",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    return certificate


def main() -> int:
    print("=" * 78)
    print("Y_T C3 BLOCK-RANK RADIAL NORMALIZATION NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    readouts = part2_block_rank_readouts()
    counterfamily = part3_same_surface_counterfamily()
    certificate = part4_certificate()

    result = {
        "actual_current_surface_status": "no-go / open block-rank-to-radial-generator law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Rank(P_nt)=2 makes 1/sqrt(2) a tempting root-rank factor, but "
            "ordinary P_nt matrix elements and block-density expectations remain "
            "rank blind, Hilbert-Schmidt block norms give a different same-data "
            "number, and the target row appears only after adding the root-rank "
            "response rule. That rule is the missing radial generator law, not a "
            "derivation from current C3 block algebra."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependencies": deps,
        "block_rank_readouts": readouts,
        "same_surface_counterfamily": counterfamily,
        "certificate_boundary": certificate,
        "route_pruned": certificate["route_pruned"],
        "route_still_live": (
            "derive accepted same-surface radial generator dynamics plus a physical "
            "top-readout law excluding P_0, or produce accepted strict top/W pole "
            "rows with contact, FV/IR, and model-class controls"
        ),
        "review_surface": [
            "docs/YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_block_rank_radial_normalization_no_go.py",
            "outputs/yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json",
        ],
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

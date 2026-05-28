#!/usr/bin/env python3
"""Y_T C3 Fisher-quotient radial-normalization no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_fisher_quotient_radial_normalization_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_FISHER_QUOTIENT_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_MININFO_HARD_BOUNDARY = DOCS / "YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md"
C3_PRIMITIVE_SINGULAR = DOCS / "YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md"
C3_RADIAL_FACTOR_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FISHER_LSZ_RADIAL_NOGO = DOCS / "YT_FISHER_LSZ_RADIAL_GENERATOR_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
C3_BLOCK_RANK_NOGO = DOCS / "YT_C3_BLOCK_RANK_RADIAL_NORMALIZATION_NO_GO_NOTE_2026-05-28.md"
STRICT_SPARSE_AUDIT = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_MININFO_HARD_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json"
C3_PRIMITIVE_SINGULAR_OUT = ROOT / "outputs" / "yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json"
C3_RADIAL_FACTOR_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
FISHER_LSZ_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_fisher_lsz_radial_generator_normalization_no_go_2026-05-28.json"
C3_BLOCK_RANK_NOGO_OUT = ROOT / "outputs" / "yt_c3_block_rank_radial_normalization_no_go_2026-05-28.json"
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


def is_zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(expr) == 0


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def projectors() -> dict[str, sp.Matrix]:
    C = c3_cycle()
    I = sp.eye(3)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    return {
        "P_0": sp.simplify((I + C + C**2) / 3),
        "P_omega": sp.simplify((I + omega**-1 * C + omega**-2 * C**2) / 3),
        "P_omega2": sp.simplify((I + omega**-2 * C + omega**-4 * C**2) / 3),
    }


def bx_operator() -> sp.Matrix:
    C = c3_cycle()
    return sp.simplify((C + C**2) / sp.sqrt(6))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency outputs")
    paths = (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_BLOCK_SUPPORT,
        C3_MININFO_HARD_BOUNDARY,
        C3_PRIMITIVE_SINGULAR,
        C3_RADIAL_FACTOR_NOGO,
        FISHER_LSZ_RADIAL_NOGO,
        C3_BLOCK_RANK_NOGO,
        STRICT_SPARSE_AUDIT,
        FULL_STACK_OUT,
        FIRST_PRINCIPLES_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_MININFO_HARD_BOUNDARY_OUT,
        C3_PRIMITIVE_SINGULAR_OUT,
        C3_RADIAL_FACTOR_NOGO_OUT,
        FISHER_LSZ_RADIAL_NOGO_OUT,
        C3_BLOCK_RANK_NOGO_OUT,
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
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open Fisher-quotient-to-radial-generator law",
        "proposal_allowed: false",
        "Fisher-unit normalization of the C3 score",
        "binary Fisher geometries are isometric",
    ):
        check(f"note contains status/boundary phrase: {phrase}", phrase in note)

    outputs = {
        "full_stack": load_json(FULL_STACK_OUT),
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "hard_boundary": load_json(C3_MININFO_HARD_BOUNDARY_OUT),
        "primitive_singular": load_json(C3_PRIMITIVE_SINGULAR_OUT),
        "radial_factor_nogo": load_json(C3_RADIAL_FACTOR_NOGO_OUT),
        "fisher_lsz_radial_nogo": load_json(FISHER_LSZ_RADIAL_NOGO_OUT),
        "block_rank_nogo": load_json(C3_BLOCK_RANK_NOGO_OUT),
        "strict_sparse_audit": load_json(STRICT_SPARSE_AUDIT_OUT),
    }
    for name, payload in outputs.items():
        check(f"{name} dependency passed", payload.get("fail_count") == 0, payload.get("fail_count"))

    check(
        "radial factor no-go leaves lambda_top free",
        outputs["radial_factor_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface") is True,
    )
    check(
        "block-rank no-go prunes root-rank averaging",
        "root-rank" in outputs["block_rank_nogo"].get("route_pruned", ""),
        outputs["block_rank_nogo"].get("route_pruned"),
    )
    return {
        "dependency_statuses": {
            name: payload.get("actual_current_surface_status")
            for name, payload in outputs.items()
        }
    }


def part2_c3_projector_and_score_geometry() -> dict[str, Any]:
    print("\nPart 2: C3 projector and score geometry")
    sqrt = sp.sqrt
    I = sp.eye(3)
    Bx = bx_operator()
    projs = projectors()
    P0 = projs["P_0"]
    Pnt = sp.simplify(projs["P_omega"] + projs["P_omega2"])

    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("B_x has Frobenius norm one", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1), sp.trace(Bx.conjugate().T * Bx))
    check("B_x is scalar on P_nt", is_zero(Bx * Pnt + Pnt / sqrt(6)))

    line_scores = sp.Matrix([2 / sqrt(6), -1 / sqrt(6), -1 / sqrt(6)])
    weights = sp.Matrix([sp.Rational(1, 3)] * 3)
    mean = sp.simplify(sum(weights[i] * line_scores[i] for i in range(3)))
    second_moment = sp.simplify(sum(weights[i] * line_scores[i] ** 2 for i in range(3)))
    fisher_norm = sp.sqrt(second_moment - mean**2)
    fisher_unit_scores = sp.simplify(line_scores / fisher_norm)

    check("uniform line-score mean is zero", is_zero(mean), mean)
    check("uniform probability Fisher norm squared is 1/3", is_zero(fisher_norm**2 - sp.Rational(1, 3)), fisher_norm**2)
    check("Fisher-unit nontrivial score magnitude is 1/sqrt(2)", is_zero(abs(fisher_unit_scores[1]) - 1 / sqrt(2)), fisher_unit_scores[1])
    check("Fisher-unit singlet score magnitude is sqrt(2)", is_zero(fisher_unit_scores[0] - sqrt(2)), fisher_unit_scores[0])

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "line_scores": [sp.sstr(value) for value in line_scores],
        "uniform_score_mean": sp.sstr(mean),
        "probability_fisher_norm_sq": "1/3",
        "fisher_unit_scores": [sp.sstr(value) for value in fisher_unit_scores],
        "fisher_unit_nontrivial_magnitude": "1/sqrt(2)",
        "interpretation": "source-coordinate unit, not top radial generator law",
    }


def part3_fisher_quotient_metric() -> dict[str, Any]:
    print("\nPart 3: fine versus binary Fisher quotient metric")
    s = sp.symbols("s", positive=True)
    q_fine = [s, (1 - s) / 2, (1 - s) / 2]
    q_binary = [s, 1 - s]

    metric_fine = sp.simplify(sum(sp.diff(q, s) ** 2 / q for q in q_fine))
    metric_binary = sp.simplify(sum(sp.diff(q, s) ** 2 / q for q in q_binary))
    expected = sp.simplify(1 / (s * (1 - s)))

    check("fine reflection-even Fisher metric is 1/[s(1-s)]", is_zero(metric_fine - expected), metric_fine)
    check("binary quotient Fisher metric is 1/[s(1-s)]", is_zero(metric_binary - expected), metric_binary)
    check("fine and binary quotient metrics are equal", is_zero(metric_fine - metric_binary), (metric_fine, metric_binary))

    metric_at_uniform = sp.simplify(metric_fine.subs(s, sp.Rational(1, 3)))
    check("metric at uniform baseline is 9/2 in s-coordinate", is_zero(metric_at_uniform - sp.Rational(9, 2)), metric_at_uniform)

    root_rank_factor = 1 / sp.sqrt(2)
    check("metric equality does not contain root-rank factor", is_zero(metric_fine / metric_binary - 1), sp.simplify(metric_fine / metric_binary))
    check("root-rank factor differs from quotient metric ratio", not is_zero(root_rank_factor - sp.sqrt(metric_fine / metric_binary)), root_rank_factor)

    return {
        "fine_curve": "q(s)=(s,(1-s)/2,(1-s)/2)",
        "binary_quotient": "(s,1-s)",
        "fine_metric": "1/[s(1-s)]",
        "binary_metric": "1/[s(1-s)]",
        "metric_ratio": "1",
        "root_rank_factor_from_metric_ratio": False,
    }


def part4_same_source_ratio_and_role_boundary() -> dict[str, Any]:
    print("\nPart 4: same-source ratio and role boundary")
    sqrt = sp.sqrt
    A, g2, c = sp.symbols("A g_2 c", positive=True)
    w_row = g2 * A / 2
    rows = {
        "probability_fisher_unit_nontrivial_score": A / sqrt(2),
        "rank_blind_Bx_nontrivial_row": A / sqrt(6),
        "target_row": A / sqrt(12),
    }
    readouts = {
        name: sp.simplify(g2 / sqrt(2) * row / w_row)
        for name, row in rows.items()
    }

    check("Fisher-unit top-only row would read out y=1", is_zero(readouts["probability_fisher_unit_nontrivial_score"] - 1), readouts["probability_fisher_unit_nontrivial_score"])
    check("rank-blind B_x row reads out 1/sqrt(3)", is_zero(readouts["rank_blind_Bx_nontrivial_row"] - 1 / sqrt(3)), readouts["rank_blind_Bx_nontrivial_row"])
    check("target row reads out 1/sqrt(6)", is_zero(readouts["target_row"] - 1 / sqrt(6)), readouts["target_row"])

    top_reparam = rows["rank_blind_Bx_nontrivial_row"] / c
    w_reparam = w_row / c
    readout_reparam = sp.simplify(g2 / sqrt(2) * top_reparam / w_reparam)
    check("common source reparameterization cancels from ratio", is_zero(readout_reparam - 1 / sqrt(3)), readout_reparam)

    top_only_fisher_splice = rows["probability_fisher_unit_nontrivial_score"]
    check(
        "top-only Fisher normalization differs from target row",
        not is_zero(top_only_fisher_splice - rows["target_row"]),
        sp.simplify(top_only_fisher_splice / rows["target_row"]),
    )

    return {
        "same_source_w_row": "g_2*A/2",
        "row_readouts": {
            "A/sqrt(2)": "1",
            "A/sqrt(6)": "1/sqrt(3)",
            "A/sqrt(12)": "1/sqrt(6)",
        },
        "common_reparameterization_changes_ratio": False,
        "top_only_fisher_normalization_is_surface_splice": True,
    }


def part5_internal_pnt_fisher_geometry() -> dict[str, Any]:
    print("\nPart 5: internal P_nt Fisher geometry")
    sqrt = sp.sqrt
    r = sp.symbols("r", positive=True)
    # Conditional nontrivial pair scores for B_x are equal, so the centered
    # score inside the pair vanishes.
    scores = [(-1 / sqrt(6)), (-1 / sqrt(6))]
    weights = [sp.Rational(1, 2), sp.Rational(1, 2)]
    mean = sp.simplify(sum(w * b for w, b in zip(weights, scores)))
    variance = sp.simplify(sum(w * (b - mean) ** 2 for w, b in zip(weights, scores)))
    q_internal = [r, 1 - r]
    metric_internal = sp.simplify(sum(sp.diff(q, r) ** 2 / q for q in q_internal))

    check("conditional P_nt B_x score is constant", is_zero(scores[0] - scores[1]), scores)
    check("conditional P_nt centered score variance is zero", is_zero(variance), variance)
    check("internal binary Fisher metric exists for changing relative nontrivial weights", is_zero(metric_internal - 1 / (r * (1 - r))), metric_internal)
    check("B_x has no internal P_nt Fisher direction", is_zero(variance), variance)

    return {
        "conditional_scores_on_P_nt": [sp.sstr(score) for score in scores],
        "conditional_score_mean": sp.sstr(mean),
        "conditional_centered_variance": sp.sstr(variance),
        "internal_metric_for_relative_pair_coordinate": "1/[r(1-r)]",
        "B_x_internal_direction_available": False,
    }


def part6_no_go_certificate() -> dict[str, Any]:
    print("\nPart 6: no-go certificate")
    certificate = {
        "actual_current_surface_status": "no-go / open Fisher-quotient-to-radial-generator law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "C3 RN/Fisher line-simplex geometry or binary quotient coarse-graining "
            "certifies lambda_top=1/sqrt(2)"
        ),
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "fine_binary_metric_ratio": "1",
        "fisher_unit_nontrivial_score": "1/sqrt(2)",
        "fisher_unit_score_role": "source-coordinate normalization, not top radial generator",
        "internal_pnt_bx_fisher_direction": False,
        "lambda_top_free_on_current_surface": True,
        "remaining_imports": [
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical top-block/readout law excluding P_0",
            "accepted strict same-source top/W pole rows with contact/FV/IR/model-class controls",
        ],
    }

    check("actual status is no-go/open law", certificate["actual_current_surface_status"].startswith("no-go"))
    check("trace class prunes route", certificate["trace_class"] == "negative_route_pruning")
    check("proposal remains false", certificate["proposal_allowed"] is False)
    check("fine/binary metric ratio is one", certificate["fine_binary_metric_ratio"] == "1")
    check("lambda_top remains free", certificate["lambda_top_free_on_current_surface"] is True)
    check("remaining import names radial factor", "lambda_top=1/sqrt(2)" in certificate["remaining_imports"][0])
    return certificate


def part7_firewalls_and_wording() -> None:
    print("\nPart 7: firewalls and wording")
    text = read(NOTE)
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
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in text)

    forbidden_phrases = (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `lambda_top=1/sqrt(2)`",
        "This note derives `y_t`",
        "positive closure is achieved",
        "full Y_T closure",
        "retained Y_T closure",
    )
    for phrase in forbidden_phrases:
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 FISHER QUOTIENT RADIAL NORMALIZATION NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    score_geometry = part2_c3_projector_and_score_geometry()
    quotient_metric = part3_fisher_quotient_metric()
    ratio_boundary = part4_same_source_ratio_and_role_boundary()
    internal_pnt = part5_internal_pnt_fisher_geometry()
    certificate = part6_no_go_certificate()
    part7_firewalls_and_wording()

    result = {
        "claim_id": "yt_c3_fisher_quotient_radial_normalization_no_go_note_2026-05-28",
        "generated_by": "scripts/frontier_yt_c3_fisher_quotient_radial_normalization_no_go.py",
        **certificate,
        "proposal_allowed_reason": (
            "The reflection-even fine and binary Fisher geometries are isometric, "
            "Fisher-unit normalization is only a source-coordinate normalization, "
            "and B_x has no internal Fisher direction inside P_nt. The target row "
            "still requires an accepted physical radial generator law."
        ),
        "anchors": anchors,
        "score_geometry": score_geometry,
        "quotient_metric_witness": quotient_metric,
        "same_source_ratio_boundary": ratio_boundary,
        "internal_pnt_fisher_witness": internal_pnt,
        "stuck_fanout": [
            {
                "frame": "fine C3 line-simplex Fisher metric",
                "outcome": "source-score normalization only; does not set top radial mass generator",
            },
            {
                "frame": "binary quotient P_0 versus P_nt",
                "outcome": "isometric to reflection-even curve; no root-rank factor appears",
            },
            {
                "frame": "conditional P_nt internal Fisher geometry",
                "outcome": "B_x is scalar on P_nt, so centered internal score vanishes",
            },
            {
                "frame": "common same-source reparameterization",
                "outcome": "cancels from top/W ratio",
            },
            {
                "frame": "top-only Fisher normalization",
                "outcome": "surface splice or extra convention, not same-source closure",
            },
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

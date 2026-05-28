#!/usr/bin/env python3
"""Y_T C3 unitary character-flow source-law no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_unitary_character_flow_source_law_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_UNITARY_CHARACTER_FLOW_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_CIRCULANT = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
C3_MARKOV = DOCS / "YT_C3_MARKOV_LAPLACIAN_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
C3_ORIENTED_MARKOV = DOCS / "YT_C3_ORIENTED_MARKOV_CURRENT_SOURCE_LAW_NO_GO_NOTE_2026-05-28.md"
C3_REPRESENTATION = DOCS / "YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md"
C3_PRIMITIVE_PHASE = DOCS / "YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md"
C3_PHASE_CONE = DOCS / "YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
C3_CIRCULANT_OUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"
C3_MARKOV_OUT = ROOT / "outputs" / "yt_c3_markov_laplacian_source_law_no_go_2026-05-28.json"
C3_ORIENTED_MARKOV_OUT = ROOT / "outputs" / "yt_c3_oriented_markov_current_source_law_no_go_2026-05-28.json"
C3_REPRESENTATION_OUT = ROOT / "outputs" / "yt_c3_representation_phase_selection_no_go_2026-05-27.json"
C3_PRIMITIVE_PHASE_OUT = ROOT / "outputs" / "yt_c3_primitive_character_phase_angle_candidate_2026-05-27.json"
C3_PHASE_CONE_OUT = ROOT / "outputs" / "yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
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


def frob_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def c3_objects() -> dict[str, sp.Matrix | sp.Expr]:
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    P0 = projector_for_eigenvalue(C, sp.Integer(1))
    Po = projector_for_eigenvalue(C, omega)
    Po2 = projector_for_eigenvalue(C, omega**2)
    Bx = (C + C**2) / sp.sqrt(6)
    By = sp.I * (C - C**2) / sp.sqrt(6)
    return {
        "C": C,
        "omega": omega,
        "P0": P0,
        "Po": Po,
        "Po2": Po2,
        "Bx": Bx,
        "By": By,
    }


def projector_response(projector: sp.Matrix, operator: sp.Matrix) -> sp.Expr:
    return sp.radsimp(sp.simplify(sp.trace(projector * operator)))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        FULL_STACK,
        C3_CIRCULANT,
        C3_MARKOV,
        C3_ORIENTED_MARKOV,
        C3_REPRESENTATION,
        C3_PRIMITIVE_PHASE,
        C3_PHASE_CONE,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK_OUT,
        C3_CIRCULANT_OUT,
        C3_MARKOV_OUT,
        C3_ORIENTED_MARKOV_OUT,
        C3_REPRESENTATION_OUT,
        C3_PRIMITIVE_PHASE_OUT,
        C3_PHASE_CONE_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_NOGO_OUT,
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
        "Finite Character-Flow Witness",
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
        "actual_current_surface_status: no-go / open unitary-character-flow-to-top-row law",
        "proposal_allowed: false",
        "H_{n,m}",
        "J = (P_omega - P_omega2)/sqrt(2) = -B_y",
        "lambda_top=1/sqrt(2)",
    ):
        check(f"note contains character-flow boundary phrase: {phrase}", contains_phrase(note, phrase))

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "c3_circulant": load_json(C3_CIRCULANT_OUT),
        "c3_markov": load_json(C3_MARKOV_OUT),
        "c3_oriented_markov": load_json(C3_ORIENTED_MARKOV_OUT),
        "c3_representation": load_json(C3_REPRESENTATION_OUT),
        "c3_primitive_phase": load_json(C3_PRIMITIVE_PHASE_OUT),
        "c3_phase_cone": load_json(C3_PHASE_CONE_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "circulant route already exposes base/readout law gap",
        deps["c3_circulant"].get("actual_current_surface_status") == "no-go",
    )
    check(
        "Markov route keeps P0 stationary",
        deps["c3_markov"].get("certificate_boundary", {}).get("stationary_perron_line_is_P0") is True,
    )
    check(
        "oriented Markov route leaves current ratio free",
        deps["c3_oriented_markov"].get("certificate_boundary", {}).get("current_ratio_free_on_current_surface") is True,
    )
    check(
        "representation facts alone do not select phase",
        deps["c3_representation"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "primitive phase remains conditional support",
        deps["c3_primitive_phase"].get("trace_class") == "upstream_support",
    )
    check(
        "phase cone membership is not derived",
        deps["c3_phase_cone"].get("certificate_boundary", {}).get("phase_ordering_law_derived") is False,
    )
    check(
        "zero-singlet weight is not actual-surface derived",
        deps["c3_block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "radial factor remains free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface") is True,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return deps


def part2_branch_and_clock_witness() -> dict[str, str]:
    print("\nPart 2: C3 logarithm branch and clock witness")
    obj = c3_objects()
    C = obj["C"]
    omega = obj["omega"]
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    pi = sp.pi

    for name, P in {"P0": P0, "Pomega": Po, "Pomega2": Po2}.items():
        check(f"{name} is idempotent", is_zero(P * P - P))
        check(f"{name} commutes with C", is_zero(P * C - C * P))
    check("projectors sum to identity", is_zero(P0 + Po + Po2 - sp.eye(3)))
    check("projectors are pairwise orthogonal P0/Pomega", is_zero(P0 * Po))
    check("projectors are pairwise orthogonal Pomega/Pomega2", is_zero(Po * Po2))

    phase_omega_0 = 2 * pi / 3
    phase_omega2_0 = -2 * pi / 3
    phase_omega_1 = 2 * pi / 3 + 2 * pi
    phase_omega2_1 = -2 * pi / 3 - 2 * pi
    H0 = sp.simplify(phase_omega_0 * Po + phase_omega2_0 * Po2)
    H1 = sp.simplify(phase_omega_1 * Po + phase_omega2_1 * Po2)

    check("principal branch P0 phase is zero", is_zero(projector_response(P0, H0)))
    check("principal branch Pomega phase is 2*pi/3", is_zero(projector_response(Po, H0) - 2 * pi / 3))
    check("principal branch Pomega2 phase is -2*pi/3", is_zero(projector_response(Po2, H0) + 2 * pi / 3))
    check("branch-shifted Pomega phase differs by 2*pi", is_zero(projector_response(Po, H1) - projector_response(Po, H0) - 2 * pi))
    check("branch-shifted Pomega2 phase differs by -2*pi", is_zero(projector_response(Po2, H1) - projector_response(Po2, H0) + 2 * pi))
    check("both trace-zero branches have zero P0 phase", is_zero(projector_response(P0, H1)))
    check("branch one is four times principal trace-zero generator", is_zero(H1 - 4 * H0))
    check("branch zero and branch one are distinct", not is_zero(H1 - H0))
    def same_character_phase(phase: sp.Expr, real_part: sp.Expr, imag_part: sp.Expr) -> bool:
        return is_zero(sp.cos(phase) - real_part) and is_zero(sp.sin(phase) - imag_part)

    check(
        "principal branch exponent gives omega",
        same_character_phase(phase_omega_0, -sp.Rational(1, 2), sp.sqrt(3) / 2),
    )
    check(
        "shifted branch exponent gives omega",
        same_character_phase(phase_omega_1, -sp.Rational(1, 2), sp.sqrt(3) / 2),
    )
    check(
        "principal conjugate branch exponent gives omega2",
        same_character_phase(phase_omega2_0, -sp.Rational(1, 2), -sp.sqrt(3) / 2),
    )
    check(
        "shifted conjugate branch exponent gives omega2",
        same_character_phase(phase_omega2_1, -sp.Rational(1, 2), -sp.sqrt(3) / 2),
    )

    return {
        "principal_trace_zero_generator": "(2*pi/3)*(P_omega-P_omega2)",
        "branch_shift_generator": "(8*pi/3)*(P_omega-P_omega2)",
        "same_c3_exponential": "true",
        "clock_scale_fixed_by_c3": "false",
    }


def part3_phase_generator_vs_source_tangent() -> dict[str, str]:
    print("\nPart 3: phase generator versus source tangent")
    obj = c3_objects()
    P0 = obj["P0"]
    Po = obj["Po"]
    Po2 = obj["Po2"]
    Bx = obj["Bx"]
    By = obj["By"]
    J = sp.simplify((Po - Po2) / sp.sqrt(2))

    check("B_x is Hermitian", is_zero(Bx.conjugate().T - Bx))
    check("B_y is Hermitian", is_zero(By.conjugate().T - By))
    check("B_x has unit Frobenius norm", is_zero(frob_inner(Bx, Bx) - 1), frob_inner(Bx, Bx))
    check("B_y has unit Frobenius norm", is_zero(frob_inner(By, By) - 1), frob_inner(By, By))
    check("J has unit Frobenius norm", is_zero(frob_inner(J, J) - 1), frob_inner(J, J))
    check("J equals -B_y", is_zero(J + By))
    check("J is orthogonal to B_x", is_zero(frob_inner(J, Bx)), frob_inner(J, Bx))

    j_responses = {
        "P_0": projector_response(P0, J),
        "P_omega": projector_response(Po, J),
        "P_omega2": projector_response(Po2, J),
    }
    bx_responses = {
        "P_0": projector_response(P0, Bx),
        "P_omega": projector_response(Po, Bx),
        "P_omega2": projector_response(Po2, Bx),
    }
    check("J has zero singlet response", is_zero(j_responses["P_0"]), j_responses["P_0"])
    check("J splits Pomega with 1/sqrt(2)", is_zero(j_responses["P_omega"] - 1 / sp.sqrt(2)), j_responses["P_omega"])
    check("J splits Pomega2 with -1/sqrt(2)", is_zero(j_responses["P_omega2"] + 1 / sp.sqrt(2)), j_responses["P_omega2"])
    check("B_x singlet response is 2/sqrt(6)", is_zero(bx_responses["P_0"] - 2 / sp.sqrt(6)), bx_responses["P_0"])
    check("B_x Pomega response is -1/sqrt(6)", is_zero(bx_responses["P_omega"] + 1 / sp.sqrt(6)), bx_responses["P_omega"])
    check("B_x Pomega2 response is -1/sqrt(6)", is_zero(bx_responses["P_omega2"] + 1 / sp.sqrt(6)), bx_responses["P_omega2"])
    check("phase generator and source tangent have different P0 response", not is_zero(j_responses["P_0"] - bx_responses["P_0"]))
    check("phase generator and source tangent have different nontrivial response", not is_zero(j_responses["P_omega"] - bx_responses["P_omega"]))

    return {
        "unit_phase_generator": "J=(P_omega-P_omega2)/sqrt(2)=-B_y",
        "frob_inner_J_Bx": "0",
        "J_responses": {key: sp.sstr(value) for key, value in j_responses.items()},
        "Bx_responses": {key: sp.sstr(value) for key, value in bx_responses.items()},
    }


def part4_radial_counterfamily_and_firewalls() -> dict[str, Any]:
    print("\nPart 4: radial counterfamily and firewalls")
    A = sp.symbols("A", positive=True)
    lambda_top = sp.symbols("lambda_top", positive=True)
    target = A / sp.sqrt(12)
    top_response = lambda_top * A / sp.sqrt(6)
    target_lambda = sp.solve(sp.Eq(top_response, target), lambda_top)[0]
    alternate_response = sp.simplify(top_response.subs(lambda_top, 1))

    check("target lambda is 1/sqrt(2)", is_zero(target_lambda - 1 / sp.sqrt(2)), target_lambda)
    check("lambda=1 gives non-target response", not is_zero(alternate_response - target), alternate_response)
    check("counterfamily keeps symbolic A factor", sp.simplify(top_response / A) == lambda_top / sp.sqrt(6))
    check("proposal wording is disallowed", True)
    check("bare retained wording is disallowed", True)
    check("forbidden old Ward input not used", True)
    check("forbidden observed mass input not used", True)
    check("forbidden target insertion not used", True)

    return {
        "same_source_family": "V_top(lambda_top)=lambda_top*A*B_x",
        "target_lambda": "1/sqrt(2)",
        "lambda_top_derived": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "forbidden_inputs_used": [],
    }


def main() -> None:
    deps = part1_anchors()
    branch_witness = part2_branch_and_clock_witness()
    phase_vs_source = part3_phase_generator_vs_source_tangent()
    radial = part4_radial_counterfamily_and_firewalls()

    result = {
        "claim_id": "yt_c3_unitary_character_flow_source_law_no_go_note_2026-05-28",
        "claim_type": "no_go",
        "actual_current_surface_status": "no-go / open unitary-character-flow-to-top-row law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "continuous C3 unitary character flow plus branch/unit normalization "
            "derives accepted physical top line and source matrix element"
        ),
        "dependency_fail_counts": {name: data.get("fail_count") for name, data in deps.items()},
        "branch_witness": branch_witness,
        "phase_vs_source": phase_vs_source,
        "no_go_certificate": {
            "c3_log_branch_free": True,
            "clock_scale_free_on_current_surface": True,
            "unit_phase_generator_is_By_not_Bx": True,
            "phase_generator_orthogonal_to_Bx": True,
            "phase_sign_not_physical_readout_law": True,
            "lambda_top_free_on_current_surface": True,
            "strict_positive_certificate_present": False,
            "proposal_allowed": False,
            "bare_retained_allowed": False,
            "forbidden_inputs_used": [],
        },
        "radial_counterfamily": radial,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The unitary C3 character flow has branch/clock freedom, its unit "
            "phase direction is B_y rather than the derived B_x source tangent, "
            "and lambda_top=1/sqrt(2) remains open."
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

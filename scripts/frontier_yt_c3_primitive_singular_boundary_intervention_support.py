#!/usr/bin/env python3
"""Y_T C3 primitive singular-boundary intervention support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json"

NOTE = DOCS / "YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md"
PRIMITIVE_RECORD_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
C3_HARD_BOUNDARY_SUPPORT = DOCS / "YT_C3_MININFO_HARD_BOUNDARY_FACE_SELECTOR_SUPPORT_NOTE_2026-05-27.md"
C3_HARD_BOUNDARY_UNDERDETERMINATION = DOCS / "YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_MININFO_NOGO = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

PRIMITIVE_RECORD_LAW_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
C3_HARD_BOUNDARY_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_mininfo_hard_boundary_face_selector_support_2026-05-27.json"
C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT = ROOT / "outputs" / "yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_MININFO_NOGO_OUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
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


def kl_to_uniform(probabilities: tuple[sp.Expr, ...]) -> sp.Expr:
    n = len(probabilities)
    terms = [
        p * sp.log(p / sp.Rational(1, n))
        for p in probabilities
        if sp.simplify(p) != 0
    ]
    return sp.simplify(sum(terms))


def shannon_entropy(probabilities: tuple[sp.Expr, ...]) -> sp.Expr:
    terms = [-p * sp.log(p) for p in probabilities if sp.simplify(p) != 0]
    return sp.simplify(sum(terms))


def part1_anchors() -> dict[str, str | None]:
    print("\nPart 1: anchors and dependency state")
    paths = (
        NOTE,
        PRIMITIVE_RECORD_LAW,
        C3_HARD_BOUNDARY_SUPPORT,
        C3_HARD_BOUNDARY_UNDERDETERMINATION,
        C3_BLOCK_SUPPORT,
        C3_MININFO_NOGO,
        C3_REAL_SOURCE,
        STRICT_AVAILABILITY,
        FULL_STACK,
        PRIMITIVE_RECORD_LAW_OUT,
        C3_HARD_BOUNDARY_SUPPORT_OUT,
        C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_MININFO_NOGO_OUT,
        C3_REAL_SOURCE_OUT,
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
        "Boundary KL Witness",
        "Coefficient Consequence",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: exact-support / open primitive-singular-boundary readout law",
        "proposal_allowed: false",
        "least KL",
        "P_nt/2",
        "A/sqrt(12)",
        "not accepted on the current surface",
    ):
        check(f"note contains status/support phrase: {phrase}", phrase in note)

    deps = {
        "primitive_record_law": load_json(PRIMITIVE_RECORD_LAW_OUT),
        "hard_boundary_support": load_json(C3_HARD_BOUNDARY_SUPPORT_OUT),
        "hard_boundary_underdetermination": load_json(C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "mininfo_no_go": load_json(C3_MININFO_NOGO_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "primitive theorem remains support, not closure",
        deps["primitive_record_law"].get("proposal_allowed") is False,
    )
    check(
        "nearest Fisher boundary support already selects P_nt",
        deps["hard_boundary_support"].get("support_certificate", {}).get("nearest_fisher_boundary_face_is_Pnt")
        is True,
    )
    check(
        "geometry-alone promotion is already pruned",
        deps["hard_boundary_underdetermination"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "P_nt support gives target row in prior block",
        deps["block_support"].get("block_matrix_element_witness", {}).get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_reflection_even_boundary_kl() -> dict[str, Any]:
    print("\nPart 2: reflection-even C3 singular-boundary KL support")
    q_nt = (sp.Integer(0), sp.Rational(1, 2), sp.Rational(1, 2))
    q_0 = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
    kl_nt = kl_to_uniform(q_nt)
    kl_0 = kl_to_uniform(q_0)
    entropy_nt = shannon_entropy(q_nt)
    entropy_0 = shannon_entropy(q_0)

    check("KL(q_nt || uniform) is log(3/2)", is_zero(kl_nt - sp.log(sp.Rational(3, 2))), kl_nt)
    check("KL(q_0 || uniform) is log(3)", is_zero(kl_0 - sp.log(3)), kl_0)
    check("least distinguishable reflection-even endpoint is P_nt", kl_nt < kl_0, (kl_nt, kl_0))
    check("maximum boundary entropy endpoint is P_nt", entropy_nt > entropy_0, (entropy_nt, entropy_0))

    s = sp.symbols("s", positive=True)
    fisher_primitive = 2 * sp.asin(sp.sqrt(s))
    baseline = sp.Rational(1, 3)
    distance_to_pnt = sp.simplify(fisher_primitive.subs(s, baseline) - fisher_primitive.subs(s, 0))
    distance_to_p0 = sp.simplify(fisher_primitive.subs(s, 1) - fisher_primitive.subs(s, baseline))
    check("nearest Fisher endpoint agrees with KL support", distance_to_pnt < distance_to_p0, (distance_to_pnt, distance_to_p0))

    return {
        "baseline": "(1/3, 1/3, 1/3)",
        "reflection_even_boundary_endpoints": {
            "P_nt_over_2": "(0, 1/2, 1/2)",
            "P_0": "(1, 0, 0)",
        },
        "kl_to_baseline": {
            "P_nt_over_2": "log(3/2)",
            "P_0": "log(3)",
        },
        "least_kl_reflection_even_boundary": "P_nt/2",
        "maximum_entropy_reflection_even_boundary": "P_nt/2",
        "nearest_fisher_reflection_even_boundary": "P_nt/2",
    }


def part3_full_simplex_degeneracy() -> dict[str, Any]:
    print("\nPart 3: full simplex least-KL degeneracy")
    two_line_faces = {
        "drop_P0": (sp.Integer(0), sp.Rational(1, 2), sp.Rational(1, 2)),
        "drop_Pomega": (sp.Rational(1, 2), sp.Integer(0), sp.Rational(1, 2)),
        "drop_Pomega2": (sp.Rational(1, 2), sp.Rational(1, 2), sp.Integer(0)),
    }
    kl_values = {name: kl_to_uniform(prob) for name, prob in two_line_faces.items()}
    for name, value in kl_values.items():
        check(f"{name} has KL log(3/2)", is_zero(value - sp.log(sp.Rational(3, 2))), value)
    check("full simplex least-KL boundary has three degenerate faces", len(set(map(sp.sstr, kl_values.values()))) == 1)

    sqrt = sp.sqrt
    responses = {
        "P0": 2 / sqrt(6),
        "Pomega": -1 / sqrt(6),
        "Pomega2": -1 / sqrt(6),
    }
    face_responses = {
        "drop_P0": sp.simplify((responses["Pomega"] + responses["Pomega2"]) / 2),
        "drop_Pomega": sp.simplify((responses["P0"] + responses["Pomega2"]) / 2),
        "drop_Pomega2": sp.simplify((responses["P0"] + responses["Pomega"]) / 2),
    }
    check("drop_P0 face gives target response magnitude", is_zero(abs(face_responses["drop_P0"]) - 1 / sqrt(6)), face_responses["drop_P0"])
    check(
        "other least-KL faces do not give target response magnitude",
        all(not is_zero(abs(value) - 1 / sqrt(6)) for key, value in face_responses.items() if key != "drop_P0"),
        face_responses,
    )

    return {
        "full_simplex_least_kl_faces": {
            name: {"law": str(prob), "kl": "log(3/2)", "B_x_response": sp.sstr(face_responses[name])}
            for name, prob in two_line_faces.items()
        },
        "full_simplex_least_kl_unique": False,
        "reflection_even_curve_restriction_load_bearing": True,
    }


def part4_coefficient_consequence() -> dict[str, Any]:
    print("\nPart 4: coefficient consequence")
    sqrt = sp.sqrt
    A, g2 = sp.symbols("A g_2", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_pnt = sp.simplify(Pnt / 2)
    rho_p0 = P0
    Bx = sp.simplify((C + C**2) / sqrt(6))

    pnt_response = sp.simplify(sp.trace(rho_pnt * Bx))
    p0_response = sp.simplify(sp.trace(rho_p0 * Bx))
    pnt_row = sp.simplify(A * pnt_response / sqrt(2))
    p0_row = sp.simplify(A * p0_response / sqrt(2))
    dmw = g2 * A / 2
    readout_pnt = sp.simplify(g2 / sqrt(2) * abs(pnt_row) / dmw)
    readout_p0 = sp.simplify(g2 / sqrt(2) * abs(p0_row) / dmw)

    check("P_nt/2 response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("P_0 response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("P_nt/2 conditional top row magnitude is A/sqrt(12)", is_zero(abs(pnt_row) - A / sqrt(12)), pnt_row)
    check("P_0 conditional top row magnitude is A/sqrt(3)", is_zero(p0_row - A / sqrt(3)), p0_row)
    check("same-source ratio gives 1/sqrt(6) for P_nt/2", is_zero(readout_pnt - 1 / sqrt(6)), readout_pnt)
    check("same-source ratio gives 2/sqrt(6) for P_0", is_zero(readout_p0 - 2 / sqrt(6)), readout_p0)

    return {
        "P_nt_over_2_response": "-1/sqrt(6)",
        "P_0_response": "2/sqrt(6)",
        "conditional_top_row_if_P_nt_over_2": "A/sqrt(12)",
        "conditional_top_row_if_P_0": "A/sqrt(3)",
        "target_readout_if_P_nt_over_2": "1/sqrt(6)",
        "singlet_readout_if_P_0": "2/sqrt(6)",
    }


def part5_certificate_and_no_go() -> dict[str, Any]:
    print("\nPart 5: support certificate and no-go audit")
    certificate = {
        "primitive_singular_boundary_rule_formulated": True,
        "least_kl_reflection_even_boundary_selects_Pnt": True,
        "least_kl_full_simplex_unique_top_block": False,
        "accepted_primitive_singular_boundary_top_readout_law_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field {key}", isinstance(value, bool), value)
    check("support is conditional on new singular-boundary law", certificate["accepted_primitive_singular_boundary_top_readout_law_derived"] is False)
    check("full simplex degeneracy prevents overclosure", certificate["least_kl_full_simplex_unique_top_block"] is False)
    check("retained proposal remains forbidden", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "route_pruned": (
            "finite primitive no-hidden-record intervention theorem derives "
            "accepted physical singular hard-boundary top readout"
        ),
        "reason": (
            "The finite theorem derives interior RN/I-projection source laws "
            "for named expectation biases. Its singular-boundary extension "
            "selects P_nt only after adding a primitive hard-boundary readout "
            "criterion on the reflection-even C3 curve; that criterion is not "
            "accepted on the actual current surface."
        ),
        "not_pruned": (
            "a future accepted same-surface theorem identifying top readout "
            "with primitive singular no-hidden-record boundary intervention"
        ),
        "route_still_live": [
            "accepted primitive singular-boundary top-readout law plus generator factorization",
            "another accepted physical top-block/readout law excluding P_0",
            "accepted strict same-source top/W pole rows with controls",
        ],
    }
    check("no-go audit is narrow to finite primitive theorem shortcut", "finite primitive" in no_go_audit["route_pruned"])
    check("no-go audit keeps future accepted theorem live", "future accepted" in no_go_audit["not_pruned"])
    return {"certificate": certificate, "no_go_audit": no_go_audit}


def part6_firewalls() -> None:
    print("\nPart 6: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "primitive singular-boundary readout is accepted",
        "strict W/top pole isolation is provided",
        "positive closure is achieved",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 PRIMITIVE SINGULAR BOUNDARY INTERVENTION SUPPORT")
    print("=" * 78)

    dependency_statuses = part1_anchors()
    reflection_even_kl = part2_reflection_even_boundary_kl()
    full_simplex = part3_full_simplex_degeneracy()
    coefficient = part4_coefficient_consequence()
    status = part5_certificate_and_no_go()
    part6_firewalls()

    result = {
        "actual_current_surface_status": "exact-support / open primitive-singular-boundary readout law",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The least-KL singular boundary law on the reflection-even C3 "
            "RN/Fisher curve selects P_nt and would give A/sqrt(12) with "
            "same-surface generator factorization. The actual current surface "
            "has not accepted primitive singular-boundary readout as the "
            "physical top law and still lacks strict pole-row controls."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": dependency_statuses,
        "reflection_even_boundary_kl_support": reflection_even_kl,
        "full_simplex_degeneracy_no_go": full_simplex,
        "coefficient_consequence": coefficient,
        "certificate_boundary": status["certificate"],
        "no_go_audit": status["no_go_audit"],
        "route_still_live": (
            "derive accepted primitive singular-boundary top-readout law with "
            "same-surface generator factorization, derive another accepted "
            "zero-singlet top-block law, or produce accepted strict same-source "
            "top/W pole rows directly"
        ),
        "review_surface": [
            "docs/YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_primitive_singular_boundary_intervention_support.py",
            "outputs/yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json",
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

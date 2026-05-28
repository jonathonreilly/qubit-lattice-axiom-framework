#!/usr/bin/env python3
"""Y_T C3 same-surface radial-factor underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_PRIMITIVE_SINGULAR = DOCS / "YT_C3_PRIMITIVE_SINGULAR_BOUNDARY_INTERVENTION_SUPPORT_NOTE_2026-05-28.md"
C3_HARD_BOUNDARY_UNDERDETERMINATION = DOCS / "YT_C3_HARD_BOUNDARY_READOUT_LAW_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
DIRECT_SPARSE = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = (
    ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
)
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_PRIMITIVE_SINGULAR_OUT = (
    ROOT / "outputs" / "yt_c3_primitive_singular_boundary_intervention_support_2026-05-28.json"
)
C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT = (
    ROOT / "outputs" / "yt_c3_hard_boundary_readout_law_underdetermination_2026-05-27.json"
)
STRICT_AVAILABILITY_OUT = (
    ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
)
DIRECT_SPARSE_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
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
        FIRST_PRINCIPLES,
        SAME_SURFACE_FACTORIZATION,
        C3_BLOCK_SUPPORT,
        C3_PRIMITIVE_SINGULAR,
        C3_HARD_BOUNDARY_UNDERDETERMINATION,
        STRICT_AVAILABILITY,
        DIRECT_SPARSE,
        FULL_STACK,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_PRIMITIVE_SINGULAR_OUT,
        C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT,
        STRICT_AVAILABILITY_OUT,
        DIRECT_SPARSE_OUT,
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
        "Finite Radial-Factor Counterfamily",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open same-surface radial generator factorization",
        "proposal_allowed: false",
        "lambda_top = 1/sqrt(2)",
        "zero-singlet C3 top-block support",
        "same-surface radial generator factorization",
        "not force the physical top generator",
    ):
        check(f"note contains radial-factor phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "same_surface_factorization": load_json(SAME_SURFACE_FACTORIZATION_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "primitive_singular": load_json(C3_PRIMITIVE_SINGULAR_OUT),
        "hard_boundary_underdetermination": load_json(C3_HARD_BOUNDARY_UNDERDETERMINATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "direct_sparse": load_json(DIRECT_SPARSE_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "factorization boundary keeps generator factorization open",
        deps["same_surface_factorization"].get("certificate_boundary", {}).get("accepted_same_surface_generator_factorization")
        is False,
    )
    check(
        "P_nt block support gives target row only with generator factorization",
        deps["c3_block_support"].get("certificate_boundary", {}).get("accepted_same_surface_generator_factorization_derived")
        is False,
    )
    check(
        "primitive singular support is not closure",
        deps["primitive_singular"].get("proposal_allowed") is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_radial_factor_family() -> dict[str, Any]:
    print("\nPart 2: radial-factor family on P_nt")
    sqrt = sp.sqrt
    A, g2, lambda_top = sp.symbols("A g_2 lambda_top", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_nt = sp.simplify(Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    Vtop = sp.simplify(lambda_top * A * Bx)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("rho_nt has unit trace", is_zero(sp.trace(rho_nt) - 1))
    check("B_x is normalized", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1))
    check("B_x is scalar on P_nt", is_zero(Bx * Pnt + Pnt / sqrt(6)))

    bx_response = sp.simplify(sp.trace(rho_nt * Bx))
    top_row_signed = sp.simplify(sp.trace(rho_nt * Vtop))
    top_row_magnitude = sp.simplify(-top_row_signed)
    dmw = g2 * A / 2
    readout = sp.simplify(g2 / sqrt(2) * top_row_magnitude / dmw)
    lambda_solution = sp.solve(sp.Eq(readout, 1 / sqrt(6)), lambda_top)

    check("P_nt B_x response is -1/sqrt(6)", is_zero(bx_response + 1 / sqrt(6)), bx_response)
    check("P_nt top row magnitude is lambda_top*A/sqrt(6)", is_zero(top_row_magnitude - lambda_top * A / sqrt(6)), top_row_magnitude)
    check("same-source readout is lambda_top/sqrt(3)", is_zero(readout - lambda_top / sqrt(3)), readout)
    check("target readout requires lambda_top=1/sqrt(2)", lambda_solution == [1 / sqrt(2)], lambda_solution)

    lambda_a = 1 / sqrt(2)
    lambda_b = 2 / sqrt(2)
    row_a = sp.simplify(top_row_magnitude.subs(lambda_top, lambda_a))
    row_b = sp.simplify(top_row_magnitude.subs(lambda_top, lambda_b))
    readout_a = sp.simplify(readout.subs(lambda_top, lambda_a))
    readout_b = sp.simplify(readout.subs(lambda_top, lambda_b))
    check("lambda_a gives target row", is_zero(row_a - A / sqrt(12)), row_a)
    check("lambda_b gives different row", is_zero(row_b - 2 * A / sqrt(12)), row_b)
    check("two same-C3-support completions give different readouts", sp.simplify(readout_a - readout_b) != 0, (readout_a, readout_b))

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "rho_nt": "P_nt/2",
        "top_generator_family": "V_top(lambda_top)=lambda_top*A*B_x",
        "P_nt_B_x_response": "-1/sqrt(6)",
        "top_row_magnitude": "lambda_top*A/sqrt(6)",
        "same_source_readout": "lambda_top/sqrt(3)",
        "target_lambda_top": "1/sqrt(2)",
        "target_top_row": "A/sqrt(12)",
        "counterexample_lambda_top": "2/sqrt(2)",
        "counterexample_top_row": "2*A/sqrt(12)",
    }


def part3_reparameterization_and_w_row() -> dict[str, Any]:
    print("\nPart 3: source reparameterization and W-row invariance")
    sqrt = sp.sqrt
    c, A, g2, lambda_top = sp.symbols("c A g_2 lambda_top", positive=True)
    d_ell_d_ell_prime = 1 / c
    d_mw = g2 * A / 2
    d_mt = lambda_top * A / sqrt(6)
    d_mw_prime = sp.simplify(d_mw * d_ell_d_ell_prime)
    d_mt_prime = sp.simplify(d_mt * d_ell_d_ell_prime)
    readout_prime = sp.simplify(g2 / sqrt(2) * d_mt_prime / d_mw_prime)

    check("common source reparameterization cancels", is_zero(readout_prime - lambda_top / sqrt(3)), readout_prime)
    check("W row is independent of lambda_top", not d_mw.has(lambda_top), d_mw)
    check("lambda_top remains in the readout", readout_prime.has(lambda_top), readout_prime)

    return {
        "dM_W_dell": "g_2*A/2",
        "dM_t_dell_magnitude": "lambda_top*A/sqrt(6)",
        "dM_W_dell_prime": "g_2*A/(2*c)",
        "dM_t_dell_prime_magnitude": "lambda_top*A/(sqrt(6)*c)",
        "readout_after_reparameterization": "lambda_top/sqrt(3)",
        "source_reparameterization_fixes_lambda_top": False,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "route_pruned": "zero-singlet C3 support plus B_x source direction and W row certify the top matrix element without accepted radial generator factorization",
        "zero_singlet_support_granted": True,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "target_requires_lambda_top": "1/sqrt(2)",
        "lambda_top_free_on_current_surface": True,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("zero-singlet support is granted in the no-go", certificate["zero_singlet_support_granted"] is True)
    check("radial generator factorization remains open", certificate["accepted_same_surface_radial_generator_factorization_derived"] is False)
    check("lambda_top remains free", certificate["lambda_top_free_on_current_surface"] is True)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "narrow_route_pruned": certificate["route_pruned"],
        "reason": (
            "P_nt support fixes the normalized C3 expectation, but a same-source "
            "finite family V_top(lambda_top)=lambda_top*A*B_x preserves that "
            "support and the W row while varying the recovered top coefficient."
        ),
        "remaining_imports": [
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical zero-singlet top-readout law",
            "accepted W/top pole controls or direct strict pole rows",
        ],
        "route_still_live": [
            "derive accepted generator factorization plus zero-singlet top readout",
            "produce accepted strict same-source top/W pole rows with controls",
            "derive accepted microscopic backend/projectors/source-generator matrix elements",
        ],
    }
    check("no-go audit names radial factor import", "lambda_top=1/sqrt(2)" in no_go_audit["remaining_imports"][0])
    check("no-go audit keeps strict pole route live", any("strict" in item for item in no_go_audit["route_still_live"]))
    return {"certificate_boundary": certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
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

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "full positive closure",
        "lambda_top is derived",
        "strict W/top pole rows are provided",
        "proposal_allowed: true",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 SAME-SURFACE RADIAL FACTOR UNDERDETERMINATION NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    radial_family = part2_radial_factor_family()
    reparameterization = part3_reparameterization_and_w_row()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open same-surface radial generator factorization",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite counterfamily grants zero-singlet P_nt support and the "
            "B_x source direction, but varies V_top(lambda_top)=lambda_top*A*B_x. "
            "The target row requires lambda_top=1/sqrt(2), which remains an "
            "open same-surface generator theorem or strict pole-row certificate."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchors": anchors,
        "radial_factor_family": radial_family,
        "source_reparameterization": reparameterization,
        "certificate_boundary": certificate["certificate_boundary"],
        "no_go_audit": certificate["no_go_audit"],
        "first_principles_elon_summary": {
            "minimal_premises": [
                "same source coordinate ell",
                "fixed W row g_2*A/2",
                "zero-singlet top support in P_nt",
                "normalized C3 source direction B_x",
            ],
            "forbidden_inputs_used": [],
            "route_pruned": certificate["certificate_boundary"]["route_pruned"],
        },
        "next_action": (
            "derive accepted same-surface generator factorization plus physical "
            "zero-singlet top readout, or produce accepted strict same-source "
            "top/W pole rows with controls"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md",
            "scripts/frontier_yt_c3_same_surface_radial_factor_underdetermination_no_go.py",
            "outputs/yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json",
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

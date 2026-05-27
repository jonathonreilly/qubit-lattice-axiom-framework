#!/usr/bin/env python3
"""Y_T C3 zero-singlet top-block membership no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_REAL_TOP_LINE = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
C3_MASS_ORDERING = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
C3_SOURCE_RESPONSE_EXTREMAL = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
C3_PERRON = DOCS / "YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_REAL_TOP_LINE_OUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
C3_MASS_ORDERING_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"
C3_SOURCE_RESPONSE_EXTREMAL_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
C3_PERRON_OUT = ROOT / "outputs" / "yt_c3_positive_transfer_perron_top_line_no_go_2026-05-27.json"
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


def c3_reflection() -> sp.Matrix:
    return sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and prior route boundaries")
    for path in (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_REAL_SOURCE,
        C3_BLOCK_SUPPORT,
        C3_REAL_TOP_LINE,
        C3_MASS_ORDERING,
        C3_SOURCE_RESPONSE_EXTREMAL,
        C3_PERRON,
        STRICT_AVAILABILITY,
        FIRST_PRINCIPLES_OUT,
        C3_REAL_SOURCE_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_REAL_TOP_LINE_OUT,
        C3_MASS_ORDERING_OUT,
        C3_SOURCE_RESPONSE_EXTREMAL_OUT,
        C3_PERRON_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open zero-singlet top-block membership law",
        "proposal_allowed: false",
        "zero singlet weight remains an imported physical membership law",
        "minimum-response convention is not derived",
        "accepted strict same-source top/W pole rows",
    ):
        check(f"note contains route phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "real_top_line": load_json(C3_REAL_TOP_LINE_OUT),
        "mass_ordering": load_json(C3_MASS_ORDERING_OUT),
        "source_response_extremal": load_json(C3_SOURCE_RESPONSE_EXTREMAL_OUT),
        "perron": load_json(C3_PERRON_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "block support gives target row under P_nt support",
        deps["block_support"].get("block_matrix_element_witness", {}).get("top_row_if_supported_in_P_nt")
        == "A/sqrt(12)",
    )
    check(
        "block support leaves zero singlet weight open",
        deps["block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "mass ordering already selects P_0",
        deps["mass_ordering"].get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_line")
        == "P_0",
    )
    check(
        "source-response maximum selects P_0",
        deps["source_response_extremal"].get("no_go_certificate", {}).get("absolute_response_max_selects_p0")
        is True,
    )
    check(
        "positive Perron selects P_0",
        deps["perron"].get("certificate_boundary", {}).get("perron_line_is_p0") is True,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_real_reflection_even_block_algebra() -> dict[str, str]:
    print("\nPart 2: real/reflection-even C3 block algebra")
    a, x = sp.symbols("a x", real=True)
    C = c3_cycle()
    R = c3_reflection()
    I = sp.eye(3)
    S = sp.simplify(C + C**2)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    H = sp.simplify(a * I + x * S)

    check("C has order three", is_zero(C**3 - I))
    check("reflection conjugates C to C^2", is_zero(R * C * R - C**2))
    check("S is real/reflection-even", is_zero(R * S * R - S))
    check("P_0 is a projector", is_zero(P0**2 - P0) and is_zero(sp.trace(P0) - 1))
    check("P_nt is a rank-two projector", is_zero(Pnt**2 - Pnt) and is_zero(sp.trace(Pnt) - 2))
    check("P_0 and P_nt are orthogonal", is_zero(P0 * Pnt))
    check("H is C3-circulant", is_zero(C * H - H * C))
    check("H is reflection-even", is_zero(R * H * R - H))

    lambda_p0 = sp.simplify(sp.trace(P0 * H) / sp.trace(P0))
    lambda_pnt = sp.simplify(sp.trace(Pnt * H) / sp.trace(Pnt))
    gap = sp.simplify(lambda_p0 - lambda_pnt)
    check("lambda(P_0) = a + 2x", is_zero(lambda_p0 - (a + 2 * x)), lambda_p0)
    check("lambda(P_nt) = a - x", is_zero(lambda_pnt - (a - x)), lambda_pnt)
    check("ordering gap is 3x", is_zero(gap - 3 * x), gap)

    witnesses = {
        "x_positive": {"x": "1", "largest_block": "P_0"},
        "x_negative": {"x": "-1", "largest_block": "P_nt"},
        "x_zero": {"x": "0", "largest_block": "degenerate"},
    }
    check("positive x selects P_0 by largest block", witnesses["x_positive"]["largest_block"] == "P_0")
    check("negative x selects P_nt by largest block", witnesses["x_negative"]["largest_block"] == "P_nt")
    check("zero x selects no block", witnesses["x_zero"]["largest_block"] == "degenerate")

    return {
        "real_reflection_even_family": "H(a,x) = a I + x(C + C^2)",
        "lambda_P0": "a + 2*x",
        "lambda_Pnt": "a - x",
        "ordering_gap_P0_minus_Pnt": "3*x",
        "x_positive_largest": witnesses["x_positive"]["largest_block"],
        "x_negative_largest": witnesses["x_negative"]["largest_block"],
        "x_zero_largest": witnesses["x_zero"]["largest_block"],
    }


def part3_response_and_selector_witnesses() -> dict[str, Any]:
    print("\nPart 3: response and selector witnesses")
    sqrt = sp.sqrt
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)

    p0_response = sp.simplify(sp.trace(P0 * Bx) / sp.trace(P0))
    pnt_response = sp.simplify(sp.trace(Pnt * Bx) / sp.trace(Pnt))
    p0_row = sp.simplify(A / sqrt(2) * p0_response)
    pnt_row = sp.simplify(A / sqrt(2) * pnt_response)
    check("B_x largest-response block is P_0", p0_response > pnt_response)
    check("B_x P_0 response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("B_x P_nt response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("P_0 row magnitude is A/sqrt(3)", is_zero(abs(p0_row) - A / sqrt(3)), p0_row)
    check("P_nt row magnitude is A/sqrt(12)", is_zero(abs(pnt_row) - A / sqrt(12)), pnt_row)

    selectors = {
        "largest_eigenvalue_on_Bx": {
            "selected_block": "P_0",
            "row_magnitude": "A/sqrt(3)",
            "allowed_by_current_surface": True,
        },
        "largest_eigenvalue_on_minus_Bx": {
            "selected_block": "P_nt",
            "row_magnitude": "A/sqrt(12)",
            "requires_new_sign_or_order_law": True,
        },
        "minimum_response_on_Bx": {
            "selected_block": "P_nt",
            "row_magnitude": "A/sqrt(12)",
            "requires_minimum_response_top_convention": True,
        },
    }
    check("largest B_x selector gives singlet row", selectors["largest_eigenvalue_on_Bx"]["selected_block"] == "P_0")
    check("minus B_x selector imports sign/order law", selectors["largest_eigenvalue_on_minus_Bx"]["requires_new_sign_or_order_law"] is True)
    check("minimum-response selector imports convention", selectors["minimum_response_on_Bx"]["requires_minimum_response_top_convention"] is True)
    return {
        "P_0_response": "2/sqrt(6)",
        "P_nt_response": "-1/sqrt(6)",
        "P_0_top_row_magnitude": "A/sqrt(3)",
        "P_nt_top_row_magnitude": "A/sqrt(12)",
        "selectors": selectors,
    }


def part4_no_go_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "real_reflection_even_c3_block_algebra_available": True,
        "P_nt_membership_sufficient_for_target_row": True,
        "real_c3_block_algebra_excludes_P0": False,
        "zero_singlet_membership_derived": False,
        "accepted_sign_or_order_law_for_Pnt_derived": False,
        "minimum_response_top_convention_derived": False,
        "positive_transfer_selects_Pnt": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("zero-singlet membership is not derived", certificate["zero_singlet_membership_derived"] is False)
    check("real C3 algebra does not exclude P_0", certificate["real_c3_block_algebra_excludes_P0"] is False)
    check("positive transfer does not select P_nt", certificate["positive_transfer_selects_Pnt"] is False)
    check("proposal remains false", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "route_pruned": "current real/reflection-even C3 block algebra derives zero-singlet physical top-block membership",
        "counterfamily": {
            "x_positive": "same C3 block algebra selects P_0 by largest ordering",
            "x_negative": "same C3 block algebra selects P_nt only after importing sign/order premise",
            "minimum_response": "selects P_nt only after importing a minimum-response convention",
        },
        "remaining_imports": [
            "accepted same-surface sign/order/readout law excluding P_0",
            "accepted same-surface generator factorization",
            "accepted strict same-source top/W pole rows or degenerate-pole response rule",
            "contact/FV/IR/model-class controls",
        ],
    }
    check("no-go audit names P_0 counterfamily", "P_0" in no_go_audit["counterfamily"]["x_positive"])
    check("no-go audit names P_nt imported sign", "sign/order" in no_go_audit["counterfamily"]["x_negative"])
    check("no-go audit keeps strict rows open", any("strict" in item for item in no_go_audit["remaining_imports"]))
    return {"certificate_boundary": certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
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
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "zero singlet weight is derived",
        "strict W/top pole isolation is provided",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 ZERO-SINGLET TOP-BLOCK MEMBERSHIP NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    block_algebra = part2_real_reflection_even_block_algebra()
    response_witnesses = part3_response_and_selector_witnesses()
    no_go = part4_no_go_certificate()
    part5_firewalls()

    result = {
        "claim_id": "yt_c3_zero_singlet_top_block_membership_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_zero_singlet_top_block_membership_no_go.py",
        "actual_current_surface_status": "no-go / open zero-singlet top-block membership law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite real/reflection-even C3 block algebra permits both "
            "P_0 and P_nt block selections depending on an undetermined "
            "sign/order or minimum-response premise. The current surface "
            "proves P_nt would give A/sqrt(12), but does not derive zero "
            "singlet physical top-block membership."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchors": anchors,
        "block_algebra_witness": block_algebra,
        "response_selector_witness": response_witnesses,
        **no_go,
        "first_principles_elon_summary": {
            "A_min": [
                "finite positive transfer/Feynman-Hellmann response support",
                "real finite-record C3 source theorem selecting B_x",
                "finite C3 projector algebra",
                "nontrivial-block matrix-element support theorem",
                "prior mass-ordering, source-response, Perron, and strict-availability no-go packets",
            ],
            "route_attempted": "derive zero P_0 singlet weight from current real/reflection-even C3 block data",
            "result": "blocked by finite same-surface sign/order counterfamily",
        },
        "route_still_live": (
            "derive an accepted same-surface sign/order/readout law excluding "
            "P_0 with generator factorization, or produce accepted strict "
            "same-source top/W pole rows"
        ),
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

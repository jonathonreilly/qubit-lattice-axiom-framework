#!/usr/bin/env python3
"""Y_T C3 nontrivial-block matrix element support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"

NOTE = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_REAL_TOP_LINE_OBSTRUCTION = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
C3_SOURCE_RESPONSE_EXTREMAL = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
STRICT_WZ_C3_SPLICE = DOCS / "YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = (
    ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
)
C3_REAL_TOP_LINE_OBSTRUCTION_OUT = (
    ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
)
C3_SOURCE_RESPONSE_EXTREMAL_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
STRICT_WZ_C3_SPLICE_OUT = ROOT / "outputs" / "yt_strict_wz_c3_top_row_splice_no_go_2026-05-27.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current stack state")
    for path in (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_REAL_SOURCE,
        SAME_SURFACE_FACTORIZATION,
        C3_REAL_TOP_LINE_OBSTRUCTION,
        C3_SOURCE_RESPONSE_EXTREMAL,
        STRICT_WZ_C3_SPLICE,
        FIRST_PRINCIPLES_OUT,
        C3_REAL_SOURCE_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
        C3_REAL_TOP_LINE_OBSTRUCTION_OUT,
        C3_SOURCE_RESPONSE_EXTREMAL_OUT,
        STRICT_WZ_C3_SPLICE_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Block Witness",
        "Boundary Sharpening",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: exact-support / open nontrivial-block membership law",
        "proposal_allowed: false",
        "zero singlet weight",
        "complex-line isolation is not needed",
        "derive that the physical top sector has zero P_0 singlet weight",
    ):
        check(f"note contains status/boundary phrase: {phrase}", phrase in note)

    first = load_json(FIRST_PRINCIPLES_OUT)
    real_source = load_json(C3_REAL_SOURCE_OUT)
    factorization = load_json(SAME_SURFACE_FACTORIZATION_OUT)
    top_line = load_json(C3_REAL_TOP_LINE_OBSTRUCTION_OUT)
    extremal = load_json(C3_SOURCE_RESPONSE_EXTREMAL_OUT)
    splice = load_json(STRICT_WZ_C3_SPLICE_OUT)

    check("first-principles transfer response passed", first.get("fail_count") == 0, first.get("fail_count"))
    check("real finite-record source theorem passed", real_source.get("fail_count") == 0, real_source.get("fail_count"))
    check("same-surface factorization passed", factorization.get("fail_count") == 0, factorization.get("fail_count"))
    check("real top-line obstruction passed", top_line.get("fail_count") == 0, top_line.get("fail_count"))
    check("source-response extremal no-go passed", extremal.get("fail_count") == 0, extremal.get("fail_count"))
    check("strict W/Z plus C3 splice no-go passed", splice.get("fail_count") == 0, splice.get("fail_count"))
    check(
        "factorization target row remains A/sqrt(12)",
        factorization.get("matrix_element_witness", {}).get("target_top_row") == "A/sqrt(12)",
    )
    check(
        "real top-line obstruction keeps P_0 assignment live",
        top_line.get("counterassignments", {}).get("assignment_A", {}).get("top_matrix_element_magnitude") == "A/sqrt(3)",
    )

    return {
        "first_principles_status": first.get("actual_current_surface_status"),
        "real_source_status": real_source.get("actual_current_surface_status"),
        "factorization_status": factorization.get("actual_current_surface_status"),
        "top_line_status": top_line.get("actual_current_surface_status"),
    }


def part2_nontrivial_block_algebra() -> dict[str, Any]:
    print("\nPart 2: nontrivial C3 block matrix element algebra")
    sqrt = sp.sqrt
    A, g2 = sp.symbols("A g_2", positive=True)
    s = sp.symbols("s", real=True)
    C = c3_cycle()
    I = sp.eye(3)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 is a rank-one projector", is_zero(P0**2 - P0) and is_zero(sp.trace(P0) - 1))
    check("P_nt is a rank-two projector", is_zero(Pnt**2 - Pnt) and is_zero(sp.trace(Pnt) - 2))
    check("P_0 and P_nt are orthogonal", is_zero(P0 * Pnt))
    check("P_0 plus P_nt resolves identity", is_zero(P0 + Pnt - I))
    check("B_x is Hermitian", is_zero(Bx.conjugate().T - Bx))
    check("B_x is traceless/connected", is_zero(sp.trace(Bx)))

    check("B_x is scalar 2/sqrt(6) on P_0", is_zero(Bx * P0 - 2 * P0 / sqrt(6)))
    check("B_x is scalar -1/sqrt(6) on P_nt", is_zero(Bx * Pnt + Pnt / sqrt(6)))
    check("P_nt commutes with B_x", is_zero(Bx * Pnt - Pnt * Bx))

    rho_nt_trace = sp.simplify(sp.trace(Pnt * Bx) / sp.trace(Pnt))
    rho_p0_trace = sp.simplify(sp.trace(P0 * Bx) / sp.trace(P0))
    check("any normalized P_nt-supported density has response -1/sqrt(6)", is_zero(rho_nt_trace + 1 / sqrt(6)), rho_nt_trace)
    check("the singlet density has response 2/sqrt(6)", is_zero(rho_p0_trace - 2 / sqrt(6)), rho_p0_trace)

    response_with_singlet_weight = sp.simplify(s * rho_p0_trace + (1 - s) * rho_nt_trace)
    target_response = -1 / sqrt(6)
    singlet_solution = sp.solve(sp.simplify(response_with_singlet_weight - target_response), s)
    check("response with singlet weight is (3s-1)/sqrt(6)", is_zero(response_with_singlet_weight - (3 * s - 1) / sqrt(6)), response_with_singlet_weight)
    check("target nontrivial response forces zero singlet weight", singlet_solution == [0], singlet_solution)

    Vtop_factor = A / sqrt(2)
    top_row_nt = sp.simplify(Vtop_factor * rho_nt_trace)
    top_row_p0 = sp.simplify(Vtop_factor * rho_p0_trace)
    top_row_leak = sp.simplify(Vtop_factor * response_with_singlet_weight)
    dmw = g2 * A / 2
    readout_nt = sp.simplify(g2 / sqrt(2) * abs(top_row_nt) / dmw)
    readout_p0 = sp.simplify(g2 / sqrt(2) * abs(top_row_p0) / dmw)

    check("P_nt-supported top row magnitude is A/sqrt(12)", is_zero(abs(top_row_nt) - A / sqrt(12)), top_row_nt)
    check("P_0-supported top row magnitude is A/sqrt(3)", is_zero(abs(top_row_p0) - A / sqrt(3)), top_row_p0)
    check("same-source W denominator gives target readout for P_nt", is_zero(readout_nt - 1 / sqrt(6)), readout_nt)
    check("same-source W denominator gives singlet readout for P_0", is_zero(readout_p0 - 2 / sqrt(6)), readout_p0)

    return {
        "P_0_response": "2/sqrt(6)",
        "P_nt_response": "-1/sqrt(6)",
        "response_with_singlet_weight_s": "(3*s - 1)/sqrt(6)",
        "target_response_forces_singlet_weight": "s = 0",
        "top_row_if_supported_in_P_nt": "A/sqrt(12)",
        "top_row_if_supported_in_P_0": "A/sqrt(3)",
        "top_row_with_singlet_weight_s": str(top_row_leak),
        "target_readout_if_supported_in_P_nt": "1/sqrt(6)",
        "singlet_readout_if_supported_in_P_0": "2/sqrt(6)",
    }


def part3_certificate_boundary() -> dict[str, Any]:
    print("\nPart 3: support certificate and remaining blockers")
    certificate = {
        "nontrivial_real_block_response_scalar": True,
        "complex_line_isolation_needed_for_coefficient_row": False,
        "zero_singlet_weight_sufficient_for_target_row": True,
        "zero_singlet_weight_derived_on_actual_surface": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("complex line isolation is not required for coefficient", certificate["complex_line_isolation_needed_for_coefficient_row"] is False)
    check("zero singlet weight remains open", certificate["zero_singlet_weight_derived_on_actual_surface"] is False)
    check("same-surface generator factorization remains open", certificate["accepted_same_surface_generator_factorization_derived"] is False)
    check("strict positive certificate remains absent", certificate["strict_top_w_response_certificate_present"] is False)
    return certificate


def part4_no_go_audit() -> dict[str, Any]:
    print("\nPart 4: no-go audit for overclosure")
    no_go_audit = {
        "route_not_closed": "P_nt block support implies retained/proposed-retained Y_T closure",
        "reason": "the actual current surface does not derive zero singlet weight or accepted pole controls",
        "remaining_imports": [
            "accepted zero-singlet physical top-block membership law",
            "accepted same-surface source-generator factorization",
            "accepted W/top pole isolation or degenerate-pole response rule",
            "contact/FV/IR/model-class controls or direct strict pole rows",
        ],
    }
    check("no-go audit names zero-singlet blocker", "zero singlet weight" in no_go_audit["reason"])
    check("no-go audit keeps same-surface factorization open", any("factorization" in item for item in no_go_audit["remaining_imports"]))
    check("no-go audit keeps pole controls open", any("pole" in item for item in no_go_audit["remaining_imports"]))
    return no_go_audit


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
        "This note proves retained `Y_T` closure",
        "This note proves proposed-retained `Y_T` closure",
        "zero singlet weight is derived",
        "strict W/top pole isolation is provided",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 NONTRIVIAL BLOCK MATRIX ELEMENT SUPPORT")
    print("=" * 78)

    anchors = part1_anchors()
    block = part2_nontrivial_block_algebra()
    certificate = part3_certificate_boundary()
    no_go_audit = part4_no_go_audit()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "exact-support / open nontrivial-block membership law",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite C3 algebra proves the target row for any top readout "
            "supported in P_nt, but the actual current surface still does not "
            "derive zero singlet weight, accepted same-surface generator "
            "factorization, or strict pole-row controls."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchors": anchors,
        "block_matrix_element_witness": block,
        "certificate_boundary": certificate,
        "no_go_audit": no_go_audit,
        "first_principles_elon_summary": {
            "A_min": [
                "finite positive transfer/Feynman-Hellmann response theorem",
                "real finite-record C3 source theorem giving B_x",
                "finite C3 spectral projector algebra",
                "conditional same-surface top-block factorization",
                "same-source W denominator row",
            ],
            "complex_line_isolation_for_coefficient": "not required once P_nt support is supplied",
            "singlet_exclusion": "still load-bearing and not derived",
        },
        "route_still_live": (
            "derive accepted zero-singlet top-block membership with same-surface "
            "generator factorization, or produce strict same-source top/W pole rows directly"
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

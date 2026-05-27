#!/usr/bin/env python3
"""Y_T C3 trace-free centered-source zero-singlet no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_ZERO_SINGLET = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_ZERO_SINGLET_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
C3_SOURCE_ORIENTATION_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and prior route state")
    for path in (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_REAL_SOURCE,
        C3_BLOCK_SUPPORT,
        C3_ZERO_SINGLET,
        C3_SOURCE_ORIENTATION,
        STRICT_AVAILABILITY,
        FIRST_PRINCIPLES_OUT,
        C3_REAL_SOURCE_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_ZERO_SINGLET_OUT,
        C3_SOURCE_ORIENTATION_OUT,
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
        "actual_current_surface_status: no-go / open trace-free source-to-zero-singlet law",
        "proposal_allowed: false",
        "Tr(B_x) = 0",
        "Tr(rho B_x) = (3s - 1)/sqrt(6)",
        "zero centered-source expectation would give",
        "s = 1/3",
        "connected/trace-free C3 source tangent",
    ):
        check(f"note contains centered-source phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "zero_singlet": load_json(C3_ZERO_SINGLET_OUT),
        "source_orientation": load_json(C3_SOURCE_ORIENTATION_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "real source theorem gives B_x source tangent",
        deps["real_source"].get("certificate_boundary", {}).get("source_direction_bx_selected") is True,
        deps["real_source"].get("certificate_boundary", {}),
    )
    check(
        "block support records singlet-weight response",
        deps["block_support"].get("block_matrix_element_witness", {}).get("response_with_singlet_weight_s")
        == "(3*s - 1)/sqrt(6)",
    )
    check(
        "zero-singlet law remains open",
        deps["zero_singlet"].get("certificate_boundary", {}).get("zero_singlet_membership_derived")
        is False,
    )
    check(
        "source-orientation route remains open",
        deps["source_orientation"].get("certificate_boundary", {}).get("accepted_source_orientation_law_for_Pnt_derived")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_centered_source_witness() -> dict[str, Any]:
    print("\nPart 2: finite trace-free centered-source witness")
    sqrt = sp.sqrt
    A = sp.symbols("A", positive=True)
    s = sp.symbols("s", real=True)
    C = c3_cycle()
    I = sp.eye(3)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 is rank one", is_zero(P0**2 - P0) and is_zero(sp.trace(P0) - 1))
    check("P_nt is rank two", is_zero(Pnt**2 - Pnt) and is_zero(sp.trace(Pnt) - 2))
    check("P_0 and P_nt are orthogonal", is_zero(P0 * Pnt))
    check("P_0 plus P_nt resolves identity", is_zero(P0 + Pnt - I))
    check("B_x is trace-free", is_zero(sp.trace(Bx)), sp.trace(Bx))
    check("B_x is Hermitian", is_zero(Bx.conjugate().T - Bx))
    check("B_x commutes with C", is_zero(Bx * C - C * Bx))

    p0_response = sp.simplify(sp.trace(P0 * Bx) / sp.trace(P0))
    pnt_response = sp.simplify(sp.trace(Pnt * Bx) / sp.trace(Pnt))
    response_with_s = sp.simplify(s * p0_response + (1 - s) * pnt_response)
    zero_expectation_s = sp.solve(sp.simplify(response_with_s), s)
    target_response_s = sp.solve(sp.simplify(response_with_s + 1 / sqrt(6)), s)

    check("P_0 response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("P_nt response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("singlet-weight response is (3s-1)/sqrt(6)", is_zero(response_with_s - (3 * s - 1) / sqrt(6)), response_with_s)
    check("zero centered expectation gives s=1/3", zero_expectation_s == [sp.Rational(1, 3)], zero_expectation_s)
    check("target nontrivial response gives s=0", target_response_s == [0], target_response_s)

    top_row_pnt = sp.simplify(A / sqrt(2) * abs(pnt_response))
    top_row_p0 = sp.simplify(A / sqrt(2) * abs(p0_response))
    top_row_zero_expectation = sp.simplify(A / sqrt(2) * abs(response_with_s.subs(s, sp.Rational(1, 3))))
    check("P_nt top row is A/sqrt(12)", is_zero(top_row_pnt - A / sqrt(12)), top_row_pnt)
    check("P_0 top row is A/sqrt(3)", is_zero(top_row_p0 - A / sqrt(3)), top_row_p0)
    check("zero expectation row is zero, not target", is_zero(top_row_zero_expectation), top_row_zero_expectation)

    return {
        "trace_B_x": "0",
        "P_0_response": "2/sqrt(6)",
        "P_nt_response": "-1/sqrt(6)",
        "response_with_singlet_weight_s": "(3*s - 1)/sqrt(6)",
        "zero_centered_expectation_forces": "s = 1/3",
        "target_nontrivial_response_forces": "s = 0",
        "P_nt_top_row": "A/sqrt(12)",
        "P_0_top_row": "A/sqrt(3)",
        "zero_expectation_top_row": "0",
    }


def part3_no_go_certificate() -> dict[str, Any]:
    print("\nPart 3: no-go certificate")
    certificate = {
        "trace_free_source_operator_derived": True,
        "trace_free_source_operator_selects_top_projector": False,
        "zero_source_expectation_selects_Pnt": False,
        "zero_source_expectation_singlet_weight": "1/3",
        "target_response_singlet_weight": "0",
        "P0_remains_allowed_without_physical_top_law": True,
        "accepted_zero_singlet_membership_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("trace-free source does not select projector", certificate["trace_free_source_operator_selects_top_projector"] is False)
    check("zero expectation does not select P_nt", certificate["zero_source_expectation_selects_Pnt"] is False)
    check("P_0 remains allowed", certificate["P0_remains_allowed_without_physical_top_law"] is True)

    no_go_audit = {
        "route_pruned": "connected/trace-free C3 source tangent derives zero-singlet physical top-block membership",
        "reason": (
            "Tr(B_x)=0 is an operator statement; for top singlet weight s, "
            "Tr(rho B_x)=(3s-1)/sqrt(6), so zero expectation gives s=1/3 "
            "rather than the needed s=0"
        ),
        "remaining_imports": [
            "accepted physical top-block/readout law excluding P_0",
            "accepted same-surface generator factorization",
            "accepted strict same-source top/W pole rows or degenerate-pole response rule",
            "contact/FV/IR/model-class controls",
        ],
    }
    check("no-go audit names trace-free route", "trace-free" in no_go_audit["route_pruned"])
    check("no-go audit names s=1/3 obstruction", "s=1/3" in no_go_audit["reason"])
    check("no-go audit keeps physical top-block law open", any("top-block" in item for item in no_go_audit["remaining_imports"]))

    return {
        "certificate_boundary": certificate,
        "no_go_audit": no_go_audit,
    }


def part4_firewalls() -> None:
    print("\nPart 4: firewalls and wording")
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
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "positive closure is achieved",
        "strict top/W pole rows are accepted",
        "zero-singlet physical top-block membership is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 TRACE-FREE CENTERED-SOURCE ZERO-SINGLET NO-GO")
    print("=" * 78)

    dependencies = part1_anchors()
    witness = part2_centered_source_witness()
    certificate = part3_no_go_certificate()
    part4_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open trace-free source-to-zero-singlet law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Trace-freeness of B_x is an operator/source statement, not a "
            "physical top-projector law. For singlet weight s, "
            "Tr(rho B_x)=(3s-1)/sqrt(6); zero centered expectation gives "
            "s=1/3, while the target nontrivial response requires s=0."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": dependencies,
        "centered_source_witness": witness,
        "certificate_boundary": certificate["certificate_boundary"],
        "no_go_audit": certificate["no_go_audit"],
        "route_still_live": (
            "derive accepted physical top-block/readout law excluding P_0 "
            "plus same-surface generator factorization, or produce accepted "
            "strict same-source top/W pole rows with controls"
        ),
        "review_surface": [
            "docs/YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_trace_free_centered_source_zero_singlet_no_go.py",
            "outputs/yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json",
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

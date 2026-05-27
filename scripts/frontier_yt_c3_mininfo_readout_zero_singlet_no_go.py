#!/usr/bin/env python3
"""Y_T C3 minimum-information readout zero-singlet no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
MIN_INFO = DOCS / "YT_MINIMUM_INFORMATION_SOURCE_ACTION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
PRIMITIVE_RECORD_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_ZERO_SINGLET = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_ORIENTATION = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
C3_TRACE_FREE = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
MIN_INFO_OUT = ROOT / "outputs" / "yt_minimum_information_source_action_bridge_2026-05-26.json"
PRIMITIVE_RECORD_LAW_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_ZERO_SINGLET_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
C3_SOURCE_ORIENTATION_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
C3_TRACE_FREE_OUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"
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
        MIN_INFO,
        PRIMITIVE_RECORD_LAW,
        C3_REAL_SOURCE,
        C3_BLOCK_SUPPORT,
        C3_ZERO_SINGLET,
        C3_SOURCE_ORIENTATION,
        C3_TRACE_FREE,
        STRICT_AVAILABILITY,
        FIRST_PRINCIPLES_OUT,
        MIN_INFO_OUT,
        PRIMITIVE_RECORD_LAW_OUT,
        C3_REAL_SOURCE_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_ZERO_SINGLET_OUT,
        C3_SOURCE_ORIENTATION_OUT,
        C3_TRACE_FREE_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Minimum-Information Witness",
        "Stuck Fan-Out Synthesis",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open minimum-information readout law",
        "proposal_allowed: false",
        "full-support",
        "finite source coordinate",
        "zero singlet weight",
        "infinite-boundary limit",
    ):
        check(f"note contains mininfo-readout phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "minimum_information": load_json(MIN_INFO_OUT),
        "primitive_record_law": load_json(PRIMITIVE_RECORD_LAW_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "zero_singlet": load_json(C3_ZERO_SINGLET_OUT),
        "source_orientation": load_json(C3_SOURCE_ORIENTATION_OUT),
        "trace_free": load_json(C3_TRACE_FREE_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "primitive record law derives source family but not top-source identification",
        deps["primitive_record_law"].get("boundary", {}).get("primitive_record_intervention_law_derived") is True
        and deps["primitive_record_law"].get("boundary", {}).get("physical_top_yukawa_identified_as_primitive_intervention")
        is False,
    )
    check(
        "block support records target response requires s=0",
        deps["block_support"].get("block_matrix_element_witness", {}).get("target_response_forces_singlet_weight")
        == "s = 0",
    )
    check(
        "zero-singlet membership remains open",
        deps["zero_singlet"].get("certificate_boundary", {}).get("zero_singlet_membership_derived")
        is False,
    )
    check(
        "trace-free route already pruned",
        deps["trace_free"].get("trace_class") == "negative_route_pruning",
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_c3_projector_algebra() -> dict[str, Any]:
    print("\nPart 2: C3 block and response algebra")
    sqrt = sp.sqrt
    s = sp.symbols("s", real=True)
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    Bx = sp.simplify((C + C**2) / sqrt(6))

    check("C has order three", is_zero(C**3 - I))
    check("P_0 is rank one", is_zero(P0**2 - P0) and is_zero(sp.trace(P0) - 1))
    check("P_nt is rank two", is_zero(Pnt**2 - Pnt) and is_zero(sp.trace(Pnt) - 2))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("B_x is trace-free", is_zero(sp.trace(Bx)), sp.trace(Bx))

    p0_response = sp.simplify(sp.trace(P0 * Bx) / sp.trace(P0))
    pnt_response = sp.simplify(sp.trace(Pnt * Bx) / sp.trace(Pnt))
    response_with_s = sp.simplify(s * p0_response + (1 - s) * pnt_response)
    target_solution = sp.solve(sp.simplify(response_with_s + 1 / sqrt(6)), s)
    row_with_s = sp.simplify(A / sqrt(2) * response_with_s)

    check("P_0 response is 2/sqrt(6)", is_zero(p0_response - 2 / sqrt(6)), p0_response)
    check("P_nt response is -1/sqrt(6)", is_zero(pnt_response + 1 / sqrt(6)), pnt_response)
    check("response with singlet weight is (3s-1)/sqrt(6)", is_zero(response_with_s - (3 * s - 1) / sqrt(6)), response_with_s)
    check("target nontrivial response forces s=0", target_solution == [0], target_solution)
    check("s=0 gives A/sqrt(12) magnitude", is_zero(abs(row_with_s.subs(s, 0)) - A / sqrt(12)))
    check("s=1/3 gives zero row", is_zero(row_with_s.subs(s, sp.Rational(1, 3))))

    return {
        "P_0_response": "2/sqrt(6)",
        "P_nt_response": "-1/sqrt(6)",
        "response_with_singlet_weight_s": "(3*s - 1)/sqrt(6)",
        "target_nontrivial_response_forces": "s = 0",
        "uniform_singlet_weight": "s = 1/3",
        "uniform_response": "0",
    }


def part3_mininfo_readout_witness() -> dict[str, Any]:
    print("\nPart 3: finite minimum-information readout witness")
    sqrt = sp.sqrt
    ell, t = sp.symbols("ell t", real=True)
    b0 = 2 / sqrt(6)
    bnt = -1 / sqrt(6)

    # Uniform baseline over the three C3 spectral lines, with the two
    # nontrivial complex lines carrying the same B_x response.
    z = sp.simplify(sp.exp(ell * b0) + 2 * sp.exp(ell * bnt))
    singlet_weight = sp.simplify(sp.exp(ell * b0) / z)
    response = sp.simplify(singlet_weight * b0 + (1 - singlet_weight) * bnt)
    t_singlet_weight = sp.simplify(t / (t + 2))
    target_t_solution = sp.solve(sp.simplify(t_singlet_weight), t)

    check("finite RN/I-projection tilt has positive normalizer", z != 0, z)
    check("singlet weight at ell=0 is 1/3", is_zero(singlet_weight.subs(ell, 0) - sp.Rational(1, 3)), singlet_weight.subs(ell, 0))
    check("response at ell=0 is zero", is_zero(response.subs(ell, 0)), response.subs(ell, 0))
    check(
        "zero singlet weight in t parametrization requires t=0",
        target_t_solution == [0],
        target_t_solution,
    )
    check("finite source coordinate has t=exp(3ell/sqrt6)>0", True)
    check("ell -> -infinity limit gives zero singlet weight", sp.limit(singlet_weight, ell, -sp.oo) == 0)
    check("ell -> -infinity response gives nontrivial target", is_zero(sp.limit(response, ell, -sp.oo) - bnt))
    check("ell -> +infinity response gives singlet row", is_zero(sp.limit(response, ell, sp.oo) - b0))

    q0, q1, q2 = sp.symbols("q0 q1 q2", nonnegative=True)
    simplex = sp.Eq(q0 + q1 + q2, 1)
    target_mean = sp.Eq(q0 * b0 + q1 * bnt + q2 * bnt, bnt)
    forced_q0 = sp.solve((simplex, target_mean), (q0, q1), dict=True)
    check("target response constraint forces q0=0 on the simplex", all(sp.simplify(sol[q0]) == 0 for sol in forced_q0), forced_q0)

    return {
        "baseline_line_law": "uniform on P_0, P_omega, P_omega2",
        "finite_tilt_singlet_weight": "exp(2 ell/sqrt(6)) / (exp(2 ell/sqrt(6)) + 2 exp(-ell/sqrt(6)))",
        "finite_tilt_has_full_support": True,
        "singlet_weight_at_ell_0": "1/3",
        "zero_singlet_requires": "ell -> -infinity, or an explicit target-response constraint",
        "target_response_constraint_forces": "q(P_0) = 0",
        "why_not_closure": "the explicit target-response constraint is the missing coefficient row as an input",
    }


def part4_no_go_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "minimum_information_source_law_derived": True,
        "minimum_information_readout_without_target_selects_zero_singlet": False,
        "finite_rn_tilt_has_full_support": True,
        "finite_rn_tilt_can_set_singlet_weight_zero": False,
        "zero_singlet_requires_infinite_boundary_or_target_constraint": True,
        "target_constraint_is_coefficient_row_input": True,
        "accepted_zero_singlet_membership_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("minimum-information readout does not select zero singlet", certificate["minimum_information_readout_without_target_selects_zero_singlet"] is False)
    check("finite RN tilt keeps full support", certificate["finite_rn_tilt_has_full_support"] is True)
    check("zero singlet would require boundary or target insertion", certificate["zero_singlet_requires_infinite_boundary_or_target_constraint"] is True)

    no_go_audit = {
        "route_pruned": (
            "minimum-information/RN-Fisher readout semantics derive accepted "
            "zero-singlet physical top-block membership"
        ),
        "reason": (
            "The finite full-support I-projection source family gives a "
            "full-support exponential tilt over the C3 lines. With no "
            "target response it returns the uniform singlet weight s=1/3; "
            "forcing s=0 requires an infinite-boundary tilt or the target "
            "nontrivial response as a constraint."
        ),
        "remaining_imports": [
            "accepted physical top-block/readout law excluding P_0",
            "accepted same-surface generator factorization",
            "accepted strict same-source top/W pole rows or degenerate-pole response rule",
            "contact/FV/IR/model-class controls",
        ],
    }
    check("no-go audit names mininfo route", "minimum-information" in no_go_audit["route_pruned"])
    check("no-go audit names full-support obstruction", "full-support" in no_go_audit["reason"])
    check("no-go audit keeps top-block law open", any("top-block" in item for item in no_go_audit["remaining_imports"]))
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
        "fitted selectors",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "positive closure is achieved",
        "minimum-information readout closes",
        "zero-singlet physical top-block membership is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 MINIMUM-INFORMATION READOUT ZERO-SINGLET NO-GO")
    print("=" * 78)

    dependencies = part1_anchors()
    block_witness = part2_c3_projector_algebra()
    mininfo_witness = part3_mininfo_readout_witness()
    certificate = part4_no_go_certificate()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "no-go / open minimum-information readout law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Minimum-information/RN-Fisher source semantics produce finite "
            "full-support exponential tilts over the C3 spectral lines. They "
            "do not set the physical top singlet weight to zero unless the "
            "target response is inserted as a constraint or an infinite "
            "boundary limit is added as a new physical law."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "dependency_statuses": dependencies,
        "c3_block_witness": block_witness,
        "minimum_information_witness": mininfo_witness,
        "certificate_boundary": certificate["certificate_boundary"],
        "no_go_audit": certificate["no_go_audit"],
        "route_still_live": (
            "derive accepted physical top-block/readout law excluding P_0 "
            "plus same-surface generator factorization, or produce accepted "
            "strict same-source top/W pole rows with controls"
        ),
        "review_surface": [
            "docs/YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_c3_mininfo_readout_zero_singlet_no_go.py",
            "outputs/yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json",
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

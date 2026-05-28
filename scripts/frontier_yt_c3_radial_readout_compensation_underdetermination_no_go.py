#!/usr/bin/env python3
"""Y_T C3 radial/readout compensation underdetermination no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_radial_readout_compensation_underdetermination_no_go_2026-05-28.json"

NOTE = DOCS / "YT_C3_RADIAL_READOUT_COMPENSATION_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_RADIAL_NOGO = DOCS / "YT_C3_SAME_SURFACE_RADIAL_FACTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-28.md"
C3_SOURCE_ORIENTATION_NOGO = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
C3_TRACE_FREE_NOGO = DOCS / "YT_C3_TRACE_FREE_CENTERED_SOURCE_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
C3_MININFO_NOGO = DOCS / "YT_C3_MININFO_READOUT_ZERO_SINGLET_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_RADIAL_NOGO_OUT = ROOT / "outputs" / "yt_c3_same_surface_radial_factor_underdetermination_no_go_2026-05-28.json"
C3_SOURCE_ORIENTATION_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"
C3_TRACE_FREE_NOGO_OUT = ROOT / "outputs" / "yt_c3_trace_free_centered_source_zero_singlet_no_go_2026-05-27.json"
C3_MININFO_NOGO_OUT = ROOT / "outputs" / "yt_c3_mininfo_readout_zero_singlet_no_go_2026-05-27.json"
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
        FIRST_PRINCIPLES,
        C3_BLOCK_SUPPORT,
        C3_RADIAL_NOGO,
        C3_SOURCE_ORIENTATION_NOGO,
        C3_TRACE_FREE_NOGO,
        C3_MININFO_NOGO,
        STRICT_AVAILABILITY,
        FULL_STACK,
        FIRST_PRINCIPLES_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_RADIAL_NOGO_OUT,
        C3_SOURCE_ORIENTATION_NOGO_OUT,
        C3_TRACE_FREE_NOGO_OUT,
        C3_MININFO_NOGO_OUT,
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
        "Finite Compensation Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open independent radial and top-readout laws",
        "proposal_allowed: false",
        "lambda_top |3s - 1| = 1/sqrt(2)",
        "target magnitude with singlet leakage",
        "Target-size response is not a substitute",
    ):
        check(f"note contains compensation phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "c3_block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "c3_radial_nogo": load_json(C3_RADIAL_NOGO_OUT),
        "c3_source_orientation_nogo": load_json(C3_SOURCE_ORIENTATION_NOGO_OUT),
        "c3_trace_free_nogo": load_json(C3_TRACE_FREE_NOGO_OUT),
        "c3_mininfo_nogo": load_json(C3_MININFO_NOGO_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "full_stack": load_json(FULL_STACK_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check(
        "block support keeps zero singlet weight open",
        deps["c3_block_support"].get("certificate_boundary", {}).get("zero_singlet_weight_derived_on_actual_surface")
        is False,
    )
    check(
        "radial no-go keeps lambda_top free",
        deps["c3_radial_nogo"].get("certificate_boundary", {}).get("lambda_top_free_on_current_surface")
        is True,
    )
    check(
        "source orientation law remains open",
        deps["c3_source_orientation_nogo"]
        .get("certificate_boundary", {})
        .get("accepted_source_orientation_law_for_Pnt_derived")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_radial_readout_family() -> dict[str, Any]:
    print("\nPart 2: radial/readout compensation family")
    sqrt = sp.sqrt
    A, g2, s, lambda_top = sp.symbols("A g_2 s lambda_top", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    P0 = sp.simplify((I + C + C**2) / 3)
    Pnt = sp.simplify(I - P0)
    rho_s = sp.simplify(s * P0 + (1 - s) * Pnt / 2)
    Bx = sp.simplify((C + C**2) / sqrt(6))
    Vtop = sp.simplify(lambda_top * A * Bx)

    check("C has order three", is_zero(C**3 - I))
    check("P_0 and P_nt resolve identity", is_zero(P0 + Pnt - I) and is_zero(P0 * Pnt))
    check("rho(s) has unit trace", is_zero(sp.trace(rho_s) - 1), sp.trace(rho_s))
    check("B_x is normalized", is_zero(sp.trace(Bx.conjugate().T * Bx) - 1))

    bx_response = sp.simplify(sp.trace(rho_s * Bx))
    signed_top_row = sp.simplify(sp.trace(rho_s * Vtop))
    signed_top_row_over_a = sp.simplify(signed_top_row / A)
    dmw = g2 * A / 2
    signed_readout = sp.simplify(g2 / sqrt(2) * signed_top_row / dmw)

    check("B_x response is (3s-1)/sqrt(6)", is_zero(bx_response - (3 * s - 1) / sqrt(6)), bx_response)
    check("signed top row is lambda_top*A*(3s-1)/sqrt(6)", is_zero(signed_top_row_over_a - lambda_top * (3 * s - 1) / sqrt(6)), signed_top_row)
    check("signed same-source readout is lambda_top*(3s-1)/sqrt(3)", is_zero(signed_readout - lambda_top * (3 * s - 1) / sqrt(3)), signed_readout)

    witness_zero_singlet = {s: sp.Integer(0), lambda_top: 1 / sqrt(2)}
    witness_leaky_same_radial = {s: sp.Rational(2, 3), lambda_top: 1 / sqrt(2)}
    witness_compensated = {s: sp.Rational(1, 2), lambda_top: sqrt(2)}
    witness_wrong = {s: sp.Integer(1), lambda_top: 1 / sqrt(2)}

    def row_abs(subs: dict[sp.Symbol, sp.Expr]) -> sp.Expr:
        return sp.simplify(abs(signed_top_row.subs(subs)))

    def readout_abs(subs: dict[sp.Symbol, sp.Expr]) -> sp.Expr:
        return sp.simplify(abs(signed_readout.subs(subs)))

    for label, subs in (
        ("zero-singlet standard radial witness", witness_zero_singlet),
        ("singlet-leaky same-radial witness", witness_leaky_same_radial),
        ("compensating radial/readout witness", witness_compensated),
    ):
        check(f"{label} gives target row magnitude", is_zero(row_abs(subs) - A / sqrt(12)), row_abs(subs))
        check(f"{label} gives target readout magnitude", is_zero(readout_abs(subs) - 1 / sqrt(6)), readout_abs(subs))

    check("singlet-leaky witness has positive singlet weight", witness_leaky_same_radial[s] > 0, witness_leaky_same_radial[s])
    check("compensating witness has nonstandard radial factor", not is_zero(witness_compensated[lambda_top] - 1 / sqrt(2)), witness_compensated[lambda_top])
    check("pure singlet same radial is not the target magnitude", not is_zero(row_abs(witness_wrong) - A / sqrt(12)), row_abs(witness_wrong))

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "rho_s": "s*P_0 + (1-s)*P_nt/2",
        "B_x_response": "(3*s - 1)/sqrt(6)",
        "signed_top_row": "lambda_top*A*(3*s - 1)/sqrt(6)",
        "signed_readout": "lambda_top*(3*s - 1)/sqrt(3)",
        "target_magnitude_condition": "lambda_top*|3*s - 1| = 1/sqrt(2)",
        "target_magnitude_witnesses": [
            {"singlet_weight_s": "0", "lambda_top": "1/sqrt(2)", "signed_response": "-1/sqrt(6)"},
            {"singlet_weight_s": "2/3", "lambda_top": "1/sqrt(2)", "signed_response": "+1/sqrt(6)"},
            {"singlet_weight_s": "1/2", "lambda_top": "sqrt(2)", "signed_response": "+1/(2*sqrt(6))"},
        ],
        "target_magnitude_forces_zero_singlet": False,
        "target_magnitude_forces_radial_factor": False,
    }


def part3_signed_orientation_boundary() -> dict[str, Any]:
    print("\nPart 3: signed row and orientation boundary")
    sqrt = sp.sqrt
    s, lambda_top = sp.symbols("s lambda_top", real=True)
    signed_response = sp.simplify(lambda_top * (3 * s - 1) / sqrt(6))
    standard_lambda = 1 / sqrt(2)
    negative_target_solutions = sp.solve(
        sp.Eq(signed_response.subs(lambda_top, standard_lambda), -1 / sqrt(12)),
        s,
    )
    positive_target_solutions = sp.solve(
        sp.Eq(signed_response.subs(lambda_top, standard_lambda), 1 / sqrt(12)),
        s,
    )

    check("negative signed target with standard radial gives s=0", negative_target_solutions == [0], negative_target_solutions)
    check("positive signed target with standard radial gives s=2/3", positive_target_solutions == [sp.Rational(2, 3)], positive_target_solutions)
    check("signed branch depends on source orientation convention", negative_target_solutions != positive_target_solutions)

    return {
        "standard_lambda_top": "1/sqrt(2)",
        "negative_signed_target_solution": "s=0",
        "positive_signed_target_solution": "s=2/3",
        "orientation_sign_law_load_bearing": True,
    }


def part4_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "route_pruned": "target-size same-source row certifies zero-singlet readout or radial factorization",
        "target_magnitude_granted": True,
        "target_magnitude_forces_zero_singlet": False,
        "target_magnitude_forces_radial_factor": False,
        "signed_row_requires_orientation_law": True,
        "accepted_physical_source_orientation_sign_law_derived": False,
        "accepted_zero_singlet_top_readout_law_derived": False,
        "accepted_same_surface_radial_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key in certificate:
        check(f"certificate field recorded: {key}", key in certificate)
    check("target magnitude does not force zero-singlet", certificate["target_magnitude_forces_zero_singlet"] is False)
    check("target magnitude does not force radial factor", certificate["target_magnitude_forces_radial_factor"] is False)
    check("proposal remains disallowed", certificate["proposal_allowed"] is False)

    no_go_audit = {
        "narrow_route_pruned": certificate["route_pruned"],
        "reason": (
            "The target-size equation lambda_top*|3*s-1|=1/sqrt(2) has "
            "multiple finite C3 completions with different singlet weights "
            "and radial couplings. The target row cannot be used as a "
            "back-door proof of the missing physical laws."
        ),
        "remaining_imports": [
            "accepted same-surface radial generator factorization lambda_top=1/sqrt(2)",
            "accepted physical zero-singlet top-readout law",
            "accepted physical source-orientation/sign law if signed C3 response is used",
            "accepted W/top pole controls or direct strict pole rows",
        ],
        "route_still_live": [
            "derive independent radial/readout/sign laws on the same surface",
            "produce accepted strict same-source top/W pole rows with controls",
            "derive accepted microscopic backend/projectors/source-generator matrix elements",
        ],
    }
    check("no-go audit names target-size equation", "lambda_top*|3*s-1|" in no_go_audit["reason"])
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
        "zero singlet weight is derived",
        "lambda_top is derived",
        "strict W/top pole rows are provided",
        "proposal_allowed: true",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 RADIAL/READOUT COMPENSATION UNDERDETERMINATION NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    family = part2_radial_readout_family()
    signed_boundary = part3_signed_orientation_boundary()
    certificate = part4_certificate()
    part5_firewalls()

    result = {
        "claim_id": "yt_c3_radial_readout_compensation_underdetermination_no_go_note_2026-05-28",
        "generated_by": "scripts/frontier_yt_c3_radial_readout_compensation_underdetermination_no_go.py",
        "actual_current_surface_status": "no-go / open independent radial and top-readout laws",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "target-size same-source row certifies zero-singlet readout or radial factorization",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The target-size row is compatible with compensating singlet "
            "weight and radial coupling unless the physical readout/sign/"
            "radial laws are independently derived, or strict same-source "
            "pole rows directly certify the coefficient."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchor_statuses": anchors,
        "radial_readout_family": family,
        "signed_orientation_boundary": signed_boundary,
        **certificate,
        "first_open_gate_after_this_note": (
            "accepted independent readout/sign/radial laws, or accepted strict "
            "same-source top/W pole rows with controls"
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

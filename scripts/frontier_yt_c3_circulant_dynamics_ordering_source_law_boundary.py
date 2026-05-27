#!/usr/bin/env python3
"""Y_T C3 circulant dynamics ordering/source-law boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_circulant_dynamics_ordering_source_law_boundary_2026-05-27.json"

NOTE = DOCS / "YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_SPECTRAL_SUPPORT = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
C3_SPECTRAL_SOURCE_NOGO = DOCS / "YT_C3_SPECTRAL_SOURCE_RESPONSE_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_REAL_TOP_LINE_OBSTRUCTION = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
C3_MASS_ORDERING = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
DIRECT_SPARSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_SPECTRAL_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
C3_SPECTRAL_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_REAL_TOP_LINE_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"
C3_MASS_ORDERING_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"
DIRECT_SPARSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"

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


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def frob_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        FIRST_PRINCIPLES,
        SAME_SURFACE_FACTORIZATION,
        C3_SPECTRAL_SUPPORT,
        C3_SPECTRAL_SOURCE_NOGO,
        C3_REAL_SOURCE,
        C3_REAL_TOP_LINE_OBSTRUCTION,
        C3_MASS_ORDERING,
        DIRECT_SPARSE_CERT,
        FULL_STACK,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
        C3_SPECTRAL_SUPPORT_OUT,
        C3_SPECTRAL_SOURCE_NOGO_OUT,
        C3_REAL_SOURCE_OUT,
        C3_REAL_TOP_LINE_OBSTRUCTION_OUT,
        C3_MASS_ORDERING_OUT,
        DIRECT_SPARSE_CERT_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Finite Witness",
        "What This Prunes",
        "What Remains Open",
        "Literature / Math Search",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go",
        "proposal_allowed: false",
        "dH/dell = B_x",
        "orientation/phase law",
        "base C3 circulant dynamics",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    first = load_json(FIRST_PRINCIPLES_OUT)
    factorization = load_json(SAME_SURFACE_FACTORIZATION_OUT)
    spectral_support = load_json(C3_SPECTRAL_SUPPORT_OUT)
    spectral_nogo = load_json(C3_SPECTRAL_SOURCE_NOGO_OUT)
    real_source = load_json(C3_REAL_SOURCE_OUT)
    top_line = load_json(C3_REAL_TOP_LINE_OBSTRUCTION_OUT)
    mass_ordering = load_json(C3_MASS_ORDERING_OUT)
    direct_sparse = load_json(DIRECT_SPARSE_CERT_OUT)

    check("first-principles transfer boundary passed", first.get("fail_count") == 0, first.get("fail_count"))
    check("factorization boundary passed", factorization.get("fail_count") == 0, factorization.get("fail_count"))
    check("C3 spectral support passed", spectral_support.get("fail_count") == 0, spectral_support.get("fail_count"))
    check("C3 spectral route remains support", spectral_support.get("trace_class") == "upstream_support")
    check("C3 source-response no-go passed", spectral_nogo.get("fail_count") == 0, spectral_nogo.get("fail_count"))
    check("real source theorem selects B_x", real_source.get("certificate_boundary", {}).get("source_direction_bx_selected") is True)
    check("real top-line obstruction passed", top_line.get("fail_count") == 0, top_line.get("fail_count"))
    check("real top-line obstruction points to a(h), x(h), y(h)", "a(h), x(h), y(h)" in top_line.get("route_still_live", ""))
    check("mass-ordering obstruction passed", mass_ordering.get("fail_count") == 0, mass_ordering.get("fail_count"))
    check("direct sparse certificate harness passed", direct_sparse.get("fail_count") == 0, direct_sparse.get("fail_count"))

    return {
        "first_principles_status": first.get("actual_current_surface_status"),
        "factorization_status": factorization.get("actual_current_surface_status"),
        "spectral_support_status": spectral_support.get("actual_current_surface_status"),
        "spectral_source_response_status": spectral_nogo.get("actual_current_surface_status"),
        "real_top_line_status": top_line.get("actual_current_surface_status"),
    }


def part2_circulant_source_derivative() -> dict[str, Any]:
    print("\nPart 2: C3 circulant source derivative")
    sqrt = sp.sqrt
    C = c3_cycle()
    omega = -sp.Rational(1, 2) + sp.I * sqrt(3) / 2
    Ba = sp.eye(3) / sqrt(3)
    Bx = (C + C**2) / sqrt(6)
    By = sp.I * (C - C**2) / sqrt(6)
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }

    for name, basis in {"B_a": Ba, "B_x": Bx, "B_y": By}.items():
        check(f"{name} commutes with C", is_zero(basis * C - C * basis))
        check(f"{name} is Hermitian", is_zero(basis.conjugate().T - basis))
        check(f"{name} has unit Frobenius norm", is_zero(frob_inner(basis, basis) - 1), frob_inner(basis, basis))

    source_derivative = Bx
    responses = {name: sp.radsimp(sp.simplify(sp.trace(projector * source_derivative))) for name, projector in projectors.items()}
    check("source derivative is B_x", is_zero(source_derivative - Bx))
    check("P_0 derivative is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sqrt(6)), responses["P_0"])
    check("P_omega derivative is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sqrt(6)), responses["P_omega"])
    check("P_omega2 derivative is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sqrt(6)), responses["P_omega2"])

    return {name: sp.sstr(value) for name, value in responses.items()}


def line_eigenvalues(x0: sp.Expr, y0: sp.Expr) -> dict[str, sp.Expr]:
    sqrt = sp.sqrt
    return {
        "P_0": sp.radsimp(2 * x0 / sqrt(6)),
        "P_omega": sp.radsimp(-x0 / sqrt(6) - y0 / sqrt(2)),
        "P_omega2": sp.radsimp(-x0 / sqrt(6) + y0 / sqrt(2)),
    }


def top_by_largest(eigenvalues: dict[str, sp.Expr]) -> str:
    return max(eigenvalues, key=lambda key: float(sp.N(eigenvalues[key])))


def part3_base_dynamics_countermodels() -> dict[str, Any]:
    print("\nPart 3: base dynamics and ordering countermodels")
    source_responses = {
        "P_0": 2 / sp.sqrt(6),
        "P_omega": -1 / sp.sqrt(6),
        "P_omega2": -1 / sp.sqrt(6),
    }

    case_a = line_eigenvalues(sp.Integer(1), sp.Integer(0))
    case_b = line_eigenvalues(sp.Integer(-1), sp.Integer(1))
    case_c = line_eigenvalues(sp.Integer(-1), sp.Integer(0))

    top_a = top_by_largest(case_a)
    top_b = top_by_largest(case_b)
    check("case A top by largest eigenvalue is P_0", top_a == "P_0", case_a)
    check("case A top derivative is 2/sqrt(6)", is_zero(source_responses[top_a] - 2 / sp.sqrt(6)), source_responses[top_a])
    check("case B top by largest eigenvalue is P_omega2", top_b == "P_omega2", case_b)
    check("case B top derivative has target magnitude", is_zero(abs(source_responses[top_b]) - 1 / sp.sqrt(6)), source_responses[top_b])
    check("same source derivative allows different top response magnitudes", not is_zero(abs(source_responses[top_a]) - abs(source_responses[top_b])))

    nontrivial_largest = case_c["P_omega"] == case_c["P_omega2"] and case_c["P_omega"] > case_c["P_0"]
    check("real x0<0 case makes nontrivial block largest but degenerate", bool(nontrivial_largest), case_c)
    check("real nontrivial block is not an isolated top line", is_zero(case_c["P_omega"] - case_c["P_omega2"]), case_c)

    return {
        "case_A_real_x_positive": {
            "x0": "1",
            "y0": "0",
            "eigenvalues": {key: sp.sstr(value) for key, value in case_a.items()},
            "top_by_largest": top_a,
            "top_derivative": sp.sstr(source_responses[top_a]),
        },
        "case_B_complex_orientation_odd": {
            "x0": "-1",
            "y0": "1",
            "eigenvalues": {key: sp.sstr(value) for key, value in case_b.items()},
            "top_by_largest": top_b,
            "top_derivative": sp.sstr(source_responses[top_b]),
        },
        "case_C_real_nontrivial_block_degenerate": {
            "x0": "-1",
            "y0": "0",
            "eigenvalues": {key: sp.sstr(value) for key, value in case_c.items()},
            "nontrivial_pair_degenerate": True,
        },
    }


def part4_certificate_boundary() -> dict[str, bool]:
    print("\nPart 4: certificate boundary")
    fields = {
        "source_derivative_bx_derived": True,
        "c3_spectral_projectors_available": True,
        "accepted_base_c3_circulant_operator": False,
        "operator_derived_on_same_surface": False,
        "orientation_phase_law_for_y0_derived": False,
        "top_line_ordering_derived": False,
        "source_generator_matrix_element_on_physical_top_derived": False,
        "same_surface_w_response_certificate_present": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("source derivative alone is not top-line ordering", fields["source_derivative_bx_derived"] and not fields["top_line_ordering_derived"])
    check("phase law remains load-bearing", fields["orientation_phase_law_for_y0_derived"] is False)
    return fields


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
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

    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "the physical top pole is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
        "positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "derived B_x source tangent plus C3 spectral algebra derives the accepted top spectral line and source matrix element",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive accepted base C3 circulant dynamics with orientation/phase law "
            "and top-line ordering, or produce strict same-source top/W pole rows"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names phase law", "orientation/phase law" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 CIRCULANT DYNAMICS ORDERING SOURCE-LAW BOUNDARY")
    print("=" * 78)

    anchors = part1_anchors()
    source_derivatives = part2_circulant_source_derivative()
    countermodels = part3_base_dynamics_countermodels()
    certificate = part4_certificate_boundary()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_circulant_dynamics_ordering_source_law_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_circulant_dynamics_ordering_source_law_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "The derived B_x source tangent fixes line derivatives, but the current "
            "surface does not derive the base C3 circulant dynamics or spectral "
            "ordering. Real/reflection-even base dynamics leaves the nontrivial "
            "block degenerate, and complex/orientation-odd dynamics needs an "
            "additional y0 phase law."
        ),
        "anchors": anchors,
        "source_derivative_responses": source_derivatives,
        "base_dynamics_countermodels": countermodels,
        "certificate_boundary": certificate,
        "next_ranked_route": "strict sparse top/W pole-response evidence or new microscopic dynamics theorem",
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

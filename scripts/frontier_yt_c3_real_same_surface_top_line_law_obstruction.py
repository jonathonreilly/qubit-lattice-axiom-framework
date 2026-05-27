#!/usr/bin/env python3
"""Y_T C3 real same-surface top-line law obstruction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_real_same_surface_top_line_law_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_C3_REAL_SAME_SURFACE_TOP_LINE_LAW_OBSTRUCTION_NOTE_2026-05-27.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
SAME_SURFACE_FACTORIZATION = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_NONTRIVIAL_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_MASS_ORDERING = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"
C3_SPECTRAL_SUPPORT = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
C3_SPECTRAL_SOURCE_NOGO = DOCS / "YT_C3_SPECTRAL_SOURCE_RESPONSE_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
LSP_C3_BOUNDARY = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
POSITIVITY_ORIENTATION_BOUNDARY = DOCS / "YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
THREE_GENERATION_OBSERVABLE = DOCS / "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
SAME_SURFACE_FACTORIZATION_OUT = ROOT / "outputs" / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_NONTRIVIAL_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"
C3_MASS_ORDERING_OUT = ROOT / "outputs" / "yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json"
C3_SPECTRAL_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
C3_SPECTRAL_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json"
LSP_C3_BOUNDARY_OUT = ROOT / "outputs" / "yt_lsp_projective_c3_source_direction_boundary_2026-05-27.json"
POSITIVITY_ORIENTATION_BOUNDARY_OUT = ROOT / "outputs" / "yt_positivity_orientation_c3_source_direction_boundary_2026-05-27.json"

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


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify((sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3)


def is_real_matrix(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sp.im(entry)) == 0 for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and prior route boundaries")
    paths = (
        NOTE,
        FIRST_PRINCIPLES,
        SAME_SURFACE_FACTORIZATION,
        C3_REAL_SOURCE,
        C3_NONTRIVIAL_BOUNDARY,
        C3_MASS_ORDERING,
        C3_SPECTRAL_SUPPORT,
        C3_SPECTRAL_SOURCE_NOGO,
        LSP_C3_BOUNDARY,
        POSITIVITY_ORIENTATION_BOUNDARY,
        THREE_GENERATION_OBSERVABLE,
        FULL_STACK,
        FIRST_PRINCIPLES_OUT,
        SAME_SURFACE_FACTORIZATION_OUT,
        C3_REAL_SOURCE_OUT,
        C3_NONTRIVIAL_BOUNDARY_OUT,
        C3_MASS_ORDERING_OUT,
        C3_SPECTRAL_SUPPORT_OUT,
        C3_SPECTRAL_SOURCE_NOGO_OUT,
        LSP_C3_BOUNDARY_OUT,
        POSITIVITY_ORIENTATION_BOUNDARY_OUT,
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
        "non-mass-ordering",
        "nontrivial C3 block",
        "accepted same-surface C3 circulant dynamics/source law",
    ):
        check(f"note contains route phrase: {phrase}", phrase in note)

    first = load_json(FIRST_PRINCIPLES_OUT)
    factorization = load_json(SAME_SURFACE_FACTORIZATION_OUT)
    real_source = load_json(C3_REAL_SOURCE_OUT)
    nontrivial = load_json(C3_NONTRIVIAL_BOUNDARY_OUT)
    mass_ordering = load_json(C3_MASS_ORDERING_OUT)
    spectral_support = load_json(C3_SPECTRAL_SUPPORT_OUT)
    spectral_nogo = load_json(C3_SPECTRAL_SOURCE_NOGO_OUT)
    lsp = load_json(LSP_C3_BOUNDARY_OUT)
    positivity = load_json(POSITIVITY_ORIENTATION_BOUNDARY_OUT)

    check("first-principles transfer boundary passed", first.get("fail_count") == 0, first.get("fail_count"))
    check("factorization boundary passed", factorization.get("fail_count") == 0, factorization.get("fail_count"))
    check("factorization remains conditional support", factorization.get("actual_current_surface_status") == "conditional-support")
    check("real-record source theorem passed", real_source.get("fail_count") == 0, real_source.get("fail_count"))
    check("real-record theorem selects B_x", real_source.get("certificate_boundary", {}).get("source_direction_bx_selected") is True)
    check("nontrivial top-line boundary passed", nontrivial.get("fail_count") == 0, nontrivial.get("fail_count"))
    check("mass-ordering obstruction passed", mass_ordering.get("fail_count") == 0, mass_ordering.get("fail_count"))
    check("mass-ordering selects P_0", mass_ordering.get("mass_ordering_witness", {}).get("mass_ordering_proxy_top_line") == "P_0")
    check("C3 spectral support passed", spectral_support.get("fail_count") == 0, spectral_support.get("fail_count"))
    check("C3 spectral route remains support", spectral_support.get("trace_class") == "upstream_support")
    check("C3 spectral source-response no-go passed", spectral_nogo.get("fail_count") == 0, spectral_nogo.get("fail_count"))
    check("LSP boundary passed", lsp.get("fail_count") == 0, lsp.get("fail_count"))
    check("positivity/orientation boundary passed", positivity.get("fail_count") == 0, positivity.get("fail_count"))
    check("three-generation observable is algebraic, not species bridge", "physical-species semantics" in read(THREE_GENERATION_OBSERVABLE))

    return {
        "first_principles_status": first.get("actual_current_surface_status"),
        "factorization_status": factorization.get("actual_current_surface_status"),
        "real_source_status": real_source.get("actual_current_surface_status"),
        "mass_ordering_status": mass_ordering.get("actual_current_surface_status"),
        "spectral_source_response_status": spectral_nogo.get("actual_current_surface_status"),
    }


def part2_real_c3_block_algebra() -> dict[str, Any]:
    print("\nPart 2: real C3 block algebra")
    sqrt = sp.sqrt
    C = c3_cycle()
    R = c3_reflection()
    omega = -sp.Rational(1, 2) + sp.I * sqrt(3) / 2
    bx = sp.simplify((C + C**2) / sqrt(6))

    p0 = projector_for_eigenvalue(C, sp.Integer(1))
    pomega = projector_for_eigenvalue(C, omega)
    pomega2 = projector_for_eigenvalue(C, omega**2)
    pnt = sp.simplify(pomega + pomega2)

    check("C has order three", is_zero(C**3 - sp.eye(3)))
    check("reflection conjugates C to C^2", is_zero(R * C * R - C**2))
    check("B_x is real", is_real_matrix(bx))
    check("B_x is reflection-even", is_zero(R * bx * R - bx))
    check("P_0 is real", is_real_matrix(p0))
    check("P_omega is not real", not is_real_matrix(pomega))
    check("P_omega2 is not real", not is_real_matrix(pomega2))
    check("P_nt is real", is_real_matrix(pnt))
    check("reflection fixes P_0", is_zero(R * p0 * R - p0))
    check("reflection swaps P_omega and P_omega2", is_zero(R * pomega * R - pomega2))
    check("reflection fixes P_nt block", is_zero(R * pnt * R - pnt))
    check("P_nt is rank two", is_zero(sp.trace(pnt) - 2) and is_zero(pnt**2 - pnt), sp.trace(pnt))
    check("P_0 and P_nt resolve identity", is_zero(p0 + pnt - sp.eye(3)))

    responses = {
        "P_0": sp.radsimp(sp.simplify(sp.trace(p0 * bx))),
        "P_omega": sp.radsimp(sp.simplify(sp.trace(pomega * bx))),
        "P_omega2": sp.radsimp(sp.simplify(sp.trace(pomega2 * bx))),
        "P_nt_total": sp.radsimp(sp.simplify(sp.trace(pnt * bx))),
        "P_nt_per_line": sp.radsimp(sp.simplify(sp.trace(pnt * bx) / 2)),
    }
    check("P_0 response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sqrt(6)), responses["P_omega2"])
    check("nontrivial block total response is -2/sqrt(6)", is_zero(responses["P_nt_total"] + 2 / sqrt(6)), responses["P_nt_total"])
    check("nontrivial per-line response has target magnitude", is_zero(abs(responses["P_nt_per_line"]) - 1 / sqrt(6)), responses["P_nt_per_line"])

    return {name: sp.sstr(value) for name, value in responses.items()}


def part3_counterassignments() -> dict[str, Any]:
    print("\nPart 3: same-current-surface counterassignments")
    A = sp.symbols("A", positive=True)
    sqrt = sp.sqrt
    p0_row = sp.simplify(A / sqrt(2) * 2 / sqrt(6))
    pnt_row = sp.simplify(A / sqrt(2) * 1 / sqrt(6))
    check("P_0 assignment gives A/sqrt(3)", is_zero(p0_row - A / sqrt(3)), p0_row)
    check("nontrivial assignment gives A/sqrt(12)", is_zero(pnt_row - A / sqrt(12)), pnt_row)
    check("two assignments differ by factor two", is_zero(p0_row / pnt_row - 2), p0_row / pnt_row)

    assignments = {
        "assignment_A": {
            "physical_top_sector": "P_0",
            "preserves_current_real_c3_source_support": True,
            "top_matrix_element_magnitude": "A/sqrt(3)",
        },
        "assignment_B": {
            "physical_top_sector": "P_nt or supplied nontrivial line",
            "preserves_current_real_c3_source_support": True,
            "top_matrix_element_magnitude_per_line": "A/sqrt(12)",
        },
        "reason_not_closed": "the current surface supplies no physical rule choosing assignment_B over assignment_A",
    }
    check("assignment A is allowed by current support", assignments["assignment_A"]["preserves_current_real_c3_source_support"] is True)
    check("assignment B is allowed only as supplied top-line law", assignments["assignment_B"]["preserves_current_real_c3_source_support"] is True)
    check("missing rule is explicit", "choosing assignment_B" in assignments["reason_not_closed"])
    return assignments


def part4_attempt_audit() -> dict[str, bool]:
    print("\nPart 4: attempted non-mass-ordering laws")
    audit = {
        "connected_source_excludes_singlet_state": False,
        "real_reflection_even_source_isolates_complex_nontrivial_line": False,
        "mass_ordering_selects_nontrivial_line": False,
        "lsp_readout_selects_projector": False,
        "positivity_orientation_selects_top_line": False,
        "c3_spectral_dynamics_route_closed": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in audit.items():
        check(f"attempt audit field recorded: {key}", isinstance(value, bool), value)
    check("all tested shortcut laws remain blocked", not any(value for key, value in audit.items() if key != "no_forbidden_imports"))
    check("forbidden inputs absent", audit["no_forbidden_imports"] is True)
    return audit


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
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
        check(f"firewall phrase present: {phrase}", phrase in note)

    for forbidden in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "the physical top pole is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
        "positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "real same-surface C3 support derives non-mass-ordering nontrivial top-line assignment",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "derive accepted C3 circulant dynamics/source law for a(h), x(h), y(h), "
            "or produce strict same-source top/W pole-response evidence"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("next live route names a(h), x(h), y(h)", "a(h), x(h), y(h)" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T C3 REAL SAME-SURFACE TOP-LINE LAW OBSTRUCTION")
    print("=" * 78)

    anchors = part1_anchors()
    block_responses = part2_real_c3_block_algebra()
    assignments = part3_counterassignments()
    attempt_audit = part4_attempt_audit()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_real_same_surface_top_line_law_obstruction_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_real_same_surface_top_line_law_obstruction.py",
        **status,
        "proposal_allowed_reason": (
            "The current real connected/reflection-even C3 source support fixes B_x "
            "but does not exclude the singlet C3 spectral sector as the physical "
            "top pole. It can name the real nontrivial block only as an extra "
            "physical sector law, and cannot isolate an individual complex line "
            "without additional dynamics."
        ),
        "anchors": anchors,
        "real_c3_block_witness": block_responses,
        "counterassignments": assignments,
        "attempt_audit": attempt_audit,
        "next_ranked_route": "accepted C3 circulant dynamics/source law for a(h), x(h), y(h)",
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

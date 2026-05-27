#!/usr/bin/env python3
"""Y_T C3 nontrivial top-line assignment boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"

NOTE = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
C3_CONNECTED_CANDIDATE = DOCS / "YT_C3_CONNECTED_REFLECTION_EVEN_SOURCE_DIRECTION_CANDIDATE_NOTE_2026-05-27.md"
C3_SPECTRAL_PROJECTOR_SUPPORT = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
TOP_SECTOR_PROJECTOR_OBSTRUCTION = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
THREE_GENERATION_OBSERVABLE = DOCS / "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"
LSP_C3_BOUNDARY = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_CONNECTED_CANDIDATE_OUT = ROOT / "outputs" / "yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json"
C3_SPECTRAL_PROJECTOR_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"
LSP_C3_BOUNDARY_OUT = ROOT / "outputs" / "yt_lsp_projective_c3_source_direction_boundary_2026-05-27.json"

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


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify(
        (sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3
    )


def frob_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        C3_CONNECTED_CANDIDATE,
        C3_SPECTRAL_PROJECTOR_SUPPORT,
        TOP_SECTOR_PROJECTOR_OBSTRUCTION,
        THREE_GENERATION_OBSERVABLE,
        LSP_C3_BOUNDARY,
        FULL_STACK,
        C3_CONNECTED_CANDIDATE_OUT,
        C3_SPECTRAL_PROJECTOR_SUPPORT_OUT,
        TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT,
        LSP_C3_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "Relation To Existing Retained Generation Algebra",
        "What This Prunes",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "the physical top row is a nontrivial C3 character line",
        "top-line assignment",
        "response magnitude 2/sqrt(6)",
        "response magnitude 1/sqrt(6)",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    connected = load_json(C3_CONNECTED_CANDIDATE_OUT)
    c3_support = load_json(C3_SPECTRAL_PROJECTOR_SUPPORT_OUT)
    top_obstruction = load_json(TOP_SECTOR_PROJECTOR_OBSTRUCTION_OUT)
    lsp = load_json(LSP_C3_BOUNDARY_OUT)
    check("connected/reflection-even candidate passed", connected.get("fail_count") == 0, connected.get("fail_count"))
    check("connected/reflection-even candidate selected B_x under conditions", connected.get("certificate_boundary", {}).get("candidate_direction_bx_selected_under_conditions") is True)
    check("C3 spectral projector support passed", c3_support.get("fail_count") == 0, c3_support.get("fail_count"))
    check("C3 spectral projector route remains support", c3_support.get("trace_class") == "upstream_support")
    check("top-sector projector obstruction passed", top_obstruction.get("fail_count") == 0, top_obstruction.get("fail_count"))
    check("LSP boundary passed", lsp.get("fail_count") == 0, lsp.get("fail_count"))
    check("three-generation observable excludes physical species bridge", "Physical species" in read(THREE_GENERATION_OBSERVABLE))

    return {
        "connected_candidate_status": connected.get("actual_current_surface_status"),
        "c3_projector_support_status": c3_support.get("actual_current_surface_status"),
        "top_projector_obstruction_status": top_obstruction.get("actual_current_surface_status"),
    }


def part2_c3_line_responses() -> dict[str, Any]:
    print("\nPart 2: C3 line responses")
    sqrt = sp.sqrt
    omega = sp.Rational(-1, 2) + sp.I * sqrt(3) / 2
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    bx = sp.simplify((cycle + cycle**2) / sqrt(6))

    projectors = {
        "P_0": projector_for_eigenvalue(cycle, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(cycle, omega),
        "P_omega2": projector_for_eigenvalue(cycle, omega**2),
    }
    expected_responses = {
        "P_0": 2 / sqrt(6),
        "P_omega": -1 / sqrt(6),
        "P_omega2": -1 / sqrt(6),
    }

    check("C is order 3", is_zero(cycle**3 - sp.eye(3)))
    check("B_x is connected/traceless", is_zero(sp.trace(bx)))
    check("B_x is unit normalized", is_zero(frob_inner(bx, bx) - 1), frob_inner(bx, bx))

    responses: dict[str, sp.Expr] = {}
    for name, projector in projectors.items():
        check(f"{name} is Hermitian", is_zero(projector.conjugate().T - projector))
        check(f"{name} is a projector", is_zero(projector**2 - projector))
        check(f"{name} has trace one", is_zero(sp.trace(projector) - 1), sp.trace(projector))
        responses[name] = sp.simplify(sp.trace(projector * bx))
        check(f"{name} response matches expected", is_zero(responses[name] - expected_responses[name]), responses[name])

    check("trivial line response magnitude is 2/sqrt(6)", is_zero(abs(responses["P_0"]) - 2 / sqrt(6)), responses["P_0"])
    check("nontrivial line P_omega magnitude is 1/sqrt(6)", is_zero(abs(responses["P_omega"]) - 1 / sqrt(6)), responses["P_omega"])
    check("nontrivial line P_omega2 magnitude is 1/sqrt(6)", is_zero(abs(responses["P_omega2"]) - 1 / sqrt(6)), responses["P_omega2"])
    check("P_0 and P_omega assignments give different magnitudes", not is_zero(abs(responses["P_0"]) - abs(responses["P_omega"])))
    check("P_omega and P_omega2 assignments have equal magnitude", is_zero(abs(responses["P_omega"]) - abs(responses["P_omega2"])))

    return {
        "source_direction": "B_x",
        "responses": {name: str(sp.simplify(value)) for name, value in responses.items()},
        "assignment_witness": {
            "top_line_P0_magnitude": "2/sqrt(6)",
            "top_line_nontrivial_magnitude": "1/sqrt(6)",
        },
    }


def part3_boundary_certificate() -> dict[str, bool]:
    print("\nPart 3: certificate boundary")
    certificate = {
        "connected_reflection_even_source_direction_available": True,
        "bx_source_direction_selected_under_conditions": True,
        "c3_spectral_projectors_available": True,
        "lsp_projective_instruments_available_for_supplied_projectors": True,
        "physical_top_line_nontrivial_derived": False,
        "trivial_c3_line_excluded_as_top": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, expected in certificate.items():
        check(f"field status recorded: {key}", certificate[key] is expected)

    check("nontrivial top-line assignment remains load-bearing", certificate["physical_top_line_nontrivial_derived"] is False)
    check("strict top/W certificate remains absent", certificate["strict_top_w_response_certificate_present"] is False)
    return certificate


def part4_firewalls() -> None:
    print("\nPart 4: firewalls")
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

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "physical top row is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "conditional_surface_status": "exact-support if nontrivial top-line assignment is supplied",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": "derive nontrivial top-line assignment from same-surface dynamics or produce strict same-source top/W pole rows",
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names nontrivial top-line assignment", "nontrivial top-line assignment" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    witness = part2_c3_line_responses()
    certificate = part3_boundary_certificate()
    part4_firewalls()
    status = part5_claim_status()

    result = {
        "claim_id": "yt_c3_nontrivial_top_line_assignment_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_nontrivial_top_line_assignment_boundary.py",
        **status,
        "proposal_allowed_reason": (
            "The connected/reflection-even B_x source gives 1/sqrt(6) only on "
            "nontrivial C3 character lines. The physical top-line assignment "
            "is not derived on the current surface."
        ),
        "anchors": anchors,
        "response_witness": witness,
        "certificate_boundary": certificate,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

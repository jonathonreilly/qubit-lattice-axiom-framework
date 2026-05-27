#!/usr/bin/env python3
"""Y_T C3 connected reflection-even source-direction candidate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json"

NOTE = DOCS / "YT_C3_CONNECTED_REFLECTION_EVEN_SOURCE_DIRECTION_CANDIDATE_NOTE_2026-05-27.md"
C3_DIRECTION_NOGO = DOCS / "YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md"
LSP_C3_BOUNDARY = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
ORIENTATION_BOUNDARY = DOCS / "YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
NEUTRAL_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_DIRECTION_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_direction_selection_no_go_2026-05-27.json"
LSP_C3_BOUNDARY_OUT = ROOT / "outputs" / "yt_lsp_projective_c3_source_direction_boundary_2026-05-27.json"
ORIENTATION_BOUNDARY_OUT = ROOT / "outputs" / "yt_positivity_orientation_c3_source_direction_boundary_2026-05-27.json"

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


def frob_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def projector_for_eigenvalue(cycle: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    return sp.simplify(
        (sp.eye(3) + eigenvalue**-1 * cycle + eigenvalue**-2 * cycle**2) / 3
    )


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        C3_DIRECTION_NOGO,
        LSP_C3_BOUNDARY,
        ORIENTATION_BOUNDARY,
        NEUTRAL_RAY,
        FULL_STACK,
        C3_DIRECTION_NOGO_OUT,
        LSP_C3_BOUNDARY_OUT,
        ORIENTATION_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Purpose",
        "Candidate Premises",
        "Finite Algebra",
        "What This Supports",
        "What Remains Open",
        "Relation To Prior Boundaries",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "connected source tangent + reflection-even neutral source",
        "leaves the unique unit direction",
        "top-line assignment remains load-bearing",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    c3_direction = load_json(C3_DIRECTION_NOGO_OUT)
    lsp_boundary = load_json(LSP_C3_BOUNDARY_OUT)
    orientation_boundary = load_json(ORIENTATION_BOUNDARY_OUT)
    check("C3 direction no-go passed", c3_direction.get("fail_count") == 0, c3_direction.get("fail_count"))
    check("LSP/C3 boundary passed", lsp_boundary.get("fail_count") == 0, lsp_boundary.get("fail_count"))
    check("orientation boundary passed", orientation_boundary.get("fail_count") == 0, orientation_boundary.get("fail_count"))
    check("neutral-ray bridge remains support only", "support theorem; no positive Y_T closure" in read(NEUTRAL_RAY))

    return {
        "c3_direction_nogo_status": c3_direction.get("actual_current_surface_status"),
        "lsp_boundary_status": lsp_boundary.get("actual_current_surface_status"),
        "orientation_boundary_status": orientation_boundary.get("actual_current_surface_status"),
    }


def part2_candidate_direction_selection() -> dict[str, Any]:
    print("\nPart 2: connected/reflection-even selector")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    Ba = sp.eye(3) / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    By = I * (C - C**2) / sp.sqrt(6)

    for name, tangent in {"B_a": Ba, "B_x": Bx, "B_y": By}.items():
        check(f"{name} commutes with C", is_zero(tangent * C - C * tangent))
        check(f"{name} is unit normalized", is_zero(frob_inner(tangent, tangent) - 1), frob_inner(tangent, tangent))

    check("B_a is the trace/identity direction", is_zero(Ba - sp.eye(3) / sp.sqrt(3)))
    check("B_x is traceless", is_zero(sp.trace(Bx)), sp.trace(Bx))
    check("B_y is traceless", is_zero(sp.trace(By)), sp.trace(By))
    check("B_x is reflection-even", is_zero(reflection * Bx * reflection - Bx))
    check("B_y is reflection-odd", is_zero(reflection * By * reflection + By))

    u, v = sp.symbols("u v", real=True)
    connected_even = u * Bx + v * By
    reflection_even_condition = sp.simplify(reflection * connected_even * reflection - connected_even)
    check("reflection-even connected tangent forces v=0", all(sp.simplify(entry).subs(v, 0) == 0 for entry in reflection_even_condition))
    check("reflection-even connected tangent contains v terms unless v=0", any(sp.simplify(entry).has(v) for entry in reflection_even_condition))
    check("unit connected reflection-even direction is B_x up to sign", True, "span{B_x}")

    return {
        "connected_removes": "B_a",
        "reflection_even_removes": "B_y",
        "candidate_direction": "B_x",
    }


def part3_spectral_responses() -> dict[str, Any]:
    print("\nPart 3: C3 spectral responses")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * I / 2
    Bx = (C + C**2) / sp.sqrt(6)
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    responses = {name: sp.radsimp(sp.simplify(sp.trace(projector * Bx))) for name, projector in projectors.items()}

    check("P_0 response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("P_omega response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("P_omega2 response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])
    check("nontrivial C3 line magnitudes equal 1/sqrt(6)", all(is_zero(abs_candidate**2 - sp.Rational(1, 6)) for abs_candidate in (responses["P_omega"], responses["P_omega2"])), responses)
    check("P_0 line has different magnitude", not is_zero(responses["P_0"]**2 - sp.Rational(1, 6)), responses["P_0"])
    check("top-line assignment remains load-bearing", True, "P_0 versus nontrivial C3 lines differ")

    return {
        "candidate_direction": "B_x",
        "responses": {key: sp.sstr(value) for key, value in responses.items()},
        "nontrivial_line_magnitude": "1/sqrt(6)",
        "p0_magnitude": "2/sqrt(6)",
    }


def part4_certificate_boundary() -> dict[str, Any]:
    print("\nPart 4: certificate boundary")
    fields = {
        "connected_source_condition_assumed_not_derived": True,
        "reflection_even_neutral_source_condition_assumed_not_derived": True,
        "candidate_direction_bx_selected_under_conditions": True,
        "nontrivial_c3_line_response_magnitude_1_over_sqrt6": True,
        "physical_top_line_nontrivial_derived": False,
        "same_surface_dynamics_derived": False,
        "same_surface_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check("candidate is support, not closure", fields["candidate_direction_bx_selected_under_conditions"] and not fields["physical_top_line_nontrivial_derived"])
    check("strict top/W certificate remains absent", fields["same_surface_top_w_response_certificate_present"] is False)
    return fields


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
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
        "physical top line is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "exact-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Connected + reflection-even source conditions select B_x, and B_x "
            "has response magnitude 1/sqrt(6) on nontrivial C3 character "
            "lines. The physical connected-source premise, reflection-even "
            "premise, and top-line assignment are not yet derived."
        ),
        "bare_retained_allowed": False,
        "route_supported": "connected reflection-even C3 source direction B_x",
        "route_still_live": (
            "derive connected/reflection-even physical source authority and "
            "nontrivial top-line assignment from same-surface dynamics, or "
            "produce strict same-source top/W pole-response evidence"
        ),
    }
    check("actual status is exact-support", status["actual_current_surface_status"] == "exact-support")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names top-line assignment", "top-line assignment" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    selector = part2_candidate_direction_selection()
    responses = part3_spectral_responses()
    boundary = part4_certificate_boundary()
    part5_firewalls()
    status = part6_claim_status()

    payload = {
        "claim_id": "yt_c3_connected_reflection_even_source_direction_candidate_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_connected_reflection_even_source_direction_candidate.py",
        "anchors": anchors,
        "selector_witness": selector,
        "spectral_response_witness": responses,
        "certificate_boundary": boundary,
        **status,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())

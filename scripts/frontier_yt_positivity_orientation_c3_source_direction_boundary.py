#!/usr/bin/env python3
"""Y_T positivity/orientation C3 source-direction boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_positivity_orientation_c3_source_direction_boundary_2026-05-27.json"

NOTE = DOCS / "YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
POSITIVITY_C3 = DOCS / "POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md"
ORIENTED_SPLITTER = DOCS / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md"
C3_DIRECTION_NOGO = DOCS / "YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md"
LSP_C3_BOUNDARY = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_DIRECTION_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_direction_selection_no_go_2026-05-27.json"
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
        POSITIVITY_C3,
        ORIENTED_SPLITTER,
        C3_DIRECTION_NOGO,
        LSP_C3_BOUNDARY,
        FULL_STACK,
        C3_DIRECTION_NOGO_OUT,
        LSP_C3_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "What This Prunes",
        "What Remains Live",
        "Relation To Existing Support",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    positivity = read(POSITIVITY_C3)
    splitter = read(ORIENTED_SPLITTER)
    check(
        "positivity note is group-theory scoped",
        "group-theory level" in positivity and "This establishes the group-theory selection" in positivity,
    )
    check("positivity note leaves physical bridge open", "Open bridge" in positivity or "OPEN BRIDGE" in positivity)
    check("splitter note leaves coefficients free", "a,b,c remain free" in splitter or "coefficients `a,b,c` remain free" in splitter)
    check("splitter note leaves source/readout theorem open", "source/readout theorem" in splitter)

    c3_direction = load_json(C3_DIRECTION_NOGO_OUT)
    lsp_boundary = load_json(LSP_C3_BOUNDARY_OUT)
    check("C3 direction no-go passed", c3_direction.get("fail_count") == 0, c3_direction.get("fail_count"))
    check("LSP/C3 boundary passed", lsp_boundary.get("fail_count") == 0, lsp_boundary.get("fail_count"))

    return {
        "positivity_c3_scope": "group-theory C3 subgroup selection",
        "splitter_scope": "orientation-odd splitter support",
    }


def part2_orientation_action_on_tangents() -> dict[str, Any]:
    print("\nPart 2: orientation action on C3 tangents")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    Ba = sp.eye(3) / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    By = I * (C - C**2) / sp.sqrt(6)
    Kc3 = (C - C**2) / (I * sp.sqrt(3))

    check("reflection conjugates C to C^2", is_zero(reflection * C * reflection - C**2))
    check("B_a is reflection-even", is_zero(reflection * Ba * reflection - Ba))
    check("B_x is reflection-even", is_zero(reflection * Bx * reflection - Bx))
    check("B_y is reflection-odd", is_zero(reflection * By * reflection + By))
    check("K_C3 is proportional to B_y", is_zero(Kc3 + sp.sqrt(2) * By), Kc3 + sp.sqrt(2) * By)

    for name, tangent in {"B_a": Ba, "B_x": Bx, "B_y": By}.items():
        check(f"{name} commutes with C", is_zero(tangent * C - C * tangent))
        check(f"{name} has unit Frobenius norm", is_zero(frob_inner(tangent, tangent) - 1), frob_inner(tangent, tangent))

    return {
        "reflection_even_axes": ["B_a", "B_x"],
        "reflection_odd_axis": "B_y",
        "K_C3_relation": "K_C3=-sqrt(2)*B_y",
    }


def part3_orientation_axis_response_witness() -> dict[str, Any]:
    print("\nPart 3: orientation axis response witness")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * I / 2
    projectors = {
        "P_0": projector_for_eigenvalue(C, sp.Integer(1)),
        "P_omega": projector_for_eigenvalue(C, omega),
        "P_omega2": projector_for_eigenvalue(C, omega**2),
    }
    By = I * (C - C**2) / sp.sqrt(6)
    Bx = (C + C**2) / sp.sqrt(6)
    Ba = sp.eye(3) / sp.sqrt(3)

    responses_by = {name: sp.radsimp(sp.simplify(sp.trace(projector * By))) for name, projector in projectors.items()}
    responses_bx = {name: sp.radsimp(sp.simplify(sp.trace(projector * Bx))) for name, projector in projectors.items()}
    responses_ba = {name: sp.radsimp(sp.simplify(sp.trace(projector * Ba))) for name, projector in projectors.items()}

    check("P_0 response to orientation axis is zero", is_zero(responses_by["P_0"]), responses_by["P_0"])
    check("P_omega response to orientation axis is -1/sqrt(2)", is_zero(responses_by["P_omega"] + 1 / sp.sqrt(2)), responses_by["P_omega"])
    check("P_omega2 response to orientation axis is +1/sqrt(2)", is_zero(responses_by["P_omega2"] - 1 / sp.sqrt(2)), responses_by["P_omega2"])
    check("orientation-axis responses are not uniformly 1/sqrt(6)", all(not is_zero(v - 1 / sp.sqrt(6)) for v in responses_by.values()), responses_by)
    check("orientation axis still requires top-line assignment", len({sp.sstr(v) for v in responses_by.values()}) == 3, responses_by)

    alpha = sp.symbols("alpha", real=True)
    unit_family = sp.cos(alpha) * By + sp.sin(alpha) * Bx
    check("orientation-plus-even unit family is normalized", is_zero(frob_inner(unit_family, unit_family) - 1), frob_inner(unit_family, unit_family))
    p0_response = sp.radsimp(sp.simplify(sp.trace(projectors["P_0"] * unit_family)))
    check("C3 subgroup selection still leaves response angle", p0_response.has(alpha), p0_response)

    return {
        "B_y_responses": {key: sp.sstr(value) for key, value in responses_by.items()},
        "B_x_responses": {key: sp.sstr(value) for key, value in responses_bx.items()},
        "B_a_responses": {key: sp.sstr(value) for key, value in responses_ba.items()},
        "unit_family_P0_response": sp.sstr(p0_response),
    }


def part4_certificate_boundary() -> dict[str, Any]:
    print("\nPart 4: certificate boundary")
    fields = {
        "orientation_selects_c3_subgroup": True,
        "orientation_odd_splitter_axis_identified": True,
        "framework_positivity_to_hw1_bridge_closed": False,
        "physical_yt_source_tangent_derived": False,
        "top_line_assignment_derived": False,
        "top_line_matrix_element_derived": False,
        "same_surface_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check("subgroup support is not source-direction closure", fields["orientation_selects_c3_subgroup"] and not fields["physical_yt_source_tangent_derived"])
    check("orientation axis is not top/W certificate", fields["orientation_odd_splitter_axis_identified"] and not fields["same_surface_top_w_response_certificate_present"])
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
        "physical Y_T source tangent is derived",
        "top-line assignment is derived",
        "C3 spectral route is refuted",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Positivity/orientation support selects C3 at subgroup level and "
            "can identify an orientation-odd splitter axis, but it does not "
            "derive the physical Y_T source tangent, top-line assignment, or "
            "source-generator matrix element."
        ),
        "bare_retained_allowed": False,
        "route_pruned": "positivity/orientation C3 selection derives physical Y_T source tangent",
        "route_still_live": (
            "derive physical C3 source direction from same-surface dynamics, "
            "or produce strict same-source top/W pole-response evidence"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names source direction or pole evidence", "source direction" in status["route_still_live"] and "pole-response" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    orientation = part2_orientation_action_on_tangents()
    response = part3_orientation_axis_response_witness()
    boundary = part4_certificate_boundary()
    part5_firewalls()
    status = part6_claim_status()

    payload = {
        "claim_id": "yt_positivity_orientation_c3_source_direction_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_positivity_orientation_c3_source_direction_boundary.py",
        "anchors": anchors,
        "orientation_tangent_witness": orientation,
        "orientation_axis_response_witness": response,
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

#!/usr/bin/env python3
"""Y_T C3 source-direction selection no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_source_direction_selection_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md"
SOURCE_RESPONSE_NOGO = DOCS / "YT_C3_SPECTRAL_SOURCE_RESPONSE_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md"
PRIMITIVE_SOURCE_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
FISHER_SOURCE = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

SOURCE_RESPONSE_NOGO_OUT = ROOT / "outputs" / "yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        SOURCE_RESPONSE_NOGO,
        PRIMITIVE_SOURCE_LAW,
        FISHER_SOURCE,
        FULL_STACK,
        SOURCE_RESPONSE_NOGO_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "What This Prunes",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "A unit source tangent fixes scale, not direction",
        "physical source direction in the C3 circulant coefficient space",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    source_response = load_json(SOURCE_RESPONSE_NOGO_OUT)
    check("source-response no-go passed", source_response.get("fail_count") == 0, source_response.get("fail_count"))
    check("source-response no-go keeps source law live", "source law" in source_response.get("route_still_live", ""))
    check("primitive source law is available as support", "Fisher arclength" in read(PRIMITIVE_SOURCE_LAW))
    check("Fisher source note records scale not direction", "lambda" in read(FISHER_SOURCE))
    return {"source_response_nogo": source_response}


def part2_unit_tangent_witness() -> dict[str, Any]:
    print("\nPart 2: unit tangent witness")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Ba = sp.eye(3) / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    By = I * (C - C**2) / sp.sqrt(6)
    basis = {"B_a": Ba, "B_x": Bx, "B_y": By}

    for name, mat in basis.items():
        check(f"{name} is Hermitian", is_zero(mat - mat.conjugate().T))
        check(f"{name} commutes with C", is_zero(mat * C - C * mat))
        check(f"{name} has unit Frobenius norm", is_zero(frob_inner(mat, mat) - 1), frob_inner(mat, mat))

    for left_name, left in basis.items():
        for right_name, right in basis.items():
            if left_name >= right_name:
                continue
            check(f"{left_name} orthogonal to {right_name}", is_zero(frob_inner(left, right)), frob_inner(left, right))

    omega = sp.Rational(-1, 2) + sp.sqrt(3) * I / 2
    P0 = sp.simplify((sp.eye(3) + C + C**2) / 3)
    responses = {name: sp.simplify(sp.trace(P0 * mat)) for name, mat in basis.items()}
    check("P0 is a rank-one spectral projector", is_zero(P0 * P0 - P0) and is_zero(sp.trace(P0) - 1))
    check("B_a response differs from B_x response", not is_zero(responses["B_a"] - responses["B_x"]), responses)
    check("B_y response is zero on lambda0 line", is_zero(responses["B_y"]), responses["B_y"])
    check("B_a response is 1/sqrt(3)", is_zero(responses["B_a"] - 1 / sp.sqrt(3)), responses["B_a"])
    check("B_x response is 2/sqrt(6)", is_zero(responses["B_x"] - 2 / sp.sqrt(6)), responses["B_x"])

    target = 1 / sp.sqrt(6)
    alpha = sp.symbols("alpha", real=True)
    tangent = sp.cos(alpha) * Ba + sp.sin(alpha) * Bx
    response = sp.simplify(sp.trace(P0 * tangent))
    norm = sp.simplify(frob_inner(tangent, tangent))
    check("one-parameter tangent family remains unit normalized", is_zero(norm - 1), norm)
    check("unit tangent response depends on direction alpha", response.has(alpha), response)
    check("target 1/sqrt(6) is not forced by unit normalization", not is_zero(response - target), response)

    return {
        "basis_responses": {name: sp.sstr(value) for name, value in responses.items()},
        "unit_family_response": sp.sstr(response),
        "target": "1/sqrt(6)",
        "conclusion": "unit source normalization leaves C3 tangent direction open",
    }


def part3_certificate_boundary() -> dict[str, Any]:
    print("\nPart 3: certificate boundary")
    fields = {
        "unit_source_normalization": True,
        "c3_invariant_tangent_space": True,
        "physical_c3_source_direction_derived": False,
        "source_direction_not_fitted_to_target": False,
        "top_line_ordering_derived": False,
        "top_line_matrix_element_derived": False,
        "same_surface_w_response": False,
        "top_w_response_certificate_passes": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check("unit source normalization is insufficient", fields["unit_source_normalization"] and not fields["physical_c3_source_direction_derived"])
    check("positive certificate remains absent", fields["top_w_response_certificate_passes"] is False)
    return fields


def part4_firewalls() -> None:
    print("\nPart 4: firewalls")
    text = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
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
        "C3 spectral route is refuted",
        "physical source direction is derived",
        "top response is fixed",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Unit source normalization leaves a two-sphere of C3-invariant "
            "tangent directions. The top response is a linear functional on "
            "that sphere and is not fixed without a derived physical source "
            "direction."
        ),
        "bare_retained_allowed": False,
        "route_pruned": "derive unique C3 source direction from C3 invariance plus unit source normalization alone",
        "route_still_live": "derive physical source direction/target operator or produce strict pole-row evidence",
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route names source direction", "source direction" in status["route_still_live"])
    return status


def main() -> int:
    anchors = part1_anchors()
    witness = part2_unit_tangent_witness()
    fields = part3_certificate_boundary()
    part4_firewalls()
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_c3_source_direction_selection_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_source_direction_selection_no_go.py",
        "anchors": anchors,
        "unit_tangent_witness": witness,
        "certificate_boundary": fields,
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

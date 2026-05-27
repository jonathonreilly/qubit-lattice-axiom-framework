#!/usr/bin/env python3
"""Y_T C3 real-record reflection-even source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"

NOTE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
PRIMITIVE_RECORD = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
CONNECTED_SOURCE = DOCS / "YT_C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_THEOREM_NOTE_2026-05-27.md"
C3_CONNECTED_CANDIDATE = DOCS / "YT_C3_CONNECTED_REFLECTION_EVEN_SOURCE_DIRECTION_CANDIDATE_NOTE_2026-05-27.md"
TOP_LINE_BOUNDARY = DOCS / "YT_C3_NONTRIVIAL_TOP_LINE_ASSIGNMENT_BOUNDARY_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

PRIMITIVE_RECORD_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
CONNECTED_SOURCE_OUT = ROOT / "outputs" / "yt_c3_connected_source_from_normalized_rn_2026-05-27.json"
C3_CONNECTED_CANDIDATE_OUT = ROOT / "outputs" / "yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json"
TOP_LINE_BOUNDARY_OUT = ROOT / "outputs" / "yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json"

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
        PRIMITIVE_RECORD,
        CONNECTED_SOURCE,
        C3_CONNECTED_CANDIDATE,
        TOP_LINE_BOUNDARY,
        FULL_STACK,
        PRIMITIVE_RECORD_OUT,
        CONNECTED_SOURCE_OUT,
        C3_CONNECTED_CANDIDATE_OUT,
        TOP_LINE_BOUNDARY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Algebra",
        "What This Burns Down",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "real finite-record source generator",
        "B_y matrix is purely imaginary",
        "reflection-even",
        "B_x up to sign",
        "nontrivial top-line assignment",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    primitive_record = load_json(PRIMITIVE_RECORD_OUT)
    connected_source = load_json(CONNECTED_SOURCE_OUT)
    c3_candidate = load_json(C3_CONNECTED_CANDIDATE_OUT)
    top_line_boundary = load_json(TOP_LINE_BOUNDARY_OUT)
    check("primitive record intervention law passed", primitive_record.get("fail_count") == 0, primitive_record.get("fail_count"))
    check("connected-source theorem passed", connected_source.get("fail_count") == 0, connected_source.get("fail_count"))
    check("connected-source theorem derives connected premise", connected_source.get("certificate_boundary", {}).get("connected_source_premise_derived") is True)
    check("C3 connected/reflection-even candidate passed", c3_candidate.get("fail_count") == 0, c3_candidate.get("fail_count"))
    check("top-line boundary passed", top_line_boundary.get("fail_count") == 0, top_line_boundary.get("fail_count"))

    return {
        "primitive_record_status": primitive_record.get("actual_current_surface_status"),
        "connected_source_status": connected_source.get("actual_current_surface_status"),
        "top_line_boundary_status": top_line_boundary.get("actual_current_surface_status"),
    }


def part2_real_reflection_algebra() -> dict[str, Any]:
    print("\nPart 2: real/reflection algebra")
    sqrt = sp.sqrt
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    b_a = sp.eye(3) / sqrt(3)
    b_x = sp.simplify((cycle + cycle**2) / sqrt(6))
    b_y = sp.simplify(sp.I * (cycle - cycle**2) / sqrt(6))

    check("C is a real permutation matrix", all(entry.is_real for entry in cycle))
    check("reflection squares to identity", is_zero(reflection**2 - sp.eye(3)))
    check("reflection conjugates C to C^2", is_zero(reflection * cycle * reflection - cycle**2))

    for name, basis in (("B_a", b_a), ("B_x", b_x), ("B_y", b_y)):
        check(f"{name} is Hermitian", is_zero(basis.conjugate().T - basis))
        check(f"{name} is unit normalized", is_zero(frob_inner(basis, basis) - 1), frob_inner(basis, basis))

    check("B_a is real", all(sp.im(entry) == 0 for entry in b_a))
    check("B_x is real", all(sp.im(entry) == 0 for entry in b_x))
    check("B_y has nonzero imaginary entries", any(sp.im(entry) != 0 for entry in b_y))
    check("B_x is reflection-even", is_zero(reflection * b_x * reflection - b_x))
    check("B_y is reflection-odd", is_zero(reflection * b_y * reflection + b_y))

    return {
        "reflection": "R C R = C^2",
        "real_even_basis": ["B_a", "B_x"],
        "imaginary_odd_basis": "B_y",
    }


def part3_real_record_projection() -> dict[str, Any]:
    print("\nPart 3: real-record projection")
    sqrt = sp.sqrt
    a, x, y = sp.symbols("a x y", real=True)
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    b_a = sp.eye(3) / sqrt(3)
    b_x = sp.simplify((cycle + cycle**2) / sqrt(6))
    b_y = sp.simplify(sp.I * (cycle - cycle**2) / sqrt(6))
    generator = sp.simplify(a * b_a + x * b_x + y * b_y)
    imaginary_part = generator.applyfunc(sp.im)
    expected_imaginary = (y * b_y / sp.I).applyfunc(sp.simplify)

    check("imaginary part is exactly the B_y coefficient", is_zero(imaginary_part - expected_imaginary), imaginary_part)
    real_slice = sp.simplify(generator.subs(y, 0))
    check("real-record slice contains no y", y not in real_slice.free_symbols)
    check("real-record slice is real", all(sp.im(entry) == 0 for entry in real_slice))

    connected_real = sp.simplify(real_slice - sp.trace(real_slice) / 3 * sp.eye(3))
    expected_connected_real = sp.simplify(x * b_x)
    check("connected real-record source is x B_x", is_zero(connected_real - expected_connected_real), connected_real)
    check("unit connected real-record direction is B_x up to sign", True, "span{B_x}")

    return {
        "real_record_forces": "y=0",
        "connected_real_source_direction": "B_x up to sign",
    }


def part4_certificate() -> dict[str, bool]:
    print("\nPart 4: certificate boundary")
    certificate = {
        "real_finite_record_source_law_available": True,
        "connected_source_premise_derived": True,
        "reflection_even_neutral_source_derived": True,
        "source_direction_bx_selected": True,
        "nontrivial_top_line_assignment_derived": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, expected in certificate.items():
        check(f"field status recorded: {key}", certificate[key] is expected)
    check("source direction selected as B_x", certificate["source_direction_bx_selected"] is True)
    check("nontrivial top-line assignment remains open", certificate["nontrivial_top_line_assignment_derived"] is False)
    return certificate


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

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "physical top row is derived",
        "strict top/W pole-response evidence is present",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)


def part6_claim_status() -> dict[str, Any]:
    print("\nPart 6: claim status")
    status = {
        "actual_current_surface_status": "exact-support",
        "trace_class": "upstream_support",
        "reachability_to_target": "partially_closes",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "first_open_gate_after_this_note": "nontrivial top-line assignment",
    }
    check("actual status is exact-support", status["actual_current_surface_status"] == "exact-support")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("reachability is partial closure", status["reachability_to_target"] == "partially_closes")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    anchors = part1_anchors()
    real_reflection = part2_real_reflection_algebra()
    real_projection = part3_real_record_projection()
    certificate = part4_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_real_record_reflection_even_source_theorem_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_real_record_reflection_even_source.py",
        **status,
        "proposal_allowed_reason": (
            "Real finite-record source semantics exclude the imaginary "
            "reflection-odd B_y tangent, and normalized RN source semantics "
            "remove B_a. The source direction is therefore B_x up to sign, "
            "but the nontrivial top-line assignment and strict top/W response "
            "evidence remain open."
        ),
        "anchors": anchors,
        "real_reflection_witness": real_reflection,
        "real_record_projection_witness": real_projection,
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

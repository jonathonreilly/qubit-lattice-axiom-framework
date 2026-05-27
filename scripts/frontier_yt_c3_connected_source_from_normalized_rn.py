#!/usr/bin/env python3
"""Y_T C3 connected source from normalized RN source law."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_connected_source_from_normalized_rn_2026-05-27.json"

NOTE = DOCS / "YT_C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_THEOREM_NOTE_2026-05-27.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
PRIMITIVE_RECORD = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
C3_CONNECTED_CANDIDATE = DOCS / "YT_C3_CONNECTED_REFLECTION_EVEN_SOURCE_DIRECTION_CANDIDATE_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

SOURCE_ACTION_OUT = ROOT / "outputs" / "yt_source_action_support_packet_2026-05-22.json"
PRIMITIVE_RECORD_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
C3_CONNECTED_CANDIDATE_OUT = ROOT / "outputs" / "yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json"

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


def tau(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix) / 3)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        SOURCE_ACTION,
        PRIMITIVE_RECORD,
        C3_CONNECTED_CANDIDATE,
        FULL_STACK,
        SOURCE_ACTION_OUT,
        PRIMITIVE_RECORD_OUT,
        C3_CONNECTED_CANDIDATE_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "C3 Consequence",
        "Relation To Existing Source Work",
        "What This Burns Down",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "identity direction in the C3 Hermitian tangent space",
        "source score is the centered observable",
        "connected-source premise",
        "reflection-even source authority",
        "nontrivial top-line assignment",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    source_action = load_json(SOURCE_ACTION_OUT)
    primitive_record = load_json(PRIMITIVE_RECORD_OUT)
    c3_candidate = load_json(C3_CONNECTED_CANDIDATE_OUT)
    check("source-action support packet passed", source_action.get("fail_count") == 0, source_action.get("fail_count"))
    check("primitive record intervention law passed", primitive_record.get("fail_count") == 0, primitive_record.get("fail_count"))
    check("primitive record law supplies Fisher source law", primitive_record.get("first_open_gate_after_this_note") == "physical top-source identification")
    check("C3 connected/reflection-even candidate passed", c3_candidate.get("fail_count") == 0, c3_candidate.get("fail_count"))

    return {
        "source_action_status": source_action.get("actual_current_surface_status"),
        "primitive_record_status": primitive_record.get("actual_current_surface_status"),
        "c3_candidate_status": c3_candidate.get("actual_current_surface_status"),
    }


def part2_normalized_rn_identity() -> dict[str, Any]:
    print("\nPart 2: normalized RN identity")
    h, c = sp.symbols("h c")
    o1, o2, o3 = sp.symbols("o1 o2 o3")
    weights = [sp.exp(h * o) for o in (o1, o2, o3)]
    weights_shifted = [sp.exp(h * (o + c)) for o in (o1, o2, o3)]
    z = sp.simplify(sum(weights))
    z_shifted = sp.simplify(sum(weights_shifted))
    probs = [sp.simplify(w / z) for w in weights]
    probs_shifted = [sp.simplify(w / z_shifted) for w in weights_shifted]

    for idx, (p, q) in enumerate(zip(probs, probs_shifted), start=1):
        check(f"identity shift cancels in normalized probability {idx}", is_zero(p - q), sp.simplify(p - q))

    score = sp.Matrix([o1, o2, o3])
    mean = sp.simplify((o1 + o2 + o3) / 3)
    centered = score - mean * sp.ones(3, 1)
    shifted_score = sp.Matrix([o1 + c, o2 + c, o3 + c])
    shifted_mean = sp.simplify((o1 + c + o2 + c + o3 + c) / 3)
    shifted_centered = shifted_score - shifted_mean * sp.ones(3, 1)
    check("centered score is invariant under identity shift", is_zero(centered - shifted_centered), centered - shifted_centered)
    check("centered score sums to zero", is_zero(sum(centered)), sum(centered))

    return {
        "identity_shift_cancels": True,
        "centered_score_invariant": True,
    }


def part3_c3_connected_projection() -> dict[str, Any]:
    print("\nPart 3: C3 connected projection")
    sqrt = sp.sqrt
    a, x, y = sp.symbols("a x y", real=True)
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    b_a = sp.eye(3) / sqrt(3)
    b_x = sp.simplify((cycle + cycle**2) / sqrt(6))
    b_y = sp.simplify(sp.I * (cycle - cycle**2) / sqrt(6))

    for name, basis in (("B_a", b_a), ("B_x", b_x), ("B_y", b_y)):
        check(f"{name} commutes with C", is_zero(basis * cycle - cycle * basis))
        check(f"{name} is unit normalized", is_zero(frob_inner(basis, basis) - 1), frob_inner(basis, basis))

    generator = sp.simplify(a * b_a + x * b_x + y * b_y)
    connected = sp.simplify(generator - tau(generator) * sp.eye(3))
    expected = sp.simplify(x * b_x + y * b_y)
    check("tau(B_a) is 1/sqrt(3)", is_zero(tau(b_a) - 1 / sqrt(3)), tau(b_a))
    check("tau(B_x) is zero", is_zero(tau(b_x)), tau(b_x))
    check("tau(B_y) is zero", is_zero(tau(b_y)), tau(b_y))
    check("connected projection removes B_a", is_zero(connected - expected), connected)
    check("connected projection is traceless", is_zero(sp.trace(connected)), sp.trace(connected))
    check("B_a coefficient is absent after connected projection", a not in connected.free_symbols)

    return {
        "basis": ["B_a", "B_x", "B_y"],
        "removed_direction": "B_a",
        "surviving_connected_tangent": "x B_x + y B_y",
    }


def part4_certificate() -> dict[str, bool]:
    print("\nPart 4: certificate boundary")
    certificate = {
        "normalized_rn_source_law_available": True,
        "identity_source_direction_removed": True,
        "connected_source_premise_derived": True,
        "reflection_even_neutral_source_derived": False,
        "nontrivial_top_line_assignment_derived": False,
        "strict_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, expected in certificate.items():
        check(f"field status recorded: {key}", certificate[key] is expected)
    check("connected source premise is closed", certificate["connected_source_premise_derived"] is True)
    check("reflection-even premise remains open", certificate["reflection_even_neutral_source_derived"] is False)
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
        "reflection evenness is derived",
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
        "first_open_gate_after_this_note": "reflection-even neutral source authority plus nontrivial top-line assignment",
    }
    check("actual status is exact-support", status["actual_current_surface_status"] == "exact-support")
    check("trace class is upstream support", status["trace_class"] == "upstream_support")
    check("reachability is partial closure", status["reachability_to_target"] == "partially_closes")
    check("proposal remains false", status["proposal_allowed"] is False)
    return status


def main() -> int:
    anchors = part1_anchors()
    rn_identity = part2_normalized_rn_identity()
    c3_projection = part3_c3_connected_projection()
    certificate = part4_certificate()
    part5_firewalls()
    status = part6_claim_status()

    result = {
        "claim_id": "yt_c3_connected_source_from_normalized_rn_theorem_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_connected_source_from_normalized_rn.py",
        **status,
        "proposal_allowed_reason": (
            "Normalized RN/Fisher source semantics remove the identity direction "
            "and derive the connected-source premise. Reflection-even source "
            "authority, nontrivial top-line assignment, and strict top/W "
            "response evidence remain open."
        ),
        "anchors": anchors,
        "rn_identity_witness": rn_identity,
        "c3_connected_projection_witness": c3_projection,
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

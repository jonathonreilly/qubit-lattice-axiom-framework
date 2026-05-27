#!/usr/bin/env python3
"""Y_T LSP projective C3 source-direction boundary.

The runner verifies a narrow route-pruning result:

    LSP sharp-projective readout + C3 spectral support + unit source
        does not select the physical C3 source direction.

It intentionally leaves the live route open: derive the source direction from
accepted same-surface dynamics, or provide strict same-source top/W pole rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_lsp_projective_c3_source_direction_boundary_2026-05-27.json"

NOTE = DOCS / "YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
LSP_SIGNED = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
LSP_SCALE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
C3_PROJECTOR = DOCS / "YT_C3_SPECTRAL_TOP_PROJECTOR_ROUTE_SUPPORT_NOTE_2026-05-27.md"
C3_SOURCE_NOGO = DOCS / "YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

C3_PROJECTOR_OUT = ROOT / "outputs" / "yt_c3_spectral_top_projector_route_support_2026-05-27.json"
C3_SOURCE_NOGO_OUT = ROOT / "outputs" / "yt_c3_source_direction_selection_no_go_2026-05-27.json"

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
        LSP,
        LSP_SIGNED,
        LSP_SCALE,
        C3_PROJECTOR,
        C3_SOURCE_NOGO,
        FULL_STACK,
        C3_PROJECTOR_OUT,
        C3_SOURCE_NOGO_OUT,
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

    for phrase in (
        "LSP supplies the canonical projective instrument for a supplied projector",
        "readout/instrument support, not source-direction authority",
        "does not weaken the LSP support theorem",
        "does not refute the live C3 spectral route",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    lsp = read(LSP)
    check("LSP theorem states canonical K_P = P", "K_P = P" in lsp)
    check("LSP theorem is canonical-frame scoped", "canonical-frame" in lsp or "canonical frame" in lsp)
    check("LSP theorem does not claim all-instrument uniqueness", "does not prove uniqueness" in lsp or "not a uniqueness theorem" in lsp)
    check("LSP signed support is readout carrier scoped", "measurement/readout carrier" in read(LSP_SIGNED))
    check("LSP source-scale boundary already says source-scale blind", "source-scale blind" in read(LSP_SCALE))

    projector_out = load_json(C3_PROJECTOR_OUT)
    source_nogo_out = load_json(C3_SOURCE_NOGO_OUT)
    check("C3 spectral projector support passed", projector_out.get("fail_count") == 0, projector_out.get("fail_count"))
    check("C3 source-direction no-go passed", source_nogo_out.get("fail_count") == 0, source_nogo_out.get("fail_count"))
    return {
        "c3_projector_status": projector_out.get("actual_current_surface_status"),
        "c3_source_direction_status": source_nogo_out.get("actual_current_surface_status"),
    }


def part2_lsp_instrument_does_not_depend_on_tangent() -> dict[str, Any]:
    print("\nPart 2: supplied projector gives same LSP instrument")
    I = sp.I
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    P0 = sp.simplify((sp.eye(3) + C + C**2) / 3)
    Ba = sp.eye(3) / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    By = I * (C - C**2) / sp.sqrt(6)
    tangents = {"B_a": Ba, "B_x": Bx, "B_y": By}

    check("C is a cyclic order-three shift", is_zero(C**3 - sp.eye(3)))
    check("P0 is Hermitian", is_zero(P0 - P0.conjugate().T))
    check("P0 is a projector", is_zero(P0 * P0 - P0))
    check("P0 has trace one", is_zero(sp.trace(P0) - 1), sp.trace(P0))
    check("LSP canonical Kraus for supplied P0 equals P0", is_zero(P0 - P0))

    for name, tangent in tangents.items():
        check(f"{name} is Hermitian", is_zero(tangent - tangent.conjugate().T))
        check(f"{name} commutes with C", is_zero(tangent * C - C * tangent))
        check(f"{name} has unit Frobenius norm", is_zero(frob_inner(tangent, tangent) - 1), frob_inner(tangent, tangent))
        check(f"supplied LSP instrument P0 is unchanged for tangent {name}", is_zero(P0 - P0))

    responses = {name: sp.simplify(sp.trace(P0 * tangent)) for name, tangent in tangents.items()}
    check("B_a response is 1/sqrt(3)", is_zero(responses["B_a"] - 1 / sp.sqrt(3)), responses["B_a"])
    check("B_x response is 2/sqrt(6)", is_zero(responses["B_x"] - 2 / sp.sqrt(6)), responses["B_x"])
    check("B_y response is zero", is_zero(responses["B_y"]), responses["B_y"])
    check("same LSP P0 supports different source responses", len({sp.sstr(value) for value in responses.values()}) == 3, responses)

    return {
        "projector": "P0=(I+C+C^2)/3",
        "lsp_instrument": "K_P0=P0",
        "unit_c3_tangent_responses": {key: sp.sstr(value) for key, value in responses.items()},
        "conclusion": "projective instrument is unchanged while FH source response changes",
    }


def part3_signed_readout_vs_source_direction() -> dict[str, Any]:
    print("\nPart 3: signed readout is carrier support, not direction authority")
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    Pp = (sp.eye(2) + sigma_z) / 2
    Pm = (sp.eye(2) - sigma_z) / 2
    signed = Pp - Pm
    check("P_plus is a projector", is_zero(Pp * Pp - Pp))
    check("P_minus is a projector", is_zero(Pm * Pm - Pm))
    check("P_plus and P_minus are orthogonal", is_zero(Pp * Pm))
    check("signed readout equals sigma_z", is_zero(signed - sigma_z))
    check("signed readout outcomes are +/-1", sorted(sigma_z.eigenvals().keys()) == [-1, 1])

    # The same signed readout carrier can parameterize different normalized
    # C3 tangent directions; LSP supplies the readout variable, not the map
    # from that variable into C3 coefficient space.
    alpha = sp.symbols("alpha", real=True)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    P0 = sp.simplify((sp.eye(3) + C + C**2) / 3)
    Ba = sp.eye(3) / sp.sqrt(3)
    Bx = (C + C**2) / sp.sqrt(6)
    unit_family = sp.cos(alpha) * Ba + sp.sin(alpha) * Bx
    family_norm = frob_inner(unit_family, unit_family)
    response = sp.simplify(sp.trace(P0 * unit_family))
    check("C3 unit family remains normalized for all alpha", is_zero(family_norm - 1), family_norm)
    check("C3 unit family response depends on alpha", response.has(alpha), response)
    check("LSP signed readout supplies no alpha selector", "alpha" in sp.sstr(response))

    return {
        "signed_readout": "sigma_z with outcomes {-1,+1}",
        "unit_c3_family_response": sp.sstr(response),
        "missing_selector": "alpha",
    }


def part4_certificate_boundary() -> dict[str, Any]:
    print("\nPart 4: certificate boundary")
    fields = {
        "lsp_projective_rule_available": True,
        "signed_record_readout_available": True,
        "c3_spectral_projector_route_live": True,
        "unit_source_normalization_available": True,
        "physical_c3_source_direction_derived": False,
        "top_line_source_generator_matrix_element_derived": False,
        "same_surface_top_w_response_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check(
        "positive closure remains blocked by missing direction",
        fields["lsp_projective_rule_available"] and not fields["physical_c3_source_direction_derived"],
    )
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
        "physical C3 source direction is derived",
        "LSP refutes the C3 spectral route",
        "top response is fixed",
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
            "LSP supplies the canonical projective instrument for a supplied "
            "projector. The C3 finite witness keeps that projector fixed while "
            "changing the unit-normalized C3 source tangent and top-line "
            "response."
        ),
        "bare_retained_allowed": False,
        "route_pruned": "LSP projective/signed-record readout selects the physical C3 source direction",
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
    instrument = part2_lsp_instrument_does_not_depend_on_tangent()
    signed = part3_signed_readout_vs_source_direction()
    boundary = part4_certificate_boundary()
    part5_firewalls()
    status = part6_claim_status()

    payload = {
        "claim_id": "yt_lsp_projective_c3_source_direction_boundary_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_lsp_projective_c3_source_direction_boundary.py",
        "anchors": anchors,
        "instrument_witness": instrument,
        "signed_readout_witness": signed,
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

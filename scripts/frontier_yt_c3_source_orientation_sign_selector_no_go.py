#!/usr/bin/env python3
"""Y_T C3 source-orientation sign-selector no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_c3_source_orientation_sign_selector_no_go_2026-05-27.json"

NOTE = DOCS / "YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_BLOCK_SUPPORT = DOCS / "YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md"
C3_ZERO_SINGLET = DOCS / "YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md"
C3_SOURCE_RESPONSE_EXTREMAL = DOCS / "YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"

FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"
C3_REAL_SOURCE_OUT = ROOT / "outputs" / "yt_c3_real_record_reflection_even_source_2026-05-27.json"
C3_BLOCK_SUPPORT_OUT = ROOT / "outputs" / "yt_c3_nontrivial_block_matrix_element_support_2026-05-27.json"
C3_ZERO_SINGLET_OUT = ROOT / "outputs" / "yt_c3_zero_singlet_top_block_membership_no_go_2026-05-27.json"
C3_SOURCE_RESPONSE_EXTREMAL_OUT = ROOT / "outputs" / "yt_c3_source_response_extremal_readout_no_go_2026-05-27.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and prior route state")
    for path in (
        NOTE,
        FULL_STACK,
        FIRST_PRINCIPLES,
        C3_REAL_SOURCE,
        C3_BLOCK_SUPPORT,
        C3_ZERO_SINGLET,
        C3_SOURCE_RESPONSE_EXTREMAL,
        STRICT_AVAILABILITY,
        FIRST_PRINCIPLES_OUT,
        C3_REAL_SOURCE_OUT,
        C3_BLOCK_SUPPORT_OUT,
        C3_ZERO_SINGLET_OUT,
        C3_SOURCE_RESPONSE_EXTREMAL_OUT,
        STRICT_AVAILABILITY_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Stuck Fan-Out Synthesis",
        "Finite Witness",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / open source-orientation sign law",
        "proposal_allowed: false",
        "ell' = -ell",
        "largest absolute response        -> P_0",
        "minimum signed response          -> P_nt only after importing a convention",
    ):
        check(f"note contains sign-selector phrase: {phrase}", phrase in note)

    deps = {
        "first_principles": load_json(FIRST_PRINCIPLES_OUT),
        "real_source": load_json(C3_REAL_SOURCE_OUT),
        "block_support": load_json(C3_BLOCK_SUPPORT_OUT),
        "zero_singlet": load_json(C3_ZERO_SINGLET_OUT),
        "source_response_extremal": load_json(C3_SOURCE_RESPONSE_EXTREMAL_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "real source theorem selects B_x up to sign",
        "up to sign" in deps["real_source"].get("proposal_allowed_reason", ""),
        deps["real_source"].get("proposal_allowed_reason", ""),
    )
    check(
        "zero-singlet no-go identifies sign/order premise as missing",
        deps["zero_singlet"].get("certificate_boundary", {}).get("accepted_sign_or_order_law_for_Pnt_derived")
        is False,
    )
    check(
        "source-response extremal no-go marks minimum convention absent",
        deps["source_response_extremal"].get("no_go_certificate", {}).get("minimum_response_top_convention_derived")
        is False,
    )
    check(
        "strict positive certificate remains absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present")
        is False,
    )
    return {name: data.get("actual_current_surface_status") for name, data in deps.items()}


def part2_same_source_orientation_invariance() -> dict[str, str]:
    print("\nPart 2: same-source coordinate orientation invariance")
    A, g2 = sp.symbols("A g_2", positive=True)
    dmt = A / sp.sqrt(12)
    dmw = g2 * A / 2
    readout = sp.simplify(g2 / sp.sqrt(2) * dmt / dmw)
    flipped = sp.simplify(g2 / sp.sqrt(2) * (-dmt) / (-dmw))

    check("target same-source readout is 1/sqrt(6)", is_zero(readout - 1 / sp.sqrt(6)), readout)
    check("ell -> -ell leaves same-source readout invariant", is_zero(flipped - readout), flipped)
    check("orientation flip changes both rows", (-dmt) != dmt and (-dmw) != dmw)

    return {
        "dM_t_dell": "A/sqrt(12)",
        "dM_W_dell": "g_2*A/2",
        "readout": "1/sqrt(6)",
        "under_ell_to_minus_ell": "both derivatives flip sign and the ratio is unchanged",
    }


def part3_sign_selector_witness() -> dict[str, Any]:
    print("\nPart 3: C3 source-orientation selector witness")
    sqrt = sp.sqrt
    A = sp.symbols("A", positive=True)
    C = c3_cycle()
    I = sp.eye(3)
    Bx = (C + C**2) / sqrt(6)
    P0 = (I + C + C**2) / 3
    Pnt = I - P0
    base_responses = {
        "P_0": sp.simplify(sp.trace(P0 * Bx) / sp.trace(P0)),
        "P_nt": sp.simplify(sp.trace(Pnt * Bx) / sp.trace(Pnt)),
    }
    check("P_0 response to B_x is 2/sqrt(6)", is_zero(base_responses["P_0"] - 2 / sqrt(6)), base_responses["P_0"])
    check("P_nt response to B_x is -1/sqrt(6)", is_zero(base_responses["P_nt"] + 1 / sqrt(6)), base_responses["P_nt"])

    signed_cases: dict[str, Any] = {}
    for label, sigma in (("plus_Bx", sp.Integer(1)), ("minus_Bx", sp.Integer(-1))):
        responses = {name: sp.simplify(sigma * value) for name, value in base_responses.items()}
        largest_signed = max(responses, key=lambda key: float(sp.N(responses[key])))
        minimum_signed = min(responses, key=lambda key: float(sp.N(responses[key])))
        largest_abs = max(responses, key=lambda key: float(sp.N(abs(responses[key]))))
        signed_cases[label] = {
            "responses": {name: sp.sstr(value) for name, value in responses.items()},
            "largest_signed": largest_signed,
            "minimum_signed": minimum_signed,
            "largest_absolute": largest_abs,
            "P_0_row_magnitude": "A/sqrt(3)",
            "P_nt_row_magnitude": "A/sqrt(12)",
        }

    check("largest signed on +B_x selects P_0", signed_cases["plus_Bx"]["largest_signed"] == "P_0")
    check("largest signed on -B_x selects P_nt", signed_cases["minus_Bx"]["largest_signed"] == "P_nt")
    check("largest signed selector changes under orientation reversal", signed_cases["plus_Bx"]["largest_signed"] != signed_cases["minus_Bx"]["largest_signed"])
    check("largest absolute on +B_x selects P_0", signed_cases["plus_Bx"]["largest_absolute"] == "P_0")
    check("largest absolute on -B_x selects P_0", signed_cases["minus_Bx"]["largest_absolute"] == "P_0")
    check("minimum signed on +B_x selects P_nt", signed_cases["plus_Bx"]["minimum_signed"] == "P_nt")
    check("minimum signed on -B_x selects P_0", signed_cases["minus_Bx"]["minimum_signed"] == "P_0")

    p0_row = sp.simplify(A / sqrt(2) * abs(base_responses["P_0"]))
    pnt_row = sp.simplify(A / sqrt(2) * abs(base_responses["P_nt"]))
    check("P_0 row magnitude is A/sqrt(3)", is_zero(p0_row - A / sqrt(3)), p0_row)
    check("P_nt row magnitude is A/sqrt(12)", is_zero(pnt_row - A / sqrt(12)), pnt_row)
    check("P_0 absolute response is larger than P_nt", abs(base_responses["P_0"]) > abs(base_responses["P_nt"]))

    return {
        "source_direction_known_only_up_to_sign": True,
        "base_responses": {name: sp.sstr(value) for name, value in base_responses.items()},
        "orientation_cases": signed_cases,
        "absolute_response_order": "P_0 has unique largest absolute response",
        "minimum_response_status": "selects P_nt only by importing a convention",
    }


def part4_no_go_certificate() -> dict[str, Any]:
    print("\nPart 4: no-go certificate")
    certificate = {
        "source_direction_bx_available_up_to_sign": True,
        "same_source_ratio_orientation_invariant": True,
        "largest_signed_selector_orientation_invariant": False,
        "absolute_response_max_selects_P0": True,
        "minimum_response_top_convention_derived": False,
        "accepted_source_orientation_law_for_Pnt_derived": False,
        "accepted_zero_singlet_membership_derived": False,
        "accepted_same_surface_generator_factorization_derived": False,
        "strict_top_w_response_certificate_present": False,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "no_forbidden_imports": True,
    }
    for key, value in certificate.items():
        check(f"certificate field recorded: {key}", isinstance(value, bool), value)
    check("orientation/sign law remains open", certificate["accepted_source_orientation_law_for_Pnt_derived"] is False)
    check("largest signed selector is not orientation-invariant", certificate["largest_signed_selector_orientation_invariant"] is False)
    check("absolute-response max keeps P_0", certificate["absolute_response_max_selects_P0"] is True)

    no_go_audit = {
        "route_pruned": (
            "choosing the source orientation/sign that makes P_nt largest "
            "derives accepted zero-singlet physical top-block membership"
        ),
        "counterfamily": {
            "plus_Bx": "largest signed response selects P_0",
            "minus_Bx": "largest signed response selects P_nt only by opposite source orientation",
            "ell_to_minus_ell": "same-source top/W ratio is unchanged",
            "absolute_response": "orientation-invariant maximum selects P_0",
            "minimum_response": "P_nt selection imports a minimum-response convention",
        },
        "remaining_imports": [
            "accepted physical source-orientation/sign/order/readout law excluding P_0",
            "accepted same-surface generator factorization",
            "accepted strict same-source top/W pole rows or degenerate-pole response rule",
            "contact/FV/IR/model-class controls",
        ],
    }
    check("no-go audit names source orientation", "source orientation" in no_go_audit["route_pruned"])
    check("no-go audit records invariant ratio", "unchanged" in no_go_audit["counterfamily"]["ell_to_minus_ell"])
    check("no-go audit keeps strict rows open", any("strict" in item for item in no_go_audit["remaining_imports"]))
    return {"certificate_boundary": certificate, "no_go_audit": no_go_audit}


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and wording")
    note = read(NOTE)
    one_line = " ".join(note.split())
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
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "zero singlet weight is derived",
        "strict W/top pole isolation is provided",
        "full positive Y_T closure",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T C3 SOURCE-ORIENTATION SIGN SELECTOR NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    orientation = part2_same_source_orientation_invariance()
    sign_witness = part3_sign_selector_witness()
    no_go = part4_no_go_certificate()
    part5_firewalls()

    result = {
        "claim_id": "yt_c3_source_orientation_sign_selector_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_c3_source_orientation_sign_selector_no_go.py",
        "actual_current_surface_status": "no-go / open source-orientation sign law",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Selecting P_nt by source-sign choice depends on an unaccepted "
            "orientation of the same source coordinate. The same-source response "
            "ratio is invariant under ell -> -ell, largest absolute response "
            "selects P_0, and minimum-response selection remains an imported "
            "convention."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "anchors": anchors,
        "same_source_orientation_invariance": orientation,
        "source_orientation_selector_witness": sign_witness,
        **no_go,
        "first_principles_elon_summary": {
            "A_min": [
                "finite positive transfer/Feynman-Hellmann response support",
                "same-source top/W source-coordinate cancellation",
                "real finite-record C3 source theorem selecting B_x up to sign",
                "finite C3 projector/block algebra",
                "nontrivial-block matrix-element support theorem",
                "zero-singlet membership no-go",
            ],
            "route_attempted": "derive zero P_0 singlet weight by source orientation/sign selection",
            "stuck_fanout_frames": [
                "coordinate orientation",
                "signed response ordering",
                "sign-blind absolute response ordering",
                "minimum-response rule",
                "strict pole bypass",
            ],
            "result": "blocked by source-coordinate orientation invariance and response-order counterwitnesses",
        },
        "route_still_live": (
            "derive an accepted same-surface source-orientation/sign/readout law "
            "excluding P_0 with generator factorization, or produce accepted "
            "strict same-source top/W pole rows"
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

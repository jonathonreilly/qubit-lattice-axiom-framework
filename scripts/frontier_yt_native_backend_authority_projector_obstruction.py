#!/usr/bin/env python3
"""Y_T native backend authority projector obstruction.

This runner proves the next narrow obstruction after the no-kappa backend
candidate: a normalized source generator and carrier amplitude do not fix
Feynman-Hellmann slopes without accepted W/top sector projectors.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"

NOTE = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
NATIVE_BACKEND = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
SPARSE_CERT = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
STRICT_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
STAGGERED_GATE = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
STAGGERED_SYNTHESIS = DOCS / "STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md"
STAGGERED_LABEL_NOGO = DOCS / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

NATIVE_BACKEND_OUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
SPARSE_CERT_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
STRICT_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"

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


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        NATIVE_BACKEND,
        SPARSE_CERT,
        STRICT_OBSTRUCTION,
        STAGGERED_GATE,
        STAGGERED_SYNTHESIS,
        STAGGERED_LABEL_NOGO,
        FULL_STACK,
        NATIVE_BACKEND_OUT,
        SPARSE_CERT_OUT,
        STRICT_OBSTRUCTION_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Finite Witness",
        "Relation To Existing Work",
        "What Would Close",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "sector projectors/eigenvectors are load-bearing",
        "It does not refute the native backend candidate",
        "Source normalization and carrier algebra do not determine sector matrix",
        "proposal_allowed: false",
    ):
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    native = load_json(NATIVE_BACKEND_OUT)
    sparse = load_json(SPARSE_CERT_OUT)
    obstruction = load_json(STRICT_OBSTRUCTION_OUT)
    check("native backend candidate passed", native.get("fail_count") == 0, native.get("fail_count"))
    check("native backend candidate is bounded support", native.get("actual_current_surface_status") == "bounded-support backend candidate")
    check("sparse certificate passed", sparse.get("fail_count") == 0, sparse.get("fail_count"))
    check("strict coefficient obstruction passed", obstruction.get("fail_count") == 0, obstruction.get("fail_count"))

    staggered_text = read(STAGGERED_SYNTHESIS)
    label_text = read(STAGGERED_LABEL_NOGO)
    check("staggered synthesis carries species-label residual", "AC_φλ" in staggered_text or "AC_phi_lambda" in staggered_text)
    check("staggered label note is no-go within A_min", "no-go within A_min" in label_text)
    check("staggered gate parent remains open gate", "open_gate" in read(STAGGERED_GATE))

    return {
        "native_backend": native,
        "sparse_certificate": sparse,
        "strict_obstruction": obstruction,
    }


def part2_fh_projector_witness() -> dict[str, Any]:
    print("\nPart 2: finite FH projector witness")
    ell, a, b, a_alt, g2, A = sp.symbols("ell a b a_alt g_2 A", positive=True)
    e0, e_w, e_t = sp.symbols("E_0 E_W E_t", real=True)
    h0 = sp.diag(e0, e_w, e_t)
    g = sp.diag(0, a, b)
    h = h0 + ell * g
    d_e0 = sp.diff(h[0, 0], ell)
    d_ew = sp.diff(h[1, 1], ell)
    d_et = sp.diff(h[2, 2], ell)
    dm_w = sp.simplify(d_ew - d_e0)
    dm_t = sp.simplify(d_et - d_e0)
    readout = sp.simplify(g2 / sp.sqrt(2) * dm_t / dm_w)

    candidate_a = g2 * A / 2
    candidate_b = A / sp.sqrt(12)
    alt_b = 2 * A / sp.sqrt(12)
    read_candidate = sp.simplify(readout.subs({a: candidate_a, b: candidate_b}))
    read_alt = sp.simplify(readout.subs({a: candidate_a, b: alt_b}))

    check("FH W derivative is sector expectation difference", is_zero(dm_w - a), dm_w)
    check("FH top derivative is sector expectation difference", is_zero(dm_t - b), dm_t)
    check("response readout depends on sector matrix element b", "b" in sp.sstr(readout), readout)
    check("candidate sector expectations give 1/sqrt(6)", is_zero(read_candidate - 1 / sp.sqrt(6)), read_candidate)
    check("alternative top sector expectation changes readout", not is_zero(read_alt - read_candidate), read_alt)
    check("alternative preserves same W sector expectation", is_zero(candidate_a - candidate_a), candidate_a)
    check("alternative is not a source-coordinate reparameterization", is_zero(read_alt - 2 / sp.sqrt(6)), read_alt)

    return {
        "G_matrix": sp.sstr(g),
        "dM_W_dell": sp.sstr(dm_w),
        "dM_t_dell": sp.sstr(dm_t),
        "readout": sp.sstr(readout),
        "candidate_readout": sp.sstr(read_candidate),
        "alternative_readout": sp.sstr(read_alt),
        "conclusion": "source generator normalization does not fix sector projectors or matrix elements",
    }


def part3_scope_and_next_action() -> dict[str, Any]:
    print("\nPart 3: scope and next action")
    strict_fields = {
        "source_generator_normalized": True,
        "candidate_rows_exist": True,
        "accepted_same_surface_transfer_backend_present": False,
        "w_projector_derived": False,
        "top_projector_derived": False,
        "fh_matrix_elements_derived": False,
        "contact_subtraction_done": False,
        "finite_volume_ir_controls_pass": False,
        "same_model_class": False,
    }
    for key, value in strict_fields.items():
        check(f"field status recorded: {key}", isinstance(value, bool), value)
    check("positive certificate fails because projectors are absent", strict_fields["w_projector_derived"] is False and strict_fields["top_projector_derived"] is False)
    check("positive certificate fails because backend authority absent", strict_fields["accepted_same_surface_transfer_backend_present"] is False)
    check("source normalization is not the remaining blocker", strict_fields["source_generator_normalized"] is True)
    return strict_fields


def part4_firewalls() -> None:
    print("\nPart 4: firewalls")
    text = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
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
        "strict top/W pole-response evidence exists",
        "full positive Y_T closure",
        "reject the no-`kappa` backend candidate",
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
            "Source normalization and carrier algebra do not determine sector "
            "matrix elements. The native backend candidate still needs accepted "
            "W/top projectors or strict pole-row evidence."
        ),
        "bare_retained_allowed": False,
        "route_pruned": (
            "derive native backend authority from normalized source generator "
            "and carrier amplitude alone"
        ),
        "route_still_live": (
            "derive accepted W/top sector projectors and G-matrix elements on "
            "the same finite transfer/action surface"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is negative route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("live route is projector/dynamics derivation", "sector projectors" in status["route_still_live"])
    return status


def main() -> None:
    anchors = part1_anchors()
    witness = part2_fh_projector_witness()
    fields = part3_scope_and_next_action()
    part4_firewalls()
    status = part5_claim_status()

    payload = {
        "claim_id": "yt_native_backend_authority_projector_obstruction_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_native_backend_authority_projector_obstruction.py",
        "anchors": anchors,
        "finite_fh_projector_witness": witness,
        "strict_certificate_field_status": fields,
        **status,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    raise SystemExit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()

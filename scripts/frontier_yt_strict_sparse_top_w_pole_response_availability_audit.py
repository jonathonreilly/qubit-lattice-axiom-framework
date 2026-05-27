#!/usr/bin/env python3
"""Y_T strict sparse top/W pole-response availability audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"

NOTE = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
DIRECT_SPARSE = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
NATIVE_BACKEND = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
BACKEND_PROJECTOR_OBSTRUCTION = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
FIRST_PRINCIPLES = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"

FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
DIRECT_SPARSE_OUT = ROOT / "outputs" / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
NATIVE_BACKEND_OUT = ROOT / "outputs" / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
BACKEND_PROJECTOR_OBSTRUCTION_OUT = ROOT / "outputs" / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"
FIRST_PRINCIPLES_OUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"

STRICT_TOP_W_ROWS = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
STRICT_SOURCE_HIGGS_ROWS = ROOT / "outputs" / "yt_source_action_block508_id_source_higgs_strict_rows_2026-05-22.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (
        NOTE,
        FULL_STACK,
        DIRECT_SPARSE,
        NATIVE_BACKEND,
        BACKEND_PROJECTOR_OBSTRUCTION,
        FIRST_PRINCIPLES,
        FULL_STACK_OUT,
        DIRECT_SPARSE_OUT,
        NATIVE_BACKEND_OUT,
        BACKEND_PROJECTOR_OBSTRUCTION_OUT,
        FIRST_PRINCIPLES_OUT,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "First-Principles / Elon Exercise",
        "Availability Witness",
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
        "blocked_no_accepted_backend",
        "accepted_same_surface_transfer_backend_present: false",
    ):
        check(f"note contains availability phrase: {phrase}", phrase in note)

    full = load_json(FULL_STACK_OUT)
    direct = load_json(DIRECT_SPARSE_OUT)
    native = load_json(NATIVE_BACKEND_OUT)
    obstruction = load_json(BACKEND_PROJECTOR_OBSTRUCTION_OUT)
    first = load_json(FIRST_PRINCIPLES_OUT)
    check("full stack passed", full.get("fail_count") == 0, full.get("fail_count"))
    check("direct sparse harness passed", direct.get("fail_count") == 0, direct.get("fail_count"))
    check("native backend candidate passed", native.get("fail_count") == 0, native.get("fail_count"))
    check("backend projector obstruction passed", obstruction.get("fail_count") == 0, obstruction.get("fail_count"))
    check("first-principles transfer boundary passed", first.get("fail_count") == 0, first.get("fail_count"))

    return {
        "full_stack_status": full.get("actual_current_surface_status"),
        "direct_sparse_status": direct.get("actual_current_surface_status"),
        "native_backend_status": native.get("actual_current_surface_status"),
        "backend_obstruction_status": obstruction.get("actual_current_surface_status"),
    }


def part2_availability_audit() -> dict[str, Any]:
    print("\nPart 2: strict artifact availability")
    direct = load_json(DIRECT_SPARSE_OUT)
    native = load_json(NATIVE_BACKEND_OUT)

    check("strict top/W rows artifact absent", not STRICT_TOP_W_ROWS.exists(), STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("strict source/Higgs rows artifact absent", not STRICT_SOURCE_HIGGS_ROWS.exists(), STRICT_SOURCE_HIGGS_ROWS.relative_to(ROOT).as_posix())
    check("direct sparse certificate says strict rows absent", direct.get("strict_top_w_response_certificate_present") is False)
    check("direct sparse strict positive certificate does not pass", direct.get("strict_certificate_schema", {}).get("strict_positive_certificate_passes") is False)
    check("candidate backend blocked by missing accepted backend", direct.get("candidate_action_backend", {}).get("status") == "blocked_no_accepted_backend")
    check("native candidate is not accepted backend", native.get("candidate_backend", {}).get("accepted_same_surface_transfer_backend_present") is False)
    check("native candidate top pole not accepted isolated", native.get("candidate_backend", {}).get("accepted_top_pole_isolated") is False)
    check("native candidate W pole not accepted isolated", native.get("candidate_backend", {}).get("accepted_w_pole_isolated") is False)
    check("native candidate contact subtraction absent", native.get("candidate_backend", {}).get("contact_subtraction_done") is False)
    check("native candidate FV/IR controls absent", native.get("candidate_backend", {}).get("finite_volume_ir_controls_pass") is False)
    check("native candidate same model class absent", native.get("candidate_backend", {}).get("same_model_class") is False)
    check("native candidate proposal not allowed", native.get("proposal_allowed") is False)
    check("native candidate readout is support only", native.get("candidate_backend", {}).get("readout_equals_1_over_sqrt6") is True)

    return {
        "strict_top_w_rows_artifact_present": STRICT_TOP_W_ROWS.exists(),
        "strict_source_higgs_rows_artifact_present": STRICT_SOURCE_HIGGS_ROWS.exists(),
        "direct_sparse_certificate_present": True,
        "strict_positive_certificate_passes": direct.get("strict_certificate_schema", {}).get("strict_positive_certificate_passes"),
        "candidate_action_backend_status": direct.get("candidate_action_backend", {}).get("status"),
        "native_candidate_backend": {
            "accepted_same_surface_transfer_backend_present": native.get("candidate_backend", {}).get("accepted_same_surface_transfer_backend_present"),
            "accepted_top_pole_isolated": native.get("candidate_backend", {}).get("accepted_top_pole_isolated"),
            "accepted_w_pole_isolated": native.get("candidate_backend", {}).get("accepted_w_pole_isolated"),
            "contact_subtraction_done": native.get("candidate_backend", {}).get("contact_subtraction_done"),
            "finite_volume_ir_controls_pass": native.get("candidate_backend", {}).get("finite_volume_ir_controls_pass"),
            "same_model_class": native.get("candidate_backend", {}).get("same_model_class"),
            "readout_equals_1_over_sqrt6": native.get("candidate_backend", {}).get("readout_equals_1_over_sqrt6"),
        },
    }


def part3_certificate_boundary() -> dict[str, bool]:
    print("\nPart 3: certificate boundary")
    fields = {
        "strict_sparse_harness_present": True,
        "native_no_kappa_candidate_present": True,
        "accepted_same_surface_backend_present": False,
        "accepted_top_pole_isolated": False,
        "accepted_w_pole_isolated": False,
        "coefficient_certified_dM_t_row_present": False,
        "coefficient_certified_dM_W_row_present": False,
        "contact_fv_ir_model_class_controls_present": False,
        "strict_positive_certificate_present": False,
        "no_forbidden_imports": True,
    }
    for key, value in fields.items():
        check(f"field recorded: {key}", isinstance(value, bool), value)
    check("strict route is unavailable because accepted backend is absent", fields["strict_sparse_harness_present"] and not fields["accepted_same_surface_backend_present"])
    check("strict positive certificate remains absent", fields["strict_positive_certificate_present"] is False)
    return fields


def part4_firewalls() -> None:
    print("\nPart 4: firewalls and wording")
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
        "strict top/W pole-response evidence is present",
        "positive Y_T closure is obtained",
        "full Y_T closure",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def part5_claim_status() -> dict[str, Any]:
    print("\nPart 5: claim status")
    status = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": "current branch already contains strict same-source top/W pole-response evidence",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_still_live": (
            "produce accepted strict top/W pole rows or derive the accepted "
            "backend/projectors/matrix elements from microscopic dynamics"
        ),
    }
    check("actual status is no-go", status["actual_current_surface_status"] == "no-go")
    check("trace class is route pruning", status["trace_class"] == "negative_route_pruning")
    check("proposal remains false", status["proposal_allowed"] is False)
    check("route still live names strict rows", "strict top/W pole rows" in status["route_still_live"])
    return status


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT SPARSE TOP/W POLE-RESPONSE AVAILABILITY AUDIT")
    print("=" * 78)

    anchors = part1_anchors()
    availability = part2_availability_audit()
    certificate = part3_certificate_boundary()
    part4_firewalls()
    status = part5_claim_status()

    result = {
        "claim_id": "yt_strict_sparse_top_w_pole_response_availability_audit_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_strict_sparse_top_w_pole_response_availability_audit.py",
        **status,
        "proposal_allowed_reason": (
            "The strict sparse harness and no-kappa candidate are present, but "
            "the accepted same-surface backend, isolated W/top projectors, and "
            "controlled coefficient-certified pole rows are absent."
        ),
        "anchors": anchors,
        "availability_witness": availability,
        "certificate_boundary": certificate,
        "next_ranked_route": "new microscopic backend/projector/matrix-element theorem",
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

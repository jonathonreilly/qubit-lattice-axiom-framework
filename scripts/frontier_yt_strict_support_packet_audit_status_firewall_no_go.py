#!/usr/bin/env python3
"""Y_T strict support-packet audit-status firewall no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_support_packet_audit_status_firewall_no_go_2026-05-28.json"

NOTE = DOCS / "YT_STRICT_SUPPORT_PACKET_AUDIT_STATUS_FIREWALL_NO_GO_NOTE_2026-05-28.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
STRICT_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
STRICT_DISCOVERY = DOCS / "YT_STRICT_TOP_W_POLE_ROW_REPOSITORY_DISCOVERY_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

STRICT_WZ_OUT = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
STRICT_TOP_OUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
STRICT_AVAILABILITY_OUT = ROOT / "outputs" / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
STRICT_DISCOVERY_OUT = ROOT / "outputs" / "yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json"
FULL_STACK_OUT = ROOT / "outputs" / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

AUDIT_QUEUE = DOCS / "audit" / "data" / "audit_queue.json"
AUDIT_LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

WZ_ID = "yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25"
TOP_ID = "yt_strict_symbolic_top_response_row_packet_note_2026-05-25"
SOURCE_RATIO_ID = "yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25"
NEUTRAL_RAY_ID = "yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25"

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


def contains_phrase(text: str, phrase: str) -> bool:
    normalized_text = " ".join(text.lower().split())
    normalized_phrase = " ".join(phrase.lower().split())
    return normalized_phrase in normalized_text


def audit_queue_row(claim_id: str) -> dict[str, Any]:
    queue = load_json(AUDIT_QUEUE)["queue"]
    for row in queue:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def audit_ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = load_json(AUDIT_LEDGER)
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> None:
    print("\nPart 1: anchors and note surface")
    for path in (
        NOTE,
        STRICT_WZ,
        STRICT_TOP,
        STRICT_AVAILABILITY,
        STRICT_DISCOVERY,
        FULL_STACK,
        STRICT_WZ_OUT,
        STRICT_TOP_OUT,
        STRICT_AVAILABILITY_OUT,
        STRICT_DISCOVERY_OUT,
        FULL_STACK_OUT,
        AUDIT_QUEUE,
        AUDIT_LEDGER,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Relation To Existing Strict Audits",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "Finite Algebra Witness",
        "No-Go Audit",
        "Stuck Fan-Out Synthesis",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / strict support packets are not accepted pole rows",
        "proposal_allowed: false",
        "dM_t/ds = (y_33/sqrt(2)) v'(s)",
        "both strict support packets are unaudited",
        "accepted coefficient-bearing strict top/W pole rows",
    ):
        check(f"note contains firewall phrase: {phrase}", contains_phrase(note, phrase))


def part2_support_packet_self_boundaries() -> dict[str, Any]:
    print("\nPart 2: support packet self-boundaries")
    wz = load_json(STRICT_WZ_OUT)
    top = load_json(STRICT_TOP_OUT)
    availability = load_json(STRICT_AVAILABILITY_OUT)
    discovery = load_json(STRICT_DISCOVERY_OUT)
    full_stack = load_json(FULL_STACK_OUT)

    for name, data in (
        ("strict_wz", wz),
        ("strict_top", top),
        ("strict_availability", availability),
        ("strict_discovery", discovery),
        ("full_stack", full_stack),
    ):
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))

    check("W/Z denominator response closed", wz.get("strict_wz_denominator_response_closed") is True)
    check(
        "W/Z packet lacks coefficient-certified top row",
        wz.get("current_blockers", {}).get("coefficient_certified_top_response_present") is False,
    )
    check(
        "W/Z packet lacks physical-scale g2 authority",
        wz.get("current_blockers", {}).get("physical_scale_g2_retained") is False,
    )
    check(
        "W/Z packet lacks retained one-Higgs authority",
        wz.get("current_blockers", {}).get("one_higgs_yukawa_selection_retained") is False,
    )
    check(
        "W/Z packet does not allow proposal",
        wz.get("proposal_allowed") is False,
        wz.get("proposal_allowed_reason", ""),
    )

    check("symbolic top row shape closed", top.get("symbolic_top_response_shape_closed") is True)
    check("symbolic top coefficient remains free", top.get("top_coefficient_derived") is False)
    check(
        "symbolic top packet lacks retained one-Higgs authority",
        top.get("current_blockers", {}).get("one_higgs_yukawa_selection_retained") is False,
    )
    check(
        "symbolic top packet lacks hypercharge authority",
        top.get("current_blockers", {}).get("hypercharge_uniqueness_retained") is False,
    )
    check(
        "symbolic top packet does not allow proposal",
        top.get("proposal_allowed") is False,
        top.get("proposal_allowed_reason", ""),
    )

    check(
        "availability audit lacks accepted backend",
        availability.get("certificate_boundary", {}).get("accepted_same_surface_backend_present") is False,
    )
    check(
        "availability audit lacks strict positive certificate",
        availability.get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    check(
        "availability audit lacks contact/FV/IR/model controls",
        availability.get("certificate_boundary", {}).get("contact_fv_ir_model_class_controls_present") is False,
    )
    check("repository discovery finds no complete strict packet", discovery.get("complete_strict_packet_count") == 0)
    check("repository discovery keeps strict certificate absent", discovery.get("strict_positive_certificate_present") is False)

    return {
        "strict_wz": wz,
        "strict_top": top,
        "strict_availability": availability,
        "strict_discovery": discovery,
        "full_stack": full_stack,
    }


def part3_audit_metadata_firewall() -> dict[str, Any]:
    print("\nPart 3: audit metadata firewall")
    ids = (WZ_ID, TOP_ID, SOURCE_RATIO_ID, NEUTRAL_RAY_ID)
    queue_rows = {claim_id: audit_queue_row(claim_id) for claim_id in ids}
    ledger_rows = {claim_id: audit_ledger_row(claim_id) for claim_id in ids}

    for claim_id in ids:
        queue = queue_rows[claim_id]
        ledger = ledger_rows[claim_id]
        check(f"{claim_id} queue row exists", queue.get("claim_id") == claim_id)
        check(f"{claim_id} ledger row exists", ledger.get("claim_id") == claim_id)
        check(f"{claim_id} queue audit status is unaudited", queue.get("audit_status") == "unaudited", queue.get("audit_status"))
        check(
            f"{claim_id} queue effective status is unaudited",
            queue.get("effective_status") == "unaudited",
            queue.get("effective_status"),
        )
        check(
            f"{claim_id} ledger audit status is unaudited",
            ledger.get("audit_status") == "unaudited",
            ledger.get("audit_status"),
        )
        check(
            f"{claim_id} ledger effective status is unaudited",
            ledger.get("effective_status") == "unaudited",
            ledger.get("effective_status"),
        )
        check(f"{claim_id} has no audit verdict", ledger.get("verdict") is None)

    check("W/Z support packet is bounded theorem in queue", queue_rows[WZ_ID].get("claim_type") == "bounded_theorem")
    check("symbolic top support packet is bounded theorem in queue", queue_rows[TOP_ID].get("claim_type") == "bounded_theorem")
    return {"queue": queue_rows, "ledger": ledger_rows}


def part4_same_source_symbolic_undertermination() -> dict[str, str]:
    print("\nPart 4: same-source symbolic underdetermination")
    y33, g2, vp = sp.symbols("y_33 g_2 vprime", nonzero=True)
    dmt = y33 * vp / sp.sqrt(2)
    dmw = g2 * vp / 2
    ratio = sp.simplify(dmt / dmw)
    y_target = sp.solve(sp.Eq(ratio, 1 / sp.sqrt(3)), y33)
    witness_1 = sp.simplify(ratio.subs(y33, g2 / sp.sqrt(6)))
    witness_2 = sp.simplify(ratio.subs(y33, g2))

    check("same-source ratio cancels source Jacobian", is_zero(ratio - sp.sqrt(2) * y33 / g2), ratio)
    check("target ratio would require a y33/g2 law", y_target == [g2 / sp.sqrt(6)], y_target)
    check("first symbolic completion gives target-sized ratio", is_zero(witness_1 - 1 / sp.sqrt(3)), witness_1)
    check("second symbolic completion gives different ratio", is_zero(witness_2 - sp.sqrt(2)), witness_2)
    check("same W row is independent of y33", not dmw.has(y33), dmw)
    check("top row remains dependent on y33", dmt.has(y33), dmt)

    return {
        "dM_t_ds": "y_33*vprime/sqrt(2)",
        "dM_W_ds": "g_2*vprime/2",
        "ratio": "sqrt(2)*y_33/g_2",
        "target_ratio_requires_y33": "g_2/sqrt(6)",
        "witness_y33_g2_over_sqrt6_ratio": "1/sqrt(3)",
        "witness_y33_g2_ratio": "sqrt(2)",
    }


def part5_forbidden_inputs_and_certificate_boundary(
    support: dict[str, Any], metadata: dict[str, Any]
) -> dict[str, Any]:
    print("\nPart 5: forbidden inputs and certificate boundary")
    note = read(NOTE)
    forbidden = (
        "H_unit",
        "old Ward authority",
        "yt_ward_identity",
        "y_t_bare",
        "observed top/W/Z masses",
        "PDG targets",
        "alpha_LM",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selectors",
        "target value insertion",
    )
    for phrase in forbidden:
        check(f"forbidden input listed as not used: {phrase}", contains_phrase(note, phrase))

    availability = support["strict_availability"]
    wz_queue = metadata["queue"][WZ_ID]
    top_queue = metadata["queue"][TOP_ID]
    boundary = {
        "strict_wz_denominator_support_present": support["strict_wz"].get("strict_wz_denominator_response_closed") is True,
        "symbolic_top_row_shape_present": support["strict_top"].get("symbolic_top_response_shape_closed") is True,
        "top_coefficient_derived": support["strict_top"].get("top_coefficient_derived") is True,
        "strict_wz_packet_audited_or_retained": wz_queue.get("effective_status") not in {None, "unaudited"},
        "strict_top_packet_audited_or_retained": top_queue.get("effective_status") not in {None, "unaudited"},
        "accepted_same_surface_backend_present": availability.get("certificate_boundary", {}).get(
            "accepted_same_surface_backend_present"
        )
        is True,
        "strict_positive_certificate_present": availability.get("certificate_boundary", {}).get(
            "strict_positive_certificate_present"
        )
        is True,
        "contact_fv_ir_model_class_controls_present": availability.get("certificate_boundary", {}).get(
            "contact_fv_ir_model_class_controls_present"
        )
        is True,
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "positive_closure_marker_allowed": False,
    }
    check("W/Z denominator support is present", boundary["strict_wz_denominator_support_present"] is True)
    check("symbolic top row shape is present", boundary["symbolic_top_row_shape_present"] is True)
    check("top coefficient is not derived", boundary["top_coefficient_derived"] is False)
    check("W/Z packet is not audited or retained", boundary["strict_wz_packet_audited_or_retained"] is False)
    check("top packet is not audited or retained", boundary["strict_top_packet_audited_or_retained"] is False)
    check("accepted same-surface backend remains absent", boundary["accepted_same_surface_backend_present"] is False)
    check("strict positive certificate remains absent", boundary["strict_positive_certificate_present"] is False)
    check("contact/FV/IR/model controls remain absent", boundary["contact_fv_ir_model_class_controls_present"] is False)
    check("proposal remains disallowed", boundary["proposal_allowed"] is False)
    check("positive marker remains disallowed", boundary["positive_closure_marker_allowed"] is False)
    return boundary


def main() -> int:
    part1_anchors()
    support = part2_support_packet_self_boundaries()
    metadata = part3_audit_metadata_firewall()
    algebra = part4_same_source_symbolic_undertermination()
    boundary = part5_forbidden_inputs_and_certificate_boundary(support, metadata)

    result = {
        "claim_id": "yt_strict_support_packet_audit_status_firewall_no_go_note_2026-05-28",
        "claim_type": "no_go",
        "actual_current_surface_status": "no-go / strict support packets are not accepted pole rows",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "route_pruned": (
            "existing strict W/Z support packet plus symbolic top response packet certify accepted "
            "coefficient-bearing strict top/W pole rows"
        ),
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "positive_closure_marker_allowed": False,
        "positive_closure_marker_written": False,
        "forbidden_inputs_used": False,
        "proposal_allowed_reason": (
            "The W/Z packet is denominator support, the top packet keeps y_33 free, both packets "
            "are unaudited in the audit queue/ledger, and the strict availability schema still "
            "lacks accepted backend/projectors/controlled pole rows."
        ),
        "same_source_symbolic_witness": algebra,
        "audit_metadata_witness": {
            claim_id: {
                "queue_effective_status": metadata["queue"][claim_id].get("effective_status"),
                "queue_audit_status": metadata["queue"][claim_id].get("audit_status"),
                "ledger_effective_status": metadata["ledger"][claim_id].get("effective_status"),
                "ledger_audit_status": metadata["ledger"][claim_id].get("audit_status"),
            }
            for claim_id in (WZ_ID, TOP_ID, SOURCE_RATIO_ID, NEUTRAL_RAY_ID)
        },
        "dependency_fail_counts": {
            "strict_wz": support["strict_wz"].get("fail_count"),
            "strict_top": support["strict_top"].get("fail_count"),
            "strict_availability": support["strict_availability"].get("fail_count"),
            "strict_discovery": support["strict_discovery"].get("fail_count"),
            "full_stack": support["full_stack"].get("fail_count"),
        },
        "certificate_boundary": boundary,
        "next_exact_action": (
            "produce accepted strict top/W pole rows with controls, or derive accepted "
            "same-surface backend/projectors/source-generator matrix elements"
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

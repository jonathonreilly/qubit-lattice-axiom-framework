#!/usr/bin/env python3
"""
PR #230 Block127 W/Z builder adapter for the Block126 top-side packet.

Block126 retired the old coarse top-side row limitation by building 1008
same-configuration top rows.  This runner verifies that the W/Z mass-fit
response-row builder now recognizes that packet as top-side support, while
still refusing strict W/Z measurement-row output until genuine W/Z rows,
matched top-W/Z covariance, strict g2, and accepted action authority exist.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block127_wz_builder_block126_top_packet_adapter_2026-05-17.json"
)

PARENTS = {
    "block126_matched_top_additive_subtraction_packet": (
        "outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json"
    ),
    "wz_mass_fit_response_row_builder": (
        "outputs/yt_wz_mass_fit_response_row_builder_2026-05-04.json"
    ),
    "wz_response_measurement_row_contract": (
        "outputs/yt_wz_response_measurement_row_contract_gate_2026-05-03.json"
    ),
    "wz_correlator_mass_fit_path": (
        "outputs/yt_wz_correlator_mass_fit_path_gate_2026-05-04.json"
    ),
    "wz_g2_authority_firewall": "outputs/yt_wz_g2_authority_firewall_2026-05-05.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "promoted_dE_dm_bare_to_dE_dh": False,
    "promoted_top_side_packet_to_wz_closure": False,
    "assumed_top_wz_covariance_or_factorization": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_g2_equal_one": False,
    "claimed_retained_or_proposed_retained": False,
}

PASS_COUNT = 0
FAIL_COUNT = 0


def report(tag: str, ok: bool, msg: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        state = "PASS"
    else:
        FAIL_COUNT += 1
        state = "FAIL"
    print(f"  [{state}] {tag}: {msg}")


def load_json(rel: str) -> dict[str, Any]:
    path = ROOT / rel
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def main() -> int:
    print("PR #230 Block127 W/Z builder Block126 top-packet adapter")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    block126 = certs["block126_matched_top_additive_subtraction_packet"]
    builder = certs["wz_mass_fit_response_row_builder"]
    top_validation = builder.get("top_response_validation", {})
    wz_validation = builder.get("wz_validation", {})
    g2_validation = builder.get("g2_validation", {})

    block126_packet = block126.get("matched_top_side_packet", {})
    strict_state = block126.get("strict_subtraction_contract_state", {})

    report(
        "parent-certificates-present",
        all(certs.values()),
        f"missing={[name for name, cert in certs.items() if not cert]}",
    )
    report(
        "block126-top-side-packet-complete",
        block126.get("block126_matched_top_additive_subtraction_packet_passed") is True
        and block126_packet.get("matched_tau1_row_count") == 1008
        and len(block126_packet.get("per_tau_summary", {})) == 23,
        f"rows={block126_packet.get('matched_tau1_row_count')}",
    )
    report(
        "builder-consumes-block126-input",
        builder.get("top_response_input")
        == "outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json",
        str(builder.get("top_response_input")),
    )
    report(
        "builder-recognizes-top-side-support",
        top_validation.get("present") is True
        and top_validation.get("top_side_packet_valid") is True
        and top_validation.get("valid") is False,
        str(top_validation.get("failed_checks", [])),
    )
    report(
        "builder-status-names-block126-boundary",
        "Block126 top-side packet" in str(builder.get("actual_current_surface_status")),
        str(builder.get("actual_current_surface_status")),
    )
    report(
        "wz-rows-still-absent",
        wz_validation.get("present") is False
        and "W/Z mass-fit rows absent" in str(wz_validation.get("failed_checks", [])),
        str(wz_validation.get("failed_checks", [])),
    )
    report(
        "g2-still-absent",
        g2_validation.get("present") is False
        and "electroweak g2 certificate absent" in str(g2_validation.get("failed_checks", [])),
        str(g2_validation.get("failed_checks", [])),
    )
    report(
        "no-strict-rows-written",
        builder.get("measurement_rows_written") is False
        and builder.get("strict_wz_mass_fit_response_row_builder_passed") is False,
        f"written={builder.get('measurement_rows_written')}",
    )
    report(
        "block126-remains-nonclosure",
        strict_state.get("wz_rows_present") is False
        and strict_state.get("matched_top_wz_covariance_present") is False
        and strict_state.get("strict_non_observed_g2_present") is False
        and strict_state.get("accepted_same_source_ew_action_present") is False,
        str(strict_state),
    )
    report(
        "claim-firewall-clean",
        all(value is False for value in FORBIDDEN_FIREWALL.values())
        and builder.get("proposal_allowed") is False,
        "no retained/proposed_retained claim",
    )

    result = {
        "actual_current_surface_status": (
            "bounded-support / Block127 wires the Block126 matched top-side packet "
            "into the W/Z row builder; W/Z rows, matched top-W/Z covariance, "
            "strict g2, and accepted action remain absent"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The W/Z builder now recognizes Block126 top-side production support, "
            "but it still lacks genuine W/Z mass-fit rows, matched top-W/Z "
            "covariance, strict non-observed g2, and accepted same-source "
            "EW/Higgs action authority."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "block127_wz_builder_block126_top_packet_adapter_passed": FAIL_COUNT == 0,
        "parent_certificates": PARENTS,
        "builder_status": builder.get("actual_current_surface_status"),
        "builder_top_response_validation": top_validation,
        "builder_wz_validation": wz_validation,
        "builder_g2_validation": g2_validation,
        "block126_top_side_summary": top_validation.get("top_side_summary", {}),
        "strict_contract_state": {
            "top_side_packet_recognized_by_wz_builder": True,
            "wz_rows_present": False,
            "matched_top_wz_covariance_present": False,
            "strict_non_observed_g2_present": False,
            "accepted_same_source_ew_action_present": False,
            "strict_measurement_rows_written": False,
            "contract_satisfied_now": False,
        },
        "strict_non_claims": {
            "does_not_treat_dE_dm_bare_as_dE_dh": True,
            "does_not_use_observed_wz_or_g2": True,
            "does_not_supply_wz_response_rows": True,
            "does_not_supply_matched_top_wz_covariance": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Supply genuine same-source W/Z mass-fit rows with configuration keys "
            "that can be matched to Block126, strict non-observed g2, and accepted "
            "same-source EW/Higgs action authority; then rerun the W/Z builder and "
            "same-source W/Z gate."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }

    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

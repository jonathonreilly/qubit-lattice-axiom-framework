#!/usr/bin/env python3
"""
PR #230 Block128 post-Block127 W/Z production launch preflight.

Block127 makes the W/Z builder consume the Block126 top-side packet.  This
runner checks the remaining W/Z launch roots after that adapter: whether the
current surface can now produce genuine same-source W/Z mass-fit rows with
matched covariance, strict g2, and accepted action authority.  It does not
synthesize W/Z rows and does not promote smoke rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block128_post_block127_wz_launch_preflight_2026-05-17.json"
)
PRODUCTION_HARNESS = ROOT / "scripts" / "yt_direct_lattice_correlator_production.py"
STRICT_ROWS = ROOT / "outputs" / "yt_fh_gauge_mass_response_measurement_rows_2026-05-03.json"
WZ_MASS_FIT_ROWS = ROOT / "outputs" / "yt_wz_correlator_mass_fit_rows_2026-05-04.json"

PARENTS = {
    "block126_matched_top_additive_subtraction_packet": (
        "outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json"
    ),
    "block127_wz_builder_block126_top_packet_adapter": (
        "outputs/yt_pr230_block127_wz_builder_block126_top_packet_adapter_2026-05-17.json"
    ),
    "wz_mass_fit_response_row_builder": (
        "outputs/yt_wz_mass_fit_response_row_builder_2026-05-04.json"
    ),
    "wz_response_row_production_attempt": (
        "outputs/yt_wz_response_row_production_attempt_2026-05-03.json"
    ),
    "wz_correlator_mass_fit_path_gate": (
        "outputs/yt_wz_correlator_mass_fit_path_gate_2026-05-04.json"
    ),
    "wz_same_source_ew_action_gate": (
        "outputs/yt_wz_same_source_ew_action_gate_2026-05-04.json"
    ),
    "wz_same_source_ew_action_certificate_builder": (
        "outputs/yt_wz_same_source_ew_action_certificate_builder_2026-05-04.json"
    ),
    "wz_g2_authority_firewall": "outputs/yt_wz_g2_authority_firewall_2026-05-05.json",
    "top_wz_matched_covariance_builder": (
        "outputs/yt_top_wz_matched_covariance_certificate_builder_2026-05-04.json"
    ),
    "wz_smoke_to_production_promotion_no_go": (
        "outputs/yt_pr230_wz_smoke_to_production_promotion_no_go_2026-05-05.json"
    ),
    "wz_response_manifest": "outputs/yt_fh_gauge_mass_response_manifest_2026-05-02.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "promoted_wz_smoke_to_production": False,
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


def status(cert: dict[str, Any]) -> str:
    return str(cert.get("actual_current_surface_status", ""))


def display(path: Path) -> str:
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def main() -> int:
    print("PR #230 Block128 post-Block127 W/Z launch preflight")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposal_allowed = [
        name for name, cert in certs.items() if cert.get("proposal_allowed") is True
    ]
    harness_text = PRODUCTION_HARNESS.read_text(encoding="utf-8")

    block126 = certs["block126_matched_top_additive_subtraction_packet"]
    block127 = certs["block127_wz_builder_block126_top_packet_adapter"]
    row_builder = certs["wz_mass_fit_response_row_builder"]
    production_attempt = certs["wz_response_row_production_attempt"]
    mass_fit_gate = certs["wz_correlator_mass_fit_path_gate"]
    action_gate = certs["wz_same_source_ew_action_gate"]
    action_builder = certs["wz_same_source_ew_action_certificate_builder"]
    g2_firewall = certs["wz_g2_authority_firewall"]
    covariance_builder = certs["top_wz_matched_covariance_builder"]
    smoke_no_go = certs["wz_smoke_to_production_promotion_no_go"]

    top_side_satisfied = (
        block126.get("block126_matched_top_additive_subtraction_packet_passed") is True
        and block127.get("block127_wz_builder_block126_top_packet_adapter_passed") is True
        and block127.get("strict_contract_state", {}).get(
            "top_side_packet_recognized_by_wz_builder"
        )
        is True
    )
    builder_refuses_strict_rows = (
        row_builder.get("strict_wz_mass_fit_response_row_builder_passed") is False
        and row_builder.get("measurement_rows_written") is False
    )
    harness_smoke_only = all(
        token in harness_text
        for token in (
            "--wz-mass-response-smoke",
            "smoke_schema_enabled_not_ew_production",
            "synthetic_scout_contract_not_EW_field",
            "production_wz_rows_written",
        )
    )
    harness_has_production_wz_path = any(
        token in harness_text
        for token in (
            "--wz-production-response",
            "gauge_mass_response_analysis",
            "wz_correlator_measurement",
            "fit_wz_mass_correlator",
            "production_wz_rows_written\": True",
        )
    )
    production_attempt_blocks = (
        production_attempt.get("raw_wz_correlator_path_present") is False
        and production_attempt.get("measurement_rows_written") is False
        and production_attempt.get("production_attempt_closes_pr230") is False
    )
    mass_fit_rows_absent = (
        not WZ_MASS_FIT_ROWS.exists()
        and "WZ correlator mass-fit path absent" in status(mass_fit_gate)
    )
    action_absent = (
        action_gate.get("same_source_ew_action_ready") is False
        and action_builder.get("same_source_ew_action_certificate_valid") is False
    )
    g2_absent = g2_firewall.get("g2_authority_gate_passed") is False
    covariance_absent = (
        "matched top-W response rows absent" in status(covariance_builder)
        and covariance_builder.get("top_wz_matched_covariance_builder_passed") is False
    )
    smoke_promotion_blocked = (
        smoke_no_go.get("wz_smoke_to_production_promotion_no_go_passed") is True
        and "cannot be promoted" in status(smoke_no_go)
    )
    strict_rows_absent = not STRICT_ROWS.exists()

    root_matrix = {
        "top_side_packet": {
            "satisfied": top_side_satisfied,
            "evidence": PARENTS["block127_wz_builder_block126_top_packet_adapter"],
        },
        "production_wz_mass_fit_rows": {
            "satisfied": False,
            "blocked_by": PARENTS["wz_correlator_mass_fit_path_gate"],
        },
        "accepted_same_source_ew_action": {
            "satisfied": False,
            "blocked_by": PARENTS["wz_same_source_ew_action_gate"],
        },
        "strict_non_observed_g2": {
            "satisfied": False,
            "blocked_by": PARENTS["wz_g2_authority_firewall"],
        },
        "matched_top_wz_covariance": {
            "satisfied": False,
            "blocked_by": PARENTS["top_wz_matched_covariance_builder"],
        },
        "production_harness_path": {
            "satisfied": False,
            "blocked_by": display(PRODUCTION_HARNESS),
            "smoke_only": harness_smoke_only,
        },
    }

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposal_allowed, f"proposal_allowed={proposal_allowed}")
    report("top-side-root-satisfied-after-block127", top_side_satisfied, "Block126/127 top packet recognized")
    report("builder-still-refuses-strict-rows", builder_refuses_strict_rows, status(row_builder))
    report("production-harness-is-smoke-only-for-wz", harness_smoke_only, display(PRODUCTION_HARNESS))
    report("production-harness-lacks-genuine-wz-path", not harness_has_production_wz_path, "no production W/Z mass-fit implementation")
    report("legacy-production-attempt-still-blocks", production_attempt_blocks, status(production_attempt))
    report("wz-mass-fit-rows-absent", mass_fit_rows_absent, display(WZ_MASS_FIT_ROWS))
    report("accepted-action-absent", action_absent, status(action_gate))
    report("strict-g2-absent", g2_absent, status(g2_firewall))
    report("matched-top-wz-covariance-absent", covariance_absent, status(covariance_builder))
    report("wz-smoke-promotion-blocked", smoke_promotion_blocked, status(smoke_no_go))
    report("strict-row-file-not-written", strict_rows_absent, display(STRICT_ROWS))
    report("claim-firewall-clean", all(v is False for v in FORBIDDEN_FIREWALL.values()), "no forbidden shortcut")

    current_closure_satisfied = all(row["satisfied"] for row in root_matrix.values())
    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block128 post-Block127 W/Z production "
            "launch preflight: top-side root satisfied, W/Z rows/action/g2/"
            "covariance/production harness roots absent"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "After Block127, the top-side packet is no longer the W/Z launch "
            "blocker. The current surface still lacks genuine W/Z mass-fit "
            "rows, accepted same-source EW/Higgs action, strict non-observed "
            "g2, matched top-W/Z covariance, and a production W/Z harness."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "current_closure_satisfied": current_closure_satisfied,
        "block128_post_block127_wz_launch_preflight_passed": FAIL_COUNT == 0,
        "root_matrix": root_matrix,
        "harness_diagnosis": {
            "path": display(PRODUCTION_HARNESS),
            "wz_smoke_only": harness_smoke_only,
            "has_genuine_wz_production_path": harness_has_production_wz_path,
            "strict_rows_path": display(STRICT_ROWS),
            "strict_rows_present": not strict_rows_absent,
        },
        "parent_certificates": PARENTS,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": {
            "does_not_write_or_synthesize_wz_rows": True,
            "does_not_promote_smoke_rows": True,
            "does_not_use_observed_wz_or_g2": True,
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_treat_top_side_packet_as_wz_closure": True,
        },
        "minimal_unlock_packet": [
            "accepted same-source EW/Higgs action certificate",
            "genuine W/Z correlator mass-fit rows by source shift",
            "configuration keys matchable to the Block126 top-side rows",
            "matched top-W/Z covariance rows",
            "strict non-observed g2 or an allowed same-source cancellation theorem",
        ],
        "exact_next_action": (
            "Implement a genuine same-source EW/Higgs W/Z correlator mass-fit "
            "production path with accepted action and strict g2/covariance, or "
            "pivot back to accepted canonical O_H/action plus numeric "
            "C_ss/C_sH/C_HH pole-residue rows."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {display(OUTPUT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

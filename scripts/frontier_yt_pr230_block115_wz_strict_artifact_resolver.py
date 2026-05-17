#!/usr/bin/env python3
"""
PR #230 Block115 W/Z strict physical-response artifact resolver.

Block114 resolved the source-Higgs O_H/action plus C_ss/C_sH/C_HH artifact
contract on the current head.  This runner pivots to the next ranked route and
asks whether the current PR230 head contains a strict W/Z physical-response
packet: accepted same-source action, production W/Z rows, same-source top
rows, matched top/W covariance, strict non-observed g2 authority, delta_perp
authority, and final W-response rows.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "yt_pr230_block115_wz_strict_artifact_resolver_2026-05-17.json"

PARENTS = {
    "wz_packet_intake": "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json",
    "wz_same_source_action_minimal_cut": "outputs/yt_pr230_wz_same_source_action_minimal_certificate_cut_2026-05-07.json",
    "wz_accepted_action_root_checkpoint": "outputs/yt_pr230_wz_accepted_action_response_root_checkpoint_2026-05-07.json",
    "same_source_ew_action_builder": "outputs/yt_wz_same_source_ew_action_certificate_builder_2026-05-04.json",
    "same_source_ew_action_gate": "outputs/yt_wz_same_source_ew_action_gate_2026-05-04.json",
    "same_source_ew_higgs_action_ansatz": "outputs/yt_pr230_same_source_ew_higgs_action_ansatz_gate_2026-05-06.json",
    "wz_correlator_mass_fit_path_gate": "outputs/yt_wz_correlator_mass_fit_path_gate_2026-05-04.json",
    "wz_mass_fit_response_row_builder": "outputs/yt_wz_mass_fit_response_row_builder_2026-05-04.json",
    "same_source_top_response_builder": "outputs/yt_same_source_top_response_certificate_builder_2026-05-04.json",
    "same_source_wz_response_gate": "outputs/yt_same_source_wz_response_certificate_gate_2026-05-02.json",
    "top_wz_matched_covariance_builder": "outputs/yt_top_wz_matched_covariance_certificate_builder_2026-05-04.json",
    "electroweak_g2_certificate_builder": "outputs/yt_electroweak_g2_certificate_builder_2026-05-05.json",
    "wz_g2_authority_firewall": "outputs/yt_wz_g2_authority_firewall_2026-05-05.json",
    "wz_g2_response_self_normalization_no_go": "outputs/yt_wz_g2_response_self_normalization_no_go_2026-05-05.json",
    "pr230_wz_v_authority_firewall": "outputs/yt_pr230_wz_v_authority_firewall_2026-05-15.json",
    "delta_perp_tomography_builder": "outputs/yt_delta_perp_tomography_correction_builder_2026-05-04.json",
    "same_source_w_response_orthogonal_correction_gate": "outputs/yt_same_source_w_response_orthogonal_correction_gate_2026-05-04.json",
    "same_source_w_response_row_builder": "outputs/yt_same_source_w_response_row_builder_2026-05-04.json",
    "wz_smoke_to_production_no_go": "outputs/yt_pr230_wz_smoke_to_production_promotion_no_go_2026-05-05.json",
    "block114_source_higgs_strict_artifact_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

EXPECTED_STRICT_PATHS = {
    "accepted_same_source_ew_action": "outputs/yt_wz_same_source_ew_action_certificate_2026-05-04.json",
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "wz_correlator_mass_fit_rows": "outputs/yt_wz_correlator_mass_fit_rows_2026-05-04.json",
    "wz_mass_fit_response_rows": "outputs/yt_wz_mass_fit_response_rows_2026-05-04.json",
    "fh_gauge_mass_response_measurement_rows": "outputs/yt_fh_gauge_mass_response_measurement_rows_2026-05-03.json",
    "fh_gauge_mass_response_certificate": "outputs/yt_fh_gauge_mass_response_certificate_2026-05-02.json",
    "same_source_top_response_certificate": "outputs/yt_same_source_top_response_certificate_2026-05-04.json",
    "top_wz_matched_response_rows": "outputs/yt_top_wz_matched_response_rows_2026-05-04.json",
    "top_wz_matched_covariance_certificate": "outputs/yt_top_wz_matched_covariance_certificate_2026-05-04.json",
    "strict_electroweak_g2_certificate": "outputs/yt_electroweak_g2_certificate_2026-05-04.json",
    "delta_perp_correction_certificate": "outputs/yt_same_source_w_response_orthogonal_correction_certificate_2026-05-04.json",
    "same_source_w_response_rows": "outputs/yt_same_source_w_response_rows_2026-05-04.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_masses_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_static_ew_algebra_as_rows": False,
    "used_scout_or_smoke_rows_as_production_evidence": False,
    "used_conditional_action_ansatz_as_accepted_action": False,
    "assumed_top_wz_covariance_or_factorization": False,
    "set_delta_perp_zero_without_certificate": False,
    "set_g2_equal_one": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
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


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: str | Path) -> dict[str, Any]:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    data = json.loads(full.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def status(cert: dict[str, Any]) -> str:
    return str(cert.get("actual_current_surface_status", ""))


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def walk(obj: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
    rows: list[tuple[tuple[str, ...], Any]] = [(path, obj)]
    if isinstance(obj, dict):
        for key, value in obj.items():
            rows.extend(walk(value, path + (str(key),)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            rows.extend(walk(value, path + (str(index),)))
    return rows


def strict_wz_packet_row(row: Any) -> bool:
    if not isinstance(row, dict):
        return False
    if row.get("phase") not in (None, "production"):
        return False
    row_kind = str(row.get("row_kind", "")).lower()
    if "scout" in row_kind or "synthetic" in row_kind:
        return False
    if row.get("same_source_coordinate") is not True:
        return False
    flat_keys = set(row)
    has_top = any(key in flat_keys for key in ("R_t", "dE_top_ds", "slope_dE_top_ds"))
    has_w = any(key in flat_keys for key in ("R_W", "dM_W_ds", "slope_dM_W_ds"))
    has_cov = any(key in flat_keys for key in ("cov_R_t_R_W", "cov_dE_top_dM_W"))
    has_g2 = any(key in flat_keys and is_number(row.get(key)) for key in ("g_2", "g2"))
    has_delta = any(key in flat_keys and is_number(row.get(key)) for key in ("delta_perp", "orthogonal_correction_delta_perp"))
    nested = row.get("top_response"), row.get("gauge_response"), row.get("electroweak_coupling")
    has_nested = all(isinstance(value, dict) for value in nested)
    return (has_top and has_w and has_cov and has_g2 and has_delta) or has_nested


def scan_wz_candidates() -> dict[str, Any]:
    files: list[Path] = []
    for path in (ROOT / "outputs").glob("*.json"):
        name = path.name.lower()
        if any(
            token in name
            for token in (
                "wz",
                "w_response",
                "w_mass",
                "g2",
                "delta_perp",
                "covariance",
                "same_source_ew",
                "gauge_mass_response",
            )
        ):
            files.append(path)

    reference_files: list[str] = []
    scout_or_schema_files: list[str] = []
    strict_packet_hits: list[dict[str, Any]] = []

    for path in sorted(files):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        text = json.dumps(data, sort_keys=True)
        if any(token in text for token in ("delta_perp", "g2", "g_2", "cov_dE_top_dM_W", "same_source_coordinate")):
            reference_files.append(rel(path))
        if any(token in path.name for token in ("scout", "smoke", "contract", "schema")):
            scout_or_schema_files.append(rel(path))
        path_is_nonproduction = any(token in path.name for token in ("scout", "smoke", "contract", "schema"))
        for node_path, value in walk(data):
            if not path_is_nonproduction and strict_wz_packet_row(value):
                strict_packet_hits.append(
                    {
                        "path": rel(path),
                        "node_path": "/".join(node_path),
                        "row_keys": sorted(value) if isinstance(value, dict) else [],
                    }
                )

    return {
        "candidate_file_count": len(files),
        "reference_file_count": len(reference_files),
        "reference_files_sample": reference_files[:50],
        "scout_or_schema_files_sample": scout_or_schema_files[:30],
        "strict_wz_packet_row_hits": strict_packet_hits,
    }


def main() -> int:
    print("PR #230 Block115 W/Z strict physical-response artifact resolver")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_PATHS.items()
    }
    scan = scan_wz_candidates()

    accepted_action_absent = (
        certs["wz_same_source_action_minimal_cut"].get("current_surface_action_certificate_satisfied")
        is False
        and certs["same_source_ew_action_builder"].get("proposal_allowed") is False
        and "certificate absent" in statuses["same_source_ew_action_builder"]
        and "same-source EW action not defined" in statuses["same_source_ew_action_gate"]
        and certs["same_source_ew_higgs_action_ansatz"].get("current_surface_adoption_passed")
        is False
        and not strict_presence["accepted_same_source_ew_action"]
        and not strict_presence["canonical_higgs_operator_certificate"]
    )
    production_wz_rows_absent = (
        "WZ correlator mass-fit path absent" in statuses["wz_correlator_mass_fit_path_gate"]
        and certs["wz_mass_fit_response_row_builder"].get("mode") == "current"
        and certs["wz_mass_fit_response_row_builder"].get("measurement_rows_written") is False
        and certs["same_source_wz_response_gate"].get("same_source_wz_response_certificate_gate_passed")
        is False
        and not strict_presence["wz_correlator_mass_fit_rows"]
        and not strict_presence["wz_mass_fit_response_rows"]
        and not strict_presence["fh_gauge_mass_response_measurement_rows"]
        and not strict_presence["fh_gauge_mass_response_certificate"]
    )
    matched_top_wz_covariance_absent = (
        certs["same_source_top_response_builder"].get("mode") == "current"
        and certs["same_source_top_response_builder"].get("top_response_certificate_written")
        is False
        and certs["top_wz_matched_covariance_builder"].get("mode") == "current"
        and certs["top_wz_matched_covariance_builder"].get("covariance_certificate_written")
        is False
        and not strict_presence["same_source_top_response_certificate"]
        and not strict_presence["top_wz_matched_response_rows"]
        and not strict_presence["top_wz_matched_covariance_certificate"]
    )
    strict_g2_delta_final_w_rows_absent = (
        certs["electroweak_g2_certificate_builder"].get("strict_certificate_written") is False
        and "WZ response g2 authority absent" in statuses["wz_g2_authority_firewall"]
        and "self-normalization no-go" in statuses["wz_g2_response_self_normalization_no_go"]
        and "explicit-v authority absent" in statuses["pr230_wz_v_authority_firewall"]
        and "production rows absent" in statuses["delta_perp_tomography_builder"]
        and "orthogonal-correction gate not passed" in statuses["same_source_w_response_orthogonal_correction_gate"]
        and certs["same_source_w_response_row_builder"].get("mode") == "current"
        and certs["same_source_w_response_row_builder"].get("row_certificate_written") is False
        and not strict_presence["strict_electroweak_g2_certificate"]
        and not strict_presence["delta_perp_correction_certificate"]
        and not strict_presence["same_source_w_response_rows"]
    )
    scout_schema_not_counted = (
        "WZ smoke rows cannot be promoted" in statuses["wz_smoke_to_production_no_go"]
        and "only scout/schema and support-contract artifacts exist" in statuses["wz_packet_intake"]
        and len(scan["strict_wz_packet_row_hits"]) == 0
    )
    completion_audit_open = (
        certs["completion_audit"].get("proposal_allowed") is False
        and "retained closure not achieved" in statuses["completion_audit"]
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and completion_audit_open
    )
    prior_block_boundary_preserved = (
        certs["block114_source_higgs_strict_artifact_resolver"].get(
            "block114_source_higgs_strict_artifact_resolver_passed"
        )
        is True
        and certs["block114_source_higgs_strict_artifact_resolver"].get("proposal_allowed")
        is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("expected-strict-wz-artifact-paths-absent", not any(strict_presence.values()), str(strict_presence))
    report("accepted-same-source-action-absent", accepted_action_absent, statuses["wz_same_source_action_minimal_cut"])
    report("production-wz-response-rows-absent", production_wz_rows_absent, statuses["wz_mass_fit_response_row_builder"])
    report("matched-top-wz-covariance-absent", matched_top_wz_covariance_absent, statuses["top_wz_matched_covariance_builder"])
    report("strict-g2-delta-final-w-rows-absent", strict_g2_delta_final_w_rows_absent, statuses["same_source_w_response_row_builder"])
    report("scout-schema-not-counted-as-production", scout_schema_not_counted, str(scan))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/completion audit deny closure")
    report("prior-block114-boundary-preserved", prior_block_boundary_preserved, statuses["block114_source_higgs_strict_artifact_resolver"])
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and not any(strict_presence.values())
        and accepted_action_absent
        and production_wz_rows_absent
        and matched_top_wz_covariance_absent
        and strict_g2_delta_final_w_rows_absent
        and scout_schema_not_counted
        and aggregate_gates_open
        and prior_block_boundary_preserved
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block115 current PR230 head contains no strict "
            "W/Z physical-response packet with accepted action, production rows, matched "
            "top-W covariance, strict g2 authority, delta_perp, and final W-response rows"
        ),
        "conditional_surface_status": (
            "W/Z physical-response closure support only after a future same-surface packet "
            "supplies accepted EW/Higgs action, production W/Z rows, same-source top rows, "
            "matched covariance, strict non-observed g2 or another allowed absolute pin, "
            "delta_perp authority, and final W-response rows"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block115 is a strict artifact resolver and exact boundary. It finds only "
            "open builders, support contracts, scout/smoke/schema rows, absent strict "
            "artifact paths, and blocked g2/v shortcuts. It does not supply a W/Z "
            "physical-response packet."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block115_wz_strict_artifact_resolver_passed": passed,
        "accepted_same_source_action_absent": accepted_action_absent,
        "production_wz_response_rows_absent": production_wz_rows_absent,
        "matched_top_wz_covariance_absent": matched_top_wz_covariance_absent,
        "strict_g2_delta_final_w_rows_absent": strict_g2_delta_final_w_rows_absent,
        "scout_schema_not_counted_as_production": scout_schema_not_counted,
        "strict_artifact_presence": strict_presence,
        "candidate_scan_summary": scan,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not use observed W/Z, observed g2, observed top, or observed y_t as proof selectors",
            "does not treat scout, smoke, schema, or support-contract W/Z rows as production evidence",
            "does not use H_unit, yt_ward_identity, alpha_LM, plaquette, or u0",
            "does not set g2, delta_perp, kappa_s, c2, or Z_match by fiat",
            "does not assume matched top-W covariance or top/W factorization",
        ],
        "exact_next_action": (
            "Create a strict W/Z physical-response packet: accepted same-source EW/Higgs "
            "action certificate, production W/Z mass-fit/response rows, same-source top "
            "response rows, matched top-W covariance rows, strict non-observed g2 or "
            "another allowed absolute pin, delta_perp authority, and final W-response rows. "
            "Otherwise pivot to strict Schur/scalar-LSZ pole authority or neutral H3/H4 "
            "physical-transfer/source-coupling authority."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {rel(OUTPUT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

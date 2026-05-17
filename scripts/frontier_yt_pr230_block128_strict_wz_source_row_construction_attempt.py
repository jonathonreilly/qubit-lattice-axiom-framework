#!/usr/bin/env python3
"""
PR #230 Block128 strict W/Z and source-Higgs row construction attempt.

Block127 made the W/Z row builder consume the Block126 top-side packet.  This
runner takes the next constructive step: it tries to find genuine W/Z
production rows that can be matched to the Block126 configuration keys, and
then checks whether the fallback source-Higgs pole-row route has the accepted
O_H/action authority plus nonempty C_ss/C_sH/C_HH pole residues.

The result is a narrow obstruction when the current raw rows contain only
top/source-Higgs support plus the known W/Z scout smoke schema.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
)

BLOCK126_RAW_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_schur_higher_shell_rows/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)
SOURCE_HIGGS_RAW_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_two_source_taste_radial_rows/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)
POLEFIT_RAW_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_fh_lsz_polefit8x8/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)
WZ_SMOKE_RAW = (
    ROOT
    / "outputs"
    / "yt_pr230_wz_harness_smoke_schema_tmp"
    / "L2xT4"
    / "ensemble_measurement.json"
)

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
    "wz_smoke_to_production_no_go": (
        "outputs/yt_pr230_wz_smoke_to_production_promotion_no_go_2026-05-05.json"
    ),
    "wz_physical_response_packet_intake": (
        "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json"
    ),
    "electroweak_g2_certificate_builder": (
        "outputs/yt_electroweak_g2_certificate_builder_2026-05-05.json"
    ),
    "wz_g2_authority_firewall": "outputs/yt_wz_g2_authority_firewall_2026-05-05.json",
    "same_source_ew_action_builder": (
        "outputs/yt_wz_same_source_ew_action_certificate_builder_2026-05-04.json"
    ),
    "canonical_oh_action_lsz_closure": "outputs/yt_canonical_oh_action_lsz_closure_2026-05-12.json",
    "source_higgs_pole_row_assembly": "outputs/yt_source_higgs_pole_row_assembly_2026-05-12.json",
    "block124_completed_source_higgs_row_intake": (
        "outputs/yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json"
    ),
    "block125_post_chunk_strict_contract_resolver": (
        "outputs/yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json"
    ),
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

EXPECTED_STRICT_WZ_PATHS = {
    "wz_correlator_mass_fit_rows": "outputs/yt_wz_correlator_mass_fit_rows_2026-05-04.json",
    "wz_mass_fit_response_rows": "outputs/yt_wz_mass_fit_response_rows_2026-05-04.json",
    "fh_gauge_mass_response_measurement_rows": (
        "outputs/yt_fh_gauge_mass_response_measurement_rows_2026-05-03.json"
    ),
    "strict_g2_certificate": "outputs/yt_electroweak_g2_certificate_2026-05-04.json",
    "same_source_ew_action_certificate": "outputs/yt_wz_same_source_ew_action_certificate_2026-05-04.json",
    "top_wz_matched_covariance_certificate": (
        "outputs/yt_top_wz_matched_covariance_certificate_2026-05-04.json"
    ),
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_package_hierarchy_v": False,
    "used_scout_or_smoke_rows_as_closure": False,
    "used_finite_chunks_as_pole_rows": False,
    "assumed_top_wz_covariance_or_factorization": False,
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


def load_json(path: str | Path) -> Any:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    return json.loads(full.read_text(encoding="utf-8"))


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def finite(value: Any) -> bool:
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


def contains_nonempty_wz_mass_fit_row(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    wz = data.get("wz_mass_response_analysis", {})
    if not isinstance(wz, dict):
        return False
    rows = wz.get("per_source_shift_rows", [])
    if not isinstance(rows, list) or not rows:
        return False
    return any(
        isinstance(row, dict)
        and (
            isinstance(row.get("w_mass_fit"), dict)
            or isinstance(row.get("z_mass_fit"), dict)
        )
        for row in rows
    )


def has_disabled_wz_stub(data: Any) -> bool:
    if not isinstance(data, dict):
        return False
    wz = data.get("wz_mass_response_analysis", {})
    return isinstance(wz, dict) and wz.get("phase") == "disabled"


def source_shift_key(value: Any) -> str:
    return f"{float(value):.15g}" if finite(value) else str(value)


def has_negative_zero_positive(values: list[Any]) -> bool:
    numeric = [float(value) for value in values if finite(value)]
    return (
        any(value < 0.0 for value in numeric)
        and any(abs(value) <= 1.0e-15 for value in numeric)
        and any(value > 0.0 for value in numeric)
    )


def block126_key_summary(block126: dict[str, Any]) -> dict[str, Any]:
    packet = block126.get("matched_top_side_packet", {})
    sample_rows = packet.get("matched_rows_sample", [])
    sample_keys = []
    for row in sample_rows[:5] if isinstance(sample_rows, list) else []:
        if isinstance(row, dict):
            sample_keys.append(
                {
                    "chunk_index": row.get("chunk_index"),
                    "configuration_index": row.get("configuration_index"),
                    "selected_mass_parameter": row.get("selected_mass_parameter"),
                }
            )
    return {
        "matched_tau1_row_count": packet.get("matched_tau1_row_count"),
        "tau_slice_count": len(packet.get("per_tau_summary", {})),
        "selected_mass_parameters": packet.get("selected_mass_parameters"),
        "sample_configuration_keys": sample_keys,
    }


def validate_smoke_wz_candidate(raw: dict[str, Any], top_key_summary: dict[str, Any]) -> dict[str, Any]:
    candidate = raw.get("wz_mass_response_analysis", {}) if isinstance(raw, dict) else {}
    rows = candidate.get("per_source_shift_rows", [])
    row_shift_set = {
        source_shift_key(row.get("source_shift"))
        for row in rows
        if isinstance(row, dict) and finite(row.get("source_shift"))
    }
    source_shift_set = {
        source_shift_key(value)
        for value in candidate.get("source_shifts", [])
        if finite(value)
    }
    synthetic_sources = [
        row.get("w_mass_fit", {}).get("correlator_source")
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("w_mass_fit"), dict)
    ]
    checks = {
        "candidate_present": bool(candidate),
        "phase_is_production": candidate.get("phase") == "production",
        "same_source_coordinate": candidate.get("same_source_coordinate") is True,
        "source_shifts_neg_zero_pos": has_negative_zero_positive(
            candidate.get("source_shifts", [])
        )
        if isinstance(candidate.get("source_shifts"), list)
        else False,
        "rows_cover_source_shifts": bool(source_shift_set) and source_shift_set.issubset(row_shift_set),
        "rows_are_correlator_mass_fits": bool(rows)
        and all(
            isinstance(row, dict)
            and isinstance(row.get("w_mass_fit"), dict)
            and row.get("w_mass_fit", {}).get("from_correlator") is True
            and finite(row.get("w_mass_fit", {}).get("mass_lat"))
            and finite(row.get("w_mass_fit", {}).get("mass_lat_err"))
            for row in rows
        ),
        "not_synthetic_contract": not any("synthetic" in str(value) for value in synthetic_sources),
        "has_configuration_keys_matchable_to_block126": False,
        "has_block126_scale_row_count": len(rows) == top_key_summary.get("matched_tau1_row_count"),
        "matched_top_wz_covariance_present": finite(
            candidate.get("gauge_response", {}).get("cov_dE_top_dM_W")
            if isinstance(candidate.get("gauge_response"), dict)
            else None
        ),
        "strict_g2_present": finite(
            candidate.get("electroweak_coupling", {}).get("g2")
            if isinstance(candidate.get("electroweak_coupling"), dict)
            else None
        ),
        "identity_certificates_passed": (
            isinstance(candidate.get("identity_certificates"), dict)
            and all(value is True for value in candidate.get("identity_certificates", {}).values())
        ),
    }
    return {
        "path": rel(WZ_SMOKE_RAW),
        "row_count": len(rows) if isinstance(rows, list) else 0,
        "phase": candidate.get("phase"),
        "configuration_count_values": sorted(
            {
                row.get("configuration_count")
                for row in rows
                if isinstance(row, dict) and row.get("configuration_count") is not None
            }
        ),
        "correlator_sources": sorted({str(value) for value in synthetic_sources}),
        "checks": checks,
        "valid_for_block126_strict_join": all(checks.values()),
        "failed_checks": [key for key, ok in checks.items() if not ok],
    }


def scan_block126_raw_for_wz() -> dict[str, Any]:
    paths = sorted(ROOT.glob(BLOCK126_RAW_GLOB))
    wz_like_files: list[dict[str, Any]] = []
    disabled_stub_files = 0
    scalar_config_rows = 0
    top_config_rows = 0
    for path in paths:
        data = load_json(path)
        if contains_nonempty_wz_mass_fit_row(data):
            wz_like_files.append({"path": rel(path)})
        if has_disabled_wz_stub(data):
            disabled_stub_files += 1
        if isinstance(data, dict):
            scalar = data.get("scalar_source_response_analysis", {})
            top = data.get("top_mass_scan_response_analysis", {})
            if isinstance(scalar, dict):
                rows = scalar.get("per_configuration_slopes", [])
                scalar_config_rows += len(rows) if isinstance(rows, list) else 0
            if isinstance(top, dict):
                rows = top.get("per_configuration_slopes", [])
                top_config_rows += len(rows) if isinstance(rows, list) else 0
    return {
        "glob": BLOCK126_RAW_GLOB,
        "raw_file_count": len(paths),
        "scalar_configuration_slope_rows": scalar_config_rows,
        "top_configuration_slope_rows": top_config_rows,
        "disabled_wz_stub_file_count": disabled_stub_files,
        "wz_like_raw_file_count": len(wz_like_files),
        "wz_like_files_sample": wz_like_files[:10],
    }


def scan_source_higgs_raw() -> dict[str, Any]:
    source_paths = sorted(ROOT.glob(SOURCE_HIGGS_RAW_GLOB))
    polefit_paths = sorted(ROOT.glob(POLEFIT_RAW_GLOB))
    finite_rows = 0
    pole_residue_rows = 0
    canonical_identity_hits = 0
    alias_firewall_hits = 0
    polefit_c_ss_mode_rows = 0
    polefit_c_sh_or_c_hh_rows = 0
    for path in source_paths:
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        analysis = data.get("source_higgs_cross_correlator_analysis", {})
        if not isinstance(analysis, dict):
            continue
        mode_rows = analysis.get("mode_rows", {})
        finite_rows += len(mode_rows) if isinstance(mode_rows, dict) else 0
        pole_rows = analysis.get("pole_residue_rows", [])
        pole_residue_rows += len(pole_rows) if isinstance(pole_rows, list) else 0
        if analysis.get("canonical_higgs_operator_identity_passed") is True:
            canonical_identity_hits += 1
        aliases = analysis.get("two_source_taste_radial_row_aliases", {})
        if (
            isinstance(aliases, dict)
            and aliases.get("available") is True
            and aliases.get("C_sx_aliases_C_sH_schema_field") is True
            and aliases.get("C_xx_aliases_C_HH_schema_field") is True
        ):
            alias_firewall_hits += 1
    for path in polefit_paths:
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        scalar = data.get("scalar_two_point_lsz_analysis", {})
        if isinstance(scalar, dict):
            mode_rows = scalar.get("mode_rows", {})
            polefit_c_ss_mode_rows += len(mode_rows) if isinstance(mode_rows, dict) else 0
            for _, row in mode_rows.items() if isinstance(mode_rows, dict) else []:
                if isinstance(row, dict) and ("C_sH_real" in row or "C_HH_real" in row):
                    polefit_c_sh_or_c_hh_rows += 1
    return {
        "source_higgs_glob": SOURCE_HIGGS_RAW_GLOB,
        "source_higgs_raw_file_count": len(source_paths),
        "raw_finite_C_ss_C_sx_C_xx_row_count": finite_rows,
        "pole_residue_row_count": pole_residue_rows,
        "canonical_identity_pass_file_count": canonical_identity_hits,
        "alias_firewall_file_count": alias_firewall_hits,
        "polefit_glob": POLEFIT_RAW_GLOB,
        "polefit_raw_file_count": len(polefit_paths),
        "polefit_C_ss_mode_rows": polefit_c_ss_mode_rows,
        "polefit_C_sH_or_C_HH_mode_rows": polefit_c_sh_or_c_hh_rows,
    }


def main() -> int:
    print("PR #230 Block128 strict W/Z/source row construction attempt")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing_parents = [name for name, cert in certs.items() if not cert]
    proposal_parents = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_wz_presence = {
        name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_WZ_PATHS.items()
    }
    top_key_summary = block126_key_summary(certs["block126_matched_top_additive_subtraction_packet"])
    block126_raw_scan = scan_block126_raw_for_wz()
    smoke_validation = validate_smoke_wz_candidate(load_json(WZ_SMOKE_RAW), top_key_summary)
    source_higgs_scan = scan_source_higgs_raw()

    source_assembly = certs["source_higgs_pole_row_assembly"]
    canonical_action = certs["canonical_oh_action_lsz_closure"]
    strict_wz_constructible = (
        block126_raw_scan["wz_like_raw_file_count"] > 0
        and any(strict_wz_presence.values())
        and smoke_validation["valid_for_block126_strict_join"]
    )
    strict_source_higgs_constructible = (
        canonical_action.get("accepted_current_surface") is True
        and source_assembly.get("strict_c_ss_c_sh_c_hh_rows_exist") is True
        and source_higgs_scan["pole_residue_row_count"] > 0
    )

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("no-parent-authorizes-proposal", not proposal_parents, f"proposal_allowed={proposal_parents}")
    report(
        "block126-top-keys-available",
        top_key_summary["matched_tau1_row_count"] == 1008
        and top_key_summary["tau_slice_count"] == 23,
        str(top_key_summary),
    )
    report(
        "block126-production-raw-has-no-wz-fields",
        block126_raw_scan["raw_file_count"] == 63
        and block126_raw_scan["disabled_wz_stub_file_count"] == 63
        and block126_raw_scan["wz_like_raw_file_count"] == 0,
        str(block126_raw_scan),
    )
    report(
        "wz-smoke-not-matchable-production",
        smoke_validation["valid_for_block126_strict_join"] is False
        and "phase_is_production" in smoke_validation["failed_checks"]
        and "has_configuration_keys_matchable_to_block126" in smoke_validation["failed_checks"],
        str(smoke_validation["failed_checks"]),
    )
    report(
        "strict-wz-paths-absent",
        not any(strict_wz_presence.values()),
        str(strict_wz_presence),
    )
    report(
        "strict-g2-and-action-absent",
        certs["electroweak_g2_certificate_builder"].get("strict_certificate_written") is False
        and "g2 authority absent" in statuses["wz_g2_authority_firewall"]
        and certs["same_source_ew_action_builder"].get("proposal_allowed") is False,
        "g2/action strict certificates absent",
    )
    report(
        "source-higgs-finite-rows-not-pole-rows",
        source_higgs_scan["source_higgs_raw_file_count"] == 63
        and source_higgs_scan["raw_finite_C_ss_C_sx_C_xx_row_count"] > 0
        and certs["block124_completed_source_higgs_row_intake"]
        .get("completed_row_audit", {})
        .get("finite_row_count")
        == 693
        and source_higgs_scan["pole_residue_row_count"] == 0,
        str(source_higgs_scan),
    )
    report(
        "canonical-oh-action-authority-absent",
        canonical_action.get("accepted_current_surface") is False
        and source_assembly.get("blocked_by_canonical_o_h_authority") is True,
        str(canonical_action.get("exact_missing_primitive")),
    )
    report(
        "source-higgs-strict-construction-not-available",
        strict_source_higgs_constructible is False,
        f"strict_source_higgs_constructible={strict_source_higgs_constructible}",
    )
    report(
        "constructive-wz-construction-not-available",
        strict_wz_constructible is False,
        f"strict_wz_constructible={strict_wz_constructible}",
    )
    report(
        "claim-firewall-clean",
        all(value is False for value in FORBIDDEN_FIREWALL.values()),
        "no forbidden closure import used",
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block128 cannot construct a strict W/Z "
            "packet from existing raw rows and the source-Higgs pole-row pivot "
            "also lacks accepted O_H/action authority plus nonempty pole residues"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The Block126 production raw files have no W/Z mass-fit rows matchable "
            "to the 1008 top-side configuration keys, the only W/Z-shaped rows are "
            "the known scout smoke schema, strict g2/action certificates are absent, "
            "and the source-Higgs fallback has zero C_ss/C_sH/C_HH pole-residue rows "
            "with no accepted canonical O_H/action authority."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "block128_strict_wz_source_row_construction_attempt_passed": FAIL_COUNT == 0,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "top_key_summary": top_key_summary,
        "block126_raw_wz_scan": block126_raw_scan,
        "wz_smoke_candidate_validation": smoke_validation,
        "strict_wz_expected_path_presence": strict_wz_presence,
        "source_higgs_raw_scan": source_higgs_scan,
        "source_higgs_assembly_summary": {
            "block124_assembled_finite_row_count": certs[
                "block124_completed_source_higgs_row_intake"
            ]
            .get("completed_row_audit", {})
            .get("finite_row_count"),
            "strict_c_ss_c_sh_c_hh_rows_exist": source_assembly.get(
                "strict_c_ss_c_sh_c_hh_rows_exist"
            ),
            "blocked_by_canonical_o_h_authority": source_assembly.get(
                "blocked_by_canonical_o_h_authority"
            ),
            "blocked_by_missing_production_pole_rows": source_assembly.get(
                "blocked_by_missing_production_pole_rows"
            ),
            "exact_missing_production_fields": source_assembly.get(
                "exact_missing_production_fields", []
            ),
        },
        "canonical_action_summary": {
            "accepted_current_surface": canonical_action.get("accepted_current_surface"),
            "same_surface_cl3_z3_derived": canonical_action.get("same_surface_cl3_z3_derived"),
            "exact_missing_primitive": canonical_action.get("exact_missing_primitive"),
        },
        "constructive_status": {
            "strict_wz_constructible_from_current_raw_rows": strict_wz_constructible,
            "strict_source_higgs_constructible_from_current_raw_rows": strict_source_higgs_constructible,
            "recommended_pivot": (
                "strict Schur/Feshbach pole authority or neutral H3/H4 "
                "physical-transfer/source-coupling authority"
            ),
        },
        "strict_non_claims": {
            "does_not_use_smoke_rows_as_closure": True,
            "does_not_treat_finite_C_sx_C_xx_as_pole_residues": True,
            "does_not_assume_block126_top_rows_are_wz_rows": True,
            "does_not_use_observed_targets_or_package_v": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Do not spend another block on W/Z row inventory unless a new production "
            "W/Z mass-fit artifact appears.  Pivot to strict Schur/Feshbach pole "
            "authority or neutral H3/H4 physical-transfer/source-coupling authority; "
            "reopen source-Higgs only with accepted canonical O_H/action plus "
            "nonempty numeric C_ss/C_sH/C_HH pole-residue rows."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

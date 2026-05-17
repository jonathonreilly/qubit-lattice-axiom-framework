#!/usr/bin/env python3
"""
PR #230 Block126 matched top-side additive-subtraction packet.

The completed higher-shell raw production files contain same-configuration
source-response slopes and three-mass top-scan slopes.  This runner joins those
rows into the top-side part of the additive-subtraction contract:

    T_total = dE_top/ds,    A_top = dE_top/dm_bare,    T_minus_A = T_total - A_top.

The packet is deliberately bounded support only.  It does not supply same-source
W/Z response rows, matched top-W/Z covariance, strict non-observed g2, or an
accepted EW/Higgs action authority.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json"
)

RAW_PRODUCTION_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_schur_higher_shell_rows/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)

PARENTS = {
    "block125_post_chunk_strict_contract_resolver": (
        "outputs/yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json"
    ),
    "additive_top_subtraction_row_contract": (
        "outputs/yt_pr230_additive_top_subtraction_row_contract_2026-05-07.json"
    ),
    "top_mass_scan_subtraction_contract_applicability_audit": (
        "outputs/yt_pr230_top_mass_scan_subtraction_contract_applicability_audit_2026-05-12.json"
    ),
    "additive_top_jacobian_rows": (
        "outputs/yt_pr230_additive_top_jacobian_rows_2026-05-07.json"
    ),
    "wz_physical_response_packet_intake_checkpoint": (
        "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json"
    ),
    "top_wz_matched_covariance_certificate_builder": (
        "outputs/yt_top_wz_matched_covariance_certificate_builder_2026-05-04.json"
    ),
    "electroweak_g2_certificate_builder": (
        "outputs/yt_electroweak_g2_certificate_builder_2026-05-05.json"
    ),
    "full_positive_closure_assembly_gate": (
        "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json"
    ),
    "retained_closure_route_certificate": (
        "outputs/yt_retained_closure_route_certificate_2026-05-01.json"
    ),
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_pilots_as_production_evidence": False,
    "promoted_dE_dm_bare_to_dE_dh": False,
    "promoted_top_side_packet_to_wz_closure": False,
    "assumed_top_wz_covariance_or_factorization": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_g2_equal_one": False,
    "set_delta_perp_zero_without_certificate": False,
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


def finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def chunk_index(path: Path) -> int:
    match = re.search(r"L12_T24_chunk(\d+)", str(path))
    if not match:
        raise ValueError(f"cannot parse chunk index from {path}")
    return int(match.group(1))


def keyed_rows(rows: Any, key: str) -> dict[int, dict[str, Any]]:
    result: dict[int, dict[str, Any]] = {}
    if not isinstance(rows, list):
        return result
    for row in rows:
        if not isinstance(row, dict):
            continue
        index = row.get(key)
        if isinstance(index, int):
            result[index] = row
    return result


def numeric_summary(values: list[float]) -> dict[str, float | int | None]:
    n = len(values)
    if n == 0:
        return {"count": 0, "mean": None, "stdev": None, "stderr": None, "min": None, "max": None}
    mean = sum(values) / n
    if n > 1:
        var = sum((value - mean) ** 2 for value in values) / (n - 1)
        stdev = math.sqrt(max(var, 0.0))
        stderr = stdev / math.sqrt(n)
    else:
        stdev = 0.0
        stderr = 0.0
    return {
        "count": n,
        "mean": mean,
        "stdev": stdev,
        "stderr": stderr,
        "min": min(values),
        "max": max(values),
    }


def covariance_matrix(rows: list[dict[str, float]], keys: list[str]) -> dict[str, Any]:
    n = len(rows)
    means = {key: sum(row[key] for row in rows) / n for key in keys}
    cov: dict[str, dict[str, float]] = {key: {} for key in keys}
    for left in keys:
        for right in keys:
            if n > 1:
                value = sum(
                    (row[left] - means[left]) * (row[right] - means[right])
                    for row in rows
                ) / (n - 1)
            else:
                value = 0.0
            cov[left][right] = value
    corr: dict[str, dict[str, float | None]] = {key: {} for key in keys}
    for left in keys:
        for right in keys:
            denom = math.sqrt(max(cov[left][left], 0.0) * max(cov[right][right], 0.0))
            corr[left][right] = cov[left][right] / denom if denom > 0.0 else None
    return {"means": means, "covariance": cov, "correlation": corr}


def sample_raw_packet(paths: list[Path]) -> dict[str, Any]:
    sample = []
    for path in paths[:5]:
        data = load_json(path)
        sample.append(
            {
                "path": rel(path),
                "chunk_index": chunk_index(path),
                "selected_mass_parameter": data.get("selected_mass_parameter"),
                "scalar_tau1_rows": len(
                    data.get("scalar_source_response_analysis", {}).get(
                        "per_configuration_slopes", []
                    )
                ),
                "top_tau1_rows": len(
                    data.get("top_mass_scan_response_analysis", {}).get(
                        "per_configuration_slopes", []
                    )
                ),
            }
        )
    return {"sample": sample}


def build_packet() -> dict[str, Any]:
    paths = sorted(ROOT.glob(RAW_PRODUCTION_GLOB))
    matched_rows: list[dict[str, Any]] = []
    tau_rows: dict[str, list[dict[str, float]]] = {}
    file_summaries = []
    errors: list[dict[str, Any]] = []
    selected_masses = set()
    seed_versions = set()
    policy_selected_mass_only_true_count = 0
    top_scan_preserved_true_count = 0

    for path in paths:
        data = load_json(path)
        chunk = chunk_index(path)

        seed = data.get("rng_seed_control") if isinstance(data.get("rng_seed_control"), dict) else {}
        seed_version = seed.get("seed_control_version")
        seed_versions.add(seed_version)

        policy = (
            data.get("fh_lsz_measurement_policy")
            if isinstance(data.get("fh_lsz_measurement_policy"), dict)
            else {}
        )
        if policy.get("scalar_source_response_selected_mass_only") is True:
            policy_selected_mass_only_true_count += 1
        if policy.get("top_correlator_mass_scan_preserved") is True:
            top_scan_preserved_true_count += 1

        selected_mass = data.get("selected_mass_parameter", policy.get("selected_mass_parameter"))
        if finite_number(selected_mass):
            selected_masses.add(float(selected_mass))

        scalar = (
            data.get("scalar_source_response_analysis")
            if isinstance(data.get("scalar_source_response_analysis"), dict)
            else {}
        )
        top = (
            data.get("top_mass_scan_response_analysis")
            if isinstance(data.get("top_mass_scan_response_analysis"), dict)
            else {}
        )

        scalar_tau1 = keyed_rows(scalar.get("per_configuration_slopes"), "configuration_index")
        top_tau1 = keyed_rows(top.get("per_configuration_slopes"), "configuration_index")
        scalar_multi = keyed_rows(
            scalar.get("per_configuration_multi_tau_slopes"), "configuration_index"
        )
        top_multi = keyed_rows(top.get("per_configuration_multi_tau_slopes"), "configuration_index")

        matched_configs = sorted(set(scalar_tau1) & set(top_tau1))
        file_summaries.append(
            {
                "path": rel(path),
                "chunk_index": chunk,
                "scalar_tau1_rows": len(scalar_tau1),
                "top_tau1_rows": len(top_tau1),
                "matched_configuration_rows": len(matched_configs),
                "selected_mass_parameter": selected_mass,
                "seed_control_version": seed_version,
                "scalar_source_response_selected_mass_only": policy.get(
                    "scalar_source_response_selected_mass_only"
                ),
                "top_correlator_mass_scan_preserved": policy.get(
                    "top_correlator_mass_scan_preserved"
                ),
            }
        )

        for cfg in matched_configs:
            scalar_row = scalar_tau1[cfg]
            top_row = top_tau1[cfg]
            t_total = scalar_row.get("slope_effective_energy_tau1")
            a_top = top_row.get("slope_dE_dm_bare_tau1")
            if not (finite_number(t_total) and finite_number(a_top)):
                errors.append(
                    {
                        "path": rel(path),
                        "chunk_index": chunk,
                        "configuration_index": cfg,
                        "error": "nonfinite tau1 matched row",
                    }
                )
                continue

            row = {
                "chunk_index": chunk,
                "configuration_index": cfg,
                "selected_mass_parameter": selected_mass,
                "seed_control_version": seed_version,
                "T_total_dE_ds_tau1": float(t_total),
                "A_top_dE_dm_bare_tau1": float(a_top),
                "T_minus_A_tau1": float(t_total) - float(a_top),
                "source_radius": scalar_row.get("source_radius"),
                "top_bracket_masses_lat": top_row.get("bracket_masses_lat"),
            }
            matched_rows.append(row)

            scalar_by_tau = scalar_multi.get(cfg, {}).get("slope_effective_energy_by_tau", {})
            top_by_tau = top_multi.get(cfg, {}).get("slope_dE_dm_bare_by_tau", {})
            if isinstance(scalar_by_tau, dict) and isinstance(top_by_tau, dict):
                for tau in sorted(set(scalar_by_tau) & set(top_by_tau), key=lambda x: int(x)):
                    t_tau = scalar_by_tau.get(tau)
                    a_tau = top_by_tau.get(tau)
                    if finite_number(t_tau) and finite_number(a_tau):
                        tau_rows.setdefault(str(tau), []).append(
                            {
                                "T_total_dE_ds": float(t_tau),
                                "A_top_dE_dm_bare": float(a_tau),
                                "T_minus_A": float(t_tau) - float(a_tau),
                            }
                        )

    stat_rows = [
        {
            "T_total_dE_ds_tau1": row["T_total_dE_ds_tau1"],
            "A_top_dE_dm_bare_tau1": row["A_top_dE_dm_bare_tau1"],
            "T_minus_A_tau1": row["T_minus_A_tau1"],
        }
        for row in matched_rows
    ]
    cov = covariance_matrix(
        stat_rows,
        ["T_total_dE_ds_tau1", "A_top_dE_dm_bare_tau1", "T_minus_A_tau1"],
    ) if stat_rows else {"means": {}, "covariance": {}, "correlation": {}}

    per_tau_summary = {}
    for tau, rows in sorted(tau_rows.items(), key=lambda item: int(item[0])):
        tau_cov = covariance_matrix(
            rows,
            ["T_total_dE_ds", "A_top_dE_dm_bare", "T_minus_A"],
        )
        per_tau_summary[tau] = {
            "row_count": len(rows),
            "T_total_dE_ds": numeric_summary([row["T_total_dE_ds"] for row in rows]),
            "A_top_dE_dm_bare": numeric_summary([row["A_top_dE_dm_bare"] for row in rows]),
            "T_minus_A": numeric_summary([row["T_minus_A"] for row in rows]),
            "cov_T_A": tau_cov["covariance"]["T_total_dE_ds"]["A_top_dE_dm_bare"],
            "corr_T_A": tau_cov["correlation"]["T_total_dE_ds"]["A_top_dE_dm_bare"],
        }

    variance_identity_lhs = cov.get("covariance", {}).get("T_minus_A_tau1", {}).get(
        "T_minus_A_tau1", 0.0
    )
    covariance = cov.get("covariance", {})
    variance_identity_rhs = (
        covariance.get("T_total_dE_ds_tau1", {}).get("T_total_dE_ds_tau1", 0.0)
        + covariance.get("A_top_dE_dm_bare_tau1", {}).get("A_top_dE_dm_bare_tau1", 0.0)
        - 2.0
        * covariance.get("T_total_dE_ds_tau1", {}).get("A_top_dE_dm_bare_tau1", 0.0)
    )
    variance_identity_abs_error = abs(variance_identity_lhs - variance_identity_rhs)

    return {
        "raw_file_count": len(paths),
        "expected_raw_file_count": 63,
        "raw_packet_sample": sample_raw_packet(paths),
        "file_summaries_sample": file_summaries[:5],
        "matched_tau1_row_count": len(matched_rows),
        "expected_matched_tau1_row_count": 63 * 16,
        "selected_mass_parameters": sorted(selected_masses),
        "seed_control_versions": sorted(str(value) for value in seed_versions),
        "policy_selected_mass_only_true_count": policy_selected_mass_only_true_count,
        "top_correlator_mass_scan_preserved_true_count": top_scan_preserved_true_count,
        "match_errors": errors,
        "tau1_summary": {
            "T_total_dE_ds_tau1": numeric_summary(
                [row["T_total_dE_ds_tau1"] for row in matched_rows]
            ),
            "A_top_dE_dm_bare_tau1": numeric_summary(
                [row["A_top_dE_dm_bare_tau1"] for row in matched_rows]
            ),
            "T_minus_A_tau1": numeric_summary(
                [row["T_minus_A_tau1"] for row in matched_rows]
            ),
            "matched_covariance": cov,
            "variance_identity_check": {
                "var_T_minus_A": variance_identity_lhs,
                "var_T_plus_var_A_minus_2cov_T_A": variance_identity_rhs,
                "absolute_error": variance_identity_abs_error,
                "passed": variance_identity_abs_error < 1e-14,
            },
        },
        "per_tau_summary": per_tau_summary,
        "matched_rows_sample": matched_rows[:10],
    }


def parent_statuses(certs: dict[str, dict[str, Any]]) -> dict[str, str]:
    return {
        key: str(value.get("actual_current_surface_status", "missing"))
        for key, value in certs.items()
    }


def main() -> int:
    print("PR #230 Block126 matched top-side additive-subtraction packet")
    print("=" * 72)

    certs = {key: load_json(path) for key, path in PARENTS.items()}
    packet = build_packet()

    strict_subtraction_contract_state = {
        "top_side_same_configuration_rows_present": packet["matched_tau1_row_count"] == 63 * 16,
        "top_side_multi_tau_rows_present": all(
            summary.get("row_count") == 63 * 16
            for summary in packet["per_tau_summary"].values()
        )
        and len(packet["per_tau_summary"]) == 23,
        "top_side_covariance_computed": bool(
            packet["tau1_summary"]["matched_covariance"].get("covariance")
        ),
        "wz_rows_present": False,
        "matched_top_wz_covariance_present": False,
        "strict_non_observed_g2_present": False,
        "accepted_same_source_ew_action_present": False,
        "accepted_canonical_higgs_or_overlap_present": False,
        "contract_satisfied_now": False,
    }

    report(
        "raw-files-complete",
        packet["raw_file_count"] == 63,
        f"{packet['raw_file_count']} raw production files",
    )
    report(
        "seed-control-preserved",
        packet["seed_control_versions"] == ["numba_gauge_seed_v1"],
        str(packet["seed_control_versions"]),
    )
    report(
        "selected-mass-policy-preserved",
        packet["policy_selected_mass_only_true_count"] == 63
        and packet["top_correlator_mass_scan_preserved_true_count"] == 63,
        (
            f"scalar selected-mass-only files={packet['policy_selected_mass_only_true_count']}; "
            f"top mass scan preserved files={packet['top_correlator_mass_scan_preserved_true_count']}"
        ),
    )
    report(
        "selected-mass-is-middle-0p75",
        packet["selected_mass_parameters"] == [0.75],
        str(packet["selected_mass_parameters"]),
    )
    report(
        "matched-tau1-row-count",
        packet["matched_tau1_row_count"] == packet["expected_matched_tau1_row_count"],
        f"{packet['matched_tau1_row_count']} matched top-side tau1 rows",
    )
    report(
        "matched-multitau-coverage",
        strict_subtraction_contract_state["top_side_multi_tau_rows_present"],
        f"{len(packet['per_tau_summary'])} tau slices with full same-config matching",
    )
    report(
        "top-side-covariance-computed",
        strict_subtraction_contract_state["top_side_covariance_computed"]
        and packet["tau1_summary"]["variance_identity_check"]["passed"],
        "tau1 covariance matrix plus exact T-A variance identity",
    )
    report(
        "wz-action-g2-still-absent",
        strict_subtraction_contract_state["wz_rows_present"] is False
        and strict_subtraction_contract_state["matched_top_wz_covariance_present"] is False
        and strict_subtraction_contract_state["strict_non_observed_g2_present"] is False
        and strict_subtraction_contract_state["accepted_same_source_ew_action_present"] is False,
        "top-side packet does not supply W/Z rows, matched top-W/Z covariance, strict g2, or action",
    )
    report(
        "no-closure-claim",
        all(value is False for value in FORBIDDEN_FIREWALL.values())
        and strict_subtraction_contract_state["contract_satisfied_now"] is False,
        "bounded support only; no retained/proposed_retained claim",
    )
    report(
        "parents-still-block-closure",
        certs["block125_post_chunk_strict_contract_resolver"].get("proposal_allowed") is False
        and certs["additive_top_subtraction_row_contract"].get(
            "current_surface_contract_satisfied"
        )
        is False
        and "WZ physical-response packet not present"
        in str(
            certs["wz_physical_response_packet_intake_checkpoint"].get(
                "actual_current_surface_status", ""
            )
        ),
        "parent row contract and W/Z intake remain open/negative",
    )

    result = {
        "actual_current_surface_status": (
            "bounded-support / Block126 constructs matched top-side additive-subtraction "
            "rows from completed PR230 chunks; W/Z response, matched top-W/Z covariance, "
            "strict g2, and accepted action remain absent"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The packet retires only the top-side same-configuration matching gap. "
            "It does not produce W/Z response rows, matched top-W/Z covariance, strict "
            "non-observed g2, or accepted same-source EW/Higgs action authority."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "current_closure_satisfied": False,
        "block126_matched_top_additive_subtraction_packet_passed": FAIL_COUNT == 0,
        "parent_certificates": PARENTS,
        "parent_statuses": parent_statuses(certs),
        "matched_top_side_packet": packet,
        "strict_subtraction_contract_state": strict_subtraction_contract_state,
        "strict_non_claims": {
            "does_not_treat_dE_dm_bare_as_dE_dh": True,
            "does_not_use_observed_top_mass_or_yukawa": True,
            "does_not_use_observed_wz_or_g2": True,
            "does_not_supply_wz_response_rows": True,
            "does_not_supply_matched_top_wz_covariance": True,
            "does_not_supply_accepted_same_source_action": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Run genuine same-source W/Z response production under the same scalar source, "
            "join it with these top-side rows into matched top-W/Z covariance, and supply "
            "strict non-observed g2 plus accepted same-source EW/Higgs action authority. "
            "Without those rows this packet remains bounded support only."
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

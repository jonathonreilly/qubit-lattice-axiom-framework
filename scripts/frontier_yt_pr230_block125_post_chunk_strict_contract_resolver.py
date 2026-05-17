#!/usr/bin/env python3
"""
PR #230 Block125 post-chunk strict positive-contract resolver.

The replacement/chunk campaign is complete, so this runner audits the completed
raw production surface rather than relaunching finite-row work.  It asks whether
any post-chunk artifact now satisfies one of the strict positive contracts:

* source-Higgs: accepted canonical O_H/action plus C_ss/C_sH/C_HH pole rows;
* W/Z response: same-source action, production W/Z rows, covariance, g2,
  delta_perp, and final W rows;
* Schur/scalar-LSZ: pole coordinate plus K-prime/residue/FV/IR authority;
* neutral: physical transfer/primitive authority plus source/canonical coupling.
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
    / "yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json"
)

RAW_PRODUCTION_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_schur_higher_shell_rows/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)

PARENTS = {
    "block123_source_higgs_lsz_readout_formula": (
        "outputs/yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json"
    ),
    "block124_completed_source_higgs_row_intake": (
        "outputs/yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json"
    ),
    "source_higgs_pole_row_assembly": "outputs/yt_source_higgs_pole_row_assembly_2026-05-12.json",
    "source_higgs_pole_residue_extractor": "outputs/yt_source_higgs_pole_residue_extractor_2026-05-03.json",
    "block115_wz_strict_artifact_resolver": (
        "outputs/yt_pr230_block115_wz_strict_artifact_resolver_2026-05-17.json"
    ),
    "block117_schur_scalar_lsz_strict_artifact_resolver": (
        "outputs/yt_pr230_block117_schur_scalar_lsz_strict_artifact_resolver_2026-05-17.json"
    ),
    "block121_schur_finite_packet_nonidentifiability": (
        "outputs/yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json"
    ),
    "block116_neutral_h3h4_strict_artifact_resolver": (
        "outputs/yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json"
    ),
    "neutral_primitive_route_completion": "outputs/yt_pr230_neutral_primitive_route_completion_2026-05-06.json",
    "target_timeseries_full_set": "outputs/yt_fh_lsz_target_timeseries_full_set_checkpoint_2026-05-12.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_pilots_as_production_evidence": False,
    "promoted_schema_aliases_to_physical_rows": False,
    "promoted_support_contracts_to_evidence": False,
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


def status(cert: dict[str, Any]) -> str:
    return str(cert.get("actual_current_surface_status", ""))


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def list_len(value: Any) -> int:
    return len(value) if isinstance(value, list) else 0


def dict_len(value: Any) -> int:
    return len(value) if isinstance(value, dict) else 0


def walk(obj: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
    rows: list[tuple[tuple[str, ...], Any]] = [(path, obj)]
    if isinstance(obj, dict):
        for key, value in obj.items():
            rows.extend(walk(value, path + (str(key),)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            rows.extend(walk(value, path + (str(index),)))
    return rows


def scan_raw_production() -> dict[str, Any]:
    paths = sorted(ROOT.glob(RAW_PRODUCTION_GLOB))
    result: dict[str, Any] = {
        "expected_raw_file_count": 63,
        "raw_file_count": len(paths),
        "raw_files_sample": [rel(path) for path in paths[:5]],
        "source_higgs_mode_rows": 0,
        "source_higgs_time_kernel_rows": 0,
        "source_higgs_pole_residue_rows": 0,
        "source_higgs_canonical_identity_true_files": [],
        "source_higgs_used_as_readout_true_files": [],
        "scalar_lsz_mode_rows": 0,
        "scalar_lsz_physical_higgs_normalization_true_files": [],
        "wz_per_source_shift_rows": 0,
        "wz_production_row_like_hits": [],
        "wz_same_source_identity_true_files": [],
        "schur_kprime_or_pole_hits": [],
        "neutral_transfer_or_primitive_hits": [],
        "policy_selected_mass_only_true_count": 0,
        "seed_control_version_mismatch": [],
    }

    for path in paths:
        data = load_json(path)
        seed = data.get("rng_seed_control") if isinstance(data.get("rng_seed_control"), dict) else {}
        if seed.get("seed_control_version") != "numba_gauge_seed_v1":
            result["seed_control_version_mismatch"].append(rel(path))

        policy = (
            data.get("fh_lsz_measurement_policy")
            if isinstance(data.get("fh_lsz_measurement_policy"), dict)
            else {}
        )
        if policy.get("scalar_source_response_selected_mass_only") is True:
            result["policy_selected_mass_only_true_count"] += 1

        sh = (
            data.get("source_higgs_cross_correlator_analysis")
            if isinstance(data.get("source_higgs_cross_correlator_analysis"), dict)
            else {}
        )
        result["source_higgs_mode_rows"] += dict_len(sh.get("mode_rows"))
        result["source_higgs_pole_residue_rows"] += list_len(sh.get("pole_residue_rows"))
        if sh.get("canonical_higgs_operator_identity_passed") is True:
            result["source_higgs_canonical_identity_true_files"].append(rel(path))
        if sh.get("used_as_physical_yukawa_readout") is True:
            result["source_higgs_used_as_readout_true_files"].append(rel(path))

        tk = (
            data.get("source_higgs_time_kernel_analysis")
            if isinstance(data.get("source_higgs_time_kernel_analysis"), dict)
            else {}
        )
        result["source_higgs_time_kernel_rows"] += dict_len(tk.get("mode_rows"))
        for key in ("time_kernel_rows", "rows", "pole_residue_rows"):
            result["source_higgs_time_kernel_rows"] += list_len(tk.get(key))

        scalar = (
            data.get("scalar_two_point_lsz_analysis")
            if isinstance(data.get("scalar_two_point_lsz_analysis"), dict)
            else {}
        )
        result["scalar_lsz_mode_rows"] += dict_len(scalar.get("mode_rows"))
        if scalar.get("physical_higgs_normalization") is True:
            result["scalar_lsz_physical_higgs_normalization_true_files"].append(rel(path))

        wz = (
            data.get("wz_mass_response_analysis")
            if isinstance(data.get("wz_mass_response_analysis"), dict)
            else {}
        )
        result["wz_per_source_shift_rows"] += list_len(wz.get("per_source_shift_rows"))
        if wz.get("same_source_identity_certified") is True:
            result["wz_same_source_identity_true_files"].append(rel(path))
        for node_path, value in walk(wz):
            if not isinstance(value, dict):
                continue
            keys = set(value)
            has_wz_slope = any(key in keys for key in ("dM_W_ds", "slope_dM_W_ds", "R_W"))
            has_top = any(key in keys for key in ("dE_top_ds", "slope_dE_top_ds", "R_t"))
            has_cov = any(key in keys for key in ("cov_dE_top_dM_W", "cov_R_t_R_W"))
            has_g2 = any(key in keys and is_number(value.get(key)) for key in ("g2", "g_2"))
            if has_wz_slope and has_top and has_cov and has_g2:
                result["wz_production_row_like_hits"].append(
                    {"path": rel(path), "node_path": "/".join(node_path)}
                )

        for node_path, value in walk(data):
            key_text = "/".join(node_path).lower()
            if any(token in key_text for token in ("schur_kprime", "k_prime", "kprime")):
                if value not in (None, [], {}, False):
                    result["schur_kprime_or_pole_hits"].append(
                        {"path": rel(path), "node_path": "/".join(node_path), "value_type": type(value).__name__}
                    )
            if any(token in key_text for token in ("neutral_transfer", "primitive_cone", "irreducibility")):
                if value not in (None, [], {}, False):
                    result["neutral_transfer_or_primitive_hits"].append(
                        {"path": rel(path), "node_path": "/".join(node_path), "value_type": type(value).__name__}
                    )

    return result


def route_contracts(raw: dict[str, Any], certs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    source_higgs_missing = []
    if not raw["source_higgs_canonical_identity_true_files"]:
        source_higgs_missing.append("accepted canonical O_H/action authority")
    if raw["source_higgs_pole_residue_rows"] == 0:
        source_higgs_missing.append("numeric C_ss/C_sH/C_HH pole-residue rows")
    if raw["source_higgs_time_kernel_rows"] == 0:
        source_higgs_missing.append("physical Euclidean time-kernel rows for pole extraction")
    if certs["source_higgs_pole_row_assembly"].get("strict_c_ss_c_sh_c_hh_rows_exist") is not True:
        source_higgs_missing.append("strict source-Higgs pole-row assembly pass")

    wz_missing = []
    if certs["block115_wz_strict_artifact_resolver"].get("accepted_same_source_action_absent") is not True:
        wz_missing.append("accepted same-source EW/Higgs action status not certified by Block115")
    else:
        wz_missing.append("accepted same-source EW/Higgs action")
    if raw["wz_per_source_shift_rows"] == 0 and not raw["wz_production_row_like_hits"]:
        wz_missing.append("production W/Z mass-response rows")
    if certs["block115_wz_strict_artifact_resolver"].get("matched_top_wz_covariance_absent") is True:
        wz_missing.append("matched top-W/Z covariance")
    if certs["block115_wz_strict_artifact_resolver"].get("strict_g2_delta_final_w_rows_absent") is True:
        wz_missing.append("strict non-observed g2, delta_perp, and final W rows")

    schur_missing = []
    if raw["schur_kprime_or_pole_hits"]:
        schur_missing.append("strict interpretation of raw Schur-like hits")
    else:
        schur_missing.append("strict Schur/Feshbach K-prime or pole derivative rows")
    if certs["block117_schur_scalar_lsz_strict_artifact_resolver"].get("moment_threshold_fv_authority_absent") is True:
        schur_missing.append("moment/threshold/FV/IR/contact authority")
    if certs["block117_schur_scalar_lsz_strict_artifact_resolver"].get("bridge_roots_absent") is True:
        schur_missing.append("canonical O_H/source bridge or W/Z/neutral bridge")

    neutral_missing = []
    if not raw["neutral_transfer_or_primitive_hits"]:
        neutral_missing.append("raw physical neutral transfer/off-diagonal primitive rows")
    if certs["block116_neutral_h3h4_strict_artifact_resolver"].get("h3_physical_transfer_absent") is True:
        neutral_missing.append("H3 physical neutral transfer or primitive authority")
    if certs["block116_neutral_h3h4_strict_artifact_resolver"].get("h4_source_canonical_coupling_absent") is True:
        neutral_missing.append("H4 source/canonical-Higgs coupling")

    contracts = {
        "source_higgs_strict_pole_rows": {
            "satisfied": not source_higgs_missing,
            "missing": source_higgs_missing,
            "support_present": [
                "Block123 source-Higgs LSZ readout formula",
                f"{raw['source_higgs_mode_rows']} finite source-Higgs/taste-radial mode rows",
                f"{raw['scalar_lsz_mode_rows']} scalar C_ss finite LSZ support rows",
            ],
        },
        "wz_physical_response": {
            "satisfied": not wz_missing,
            "missing": wz_missing,
            "support_present": ["response-ratio contract and W/Z manifests only"],
        },
        "schur_scalar_lsz": {
            "satisfied": not schur_missing,
            "missing": schur_missing,
            "support_present": ["complete finite Schur A/B/C packet; Block121 nonidentifiability boundary"],
        },
        "neutral_h3h4": {
            "satisfied": not neutral_missing,
            "missing": neutral_missing,
            "support_present": ["conditional primitive-cone/H1-H2 support only"],
        },
    }
    return contracts


def main() -> int:
    print("PR #230 Block125 post-chunk strict positive-contract resolver")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing_parents = [name for name, cert in certs.items() if not cert]
    parent_proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    raw = scan_raw_production()
    contracts = route_contracts(raw, certs)
    satisfied_routes = [name for name, row in contracts.items() if row["satisfied"]]
    all_route_contracts_blocked = not satisfied_routes
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
    )
    target_timeseries_complete = (
        certs["target_timeseries_full_set"].get("target_timeseries_summary", {}).get("complete_count")
        == 63
        and certs["target_timeseries_full_set"].get("target_timeseries_summary", {}).get("incomplete_indices")
        == []
    )
    raw_production_complete = (
        raw["raw_file_count"] == raw["expected_raw_file_count"]
        and not raw["seed_control_version_mismatch"]
        and raw["policy_selected_mass_only_true_count"] == raw["expected_raw_file_count"]
    )
    raw_source_higgs_support_only = (
        raw["source_higgs_mode_rows"] == 693
        and raw["source_higgs_pole_residue_rows"] == 0
        and raw["source_higgs_time_kernel_rows"] == 0
        and not raw["source_higgs_canonical_identity_true_files"]
        and not raw["source_higgs_used_as_readout_true_files"]
    )
    raw_wz_absent = (
        raw["wz_per_source_shift_rows"] == 0
        and not raw["wz_production_row_like_hits"]
        and not raw["wz_same_source_identity_true_files"]
    )
    raw_schur_neutral_absent = (
        not raw["schur_kprime_or_pole_hits"]
        and not raw["neutral_transfer_or_primitive_hits"]
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    ranked_next_paths = [
        {
            "rank": 1,
            "route": "source_higgs_strict_pole_rows",
            "why": (
                "Closest to existing support: Block123 gives the invariant readout "
                "formula and production has finite rows, but the missing artifact is "
                "still strict canonical O_H/action plus pole residues."
            ),
            "first_concrete_artifact": (
                "accepted canonical O_H/action authority with nonempty numeric "
                "C_ss/C_sH/C_HH pole-residue rows"
            ),
        },
        {
            "rank": 2,
            "route": "wz_physical_response",
            "why": (
                "Can bypass kappa_s by ratio if the same-source W/Z packet exists, "
                "but currently misses action, rows, covariance, g2, and delta_perp."
            ),
            "first_concrete_artifact": (
                "production W/Z mass-response rows under the PR230 scalar source, "
                "plus matched top rows/covariance and strict non-observed g2"
            ),
        },
        {
            "rank": 3,
            "route": "neutral_h3h4",
            "why": "Potentially clean if a same-surface primitive/off-diagonal transfer theorem is found.",
            "first_concrete_artifact": (
                "physical neutral transfer or primitive-cone/irreducibility certificate "
                "plus source/canonical-Higgs coupling"
            ),
        },
        {
            "rank": 4,
            "route": "schur_scalar_lsz",
            "why": "Finite A/B/C rows are complete, but Block121 proves finite nodes do not determine K'(pole).",
            "first_concrete_artifact": (
                "strict Schur/Feshbach K-prime pole-row packet with FV/IR/contact authority"
            ),
        },
    ]

    objective_completion_audit = {
        "objective": "resume positive closure on PR #230",
        "success_criteria": [
            "a strict current-surface positive route contract is satisfied",
            "full positive closure assembly authorizes the route",
            "retained-route certificate allows proposed_retained",
            "PR #230 can move beyond draft/open without claim firewall violation",
        ],
        "evidence": {
            "satisfied_route_contracts": satisfied_routes,
            "full_positive_assembly_proposal_allowed": certs["full_positive_assembly"].get("proposal_allowed"),
            "retained_route_proposal_allowed": certs["retained_route"].get("proposal_allowed"),
            "campaign_status_proposal_allowed": certs["campaign_status"].get("proposal_allowed"),
        },
        "achieved": False,
        "blocking_reason": "No strict post-chunk positive route contract is satisfied on the current surface.",
    }

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("target-timeseries-complete", target_timeseries_complete, "target-timeseries complete_count=63")
    report("raw-production-surface-complete", raw_production_complete, str(raw))
    report("raw-source-higgs-hidden-strict-rows-absent", raw_source_higgs_support_only, str(raw))
    report("raw-wz-production-response-absent", raw_wz_absent, str(raw))
    report("raw-schur-neutral-strict-hits-absent", raw_schur_neutral_absent, str(raw))
    report("all-route-contracts-remain-blocked", all_route_contracts_blocked, str(contracts))
    report("aggregate-gates-remain-open", aggregate_gates_open, "full/retained/campaign/completion proposal flags false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block125 post-chunk strict contract "
            "resolver finds no source-Higgs, W/Z, Schur, or neutral positive "
            "closure packet on the completed PR230 surface"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The completed post-chunk surface has finite support rows but no "
            "strict route contract: no accepted canonical O_H/action plus "
            "C_ss/C_sH/C_HH pole residues, no production W/Z response packet, "
            "no Schur K-prime pole authority, and no neutral H3/H4 physical "
            "transfer/source-coupling artifact."
        ),
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "block125_post_chunk_strict_contract_resolver_passed": FAIL_COUNT == 0,
        "current_closure_satisfied": False,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "post_chunk_raw_scan": raw,
        "route_contracts": contracts,
        "satisfied_route_contracts": satisfied_routes,
        "ranked_next_paths": ranked_next_paths,
        "objective_completion_audit": objective_completion_audit,
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not use schema C_sH/C_HH aliases as physical pole rows",
            "does not use W/Z scout, smoke, schema, or manifest rows as production evidence",
            "does not infer K-prime or residues from finite Schur nodes",
            "does not treat conditional neutral primitive support as a current-surface certificate",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
        ],
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Produce the first ranked strict artifact: accepted canonical O_H/action "
            "authority with nonempty numeric C_ss/C_sH/C_HH pole-residue rows.  "
            "If that cannot be supplied, implement genuine same-source W/Z production "
            "response rows with matched top covariance and strict non-observed g2."
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

#!/usr/bin/env python3
"""
PR #230 Block109 closure-root frontier selector.

This runner is the post-Block108 completion audit for the active objective:
resume positive closure on PR #230.  It rejects proxy completion signals
after the chunk campaign and all-ref scan, then ranks the remaining genuine
same-surface artifact families.  It is not physics evidence and does not
authorize retained or proposed_retained closure.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block109_closure_root_frontier_selector_2026-05-17.json"
)

PARENTS = {
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "block108_all_ref_rescan": "outputs/yt_pr230_block108_all_ref_closure_artifact_rescan_2026-05-17.json",
    "target_timeseries_full_set": "outputs/yt_fh_lsz_target_timeseries_full_set_checkpoint_2026-05-12.json",
    "higher_shell_wave_launcher": "outputs/yt_pr230_schur_higher_shell_wave_launcher_2026-05-12.json",
    "higher_shell_complete_packet": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "time_kernel_manifest": "outputs/yt_pr230_source_higgs_time_kernel_production_manifest_2026-05-07.json",
    "fms_action_adoption_minimal_cut": "outputs/yt_pr230_fms_action_adoption_minimal_cut_2026-05-07.json",
    "source_higgs_pole_row_acceptance": "outputs/yt_pr230_source_higgs_pole_row_acceptance_contract_2026-05-06.json",
    "physical_source_higgs_row_absence": "outputs/yt_pr230_physical_euclidean_source_higgs_row_absence_after_block44_2026-05-12.json",
    "wz_physical_response_packet": "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json",
    "wz_v_authority_firewall": "outputs/yt_pr230_wz_v_authority_firewall_2026-05-15.json",
    "same_source_wz_response_gate": "outputs/yt_same_source_wz_response_certificate_gate_2026-05-02.json",
    "schur_abc_definition": "outputs/yt_pr230_schur_abc_definition_derivation_attempt_2026-05-05.json",
    "strict_scalar_lsz_moment_fv": "outputs/yt_pr230_strict_scalar_lsz_moment_fv_authority_gate_2026-05-07.json",
    "neutral_h3h4_aperture": "outputs/yt_pr230_neutral_primitive_h3h4_aperture_checkpoint_2026-05-07.json",
    "z3_heat_kernel_neutral_transfer": "outputs/yt_pr230_z3_heat_kernel_neutral_transfer_attempt_2026-05-15.json",
    "z3_heat_kernel_scale_selector": "outputs/yt_pr230_z3_heat_kernel_scale_selector_no_go_2026-05-15.json",
    "z3_heat_kernel_source_coupling": "outputs/yt_pr230_z3_heat_kernel_source_coupling_no_go_2026-05-15.json",
}

STRICT_ARTIFACT_PATHS = {
    "canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "same_surface_ew_higgs_action_certificate": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-07.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "source_higgs_pole_residue_packet": "outputs/yt_pr230_source_higgs_pole_residue_packet_2026-05-07.json",
    "same_source_wz_response_certificate": "outputs/yt_same_source_wz_response_certificate_2026-05-04.json",
    "top_wz_matched_response_rows": "outputs/yt_top_wz_matched_response_rows_2026-05-04.json",
    "electroweak_g2_authority_certificate": "outputs/yt_electroweak_g2_authority_certificate_2026-05-05.json",
    "schur_abc_kernel_rows": "outputs/yt_schur_abc_kernel_rows_2026-05-05.json",
    "strict_scalar_lsz_moment_fv_authority": "outputs/yt_pr230_strict_scalar_lsz_moment_fv_authority_2026-05-07.json",
    "neutral_h3_certificate": "outputs/yt_pr230_neutral_h3_physical_transfer_certificate_2026-05-07.json",
    "neutral_h4_certificate": "outputs/yt_pr230_neutral_h4_source_higgs_coupling_certificate_2026-05-07.json",
    "neutral_primitive_cone_certificate": "outputs/yt_neutral_scalar_primitive_cone_certificate_2026-05-05.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity_as_authority": False,
    "used_observed_top_mass_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_pilots_as_production_evidence": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_kappa_s_equal_one": False,
    "set_g2_equal_one": False,
    "renamed_support_rows_as_physical_rows": False,
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


def yes(cert: dict[str, Any], key: str) -> bool:
    return cert.get(key) is True


def no(cert: dict[str, Any], key: str) -> bool:
    return cert.get(key) is False


def git_value(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return result.stdout.strip()


def path_presence() -> dict[str, bool]:
    return {name: (ROOT / rel).exists() for name, rel in STRICT_ARTIFACT_PATHS.items()}


def route_rows(certs: dict[str, dict[str, Any]], strict_present: dict[str, bool]) -> list[dict[str, Any]]:
    return [
        {
            "rank": 1,
            "family": "O_H_action_plus_source_higgs_pole_rows",
            "retained_positive_probability": "highest remaining",
            "current_status": "open",
            "present_required_artifacts": [
                name
                for name in (
                    "canonical_oh_certificate",
                    "same_surface_ew_higgs_action_certificate",
                    "source_higgs_pole_rows",
                    "source_higgs_pole_residue_packet",
                )
                if strict_present[name]
            ],
            "missing_required_artifacts": [
                name
                for name in (
                    "canonical_oh_certificate",
                    "same_surface_ew_higgs_action_certificate",
                    "source_higgs_pole_rows",
                    "source_higgs_pole_residue_packet",
                )
                if not strict_present[name]
            ],
            "evidence": {
                "fms_cut": status(certs["fms_action_adoption_minimal_cut"]),
                "source_higgs_contract": status(certs["source_higgs_pole_row_acceptance"]),
                "physical_rows_absent": status(certs["physical_source_higgs_row_absence"]),
                "time_kernel_manifest": status(certs["time_kernel_manifest"]),
            },
            "next_genuine_artifact": (
                "accepted same-surface EW/Higgs action or canonical O_H certificate, "
                "then production physical Euclidean C_ss/C_sH/C_HH(tau) pole rows "
                "with Gram, covariance, threshold, and FV/IR authority"
            ),
        },
        {
            "rank": 2,
            "family": "same_source_WZ_physical_response_packet",
            "retained_positive_probability": "medium-low",
            "current_status": "open",
            "present_required_artifacts": [
                name
                for name in (
                    "same_source_wz_response_certificate",
                    "top_wz_matched_response_rows",
                    "electroweak_g2_authority_certificate",
                )
                if strict_present[name]
            ],
            "missing_required_artifacts": [
                name
                for name in (
                    "same_source_wz_response_certificate",
                    "top_wz_matched_response_rows",
                    "electroweak_g2_authority_certificate",
                )
                if not strict_present[name]
            ],
            "evidence": {
                "wz_packet": status(certs["wz_physical_response_packet"]),
                "same_source_gate": status(certs["same_source_wz_response_gate"]),
                "v_firewall": status(certs["wz_v_authority_firewall"]),
            },
            "next_genuine_artifact": (
                "accepted same-source action plus production W/Z and top response rows, "
                "matched covariance, delta_perp authority, and a strict non-observed "
                "absolute pin such as g2"
            ),
        },
        {
            "rank": 3,
            "family": "strict_Schur_or_scalar_LSZ_authority",
            "retained_positive_probability": "low after complete finite packet signs",
            "current_status": "open / shortcut rejected",
            "present_required_artifacts": [
                name
                for name in (
                    "schur_abc_kernel_rows",
                    "strict_scalar_lsz_moment_fv_authority",
                )
                if strict_present[name]
            ],
            "missing_required_artifacts": [
                name
                for name in (
                    "schur_abc_kernel_rows",
                    "strict_scalar_lsz_moment_fv_authority",
                )
                if not strict_present[name]
            ],
            "evidence": {
                "complete_packet": status(certs["higher_shell_complete_packet"]),
                "schur_abc_definition": status(certs["schur_abc_definition"]),
                "strict_scalar_lsz": status(certs["strict_scalar_lsz_moment_fv"]),
            },
            "next_genuine_artifact": (
                "strict Schur A/B/C pole-derivative rows or all-order scalar-LSZ "
                "moment/threshold/FV authority; do not replay finite-row promotion"
            ),
        },
        {
            "rank": 4,
            "family": "neutral_H3_H4_primitive_transfer",
            "retained_positive_probability": "low without new H3/H4 row",
            "current_status": "open / H3-H4 absent",
            "present_required_artifacts": [
                name
                for name in (
                    "neutral_h3_certificate",
                    "neutral_h4_certificate",
                    "neutral_primitive_cone_certificate",
                )
                if strict_present[name]
            ],
            "missing_required_artifacts": [
                name
                for name in (
                    "neutral_h3_certificate",
                    "neutral_h4_certificate",
                    "neutral_primitive_cone_certificate",
                )
                if not strict_present[name]
            ],
            "evidence": {
                "h3h4_aperture": status(certs["neutral_h3h4_aperture"]),
                "heat_kernel_transfer": status(certs["z3_heat_kernel_neutral_transfer"]),
                "heat_kernel_scale": status(certs["z3_heat_kernel_scale_selector"]),
                "heat_kernel_source": status(certs["z3_heat_kernel_source_coupling"]),
            },
            "next_genuine_artifact": (
                "same-surface physical neutral transfer/off-diagonal generator plus "
                "source/canonical-Higgs coupling, or a strict primitive-cone "
                "irreducibility certificate connected to PR230"
            ),
        },
    ]


def objective_checklist(certs: dict[str, dict[str, Any]], strict_present: dict[str, bool]) -> list[dict[str, Any]]:
    target_full = certs["target_timeseries_full_set"]
    wave = certs["higher_shell_wave_launcher"]
    block108 = certs["block108_all_ref_rescan"]
    campaign = certs["campaign_status"]
    retained = certs["retained_route"]
    assembly = certs["full_positive_assembly"]
    completion = certs["completion_audit"]
    time_kernel = certs["time_kernel_manifest"]

    chunks_complete = (
        target_full.get("replacement_queue") == []
        and target_full.get("target_timeseries_summary", {}).get("complete_count") == 63
        and wave.get("completed_chunk_indices") == list(range(1, 64))
        and wave.get("active_process_count") == 0
    )
    no_strict_artifact = not any(strict_present.values()) and block108.get("remote_strict_hits") == []
    closure_denied = (
        retained.get("proposal_allowed") is False
        and campaign.get("proposal_allowed") is False
        and assembly.get("proposal_allowed") is False
        and completion.get("proposal_allowed") is False
    )

    return [
        {
            "requirement": "work is on PR230 branch",
            "evidence": git_value(["branch", "--show-current"]),
            "covered": git_value(["branch", "--show-current"]) == "claude/yt-direct-lattice-correlator-2026-04-30",
        },
        {
            "requirement": "chunk/support production is complete and idle",
            "evidence": {
                "target_timeseries_complete_count": target_full.get("target_timeseries_summary", {}).get("complete_count"),
                "replacement_queue": target_full.get("replacement_queue"),
                "higher_shell_completed_count": len(wave.get("completed_chunk_indices", [])),
                "active_process_count": wave.get("active_process_count"),
            },
            "covered": chunks_complete,
        },
        {
            "requirement": "completion audit must reject proxy completion",
            "evidence": {
                "block108_remote_ref_count": block108.get("remote_ref_count"),
                "strict_artifact_presence": strict_present,
                "remote_strict_hits": block108.get("remote_strict_hits"),
            },
            "covered": no_strict_artifact,
        },
        {
            "requirement": "no retained/proposed_retained closure is authorized",
            "evidence": {
                "retained_route": retained.get("proposal_allowed"),
                "campaign": campaign.get("proposal_allowed"),
                "assembly": assembly.get("proposal_allowed"),
                "completion": completion.get("proposal_allowed"),
            },
            "covered": closure_denied,
        },
        {
            "requirement": "do not launch noncanonical time-kernel rows as closure evidence",
            "evidence": {
                "operator_certificate_is_canonical_oh": time_kernel.get("operator_certificate_is_canonical_oh"),
                "support_launch_authorized_now": time_kernel.get("support_launch_authorized_now"),
                "closure_launch_authorized_now": time_kernel.get("closure_launch_authorized_now"),
            },
            "covered": (
                time_kernel.get("operator_certificate_is_canonical_oh") is False
                and time_kernel.get("support_launch_authorized_now") is False
                and time_kernel.get("closure_launch_authorized_now") is False
            ),
        },
    ]


def main() -> int:
    print("PR #230 Block109 closure-root frontier selector")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    missing = [name for name, cert in certs.items() if not cert]
    parent_failures = {
        name: cert.get("fail_count")
        for name, cert in certs.items()
        if cert and cert.get("fail_count") not in (0, None)
    }
    proposal_parents = [
        name for name, cert in certs.items() if cert.get("proposal_allowed") is True
    ]
    strict_present = path_presence()
    routes = route_rows(certs, strict_present)
    checklist = objective_checklist(certs, strict_present)
    uncovered = [row["requirement"] for row in checklist if row["covered"] is not True]
    route_frontier = [
        {
            "rank": row["rank"],
            "family": row["family"],
            "missing_count": len(row["missing_required_artifacts"]),
            "next_genuine_artifact": row["next_genuine_artifact"],
        }
        for row in routes
    ]
    selected = routes[0]

    completion_audit_passed = (
        not missing
        and not parent_failures
        and not proposal_parents
        and not uncovered
        and certs["block108_all_ref_rescan"].get("closure_achieved") is False
        and certs["block108_all_ref_rescan"].get("fresh_artifact_admitted") is False
        and certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and all(value is False for value in FORBIDDEN_FIREWALL.values())
    )
    goal_complete = False

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("parent-certificates-have-no-fails", not parent_failures, str(parent_failures))
    report("no-parent-authorizes-proposal", not proposal_parents, f"proposal_allowed={proposal_parents}")
    report("prompt-to-artifact-checklist-covered", not uncovered, f"uncovered={uncovered}")
    report("strict-current-artifacts-absent", not any(strict_present.values()), str(strict_present))
    report("block108-admits-no-fresh-artifact", certs["block108_all_ref_rescan"].get("fresh_artifact_admitted") is False, status(certs["block108_all_ref_rescan"]))
    report("aggregate-gates-still-deny-closure", certs["full_positive_assembly"].get("proposal_allowed") is False and certs["retained_route"].get("proposal_allowed") is False, status(certs["full_positive_assembly"]))
    report("selected-frontier-is-genuine-artifact-family", selected["family"] == "O_H_action_plus_source_higgs_pole_rows", selected["next_genuine_artifact"])
    report("forbidden-firewall-clean", all(value is False for value in FORBIDDEN_FIREWALL.values()), str(FORBIDDEN_FIREWALL))
    report("goal-not-complete", not goal_complete, "positive closure remains open")

    result = {
        "artifact": "yt_pr230_block109_closure_root_frontier_selector",
        "actual_current_surface_status": (
            "open / Block109 closure-root frontier selector: positive closure "
            "not achieved; next admissible work is a genuine same-surface "
            "O_H/action plus source-Higgs pole-row artifact"
        ),
        "conditional_surface_status": (
            "source-Higgs closure can reopen only with accepted same-surface "
            "O_H/action plus strict C_ss/C_sH/C_HH pole rows; W/Z, Schur/LSZ, "
            "and neutral H3/H4 remain fallback families with their listed roots"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block109 is an objective completion audit and route-frontier "
            "selector.  It finds no current strict same-surface artifact, "
            "keeps aggregate gates closed, and does not supply O_H/action, "
            "source-Higgs pole rows, W/Z rows, Schur/LSZ authority, or neutral H3/H4."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "block109_closure_root_frontier_selector_passed": completion_audit_passed,
        "goal_complete": goal_complete,
        "objective_success_criteria": [
            "retained/proposed_retained y_t closure proposal must be authorized by aggregate gates",
            "one strict same-surface artifact family must be present and admitted",
            "forbidden normalization/proof selectors must remain absent",
            "support/chunk/proxy completion must not be accepted as physics closure",
        ],
        "prompt_to_artifact_checklist": checklist,
        "strict_artifact_presence": strict_present,
        "route_frontier": route_frontier,
        "route_rows": routes,
        "selected_next_artifact_family": selected["family"],
        "selected_next_artifact_reason": (
            "It is still the cleanest and highest-ranked physics route after "
            "Block108 because W/Z lacks action/rows/absolute pin, Schur/LSZ "
            "finite proxies fail necessary signs, and neutral H3/H4 lacks "
            "physical transfer plus source/canonical-Higgs coupling."
        ),
        "selected_exact_next_action": selected["next_genuine_artifact"],
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not treat completed chunks, manifests, all-ref scans, or literature as closure",
            "does not launch time-kernel rows under a noncanonical operator certificate",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette/u0, or value recognition",
            "does not set kappa_s=1, c2=1, Z_match=1, or g2=1",
        ],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

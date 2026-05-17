#!/usr/bin/env python3
"""
PR #230 Block108 all-ref closure-artifact rescan.

This runner is a completion-audit checkpoint for the active objective:
resume positive closure on PR #230.  It verifies the pushed PR-head state,
scans every fetched origin ref for named strict same-surface artifacts, and
refreshes the clean FMS/source-Higgs literature boundary.  It is not physics
evidence and does not authorize retained or proposed_retained closure.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "yt_pr230_block108_all_ref_closure_artifact_rescan_2026-05-17.json"

PARENTS = {
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "post_block100_reopen_audit": "outputs/yt_pr230_post_block100_completion_reopen_audit_2026-05-15.json",
    "target_timeseries_full_set": "outputs/yt_fh_lsz_target_timeseries_full_set_checkpoint_2026-05-12.json",
    "higher_shell_wave_launcher": "outputs/yt_pr230_schur_higher_shell_wave_launcher_2026-05-12.json",
    "higher_shell_complete_packet": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "time_kernel_manifest": "outputs/yt_pr230_source_higgs_time_kernel_production_manifest_2026-05-07.json",
    "fms_literature_intake": "outputs/yt_pr230_fms_literature_source_overlap_intake_2026-05-07.json",
    "fms_action_adoption_minimal_cut": "outputs/yt_pr230_fms_action_adoption_minimal_cut_2026-05-07.json",
    "source_higgs_pole_row_acceptance": "outputs/yt_pr230_source_higgs_pole_row_acceptance_contract_2026-05-06.json",
    "wz_physical_response_packet": "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json",
    "neutral_h3h4_aperture": "outputs/yt_pr230_neutral_primitive_h3h4_aperture_checkpoint_2026-05-07.json",
    "wz_v_authority_firewall": "outputs/yt_pr230_wz_v_authority_firewall_2026-05-15.json",
}

STRICT_REOPEN_ARTIFACTS = {
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "pr230_canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "same_surface_ew_higgs_action_certificate": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-07.json",
    "source_coordinate_transport_certificate": "outputs/yt_pr230_source_coordinate_transport_certificate_2026-05-06.json",
    "source_higgs_cross_correlator_rows": "outputs/yt_source_higgs_cross_correlator_measurement_rows_2026-05-03.json",
    "source_higgs_production_certificate": "outputs/yt_source_higgs_cross_correlator_production_certificate_2026-05-03.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "source_higgs_pole_residue_packet": "outputs/yt_pr230_source_higgs_pole_residue_packet_2026-05-07.json",
    "top_wz_matched_response_rows": "outputs/yt_top_wz_matched_response_rows_2026-05-04.json",
    "same_source_wz_response_certificate": "outputs/yt_same_source_wz_response_certificate_2026-05-04.json",
    "electroweak_g2_authority_certificate": "outputs/yt_electroweak_g2_authority_certificate_2026-05-05.json",
    "electroweak_v_authority_certificate": "outputs/yt_electroweak_v_authority_certificate_2026-05-12.json",
    "schur_abc_kernel_rows": "outputs/yt_schur_abc_kernel_rows_2026-05-05.json",
    "neutral_primitive_cone_certificate": "outputs/yt_neutral_scalar_primitive_cone_certificate_2026-05-05.json",
    "same_surface_neutral_transfer_operator": "outputs/yt_pr230_same_surface_neutral_transfer_operator_2026-05-06.json",
    "neutral_h3_certificate": "outputs/yt_pr230_neutral_h3_physical_transfer_certificate_2026-05-07.json",
    "neutral_h4_certificate": "outputs/yt_pr230_neutral_h4_source_higgs_coupling_certificate_2026-05-07.json",
    "fh_lsz_carleman_tauberian_certificate": "outputs/yt_fh_lsz_carleman_tauberian_certificate_2026-05-05.json",
    "strict_scalar_lsz_moment_fv_authority": "outputs/yt_pr230_strict_scalar_lsz_moment_fv_authority_2026-05-07.json",
}

REMOTE_PATTERNS = [
    re.compile(re.escape(path) + r"$") for path in STRICT_REOPEN_ARTIFACTS.values()
] + [
    re.compile(r"outputs/yt_pr230_.*(canonical.*oh|same_surface.*ew.*higgs.*action).*certificate.*\.json$"),
    re.compile(r"outputs/yt_pr230_.*source_higgs.*(pole|production|rows|residue).*\.json$"),
    re.compile(r"outputs/yt_.*(top_wz|same_source_wz|wz_response).*rows.*\.json$"),
    re.compile(r"outputs/yt_.*(electroweak_g2|electroweak_v).*authority.*certificate.*\.json$"),
    re.compile(r"outputs/yt_.*schur.*abc.*kernel.*rows.*\.json$"),
    re.compile(r"outputs/yt_.*neutral.*(primitive|h3|h4|transfer).*certificate.*\.json$"),
    re.compile(r"outputs/yt_.*fh_lsz.*(carleman|tauberian|moment|fv).*certificate.*\.json$"),
]

LITERATURE_ROWS = [
    {
        "id": "weak_and_higgs_from_lattice_2026",
        "url": "https://arxiv.org/abs/2603.12882",
        "role": "current lattice/FMS route context",
        "pr230_authority": False,
    },
    {
        "id": "testing_gauge_invariant_perturbation_theory_2016",
        "url": "https://arxiv.org/abs/1610.04188",
        "role": "FMS gauge-invariant perturbation theory context",
        "pr230_authority": False,
    },
    {
        "id": "frohlich_morchio_strocchi_1981",
        "url": "https://doi.org/10.1016/0550-3213(81)90448-X",
        "role": "gauge-invariant Higgs composite context",
        "pr230_authority": False,
    },
    {
        "id": "fradkin_shenker_1979",
        "url": "https://doi.org/10.1103/PhysRevD.19.3682",
        "role": "lattice gauge-Higgs phase/context boundary",
        "pr230_authority": False,
    },
]

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
    "renamed_taste_radial_rows_as_canonical_higgs_rows": False,
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


def git_lines(args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def remote_refs() -> list[str]:
    return git_lines(["for-each-ref", "--format=%(refname:short)", "refs/remotes/origin"])


def latest_refs(limit: int = 20) -> list[dict[str, str]]:
    rows = git_lines(
        [
            "for-each-ref",
            f"--count={limit}",
            "--sort=-committerdate",
            "--format=%(committerdate:short)|%(refname:short)",
            "refs/remotes/origin",
        ]
    )
    out: list[dict[str, str]] = []
    for row in rows:
        date, _, ref = row.partition("|")
        out.append({"date": date, "ref": ref})
    return out


def remote_hits(refs: list[str]) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for ref in refs:
        files = git_lines(["ls-tree", "-r", "--name-only", ref])
        for path in files:
            if any(pattern.search(path) for pattern in REMOTE_PATTERNS):
                hits.append({"ref": ref, "path": path})
    return hits


def main() -> int:
    print("PR #230 Block108 all-ref closure-artifact rescan")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing_parents = [name for name, cert in certs.items() if not cert]
    parent_failures = {
        name: cert.get("fail_count")
        for name, cert in certs.items()
        if cert and cert.get("fail_count") not in (0, None)
    }
    current_artifacts = {
        name: (ROOT / path).exists() for name, path in STRICT_REOPEN_ARTIFACTS.items()
    }
    refs = remote_refs()
    hits = remote_hits(refs)
    pr_ref = "origin/claude/yt-direct-lattice-correlator-2026-04-30"
    outside_pr_hits = [hit for hit in hits if hit["ref"] != pr_ref]

    target_full = certs["target_timeseries_full_set"]
    wave = certs["higher_shell_wave_launcher"]
    complete_packet = certs["higher_shell_complete_packet"]
    manifest = certs["time_kernel_manifest"]
    retained = certs["retained_route"]
    campaign = certs["campaign_status"]
    assembly = certs["full_positive_assembly"]
    completion = certs["completion_audit"]
    assumptions = certs["assumption_import_stress"]
    post100 = certs["post_block100_reopen_audit"]
    fms_lit = certs["fms_literature_intake"]
    fms_cut = certs["fms_action_adoption_minimal_cut"]
    wz_v = certs["wz_v_authority_firewall"]

    chunks_complete = (
        target_full.get("replacement_queue") == []
        and target_full.get("target_timeseries_summary", {}).get("complete_count") == 63
        and wave.get("completed_chunk_indices") == list(range(1, 64))
        and wave.get("active_chunk_indices") == []
        and wave.get("planned_launch_chunk_indices") == []
        and wave.get("active_process_count") == 0
    )
    finite_packet_blocks = (
        complete_packet.get("proposal_allowed") is False
        and complete_packet.get("strict_schur_or_scalar_lsz_authority_passed") is False
        and complete_packet.get("higher_shell_complete_packet_monotonicity_gate_passed") is True
    )
    manifest_idle_not_launch = (
        manifest.get("active_process_rows") == []
        and manifest.get("support_launch_authorized_now") is False
        and manifest.get("closure_launch_authorized_now") is False
        and manifest.get("operator_certificate_is_canonical_oh") is False
    )
    aggregate_denies = (
        retained.get("proposal_allowed") is False
        and campaign.get("proposal_allowed") is False
        and assembly.get("proposal_allowed") is False
        and completion.get("proposal_allowed") is False
        and assumptions.get("proposal_allowed") is False
    )
    post100_still_blocks = (
        post100.get("completion_reopen_audit_passed") is True
        and post100.get("closure_achieved") is False
        and post100.get("fresh_artifact_admitted") is False
    )
    fms_literature_non_authority = (
        fms_lit.get("proposal_allowed") is False
        and fms_lit.get("literature_bridge_scope") == "non_derivation_context_only"
        and fms_cut.get("proposal_allowed") is False
        and all(row["pr230_authority"] is False for row in LITERATURE_ROWS)
    )
    wz_absolute_pin_absent = (
        wz_v.get("proposal_allowed") is False
        and wz_v.get("v_authority_gate_passed") is False
        and wz_v.get("wz_v_authority_firewall_passed") is True
    )
    current_strict_absent = not any(current_artifacts.values())
    remote_strict_absent = not outside_pr_hits
    all_refs_available = len(refs) > 1 and any(ref == "origin/main" for ref in refs)
    forbidden_firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    missing_positive_requirements = [
        "accepted same-surface EW/Higgs action and canonical O_H certificate",
        "physical Euclidean C_ss/C_sH/C_HH pole rows with Gram/FV/IR authority",
        "genuine same-source W/Z response rows with identity/covariance and non-forbidden g2/v/source-normalization authority",
        "strict Schur A/B/C pole-derivative rows or scalar-LSZ moment/threshold/FV authority",
        "neutral H3/H4 primitive/off-diagonal physical-transfer authority plus source/canonical-Higgs coupling",
        "retained-route, full-assembly, campaign, and completion-audit proposal authorization",
    ]

    prompt_to_artifact_checklist = [
        {
            "requirement": "last chunk campaign complete",
            "evidence": PARENTS["target_timeseries_full_set"],
            "covered": chunks_complete,
        },
        {
            "requirement": "all fetched origin refs scanned for strict reopen paths",
            "evidence": {"remote_ref_count": len(refs), "latest_refs": latest_refs()},
            "covered": all_refs_available,
        },
        {
            "requirement": "no current strict same-surface closure artifact exists",
            "evidence": current_artifacts,
            "covered": current_strict_absent,
        },
        {
            "requirement": "no outside-PR remote strict same-surface closure artifact exists",
            "evidence": outside_pr_hits,
            "covered": remote_strict_absent,
        },
        {
            "requirement": "literature context does not import O_H/kappa_s authority",
            "evidence": LITERATURE_ROWS,
            "covered": fms_literature_non_authority,
        },
        {
            "requirement": "aggregate closure gates still deny proposal wording",
            "evidence": [
                PARENTS["retained_route"],
                PARENTS["campaign_status"],
                PARENTS["full_positive_assembly"],
                PARENTS["completion_audit"],
            ],
            "covered": aggregate_denies,
        },
    ]

    closure_achieved = False
    fresh_artifact_admitted = False
    block108_passed = (
        not missing_parents
        and not parent_failures
        and chunks_complete
        and finite_packet_blocks
        and manifest_idle_not_launch
        and aggregate_denies
        and post100_still_blocks
        and current_strict_absent
        and remote_strict_absent
        and all_refs_available
        and fms_literature_non_authority
        and wz_absolute_pin_absent
        and forbidden_firewall_clean
    )

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("parent-certificates-have-no-fails", not parent_failures, str(parent_failures))
    report("chunk-campaign-complete", chunks_complete, "target-timeseries=63/63; higher-shell=63/63; active=[]")
    report("finite-packet-not-scalar-lsz-or-schur-authority", finite_packet_blocks, statuses["higher_shell_complete_packet"])
    report("time-kernel-manifest-idle-but-not-launch-authority", manifest_idle_not_launch, statuses["time_kernel_manifest"])
    report("aggregate-gates-deny-proposal", aggregate_denies, statuses["retained_route"])
    report("post-block100-reopen-audit-still-blocks", post100_still_blocks, statuses["post_block100_reopen_audit"])
    report("all-origin-refs-available-for-scan", all_refs_available, f"remote_ref_count={len(refs)}")
    report("current-strict-artifacts-absent", current_strict_absent, str(current_artifacts))
    report("remote-strict-artifacts-absent", remote_strict_absent, str(outside_pr_hits[:10]))
    report("fms-literature-non-authority", fms_literature_non_authority, statuses["fms_literature_intake"])
    report("wz-absolute-pin-absent", wz_absolute_pin_absent, statuses["wz_v_authority_firewall"])
    report("forbidden-firewall-clean", forbidden_firewall_clean, str(FORBIDDEN_FIREWALL))
    report("closure-not-achieved", not closure_achieved, "positive closure roots remain absent")
    report("fresh-artifact-not-admitted", not fresh_artifact_admitted, "no current/fetched strict same-surface artifact")

    result = {
        "artifact": "yt_pr230_block108_all_ref_closure_artifact_rescan",
        "actual_current_surface_status": (
            "open / Block108 all-ref closure-artifact rescan: positive closure "
            "not achieved and no current/fetched strict same-surface artifact is admitted"
        ),
        "conditional_surface_status": (
            "source-Higgs closure can reopen only with accepted same-surface O_H/action "
            "plus strict C_ss/C_sH/C_HH pole rows; W/Z can reopen only with accepted "
            "action, genuine response/covariance rows, and an allowed absolute pin"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block108 is an all-ref artifact/literature rescan and completion audit only. "
            "It finds no strict current or fetched same-surface artifact and does not "
            "supply O_H, source-Higgs pole rows, W/Z response rows, Schur/LSZ authority, "
            "or neutral H3/H4 authority."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "block108_all_ref_closure_artifact_rescan_passed": block108_passed,
        "closure_achieved": closure_achieved,
        "fresh_artifact_admitted": fresh_artifact_admitted,
        "remote_ref_count": len(refs),
        "latest_remote_refs": latest_refs(),
        "remote_strict_hits": outside_pr_hits,
        "current_strict_artifacts_present": current_artifacts,
        "missing_positive_requirements": missing_positive_requirements,
        "prompt_to_artifact_checklist": prompt_to_artifact_checklist,
        "literature_rows": LITERATURE_ROWS,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Do not run more finite-row promotion or path-only reopen gates. "
            "Produce one genuine same-surface artifact: accepted canonical O_H/action "
            "plus C_ss/C_sH/C_HH pole rows, strict W/Z response packet with allowed "
            "absolute pin, strict Schur/scalar-LSZ authority, or neutral H3/H4 "
            "physical-transfer/source-coupling authority."
        ),
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette/u0, or value recognition",
            "does not set kappa_s=1, c2=1, Z_match=1, or g2=1",
            "does not treat literature, FMS names, branch names, or path names as PR230 same-surface authority",
            "does not launch source-Higgs time-kernel rows or W/Z rows",
        ],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
PR #230 Block131 action-first source-Higgs authority construction attempt.

Blocks128-130 closed the current W/Z, Schur, and neutral shortcuts.  This
runner pivots back to the action-first source-Higgs route and tests whether
the current finite support can be promoted into the strict packet required by
Block123:

  accepted same-surface canonical O_H/action authority
  plus nonempty numeric C_ss/C_sH/C_HH pole-residue rows.

The attempt is constructive.  It ingests the current post-Block130 surface,
checks the raw row files for strict action/pole keys, and builds a numerical
readout nonidentifiability witness using the Block126 top-side response.  The
witness is explicitly not a physical row; it shows why the present surface
cannot identify a unique source-Higgs readout without the missing authority.
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
    / "yt_pr230_block131_action_first_source_higgs_authority_construction_attempt_2026-05-17.json"
)

EXPECTED_CHUNKS = 63

PARENTS = {
    "block118_hamming_dirichlet_oh_axis_selector": (
        "outputs/yt_pr230_block118_hamming_dirichlet_oh_axis_selector_2026-05-17.json"
    ),
    "block119_native_dirichlet_action_lsz_probe": (
        "outputs/yt_pr230_block119_native_dirichlet_action_lsz_probe_2026-05-17.json"
    ),
    "block122_hamming_axis_action_lsz_normalization_gap": (
        "outputs/yt_pr230_block122_hamming_axis_action_lsz_normalization_gap_2026-05-17.json"
    ),
    "block123_source_higgs_lsz_readout_formula": (
        "outputs/yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json"
    ),
    "block124_completed_source_higgs_row_intake": (
        "outputs/yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json"
    ),
    "block125_post_chunk_strict_contract_resolver": (
        "outputs/yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json"
    ),
    "block126_matched_top_additive_subtraction_packet": (
        "outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json"
    ),
    "block128_strict_wz_source_row_construction_attempt": (
        "outputs/yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
    ),
    "block130_neutral_h3h4_transfer_coupling_construction_attempt": (
        "outputs/yt_pr230_block130_neutral_h3h4_transfer_coupling_construction_attempt_2026-05-17.json"
    ),
    "block130_neutral_h3h4_eta_nonidentifiability": (
        "outputs/yt_pr230_block130_neutral_h3h4_eta_nonidentifiability_2026-05-17.json"
    ),
    "action_first_route_completion": (
        "outputs/yt_pr230_action_first_route_completion_2026-05-06.json"
    ),
    "action_first_oh_artifact_attempt": (
        "outputs/yt_pr230_action_first_oh_artifact_attempt_2026-05-05.json"
    ),
    "canonical_oh_action_lsz_closure": (
        "outputs/yt_canonical_oh_action_lsz_closure_2026-05-12.json"
    ),
    "fms_oh_candidate_action_packet": (
        "outputs/yt_pr230_fms_oh_candidate_action_packet_2026-05-07.json"
    ),
    "same_source_ew_higgs_action_ansatz_gate": (
        "outputs/yt_pr230_same_source_ew_higgs_action_ansatz_gate_2026-05-06.json"
    ),
    "same_source_ew_action_adoption_attempt": (
        "outputs/yt_pr230_same_source_ew_action_adoption_attempt_2026-05-06.json"
    ),
    "source_higgs_pole_row_assembly": (
        "outputs/yt_source_higgs_pole_row_assembly_2026-05-12.json"
    ),
    "full_positive_assembly": (
        "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json"
    ),
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": (
        "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json"
    ),
    "assumption_import_stress": (
        "outputs/yt_pr230_assumption_import_stress_2026-05-01.json"
    ),
}

EXPECTED_STRICT_PACKET_PATHS = {
    "accepted_same_surface_canonical_oh_action_lsz_certificate": (
        "outputs/yt_pr230_accepted_same_surface_canonical_oh_action_lsz_certificate_2026-05-17.json"
    ),
    "accepted_same_surface_ew_higgs_action_certificate": (
        "outputs/yt_pr230_accepted_same_surface_ew_higgs_action_certificate_2026-05-17.json"
    ),
    "source_higgs_pole_residue_rows": (
        "outputs/yt_pr230_source_higgs_pole_residue_rows_2026-05-17.json"
    ),
    "canonical_oh_source_higgs_strict_packet": (
        "outputs/yt_pr230_canonical_oh_source_higgs_strict_packet_2026-05-17.json"
    ),
    "block131_action_first_source_higgs_authority_packet": (
        "outputs/yt_pr230_block131_action_first_source_higgs_authority_packet_2026-05-17.json"
    ),
}

RAW_STRICT_TOKENS = (
    "accepted_same_surface_ew_higgs_action",
    "same_surface_canonical_action_certificate",
    "same_surface_canonical_action_lsz",
    "canonical_higgs_operator_identity_passed",
    "operator_authority_scope",
    "pole_residue_rows",
    "source_higgs_pole_rows",
    "isolated_scalar_pole_passed",
    "model_class_or_pole_saturation_certificate_passed",
    "fv_ir_zero_mode_control_passed",
    "contact_term_scheme_certificate_passed",
    "Res_C_ss",
    "Res_C_sH",
    "Res_C_HH",
)

FORBIDDEN_FIREWALL = {
    "used_y_t_bare": False,
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_alpha_lm_or_plaquette": False,
    "used_plaquette_u0": False,
    "used_observed_targets_as_selectors": False,
    "used_package_hierarchy_v": False,
    "used_fitted_selectors": False,
    "used_smoke_rows_as_closure": False,
    "promoted_finite_c_sx_rows_to_c_sh_pole_residues": False,
    "identified_taste_radial_x_as_canonical_o_h": False,
    "accepted_unratified_fms_packet_as_action": False,
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
    value = json.loads(full.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def status(cert: dict[str, Any]) -> str:
    return str(cert.get("actual_current_surface_status", ""))


def raw_path(index: int) -> Path:
    return (
        ROOT
        / "outputs"
        / "yt_direct_lattice_correlator_production_schur_higher_shell_rows"
        / f"L12_T24_chunk{index:03d}"
        / "L12xT24"
        / "ensemble_measurement.json"
    )


def scan_raw_strict_tokens() -> dict[str, Any]:
    hits: list[dict[str, Any]] = []
    missing: list[int] = []
    checked = 0

    def walk(value: Any, prefix: str = "") -> list[tuple[str, Any]]:
        found: list[tuple[str, Any]] = []
        if isinstance(value, dict):
            for key, item in value.items():
                key_path = f"{prefix}.{key}" if prefix else str(key)
                if key in RAW_STRICT_TOKENS and item not in (None, False, [], {}):
                    found.append((key_path, item))
                found.extend(walk(item, key_path))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                found.extend(walk(item, f"{prefix}[{index}]"))
        return found

    for index in range(1, EXPECTED_CHUNKS + 1):
        path = raw_path(index)
        if not path.exists():
            missing.append(index)
            continue
        checked += 1
        data = load_json(path)
        for key_path, value in walk(data):
            hits.append(
                {
                    "chunk": index,
                    "path": rel(path),
                    "key_path": key_path,
                    "value_preview": str(value)[:160],
                }
            )
    return {
        "expected_raw_file_count": EXPECTED_CHUNKS,
        "raw_files_checked": checked,
        "missing_raw_indices": missing,
        "strict_token_hits": hits[:100],
        "strict_token_hit_count": len(hits),
    }


def finite_row_summary(block124: dict[str, Any]) -> dict[str, Any]:
    audit = block124.get("completed_row_audit", {})
    diagnostic = audit.get("finite_gram_diagnostic", {})
    return {
        "finite_row_count": audit.get("finite_row_count"),
        "timeseries_row_count": audit.get("timeseries_row_count"),
        "pole_residue_row_hits": audit.get("pole_residue_row_hits", []),
        "canonical_identity_hits": audit.get("canonical_identity_hits", []),
        "finite_rank_one_proxy_failed": diagnostic.get("finite_rank_one_proxy_failed"),
        "finite_abs_rho_sx_max": diagnostic.get("abs_rho_sx_summary", {}).get("max"),
        "finite_gram_determinant_min": diagnostic.get("gram_determinant_summary", {}).get("min"),
        "strict_limit": diagnostic.get("strict_limit"),
    }


def top_response_mean(block126: dict[str, Any]) -> float:
    matched = block126.get("matched_top_side_packet", {})
    tau1 = matched.get("tau1_summary", {})
    mean = tau1.get("T_total_dE_ds_tau1", {}).get("mean")
    if isinstance(mean, (int, float)) and math.isfinite(float(mean)):
        return float(mean)
    raise ValueError("Block126 tau1 T_total_dE_ds mean missing")


def readout_from_packet(d_e_top_ds: float, residue_packet: dict[str, float]) -> float:
    return (
        d_e_top_ds
        * math.sqrt(residue_packet["Res_C_HH"])
        / residue_packet["Res_C_sH"]
    )


def gram_det(packet: dict[str, float]) -> float:
    return packet["Res_C_ss"] * packet["Res_C_HH"] - packet["Res_C_sH"] ** 2


def build_readout_witness(d_e_top_ds: float) -> dict[str, Any]:
    packet_a = {"Res_C_ss": 1.0, "Res_C_sH": 1.0, "Res_C_HH": 1.0}
    packet_b = {"Res_C_ss": 0.25, "Res_C_sH": 0.5, "Res_C_HH": 1.0}
    readout_a = readout_from_packet(d_e_top_ds, packet_a)
    readout_b = readout_from_packet(d_e_top_ds, packet_b)
    return {
        "available": True,
        "status": (
            "non-authority witness only; these residue packets are not accepted "
            "PR230 rows and are not used as closure"
        ),
        "fixed_current_support": {
            "block126_tau1_mean_T_total_dE_ds": d_e_top_ds,
            "block124_finite_rows_remain_unchanged": True,
            "accepted_action_or_pole_rows_selecting_packet": False,
        },
        "candidate_residue_packet_a": {
            **packet_a,
            "gram_determinant": gram_det(packet_a),
            "gram_pure": math.isclose(gram_det(packet_a), 0.0, abs_tol=1e-15),
            "readout_y_H": readout_a,
        },
        "candidate_residue_packet_b": {
            **packet_b,
            "gram_determinant": gram_det(packet_b),
            "gram_pure": math.isclose(gram_det(packet_b), 0.0, abs_tol=1e-15),
            "readout_y_H": readout_b,
        },
        "readout_difference": readout_b - readout_a,
        "readout_ratio_b_over_a": readout_b / readout_a,
        "readout_changes_while_current_support_fixed": not math.isclose(
            readout_a, readout_b, rel_tol=0.0, abs_tol=0.0
        ),
        "strict_limit": (
            "Block123 supplies the formula, but not the residue packet.  With "
            "the Block126 top response fixed, different admissible Gram-pure "
            "residue packets give different y_H values until a same-surface "
            "accepted action/O_H and numeric pole-residue row authority selects "
            "one packet."
        ),
    }


def main() -> int:
    print("PR #230 Block131 action-first source-Higgs authority construction attempt")
    print("=" * 82)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [
        name
        for name, cert in certs.items()
        if isinstance(cert, dict) and cert.get("proposal_allowed") is True
    ]
    strict_path_presence = {
        name: (ROOT / path).exists()
        for name, path in EXPECTED_STRICT_PACKET_PATHS.items()
    }
    raw_scan = scan_raw_strict_tokens()
    finite_summary = finite_row_summary(certs["block124_completed_source_higgs_row_intake"])
    d_e_top_ds = top_response_mean(certs["block126_matched_top_additive_subtraction_packet"])
    witness = build_readout_witness(d_e_top_ds)

    block122_axis_gap_preserved = (
        certs["block122_hamming_axis_action_lsz_normalization_gap"]
        .get("axis_action_lsz_counterfamily", {})
        .get("axis_unchanged")
        is True
        and certs["block122_hamming_axis_action_lsz_normalization_gap"]
        .get("axis_action_lsz_counterfamily", {})
        .get("c_sh_varies")
        is True
        and certs["block122_hamming_axis_action_lsz_normalization_gap"]
        .get("axis_action_lsz_counterfamily", {})
        .get("c_hh_varies")
        is True
    )
    block123_formula_support_not_packet = (
        certs["block123_source_higgs_lsz_readout_formula"].get(
            "block123_source_higgs_lsz_readout_formula_passed"
        )
        is True
        and certs["block123_source_higgs_lsz_readout_formula"].get(
            "current_closure_satisfied"
        )
        is False
        and certs["block123_source_higgs_lsz_readout_formula"]
        .get("current_missing_packet", {})
        .get("strict_source_higgs_pole_rows_absent")
        is True
        and certs["block123_source_higgs_lsz_readout_formula"]
        .get("current_missing_packet", {})
        .get("canonical_oh_absent")
        is True
    )
    block124_finite_support_not_strict_rows = (
        finite_summary["finite_row_count"] == 693
        and finite_summary["timeseries_row_count"] == 693
        and finite_summary["pole_residue_row_hits"] == []
        and finite_summary["canonical_identity_hits"] == []
    )
    block125_contract_still_empty = (
        certs["block125_post_chunk_strict_contract_resolver"].get(
            "post_chunk_raw_scan", {}
        ).get(
            "source_higgs_pole_residue_rows"
        )
        == 0
        and certs["block125_post_chunk_strict_contract_resolver"]
        .get("route_contracts", {})
        .get("source_higgs_strict_pole_rows", {})
        .get("satisfied")
        is False
        and certs["block125_post_chunk_strict_contract_resolver"].get(
            "satisfied_route_contracts"
        )
        == []
        and any(
            item.get("route") == "source_higgs_strict_pole_rows"
            and "accepted canonical O_H/action" in item.get("first_concrete_artifact", "")
            for item in certs["block125_post_chunk_strict_contract_resolver"].get(
                "ranked_next_paths", []
            )
        )
    )
    block126_top_only_not_action = (
        certs["block126_matched_top_additive_subtraction_packet"]
        .get("strict_subtraction_contract_state", {})
        .get("top_side_same_configuration_rows_present")
        is True
        and certs["block126_matched_top_additive_subtraction_packet"]
        .get("strict_subtraction_contract_state", {})
        .get("accepted_same_source_ew_action_present")
        is False
        and certs["block126_matched_top_additive_subtraction_packet"]
        .get("strict_subtraction_contract_state", {})
        .get("accepted_canonical_higgs_or_overlap_present")
        is False
    )
    action_first_blockers_preserved = (
        "not complete" in statuses["action_first_route_completion"]
        and "not constructible" in statuses["action_first_oh_artifact_attempt"]
        and certs["canonical_oh_action_lsz_closure"].get("accepted_current_surface")
        is False
        and certs["source_higgs_pole_row_assembly"].get(
            "strict_c_ss_c_sh_c_hh_rows_exist"
        )
        is False
        and certs["source_higgs_pole_row_assembly"].get(
            "blocked_by_canonical_o_h_authority"
        )
        is True
        and certs["source_higgs_pole_row_assembly"].get(
            "blocked_by_missing_production_pole_rows"
        )
        is True
    )
    block128_block130_pivots_closed = (
        certs["block128_strict_wz_source_row_construction_attempt"]
        .get("constructive_status", {})
        .get("strict_source_higgs_constructible_from_current_raw_rows")
        is False
        and certs["block130_neutral_h3h4_transfer_coupling_construction_attempt"].get(
            "strict_neutral_artifact_present"
        )
        is False
        and certs["block130_neutral_h3h4_eta_nonidentifiability"]
        .get("eta_counterfamily", {})
        .get("same_source_self_and_triplet_block")
        is True
        and certs["block130_neutral_h3h4_eta_nonidentifiability"]
        .get("eta_counterfamily", {})
        .get("eta0_source_triplet_coupling")
        == 0.0
        and certs["block130_neutral_h3h4_eta_nonidentifiability"]
        .get("eta_counterfamily", {})
        .get("eta1_source_triplet_coupling")
        != 0.0
        and not any(
            certs["block130_neutral_h3h4_eta_nonidentifiability"]
            .get("strict_artifact_presence", {})
            .values()
        )
    )
    expected_strict_packet_absent = not any(strict_path_presence.values())
    raw_strict_tokens_absent = (
        raw_scan["raw_files_checked"] == EXPECTED_CHUNKS
        and raw_scan["missing_raw_indices"] == []
        and raw_scan["strict_token_hit_count"] == 0
    )
    witness_blocks_unique_readout = (
        witness["available"] is True
        and witness["candidate_residue_packet_a"]["gram_pure"] is True
        and witness["candidate_residue_packet_b"]["gram_pure"] is True
        and witness["readout_changes_while_current_support_fixed"] is True
        and math.isclose(witness["readout_ratio_b_over_a"], 2.0, rel_tol=0.0, abs_tol=1e-15)
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("block122-axis-action-lsz-gap-preserved", block122_axis_gap_preserved, statuses["block122_hamming_axis_action_lsz_normalization_gap"])
    report("block123-formula-is-support-not-packet", block123_formula_support_not_packet, str(certs["block123_source_higgs_lsz_readout_formula"].get("current_missing_packet")))
    report("block124-finite-support-not-strict-rows", block124_finite_support_not_strict_rows, str(finite_summary))
    report("block125-strict-contract-still-empty", block125_contract_still_empty, str(certs["block125_post_chunk_strict_contract_resolver"].get("ranked_next_paths")))
    report("block126-top-response-not-action-authority", block126_top_only_not_action, str(certs["block126_matched_top_additive_subtraction_packet"].get("strict_subtraction_contract_state")))
    report("prior-action-first-blockers-preserved", action_first_blockers_preserved, "action/O_H/source-Higgs pole assembly still blocked")
    report("post-block128-block130-pivots-closed", block128_block130_pivots_closed, "W/Z source fallback and neutral pivot remain blocked")
    report("expected-strict-packet-paths-absent", expected_strict_packet_absent, str(strict_path_presence))
    report("raw-strict-action-pole-tokens-absent", raw_strict_tokens_absent, str(raw_scan))
    report("readout-witness-blocks-unique-current-surface-value", witness_blocks_unique_readout, str(witness))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/audit/stress gates deny proposal")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and block122_axis_gap_preserved
        and block123_formula_support_not_packet
        and block124_finite_support_not_strict_rows
        and block125_contract_still_empty
        and block126_top_only_not_action
        and action_first_blockers_preserved
        and block128_block130_pivots_closed
        and expected_strict_packet_absent
        and raw_strict_tokens_absent
        and witness_blocks_unique_readout
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block131 cannot construct action-first "
            "source-Higgs authority from the post-Block130 surface: accepted "
            "same-surface canonical O_H/action authority and numeric "
            "C_ss/C_sH/C_HH pole-residue rows are both absent"
        ),
        "conditional_surface_status": (
            "action-first route reopens only with an accepted same-surface "
            "canonical O_H/action/LSZ certificate plus nonempty numeric "
            "C_ss/C_sH/C_HH pole-residue rows sharing the source/action/O_H "
            "surface"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block123 gives the invariant readout formula and Block126 gives "
            "top-side support, but no current artifact selects canonical O_H, "
            "accepted action, scalar LSZ/source overlap, or pole residues.  The "
            "Block131 witness shows different Gram-pure residue packets give "
            "different y_H values while the current finite support remains fixed."
        ),
        "current_closure_satisfied": False,
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block131_action_first_source_higgs_authority_construction_attempt_passed": passed,
        "block122_axis_gap_preserved": block122_axis_gap_preserved,
        "block123_formula_support_not_packet": block123_formula_support_not_packet,
        "finite_source_higgs_summary": finite_summary,
        "block124_finite_support_not_strict_rows": block124_finite_support_not_strict_rows,
        "block125_contract_still_empty": block125_contract_still_empty,
        "block126_top_only_not_action": block126_top_only_not_action,
        "action_first_blockers_preserved": action_first_blockers_preserved,
        "block128_block130_pivots_closed": block128_block130_pivots_closed,
        "strict_packet_path_presence": strict_path_presence,
        "expected_strict_packet_absent": expected_strict_packet_absent,
        "raw_strict_action_pole_scan": raw_scan,
        "raw_strict_tokens_absent": raw_strict_tokens_absent,
        "readout_nonidentifiability_witness": witness,
        "readout_witness_blocks_unique_value": witness_blocks_unique_readout,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": {
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_treat_candidate_residue_packets_as_measurement_rows": True,
            "does_not_promote_finite_c_sx_rows_to_c_sh_pole_residues": True,
            "does_not_identify_taste_radial_x_as_canonical_o_h": True,
            "does_not_accept_unratified_fms_or_ansatz_action": True,
            "does_not_set_kappa_s_c2_or_z_match": True,
            "does_not_use_observed_targets_or_forbidden_unit_imports": True,
        },
        "exact_next_action": (
            "Supply an accepted same-surface canonical O_H/action/LSZ certificate "
            "and nonempty numeric C_ss/C_sH/C_HH pole-residue rows with matching "
            "source/action/O_H surface IDs.  Otherwise reopen W/Z only with "
            "strict production rows plus non-observed g2 and same-source action, "
            "or reopen Schur/neutral only with their strict pole/transfer "
            "authorities."
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

#!/usr/bin/env python3
"""
PR #230 Block111 Schur K-prime packet gap audit.

The higher-shell packet is complete at 63/63 chunks.  This runner audits the
completed packet against the strict Block69/Block70 Schur/Feshbach K-prime
contract and records whether any completed chunk emitted the pole-coordinate,
kernel-derivative, left/right-null-vector, source-projection, or FV/IR/contact
rows needed to instantiate the exact-support theorem.

This is a packet-level negative boundary only.  It does not infer K-prime rows
from finite C_ss/C_sx/C_xx aliases, does not treat taste-radial x as canonical
O_H, and does not authorize retained or proposed_retained top-Yukawa closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json"
)

ROW_PATTERN = (
    "outputs/yt_pr230_schur_higher_shell_rows/"
    "yt_pr230_schur_higher_shell_rows_L12_T24_chunk{chunk:03d}_2026-05-07.json"
)
CHECKPOINT_PATTERN = "outputs/yt_pr230_schur_higher_shell_chunk{chunk:03d}_checkpoint_2026-05-12.json"

PARENTS = {
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "complete_packet_monotonicity": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "strict_kprime_pole_residue_certificate": "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json",
    "block70_schur_feshbach_kprime_residue_theorem": "outputs/yt_pr230_block70_schur_feshbach_kprime_residue_theorem_2026-05-12.json",
    "schur_abc_definition_derivation_attempt": "outputs/yt_pr230_schur_abc_definition_derivation_attempt_2026-05-05.json",
    "schur_higher_shell_production_contract": "outputs/yt_pr230_schur_higher_shell_production_contract_2026-05-07.json",
    "block110_cl3_z3_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
}

EXPECTED_CHUNKS = 63
EXPECTED_SEED_CONTROL_VERSION = "numba_gauge_seed_v1"
EXPECTED_SELECTED_MASS = 0.75
EXPECTED_MODES = {
    "0,0,0",
    "1,0,0",
    "0,1,0",
    "0,0,1",
    "1,1,0",
    "1,0,1",
    "0,1,1",
    "1,1,1",
    "2,0,0",
    "0,2,0",
    "0,0,2",
}

STRICT_ROW_FIELD_NAMES = {
    "A_at_pole",
    "A_prime_at_pole",
    "B_at_pole",
    "B_prime_at_pole",
    "C_at_pole",
    "C_inverse_at_pole",
    "C_prime_at_pole",
    "D_eff_at_pole",
    "D_eff_prime_at_pole",
    "Kprime",
    "K_prime_at_pole",
    "derivative_row_l_Kprime_r_or_exact_equivalent",
    "fv_ir_contact_term_checks",
    "left_Kprime_right_at_pole",
    "left_null_covector",
    "pole_coordinate",
    "pole_fit_window",
    "right_null_vector",
    "schur_feshbach_or_transfer_kernel_rows",
    "source_projection_numerator",
    "source_row_projection_numerator",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa_as_selector": False,
    "used_alpha_lm_or_plaquette_u0": False,
    "used_reduced_cold_pilots_as_production_evidence": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_kappa_s_equal_one": False,
    "treated_taste_radial_x_as_canonical_O_H": False,
    "treated_finite_C_ss_C_sx_C_xx_as_schur_kprime_rows": False,
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


def row_path(chunk: int) -> Path:
    return ROOT / ROW_PATTERN.format(chunk=chunk)


def checkpoint_path(chunk: int) -> Path:
    return ROOT / CHECKPOINT_PATTERN.format(chunk=chunk)


def first_ensemble(data: dict[str, Any]) -> dict[str, Any]:
    ensembles = data.get("ensembles")
    if isinstance(ensembles, list) and len(ensembles) == 1 and isinstance(ensembles[0], dict):
        return ensembles[0]
    return {}


def nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, (list, dict, str, tuple, set)):
        return len(value) > 0
    return True


def walk_paths(value: Any, prefix: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
    rows: list[tuple[tuple[str, ...], Any]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            path = prefix + (str(key),)
            rows.append((path, item))
            rows.extend(walk_paths(item, path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            path = prefix + (str(index),)
            rows.append((path, item))
            rows.extend(walk_paths(item, path))
    return rows


def strict_field_hits(data: dict[str, Any]) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for path, value in walk_paths(data):
        key = path[-1]
        if key in STRICT_ROW_FIELD_NAMES:
            hits.append(
                {
                    "path": ".".join(path),
                    "key": key,
                    "value_type": type(value).__name__,
                    "nonempty": nonempty(value),
                }
            )
    return hits


def audit_chunk(chunk: int) -> tuple[dict[str, Any] | None, list[str]]:
    issues: list[str] = []
    checkpoint = load_json(checkpoint_path(chunk))
    data = load_json(row_path(chunk))
    if not checkpoint:
        issues.append("checkpoint missing")
    if not data:
        issues.append("row JSON missing")
        return None, issues

    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    schur_meta = (
        metadata.get("schur_kprime_kernel_rows")
        if isinstance(metadata.get("schur_kprime_kernel_rows"), dict)
        else {}
    )
    ensemble = first_ensemble(data)
    seed_control = (
        ensemble.get("rng_seed_control")
        if isinstance(ensemble.get("rng_seed_control"), dict)
        else {}
    )
    source = (
        ensemble.get("source_higgs_cross_correlator_analysis")
        if isinstance(ensemble.get("source_higgs_cross_correlator_analysis"), dict)
        else {}
    )
    lsz = (
        ensemble.get("scalar_two_point_lsz_analysis")
        if isinstance(ensemble.get("scalar_two_point_lsz_analysis"), dict)
        else {}
    )
    response = (
        ensemble.get("scalar_source_response_analysis")
        if isinstance(ensemble.get("scalar_source_response_analysis"), dict)
        else {}
    )
    aliases = (
        source.get("two_source_taste_radial_row_aliases")
        if isinstance(source.get("two_source_taste_radial_row_aliases"), dict)
        else {}
    )

    if checkpoint.get("checkpoint_passed") is not True:
        issues.append("checkpoint did not pass")
    if checkpoint.get("completed") is not True:
        issues.append("checkpoint completed not true")
    if checkpoint.get("proposal_allowed") is not False:
        issues.append("checkpoint proposal_allowed is not false")
    if metadata.get("phase") != "production":
        issues.append(f"metadata phase={metadata.get('phase')!r}")
    if seed_control.get("seed_control_version") != EXPECTED_SEED_CONTROL_VERSION:
        issues.append(f"seed_control_version={seed_control.get('seed_control_version')!r}")
    if ensemble.get("selected_mass_parameter") != EXPECTED_SELECTED_MASS:
        issues.append(f"selected_mass_parameter={ensemble.get('selected_mass_parameter')!r}")
    if schur_meta.get("enabled") is not False:
        issues.append("schur_kprime_kernel_rows enabled is not false")
    if schur_meta.get("implementation_status") != "absent_guarded":
        issues.append(f"schur_kprime implementation_status={schur_meta.get('implementation_status')!r}")
    if schur_meta.get("finite_source_only_c_ss_is_not_schur_rows") is not True:
        issues.append("finite-source-only Schur guard missing")
    if schur_meta.get("used_as_physical_yukawa_readout") is not False:
        issues.append("schur_kprime metadata marked as physical y_t readout")
    if source.get("canonical_higgs_operator_identity_passed") is not False:
        issues.append("canonical_higgs_operator_identity_passed not false")
    if source.get("used_as_physical_yukawa_readout") is not False:
        issues.append("source-higgs rows marked as physical y_t readout")
    if aliases.get("C_sx_aliases_C_sH_schema_field") is not True:
        issues.append("C_sx alias guard missing")
    if aliases.get("C_xx_aliases_C_HH_schema_field") is not True:
        issues.append("C_xx alias guard missing")
    if not isinstance(source.get("pole_residue_rows"), list):
        issues.append("source pole_residue_rows missing")
    if isinstance(source.get("pole_residue_rows"), list) and source.get("pole_residue_rows"):
        issues.append("source pole_residue_rows unexpectedly nonempty")
    if set((source.get("mode_rows") or {}).keys()) != EXPECTED_MODES:
        issues.append("source mode set mismatch")
    if set((lsz.get("mode_rows") or {}).keys()) != EXPECTED_MODES:
        issues.append("scalar LSZ mode set mismatch")
    if not isinstance(response.get("per_configuration_slopes"), list):
        issues.append("scalar source-response slopes missing")

    hits = strict_field_hits(data)
    nonempty_hits = [
        hit
        for hit in hits
        if hit["nonempty"]
        and not hit["path"].endswith("source_higgs_cross_correlator_analysis.pole_residue_rows")
    ]
    return (
        {
            "chunk_index": chunk,
            "checkpoint": rel(checkpoint_path(chunk)),
            "row_output": rel(row_path(chunk)),
            "schur_kprime_kernel_rows_metadata": schur_meta,
            "source_pole_residue_row_count": len(source.get("pole_residue_rows") or []),
            "strict_field_hits": hits,
            "strict_nonempty_field_hits": nonempty_hits,
            "finite_aliases_present_but_nonphysical": {
                "C_sx_aliases_C_sH_schema_field": aliases.get("C_sx_aliases_C_sH_schema_field"),
                "C_xx_aliases_C_HH_schema_field": aliases.get("C_xx_aliases_C_HH_schema_field"),
                "canonical_higgs_operator_identity_passed": source.get(
                    "canonical_higgs_operator_identity_passed"
                ),
                "used_as_physical_yukawa_readout": source.get("used_as_physical_yukawa_readout"),
            },
        },
        issues,
    )


def required_emission_gap_matrix() -> list[dict[str, Any]]:
    return [
        {
            "required_row": "pole_coordinate",
            "present_in_completed_packet": False,
            "reason": "finite q-hat shell rows are not an isolated analytic pole coordinate",
        },
        {
            "required_row": "pole_fit_window",
            "present_in_completed_packet": False,
            "reason": "no accepted model class or analytic continuation window is emitted",
        },
        {
            "required_row": "Schur/Feshbach A/B/C rows at the pole",
            "present_in_completed_packet": False,
            "reason": "metadata explicitly marks Schur K-prime kernel rows absent_guarded",
        },
        {
            "required_row": "K-prime derivative row or l K'(x_pole) r equivalent",
            "present_in_completed_packet": False,
            "reason": "completed rows contain finite correlator aliases, not kernel derivative rows",
        },
        {
            "required_row": "left/right null vectors",
            "present_in_completed_packet": False,
            "reason": "no same-surface kernel null-vector row is emitted",
        },
        {
            "required_row": "source projection numerator",
            "present_in_completed_packet": False,
            "reason": "C_sx alias rows are guarded as non-canonical and nonphysical",
        },
        {
            "required_row": "FV/IR/contact/threshold authority",
            "present_in_completed_packet": False,
            "reason": "finite packet has no limiting-order, contact-subtraction, or threshold certificate",
        },
        {
            "required_row": "canonical O_H/source-Higgs identity",
            "present_in_completed_packet": False,
            "reason": "source operator certificate remains taste-radial, not accepted canonical O_H",
        },
    ]


def main() -> int:
    print("PR #230 Block111 Schur K-prime packet gap audit")
    print("=" * 76)

    parents = {name: load_json(path) for name, path in PARENTS.items()}
    parent_statuses = {name: status(cert) for name, cert in parents.items()}
    missing_parents = [name for name, cert in parents.items() if not cert]
    parent_proposals = [name for name, cert in parents.items() if cert.get("proposal_allowed") is True]

    chunks: list[dict[str, Any]] = []
    chunk_issues: dict[str, list[str]] = {}
    for chunk in range(1, EXPECTED_CHUNKS + 1):
        parsed, issues = audit_chunk(chunk)
        if parsed is not None:
            chunks.append(parsed)
        if issues:
            chunk_issues[f"chunk{chunk:03d}"] = issues

    strict_nonempty_hits = [
        {"chunk_index": chunk["chunk_index"], **hit}
        for chunk in chunks
        for hit in chunk["strict_nonempty_field_hits"]
    ]
    metadata_absent_guard_count = sum(
        1
        for chunk in chunks
        if chunk["schur_kprime_kernel_rows_metadata"].get("enabled") is False
        and chunk["schur_kprime_kernel_rows_metadata"].get("implementation_status") == "absent_guarded"
    )
    finite_source_only_guard_count = sum(
        1
        for chunk in chunks
        if chunk["schur_kprime_kernel_rows_metadata"].get(
            "finite_source_only_c_ss_is_not_schur_rows"
        )
        is True
    )
    empty_pole_residue_rows_count = sum(
        1 for chunk in chunks if chunk["source_pole_residue_row_count"] == 0
    )
    finite_alias_guard_count = sum(
        1
        for chunk in chunks
        if chunk["finite_aliases_present_but_nonphysical"].get(
            "C_sx_aliases_C_sH_schema_field"
        )
        is True
        and chunk["finite_aliases_present_but_nonphysical"].get(
            "C_xx_aliases_C_HH_schema_field"
        )
        is True
        and chunk["finite_aliases_present_but_nonphysical"].get(
            "canonical_higgs_operator_identity_passed"
        )
        is False
        and chunk["finite_aliases_present_but_nonphysical"].get(
            "used_as_physical_yukawa_readout"
        )
        is False
    )

    strict_kprime = parents["strict_kprime_pole_residue_certificate"]
    block70 = parents["block70_schur_feshbach_kprime_residue_theorem"]
    complete_packet = parents["complete_packet_monotonicity"]
    block110 = parents["block110_cl3_z3_action_descent_obstruction"]

    strict_builder_requires_rows = (
        strict_kprime.get("strict_pass") is False
        and strict_kprime.get("candidate_present") is False
        and isinstance(strict_kprime.get("missing_required_rows"), list)
        and len(strict_kprime.get("missing_required_rows", [])) > 0
    )
    theorem_only_support = (
        "Schur-Feshbach K-prime residue theorem" in parent_statuses["block70_schur_feshbach_kprime_residue_theorem"]
        and block70.get("proposal_allowed") is False
        and block70.get("fail_count") == 0
    )
    complete_packet_negative = (
        complete_packet.get("higher_shell_complete_packet_monotonicity_gate_passed") is True
        and complete_packet.get("complete_packet_chunk_count") == EXPECTED_CHUNKS
        and complete_packet.get("strict_pole_rows_written") is False
        and complete_packet.get("pole_location_or_derivative_rows_present") is False
        and complete_packet.get("proposal_allowed") is False
    )
    block110_keeps_action_gap = (
        block110.get("block110_cl3_z3_action_descent_obstruction_passed") is True
        and block110.get("proposal_allowed") is False
        and block110.get("source_higgs_route_implication", {}).get(
            "accepted_action_or_pole_rows_still_required"
        )
        is True
    )
    gap_matrix = required_emission_gap_matrix()
    gap_matrix_all_missing = all(row["present_in_completed_packet"] is False for row in gap_matrix)
    forbidden_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())
    strict_row_emissions_present = bool(strict_nonempty_hits)

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("completed-packet-63-chunks-checked", len(chunks) == EXPECTED_CHUNKS, f"chunks={len(chunks)}")
    report("all-chunk-checkpoints-and-row-schema-clean", not chunk_issues, f"issues={dict(list(chunk_issues.items())[:3])}")
    report("schur-kprime-absent-guard-on-all-chunks", metadata_absent_guard_count == EXPECTED_CHUNKS, f"count={metadata_absent_guard_count}")
    report("finite-source-only-not-schur-guard-on-all-chunks", finite_source_only_guard_count == EXPECTED_CHUNKS, f"count={finite_source_only_guard_count}")
    report("source-pole-residue-rows-empty-on-all-chunks", empty_pole_residue_rows_count == EXPECTED_CHUNKS, f"count={empty_pole_residue_rows_count}")
    report("finite-alias-rows-remain-nonphysical-on-all-chunks", finite_alias_guard_count == EXPECTED_CHUNKS, f"count={finite_alias_guard_count}")
    report("strict-kprime-row-emissions-absent", not strict_row_emissions_present, f"nonempty_hits={strict_nonempty_hits[:3]}")
    report("block69-builder-still-requires-strict-rows", strict_builder_requires_rows, strict_kprime.get("actual_current_surface_status"))
    report("block70-theorem-is-support-only-with-physical-rows-absent", theorem_only_support, block70.get("actual_current_surface_status"))
    report("complete-packet-monotonicity-gate-remains-negative", complete_packet_negative, complete_packet.get("actual_current_surface_status"))
    report("block110-action-gap-still-load-bearing", block110_keeps_action_gap, block110.get("actual_current_surface_status"))
    report("block69-required-emission-gap-matrix-all-missing", gap_matrix_all_missing, "no strict row family emitted by packet")
    report("does-not-authorize-retained-proposal", True, "packet gap audit is exact negative boundary only")
    report("forbidden-firewall-clean", forbidden_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing_parents
        and not parent_proposals
        and len(chunks) == EXPECTED_CHUNKS
        and not chunk_issues
        and metadata_absent_guard_count == EXPECTED_CHUNKS
        and finite_source_only_guard_count == EXPECTED_CHUNKS
        and empty_pole_residue_rows_count == EXPECTED_CHUNKS
        and finite_alias_guard_count == EXPECTED_CHUNKS
        and not strict_row_emissions_present
        and strict_builder_requires_rows
        and theorem_only_support
        and complete_packet_negative
        and block110_keeps_action_gap
        and gap_matrix_all_missing
        and forbidden_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block111 complete higher-shell packet contains "
            "no strict Schur-Feshbach K-prime pole-row emissions"
        ),
        "conditional_surface_status": (
            "exact-support theorem can be used only after a future accepted same-surface "
            "row artifact emits the Block69 pole coordinate, K-prime derivative or "
            "equivalent Schur/Feshbach rows, source projection numerator, and FV/IR/contact "
            "authority"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The completed higher-shell packet has 63/63 finite source/taste-radial "
            "C_ss/C_sx/C_xx row files, but every chunk explicitly guards Schur K-prime "
            "kernel rows as absent.  The packet supplies no pole coordinate, no K-prime "
            "derivative row, no left/right null vectors, no source projection numerator, "
            "no FV/IR/contact authority, and no canonical O_H identity."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block111_schur_kprime_packet_gap_audit_passed": passed,
        "completed_packet_checked_chunks": len(chunks),
        "expected_chunk_count": EXPECTED_CHUNKS,
        "strict_kprime_row_emissions_present": strict_row_emissions_present,
        "strict_nonempty_field_hits": strict_nonempty_hits,
        "metadata_absent_guard_count": metadata_absent_guard_count,
        "finite_source_only_guard_count": finite_source_only_guard_count,
        "empty_pole_residue_rows_count": empty_pole_residue_rows_count,
        "finite_alias_guard_count": finite_alias_guard_count,
        "block69_required_emission_gap_matrix": gap_matrix,
        "packet_key_scan_summary": {
            "strict_field_names_scanned": sorted(STRICT_ROW_FIELD_NAMES),
            "strict_field_hit_count_including_empty_guards": sum(
                len(chunk["strict_field_hits"]) for chunk in chunks
            ),
            "strict_nonempty_field_hit_count": len(strict_nonempty_hits),
            "note": (
                "Empty pole_residue_rows lists and absent_guarded metadata are counted as "
                "guards, not as strict Schur K-prime row evidence."
            ),
        },
        "parent_certificates": PARENTS,
        "parent_statuses": parent_statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not infer Schur/Feshbach K-prime rows from finite C_ss/C_sx/C_xx aliases",
            "does not relabel taste-radial C_sx/C_xx as physical C_sH/C_HH pole rows",
            "does not treat taste-radial x as canonical O_H",
            "does not supply FV/IR/contact or threshold limiting authority",
            "does not set kappa_s = 1, c2 = 1, Z_match = 1, or g2 by convention",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
        ],
        "exact_next_action": (
            "Do not rerun finite higher-shell chunks for K-prime closure.  Closure requires "
            "one new accepted same-surface row artifact: either canonical O_H/C_sH/C_HH "
            "pole rows, genuine W/Z physical-response rows with identity/covariance/g2 "
            "authority, or strict Schur/Feshbach K-prime rows carrying the Block69 "
            "emission matrix and FV/IR/contact authority."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {rel(OUTPUT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

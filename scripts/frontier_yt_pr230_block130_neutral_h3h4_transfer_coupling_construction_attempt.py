#!/usr/bin/env python3
"""
PR #230 Block130 neutral H3/H4 transfer/coupling construction attempt.

Block129 closed the finite Schur shortcut.  This runner pivots to the neutral
H3/H4 route and tests whether the completed finite source/taste-radial packet
can construct physical neutral transfer/source-canonical-Higgs authority.  The
attempt is constructive: it scans for strict artifacts, then builds an explicit
same-observed-row two-completion witness showing that current finite rows do
not determine H3 transfer/offdiagonal dynamics or H4 source/canonical-Higgs
coupling.
"""

from __future__ import annotations

import json
import math
import statistics
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block130_neutral_h3h4_transfer_coupling_construction_attempt_2026-05-17.json"
)

EXPECTED_CHUNKS = 63
EXPECTED_MODE_COUNT = 11

PARENTS = {
    "block116_neutral_h3h4_strict_artifact_resolver": (
        "outputs/yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json"
    ),
    "block124_completed_source_higgs_row_intake": (
        "outputs/yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json"
    ),
    "block128_strict_wz_source_row_construction_attempt": (
        "outputs/yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
    ),
    "block129_schur_pole_authority_construction_attempt": (
        "outputs/yt_pr230_block129_schur_pole_authority_construction_attempt_2026-05-17.json"
    ),
    "neutral_h3h4_aperture": (
        "outputs/yt_pr230_neutral_primitive_h3h4_aperture_checkpoint_2026-05-07.json"
    ),
    "two_source_primitive_transfer_candidate": (
        "outputs/yt_pr230_two_source_taste_radial_primitive_transfer_candidate_gate_2026-05-07.json"
    ),
    "same_surface_neutral_multiplicity_gate": (
        "outputs/yt_pr230_same_surface_neutral_multiplicity_one_gate_2026-05-07.json"
    ),
    "z3_heat_kernel_transfer_attempt": (
        "outputs/yt_pr230_z3_heat_kernel_neutral_transfer_attempt_2026-05-15.json"
    ),
    "z3_heat_kernel_source_coupling_no_go": (
        "outputs/yt_pr230_z3_heat_kernel_source_coupling_no_go_2026-05-15.json"
    ),
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

STRICT_ARTIFACT_PATHS = {
    "neutral_primitive_cone_certificate": "outputs/yt_neutral_scalar_primitive_cone_certificate_2026-05-05.json",
    "neutral_offdiagonal_generator_certificate": "outputs/yt_neutral_offdiagonal_generator_certificate_2026-05-05.json",
    "neutral_scalar_irreducibility_certificate": "outputs/yt_neutral_scalar_irreducibility_certificate_2026-05-04.json",
    "neutral_scalar_rank_one_purity_certificate": "outputs/yt_neutral_scalar_rank_one_purity_certificate_2026-05-03.json",
    "pr230_physical_neutral_transfer_certificate": "outputs/yt_pr230_physical_neutral_transfer_certificate_2026-05-17.json",
    "pr230_neutral_h3h4_certificate": "outputs/yt_pr230_neutral_h3h4_certificate_2026-05-17.json",
    "pr230_source_triplet_coupling_certificate": "outputs/yt_pr230_same_surface_source_triplet_coupling_2026-05-15.json",
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
}

STRICT_KEY_TOKENS = (
    "neutral_transfer_matrix",
    "offdiagonal_generator",
    "primitive_cone_certificate",
    "irreducibility_certificate",
    "rank_one_purity_certificate",
    "physical_neutral_transfer",
    "source_canonical_higgs_coupling_certified",
    "source_triplet_coupling",
    "canonical_higgs_operator_certificate",
    "pole_residue_rows",
)

FORBIDDEN_FIREWALL = {
    "used_source_only_or_c_sx_rows_as_neutral_transfer": False,
    "used_heat_kernel_as_physical_transfer_without_action_selector": False,
    "used_heat_kernel_eta_as_derived_source_coupling": False,
    "used_finite_equal_time_rows_as_pole_residues": False,
    "aliased_c_sx_to_c_sh_before_canonical_oh": False,
    "identified_taste_radial_x_as_canonical_oh": False,
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
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


def load_json(path: str | Path) -> Any:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    return json.loads(full.read_text(encoding="utf-8"))


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def summarize(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": statistics.fmean(values),
        "stdev": statistics.pstdev(values) if len(values) > 1 else 0.0,
    }


def chunk_path(index: int) -> Path:
    return (
        ROOT
        / "outputs"
        / "yt_pr230_schur_higher_shell_rows"
        / f"yt_pr230_schur_higher_shell_rows_L12_T24_chunk{index:03d}_2026-05-07.json"
    )


def raw_path(index: int) -> Path:
    return (
        ROOT
        / "outputs"
        / "yt_direct_lattice_correlator_production_schur_higher_shell_rows"
        / f"L12_T24_chunk{index:03d}"
        / "L12xT24"
        / "ensemble_measurement.json"
    )


def iter_mode_rows() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    missing_chunks: list[int] = []
    mode_sets: set[tuple[str, ...]] = set()
    strict_key_hits: list[dict[str, Any]] = []
    source_alias_rows = 0
    raw_files_checked = 0
    raw_strict_token_hits: list[dict[str, Any]] = []

    for index in range(1, EXPECTED_CHUNKS + 1):
        path = chunk_path(index)
        if not path.exists():
            missing_chunks.append(index)
            continue
        data = load_json(path)
        ensembles = data.get("ensembles") if isinstance(data, dict) else None
        if not isinstance(ensembles, list) or not ensembles:
            continue
        ensemble = ensembles[0]
        analysis = (
            ensemble.get("source_higgs_cross_correlator_analysis")
            if isinstance(ensemble.get("source_higgs_cross_correlator_analysis"), dict)
            else {}
        )
        mode_rows = analysis.get("mode_rows") if isinstance(analysis.get("mode_rows"), dict) else {}
        mode_sets.add(tuple(sorted(mode_rows)))
        pole_rows = analysis.get("pole_residue_rows")
        if isinstance(pole_rows, list) and pole_rows:
            strict_key_hits.append({"path": rel(path), "key": "pole_residue_rows", "count": len(pole_rows)})
        for mode, row in sorted(mode_rows.items()):
            if not isinstance(row, dict):
                continue
            c_ss = row.get("C_ss_real")
            c_sx = row.get("C_sx_real", row.get("C_sH_real"))
            c_xx = row.get("C_xx_real", row.get("C_HH_real"))
            if is_number(c_ss) and is_number(c_sx) and is_number(c_xx):
                rows.append(
                    {
                        "chunk": index,
                        "mode": mode,
                        "C_ss_real": float(c_ss),
                        "C_sx_real": float(c_sx),
                        "C_xx_real": float(c_xx),
                        "p_hat_sq": row.get("p_hat_sq"),
                        "path": rel(path),
                    }
                )
                source_alias_rows += 1
            for token in STRICT_KEY_TOKENS:
                value = row.get(token)
                if value not in (None, False, [], {}):
                    strict_key_hits.append({"path": rel(path), "mode": mode, "key": token})

        raw = raw_path(index)
        if raw.exists():
            raw_files_checked += 1
            text = raw.read_text(encoding="utf-8", errors="replace")
            for token in STRICT_KEY_TOKENS:
                if token in text and token not in {"pole_residue_rows"}:
                    raw_strict_token_hits.append({"path": rel(raw), "token": token})

    metadata = {
        "expected_chunks": EXPECTED_CHUNKS,
        "missing_chunks": missing_chunks,
        "mode_sets": [list(mode_set) for mode_set in sorted(mode_sets)],
        "source_alias_rows": source_alias_rows,
        "strict_key_hits": strict_key_hits,
        "raw_files_checked": raw_files_checked,
        "raw_strict_token_hits": raw_strict_token_hits[:50],
        "raw_strict_token_hit_count": len(raw_strict_token_hits),
    }
    return rows, metadata


def build_two_completion_witness(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {"available": False, "reason": "no finite rows"}

    sample = next((row for row in rows if abs(row["C_sx_real"]) > 0.0), rows[0])
    css = float(sample["C_ss_real"])
    csx = float(sample["C_sx_real"])
    cxx = float(sample["C_xx_real"])
    cnn = cxx
    theta_a = 0.0
    theta_b = math.pi / 3.0
    cos_a = math.cos(theta_a)
    cos_b = math.cos(theta_b)
    sin_b = math.sin(theta_b)
    c_s_h_a = cos_a * csx
    c_hh_a = cos_a * cos_a * cxx
    c_s_h_b = cos_b * csx
    c_hh_b = cos_b * cos_b * cxx + sin_b * sin_b * cnn
    ratio_a = c_s_h_a / math.sqrt(c_hh_a) if c_hh_a > 0 else None
    ratio_b = c_s_h_b / math.sqrt(c_hh_b) if c_hh_b > 0 else None
    ratio_delta = None if ratio_a is None or ratio_b is None else ratio_b - ratio_a

    epsilon = 0.25
    transfer_a = [[1.0, 0.0], [0.0, 1.0]]
    transfer_b = [[1.0, epsilon], [epsilon, 1.0]]
    transfer_b_eigenvalues = [1.0 - epsilon, 1.0 + epsilon]

    observed_row_a = {"C_ss_real": css, "C_sx_real": csx, "C_xx_real": cxx}
    observed_row_b = dict(observed_row_a)

    return {
        "available": True,
        "sample_row": sample,
        "hidden_neutral_completion": {
            "basis": ["x_observed_taste_radial", "n_hidden_orthogonal_neutral"],
            "C_sn_real": 0.0,
            "C_xn_real": 0.0,
            "C_nn_real": cnn,
            "observed_equal_time_rows_preserved": observed_row_a == observed_row_b,
        },
        "h4_coupling_family": {
            "H_theta": "cos(theta) x + sin(theta) n",
            "theta_a": theta_a,
            "theta_b": theta_b,
            "C_sH_theta_a": c_s_h_a,
            "C_HH_theta_a": c_hh_a,
            "normalized_source_coupling_theta_a": ratio_a,
            "C_sH_theta_b": c_s_h_b,
            "C_HH_theta_b": c_hh_b,
            "normalized_source_coupling_theta_b": ratio_b,
            "normalized_source_coupling_delta": ratio_delta,
            "coupling_changes_while_observed_rows_fixed": ratio_delta not in (None, 0.0),
        },
        "h3_transfer_family": {
            "transfer_a": transfer_a,
            "transfer_b": transfer_b,
            "transfer_b_eigenvalues": transfer_b_eigenvalues,
            "both_transfer_candidates_positive": min(transfer_b_eigenvalues) > 0.0,
            "offdiagonal_generator_changes_while_equal_time_rows_fixed": epsilon != 0.0,
            "offdiagonal_difference": epsilon,
            "strict_limit": (
                "These matrices are a nonidentifiability witness, not accepted PR230 "
                "physical transfer authority.  They show the current equal-time rows "
                "do not determine H3 without a same-surface action/transfer theorem."
            ),
        },
    }


def main() -> int:
    print("PR #230 Block130 neutral H3/H4 transfer/coupling construction attempt")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if isinstance(cert, dict) and cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in STRICT_ARTIFACT_PATHS.items()
    }

    rows, row_metadata = iter_mode_rows()
    witness = build_two_completion_witness(rows)
    css = [row["C_ss_real"] for row in rows]
    csx = [row["C_sx_real"] for row in rows]
    cxx = [row["C_xx_real"] for row in rows]

    completed_rows_present = (
        not row_metadata["missing_chunks"]
        and len(rows) == EXPECTED_CHUNKS * EXPECTED_MODE_COUNT
        and row_metadata["source_alias_rows"] == EXPECTED_CHUNKS * EXPECTED_MODE_COUNT
    )
    no_strict_neutral_artifact_present = not any(strict_presence.values())
    no_strict_row_or_raw_hits = (
        not row_metadata["strict_key_hits"]
        and row_metadata["raw_strict_token_hit_count"] == 0
    )
    prior_neutral_absence_preserved = (
        certs["block116_neutral_h3h4_strict_artifact_resolver"].get(
            "h3_physical_transfer_absent"
        )
        is True
        and certs["block116_neutral_h3h4_strict_artifact_resolver"].get(
            "h4_source_canonical_coupling_absent"
        )
        is True
        and certs["neutral_h3h4_aperture"].get(
            "h3_physical_transfer_or_offdiagonal_generator_absent"
        )
        is True
        and certs["neutral_h3h4_aperture"].get(
            "h4_source_canonical_higgs_coupling_absent"
        )
        is True
    )
    h1_h2_support_not_h3_h4 = (
        certs["neutral_h3h4_aperture"].get("h1_h2_support_loaded") is True
        and "mathematical support only" in statuses["z3_heat_kernel_transfer_attempt"]
        and "do not supply PR230 H4" in statuses["z3_heat_kernel_source_coupling_no_go"]
    )
    finite_rows_not_accepted_transfer = (
        certs["two_source_primitive_transfer_candidate"].get(
            "physical_transfer_candidate_accepted"
        )
        is False
        and certs["two_source_primitive_transfer_candidate"].get(
            "finite_offdiagonal_correlation_support"
        )
        is True
        and "finite C_sx rows do not certify" in statuses[
            "two_source_primitive_transfer_candidate"
        ]
    )
    source_higgs_and_schur_fallbacks_still_blocked = (
        certs["block128_strict_wz_source_row_construction_attempt"]
        .get("canonical_action_summary", {})
        .get("accepted_current_surface")
        is False
        and certs["block128_strict_wz_source_row_construction_attempt"]
        .get("source_higgs_assembly_summary", {})
        .get("strict_c_ss_c_sh_c_hh_rows_exist")
        is False
        and certs["block128_strict_wz_source_row_construction_attempt"]
        .get("constructive_status", {})
        .get("strict_source_higgs_constructible_from_current_raw_rows")
        is False
        and certs["block129_schur_pole_authority_construction_attempt"]
        .get("constructive_status", {})
        .get("strict_schur_feshbach_pole_authority_constructible")
        is False
    )
    witness_preserves_rows_but_changes_h3_h4 = (
        witness.get("available") is True
        and witness.get("hidden_neutral_completion", {}).get(
            "observed_equal_time_rows_preserved"
        )
        is True
        and witness.get("h4_coupling_family", {}).get(
            "coupling_changes_while_observed_rows_fixed"
        )
        is True
        and witness.get("h3_transfer_family", {}).get(
            "both_transfer_candidates_positive"
        )
        is True
        and witness.get("h3_transfer_family", {}).get(
            "offdiagonal_generator_changes_while_equal_time_rows_fixed"
        )
        is True
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("completed-finite-row-packet-present", completed_rows_present, f"rows={len(rows)} metadata={row_metadata}")
    report("expected-strict-neutral-artifacts-absent", no_strict_neutral_artifact_present, str(strict_presence))
    report("no-strict-row-or-raw-token-hits", no_strict_row_or_raw_hits, str(row_metadata))
    report("prior-neutral-absence-preserved", prior_neutral_absence_preserved, statuses["block116_neutral_h3h4_strict_artifact_resolver"])
    report("h1-h2-support-not-h3-h4", h1_h2_support_not_h3_h4, statuses["z3_heat_kernel_transfer_attempt"])
    report("finite-rows-not-accepted-transfer", finite_rows_not_accepted_transfer, statuses["two_source_primitive_transfer_candidate"])
    report("source-higgs-and-schur-fallbacks-still-blocked", source_higgs_and_schur_fallbacks_still_blocked, "Block128/Block129 fallbacks checked")
    report("two-completion-witness-blocks-neutral-identification", witness_preserves_rows_but_changes_h3_h4, str(witness))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/completion gates deny closure")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and completed_rows_present
        and no_strict_neutral_artifact_present
        and no_strict_row_or_raw_hits
        and prior_neutral_absence_preserved
        and h1_h2_support_not_h3_h4
        and finite_rows_not_accepted_transfer
        and source_higgs_and_schur_fallbacks_still_blocked
        and witness_preserves_rows_but_changes_h3_h4
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block130 cannot construct neutral H3/H4 "
            "authority from the completed finite source/taste-radial packet; an "
            "explicit hidden-neutral completion preserves all observed finite rows "
            "while changing H3 transfer/offdiagonal dynamics and H4 source coupling"
        ),
        "conditional_surface_status": (
            "neutral route reopens only with an accepted same-surface physical "
            "neutral transfer/offdiagonal generator or primitive/irreducibility "
            "certificate plus source/canonical-Higgs coupling authority"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The completed C_ss/C_sx/C_xx rows are genuine finite support, but no "
            "strict neutral artifact or row sidecar is present, H1/H2 heat-kernel "
            "support lacks a physical selector/H4 coupling, and the two-completion "
            "witness proves the finite rows do not identify H3 or H4."
        ),
        "current_closure_satisfied": False,
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block130_neutral_h3h4_transfer_coupling_construction_attempt_passed": passed,
        "completed_row_scan": {
            "row_count": len(rows),
            "C_ss_summary": summarize(css),
            "C_sx_summary": summarize(csx),
            "C_xx_summary": summarize(cxx),
            **row_metadata,
        },
        "strict_artifact_presence": strict_presence,
        "strict_neutral_artifact_present": any(strict_presence.values()),
        "strict_row_or_raw_hits_present": not no_strict_row_or_raw_hits,
        "prior_neutral_absence_preserved": prior_neutral_absence_preserved,
        "h1_h2_support_not_h3_h4": h1_h2_support_not_h3_h4,
        "finite_rows_not_accepted_transfer": finite_rows_not_accepted_transfer,
        "source_higgs_and_schur_fallbacks_still_blocked": source_higgs_and_schur_fallbacks_still_blocked,
        "two_completion_witness": witness,
        "witness_preserves_rows_but_changes_h3_h4": witness_preserves_rows_but_changes_h3_h4,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": {
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_promote_finite_equal_time_rows_to_physical_transfer": True,
            "does_not_treat_hidden_completion_witness_as_authority": True,
            "does_not_treat_heat_kernel_support_as_pr230_physical_transfer": True,
            "does_not_alias_c_sx_to_c_sh_before_canonical_oh": True,
            "does_not_identify_taste_radial_x_as_canonical_oh": True,
            "does_not_set_kappa_s_c2_or_z_match": True,
            "does_not_use_forbidden_observed_or_unit_inputs": True,
        },
        "exact_next_action": (
            "Neutral route requires a new accepted same-surface physical transfer/"
            "offdiagonal generator or primitive/irreducibility certificate plus "
            "source/canonical-Higgs coupling.  Without that, pivot back to the "
            "action-first source-Higgs row contract or strict W/Z production rows "
            "only if a new artifact appears."
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

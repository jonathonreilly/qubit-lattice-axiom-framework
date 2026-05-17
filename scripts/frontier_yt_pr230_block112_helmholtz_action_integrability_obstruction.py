#!/usr/bin/env python3
"""
PR #230 Block112 Helmholtz action-integrability obstruction.

The cleanest remaining positive route is still an accepted same-surface
EW/Higgs action plus canonical O_H and physical C_ss/C_sH/C_HH pole rows.
This runner attacks a narrower possible shortcut for that root:

    current source/response/correlator rows
        => integrable same-source EW/Higgs action coordinate
        => canonical source-Higgs overlap

The current surface does not contain the mixed response rows needed for that
inverse-variational step.  Finite source-only and taste-radial rows can share
the same current observables while either failing Helmholtz symmetry or
satisfying it with different source-Higgs overlap.  Therefore the action root
still needs a real same-surface action/canonical-O_H artifact or physical
source-Higgs/WZ response rows.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json"
)

ROW_PATTERN = (
    "outputs/yt_pr230_schur_higher_shell_rows/"
    "yt_pr230_schur_higher_shell_rows_L12_T24_chunk{chunk:03d}_2026-05-07.json"
)

PARENTS = {
    "block109_frontier_selector": "outputs/yt_pr230_block109_closure_root_frontier_selector_2026-05-17.json",
    "block110_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
    "block111_schur_kprime_packet_gap_audit": "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json",
    "fms_action_adoption_minimal_cut": "outputs/yt_pr230_fms_action_adoption_minimal_cut_2026-05-07.json",
    "same_source_ew_higgs_action_ansatz": "outputs/yt_pr230_same_source_ew_higgs_action_ansatz_gate_2026-05-06.json",
    "same_source_ew_action_adoption_attempt": "outputs/yt_pr230_same_source_ew_action_adoption_attempt_2026-05-06.json",
    "canonical_oh_wz_common_action_cut": "outputs/yt_pr230_canonical_oh_wz_common_action_cut_2026-05-07.json",
    "canonical_oh_hard_residual": "outputs/yt_pr230_canonical_oh_hard_residual_equivalence_gate_2026-05-07.json",
    "source_higgs_overlap_kappa_contract": "outputs/yt_pr230_source_higgs_overlap_kappa_contract_2026-05-06.json",
    "source_higgs_direct_pole_row_contract": "outputs/yt_pr230_source_higgs_direct_pole_row_contract_2026-05-07.json",
    "wz_physical_response_packet_intake": "outputs/yt_pr230_wz_physical_response_packet_intake_checkpoint_2026-05-07.json",
    "top_wz_covariance_theorem_import_audit": "outputs/yt_top_wz_covariance_theorem_import_audit_2026-05-05.json",
    "complete_packet_monotonicity": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
}

STRICT_ACTION_OR_RESPONSE_PATHS = {
    "same_surface_ew_higgs_action_certificate": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-07.json",
    "accepted_same_source_ew_action_certificate": "outputs/yt_wz_same_source_ew_action_certificate_2026-05-04.json",
    "canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "source_higgs_measurement_rows": "outputs/yt_source_higgs_cross_correlator_measurement_rows_2026-05-03.json",
    "wz_response_rows": "outputs/yt_pr230_wz_response_rows_2026-05-07.json",
    "top_wz_matched_covariance_rows": "outputs/yt_pr230_top_wz_matched_covariance_rows_2026-05-05.json",
    "delta_perp_tomography_rows": "outputs/yt_pr230_delta_perp_tomography_rows_2026-05-04.json",
}

EXPECTED_CHUNKS = 63
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

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_pilots_as_production_evidence": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_g2_equal_one": False,
    "treated_helmholtz_counterfamily_as_physical_model": False,
    "treated_finite_c_sx_c_xx_as_canonical_c_sh_c_hh": False,
    "treated_taste_radial_x_as_canonical_O_H": False,
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


def first_ensemble(data: dict[str, Any]) -> dict[str, Any]:
    ensembles = data.get("ensembles")
    if isinstance(ensembles, list) and len(ensembles) == 1 and isinstance(ensembles[0], dict):
        return ensembles[0]
    return {}


def row_path(chunk: int) -> Path:
    return ROOT / ROW_PATTERN.format(chunk=chunk)


def finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def audit_higher_shell_rows() -> dict[str, Any]:
    issues: dict[str, list[str]] = {}
    checked = 0
    finite_alias_chunks = 0
    canonical_identity_false_chunks = 0
    source_time_kernel_nonempty_chunks = 0
    wz_response_nonempty_chunks = 0
    scalar_source_response_chunks = 0

    for chunk in range(1, EXPECTED_CHUNKS + 1):
        path = row_path(chunk)
        data = load_json(path)
        chunk_issues: list[str] = []
        if not data:
            issues[f"chunk{chunk:03d}"] = ["row JSON missing"]
            continue
        checked += 1
        ensemble = first_ensemble(data)
        source = (
            ensemble.get("source_higgs_cross_correlator_analysis")
            if isinstance(ensemble.get("source_higgs_cross_correlator_analysis"), dict)
            else {}
        )
        time_kernel = (
            ensemble.get("source_higgs_time_kernel_analysis")
            if isinstance(ensemble.get("source_higgs_time_kernel_analysis"), dict)
            else {}
        )
        response = (
            ensemble.get("scalar_source_response_analysis")
            if isinstance(ensemble.get("scalar_source_response_analysis"), dict)
            else {}
        )
        wz = (
            ensemble.get("wz_mass_response_analysis")
            if isinstance(ensemble.get("wz_mass_response_analysis"), dict)
            else {}
        )
        aliases = (
            source.get("two_source_taste_radial_row_aliases")
            if isinstance(source.get("two_source_taste_radial_row_aliases"), dict)
            else {}
        )
        mode_rows = source.get("mode_rows") if isinstance(source.get("mode_rows"), dict) else {}
        if set(mode_rows) != EXPECTED_MODES:
            chunk_issues.append("source mode set mismatch")
        finite_alias_ok = (
            aliases.get("C_sx_aliases_C_sH_schema_field") is True
            and aliases.get("C_xx_aliases_C_HH_schema_field") is True
            and source.get("used_as_physical_yukawa_readout") is False
        )
        if finite_alias_ok:
            finite_alias_chunks += 1
        if source.get("canonical_higgs_operator_identity_passed") is False:
            canonical_identity_false_chunks += 1
        if isinstance(time_kernel.get("mode_rows"), dict) and time_kernel.get("mode_rows"):
            source_time_kernel_nonempty_chunks += 1
        if isinstance(wz.get("per_source_shift_rows"), list) and wz.get("per_source_shift_rows"):
            wz_response_nonempty_chunks += 1
        slopes = response.get("per_configuration_slopes")
        if (
            isinstance(slopes, list)
            and slopes
            and all(
                isinstance(item, dict)
                and item.get("finite") is True
                and finite(item.get("slope_effective_energy_tau1"))
                for item in slopes
            )
        ):
            scalar_source_response_chunks += 1
        if chunk_issues:
            issues[f"chunk{chunk:03d}"] = chunk_issues

    return {
        "checked_chunks": checked,
        "issues": issues,
        "finite_taste_radial_alias_chunks": finite_alias_chunks,
        "canonical_higgs_identity_false_chunks": canonical_identity_false_chunks,
        "source_higgs_time_kernel_nonempty_chunks": source_time_kernel_nonempty_chunks,
        "wz_response_nonempty_chunks": wz_response_nonempty_chunks,
        "scalar_source_response_chunks": scalar_source_response_chunks,
    }


def helmholtz_counterfamily() -> dict[str, Any]:
    """
    Finite inverse-variational witness.

    A local response one-form alpha_i(x) is a gradient of an action only if the
    mixed Jacobian is symmetric.  The current source-only rows do not supply the
    mixed canonical source-Higgs derivatives.  Even after imposing symmetry,
    multiple positive quadratic actions share the same source-source block and
    differ in source-Higgs overlap.
    """
    nonintegrable = np.array([[1.0, 0.20], [0.70, 1.0]], dtype=float)
    nonintegrable_curl = float(nonintegrable[0, 1] - nonintegrable[1, 0])

    symmetric_rows: list[dict[str, Any]] = []
    for lam in (0.0, 0.25, 0.60):
        hessian = np.array([[1.0, lam], [lam, 1.0]], dtype=float)
        eigvals = np.linalg.eigvalsh(hessian)
        overlap = lam / math.sqrt(hessian[0, 0] * hessian[1, 1])
        symmetric_rows.append(
            {
                "lambda_source_higgs": lam,
                "hessian": hessian.tolist(),
                "eigenvalues": eigvals.tolist(),
                "positive_definite": bool(np.all(eigvals > 0.0)),
                "helmholtz_symmetric": bool(np.allclose(hessian, hessian.T)),
                "source_source_block": float(hessian[0, 0]),
                "higgs_higgs_block": float(hessian[1, 1]),
                "normalized_source_higgs_overlap": overlap,
            }
        )

    source_only_signature = {
        "source_source_block": 1.0,
        "source_direction_linear_response": "held fixed in all rows",
        "canonical_higgs_identity": "not observed",
        "mixed_source_higgs_derivative": "not observed",
    }
    distinct_overlaps = sorted(float(row["normalized_source_higgs_overlap"]) for row in symmetric_rows)
    return {
        "nonintegrable_same_source_signature_example": {
            "jacobian": nonintegrable.tolist(),
            "helmholtz_curl_H_sh_minus_H_hs": nonintegrable_curl,
            "helmholtz_condition_passed": abs(nonintegrable_curl) < 1.0e-12,
            "meaning": (
                "Without both mixed rows H_sh and H_hs, the current data cannot "
                "test whether the response one-form is action-integrable."
            ),
        },
        "integrable_same_source_signature_family": symmetric_rows,
        "shared_source_only_signature": source_only_signature,
        "distinct_source_higgs_overlaps": distinct_overlaps,
        "counterfamily_passed": bool(
            abs(nonintegrable_curl) > 1.0e-12
            and all(row["positive_definite"] and row["helmholtz_symmetric"] for row in symmetric_rows)
            and len(distinct_overlaps) == len(symmetric_rows)
        ),
        "strict_limit": (
            "This is a finite inverse-variational witness only.  It proves the "
            "missing-row non-identifiability of the current source surface; it "
            "does not model PR230 dynamics or supply physical y_t evidence."
        ),
    }


def main() -> int:
    print("PR #230 Block112 Helmholtz action-integrability obstruction")
    print("=" * 78)

    parents = {name: load_json(path) for name, path in PARENTS.items()}
    parent_statuses = {name: status(cert) for name, cert in parents.items()}
    missing_parents = [name for name, cert in parents.items() if not cert]
    parent_proposals = [name for name, cert in parents.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in STRICT_ACTION_OR_RESPONSE_PATHS.items()
    }
    row_audit = audit_higher_shell_rows()
    counterfamily = helmholtz_counterfamily()

    block109_selects_action_root = (
        parents["block109_frontier_selector"].get("selected_next_artifact_family")
        == "O_H_action_plus_source_higgs_pole_rows"
        and parents["block109_frontier_selector"].get("goal_complete") is False
        and parents["block109_frontier_selector"].get("proposal_allowed") is False
    )
    block110_blocks_finite_algebra_action = (
        parents["block110_action_descent_obstruction"].get(
            "block110_cl3_z3_action_descent_obstruction_passed"
        )
        is True
        and parents["block110_action_descent_obstruction"].get("proposal_allowed") is False
    )
    block111_blocks_schur_shortcut = (
        parents["block111_schur_kprime_packet_gap_audit"].get(
            "block111_schur_kprime_packet_gap_audit_passed"
        )
        is True
        and parents["block111_schur_kprime_packet_gap_audit"].get(
            "strict_kprime_row_emissions_present"
        )
        is False
    )
    action_or_response_absent = not any(strict_presence.values())
    fms_cut_still_open = (
        parents["fms_action_adoption_minimal_cut"].get(
            "fms_action_adoption_minimal_cut_passed"
        )
        is True
        and parents["fms_action_adoption_minimal_cut"].get("proposal_allowed") is False
    )
    ansatz_not_adopted = (
        parents["same_source_ew_higgs_action_ansatz"].get(
            "current_surface_adoption_passed"
        )
        is False
        and parents["same_source_ew_action_adoption_attempt"].get(
            "same_source_ew_action_adoption_attempt_passed"
        )
        is True
    )
    canonical_oh_open = (
        parents["canonical_oh_hard_residual"].get(
            "canonical_oh_hard_residual_equivalence_gate_passed"
        )
        is True
        and parents["canonical_oh_hard_residual"].get("proposal_allowed") is False
    )
    physical_rows_absent = (
        row_audit["checked_chunks"] == EXPECTED_CHUNKS
        and not row_audit["issues"]
        and row_audit["finite_taste_radial_alias_chunks"] == EXPECTED_CHUNKS
        and row_audit["canonical_higgs_identity_false_chunks"] == EXPECTED_CHUNKS
        and row_audit["source_higgs_time_kernel_nonempty_chunks"] == 0
        and row_audit["wz_response_nonempty_chunks"] == 0
    )
    helmholtz_mixed_rows_absent = (
        physical_rows_absent
        and parents["source_higgs_overlap_kappa_contract"].get("proposal_allowed") is False
        and parents["source_higgs_direct_pole_row_contract"].get("proposal_allowed") is False
        and parents["wz_physical_response_packet_intake"].get("proposal_allowed") is False
        and parents["top_wz_covariance_theorem_import_audit"].get("proposal_allowed") is False
    )
    counterfamily_blocks_inference = counterfamily["counterfamily_passed"] is True
    aggregate_gates_deny_proposal = (
        parents["full_positive_assembly"].get("proposal_allowed") is False
        and parents["retained_route"].get("proposal_allowed") is False
        and parents["campaign_status"].get("proposal_allowed") is False
    )
    forbidden_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("no-parent-authorizes-proposal", not parent_proposals, f"proposal_allowed={parent_proposals}")
    report("block109-selects-action-root", block109_selects_action_root, parent_statuses["block109_frontier_selector"])
    report("block110-finite-algebra-action-shortcut-blocked", block110_blocks_finite_algebra_action, parent_statuses["block110_action_descent_obstruction"])
    report("block111-schur-shortcut-blocked", block111_blocks_schur_shortcut, parent_statuses["block111_schur_kprime_packet_gap_audit"])
    report("strict-action-or-response-artifacts-absent", action_or_response_absent, str(strict_presence))
    report("fms-action-adoption-cut-still-open", fms_cut_still_open, parent_statuses["fms_action_adoption_minimal_cut"])
    report("same-source-ew-higgs-ansatz-not-adopted", ansatz_not_adopted, parent_statuses["same_source_ew_higgs_action_ansatz"])
    report("canonical-oh-hard-residual-open", canonical_oh_open, parent_statuses["canonical_oh_hard_residual"])
    report("completed-packet-has-only-noncanonical-finite-alias-rows", physical_rows_absent, str(row_audit))
    report("helmholtz-mixed-response-rows-absent", helmholtz_mixed_rows_absent, "no canonical C_sH/C_HH, W/Z covariance, or action Hessian rows")
    report("helmholtz-counterfamily-blocks-source-only-inference", counterfamily_blocks_inference, str(counterfamily["distinct_source_higgs_overlaps"]))
    report("aggregate-gates-deny-proposal", aggregate_gates_deny_proposal, "assembly/retained/campaign proposal_allowed=false")
    report("does-not-authorize-retained-proposal", True, "inverse-variational obstruction only")
    report("forbidden-firewall-clean", forbidden_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing_parents
        and not parent_proposals
        and block109_selects_action_root
        and block110_blocks_finite_algebra_action
        and block111_blocks_schur_shortcut
        and action_or_response_absent
        and fms_cut_still_open
        and ansatz_not_adopted
        and canonical_oh_open
        and physical_rows_absent
        and helmholtz_mixed_rows_absent
        and counterfamily_blocks_inference
        and aggregate_gates_deny_proposal
        and forbidden_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block112 current PR230 response surface lacks "
            "Helmholtz mixed-derivative rows for accepted same-source EW/Higgs action"
        ),
        "conditional_surface_status": (
            "exact support only after a future accepted same-surface action or physical "
            "response packet supplies canonical O_H, source-Higgs or W/Z mixed response "
            "rows, covariance, absolute normalization authority, and FV/IR/contact limits"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current surface has source-only responses and finite taste-radial "
            "C_ss/C_sx/C_xx aliases, but lacks the canonical mixed derivatives needed "
            "to integrate a same-source EW/Higgs action or fix source-Higgs overlap.  "
            "The finite counterfamily shows identical source-only signatures with "
            "different integrable source-Higgs overlaps."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block112_helmholtz_action_integrability_obstruction_passed": passed,
        "strict_action_or_response_artifact_presence": strict_presence,
        "higher_shell_row_audit": row_audit,
        "helmholtz_counterfamily": counterfamily,
        "helmholtz_mixed_response_rows_present": False,
        "same_source_action_integrability_authority_present": False,
        "canonical_source_higgs_overlap_fixed": False,
        "parent_certificates": PARENTS,
        "parent_statuses": parent_statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not infer an accepted EW/Higgs action from source-only or taste-radial finite rows",
            "does not identify taste-radial x with canonical O_H",
            "does not relabel C_sx/C_xx as physical C_sH/C_HH pole rows",
            "does not treat the finite Helmholtz counterfamily as a PR230 dynamics model",
            "does not set kappa_s = 1, c2 = 1, Z_match = 1, or g2 = 1",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
        ],
        "exact_next_action": (
            "Supply one accepted mixed-response/action artifact: a same-surface EW/Higgs "
            "action certificate with Helmholtz-symmetric source/Higgs/WZ response Hessian "
            "rows, canonical O_H and C_ss/C_sH/C_HH pole rows, or a strict W/Z packet "
            "with matched top-W/Z covariance and an allowed absolute pin.  Do not promote "
            "source-only or finite taste-radial rows to an action-integrability certificate."
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

#!/usr/bin/env python3
"""
PR #230 Block119 native Dirichlet action/LSZ probe.

Block118 fixes the finite taste-radial axis from the native Hamming-Dirichlet
form on the current Cl(3)/Z3 source/taste Boolean cube.  This block tests the
next optimistic lift:

    selected finite O_H axis + native graph Dirichlet quadratic form
        => accepted EW/Higgs action, scalar LSZ/canonical normalization,
           source-overlap authority, and physical C_ss/C_sH/C_HH rows.

The result is support plus boundary.  A finite spatial Dirichlet quadratic form
can be built and normalized mathematically on the selected axis, but that does
not derive the PR230 same-surface EW/Higgs action, the source derivative
dS/ds=sum O_H, the canonical Higgs radial field, kappa_sH, or strict physical
pole rows.
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
    / "yt_pr230_block119_native_dirichlet_action_lsz_probe_2026-05-17.json"
)

PARENTS = {
    "block118_hamming_dirichlet_axis": "outputs/yt_pr230_block118_hamming_dirichlet_oh_axis_selector_2026-05-17.json",
    "block110_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
    "block112_helmholtz_obstruction": "outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json",
    "block114_source_higgs_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "canonical_scalar_import_audit": "outputs/yt_canonical_scalar_normalization_import_audit_2026-05-01.json",
    "source_functional_lsz_identifiability": "outputs/yt_source_functional_lsz_identifiability_theorem_2026-05-03.json",
    "canonical_oh_action_lsz_closure": "outputs/yt_canonical_oh_action_lsz_closure_2026-05-12.json",
    "same_source_ew_higgs_action_ansatz": "outputs/yt_pr230_same_source_ew_higgs_action_ansatz_gate_2026-05-06.json",
    "fms_source_overlap_readout_gate": "outputs/yt_pr230_fms_source_overlap_readout_gate_2026-05-07.json",
    "source_higgs_direct_pole_contract": "outputs/yt_pr230_source_higgs_direct_pole_row_contract_2026-05-07.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

STRICT_AUTHORITY_PATHS = {
    "accepted_same_surface_ew_higgs_action": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-07.json",
    "accepted_same_source_ew_higgs_action": "outputs/yt_pr230_same_source_ew_higgs_action_certificate_2026-05-06.json",
    "accepted_canonical_oh": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "source_higgs_pole_residue_packet": "outputs/yt_pr230_source_higgs_pole_residue_packet_2026-05-07.json",
    "source_higgs_production_certificate": "outputs/yt_source_higgs_cross_correlator_production_certificate_2026-05-03.json",
    "same_source_w_response_rows": "outputs/yt_same_source_w_response_rows_2026-05-04.json",
    "neutral_h3h4_certificate": "outputs/yt_pr230_neutral_h3h4_certificate_2026-05-17.json",
    "strict_schur_feshbach_rows": "outputs/yt_pr230_strict_schur_feshbach_kprime_rows_2026-05-17.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_higgs_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_planck_or_alpha_s_surface": False,
    "used_reduced_cold_pilots_as_production_evidence": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "set_g2_equal_one": False,
    "treated_dirichlet_quadratic_as_accepted_ew_higgs_action": False,
    "treated_graph_normalization_as_scalar_lsz_metric": False,
    "treated_selected_axis_as_source_overlap": False,
    "renamed_C_sx_C_xx_as_C_sH_C_HH": False,
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


def dirichlet_path_laplacian(interior_sites: int) -> np.ndarray:
    """Interior Dirichlet Laplacian for a one-dimensional path."""
    laplacian = np.zeros((interior_sites, interior_sites), dtype=float)
    for i in range(interior_sites):
        laplacian[i, i] = 2.0
        if i > 0:
            laplacian[i, i - 1] = -1.0
        if i + 1 < interior_sites:
            laplacian[i, i + 1] = -1.0
    return laplacian


def normalized_lowest_mode(laplacian: np.ndarray) -> dict[str, Any]:
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    order = np.argsort(eigenvalues)
    lowest = int(order[0])
    vector = eigenvectors[:, lowest]
    if vector.sum() < 0:
        vector = -vector
    rayleigh = float(vector.T @ laplacian @ vector)
    residual = float(np.max(np.abs(laplacian @ vector - eigenvalues[lowest] * vector)))
    return {
        "eigenvalues": [float(value) for value in eigenvalues],
        "lowest_eigenvalue": float(eigenvalues[lowest]),
        "lowest_mode": [float(value) for value in vector],
        "lowest_mode_norm": float(np.linalg.norm(vector)),
        "rayleigh_quotient": rayleigh,
        "eigen_residual_max_abs": residual,
        "strictly_positive_spectrum": bool(np.min(eigenvalues) > 0.0),
    }


def finite_dirichlet_candidate() -> dict[str, Any]:
    spatial_laplacian = dirichlet_path_laplacian(4)
    spatial = normalized_lowest_mode(spatial_laplacian)

    # Block118 already selected a one-dimensional internal axis.  The tensor
    # product candidate on that axis has the same positive spatial spectrum.
    selected_axis_projector = np.array([[1.0]])
    tensor_laplacian = np.kron(spatial_laplacian, selected_axis_projector)
    tensor = normalized_lowest_mode(tensor_laplacian)
    symmetric = bool(np.allclose(tensor_laplacian, tensor_laplacian.T))
    row_sum_boundary_not_zero = [float(value) for value in tensor_laplacian.sum(axis=1)]
    quadratic_examples = []
    for scale in (0.5, 1.0, 2.0):
        mode = np.array(tensor["lowest_mode"], dtype=float) * scale
        quadratic_examples.append(
            {
                "field_scale": scale,
                "quadratic_action": float(0.5 * mode.T @ tensor_laplacian @ mode),
                "canonical_coordinate_norm": float(np.linalg.norm(mode)),
            }
        )
    return {
        "spatial_laplacian": spatial_laplacian.tolist(),
        "spatial_dirichlet_spectrum": spatial,
        "selected_axis_dimension": 1,
        "tensor_laplacian": tensor_laplacian.tolist(),
        "tensor_spectrum": tensor,
        "tensor_laplacian_symmetric": symmetric,
        "tensor_laplacian_strictly_positive": tensor["strictly_positive_spectrum"],
        "row_sums_show_dirichlet_boundary_not_periodic_zero_mode": row_sum_boundary_not_zero,
        "quadratic_examples": quadratic_examples,
        "mathematical_candidate_summary": (
            "A finite graph Dirichlet quadratic form can be normalized on the "
            "Block118 selected internal axis. This is only a dimensionless "
            "quadratic candidate, not an adopted PR230 EW/Higgs action."
        ),
    }


def source_overlap_scaling_orbit() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    reference_source_slope = 0.19
    reference_lsz_derivative = 7.0
    for scale in (0.5, 1.0, 2.0):
        # Same-source FH/LSZ product is invariant under source-coordinate
        # rescaling, while forbidden direct dE/ds readouts are not.
        d_e_ds = reference_source_slope / scale
        d_gamma_dp2 = reference_lsz_derivative * scale * scale
        rows.append(
            {
                "source_coordinate_scale": scale,
                "dE_top_ds": d_e_ds,
                "dGamma_ss_dp2_at_pole": d_gamma_dp2,
                "same_source_lsz_product": d_e_ds * math.sqrt(d_gamma_dp2),
                "forbidden_kappa_s_equals_one_readout": d_e_ds,
            }
        )
    return rows


def main() -> int:
    print("PR #230 Block119 native Dirichlet action/LSZ probe")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / rel).exists() for name, rel in STRICT_AUTHORITY_PATHS.items()
    }

    candidate = finite_dirichlet_candidate()
    scaling_orbit = source_overlap_scaling_orbit()
    invariant_products = [
        row["same_source_lsz_product"] for row in scaling_orbit
    ]
    forbidden_readouts = [
        row["forbidden_kappa_s_equals_one_readout"] for row in scaling_orbit
    ]

    block118_axis_loaded = (
        certs["block118_hamming_dirichlet_axis"].get(
            "block118_hamming_dirichlet_oh_axis_selector_passed"
        )
        is True
        and certs["block118_hamming_dirichlet_axis"].get("selector_exact_support")
        is True
        and certs["block118_hamming_dirichlet_axis"].get("proposal_allowed") is False
    )
    native_dirichlet_candidate_constructed = (
        candidate["tensor_laplacian_symmetric"]
        and candidate["tensor_laplacian_strictly_positive"]
        and candidate["tensor_spectrum"]["eigen_residual_max_abs"] < 1.0e-12
    )
    finite_kinetic_normalization_mathematically_available = (
        native_dirichlet_candidate_constructed
        and abs(candidate["tensor_spectrum"]["lowest_mode_norm"] - 1.0) < 1.0e-12
        and candidate["tensor_spectrum"]["lowest_eigenvalue"] > 0.0
    )
    accepted_same_surface_action_absent = (
        certs["block110_action_descent_obstruction"].get(
            "block110_cl3_z3_action_descent_obstruction_passed"
        )
        is True
        and certs["same_source_ew_higgs_action_ansatz"].get(
            "current_surface_adoption_passed"
        )
        is False
        and certs["canonical_oh_action_lsz_closure"].get("accepted_current_surface")
        is False
        and not strict_presence["accepted_same_surface_ew_higgs_action"]
        and not strict_presence["accepted_same_source_ew_higgs_action"]
    )
    scalar_lsz_canonical_metric_absent = (
        "No hidden retained current-surface theorem fixes kappa_s"
        in str(certs["canonical_scalar_import_audit"].get("verdict", ""))
        and certs["canonical_oh_action_lsz_closure"].get("closure_succeeds") is False
        and "scalar LSZ metric" in statuses["block110_action_descent_obstruction"]
    )
    source_overlap_not_fixed = (
        certs["fms_source_overlap_readout_gate"].get("readout_executable_now") is False
        and certs["fms_source_overlap_readout_gate"].get("strict_rows_present") is False
        and certs["block112_helmholtz_obstruction"].get(
            "canonical_source_higgs_overlap_fixed"
        )
        is False
        and certs["block112_helmholtz_obstruction"].get(
            "helmholtz_mixed_response_rows_present"
        )
        is False
        and max(invariant_products) - min(invariant_products) < 1.0e-12
        and max(forbidden_readouts) - min(forbidden_readouts) > 0.1
    )
    physical_pole_rows_absent = (
        certs["block114_source_higgs_resolver"].get("canonical_oh_certificate_absent")
        is True
        and certs["block114_source_higgs_resolver"].get(
            "accepted_same_source_action_absent"
        )
        is True
        and certs["block114_source_higgs_resolver"].get(
            "strict_source_higgs_pole_rows_absent"
        )
        is True
        and not strict_presence["source_higgs_pole_rows"]
        and not strict_presence["source_higgs_pole_residue_packet"]
        and not strict_presence["source_higgs_production_certificate"]
    )
    source_functional_identifiability_blocks_source_only_lift = (
        "source-only pole data do not determine the overlap"
        in str(certs["source_functional_lsz_identifiability"].get("verdict", ""))
        and certs["source_functional_lsz_identifiability"].get("proposal_allowed")
        is False
    )
    aggregate_gates_still_deny_closure = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and "retained closure not achieved" in statuses["completion_audit"]
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())
    block119_passed = (
        not missing
        and not proposals
        and block118_axis_loaded
        and native_dirichlet_candidate_constructed
        and finite_kinetic_normalization_mathematically_available
        and accepted_same_surface_action_absent
        and scalar_lsz_canonical_metric_absent
        and source_overlap_not_fixed
        and physical_pole_rows_absent
        and source_functional_identifiability_blocks_source_only_lift
        and aggregate_gates_still_deny_closure
        and firewall_clean
    )

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("block118-selected-axis-loaded", block118_axis_loaded, statuses["block118_hamming_dirichlet_axis"])
    report("native-dirichlet-quadratic-candidate-constructed", native_dirichlet_candidate_constructed, str(candidate["tensor_spectrum"]))
    report("finite-kinetic-normalization-mathematically-available", finite_kinetic_normalization_mathematically_available, "unit lowest mode on positive Dirichlet form")
    report("accepted-same-surface-action-absent", accepted_same_surface_action_absent, str(strict_presence))
    report("scalar-lsz-canonical-metric-absent", scalar_lsz_canonical_metric_absent, statuses["canonical_oh_action_lsz_closure"])
    report("source-overlap-not-fixed", source_overlap_not_fixed, str(scaling_orbit))
    report("physical-source-higgs-pole-rows-absent", physical_pole_rows_absent, statuses["block114_source_higgs_resolver"])
    report("source-functional-identifiability-blocks-source-only-lift", source_functional_identifiability_blocks_source_only_lift, statuses["source_functional_lsz_identifiability"])
    report("aggregate-gates-still-deny-closure", aggregate_gates_still_deny_closure, statuses["completion_audit"])
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))
    report("block119-native-dirichlet-action-lsz-probe-passed", block119_passed, "support plus boundary; no closure")

    result: dict[str, Any] = {
        "certificate_kind": "pr230_block119_native_dirichlet_action_lsz_probe",
        "actual_current_surface_status": (
            "exact support plus boundary / Block119 native spatial Dirichlet "
            "tensor-product probe gives a mathematical kinetic candidate for "
            "the Block118 selected O_H axis, but it is not an accepted "
            "EW/Higgs action, scalar LSZ/canonical normalization, "
            "source-overlap theorem, or strict C_ss/C_sH/C_HH pole-row "
            "authority"
        ),
        "conditional_surface_status": (
            "source-Higgs support if a future accepted same-surface EW/Higgs "
            "action adopts the Block118 axis, derives the canonical scalar LSZ "
            "metric and source derivative, and production physical Euclidean "
            "C_ss/C_sH/C_HH(tau) pole rows pass Gram, threshold, FV/IR, "
            "contact, and covariance gates"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The native Dirichlet quadratic form is only a finite mathematical "
            "candidate. It does not adopt or derive the same-surface EW/Higgs "
            "action, kappa_sH/source overlap, canonical Higgs radial field, "
            "physical pole rows, W/Z response, Schur/Feshbach pole authority, "
            "or neutral H3/H4 bridge."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "parent_statuses": statuses,
        "strict_authority_path_presence": strict_presence,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "finite_dirichlet_candidate": candidate,
        "source_overlap_scaling_orbit": scaling_orbit,
        "block118_axis_loaded": block118_axis_loaded,
        "native_dirichlet_candidate_constructed": native_dirichlet_candidate_constructed,
        "finite_kinetic_normalization_mathematically_available": finite_kinetic_normalization_mathematically_available,
        "accepted_same_surface_action_absent": accepted_same_surface_action_absent,
        "scalar_lsz_canonical_metric_absent": scalar_lsz_canonical_metric_absent,
        "source_overlap_not_fixed": source_overlap_not_fixed,
        "physical_source_higgs_pole_rows_absent": physical_pole_rows_absent,
        "source_functional_identifiability_blocks_source_only_lift": source_functional_identifiability_blocks_source_only_lift,
        "aggregate_gates_still_deny_closure": aggregate_gates_still_deny_closure,
        "native_dirichlet_action_lsz_probe_support_only": True,
        "block119_native_dirichlet_action_lsz_probe_passed": block119_passed,
        "minimal_allowed_premises": [
            "Block118 native Hamming-Dirichlet selected taste-radial axis as exact support only",
            "finite graph Dirichlet quadratic forms as mathematical candidates",
            "current PR230 action/LSZ/source-overlap/pole-row absence certificates",
            "source-functional identifiability and Helmholtz counterfamily firewalls",
        ],
        "open_imports_after_block119": [
            "accepted same-surface EW/Higgs action on the PR230 substrate",
            "canonical scalar LSZ/kinetic normalization tied to that action",
            "source derivative and source-to-canonical-Higgs overlap kappa_sH",
            "production physical Euclidean C_ss/C_sH/C_HH(tau) pole rows",
            "Gram flatness, threshold, FV/IR, contact, and covariance authority",
            "or a strict W/Z, Schur/scalar-LSZ, or neutral H3/H4 physical bridge",
        ],
        "claim_boundary": (
            "Block119 may be used only as a finite mathematical support and "
            "firewall artifact. It must not be used to set kappa_s, c2, "
            "Z_match, or g2 to one; to treat a graph normalization as scalar "
            "LSZ; or to relabel finite C_sx/C_xx rows as physical C_sH/C_HH."
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

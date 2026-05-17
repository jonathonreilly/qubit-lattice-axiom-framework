#!/usr/bin/env python3
"""
PR #230 Block110 Cl(3)/Z3 action-descent obstruction.

Block109 selected the cleanest remaining root: accepted same-surface EW/Higgs
action or canonical O_H, followed by strict physical C_ss/C_sH/C_HH rows.
This runner attacks the most optimistic first-principles shortcut for that
root:

    PR230 Cl(3)/Z3 source/taste algebra alone
        => dynamic EW/Higgs action, canonical O_H, scalar LSZ metric.

The current answer is no.  The PR230 Z3 taste/source subalgebra gives a real
degree-one radial axis, but as a finite semisimple source algebra it does not
contain a spacetime scalar field, kinetic/update semantics, radial background,
or a canonical pole metric.  Those must arrive through an accepted action
extension/theorem or through strict pole rows / a physical response bypass.
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
    / "yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json"
)

PARENTS = {
    "block109_frontier_selector": "outputs/yt_pr230_block109_closure_root_frontier_selector_2026-05-17.json",
    "degree_one_radial_tangent": "outputs/yt_pr230_degree_one_radial_tangent_oh_theorem_2026-05-07.json",
    "degree_one_action_premise": "outputs/yt_pr230_degree_one_higgs_action_premise_gate_2026-05-06.json",
    "fms_action_adoption_minimal_cut": "outputs/yt_pr230_fms_action_adoption_minimal_cut_2026-05-07.json",
    "fms_oh_candidate_action_packet": "outputs/yt_pr230_fms_oh_candidate_action_packet_2026-05-07.json",
    "lane1_action_premise": "outputs/yt_pr230_lane1_action_premise_derivation_attempt_2026-05-12.json",
    "block67_action_lsz_probe": "outputs/yt_pr230_block67_same_surface_canonical_oh_action_lsz_probe_2026-05-12.json",
    "hs_logdet_scalar_action_no_go": "outputs/yt_pr230_hs_logdet_scalar_action_normalization_no_go_2026-05-12.json",
    "canonical_oh_action_lsz": "outputs/yt_canonical_oh_action_lsz_closure_2026-05-12.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

STRICT_AUTHORITY_PATHS = {
    "same_surface_ew_higgs_action_certificate": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-07.json",
    "canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "source_higgs_pole_residue_packet": "outputs/yt_pr230_source_higgs_pole_residue_packet_2026-05-07.json",
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
    "treated_degree_one_axis_as_action": False,
    "treated_finite_source_algebra_as_dynamic_phi": False,
    "treated_fms_packet_as_adopted_action": False,
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


def pauli_x() -> np.ndarray:
    return np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)


def taste_axes() -> list[np.ndarray]:
    i2 = np.eye(2, dtype=complex)
    sx = pauli_x()
    return [
        np.kron(sx, np.kron(i2, i2)),
        np.kron(i2, np.kron(sx, i2)),
        np.kron(i2, np.kron(i2, sx)),
    ]


def hs_inner(a: np.ndarray, b: np.ndarray) -> complex:
    return complex(np.trace(a.conj().T @ b))


def hs_norm(a: np.ndarray) -> float:
    return math.sqrt(max(float(hs_inner(a, a).real), 0.0))


def normalize(a: np.ndarray) -> np.ndarray:
    norm = hs_norm(a)
    if norm == 0.0:
        raise ValueError("cannot normalize zero operator")
    return a / norm


def max_abs(a: np.ndarray) -> float:
    return float(np.max(np.abs(a)))


def matrix_rank(mats: list[np.ndarray], tol: float = 1.0e-12) -> int:
    rows = [mat.reshape(-1) for mat in mats]
    return int(np.linalg.matrix_rank(np.vstack(rows), tol=tol))


def generated_taste_monomials(axes: list[np.ndarray]) -> list[np.ndarray]:
    identity = np.eye(8, dtype=complex)
    s0, s1, s2 = axes
    return [
        identity,
        s0,
        s1,
        s2,
        s0 @ s1,
        s0 @ s2,
        s1 @ s2,
        s0 @ s1 @ s2,
    ]


def primitive_idempotents(axes: list[np.ndarray]) -> list[np.ndarray]:
    identity = np.eye(8, dtype=complex)
    s0, s1, s2 = axes
    projectors = []
    for eps0 in (-1.0, 1.0):
        for eps1 in (-1.0, 1.0):
            for eps2 in (-1.0, 1.0):
                projectors.append(
                    (identity + eps0 * s0)
                    @ (identity + eps1 * s1)
                    @ (identity + eps2 * s2)
                    / 8.0
                )
    return projectors


def z3_invariant_basis(axes: list[np.ndarray]) -> list[np.ndarray]:
    s0, s1, s2 = axes
    return [
        s0 + s1 + s2,
        s0 @ s1 + s1 @ s2 + s2 @ s0,
        s0 @ s1 @ s2,
    ]


def idempotent_derivation_obstruction(projectors: list[np.ndarray]) -> dict[str, Any]:
    """
    Finite commutative semisimple algebra derivation witness.

    In C^8, primitive idempotents e_i satisfy e_i^2=e_i and e_i e_j=0.  Any
    internal derivation D obeys D(e_i)=D(e_i^2)=2 e_i D(e_i), while applying D
    to sum_i e_i=1 gives sum_i D(e_i)=0.  Componentwise in the idempotent
    basis this forces D(e_i)=0 for every i.  The calculation below checks the
    projector/idempotent structure used by that proof.
    """
    identity = np.eye(8, dtype=complex)
    idempotent_errors = [max_abs(p @ p - p) for p in projectors]
    orthogonality_errors = []
    for i, p_i in enumerate(projectors):
        for j, p_j in enumerate(projectors):
            if i != j:
                orthogonality_errors.append(max_abs(p_i @ p_j))
    resolution_error = max_abs(sum(projectors, np.zeros((8, 8), dtype=complex)) - identity)
    return {
        "primitive_idempotent_count": len(projectors),
        "max_idempotent_error": max(idempotent_errors),
        "max_orthogonality_error": max(orthogonality_errors),
        "resolution_of_identity_error": resolution_error,
        "finite_semisimple_commutative_derivations_vanish": (
            max(idempotent_errors) < 1.0e-12
            and max(orthogonality_errors) < 1.0e-12
            and resolution_error < 1.0e-12
        ),
        "meaning": (
            "The finite PR230 source/taste algebra supplies idempotent labels "
            "and invariant axes, but no internal continuous scalar flow or "
            "kinetic/LSZ metric."
        ),
    }


def main() -> int:
    print("PR #230 Block110 Cl(3)/Z3 action-descent obstruction")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposal_parents = [
        name for name, cert in certs.items() if cert.get("proposal_allowed") is True
    ]
    strict_presence = {
        name: (ROOT / rel).exists() for name, rel in STRICT_AUTHORITY_PATHS.items()
    }

    axes = taste_axes()
    monomials = generated_taste_monomials(axes)
    projectors = primitive_idempotents(axes)
    invariant_basis = z3_invariant_basis(axes)
    algebra_dimension = matrix_rank(monomials)
    invariant_dimension = matrix_rank(invariant_basis)
    commutator_errors = [
        max_abs(a @ b - b @ a)
        for i, a in enumerate(monomials)
        for b in monomials[i + 1 :]
    ]
    radial_line = normalize(invariant_basis[0])
    radial_hs_norm = hs_norm(radial_line)
    derivation_obstruction = idempotent_derivation_obstruction(projectors)

    algebra_facts = {
        "generated_source_taste_algebra_dimension": algebra_dimension,
        "generated_source_taste_algebra_commutative": max(commutator_errors) < 1.0e-12,
        "max_commutator_error": max(commutator_errors),
        "z3_trace_zero_invariant_dimension": invariant_dimension,
        "degree_one_radial_axis_hs_norm": radial_hs_norm,
        "derivation_obstruction": derivation_obstruction,
    }

    block109_selects_route = (
        certs["block109_frontier_selector"].get("selected_next_artifact_family")
        == "O_H_action_plus_source_higgs_pole_rows"
        and certs["block109_frontier_selector"].get("goal_complete") is False
        and certs["block109_frontier_selector"].get("proposal_allowed") is False
    )
    degree_one_support_only = (
        "degree-one radial-tangent" in statuses["degree_one_radial_tangent"]
        and certs["degree_one_radial_tangent"].get("proposal_allowed") is False
        and certs["degree_one_action_premise"].get(
            "degree_one_premise_authorized_on_current_surface"
        )
        is False
    )
    fms_not_adopted = (
        certs["fms_action_adoption_minimal_cut"].get("proposal_allowed") is False
        and certs["fms_oh_candidate_action_packet"].get("accepted_current_surface")
        is False
        and certs["fms_oh_candidate_action_packet"].get("same_surface_cl3_z3_derived")
        is False
    )
    previous_action_attempts_block = (
        certs["lane1_action_premise"].get("exact_negative_boundary_passed") is True
        and certs["block67_action_lsz_probe"].get("current_surface_closure_possible")
        is False
        and certs["hs_logdet_scalar_action_no_go"].get(
            "hs_logdet_scalar_action_normalization_no_go_passed"
        )
        is True
        and certs["canonical_oh_action_lsz"].get("accepted_current_surface") is False
    )
    aggregate_denies_closure = (
        certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
    )
    strict_artifacts_absent = not any(strict_presence.values())
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    theorem_passed = (
        not missing
        and not proposal_parents
        and block109_selects_route
        and algebra_facts["generated_source_taste_algebra_dimension"] == 8
        and algebra_facts["generated_source_taste_algebra_commutative"]
        and algebra_facts["z3_trace_zero_invariant_dimension"] == 3
        and derivation_obstruction["finite_semisimple_commutative_derivations_vanish"]
        and degree_one_support_only
        and fms_not_adopted
        and previous_action_attempts_block
        and aggregate_denies_closure
        and strict_artifacts_absent
        and firewall_clean
    )

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposal_parents, f"proposal_allowed={proposal_parents}")
    report("block109-selects-action-root", block109_selects_route, statuses["block109_frontier_selector"])
    report("source-taste-algebra-dimension-8", algebra_dimension == 8, str(algebra_facts))
    report("source-taste-algebra-commutative", algebra_facts["generated_source_taste_algebra_commutative"], f"max_commutator={max(commutator_errors)}")
    report("z3-invariant-neutral-space-nonunique", invariant_dimension == 3, f"dimension={invariant_dimension}")
    report("finite-commutative-derivations-vanish", derivation_obstruction["finite_semisimple_commutative_derivations_vanish"], str(derivation_obstruction))
    report("degree-one-support-only", degree_one_support_only, statuses["degree_one_radial_tangent"])
    report("fms-action-not-adopted", fms_not_adopted, statuses["fms_action_adoption_minimal_cut"])
    report("previous-action-attempts-block", previous_action_attempts_block, statuses["lane1_action_premise"])
    report("aggregate-gates-deny-closure", aggregate_denies_closure, statuses["full_positive_assembly"])
    report("strict-action-source-higgs-artifacts-absent", strict_artifacts_absent, str(strict_presence))
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))
    report("block110-exact-boundary", theorem_passed, "finite source algebra does not descend to accepted EW/Higgs action/O_H")

    result = {
        "artifact": "yt_pr230_block110_cl3_z3_action_descent_obstruction",
        "actual_current_surface_status": (
            "exact negative boundary / Block110 Cl(3)/Z3 source-taste algebra "
            "does not derive accepted EW/Higgs action, canonical O_H, or scalar "
            "LSZ metric on the current PR230 surface"
        ),
        "conditional_surface_status": (
            "source-Higgs route can reopen with an accepted same-surface "
            "EW/Higgs action or canonical O_H certificate plus strict physical "
            "C_ss/C_sH/C_HH pole rows; this block only rejects deriving that "
            "action from the finite source/taste algebra alone"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block110 is a current-surface exact boundary.  It supplies no "
            "dynamic Phi, accepted action, canonical O_H certificate, source-"
            "Higgs pole rows, W/Z response rows, Schur/LSZ authority, or "
            "neutral H3/H4 authority."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "claim_type": "no_go",
        "block110_cl3_z3_action_descent_obstruction_passed": theorem_passed,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "algebra_facts": algebra_facts,
        "strict_authority_file_presence": strict_presence,
        "source_higgs_route_implication": {
            "degree_one_axis_is_real_support": True,
            "degree_filter_not_current_action": True,
            "finite_source_algebra_not_dynamic_phi": True,
            "internal_derivations_do_not_supply_kinetic_term": True,
            "accepted_action_or_pole_rows_still_required": True,
        },
        "exact_next_action": (
            "Do not retry finite-algebra action descent.  Either admit/derive a "
            "real same-surface EW/Higgs action extension with canonical O_H and "
            "then produce strict C_ss/C_sH/C_HH pole rows, or pivot to a strict "
            "W/Z response packet, strict Schur/scalar-LSZ authority, or neutral "
            "H3/H4 physical-transfer/source-coupling artifact."
        ),
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not set kappa_s, c2, Z_match, or g2 to one",
            "does not import H_unit, Ward identity, observed targets, alpha_LM, plaquette, or u0",
            "does not treat the degree-one taste-radial axis as canonical O_H on the current surface",
            "does not relabel finite C_sx/C_xx rows as physical C_sH/C_HH rows",
        ],
    }

    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

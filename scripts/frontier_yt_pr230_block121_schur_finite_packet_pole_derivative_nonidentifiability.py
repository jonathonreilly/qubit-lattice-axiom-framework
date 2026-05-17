#!/usr/bin/env python3
"""
PR #230 Block121 Schur finite-packet pole-derivative nonidentifiability.

Block113 confirms a complete finite A/B/C inverse-block support packet, while
Block111 confirms that no strict K-prime pole rows were emitted.  This runner
tests the remaining promotion shortcut: can exact finite A/B/C rows determine
the Schur/Feshbach pole derivative after the pole location is held fixed?

The answer is no.  A finite-node vanishing perturbation preserves every finite
row and the declared pole location but changes K'(pole).  Thus the complete
finite packet remains staging support unless a model-class/analytic-continuation
certificate or strict pole-row artifact is supplied.
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
    / "yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json"
)

PARENTS = {
    "block120_invariant_minimal_data": "outputs/yt_pr230_block120_source_reparam_invariant_minimal_data_2026-05-17.json",
    "block117_schur_scalar_lsz_strict_artifact_resolver": "outputs/yt_pr230_block117_schur_scalar_lsz_strict_artifact_resolver_2026-05-17.json",
    "block113_schur_abc_complete_packet_refresh": "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json",
    "finite_schur_abc_rows": "outputs/yt_pr230_two_source_taste_radial_schur_abc_finite_rows_2026-05-06.json",
    "block111_schur_kprime_gap_audit": "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json",
    "block70_schur_feshbach_kprime_theorem": "outputs/yt_pr230_block70_schur_feshbach_kprime_residue_theorem_2026-05-12.json",
    "strict_kprime_pole_residue_certificate": "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json",
    "schur_compressed_denominator_bootstrap_no_go": "outputs/yt_schur_compressed_denominator_row_bootstrap_no_go_2026-05-05.json",
    "fh_lsz_finite_shell_identifiability_no_go": "outputs/yt_fh_lsz_finite_shell_identifiability_no_go_2026-05-02.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
}

FORBIDDEN_FIREWALL = {
    "used_y_t_bare": False,
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_fitted_selector": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "renamed_c_sx_c_xx_as_c_sh_c_hh": False,
    "promoted_finite_abc_rows_to_pole_rows": False,
    "claimed_retained_or_proposed_retained": False,
}

FINITE_QHAT2_NODES = [
    0.0,
    0.267949192431,
    0.535898384862,
    0.803847577293,
    1.0,
]

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


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def finite_node_vanishing_witness() -> dict[str, Any]:
    """
    Construct two one-source Schur/Feshbach kernels with identical finite-node
    A/B/C rows and identical pole location, but different pole derivative.

    Let B=0, C=1, and A_0(x)=x-x_p.  For any finite row nodes x_i, define
    A_eps(x)=A_0(x)+eps*(x-x_p)*prod_i(x-x_i).  At every x_i, the perturbation
    vanishes, and it also vanishes at x_p.  But A_eps'(x_p) differs by
    eps*prod_i(x_p-x_i), so Res C_ss = 1/A'(x_p) changes.
    """

    pole = -0.25
    eps = 0.2

    def base_a(x: float) -> float:
        return x - pole

    def vanish_poly(x: float) -> float:
        out = x - pole
        for node in FINITE_QHAT2_NODES:
            out *= x - node
        return out

    def perturbed_a(x: float) -> float:
        return base_a(x) + eps * vanish_poly(x)

    derivative_shift = eps
    for node in FINITE_QHAT2_NODES:
        derivative_shift *= pole - node

    base_derivative = 1.0
    perturbed_derivative = base_derivative + derivative_shift
    rows = []
    for node in FINITE_QHAT2_NODES:
        rows.append(
            {
                "qhat2": node,
                "A_base": base_a(node),
                "A_perturbed": perturbed_a(node),
                "B_base": 0.0,
                "B_perturbed": 0.0,
                "C_base": 1.0,
                "C_perturbed": 1.0,
                "finite_rows_match": close(base_a(node), perturbed_a(node)),
            }
        )

    residue_base = 1.0 / base_derivative
    residue_perturbed = 1.0 / perturbed_derivative
    return {
        "pole_variable": "x=qhat^2 analytic continuation",
        "finite_nodes": FINITE_QHAT2_NODES,
        "pole_location": pole,
        "epsilon": eps,
        "rows": rows,
        "finite_rows_all_match": all(row["finite_rows_match"] for row in rows),
        "pole_location_preserved": close(base_a(pole), perturbed_a(pole)) and close(base_a(pole), 0.0),
        "base_kprime_at_pole": base_derivative,
        "perturbed_kprime_at_pole": perturbed_derivative,
        "kprime_changes": not close(base_derivative, perturbed_derivative),
        "base_residue": residue_base,
        "perturbed_residue": residue_perturbed,
        "residue_changes": not close(residue_base, residue_perturbed),
        "derivative_shift": derivative_shift,
    }


def main() -> int:
    print("PR #230 Block121 Schur finite-packet pole-derivative nonidentifiability")
    print("=" * 86)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    witness = finite_node_vanishing_witness()

    block120_open_boundary = (
        certs["block120_invariant_minimal_data"].get(
            "block120_source_reparam_invariant_minimal_data_passed"
        )
        is True
        and certs["block120_invariant_minimal_data"].get("proposal_allowed") is False
    )
    finite_packet_complete_support = (
        certs["block113_schur_abc_complete_packet_refresh"].get(
            "block113_schur_abc_complete_packet_refresh_passed"
        )
        is True
        and certs["block113_schur_abc_complete_packet_refresh"].get(
            "complete_finite_schur_abc_rows_confirmed"
        )
        is True
        and certs["block113_schur_abc_complete_packet_refresh"].get(
            "finite_rows_support_only"
        )
        is True
        and certs["finite_schur_abc_rows"].get("ready_chunks") == 63
        and certs["finite_schur_abc_rows"].get("expected_chunks") == 63
    )
    strict_schur_rows_absent = (
        certs["block117_schur_scalar_lsz_strict_artifact_resolver"].get(
            "block117_schur_scalar_lsz_strict_artifact_resolver_passed"
        )
        is True
        and certs["block117_schur_scalar_lsz_strict_artifact_resolver"].get(
            "scan_finds_no_strict_schur_scalar_lsz_artifact"
        )
        is True
        and certs["block117_schur_scalar_lsz_strict_artifact_resolver"].get(
            "proposal_allowed"
        )
        is False
        and
        certs["block113_schur_abc_complete_packet_refresh"].get(
            "strict_schur_abc_kernel_rows_present"
        )
        is False
        and certs["block113_schur_abc_complete_packet_refresh"].get(
            "strict_schur_kprime_rows_present"
        )
        is False
        and certs["block113_schur_abc_complete_packet_refresh"].get(
            "pole_location_or_derivative_rows_present"
        )
        is False
        and certs["block111_schur_kprime_gap_audit"].get(
            "block111_schur_kprime_packet_gap_audit_passed"
        )
        is True
        and certs["strict_kprime_pole_residue_certificate"].get("proposal_allowed") is False
    )
    theorem_support_not_closure = (
        "exact-support" in statuses["block70_schur_feshbach_kprime_theorem"]
        and certs["block70_schur_feshbach_kprime_theorem"].get("proposal_allowed") is False
    )
    finite_identifiability_shortcuts_blocked = (
        "row-bootstrap no-go" in statuses["schur_compressed_denominator_bootstrap_no_go"]
        and "finite-shell pole-fit identifiability no-go" in statuses["fh_lsz_finite_shell_identifiability_no_go"]
    )
    finite_nodes_do_not_fix_kprime = (
        witness["finite_rows_all_match"]
        and witness["pole_location_preserved"]
        and witness["kprime_changes"]
        and witness["residue_changes"]
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
    report("block120-boundary-preserved", block120_open_boundary, statuses["block120_invariant_minimal_data"])
    report("finite-schur-abc-packet-complete-support", finite_packet_complete_support, statuses["block113_schur_abc_complete_packet_refresh"])
    report("strict-schur-pole-rows-absent", strict_schur_rows_absent, statuses["block111_schur_kprime_gap_audit"])
    report("block70-theorem-support-not-closure", theorem_support_not_closure, statuses["block70_schur_feshbach_kprime_theorem"])
    report("finite-identifiability-shortcuts-blocked", finite_identifiability_shortcuts_blocked, "compressed-denominator and finite-shell shortcuts checked")
    report("finite-nodes-do-not-fix-kprime", finite_nodes_do_not_fix_kprime, str(witness))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/audit/stress deny proposal")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and block120_open_boundary
        and finite_packet_complete_support
        and strict_schur_rows_absent
        and theorem_support_not_closure
        and finite_identifiability_shortcuts_blocked
        and finite_nodes_do_not_fix_kprime
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block121 complete finite Schur A/B/C packet "
            "does not determine strict Schur/Feshbach K-prime pole derivative"
        ),
        "conditional_surface_status": (
            "Schur route can reopen only with strict same-surface pole rows, or with "
            "a model-class/analytic-continuation certificate that fixes the pole "
            "derivative from the finite packet plus FV/IR/contact authority and a "
            "canonical O_H/source bridge or physical-response bypass"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The complete finite A/B/C packet is real support, but finite nodes can be "
            "preserved while the Schur/Feshbach pole derivative and residue change. "
            "No strict K-prime rows, pole coordinate, FV/IR/contact authority, or "
            "canonical source-Higgs bridge are present."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block121_schur_finite_packet_pole_derivative_nonidentifiability_passed": passed,
        "finite_node_vanishing_witness": witness,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not turn finite A/B/C rows into strict pole rows",
            "does not relabel C_sx/C_xx as physical C_sH/C_HH rows",
            "does not identify the taste-radial source with canonical O_H",
            "does not use H_unit, yt_ward_identity, y_t_bare, observed targets, alpha_LM, plaquette, or u0",
            "does not set kappa_s, c2, or Z_match by convention",
        ],
        "exact_next_action": (
            "Do not spend more runtime extending finite A/B/C shells as if they could "
            "become K-prime authority. The Schur route needs a strict pole-row packet "
            "or a certified analytic/model-class theorem fixing K'(pole), plus FV/IR/"
            "contact authority and a canonical O_H/source bridge or W/Z physical-response bypass."
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

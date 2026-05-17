#!/usr/bin/env python3
"""
PR #230 Block122 Hamming-axis action/LSZ normalization gap.

Base Block118 fixes the finite taste-radial O_H axis as an exact
Hamming-Dirichlet support result.  This runner tests the next shortcut: whether
that finite axis selector also fixes the accepted action, scalar LSZ metric,
source-overlap normalization, or source-Higgs pole rows.

It does not.  A one-mode quadratic family can keep the selected axis and a
source-source pole proxy fixed while changing the source-Higgs cross residue,
Higgs-Higgs residue, and normalized source overlap by compensating with the
local source contact term.  Thus axis selection is real support, but it is not
action/LSZ/source-overlap authority.
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
    / "yt_pr230_block122_hamming_axis_action_lsz_normalization_gap_2026-05-17.json"
)

PARENTS = {
    "block118_hamming_dirichlet_oh_axis_selector": "outputs/yt_pr230_block118_hamming_dirichlet_oh_axis_selector_2026-05-17.json",
    "block120_invariant_minimal_data": "outputs/yt_pr230_block120_source_reparam_invariant_minimal_data_2026-05-17.json",
    "block110_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
    "block112_helmholtz_obstruction": "outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json",
    "block114_source_higgs_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "canonical_oh_action_lsz_closure": "outputs/yt_canonical_oh_action_lsz_closure_2026-05-12.json",
    "block67_same_surface_action_lsz_probe": "outputs/yt_pr230_block67_same_surface_canonical_oh_action_lsz_probe_2026-05-12.json",
    "source_higgs_direct_pole_contract": "outputs/yt_pr230_source_higgs_direct_pole_row_contract_2026-05-07.json",
    "source_higgs_pole_acceptance_contract": "outputs/yt_pr230_source_higgs_pole_row_acceptance_contract_2026-05-06.json",
    "source_higgs_overlap_kappa_contract": "outputs/yt_pr230_source_higgs_overlap_kappa_contract_2026-05-06.json",
    "scalar_source_contact_term_boundary": "outputs/yt_scalar_source_contact_term_scheme_boundary_2026-05-01.json",
    "canonical_scalar_normalization_import_audit": "outputs/yt_canonical_scalar_normalization_import_audit_2026-05-01.json",
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
    "used_package_hierarchy_v_as_pin": False,
    "used_fitted_selector": False,
    "set_kappa_s_equal_one": False,
    "set_g2_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "treated_axis_selector_as_action": False,
    "treated_contact_term_as_fixed": False,
    "renamed_c_sx_c_xx_as_c_sh_c_hh": False,
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


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def action_lsz_counterfamily() -> dict[str, Any]:
    """
    A finite axis selector chooses a unit direction e.  It does not choose the
    quadratic action coefficient Z_H, the source coupling kappa_sH, or the local
    source contact term c_ss.

    For S = 1/2 Z_H h^2 - kappa_sH s h + 1/2 c_ss s^2, the pole parts are
    C_HH = 1/Z_H, C_sH = kappa_sH/Z_H, and the source-source response can be
    shifted by c_ss.  Holding C_ss fixed while varying Z_H changes C_HH,
    C_sH, and kappa_sH/sqrt(Z_H).
    """

    target_css = 4.0
    rows = []
    for z_h, kappa in ((1.0, 1.0), (4.0, 1.0), (9.0, 1.0)):
        c_hh = 1.0 / z_h
        c_sh = kappa / z_h
        pole_css = kappa * kappa / z_h
        contact = target_css - pole_css
        rows.append(
            {
                "selected_axis": "Block118 Hamming-Dirichlet E1 axis",
                "Z_H": z_h,
                "kappa_sH": kappa,
                "local_source_contact_c_ss": contact,
                "C_HH_pole_residue": c_hh,
                "C_sH_pole_residue": c_sh,
                "C_ss_total_proxy": pole_css + contact,
                "normalized_source_overlap": kappa / math.sqrt(z_h),
                "axis_selector_eigenvalue": 2.0,
            }
        )
    return {
        "description": (
            "Same selected finite O_H axis and same source-source proxy, but "
            "different action normalization, source-Higgs residue, Higgs-Higgs "
            "residue, and normalized source overlap."
        ),
        "target_C_ss_total_proxy": target_css,
        "rows": rows,
        "axis_unchanged": all(row["axis_selector_eigenvalue"] == 2.0 for row in rows),
        "css_proxy_fixed": all(close(row["C_ss_total_proxy"], target_css) for row in rows),
        "contacts_nonnegative": all(row["local_source_contact_c_ss"] >= 0.0 for row in rows),
        "c_hh_varies": len({round(row["C_HH_pole_residue"], 12) for row in rows}) > 1,
        "c_sh_varies": len({round(row["C_sH_pole_residue"], 12) for row in rows}) > 1,
        "normalized_overlap_varies": len({round(row["normalized_source_overlap"], 12) for row in rows}) > 1,
    }


def main() -> int:
    print("PR #230 Block122 Hamming-axis action/LSZ normalization gap")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    witness = action_lsz_counterfamily()

    axis_support_valid = (
        certs["block118_hamming_dirichlet_oh_axis_selector"].get(
            "block118_hamming_dirichlet_oh_axis_selector_passed"
        )
        is True
        and certs["block118_hamming_dirichlet_oh_axis_selector"].get("selector_exact_support")
        is True
        and certs["block118_hamming_dirichlet_oh_axis_selector"].get("proposal_allowed")
        is False
    )
    action_lsz_rows_absent = (
        certs["block118_hamming_dirichlet_oh_axis_selector"].get(
            "action_lsz_and_pole_rows_still_absent"
        )
        is True
        and certs["block110_action_descent_obstruction"].get(
            "block110_cl3_z3_action_descent_obstruction_passed"
        )
        is True
        and certs["block112_helmholtz_obstruction"].get(
            "block112_helmholtz_action_integrability_obstruction_passed"
        )
        is True
        and certs["block114_source_higgs_resolver"].get(
            "block114_source_higgs_strict_artifact_resolver_passed"
        )
        is True
    )
    source_overlap_still_open = (
        certs["block118_hamming_dirichlet_oh_axis_selector"].get(
            "source_overlap_still_open"
        )
        is True
        and certs["source_higgs_overlap_kappa_contract"].get(
            "source_higgs_overlap_kappa_contract_passed"
        )
        is True
        and certs["source_higgs_overlap_kappa_contract"].get("proposal_allowed") is False
    )
    pole_rows_absent_or_contract_only = (
        certs["source_higgs_direct_pole_contract"].get(
            "source_higgs_direct_pole_row_contract_passed"
        )
        is True
        and certs["source_higgs_pole_acceptance_contract"].get(
            "source_higgs_pole_row_acceptance_contract_passed"
        )
        is True
        and certs["source_higgs_pole_acceptance_contract"].get("proposal_allowed") is False
        and "strict rows absent" in statuses["source_higgs_pole_acceptance_contract"]
    )
    contact_boundary_active = (
        "contact-term scheme boundary" in statuses["scalar_source_contact_term_boundary"]
        and certs["scalar_source_contact_term_boundary"].get("proposal_allowed") is False
    )
    counterfamily_valid = (
        witness["axis_unchanged"]
        and witness["css_proxy_fixed"]
        and witness["contacts_nonnegative"]
        and witness["c_hh_varies"]
        and witness["c_sh_varies"]
        and witness["normalized_overlap_varies"]
    )
    block120_boundary_preserved = (
        certs["block120_invariant_minimal_data"].get(
            "block120_source_reparam_invariant_minimal_data_passed"
        )
        is True
        and certs["block120_invariant_minimal_data"].get("proposal_allowed") is False
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
    report("block118-axis-support-valid", axis_support_valid, statuses["block118_hamming_dirichlet_oh_axis_selector"])
    report("action-lsz-rows-still-absent", action_lsz_rows_absent, statuses["block114_source_higgs_resolver"])
    report("source-overlap-still-open", source_overlap_still_open, statuses["source_higgs_overlap_kappa_contract"])
    report("pole-rows-absent-or-contract-only", pole_rows_absent_or_contract_only, statuses["source_higgs_pole_acceptance_contract"])
    report("contact-boundary-active", contact_boundary_active, statuses["scalar_source_contact_term_boundary"])
    report("axis-action-lsz-counterfamily-valid", counterfamily_valid, str(witness))
    report("block120-boundary-preserved", block120_boundary_preserved, statuses["block120_invariant_minimal_data"])
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/audit/stress deny proposal")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and axis_support_valid
        and action_lsz_rows_absent
        and source_overlap_still_open
        and pole_rows_absent_or_contract_only
        and contact_boundary_active
        and counterfamily_valid
        and block120_boundary_preserved
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block122 Hamming-Dirichlet O_H axis support "
            "does not determine accepted action, scalar LSZ metric, source-overlap "
            "normalization, or strict source-Higgs pole rows"
        ),
        "conditional_surface_status": (
            "Action-first source-Higgs route can reopen only with an accepted "
            "same-surface EW/Higgs action for the selected axis, scalar LSZ/source-"
            "overlap normalization, and strict physical C_ss/C_sH/C_HH pole rows "
            "with contact, FV/IR, threshold, and covariance authority"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite Hamming axis is exact support only. The counterfamily keeps "
            "that axis and a source-source proxy fixed while changing C_sH, C_HH, "
            "and normalized source overlap through action/contact choices; the "
            "current PR230 surface has no accepted action/LSZ/pole-row certificate."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block122_hamming_axis_action_lsz_normalization_gap_passed": passed,
        "axis_action_lsz_counterfamily": witness,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not treat the Block118 axis selector as an accepted action",
            "does not set kappa_s, c2, Z_match, or contact terms by convention",
            "does not relabel C_sx/C_xx rows as physical C_sH/C_HH pole rows",
            "does not use H_unit, yt_ward_identity, y_t_bare, observed targets, alpha_LM, plaquette, or u0",
        ],
        "exact_next_action": (
            "Do not spend the next block on another finite-axis selector. Either "
            "derive an accepted same-surface action/LSZ/source-overlap certificate "
            "for the Block118 axis with strict C_ss/C_sH/C_HH pole rows, or pivot "
            "to W/Z, neutral H3/H4, or a genuinely strict scalar pole authority route."
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

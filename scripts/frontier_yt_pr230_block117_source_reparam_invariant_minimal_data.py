#!/usr/bin/env python3
"""
PR #230 Block117 source-reparametrization invariant minimal-data boundary.

Block115 and Block116 resolve the W/Z and neutral H3/H4 strict artifact
families as absent on the current PR230 head.  This runner compresses the
remaining top-Yukawa closure problem to the source-reparametrization invariant
data that would be sufficient, checks current strict disjuncts, and keeps the
prior FH/LSZ invariant-readout support separate from closure.
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
    / "yt_pr230_block117_source_reparam_invariant_minimal_data_2026-05-17.json"
)

PARENTS = {
    "source_reparametrization_gauge_no_go": "outputs/yt_source_reparametrization_gauge_no_go_2026-05-01.json",
    "fh_lsz_invariant_readout": "outputs/yt_fh_lsz_invariant_readout_theorem_2026-05-01.json",
    "fh_gauge_normalized_response_route": "outputs/yt_fh_gauge_normalized_response_route_2026-05-02.json",
    "wz_response_only_g2_self_normalization_no_go": "outputs/yt_wz_g2_response_self_normalization_no_go_2026-05-05.json",
    "wz_mass_response_self_normalization_no_go": "outputs/yt_pr230_wz_mass_response_self_normalization_no_go_2026-05-12.json",
    "wz_v_authority_firewall": "outputs/yt_pr230_wz_v_authority_firewall_2026-05-15.json",
    "strict_kprime_pole_residue_certificate": "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json",
    "block110_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
    "block111_schur_kprime_gap_audit": "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json",
    "block112_helmholtz_obstruction": "outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json",
    "block113_schur_abc_refresh": "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json",
    "block114_source_higgs_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "block115_wz_resolver": "outputs/yt_pr230_block115_wz_strict_artifact_resolver_2026-05-17.json",
    "block116_neutral_h3h4_resolver": "outputs/yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

EXPECTED_POSITIVE_PACKET_PATHS = {
    "accepted_same_surface_ew_higgs_action": "outputs/yt_pr230_same_surface_ew_higgs_action_certificate_2026-05-06.json",
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "pr230_canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "pr230_source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "wz_production_response_rows": "outputs/yt_wz_mass_fit_response_rows_2026-05-04.json",
    "same_source_top_response_certificate": "outputs/yt_same_source_top_response_certificate_2026-05-04.json",
    "top_wz_matched_covariance_certificate": "outputs/yt_top_wz_matched_covariance_certificate_2026-05-04.json",
    "strict_electroweak_g2_certificate": "outputs/yt_electroweak_g2_certificate_2026-05-04.json",
    "delta_perp_correction_certificate": "outputs/yt_same_source_w_response_orthogonal_correction_certificate_2026-05-04.json",
    "same_source_w_response_rows": "outputs/yt_same_source_w_response_rows_2026-05-04.json",
    "neutral_h3h4_certificate": "outputs/yt_pr230_neutral_h3h4_certificate_2026-05-17.json",
    "physical_neutral_transfer_certificate": "outputs/yt_pr230_physical_neutral_transfer_certificate_2026-05-17.json",
    "source_triplet_coupling_certificate": "outputs/yt_pr230_same_surface_source_triplet_coupling_2026-05-15.json",
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
    "renamed_c_sx_c_xx_as_c_sh_c_hh": False,
    "promoted_smoke_or_finite_rows_to_closure": False,
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


def source_rescaling_witness() -> dict[str, Any]:
    base_slope = 3.0
    base_residue = 9.0
    base_gamma_prime = 1.0 / base_residue
    rows: list[dict[str, float]] = []
    for scale in (0.25, 0.5, 2.0, 5.0):
        slope = scale * base_slope
        residue = scale * scale * base_residue
        gamma_prime = base_gamma_prime / (scale * scale)
        rows.append(
            {
                "source_operator_scale": scale,
                "dE_top_ds": slope,
                "Res_C_ss": residue,
                "dGamma_ss_dp2": gamma_prime,
                "raw_kappa_equals_one_readout": slope,
                "lsz_residue_readout": slope / math.sqrt(residue),
                "lsz_inverse_readout": slope * math.sqrt(gamma_prime),
            }
        )
    invariant = all(
        close(row["lsz_residue_readout"], rows[0]["lsz_residue_readout"])
        and close(row["lsz_inverse_readout"], rows[0]["lsz_inverse_readout"])
        for row in rows
    )
    raw_varies = len({round(row["raw_kappa_equals_one_readout"], 12) for row in rows}) > 1
    return {
        "description": (
            "Raw dE_top/ds changes under source/operator rescaling, while the "
            "same-source FH/LSZ combination dE_top/ds / sqrt(Res_C_ss) is invariant "
            "if the physical scalar pole residue exists."
        ),
        "rows": rows,
        "raw_kappa_equals_one_readout_varies": raw_varies,
        "lsz_readout_invariant": invariant,
    }


def wz_scale_orbit_witness() -> dict[str, Any]:
    base = {
        "v": 2.0,
        "dv_ds": 0.3,
        "y_t": 1.2,
        "g2": 0.8,
        "gY": 0.6,
    }
    rows: list[dict[str, float]] = []
    for scale in (0.5, 1.0, 3.0, 8.0):
        v = scale * base["v"]
        dv_ds = scale * base["dv_ds"]
        y_t = base["y_t"] / scale
        g2 = base["g2"] / scale
        gY = base["gY"] / scale
        rows.append(
            {
                "absolute_scale": scale,
                "v": v,
                "dv_ds": dv_ds,
                "y_t": y_t,
                "g2": g2,
                "gY": gY,
                "m_t": y_t * v / math.sqrt(2.0),
                "M_W": g2 * v / 2.0,
                "M_Z": math.sqrt(g2 * g2 + gY * gY) * v / 2.0,
                "dm_t_ds": y_t * dv_ds / math.sqrt(2.0),
                "dM_W_ds": g2 * dv_ds / 2.0,
                "dM_Z_ds": math.sqrt(g2 * g2 + gY * gY) * dv_ds / 2.0,
            }
        )
    invariant_keys = ("m_t", "M_W", "M_Z", "dm_t_ds", "dM_W_ds", "dM_Z_ds")
    invariant = all(
        all(close(row[key], rows[0][key]) for key in invariant_keys) for row in rows
    )
    absolute_couplings_vary = (
        len({round(row["y_t"], 12) for row in rows}) > 1
        and len({round(row["g2"], 12) for row in rows}) > 1
    )
    return {
        "description": (
            "Top/W/Z masses and same-source mass responses can stay fixed under a "
            "common electroweak scale orbit while y_t, g2, and gY vary. An allowed "
            "absolute pin is still required."
        ),
        "rows": rows,
        "mass_and_response_dictionary_invariant": invariant,
        "absolute_couplings_vary": absolute_couplings_vary,
    }


def strict_packet_presence() -> dict[str, bool]:
    return {
        name: (ROOT / path).exists()
        for name, path in EXPECTED_POSITIVE_PACKET_PATHS.items()
    }


def packet_contracts(certs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    block114 = certs["block114_source_higgs_resolver"]
    block115 = certs["block115_wz_resolver"]
    block116 = certs["block116_neutral_h3h4_resolver"]
    block111 = certs["block111_schur_kprime_gap_audit"]
    block113 = certs["block113_schur_abc_refresh"]
    strict_kprime = certs["strict_kprime_pole_residue_certificate"]
    paths = strict_packet_presence()

    source_higgs_satisfied = (
        block114.get("proposal_allowed") is True
        and block114.get("canonical_oh_certificate_absent") is False
        and block114.get("strict_source_higgs_pole_rows_absent") is False
    )
    wz_satisfied = (
        block115.get("proposal_allowed") is True
        and block115.get("accepted_action_absent") is False
        and block115.get("production_wz_response_rows_absent") is False
        and block115.get("matched_top_wz_covariance_absent") is False
    )
    schur_satisfied = (
        strict_kprime.get("proposal_allowed") is True
        or (
            block111.get("proposal_allowed") is True
            and block113.get("proposal_allowed") is True
        )
    )
    neutral_satisfied = (
        block116.get("proposal_allowed") is True
        and block116.get("h3_physical_transfer_absent") is False
        and block116.get("h4_source_canonical_coupling_absent") is False
    )

    return {
        "source_higgs": {
            "satisfied": source_higgs_satisfied,
            "minimal_packet": [
                "accepted same-surface EW/Higgs action with dS/ds = sum O_H",
                "canonical O_H identity and normalization",
                "physical Euclidean C_ss/C_sH/C_HH(tau) pole rows",
                "Gram flatness, scalar LSZ/model-class, FV/IR, contact, and covariance authority",
            ],
            "current_boundary": status(block114),
        },
        "wz": {
            "satisfied": wz_satisfied,
            "minimal_packet": [
                "accepted same-source action",
                "production W/Z response rows and same-source top response rows",
                "matched top-W covariance",
                "strict non-observed g2 or another allowed absolute pin",
                "delta_perp authority and final W-response rows",
            ],
            "current_boundary": status(block115),
        },
        "schur": {
            "satisfied": schur_satisfied,
            "minimal_packet": [
                "strict pole coordinate",
                "K'(pole) derivative or exact Schur/Feshbach equivalent",
                "source projection numerator",
                "canonical O_H/source bridge",
                "model-class, FV/IR, and contact authority",
            ],
            "current_boundary": status(block113),
            "kprime_boundary": status(block111),
            "strict_kprime_boundary": status(strict_kprime),
        },
        "neutral_h3h4": {
            "satisfied": neutral_satisfied,
            "minimal_packet": [
                "same-surface physical neutral transfer or off-diagonal generator",
                "primitive-cone/irreducibility/rank-one authority",
                "H4 source/canonical-Higgs coupling",
                "physical transfer scale and scalar pole/FV/IR normalization",
            ],
            "current_boundary": status(block116),
        },
        "strict_packet_path_presence": paths,
        "any_contract_satisfied": any(
            (source_higgs_satisfied, wz_satisfied, schur_satisfied, neutral_satisfied)
        ),
    }


def main() -> int:
    print("PR #230 Block117 source-reparametrization invariant minimal-data boundary")
    print("=" * 86)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    contracts = packet_contracts(certs)
    source_witness = source_rescaling_witness()
    wz_witness = wz_scale_orbit_witness()

    source_reparam_boundary = (
        "source reparametrization gauge" in statuses["source_reparametrization_gauge_no_go"]
        and certs["source_reparametrization_gauge_no_go"].get("proposal_allowed") is False
    )
    fh_lsz_support_not_closure = (
        "Feynman-Hellmann" in statuses["fh_lsz_invariant_readout"]
        and certs["fh_lsz_invariant_readout"].get("proposal_allowed") is False
        and "required_data_before_closure" in certs["fh_lsz_invariant_readout"]
    )
    action_source_higgs_currently_absent = (
        certs["block110_action_descent_obstruction"].get(
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
        and contracts["source_higgs"]["satisfied"] is False
    )
    wz_currently_absent = (
        certs["block115_wz_resolver"].get("block115_wz_strict_artifact_resolver_passed")
        is True
        and contracts["wz"]["satisfied"] is False
        and "explicit-v authority absent" in statuses["wz_v_authority_firewall"]
        and "self-normalization" in statuses["wz_mass_response_self_normalization_no_go"]
    )
    schur_currently_absent = (
        certs["block111_schur_kprime_gap_audit"].get(
            "block111_schur_kprime_packet_gap_audit_passed"
        )
        is True
        and certs["block113_schur_abc_refresh"].get(
            "block113_schur_abc_complete_packet_refresh_passed"
        )
        is True
        and contracts["schur"]["satisfied"] is False
    )
    neutral_currently_absent = (
        certs["block116_neutral_h3h4_resolver"].get(
            "block116_neutral_h3h4_strict_artifact_resolver_passed"
        )
        is True
        and contracts["neutral_h3h4"]["satisfied"] is False
    )
    no_strict_packet_paths = not any(
        contracts["strict_packet_path_presence"].values()
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and "retained closure not achieved" in statuses["completion_audit"]
    )
    minimal_contract_unsatisfied = contracts["any_contract_satisfied"] is False
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("source-reparam-boundary-present", source_reparam_boundary, statuses["source_reparametrization_gauge_no_go"])
    report("fh-lsz-support-not-closure", fh_lsz_support_not_closure, statuses["fh_lsz_invariant_readout"])
    report("source-rescaling-witness-valid", source_witness["raw_kappa_equals_one_readout_varies"] and source_witness["lsz_readout_invariant"], str(source_witness))
    report("wz-scale-orbit-witness-valid", wz_witness["mass_and_response_dictionary_invariant"] and wz_witness["absolute_couplings_vary"], str(wz_witness))
    report("action-source-higgs-currently-absent", action_source_higgs_currently_absent, contracts["source_higgs"]["current_boundary"])
    report("wz-currently-absent", wz_currently_absent, contracts["wz"]["current_boundary"])
    report("schur-currently-absent", schur_currently_absent, contracts["schur"]["current_boundary"])
    report("neutral-currently-absent", neutral_currently_absent, contracts["neutral_h3h4"]["current_boundary"])
    report("expected-positive-packet-paths-absent", no_strict_packet_paths, str(contracts["strict_packet_path_presence"]))
    report("minimal-invariant-contract-unsatisfied", minimal_contract_unsatisfied, str(contracts))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/completion audit deny closure")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and source_reparam_boundary
        and fh_lsz_support_not_closure
        and source_witness["raw_kappa_equals_one_readout_varies"]
        and source_witness["lsz_readout_invariant"]
        and wz_witness["mass_and_response_dictionary_invariant"]
        and wz_witness["absolute_couplings_vary"]
        and action_source_higgs_currently_absent
        and wz_currently_absent
        and schur_currently_absent
        and neutral_currently_absent
        and no_strict_packet_paths
        and minimal_contract_unsatisfied
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block117 source-reparametrization invariant "
            "minimal-data contract is unsatisfied on the current PR230 head"
        ),
        "conditional_surface_status": (
            "proposal can reopen only after one strict same-surface disjunct is supplied: "
            "accepted canonical O_H/action plus physical C_ss/C_sH/C_HH pole rows; "
            "strict W/Z response packet with accepted action, matched covariance, "
            "delta_perp, and an allowed absolute pin; strict Schur/Feshbach pole "
            "rows; or strict neutral H3/H4 physical transfer plus source/canonical-Higgs coupling"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current surface has exact FH/LSZ invariant-readout support, but none "
            "of the required physical data packets exists. Raw source slopes and "
            "finite aliases remain source-reparametrization dependent or support-only."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block117_source_reparam_invariant_minimal_data_passed": passed,
        "source_rescaling_witness": source_witness,
        "wz_scale_orbit_witness": wz_witness,
        "packet_contracts": contracts,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not define y_t_bare",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
            "does not use package hierarchy v as a W/Z absolute pin",
            "does not set kappa_s, g2, c2, or Z_match by unit convention",
            "does not rename finite C_sx/C_xx rows as physical C_sH/C_HH pole rows",
            "does not promote chunk completion, smoke rows, or support rows to closure",
        ],
        "exact_next_action": (
            "Stop attempting source-only or finite-row promotion. The next positive "
            "work item must create one strict packet: action/canonical O_H plus "
            "physical source-Higgs pole rows; W/Z production response with matched "
            "covariance and an allowed absolute pin; Schur/Feshbach pole derivative "
            "rows; or neutral H3/H4 physical transfer with source/canonical-Higgs coupling."
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

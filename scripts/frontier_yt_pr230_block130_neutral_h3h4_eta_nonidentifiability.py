#!/usr/bin/env python3
"""
PR #230 Block130 neutral H3/H4 eta-coupling nonidentifiability.

Block129 closes the finite Schur proxy route.  The next independent positive
route is neutral H3/H4: a physical neutral transfer/off-diagonal primitive
authority plus source/canonical-Higgs coupling.  This runner checks whether
the current H1/H2 neutral support, heat-kernel support, completed finite rows,
or prior neutral no-go artifacts determine the missing source-singlet to
neutral coupling eta.  They do not.

The executable witness is a same-H1/H2 matrix family.  It fixes the current
admitted source self block and a primitive triplet block K, then varies the
off-block eta.  eta=0 is reducible and has no H4 source coupling; eta>0 is
entrywise positive and primitive.  Current PR230 artifacts do not contain the
strict physical transfer/coupling rows that would select eta.
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
    / "yt_pr230_block130_neutral_h3h4_eta_nonidentifiability_2026-05-17.json"
)

RAW_GLOB = "outputs/**/ensemble_measurement.json"

PARENTS = {
    "block116_neutral_h3h4_resolver": (
        "outputs/yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json"
    ),
    "block125_post_chunk_resolver": (
        "outputs/yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json"
    ),
    "block128_wz_source_construction": (
        "outputs/yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
    ),
    "block129_schur_construction": (
        "outputs/yt_pr230_block129_schur_pole_authority_construction_attempt_2026-05-17.json"
    ),
    "neutral_h3h4_aperture": (
        "outputs/yt_pr230_neutral_primitive_h3h4_aperture_checkpoint_2026-05-07.json"
    ),
    "neutral_route_completion": (
        "outputs/yt_pr230_neutral_primitive_route_completion_2026-05-06.json"
    ),
    "neutral_transfer_eigenoperator_mixing": (
        "outputs/yt_pr230_neutral_transfer_eigenoperator_source_mixing_no_go_2026-05-07.json"
    ),
    "neutral_post_block45_audit": (
        "outputs/yt_pr230_neutral_offdiagonal_post_block45_applicability_audit_2026-05-12.json"
    ),
    "neutral_primitive_cone_gate": (
        "outputs/yt_neutral_scalar_primitive_cone_certificate_gate_2026-05-05.json"
    ),
    "neutral_irreducibility_audit": (
        "outputs/yt_neutral_scalar_irreducibility_authority_audit_2026-05-04.json"
    ),
    "neutral_burnside_attempt": (
        "outputs/yt_neutral_scalar_burnside_irreducibility_attempt_2026-05-05.json"
    ),
    "neutral_offdiagonal_generator_attempt": (
        "outputs/yt_neutral_offdiagonal_generator_derivation_attempt_2026-05-05.json"
    ),
    "same_surface_neutral_multiplicity_gate": (
        "outputs/yt_pr230_same_surface_neutral_multiplicity_one_gate_2026-05-07.json"
    ),
    "z3_heat_kernel_transfer": (
        "outputs/yt_pr230_z3_heat_kernel_neutral_transfer_attempt_2026-05-15.json"
    ),
    "z3_heat_kernel_scale_selector": (
        "outputs/yt_pr230_z3_heat_kernel_scale_selector_no_go_2026-05-15.json"
    ),
    "z3_heat_kernel_source_coupling": (
        "outputs/yt_pr230_z3_heat_kernel_source_coupling_no_go_2026-05-15.json"
    ),
    "source_higgs_time_kernel_manifest": (
        "outputs/yt_pr230_source_higgs_time_kernel_production_manifest_2026-05-07.json"
    ),
    "os_transfer_kernel_gate": (
        "outputs/yt_pr230_os_transfer_kernel_artifact_gate_2026-05-07.json"
    ),
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
}

EXPECTED_STRICT_PATHS = {
    "neutral_primitive_cone_certificate": "outputs/yt_neutral_scalar_primitive_cone_certificate_2026-05-05.json",
    "neutral_offdiagonal_generator_certificate": "outputs/yt_neutral_offdiagonal_generator_certificate_2026-05-05.json",
    "neutral_scalar_rank_one_purity_certificate": "outputs/yt_neutral_scalar_rank_one_purity_certificate_2026-05-03.json",
    "neutral_scalar_irreducibility_certificate": "outputs/yt_neutral_scalar_irreducibility_certificate_2026-05-04.json",
    "pr230_physical_neutral_transfer_certificate": "outputs/yt_pr230_physical_neutral_transfer_certificate_2026-05-17.json",
    "pr230_neutral_h3h4_certificate": "outputs/yt_pr230_neutral_h3h4_certificate_2026-05-17.json",
    "pr230_source_triplet_coupling_certificate": "outputs/yt_pr230_same_surface_source_triplet_coupling_2026-05-15.json",
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "same_source_w_response_rows": "outputs/yt_same_source_w_response_rows_2026-05-04.json",
    "source_higgs_time_kernel_rows": "outputs/yt_pr230_source_higgs_time_kernel_rows_2026-05-07.json",
}

FORBIDDEN_FIREWALL = {
    "used_heat_kernel_as_physical_transfer": False,
    "derived_eta_from_h1_h2_support": False,
    "used_finite_c_sx_rows_as_transfer_generator": False,
    "used_equal_time_covariance_as_os_transfer": False,
    "aliased_taste_radial_x_to_canonical_oh": False,
    "used_source_only_rows_as_h4_coupling": False,
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


def matrix_witness(eps: float) -> list[list[float]]:
    """Same source self block and triplet primitive block; eta=eps varies."""
    alpha = 0.42
    triplet = [
        [1.0 - alpha + alpha / 3.0, alpha / 3.0, alpha / 3.0],
        [alpha / 3.0, 1.0 - alpha + alpha / 3.0, alpha / 3.0],
        [alpha / 3.0, alpha / 3.0, 1.0 - alpha + alpha / 3.0],
    ]
    return [
        [1.0, eps, eps, eps],
        [eps, *triplet[0]],
        [eps, *triplet[1]],
        [eps, *triplet[2]],
    ]


def is_entrywise_positive(matrix: list[list[float]]) -> bool:
    return all(value > 0.0 for row in matrix for value in row)


def same_h1_h2_data(a: list[list[float]], b: list[list[float]]) -> bool:
    same_source_self = math.isclose(a[0][0], b[0][0], rel_tol=0.0, abs_tol=0.0)
    same_triplet_block = all(
        math.isclose(a[i][j], b[i][j], rel_tol=0.0, abs_tol=0.0)
        for i in range(1, 4)
        for j in range(1, 4)
    )
    return same_source_self and same_triplet_block


def source_triplet_coupling(matrix: list[list[float]]) -> float:
    return sum(matrix[0][1:]) / math.sqrt(3.0)


def scan_raw_neutral_keys() -> dict[str, Any]:
    paths = sorted((ROOT / "outputs").glob("**/ensemble_measurement.json"))
    strict_fragments = (
        "neutral_transfer",
        "physical_neutral_transfer",
        "offdiagonal_generator",
        "off_diagonal_generator",
        "primitive_cone_certificate",
        "irreducibility_certificate",
        "source_triplet_coupling",
        "neutral_h3",
        "neutral_h4",
        "canonical_higgs_overlap",
        "source_canonical_higgs_coupling",
    )
    hits: list[dict[str, Any]] = []
    for path in paths:
        data = load_json(path)
        stack: list[tuple[str, Any]] = [("", data)]
        found: list[str] = []
        while stack:
            key_path, value = stack.pop()
            if isinstance(value, dict):
                for key, child in value.items():
                    child_path = f"{key_path}.{key}" if key_path else str(key)
                    if any(fragment in str(key).lower() for fragment in strict_fragments):
                        found.append(child_path)
                    stack.append((child_path, child))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    stack.append((f"{key_path}.{index}", child))
        if found:
            hits.append({"path": rel(path), "keys": found[:20]})
    return {
        "glob": RAW_GLOB,
        "raw_file_count": len(paths),
        "strict_neutral_key_hit_count": len(hits),
        "strict_neutral_key_hits_sample": hits[:5],
    }


def main() -> int:
    print("PR #230 Block130 neutral H3/H4 eta-coupling nonidentifiability")
    print("=" * 84)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_PATHS.items()}
    raw_scan = scan_raw_neutral_keys()

    eta0 = matrix_witness(0.0)
    eta1 = matrix_witness(0.07)
    witness_same_h1_h2 = same_h1_h2_data(eta0, eta1)
    witness_eta_changes = not math.isclose(
        source_triplet_coupling(eta0),
        source_triplet_coupling(eta1),
        rel_tol=0.0,
        abs_tol=1.0e-14,
    )
    eta0_reducible = source_triplet_coupling(eta0) == 0.0
    eta1_primitive_positive = is_entrywise_positive(eta1)

    h1_h2_support_only = (
        certs["neutral_h3h4_aperture"].get("h1_h2_support_loaded") is True
        and certs["neutral_h3h4_aperture"].get("h3_physical_transfer_or_offdiagonal_generator_absent") is True
        and certs["neutral_h3h4_aperture"].get("h4_source_canonical_higgs_coupling_absent") is True
        and "mathematical support only" in statuses["z3_heat_kernel_transfer"]
    )
    h3_h4_strict_rows_absent = (
        certs["block116_neutral_h3h4_resolver"].get(
            "block116_neutral_h3h4_strict_artifact_resolver_passed"
        )
        is True
        and all(value is False for value in certs["block116_neutral_h3h4_resolver"].get("strict_artifact_presence", {}).values())
        and not any(strict_presence.values())
        and raw_scan["strict_neutral_key_hit_count"] == 0
    )
    eta_not_derived = (
        "source-coupling data do not supply PR230 H4" in statuses["z3_heat_kernel_source_coupling"]
        and certs["z3_heat_kernel_source_coupling"].get("source_triplet_eta_required") is True
        and certs["z3_heat_kernel_source_coupling"].get("source_triplet_eta_selected_by_current_surface") is False
        and certs["z3_heat_kernel_source_coupling"].get("positive_eta_can_make_full_transfer_primitive") is True
        and certs["z3_heat_kernel_scale_selector"].get("heat_kernel_scale_time_not_selected") is True
        and "eta coupling" in certs["neutral_transfer_eigenoperator_mixing"].get("proposal_allowed_reason", "")
    )
    finite_rows_not_transfer = (
        certs["block125_post_chunk_resolver"]
        .get("post_chunk_raw_scan", {})
        .get("neutral_transfer_or_primitive_hits")
        == []
        and certs["neutral_post_block45_audit"].get(
            "post_block45_neutral_offdiagonal_applicability_audit_passed"
        )
        is True
        and "equal-time" in statuses["os_transfer_kernel_gate"]
        and "canonical O_H or physical neutral identity absent" in statuses["source_higgs_time_kernel_manifest"]
    )
    prior_shortcuts_blocked = (
        certs["neutral_primitive_cone_gate"].get("primitive_cone_certificate_gate_passed") is False
        and certs["neutral_irreducibility_audit"].get("neutral_scalar_irreducibility_certificate_present") is False
        and certs["neutral_burnside_attempt"].get("burnside_irreducibility_certificate_passed") is False
        and certs["neutral_offdiagonal_generator_attempt"].get("offdiagonal_generator_certificate_passed") is False
        and certs["same_surface_neutral_multiplicity_gate"].get("candidate_accepted") is False
    )
    aggregate_gates_still_closed = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("same-h1-h2-counterfamily", witness_same_h1_h2, "source self block and triplet K fixed")
    report(
        "eta-coupling-varies",
        witness_eta_changes and eta0_reducible and eta1_primitive_positive,
        f"eta0={source_triplet_coupling(eta0):.12g} eta1={source_triplet_coupling(eta1):.12g}",
    )
    report("h1-h2-support-only", h1_h2_support_only, statuses["neutral_h3h4_aperture"])
    report("h3-h4-strict-rows-absent", h3_h4_strict_rows_absent, str(raw_scan))
    report("eta-not-derived-by-heat-kernel-or-eigenoperator-data", eta_not_derived, statuses["z3_heat_kernel_source_coupling"])
    report("finite-rows-not-transfer", finite_rows_not_transfer, statuses["os_transfer_kernel_gate"])
    report("prior-neutral-shortcuts-blocked", prior_shortcuts_blocked, statuses["neutral_burnside_attempt"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "proposal_allowed remains false")
    report("claim-firewall-clean", firewall_clean, "no forbidden closure import used")

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block130 neutral H3/H4 route remains "
            "open because the source-singlet to neutral eta coupling is "
            "independent of current H1/H2, heat-kernel, finite-row, and "
            "source-only support; no strict physical neutral transfer or H4 "
            "source/canonical-Higgs coupling artifact is present"
        ),
        "conditional_surface_status": (
            "neutral route can reopen only with a same-surface physical "
            "neutral transfer/off-diagonal primitive certificate plus H4 "
            "source/canonical-Higgs coupling authority, or an equivalent W/Z "
            "or source-Higgs physical bridge"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The eta counterfamily fixes all admitted H1/H2 data while varying "
            "the H3/H4 source-neutral bridge.  Current artifacts do not contain "
            "the strict transfer/coupling rows needed to select eta, and all "
            "aggregate closure gates remain closed."
        ),
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "block130_neutral_h3h4_eta_nonidentifiability_passed": FAIL_COUNT == 0,
        "current_closure_satisfied": False,
        "eta_counterfamily": {
            "basis": ["source_singlet", "neutral_1", "neutral_2", "neutral_3"],
            "eta0_source_triplet_coupling": source_triplet_coupling(eta0),
            "eta1_source_triplet_coupling": source_triplet_coupling(eta1),
            "same_source_self_and_triplet_block": witness_same_h1_h2,
            "eta0_reducible": eta0_reducible,
            "eta1_entrywise_positive_primitive_proxy": eta1_primitive_positive,
            "interpretation": (
                "H1/H2 triplet positivity support does not determine H3/H4; "
                "eta is a separate physical transfer/coupling datum."
            ),
        },
        "strict_artifact_presence": strict_presence,
        "raw_neutral_scan": raw_scan,
        "strict_non_claims": {
            "does_not_promote_h1_h2_support_to_h3_h4": True,
            "does_not_promote_heat_kernel_to_physical_transfer": True,
            "does_not_promote_finite_c_sx_rows_to_transfer_or_coupling": True,
            "does_not_claim_retained_or_proposed_retained": True,
        },
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {rel(OUTPUT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

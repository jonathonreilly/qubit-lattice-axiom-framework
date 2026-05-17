#!/usr/bin/env python3
"""
PR #230 Block116 neutral H3/H4 strict artifact resolver.

Blocks 114 and 115 resolved the source-Higgs and W/Z strict artifact families
as absent on the current head.  This runner resolves the next independent
neutral-sector route: a same-surface H3 physical neutral transfer /
off-diagonal generator / primitive-cone or irreducibility certificate, plus H4
source-to-canonical-Higgs coupling authority.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json"

PARENTS = {
    "neutral_h3h4_aperture": "outputs/yt_pr230_neutral_primitive_h3h4_aperture_checkpoint_2026-05-07.json",
    "neutral_route_completion": "outputs/yt_pr230_neutral_primitive_route_completion_2026-05-06.json",
    "neutral_primitive_cone_gate": "outputs/yt_neutral_scalar_primitive_cone_certificate_gate_2026-05-05.json",
    "neutral_irreducibility_audit": "outputs/yt_neutral_scalar_irreducibility_authority_audit_2026-05-04.json",
    "neutral_burnside_attempt": "outputs/yt_neutral_scalar_burnside_irreducibility_attempt_2026-05-05.json",
    "neutral_offdiagonal_generator_attempt": "outputs/yt_neutral_offdiagonal_generator_derivation_attempt_2026-05-05.json",
    "neutral_rank_one_purity_gate": "outputs/yt_neutral_scalar_rank_one_purity_gate_2026-05-02.json",
    "neutral_commutant_rank_no_go": "outputs/yt_neutral_scalar_commutant_rank_no_go_2026-05-02.json",
    "neutral_dynamical_rank_one": "outputs/yt_neutral_scalar_dynamical_rank_one_closure_attempt_2026-05-02.json",
    "orthogonal_neutral_decoupling": "outputs/yt_orthogonal_neutral_decoupling_no_go_2026-05-02.json",
    "same_surface_neutral_multiplicity_gate": "outputs/yt_pr230_same_surface_neutral_multiplicity_one_gate_2026-05-07.json",
    "same_surface_neutral_multiplicity_candidate": "outputs/yt_pr230_same_surface_neutral_multiplicity_one_certificate_2026-05-07.json",
    "z3_conditional_primitive": "outputs/yt_pr230_z3_triplet_conditional_primitive_cone_theorem_2026-05-06.json",
    "z3_h2_positive_cone": "outputs/yt_pr230_z3_triplet_positive_cone_support_certificate_2026-05-06.json",
    "z3_heat_kernel_transfer_attempt": "outputs/yt_pr230_z3_heat_kernel_neutral_transfer_attempt_2026-05-15.json",
    "z3_heat_kernel_scale_selector_no_go": "outputs/yt_pr230_z3_heat_kernel_scale_selector_no_go_2026-05-15.json",
    "z3_heat_kernel_source_coupling_no_go": "outputs/yt_pr230_z3_heat_kernel_source_coupling_no_go_2026-05-15.json",
    "two_source_primitive_transfer_candidate": "outputs/yt_pr230_two_source_taste_radial_primitive_transfer_candidate_gate_2026-05-07.json",
    "block114_source_higgs_strict_artifact_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "block115_wz_strict_artifact_resolver": "outputs/yt_pr230_block115_wz_strict_artifact_resolver_2026-05-17.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
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
}

FORBIDDEN_FIREWALL = {
    "used_positivity_without_irreducibility": False,
    "used_commutant_rank_as_rank_one_purity": False,
    "used_source_only_or_c_sx_rows_as_neutral_transfer": False,
    "used_heat_kernel_as_physical_transfer_without_action_selector": False,
    "used_heat_kernel_eta_as_derived_source_coupling": False,
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


def walk(obj: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
    rows: list[tuple[tuple[str, ...], Any]] = [(path, obj)]
    if isinstance(obj, dict):
        for key, value in obj.items():
            rows.extend(walk(value, path + (str(key),)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            rows.extend(walk(value, path + (str(index),)))
    return rows


def strict_neutral_certificate(node: Any) -> bool:
    if not isinstance(node, dict):
        return False
    kind = str(node.get("certificate_kind", ""))
    has_transfer = node.get("same_surface_cl3_z3") is True and (
        "neutral_transfer_matrix" in node or "offdiagonal_generator" in node
    )
    has_coupling = (
        node.get("source_pole_overlap", 0) not in (0, None)
        or node.get("canonical_higgs_overlap", 0) not in (0, None)
        or node.get("source_canonical_higgs_coupling_certified") is True
    )
    has_strict_kind = kind in {
        "neutral_scalar_primitive_cone_certificate",
        "neutral_offdiagonal_generator_certificate",
        "neutral_scalar_irreducibility_certificate",
        "neutral_h3h4_certificate",
    }
    return bool(has_strict_kind and has_transfer and has_coupling)


def scan_neutral_candidates() -> dict[str, Any]:
    files: list[Path] = []
    for path in (ROOT / "outputs").glob("*.json"):
        name = path.name.lower()
        if any(
            token in name
            for token in (
                "neutral",
                "primitive",
                "irreduc",
                "rank_one",
                "offdiagonal",
                "heat_kernel",
                "z3",
                "h3",
                "h4",
            )
        ):
            files.append(path)

    reference_files: list[str] = []
    strict_hits: list[dict[str, Any]] = []
    support_only_hits: list[str] = []

    for path in sorted(files):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        text = json.dumps(data, sort_keys=True)
        if any(token in text for token in ("H3", "H4", "primitive", "irreducibility", "neutral_transfer", "offdiagonal")):
            reference_files.append(rel(path))
        if any(token in status(data) for token in ("support", "negative boundary", "absent", "not complete", "not physical")):
            support_only_hits.append(rel(path))
        for node_path, value in walk(data):
            if strict_neutral_certificate(value):
                strict_hits.append(
                    {
                        "path": rel(path),
                        "node_path": "/".join(node_path),
                        "row_keys": sorted(value) if isinstance(value, dict) else [],
                    }
                )

    return {
        "candidate_file_count": len(files),
        "reference_file_count": len(reference_files),
        "reference_files_sample": reference_files[:50],
        "support_only_files_sample": support_only_hits[:35],
        "strict_neutral_certificate_hits": strict_hits,
    }


def main() -> int:
    print("PR #230 Block116 neutral H3/H4 strict artifact resolver")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_PATHS.items()
    }
    scan = scan_neutral_candidates()

    h1_h2_support_only = (
        "H1/H2 support" in statuses["neutral_h3h4_aperture"]
        and certs["neutral_h3h4_aperture"].get("h1_h2_support_loaded") is True
        and certs["z3_conditional_primitive"].get("h2_positive_cone_support_supplied") is True
        and certs["z3_conditional_primitive"].get("remaining_unsupplied_conditional_premises") == ["H3", "H4"]
        and certs["z3_h2_positive_cone"].get("z3_triplet_positive_cone_h2_support_passed") is True
        and certs["z3_h2_positive_cone"].get("proposal_allowed") is False
    )
    h3_physical_transfer_absent = (
        certs["neutral_route_completion"].get("h3_physical_transfer_or_offdiagonal_generator_absent") is True
        and certs["neutral_h3h4_aperture"].get("h3_physical_transfer_or_offdiagonal_generator_absent") is True
        and certs["neutral_primitive_cone_gate"].get("primitive_cone_certificate_gate_passed") is False
        and certs["neutral_irreducibility_audit"].get("neutral_scalar_irreducibility_certificate_present") is False
        and certs["neutral_offdiagonal_generator_attempt"].get("offdiagonal_generator_written") is False
        and certs["same_surface_neutral_multiplicity_gate"].get("candidate_accepted") is False
        and not strict_presence["neutral_primitive_cone_certificate"]
        and not strict_presence["neutral_offdiagonal_generator_certificate"]
        and not strict_presence["neutral_scalar_rank_one_purity_certificate"]
        and not strict_presence["neutral_scalar_irreducibility_certificate"]
        and not strict_presence["pr230_physical_neutral_transfer_certificate"]
        and not strict_presence["pr230_neutral_h3h4_certificate"]
    )
    h4_source_canonical_coupling_absent = (
        certs["neutral_route_completion"].get("h4_source_canonical_higgs_coupling_absent") is True
        and certs["neutral_h3h4_aperture"].get("h4_source_canonical_higgs_coupling_absent") is True
        and "source-coupling data do not supply PR230 H4" in statuses["z3_heat_kernel_source_coupling_no_go"]
        and certs["block114_source_higgs_strict_artifact_resolver"].get("canonical_oh_certificate_absent") is True
        and certs["block114_source_higgs_strict_artifact_resolver"].get("strict_source_higgs_pole_rows_absent") is True
        and certs["block115_wz_strict_artifact_resolver"].get("production_wz_response_rows_absent") is True
        and not strict_presence["pr230_source_triplet_coupling_certificate"]
        and not strict_presence["canonical_higgs_operator_certificate"]
        and not strict_presence["source_higgs_pole_rows"]
        and not strict_presence["same_source_w_response_rows"]
    )
    shortcuts_blocked = (
        "commutant does not force rank-one purity" in statuses["neutral_commutant_rank_no_go"]
        and "dynamical rank-one neutral scalar theorem not derived" in statuses["neutral_dynamical_rank_one"]
        and "orthogonal neutral decoupling shortcut not derived" in statuses["orthogonal_neutral_decoupling"]
        and "Burnside neutral irreducibility attempt blocked" in statuses["neutral_burnside_attempt"]
        and "Z3 heat-kernel primitive transfer is mathematical support only" in statuses["z3_heat_kernel_transfer_attempt"]
        and "scale and time selectors do not derive" in statuses["z3_heat_kernel_scale_selector_no_go"]
        and "finite C_sx rows do not certify a physical primitive neutral transfer" in statuses["two_source_primitive_transfer_candidate"]
    )
    scan_no_strict_current_artifact = len(scan["strict_neutral_certificate_hits"]) == 0
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and "retained closure not achieved" in statuses["completion_audit"]
    )
    prior_boundaries_preserved = (
        certs["block114_source_higgs_strict_artifact_resolver"].get(
            "block114_source_higgs_strict_artifact_resolver_passed"
        )
        is True
        and certs["block115_wz_strict_artifact_resolver"].get(
            "block115_wz_strict_artifact_resolver_passed"
        )
        is True
        and certs["block114_source_higgs_strict_artifact_resolver"].get("proposal_allowed") is False
        and certs["block115_wz_strict_artifact_resolver"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("expected-strict-neutral-artifact-paths-absent", not any(strict_presence.values()), str(strict_presence))
    report("h1-h2-support-only", h1_h2_support_only, statuses["neutral_h3h4_aperture"])
    report("h3-physical-transfer-absent", h3_physical_transfer_absent, statuses["neutral_route_completion"])
    report("h4-source-canonical-coupling-absent", h4_source_canonical_coupling_absent, statuses["z3_heat_kernel_source_coupling_no_go"])
    report("neutral-shortcuts-blocked", shortcuts_blocked, "commutant/dynamical/decoupling/Burnside/heat-kernel/finite-row shortcuts checked")
    report("scan-finds-no-strict-neutral-artifact", scan_no_strict_current_artifact, str(scan))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/completion audit deny closure")
    report("prior-block114-115-boundaries-preserved", prior_boundaries_preserved, "source-Higgs and W/Z strict artifact resolvers still block")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and not any(strict_presence.values())
        and h1_h2_support_only
        and h3_physical_transfer_absent
        and h4_source_canonical_coupling_absent
        and shortcuts_blocked
        and scan_no_strict_current_artifact
        and aggregate_gates_open
        and prior_boundaries_preserved
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block116 current PR230 head contains no strict "
            "neutral H3/H4 artifact: physical neutral transfer or off-diagonal primitive "
            "authority plus source/canonical-Higgs coupling remain absent"
        ),
        "conditional_surface_status": (
            "neutral-route support only after a future same-surface artifact supplies H3 "
            "physical neutral transfer, off-diagonal generator, primitive-cone or "
            "irreducibility authority, and H4 source/canonical-Higgs coupling authority"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block116 is a strict artifact resolver and exact boundary. It finds H1/H2 "
            "support and finite-row staging only; H3 physical transfer/primitive authority "
            "and H4 source/canonical-Higgs coupling are absent."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block116_neutral_h3h4_strict_artifact_resolver_passed": passed,
        "h1_h2_support_only": h1_h2_support_only,
        "h3_physical_transfer_absent": h3_physical_transfer_absent,
        "h4_source_canonical_coupling_absent": h4_source_canonical_coupling_absent,
        "neutral_shortcuts_blocked": shortcuts_blocked,
        "scan_finds_no_strict_neutral_artifact": scan_no_strict_current_artifact,
        "strict_artifact_presence": strict_presence,
        "candidate_scan_summary": scan,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not treat H1/H2 support as physical H3/H4 authority",
            "does not treat positivity, commutant rank, heat-kernel math support, or finite C_sx/C_xx rows as physical transfer",
            "does not treat heat-kernel scale or source-coupling eta as derived from the PR230 action",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
            "does not set kappa_s, c2, or Z_match by fiat",
        ],
        "exact_next_action": (
            "Create a strict neutral H3/H4 artifact: same-surface physical neutral "
            "transfer/off-diagonal generator or primitive-cone/irreducibility certificate "
            "plus source/canonical-Higgs coupling. Otherwise pivot to strict Schur/scalar-LSZ "
            "pole authority or a fresh source-Higgs/WZ strict packet."
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

#!/usr/bin/env python3
"""
PR #230 Block117 strict Schur/scalar-LSZ artifact resolver.

Blocks 114-116 resolved the source-Higgs, W/Z, and neutral H3/H4 strict
artifact families as absent on the current head. This runner resolves the next
independent residual: strict Schur/Feshbach K-prime pole rows or strict
scalar-LSZ moment/threshold/FV authority. Finite C_ss/C_sx/C_xx rows and
finite A/B/C inverse blocks remain support only unless a strict pole authority
artifact supplies the missing rows and limiting certificates.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block117_schur_scalar_lsz_strict_artifact_resolver_2026-05-17.json"
)

PARENTS = {
    "block111_schur_kprime_packet_gap_audit": "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json",
    "block113_schur_abc_complete_packet_refresh": "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json",
    "block70_schur_feshbach_kprime_residue_theorem": "outputs/yt_pr230_block70_schur_feshbach_kprime_residue_theorem_2026-05-12.json",
    "strict_kprime_pole_residue_builder": "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json",
    "strict_scalar_lsz_moment_fv_gate": "outputs/yt_pr230_strict_scalar_lsz_moment_fv_authority_gate_2026-05-07.json",
    "higher_shell_complete_packet_monotonicity_gate": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "finite_moment_atom_residue_obstruction": "outputs/yt_pr230_block64_finite_moment_atom_residue_obstruction_2026-05-12.json",
    "schur_route_completion": "outputs/yt_pr230_schur_route_completion_2026-05-06.json",
    "schur_kernel_row_contract_gate": "outputs/yt_schur_kernel_row_contract_gate_2026-05-03.json",
    "schur_kprime_row_absence_guard": "outputs/yt_schur_kprime_row_absence_guard_2026-05-03.json",
    "schur_complement_kprime_sufficiency": "outputs/yt_schur_complement_kprime_sufficiency_2026-05-03.json",
    "block114_source_higgs_strict_artifact_resolver": "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json",
    "block115_wz_strict_artifact_resolver": "outputs/yt_pr230_block115_wz_strict_artifact_resolver_2026-05-17.json",
    "block116_neutral_h3h4_strict_artifact_resolver": "outputs/yt_pr230_block116_neutral_h3h4_strict_artifact_resolver_2026-05-17.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

EXPECTED_STRICT_PATHS = {
    "block69_strict_kprime_rows": "outputs/yt_pr230_block69_strict_kprime_pole_residue_rows_2026-05-12.json",
    "strict_kprime_rows": "outputs/yt_pr230_strict_kprime_pole_residue_rows_2026-05-12.json",
    "schur_kprime_rows": "outputs/yt_schur_kprime_pole_residue_rows_2026-05-12.json",
    "pr230_schur_scalar_kernel_rows": "outputs/yt_pr230_schur_scalar_kernel_rows_2026-05-12.json",
    "schur_scalar_kernel_rows": "outputs/yt_schur_scalar_kernel_rows_2026-05-03.json",
    "strict_schur_feshbach_kprime_rows": "outputs/yt_pr230_strict_schur_feshbach_kprime_rows_2026-05-17.json",
    "strict_schur_feshbach_pole_rows": "outputs/yt_pr230_strict_schur_feshbach_pole_rows_2026-05-17.json",
    "strict_scalar_lsz_moment_threshold_fv_certificate": "outputs/yt_pr230_strict_scalar_lsz_moment_threshold_fv_certificate_2026-05-17.json",
    "strict_scalar_lsz_pole_authority": "outputs/yt_pr230_strict_scalar_lsz_pole_authority_2026-05-17.json",
    "strict_fvir_threshold_certificate": "outputs/yt_pr230_strict_fvir_threshold_certificate_2026-05-17.json",
}

FORBIDDEN_FIREWALL = {
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_cold_pilots_as_production_evidence": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "treated_finite_rows_as_strict_pole_rows": False,
    "treated_taste_radial_x_as_canonical_oh": False,
    "treated_model_fit_as_threshold_or_fvir_authority": False,
    "treated_kprime_support_theorem_as_row_evidence": False,
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


def truthy_interval(row: Any) -> bool:
    if row in (None, False, {}, [], 0):
        return False
    if isinstance(row, dict):
        if row.get("valid") is True or row.get("passed") is True:
            return True
        if row.get("computed") is True:
            return True
        if "interval" in row and row.get("interval") not in (None, [], {}):
            return True
        if "value" in row and row.get("value") is not None:
            return True
        if "lo" in row and "hi" in row:
            return True
        return any(truthy_interval(value) for value in row.values())
    return True


def firewall_false(node: dict[str, Any]) -> bool:
    firewall = node.get("forbidden_firewall") or node.get("forbidden_import_firewall") or {}
    if not isinstance(firewall, dict) or not firewall:
        return False
    raw_values = []
    if "normalized" in firewall and isinstance(firewall["normalized"], dict):
        raw_values.extend(firewall["normalized"].values())
    else:
        raw_values.extend(firewall.values())
    return raw_values != [] and all(value is False for value in raw_values)


def strict_schur_certificate(node: Any) -> bool:
    if not isinstance(node, dict):
        return False
    kind = str(node.get("certificate_kind", ""))
    strict_kind = kind in {
        "strict_schur_feshbach_kprime_rows",
        "strict_schur_feshbach_pole_rows",
        "strict_kprime_pole_residue_rows",
        "schur_scalar_kernel_rows",
    }
    strict_status = (
        node.get("strict_pass") is True
        or node.get("strict_schur_or_scalar_lsz_authority_passed") is True
        or node.get("strict_schur_kprime_rows_present") is True
    )
    same_surface = node.get("same_surface_cl3_z3") is True or node.get("same_surface") is True
    has_pole = truthy_interval(node.get("pole_coordinate"))
    has_source_projection = truthy_interval(
        node.get("source_projection_numerator")
        or node.get("source_row_projection_numerator")
    )
    derivative = (
        node.get("derivative_row_l_Kprime_r_or_exact_equivalent")
        or node.get("schur_feshbach_or_transfer_kernel_rows")
        or node.get("left_Kprime_right_at_pole")
        or node.get("K_prime_at_pole")
    )
    fv = node.get("FV_IR_contact_term_checks") or node.get("fv_ir_contact_checks") or {}
    fv_passed = isinstance(fv, dict) and (
        fv.get("passed") is True
        or all(
            fv.get(key) is True
            for key in (
                "finite_volume_passed",
                "ir_zero_mode_order_passed",
                "contact_terms_subtracted_or_bounded",
                "model_class_or_analytic_continuation_passed",
            )
        )
    )
    return bool(
        (strict_kind or strict_status)
        and same_surface
        and has_pole
        and has_source_projection
        and truthy_interval(derivative)
        and fv_passed
        and firewall_false(node)
    )


def strict_scalar_lsz_certificate(node: Any) -> bool:
    if not isinstance(node, dict):
        return False
    kind = str(node.get("certificate_kind", ""))
    strict_kind = kind in {
        "strict_scalar_lsz_moment_threshold_fv_certificate",
        "strict_scalar_lsz_pole_authority",
        "strict_scalar_lsz_moment_fv_authority",
        "strict_fvir_threshold_certificate",
    }
    same_surface = node.get("same_surface_cl3_z3") is True or node.get("same_surface") is True
    strict_status = (
        node.get("strict_scalar_lsz_moment_fv_authority_present") is True
        or node.get("strict_scalar_lsz_authority_present") is True
        or node.get("strict_scalar_lsz_authority_passed") is True
    )
    threshold = (
        node.get("threshold_gap_authority_present") is True
        or node.get("threshold_authority_present") is True
    )
    fvir = (
        node.get("multivolume_fv_ir_authority_present") is True
        or node.get("fv_ir_threshold_authority_present") is True
    )
    pole_model = (
        node.get("isolated_pole_model_class_authority_present") is True
        or node.get("pole_residue_authority_present") is True
    )
    contact = (
        node.get("contact_terms_subtracted_or_bounded") is True
        or node.get("contact_subtraction_authority_present") is True
    )
    return bool(
        (strict_kind or strict_status)
        and same_surface
        and threshold
        and fvir
        and pole_model
        and contact
        and firewall_false(node)
    )


def scan_schur_scalar_candidates() -> dict[str, Any]:
    files: list[Path] = []
    for path in (ROOT / "outputs").glob("*.json"):
        name = path.name.lower()
        if any(
            token in name
            for token in (
                "schur",
                "lsz",
                "kprime",
                "k_prime",
                "fvir",
                "fv_ir",
                "threshold",
                "moment",
                "pole",
                "stieltjes",
            )
        ):
            files.append(path)

    reference_files: list[str] = []
    support_only_files: list[str] = []
    strict_hits: list[dict[str, Any]] = []

    for path in sorted(files):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        text = json.dumps(data, sort_keys=True)
        if any(
            token in text
            for token in (
                "K-prime",
                "Kprime",
                "strict scalar",
                "FV/IR",
                "threshold",
                "Stieltjes",
                "pole",
            )
        ):
            reference_files.append(rel(path))
        if any(
            token in status(data)
            for token in (
                "support",
                "negative boundary",
                "open",
                "absent",
                "not complete",
                "not derivable",
            )
        ):
            support_only_files.append(rel(path))
        for node_path, value in walk(data):
            if strict_schur_certificate(value) or strict_scalar_lsz_certificate(value):
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
        "reference_files_sample": reference_files[:60],
        "support_only_files_sample": support_only_files[:45],
        "strict_schur_scalar_lsz_certificate_hits": strict_hits,
    }


def main() -> int:
    print("PR #230 Block117 strict Schur/scalar-LSZ artifact resolver")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_PATHS.items()
    }
    scan = scan_schur_scalar_candidates()

    finite_schur_support_only = (
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
        and certs["block113_schur_abc_complete_packet_refresh"].get(
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
    )
    strict_kprime_rows_absent = (
        "strict K-prime pole-residue certificate rows missing"
        in statuses["strict_kprime_pole_residue_builder"]
        and certs["strict_kprime_pole_residue_builder"].get("candidate_present") is False
        and certs["strict_kprime_pole_residue_builder"].get("strict_pass") is False
        and "strict row artifact absent"
        in certs["strict_kprime_pole_residue_builder"].get("missing_required_rows", [])
        and certs["block111_schur_kprime_packet_gap_audit"].get(
            "block111_schur_kprime_packet_gap_audit_passed"
        )
        is True
        and certs["block111_schur_kprime_packet_gap_audit"].get(
            "strict_kprime_row_emissions_present"
        )
        is False
        and certs["block111_schur_kprime_packet_gap_audit"].get(
            "strict_nonempty_field_hits"
        )
        == []
        and not any(
            strict_presence[name]
            for name in (
                "block69_strict_kprime_rows",
                "strict_kprime_rows",
                "schur_kprime_rows",
                "pr230_schur_scalar_kernel_rows",
                "schur_scalar_kernel_rows",
                "strict_schur_feshbach_kprime_rows",
                "strict_schur_feshbach_pole_rows",
            )
        )
    )
    scalar_lsz_authority_absent = (
        certs["strict_scalar_lsz_moment_fv_gate"].get(
            "strict_scalar_lsz_moment_fv_authority_gate_passed"
        )
        is True
        and certs["strict_scalar_lsz_moment_fv_gate"].get(
            "strict_scalar_lsz_moment_fv_authority_present"
        )
        is False
        and certs["strict_scalar_lsz_moment_fv_gate"].get(
            "current_raw_c_ss_proxy_fails_stieltjes_monotonicity"
        )
        is True
        and certs["strict_scalar_lsz_moment_fv_gate"].get(
            "threshold_gap_authority_present"
        )
        is False
        and certs["strict_scalar_lsz_moment_fv_gate"].get(
            "multivolume_fv_ir_authority_present"
        )
        is False
        and certs["strict_scalar_lsz_moment_fv_gate"].get(
            "isolated_pole_model_class_authority_present"
        )
        is False
        and not any(
            strict_presence[name]
            for name in (
                "strict_scalar_lsz_moment_threshold_fv_certificate",
                "strict_scalar_lsz_pole_authority",
                "strict_fvir_threshold_certificate",
            )
        )
    )
    finite_promotion_blocked = (
        certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "higher_shell_complete_packet_monotonicity_gate_passed"
        )
        is True
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "strict_schur_or_scalar_lsz_authority_passed"
        )
        is False
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "finite_rows_written"
        )
        is True
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "strict_pole_rows_written"
        )
        is False
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "pole_location_or_derivative_rows_present"
        )
        is False
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "fv_ir_threshold_authority_present"
        )
        is False
        and certs["higher_shell_complete_packet_monotonicity_gate"].get(
            "source_operator_is_taste_radial_not_canonical_oh"
        )
        is True
    )
    moment_threshold_fv_authority_absent = (
        certs["finite_moment_atom_residue_obstruction"].get(
            "block64_finite_moment_atom_residue_obstruction_passed"
        )
        is True
        and certs["finite_moment_atom_residue_obstruction"].get(
            "current_finite_prefix_residue_authority_present"
        )
        is False
        and certs["finite_moment_atom_residue_obstruction"].get(
            "direct_pole_row_residue_measurement_present"
        )
        is False
        and certs["finite_moment_atom_residue_obstruction"].get(
            "strict_extremal_moment_certificate_present"
        )
        is False
        and certs["finite_moment_atom_residue_obstruction"].get(
            "threshold_fvir_contact_authority_present"
        )
        is False
        and certs["finite_moment_atom_residue_obstruction"].get(
            "kprime_authority_present"
        )
        is False
        and certs["finite_moment_atom_residue_obstruction"].get(
            "pole_residue_authority_present"
        )
        is False
    )
    bridge_roots_absent = (
        certs["block114_source_higgs_strict_artifact_resolver"].get(
            "block114_source_higgs_strict_artifact_resolver_passed"
        )
        is True
        and certs["block114_source_higgs_strict_artifact_resolver"].get(
            "canonical_oh_certificate_absent"
        )
        is True
        and certs["block115_wz_strict_artifact_resolver"].get(
            "block115_wz_strict_artifact_resolver_passed"
        )
        is True
        and certs["block115_wz_strict_artifact_resolver"].get(
            "production_wz_response_rows_absent"
        )
        is True
        and certs["block116_neutral_h3h4_strict_artifact_resolver"].get(
            "block116_neutral_h3h4_strict_artifact_resolver_passed"
        )
        is True
        and certs["block116_neutral_h3h4_strict_artifact_resolver"].get(
            "h4_source_canonical_coupling_absent"
        )
        is True
    )
    scan_no_strict_current_artifact = (
        len(scan["strict_schur_scalar_lsz_certificate_hits"]) == 0
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and "retained closure not achieved" in statuses["completion_audit"]
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report(
        "expected-strict-schur-scalar-artifact-paths-absent",
        not any(strict_presence.values()),
        str(strict_presence),
    )
    report(
        "finite-schur-abc-support-only",
        finite_schur_support_only,
        statuses["block113_schur_abc_complete_packet_refresh"],
    )
    report(
        "strict-kprime-pole-rows-absent",
        strict_kprime_rows_absent,
        statuses["strict_kprime_pole_residue_builder"],
    )
    report(
        "scalar-lsz-moment-threshold-fv-authority-absent",
        scalar_lsz_authority_absent,
        statuses["strict_scalar_lsz_moment_fv_gate"],
    )
    report(
        "finite-packet-promotion-blocked",
        finite_promotion_blocked,
        statuses["higher_shell_complete_packet_monotonicity_gate"],
    )
    report(
        "finite-moment-threshold-fv-authority-absent",
        moment_threshold_fv_authority_absent,
        statuses["finite_moment_atom_residue_obstruction"],
    )
    report(
        "bridge-roots-remain-absent",
        bridge_roots_absent,
        "source-Higgs, W/Z, and neutral bridge roots checked",
    )
    report(
        "scan-finds-no-strict-schur-scalar-lsz-artifact",
        scan_no_strict_current_artifact,
        str(scan),
    )
    report(
        "aggregate-gates-remain-open",
        aggregate_gates_open,
        "assembly/retained/campaign/completion audit deny closure",
    )
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and not any(strict_presence.values())
        and finite_schur_support_only
        and strict_kprime_rows_absent
        and scalar_lsz_authority_absent
        and finite_promotion_blocked
        and moment_threshold_fv_authority_absent
        and bridge_roots_absent
        and scan_no_strict_current_artifact
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block117 current PR230 head contains no strict "
            "Schur/scalar-LSZ pole authority artifact: K-prime pole rows, strict "
            "moment/threshold/FV authority, and required source-Higgs/WZ/neutral "
            "bridge roots remain absent"
        ),
        "conditional_surface_status": (
            "Schur/scalar-LSZ support only after a future same-surface artifact supplies "
            "strict pole coordinate, K-prime derivative or Schur/Feshbach equivalent, "
            "source projection numerator, threshold/FV/IR/contact authority, and a "
            "canonical O_H/source-overlap or physical W/Z/neutral bridge"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block117 is a strict artifact resolver and exact boundary. It confirms "
            "finite A/B/C rows and finite C_ss/C_sx/C_xx packets are support only; no "
            "strict K-prime pole-row artifact, scalar-LSZ moment/threshold/FV authority, "
            "or physical bridge root is present."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block117_schur_scalar_lsz_strict_artifact_resolver_passed": passed,
        "finite_schur_abc_support_only": finite_schur_support_only,
        "strict_kprime_rows_absent": strict_kprime_rows_absent,
        "scalar_lsz_authority_absent": scalar_lsz_authority_absent,
        "finite_packet_promotion_blocked": finite_promotion_blocked,
        "moment_threshold_fv_authority_absent": moment_threshold_fv_authority_absent,
        "bridge_roots_absent": bridge_roots_absent,
        "scan_finds_no_strict_schur_scalar_lsz_artifact": scan_no_strict_current_artifact,
        "strict_artifact_presence": strict_presence,
        "candidate_scan_summary": scan,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not infer K-prime pole rows from finite C_ss/C_sx/C_xx rows",
            "does not treat finite A/B/C inverse blocks as strict pole Schur/Feshbach rows",
            "does not treat Stieltjes diagnostics or finite fits as threshold/FVIR authority",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
            "does not set kappa_s, c2, or Z_match by fiat",
        ],
        "exact_next_action": (
            "Create a strict Schur/scalar-LSZ artifact: pole coordinate, K-prime "
            "derivative or exact Schur/Feshbach equivalent, source projection numerator, "
            "threshold/FV/IR/contact authority, and canonical O_H/source-overlap or a "
            "physical W/Z/neutral bridge. Otherwise pivot to a fresh source-Higgs, W/Z, "
            "or neutral strict packet."
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

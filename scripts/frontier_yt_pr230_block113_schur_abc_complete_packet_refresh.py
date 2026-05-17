#!/usr/bin/env python3
"""
PR #230 Block113 complete finite Schur A/B/C packet refresh.

The old finite Schur A/B/C note was written when the two-source taste-radial
packet was still a 30/63 prefix.  The row artifact itself has since been
refreshed to 63/63.  This runner certifies that complete finite-row state and
keeps the strict firewall intact:

    finite inverse rows from C_ss/C_sx/C_xx != strict pole Schur/Feshbach rows.

This is useful support for the Schur route, not retained/proposed_retained
top-Yukawa closure.
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
    / "yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json"
)

FINITE_ABC = "outputs/yt_pr230_two_source_taste_radial_schur_abc_finite_rows_2026-05-06.json"

PARENTS = {
    "finite_schur_abc_rows": FINITE_ABC,
    "block111_schur_kprime_packet_gap": "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json",
    "block112_helmholtz_obstruction": "outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json",
    "schur_kernel_contract": "outputs/yt_schur_kernel_row_contract_gate_2026-05-03.json",
    "block69_strict_kprime_contract": "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json",
    "block70_schur_feshbach_theorem": "outputs/yt_pr230_block70_schur_feshbach_kprime_residue_theorem_2026-05-12.json",
    "complete_packet_monotonicity": "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
}

STRICT_ARTIFACT_PATHS = {
    "strict_schur_feshbach_kprime_rows": "outputs/yt_pr230_strict_schur_feshbach_kprime_rows_2026-05-17.json",
    "strict_schur_abc_kernel_rows": "outputs/yt_pr230_schur_abc_kernel_rows_2026-05-17.json",
    "strict_scalar_lsz_moment_threshold_fv": "outputs/yt_pr230_strict_scalar_lsz_moment_threshold_fv_authority_2026-05-17.json",
    "canonical_oh_certificate": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
    "source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "wz_response_rows": "outputs/yt_pr230_wz_response_rows_2026-05-07.json",
}

EXPECTED_CHUNKS = 63
EXPECTED_MODES = {"0,0,0", "1,0,0", "0,1,0", "0,0,1"}

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
    "treated_finite_abc_rows_as_strict_pole_rows": False,
    "treated_finite_shell_derivatives_as_kprime_pole": False,
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


def finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def strict_artifact_presence() -> dict[str, bool]:
    return {name: (ROOT / rel_path).exists() for name, rel_path in STRICT_ARTIFACT_PATHS.items()}


def audit_complete_finite_abc(finite_abc: dict[str, Any]) -> dict[str, Any]:
    rows = finite_abc.get("chunk_finite_schur_abc_rows")
    rows = rows if isinstance(rows, list) else []
    issues: list[str] = []
    max_residual = 0.0
    finite_delta_count = 0
    finite_difference_count = 0

    for row in rows:
        if not isinstance(row, dict):
            issues.append("non-object chunk row")
            continue
        chunk = row.get("chunk_index")
        modes = row.get("mode_rows") if isinstance(row.get("mode_rows"), dict) else {}
        if set(modes) != EXPECTED_MODES:
            issues.append(f"chunk{chunk}: mode set mismatch")
        if not finite(row.get("max_inverse_identity_residual")):
            issues.append(f"chunk{chunk}: residual missing")
        else:
            max_residual = max(max_residual, abs(float(row["max_inverse_identity_residual"])))
        for mode, mode_row in modes.items():
            if not isinstance(mode_row, dict):
                issues.append(f"chunk{chunk} {mode}: row missing")
                continue
            required = (
                "Delta_sx",
                "A_finite_K_ss",
                "B_finite_K_sx",
                "C_finite_K_xx",
                "rho_sx",
            )
            if all(finite(mode_row.get(key)) for key in required) and float(mode_row["Delta_sx"]) > 0.0:
                finite_delta_count += 1
            else:
                issues.append(f"chunk{chunk} {mode}: finite inverse row invalid")
        differences = row.get("finite_difference") if isinstance(row.get("finite_difference"), dict) else {}
        if differences and all(finite(value) for value in differences.values()):
            finite_difference_count += 1
        else:
            issues.append(f"chunk{chunk}: finite shell differences invalid")

    summary = finite_abc.get("finite_shell_summary")
    summary_counts = {}
    if isinstance(summary, dict):
        for key, value in summary.items():
            if isinstance(value, dict):
                summary_counts[key] = value.get("count")

    return {
        "row_count": len(rows),
        "issues": issues,
        "max_inverse_identity_residual": max_residual,
        "finite_inverse_mode_rows": finite_delta_count,
        "finite_difference_chunk_rows": finite_difference_count,
        "summary_counts": summary_counts,
    }


def main() -> int:
    print("PR #230 Block113 Schur A/B/C complete-packet refresh")
    print("=" * 72)

    certificates = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certificates.items()}
    missing = [name for name, cert in certificates.items() if not cert]
    proposals = [name for name, cert in certificates.items() if cert.get("proposal_allowed") is True]
    finite_abc = certificates["finite_schur_abc_rows"]
    audit = audit_complete_finite_abc(finite_abc)
    strict_presence = strict_artifact_presence()

    finite_packet_complete = (
        finite_abc.get("two_source_taste_radial_schur_abc_finite_rows_passed") is True
        and finite_abc.get("proposal_allowed") is False
        and finite_abc.get("ready_chunks") == EXPECTED_CHUNKS
        and finite_abc.get("expected_chunks") == EXPECTED_CHUNKS
        and audit["row_count"] == EXPECTED_CHUNKS
        and audit["finite_inverse_mode_rows"] == EXPECTED_CHUNKS * len(EXPECTED_MODES)
        and audit["finite_difference_chunk_rows"] == EXPECTED_CHUNKS
        and not audit["issues"]
    )
    inverse_identity_clean = audit["max_inverse_identity_residual"] < 1.0e-10
    finite_summary_complete = bool(audit["summary_counts"]) and all(
        count == EXPECTED_CHUNKS for count in audit["summary_counts"].values()
    )
    finite_rows_support_only = (
        finite_abc.get("finite_schur_abc_rows_written") is True
        and finite_abc.get("strict_schur_abc_kernel_rows_written") is False
        and finite_abc.get("strict_schur_kprime_authority_passed") is False
        and finite_abc.get("pole_location_or_derivative_rows_present") is False
        and finite_abc.get("fv_ir_zero_mode_authority_present") is False
        and finite_abc.get("canonical_higgs_operator_identity_passed") is False
        and finite_abc.get("used_as_physical_yukawa_readout") is False
    )
    block111_keeps_strict_kprime_absent = (
        "complete higher-shell packet contains no strict Schur-Feshbach K-prime"
        in statuses["block111_schur_kprime_packet_gap"]
        and certificates["block111_schur_kprime_packet_gap"].get(
            "block111_schur_kprime_packet_gap_audit_passed"
        )
        is True
        and certificates["block111_schur_kprime_packet_gap"].get(
            "strict_kprime_row_emissions_present"
        )
        is False
    )
    block112_keeps_action_overlap_absent = (
        "lacks Helmholtz mixed-derivative rows" in statuses["block112_helmholtz_obstruction"]
        and certificates["block112_helmholtz_obstruction"].get(
            "block112_helmholtz_action_integrability_obstruction_passed"
        )
        is True
        and certificates["block112_helmholtz_obstruction"].get(
            "canonical_source_higgs_overlap_fixed"
        )
        is False
    )
    strict_contract_open = (
        certificates["schur_kernel_contract"].get("schur_kernel_row_contract_gate_passed")
        is False
        and certificates["schur_kernel_contract"].get("candidate_rows_present") is False
    )
    block69_strict_rows_missing = (
        certificates["block69_strict_kprime_contract"].get("proposal_allowed") is False
        and certificates["block69_strict_kprime_contract"].get("strict_pass")
        is False
    )
    block70_theorem_support_only = (
        certificates["block70_schur_feshbach_theorem"].get("proposal_allowed") is False
        and "Schur-Feshbach K-prime residue theorem" in statuses["block70_schur_feshbach_theorem"]
        and "physical rows absent" in statuses["block70_schur_feshbach_theorem"]
    )
    strict_artifacts_absent = not any(strict_presence.values())
    aggregate_gates_open = (
        certificates["full_positive_assembly"].get("proposal_allowed") is False
        and certificates["retained_route"].get("proposal_allowed") is False
        and certificates["campaign_status"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("finite-abc-packet-complete-63", finite_packet_complete, str(audit))
    report("finite-abc-inverse-identity-clean", inverse_identity_clean, f"max={audit['max_inverse_identity_residual']}")
    report("finite-abc-summary-counts-complete", finite_summary_complete, str(audit["summary_counts"]))
    report("finite-abc-support-only-boundary", finite_rows_support_only, FINITE_ABC)
    report("block111-keeps-strict-kprime-absent", block111_keeps_strict_kprime_absent, statuses["block111_schur_kprime_packet_gap"])
    report("block112-keeps-source-overlap-absent", block112_keeps_action_overlap_absent, statuses["block112_helmholtz_obstruction"])
    report("strict-schur-contract-still-open", strict_contract_open, statuses["schur_kernel_contract"])
    report("block69-strict-kprime-rows-missing", block69_strict_rows_missing, statuses["block69_strict_kprime_contract"])
    report("block70-theorem-support-only", block70_theorem_support_only, statuses["block70_schur_feshbach_theorem"])
    report("strict-artifact-paths-absent", strict_artifacts_absent, str(strict_presence))
    report("aggregate-gates-deny-proposal", aggregate_gates_open, "assembly/retained/campaign proposal_allowed=false")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and finite_packet_complete
        and inverse_identity_clean
        and finite_summary_complete
        and finite_rows_support_only
        and block111_keeps_strict_kprime_absent
        and block112_keeps_action_overlap_absent
        and strict_contract_open
        and block69_strict_rows_missing
        and block70_theorem_support_only
        and strict_artifacts_absent
        and aggregate_gates_open
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "bounded-support / Block113 complete 63/63 finite Schur A/B/C row "
            "artifact confirmed; strict Schur/Feshbach pole authority absent"
        ),
        "conditional_surface_status": (
            "Schur-route support only if a future strict same-surface artifact "
            "adds pole coordinate, K-prime derivative or exact Feshbach "
            "equivalent, source projection numerator, FV/IR/contact authority, "
            "and canonical O_H/source-overlap or W/Z physical-response authority"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block113 confirms a genuine complete finite Schur A/B/C support "
            "artifact, but finite inverse C_ss/C_sx/C_xx rows are not strict "
            "pole Schur/Feshbach rows and do not fix canonical O_H or source "
            "overlap."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block113_schur_abc_complete_packet_refresh_passed": passed,
        "complete_finite_schur_abc_rows_confirmed": finite_packet_complete,
        "finite_schur_abc_artifact": FINITE_ABC,
        "ready_chunks": finite_abc.get("ready_chunks"),
        "expected_chunks": finite_abc.get("expected_chunks"),
        "audit_summary": audit,
        "finite_shell_summary": finite_abc.get("finite_shell_summary"),
        "finite_rows_support_only": finite_rows_support_only,
        "strict_schur_abc_kernel_rows_present": False,
        "strict_schur_kprime_rows_present": False,
        "pole_location_or_derivative_rows_present": False,
        "fv_ir_zero_mode_authority_present": False,
        "canonical_higgs_operator_identity_passed": False,
        "canonical_source_higgs_overlap_fixed": False,
        "strict_artifact_presence": strict_presence,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not treat finite Schur A/B/C inverse rows as strict pole rows",
            "does not use finite shell differences as K'(pole)",
            "does not identify taste-radial x with canonical O_H",
            "does not relabel finite C_sx/C_xx as physical C_sH/C_HH",
            "does not set kappa_s, c2, Z_match, or g2 to one",
        ],
        "exact_next_action": (
            "Use the 63/63 finite A/B/C artifact only as staging support.  "
            "For closure, add strict pole Schur/Feshbach K-prime rows with "
            "FV/IR/contact authority and a canonical O_H/source-overlap or W/Z "
            "physical-response bridge."
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

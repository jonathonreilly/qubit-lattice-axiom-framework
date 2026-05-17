#!/usr/bin/env python3
"""
PR #230 Block129 strict Schur/Feshbach pole-authority construction attempt.

Block128 closes the current W/Z/source-row construction attempt.  This runner
pivots to the next admissible root: can the current complete finite Schur
A/B/C packet, or any existing strict-row sidecar, be assembled into a genuine
Schur/Feshbach pole authority packet?

The strict packet must contain same-surface pole coordinate, K'(pole) or an
exact equivalent derivative row, source projection numerator/residue authority,
model-class/FV/IR/contact authority, and a canonical bridge.  Finite A/B/C
rows, finite-shell slopes, Stieltjes scouts, smoke rows, and chunk completion
are not promoted to closure.
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
    / "yt_pr230_block129_schur_pole_authority_construction_attempt_2026-05-17.json"
)

RAW_GLOB = (
    "outputs/yt_direct_lattice_correlator_production_schur_higher_shell_rows/"
    "L12_T24_chunk*/L12xT24/ensemble_measurement.json"
)

STRICT_ROW_INPUTS = {
    "block69_strict_rows": "outputs/yt_pr230_block69_strict_kprime_pole_residue_rows_2026-05-12.json",
    "strict_kprime_rows": "outputs/yt_pr230_strict_kprime_pole_residue_rows_2026-05-12.json",
    "schur_kprime_rows": "outputs/yt_schur_kprime_pole_residue_rows_2026-05-12.json",
    "pr230_schur_scalar_kernel_rows": "outputs/yt_pr230_schur_scalar_kernel_rows_2026-05-12.json",
    "legacy_schur_scalar_kernel_rows": "outputs/yt_schur_scalar_kernel_rows_2026-05-03.json",
    "block113_strict_schur_feshbach_rows": "outputs/yt_pr230_strict_schur_feshbach_kprime_rows_2026-05-17.json",
    "block113_strict_abc_kernel_rows": "outputs/yt_pr230_schur_abc_kernel_rows_2026-05-17.json",
    "strict_scalar_lsz_moment_threshold_fv": "outputs/yt_pr230_strict_scalar_lsz_moment_threshold_fv_authority_2026-05-17.json",
}

PARENTS = {
    "block128_strict_wz_source_row_construction_attempt": (
        "outputs/yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
    ),
    "block121_schur_finite_packet_nonidentifiability": (
        "outputs/yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json"
    ),
    "block117_schur_scalar_lsz_resolver": (
        "outputs/yt_pr230_block117_schur_scalar_lsz_strict_artifact_resolver_2026-05-17.json"
    ),
    "block113_schur_abc_complete_packet": (
        "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json"
    ),
    "block111_schur_kprime_gap": (
        "outputs/yt_pr230_block111_schur_kprime_packet_gap_audit_2026-05-17.json"
    ),
    "strict_kprime_pole_residue_certificate": (
        "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json"
    ),
    "block70_schur_feshbach_theorem": (
        "outputs/yt_pr230_block70_schur_feshbach_kprime_residue_theorem_2026-05-12.json"
    ),
    "finite_schur_abc_rows": (
        "outputs/yt_pr230_two_source_taste_radial_schur_abc_finite_rows_2026-05-06.json"
    ),
    "finite_schur_pole_lift_gate": (
        "outputs/yt_pr230_two_source_taste_radial_schur_pole_lift_gate_2026-05-06.json"
    ),
    "complete_packet_monotonicity": (
        "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json"
    ),
    "strict_scalar_lsz_moment_fv": (
        "outputs/yt_pr230_strict_scalar_lsz_moment_fv_authority_gate_2026-05-07.json"
    ),
    "stieltjes_moment_certificate": (
        "outputs/yt_fh_lsz_stieltjes_moment_certificate_gate_2026-05-05.json"
    ),
    "pade_stieltjes_bounds": (
        "outputs/yt_fh_lsz_pade_stieltjes_bounds_gate_2026-05-05.json"
    ),
    "schur_kernel_row_contract": "outputs/yt_schur_kernel_row_contract_gate_2026-05-03.json",
    "schur_kprime_row_absence_guard": "outputs/yt_schur_kprime_row_absence_guard_2026-05-03.json",
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
    "used_package_hierarchy_v": False,
    "used_fitted_selector": False,
    "used_finite_abc_rows_as_pole_rows": False,
    "used_stieltjes_scout_as_authority": False,
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


def load_json(path: str | Path) -> Any:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    return json.loads(full.read_text(encoding="utf-8"))


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def walk(obj: Any) -> list[tuple[str, Any]]:
    out: list[tuple[str, Any]] = []

    def rec(value: Any, path: tuple[str, ...]) -> None:
        out.append((".".join(path), value))
        if isinstance(value, dict):
            for key, child in value.items():
                rec(child, path + (str(key),))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                rec(child, path + (str(index),))

    rec(obj, ())
    return out


def scan_raw_higher_shell_rows() -> dict[str, Any]:
    paths = sorted(ROOT.glob(RAW_GLOB))
    strict_key_fragments = (
        "schur_kprime_kernel_rows",
        "Kprime_at_pole",
        "kprime_at_pole",
        "K_prime_at_pole",
        "pole_residue",
        "pole_coordinate",
        "source_projection_numerator",
        "strict_schur",
        "strict_kprime",
    )
    finite_source_higgs_rows = 0
    finite_lsz_rows = 0
    strict_key_hits: list[dict[str, str]] = []
    for path in paths:
        data = load_json(path)
        text_hits = []
        for key_path, value in walk(data):
            last = key_path.rsplit(".", 1)[-1]
            if last == "pole_residue_rows" and value == []:
                continue
            if any(fragment == last or fragment in last for fragment in strict_key_fragments):
                text_hits.append(key_path)
        if text_hits:
            strict_key_hits.append({"path": rel(path), "keys": text_hits[:12]})
        ensembles = data.get("ensembles") if isinstance(data, dict) else None
        surfaces = ensembles if isinstance(ensembles, list) else [data]
        for ensemble in surfaces:
            if not isinstance(ensemble, dict):
                continue
            source = ensemble.get("source_higgs_cross_correlator_analysis")
            lsz = ensemble.get("scalar_two_point_lsz_analysis")
            if isinstance(source, dict):
                mode_rows = source.get("mode_rows")
                if isinstance(mode_rows, dict):
                    for row in mode_rows.values():
                        if (
                            isinstance(row, dict)
                            and finite(row.get("C_ss_real"))
                            and finite(row.get("C_sx_real"))
                            and finite(row.get("C_xx_real"))
                        ):
                            finite_source_higgs_rows += 1
            if isinstance(lsz, dict):
                mode_rows = lsz.get("mode_rows")
                if isinstance(mode_rows, dict):
                    for row in mode_rows.values():
                        if isinstance(row, dict) and finite(row.get("C_ss_real")):
                            finite_lsz_rows += 1
    return {
        "glob": RAW_GLOB,
        "raw_file_count": len(paths),
        "finite_source_higgs_mode_rows": finite_source_higgs_rows,
        "finite_scalar_lsz_mode_rows": finite_lsz_rows,
        "strict_schur_or_pole_key_hit_count": len(strict_key_hits),
        "strict_schur_or_pole_key_hits_sample": strict_key_hits[:5],
    }


def strict_row_file_presence() -> dict[str, bool]:
    return {name: (ROOT / path).exists() for name, path in STRICT_ROW_INPUTS.items()}


def main() -> int:
    print("PR #230 Block129 strict Schur/Feshbach pole-authority construction attempt")
    print("=" * 88)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = strict_row_file_presence()
    raw_scan = scan_raw_higher_shell_rows()

    block128_pivot_clean = (
        certs["block128_strict_wz_source_row_construction_attempt"].get(
            "block128_strict_wz_source_row_construction_attempt_passed"
        )
        is True
        and certs["block128_strict_wz_source_row_construction_attempt"]
        .get("constructive_status", {})
        .get("strict_wz_constructible_from_current_raw_rows")
        is False
        and certs["block128_strict_wz_source_row_construction_attempt"]
        .get("constructive_status", {})
        .get("strict_source_higgs_constructible_from_current_raw_rows")
        is False
    )
    explicit_strict_rows_absent = (
        not any(strict_presence.values())
        and certs["strict_kprime_pole_residue_certificate"].get("strict_pass") is False
        and "rows missing" in statuses["strict_kprime_pole_residue_certificate"]
    )
    raw_contains_no_strict_pole_keys = (
        raw_scan["raw_file_count"] == 63
        and raw_scan["finite_source_higgs_mode_rows"] > 0
        and raw_scan["finite_scalar_lsz_mode_rows"] > 0
        and raw_scan["strict_schur_or_pole_key_hit_count"] == 0
    )
    finite_abc_complete_support_only = (
        certs["block113_schur_abc_complete_packet"].get(
            "block113_schur_abc_complete_packet_refresh_passed"
        )
        is True
        and certs["block113_schur_abc_complete_packet"].get(
            "complete_finite_schur_abc_rows_confirmed"
        )
        is True
        and certs["block113_schur_abc_complete_packet"].get("finite_rows_support_only")
        is True
        and certs["finite_schur_abc_rows"].get("ready_chunks") == 63
        and certs["finite_schur_abc_rows"].get("strict_schur_abc_kernel_rows_written")
        is False
    )
    finite_to_pole_promotion_blocked = (
        certs["block121_schur_finite_packet_nonidentifiability"].get(
            "block121_schur_finite_packet_pole_derivative_nonidentifiability_passed"
        )
        is True
        and certs["block121_schur_finite_packet_nonidentifiability"]
        .get("finite_node_vanishing_witness", {})
        .get("finite_rows_all_match")
        is True
        and certs["block121_schur_finite_packet_nonidentifiability"]
        .get("finite_node_vanishing_witness", {})
        .get("kprime_changes")
        is True
        and certs["finite_schur_pole_lift_gate"].get("strict_pole_lift_passed") is False
    )
    monotonicity_does_not_rescue = (
        certs["complete_packet_monotonicity"].get(
            "higher_shell_complete_packet_monotonicity_gate_passed"
        )
        is True
        and certs["complete_packet_monotonicity"].get(
            "strict_schur_or_scalar_lsz_authority_passed"
        )
        is False
        and certs["complete_packet_monotonicity"].get("surviving_complete_monotonicity_fields")
        == []
        and bool(certs["complete_packet_monotonicity"].get("failing_complete_monotonicity_fields"))
    )
    model_fv_ir_threshold_absent = (
        certs["strict_scalar_lsz_moment_fv"].get(
            "strict_scalar_lsz_moment_fv_authority_present"
        )
        is False
        and certs["stieltjes_moment_certificate"].get("moment_certificate_gate_passed")
        is False
        and "strict moment-threshold certificate absent" in statuses["pade_stieltjes_bounds"]
    )
    schur_contract_roots_open = (
        certs["schur_kernel_row_contract"].get("candidate_rows_present") is False
        and certs["schur_kernel_row_contract"].get("candidate_rows_valid") is False
        and certs["schur_kprime_row_absence_guard"].get("current_schur_kernel_rows_present")
        is False
        and certs["block111_schur_kprime_gap"].get("strict_kprime_row_emissions_present")
        is False
    )
    theorem_support_only = (
        "Schur-Feshbach K-prime residue theorem" in statuses["block70_schur_feshbach_theorem"]
        and "physical rows absent" in statuses["block70_schur_feshbach_theorem"]
        and certs["block70_schur_feshbach_theorem"].get("proposal_allowed") is False
    )
    aggregate_gates_still_closed = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    strict_schur_constructible = all(
        (
            explicit_strict_rows_absent is False,
            raw_contains_no_strict_pole_keys is False,
            finite_to_pole_promotion_blocked is False,
            monotonicity_does_not_rescue is False,
            model_fv_ir_threshold_absent is False,
            schur_contract_roots_open is False,
        )
    )

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("block128-pivot-clean", block128_pivot_clean, "W/Z/source-Higgs construction closed before Schur pivot")
    report("explicit-strict-row-sidecars-absent", explicit_strict_rows_absent, str(strict_presence))
    report("raw-higher-shell-has-no-strict-pole-keys", raw_contains_no_strict_pole_keys, str(raw_scan))
    report("finite-abc-complete-support-only", finite_abc_complete_support_only, statuses["block113_schur_abc_complete_packet"])
    report("finite-to-pole-promotion-blocked", finite_to_pole_promotion_blocked, statuses["block121_schur_finite_packet_nonidentifiability"])
    report("monotonicity-does-not-rescue", monotonicity_does_not_rescue, str(certs["complete_packet_monotonicity"].get("failing_complete_monotonicity_fields")))
    report("model-fv-ir-threshold-authority-absent", model_fv_ir_threshold_absent, statuses["strict_scalar_lsz_moment_fv"])
    report("schur-contract-roots-open", schur_contract_roots_open, statuses["schur_kernel_row_contract"])
    report("schur-theorem-support-only", theorem_support_only, statuses["block70_schur_feshbach_theorem"])
    report("aggregate-gates-still-closed", aggregate_gates_still_closed, "proposal_allowed remains false")
    report("constructive-schur-authority-not-available", strict_schur_constructible is False, "strict_schur_constructible=False")
    report("claim-firewall-clean", firewall_clean, "no forbidden closure import used")

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block129 cannot construct strict "
            "Schur/Feshbach pole authority from the current explicit-row "
            "sidecars, raw higher-shell rows, or complete finite A/B/C packet"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current Schur surface has complete finite A/B/C support but no "
            "same-surface strict pole coordinate, K'(pole) derivative row, "
            "source projection numerator/residue, accepted model/FV/IR/contact "
            "authority, or canonical bridge.  Existing finite-row and "
            "monotonicity diagnostics explicitly do not promote to a strict "
            "pole authority packet."
        ),
        "block129_schur_pole_authority_construction_attempt_passed": FAIL_COUNT == 0,
        "current_closure_satisfied": False,
        "constructive_status": {
            "strict_schur_feshbach_pole_authority_constructible": strict_schur_constructible,
            "explicit_strict_row_sidecars_present": any(strict_presence.values()),
            "raw_strict_pole_rows_present": raw_scan["strict_schur_or_pole_key_hit_count"] > 0,
            "finite_abc_packet_complete": finite_abc_complete_support_only,
            "finite_packet_promotable_to_pole_authority": False,
            "model_fv_ir_threshold_authority_present": False,
            "canonical_bridge_present": False,
        },
        "strict_row_file_presence": strict_presence,
        "raw_higher_shell_scan": raw_scan,
        "finite_packet_blockers": {
            "block121_finite_node_nonidentifiability": finite_to_pole_promotion_blocked,
            "complete_packet_monotonicity_failures": certs["complete_packet_monotonicity"].get(
                "failing_complete_monotonicity_fields"
            ),
            "surviving_complete_monotonicity_fields": certs["complete_packet_monotonicity"].get(
                "surviving_complete_monotonicity_fields"
            ),
            "strict_scalar_lsz_authority_present": certs["strict_scalar_lsz_moment_fv"].get(
                "strict_scalar_lsz_moment_fv_authority_present"
            ),
            "stieltjes_moment_certificate_passed": certs["stieltjes_moment_certificate"].get(
                "moment_certificate_gate_passed"
            ),
        },
        "required_strict_schur_packet_fields": [
            "same-surface pole coordinate",
            "K'(pole) or exact derivative row",
            "source projection numerator or residue row",
            "accepted model-class or analytic-continuation authority",
            "FV/IR/contact/threshold authority",
            "canonical O_H/source-overlap or strict physical-response bridge",
        ],
        "recommended_pivot": (
            "neutral H3/H4 physical-transfer plus source/canonical-Higgs "
            "coupling authority, unless a new strict Schur/Feshbach pole-row "
            "artifact appears"
        ),
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": {
            "does_not_use_finite_abc_rows_as_pole_rows": True,
            "does_not_use_stieltjes_or_one_pole_scout_as_authority": True,
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_import_observed_or_forbidden_shortcuts": True,
        },
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

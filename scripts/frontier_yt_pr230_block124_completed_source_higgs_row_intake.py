#!/usr/bin/env python3
"""
PR #230 Block124 completed source-Higgs row strict intake.

The L12 higher-shell source-Higgs/taste-radial chunks are now complete.  This
runner consumes the completed chunk packet and resolves it against the Block123
source-Higgs LSZ readout contract:

    y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH

The current rows are finite equal-time C_ss/C_sx/C_xx rows with an unratified
taste-radial second source x.  They are useful diagnostics, but they are not
strict same-pole C_ss/C_sH/C_HH residues and they do not certify canonical O_H.
"""

from __future__ import annotations

import json
import math
import statistics
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json"
)

EXPECTED_CHUNKS = 63
EXPECTED_MODE_COUNT = 11

PARENTS = {
    "block123_source_higgs_lsz_readout_formula": (
        "outputs/yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json"
    ),
    "block113_complete_finite_schur_abc": (
        "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json"
    ),
    "block114_source_higgs_strict_artifact_resolver": (
        "outputs/yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json"
    ),
    "target_timeseries_full_set": (
        "outputs/yt_fh_lsz_target_timeseries_full_set_checkpoint_2026-05-12.json"
    ),
    "higher_shell_chunk063_checkpoint": (
        "outputs/yt_pr230_schur_higher_shell_chunk063_checkpoint_2026-05-12.json"
    ),
    "two_source_chunk063_checkpoint": (
        "outputs/yt_pr230_two_source_taste_radial_chunk063_checkpoint_2026-05-06.json"
    ),
    "full_positive_assembly": (
        "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json"
    ),
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
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
    "treated_finite_c_sx_c_xx_as_c_sh_c_hh_pole_rows": False,
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


def load_json(path: str | Path) -> Any:
    full = Path(path)
    if not full.is_absolute():
        full = ROOT / full
    if not full.exists():
        return {}
    return json.loads(full.read_text(encoding="utf-8"))


def status(cert: Any) -> str:
    return str(cert.get("actual_current_surface_status", "")) if isinstance(cert, dict) else ""


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def summarize(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": statistics.fmean(values),
        "stdev": statistics.pstdev(values) if len(values) > 1 else 0.0,
    }


def chunk_path(index: int) -> Path:
    return (
        ROOT
        / "outputs"
        / "yt_pr230_schur_higher_shell_rows"
        / f"yt_pr230_schur_higher_shell_rows_L12_T24_chunk{index:03d}_2026-05-07.json"
    )


def audit_completed_rows() -> dict[str, Any]:
    present_indices: list[int] = []
    missing_indices: list[int] = []
    issues: list[str] = []
    mode_sets: set[tuple[str, ...]] = set()
    pole_residue_row_hits: list[dict[str, Any]] = []
    canonical_identity_hits: list[int] = []
    alias_firewall_hits: list[int] = []
    nonreadout_violations: list[int] = []
    forbidden_firewall_hits: list[dict[str, Any]] = []
    finite_row_count = 0
    timeseries_row_count = 0
    rho_values: list[float] = []
    abs_rho_values: list[float] = []
    gram_determinants: list[float] = []
    c_ss_values: list[float] = []
    c_sx_values: list[float] = []
    c_xx_values: list[float] = []
    p_hat_sq_values: list[float] = []

    for index in range(1, EXPECTED_CHUNKS + 1):
        path = chunk_path(index)
        if not path.exists():
            missing_indices.append(index)
            continue
        present_indices.append(index)
        data = load_json(path)
        if not isinstance(data, dict):
            issues.append(f"chunk{index:03d}: root is not an object")
            continue
        ensembles = data.get("ensembles")
        if not isinstance(ensembles, list) or len(ensembles) != 1:
            issues.append(f"chunk{index:03d}: expected exactly one ensemble")
            continue
        ensemble = ensembles[0]
        metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
        run_control = metadata.get("run_control") if isinstance(metadata.get("run_control"), dict) else {}
        source_meta = (
            metadata.get("source_higgs_cross_correlator")
            if isinstance(metadata.get("source_higgs_cross_correlator"), dict)
            else {}
        )
        analysis = (
            ensemble.get("source_higgs_cross_correlator_analysis")
            if isinstance(ensemble.get("source_higgs_cross_correlator_analysis"), dict)
            else {}
        )
        scalar = (
            ensemble.get("scalar_two_point_lsz_analysis")
            if isinstance(ensemble.get("scalar_two_point_lsz_analysis"), dict)
            else {}
        )
        mode_rows = analysis.get("mode_rows") if isinstance(analysis.get("mode_rows"), dict) else {}
        scalar_mode_rows = (
            scalar.get("mode_rows") if isinstance(scalar.get("mode_rows"), dict) else {}
        )
        mode_sets.add(tuple(sorted(mode_rows)))

        if run_control.get("production_targets") is not True:
            issues.append(f"chunk{index:03d}: production_targets not true")
        if run_control.get("seed_control_version") != "numba_gauge_seed_v1":
            issues.append(f"chunk{index:03d}: seed_control_version mismatch")
        if run_control.get("fh_lsz_selected_mass_only") is not True:
            issues.append(f"chunk{index:03d}: selected-mass-only policy missing")
        if run_control.get("normal_equation_cache_enabled") is not True:
            issues.append(f"chunk{index:03d}: normal-equation cache metadata missing")
        if source_meta.get("enabled") is not True:
            issues.append(f"chunk{index:03d}: source-Higgs finite rows not enabled")
        if source_meta.get("used_as_physical_yukawa_readout") is not False:
            nonreadout_violations.append(index)
        if source_meta.get("canonical_higgs_operator_realization") != "certificate_supplied_unratified":
            issues.append(f"chunk{index:03d}: canonical operator status is not unratified")

        operator = source_meta.get("operator") if isinstance(source_meta.get("operator"), dict) else {}
        if operator.get("canonical_higgs_operator_identity_passed") is True:
            canonical_identity_hits.append(index)
        if analysis.get("canonical_higgs_operator_identity_passed") is True:
            canonical_identity_hits.append(index)
        if analysis.get("used_as_physical_yukawa_readout") is not False:
            nonreadout_violations.append(index)

        meta_firewall = source_meta.get("firewall") if isinstance(source_meta.get("firewall"), dict) else {}
        analysis_firewall = (
            analysis.get("firewall") if isinstance(analysis.get("firewall"), dict) else {}
        )
        for name, value in {**meta_firewall, **analysis_firewall}.items():
            if value not in (False, None):
                forbidden_firewall_hits.append(
                    {"chunk_index": index, "field": name, "value": value}
                )

        aliases = (
            analysis.get("two_source_taste_radial_row_aliases")
            if isinstance(analysis.get("two_source_taste_radial_row_aliases"), dict)
            else {}
        )
        alias_ok = (
            aliases.get("available") is True
            and aliases.get("source_operator_symbol") == "x"
            and "not canonical-Higgs C_sH/C_HH rows" in str(aliases.get("strict_limit", ""))
        )
        if not alias_ok:
            alias_firewall_hits.append(index)

        pole_rows = analysis.get("pole_residue_rows")
        if isinstance(pole_rows, list) and pole_rows:
            pole_residue_row_hits.append(
                {"chunk_index": index, "count": len(pole_rows), "path": rel(path)}
            )
        elif not isinstance(pole_rows, list):
            issues.append(f"chunk{index:03d}: pole_residue_rows is not a list")

        if len(mode_rows) != EXPECTED_MODE_COUNT:
            issues.append(f"chunk{index:03d}: expected {EXPECTED_MODE_COUNT} mode rows")
        if set(mode_rows) != set(scalar_mode_rows):
            issues.append(f"chunk{index:03d}: scalar/source-Higgs mode sets differ")

        for mode, row in sorted(mode_rows.items()):
            if not isinstance(row, dict):
                issues.append(f"chunk{index:03d} {mode}: row is not an object")
                continue
            c_ss = row.get("C_ss_real")
            c_sx = row.get("C_sx_real", row.get("C_sH_real"))
            c_xx = row.get("C_xx_real", row.get("C_HH_real"))
            p_hat_sq = row.get("p_hat_sq")
            required_numbers = (c_ss, c_sx, c_xx, p_hat_sq)
            if not all(is_number(value) for value in required_numbers):
                issues.append(f"chunk{index:03d} {mode}: finite row numbers missing")
                continue
            c_ss_f = float(c_ss)
            c_sx_f = float(c_sx)
            c_xx_f = float(c_xx)
            if c_ss_f <= 0.0 or c_xx_f <= 0.0:
                issues.append(f"chunk{index:03d} {mode}: finite row is not positive")
                continue
            determinant = c_ss_f * c_xx_f - c_sx_f * c_sx_f
            rho = c_sx_f / math.sqrt(c_ss_f * c_xx_f)
            finite_row_count += 1
            gram_determinants.append(determinant)
            rho_values.append(rho)
            abs_rho_values.append(abs(rho))
            c_ss_values.append(c_ss_f)
            c_sx_values.append(c_sx_f)
            c_xx_values.append(c_xx_f)
            p_hat_sq_values.append(float(p_hat_sq))
            if (
                isinstance(row.get("C_ss_timeseries"), list)
                and isinstance(row.get("C_sx_timeseries"), list)
                and isinstance(row.get("C_xx_timeseries"), list)
            ):
                if (
                    len(row["C_ss_timeseries"]) == 16
                    and len(row["C_sx_timeseries"]) == 16
                    and len(row["C_xx_timeseries"]) == 16
                ):
                    timeseries_row_count += 1
                else:
                    issues.append(f"chunk{index:03d} {mode}: time series length mismatch")
            else:
                issues.append(f"chunk{index:03d} {mode}: time series absent")

    return {
        "expected_chunks": EXPECTED_CHUNKS,
        "present_indices": present_indices,
        "missing_indices": missing_indices,
        "mode_sets": [list(row) for row in sorted(mode_sets)],
        "issues": issues,
        "finite_row_count": finite_row_count,
        "expected_finite_row_count": EXPECTED_CHUNKS * EXPECTED_MODE_COUNT,
        "timeseries_row_count": timeseries_row_count,
        "expected_timeseries_row_count": EXPECTED_CHUNKS * EXPECTED_MODE_COUNT,
        "pole_residue_row_hits": pole_residue_row_hits,
        "canonical_identity_hits": sorted(set(canonical_identity_hits)),
        "alias_firewall_hits": alias_firewall_hits,
        "nonreadout_violations": sorted(set(nonreadout_violations)),
        "forbidden_firewall_hits": forbidden_firewall_hits,
        "finite_gram_diagnostic": {
            "rho_sx_summary": summarize(rho_values),
            "abs_rho_sx_summary": summarize(abs_rho_values),
            "gram_determinant_summary": summarize(gram_determinants),
            "C_ss_summary": summarize(c_ss_values),
            "C_sx_summary": summarize(c_sx_values),
            "C_xx_summary": summarize(c_xx_values),
            "p_hat_sq_values": sorted(set(round(value, 12) for value in p_hat_sq_values)),
            "finite_rank_one_proxy_failed": (
                bool(gram_determinants)
                and min(gram_determinants) > 1.0e-6
                and max(abs_rho_values) < 1.0e-2
            ),
            "strict_limit": (
                "This is a finite equal-time taste-radial diagnostic only.  "
                "It is not a pole-residue Gram-purity certificate and cannot "
                "be used as scalar LSZ or canonical-Higgs authority."
            ),
        },
    }


def main() -> int:
    print("PR #230 Block124 completed source-Higgs row strict intake")
    print("=" * 72)

    parents = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in parents.items()}
    missing_parents = [name for name, cert in parents.items() if not cert]
    proposal_parents = [
        name
        for name, cert in parents.items()
        if isinstance(cert, dict) and cert.get("proposal_allowed") is True
    ]
    audit = audit_completed_rows()

    block123 = parents["block123_source_higgs_lsz_readout_formula"]
    block113 = parents["block113_complete_finite_schur_abc"]
    block114 = parents["block114_source_higgs_strict_artifact_resolver"]
    full_set = parents["target_timeseries_full_set"]
    higher_chunk063 = parents["higher_shell_chunk063_checkpoint"]
    two_source_chunk063 = parents["two_source_chunk063_checkpoint"]

    completed_chunk_support_present = (
        full_set.get("proposal_allowed") is False
        and full_set.get("pass_count") == 9
        and full_set.get("fail_count") == 0
        and full_set.get("target_timeseries_summary", {}).get("complete_count") == 63
        and full_set.get("target_timeseries_summary", {}).get("incomplete_indices") == []
    )
    higher_shell_tail_verified = (
        higher_chunk063.get("proposal_allowed") is False
        and higher_chunk063.get("checkpoint_passed") is True
        and higher_chunk063.get("pass_count") == 15
        and higher_chunk063.get("fail_count") == 0
        and two_source_chunk063.get("proposal_allowed") is False
        and two_source_chunk063.get("checkpoint_passed") is True
        and two_source_chunk063.get("pass_count") == 15
        and two_source_chunk063.get("fail_count") == 0
    )
    finite_packet_complete = (
        len(audit["present_indices"]) == EXPECTED_CHUNKS
        and not audit["missing_indices"]
        and audit["finite_row_count"] == audit["expected_finite_row_count"]
        and audit["timeseries_row_count"] == audit["expected_timeseries_row_count"]
        and not audit["issues"]
    )
    finite_rows_not_strict_pole_rows = (
        len(audit["pole_residue_row_hits"]) == 0
        and len(audit["canonical_identity_hits"]) == 0
        and len(audit["alias_firewall_hits"]) == 0
        and len(audit["nonreadout_violations"]) == 0
        and len(audit["forbidden_firewall_hits"]) == 0
    )
    block123_contract_still_open = (
        isinstance(block123, dict)
        and block123.get("block123_source_higgs_lsz_readout_formula_passed") is True
        and block123.get("proposal_allowed") is False
        and block123.get("current_closure_satisfied") is False
        and block123.get("current_missing_packet", {}).get("strict_source_higgs_pole_rows_absent")
        is True
    )
    prior_strict_resolver_absent = (
        isinstance(block114, dict)
        and block114.get("block114_source_higgs_strict_artifact_resolver_passed") is True
        and block114.get("strict_source_higgs_pole_rows_absent") is True
        and block114.get("proposal_allowed") is False
    )
    finite_schur_packet_support_only = (
        isinstance(block113, dict)
        and block113.get("block113_schur_abc_complete_packet_refresh_passed") is True
        and block113.get("complete_finite_schur_abc_rows_confirmed") is True
        and block113.get("finite_rows_support_only") is True
        and block113.get("proposal_allowed") is False
    )
    aggregate_gates_open = (
        parents["full_positive_assembly"].get("proposal_allowed") is False
        and parents["retained_route"].get("proposal_allowed") is False
        and parents["campaign_status"].get("proposal_allowed") is False
    )
    finite_gram_support_only = (
        audit["finite_gram_diagnostic"]["finite_rank_one_proxy_failed"] is True
        and audit["finite_gram_diagnostic"]["abs_rho_sx_summary"].get("max", 1.0) < 1.0e-2
        and audit["finite_gram_diagnostic"]["gram_determinant_summary"].get("min", 0.0)
        > 1.0e-6
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing_parents, f"missing={missing_parents}")
    report("no-parent-authorizes-proposal", not proposal_parents, f"proposal_allowed={proposal_parents}")
    report(
        "target-timeseries-and-tail-chunks-complete",
        completed_chunk_support_present and higher_shell_tail_verified,
        "target-timeseries 63/63 plus chunk063 higher-shell/two-source checkpoints",
    )
    report(
        "completed-higher-shell-row-packet-present",
        finite_packet_complete,
        f"rows={audit['finite_row_count']} missing={audit['missing_indices']} issues={audit['issues'][:3]}",
    )
    report(
        "finite-rows-are-not-strict-pole-rows",
        finite_rows_not_strict_pole_rows,
        (
            f"pole_hits={audit['pole_residue_row_hits']} "
            f"identity_hits={audit['canonical_identity_hits']} "
            f"alias_hits={audit['alias_firewall_hits']}"
        ),
    )
    report(
        "finite-gram-diagnostic-support-only",
        finite_gram_support_only,
        str(audit["finite_gram_diagnostic"]),
    )
    report(
        "block123-readout-contract-still-open",
        block123_contract_still_open and prior_strict_resolver_absent,
        statuses["block123_source_higgs_lsz_readout_formula"],
    )
    report(
        "finite-schur-packet-still-support-only",
        finite_schur_packet_support_only,
        statuses["block113_complete_finite_schur_abc"],
    )
    report(
        "aggregate-closure-gates-remain-open",
        aggregate_gates_open,
        "full-positive, retained-route, and campaign proposal flags remain false",
    )
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    current_closure_satisfied = False
    result = {
        "actual_current_surface_status": (
            "bounded-support / Block124 completed 63/63 finite source-Higgs row "
            "intake; strict Block123 pole packet absent"
        ),
        "conditional_surface_status": None,
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The completed rows are finite equal-time C_ss/C_sx/C_xx taste-radial "
            "support with no pole_residue_rows, no accepted canonical O_H/action "
            "authority, and no scalar LSZ/FV/IR/contact certificate.  They cannot "
            "satisfy the Block123 source-Higgs LSZ readout contract."
        ),
        "audit_required_before_effective_retained": False,
        "bare_retained_allowed": False,
        "block124_completed_source_higgs_row_intake_passed": FAIL_COUNT == 0,
        "current_closure_satisfied": current_closure_satisfied,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "completed_row_audit": audit,
        "block123_contract_state": {
            "formula": "y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH",
            "strict_same_pole_rows_required": True,
            "strict_same_pole_rows_present": False,
            "canonical_O_H_action_authority_present": False,
            "finite_C_sx_C_xx_aliases_promoted": False,
            "contract_satisfied_now": False,
        },
        "finite_row_diagnostic_interpretation": [
            "The completed row packet is genuine production support.",
            "The finite taste-radial Gram diagnostic has small |rho_sx| and positive determinant on all current rows.",
            "That diagnostic is not a physical no-go for a future canonical O_H, because these are not pole residues and x is not certified as O_H.",
            "It does block using the current finite rows as the Block123 Res C_sH/Res C_HH packet.",
        ],
        "strict_non_claims": [
            "does not claim retained or proposed_retained y_t closure",
            "does not set kappa_s = 1",
            "does not rename finite C_sx/C_xx rows as physical C_sH/C_HH pole rows",
            "does not identify taste-radial x with canonical O_H",
            "does not use H_unit, yt_ward_identity, observed top/y_t, alpha_LM, plaquette, or u0 as proof input",
        ],
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "exact_next_action": (
            "Produce a strict same-surface row artifact with accepted canonical O_H/action "
            "authority and numeric C_ss/C_sH/C_HH pole residues, then rerun the "
            "Block123 readout/Gram/FV/IR/contact and retained-route gates.  If that "
            "cannot be supplied, pivot to genuine same-source W/Z response rows with "
            "identity/covariance/g2 authority rather than reusing finite C_sx/C_xx aliases."
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

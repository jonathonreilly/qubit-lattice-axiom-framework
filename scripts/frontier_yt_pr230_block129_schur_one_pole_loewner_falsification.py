#!/usr/bin/env python3
"""
PR #230 Block129 Schur one-pole/Loewner-Stieltjes closure attempt.

Block128 exhausts the current W/Z and source-Higgs construction paths unless a
new strict artifact appears.  This runner pivots to the Schur/Feshbach side and
tests the strongest remaining finite diagnostic: the earlier C_x|s one-pole
scout.  The completed higher-shell packet now supplies five qhat^2 levels, so a
two-point one-pole interpolation can be tested against unused levels and the
finite Stieltjes/Loewner sign conditions can be checked across the full packet.

The result is support for future targeting, not closure: the one-pole scout is
falsified by the higher-shell rows and every candidate finite Stieltjes proxy
fails necessary divided-difference signs.  Strict Schur/Feshbach pole rows,
FV/IR/contact authority, and a physical bridge remain required.
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
    / "yt_pr230_block129_schur_one_pole_loewner_falsification_2026-05-17.json"
)

PARENTS = {
    "block121_schur_finite_packet_pole_derivative_nonidentifiability": (
        "outputs/yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json"
    ),
    "block128_strict_wz_source_row_construction_attempt": (
        "outputs/yt_pr230_block128_strict_wz_source_row_construction_attempt_2026-05-17.json"
    ),
    "higher_shell_complete_packet_monotonicity": (
        "outputs/yt_pr230_schur_higher_shell_complete_packet_monotonicity_gate_2026-05-15.json"
    ),
    "schur_x_given_source_one_pole_scout": (
        "outputs/yt_pr230_schur_x_given_source_one_pole_scout_2026-05-07.json"
    ),
    "strict_kprime_pole_residue_certificate": (
        "outputs/yt_pr230_strict_kprime_pole_residue_certificate_2026-05-12.json"
    ),
    "schur_route_completion": "outputs/yt_pr230_schur_route_completion_2026-05-06.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "assumption_import_stress": "outputs/yt_pr230_assumption_import_stress_2026-05-01.json",
}

FORBIDDEN_FIREWALL = {
    "claimed_retained_or_proposed_retained": False,
    "promoted_one_pole_scout_to_physical_pole": False,
    "promoted_finite_stieltjes_proxy_to_lsz_authority": False,
    "promoted_finite_abc_rows_to_pole_rows": False,
    "treated_taste_radial_x_as_canonical_oh": False,
    "set_kappa_s_equal_one": False,
    "set_c2_equal_one": False,
    "set_z_match_equal_one": False,
    "used_hunit_matrix_element_readout": False,
    "used_yt_ward_identity": False,
    "used_y_t_bare": False,
    "used_observed_top_or_yukawa": False,
    "used_observed_wz_or_g2": False,
    "used_alpha_lm_plaquette_or_u0": False,
    "used_reduced_cold_pilots_as_production_evidence": False,
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


def finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def field_series(packet: dict[str, Any], field: str) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    levels = packet.get("level_aggregates", {})
    if not isinstance(levels, dict):
        return rows
    for key, aggregate in sorted(levels.items(), key=lambda item: float(item[0])):
        if not isinstance(aggregate, dict):
            continue
        summary = aggregate.get("summary", {})
        field_summary = summary.get(field, {}) if isinstance(summary, dict) else {}
        if not isinstance(field_summary, dict):
            continue
        mean = field_summary.get("mean")
        stdev = field_summary.get("stdev")
        count = field_summary.get("count")
        if finite(mean) and finite(stdev) and isinstance(count, int) and count > 0:
            rows.append(
                {
                    "x": float(key),
                    "mean": float(mean),
                    "stderr": float(stdev) / math.sqrt(count),
                    "count": float(count),
                }
            )
    return rows


def one_pole_fit_from_first_two(series: list[dict[str, float]]) -> dict[str, Any]:
    if len(series) < 3:
        return {"fit_valid": False, "reason": "need at least three levels"}
    x0 = series[0]["x"]
    x1 = series[1]["x"]
    y0 = series[0]["mean"]
    y1 = series[1]["mean"]
    denom = y0 - y1
    if abs(denom) <= 1.0e-15:
        return {"fit_valid": False, "reason": "first two means do not determine finite mass"}
    m_sq = (y1 * x1 - y0 * x0) / denom
    residue = y0 * (x0 + m_sq)
    residual_rows = []
    max_abs_z = 0.0
    unused_failures = 0
    for index, row in enumerate(series):
        pred = residue / (row["x"] + m_sq)
        residual = row["mean"] - pred
        stderr = row["stderr"]
        z = residual / stderr if stderr > 0 else math.inf
        if index >= 2 and abs(z) > 5.0:
            unused_failures += 1
        max_abs_z = max(max_abs_z, abs(z))
        residual_rows.append(
            {
                "x": row["x"],
                "mean": row["mean"],
                "one_pole_prediction": pred,
                "residual": residual,
                "stderr": stderr,
                "z_score": z,
                "used_in_fit": index < 2,
            }
        )
    return {
        "fit_valid": m_sq > 0.0 and residue > 0.0,
        "model": "C(x)=R/(x+m^2) fit through the zero and first-shell means",
        "m_sq": m_sq,
        "implied_pole_location_qhat_sq": -m_sq,
        "residue": residue,
        "residual_rows": residual_rows,
        "unused_level_failure_count_at_5sigma": unused_failures,
        "max_abs_z_score": max_abs_z,
        "strict_limit": (
            "This tests the prior two-point one-pole scout against higher-shell "
            "finite rows.  Passing would still be only model support; failing "
            "rejects one-pole promotion on the current packet."
        ),
    }


def loewner_stieltjes_summary(packet: dict[str, Any]) -> dict[str, Any]:
    diagnostics = packet.get("candidate_complete_monotonicity_diagnostics", {})
    if not isinstance(diagnostics, dict):
        return {"available": False}
    fields = sorted(diagnostics)
    failing = []
    surviving = []
    for field in fields:
        diag = diagnostics[field]
        if not isinstance(diag, dict):
            continue
        passed = diag.get("complete_monotone_necessary_signs_passed") is True
        entry = {
            "field": field,
            "complete_monotone_necessary_signs_passed": passed,
            "first_failed_order": diag.get("first_failed_order"),
        }
        if passed:
            surviving.append(entry)
        else:
            failing.append(entry)
    return {
        "available": True,
        "field_count": len(fields),
        "surviving_fields": surviving,
        "failing_fields": failing,
        "all_candidate_fields_fail_necessary_stieltjes_signs": len(fields) > 0 and not surviving,
        "strict_limit": (
            "The divided-difference sign test is a finite Loewner/Stieltjes "
            "necessary condition for a positive scalar spectral proxy.  Failure "
            "rejects the finite packet as strict authority; success would still "
            "need pole/FV/IR/contact and bridge authority."
        ),
    }


def main() -> int:
    print("PR #230 Block129 Schur one-pole/Loewner-Stieltjes closure attempt")
    print("=" * 78)

    parents = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in parents.items()}
    missing = [name for name, cert in parents.items() if not cert]
    proposal_parents = [name for name, cert in parents.items() if cert.get("proposal_allowed") is True]

    complete_packet = parents["higher_shell_complete_packet_monotonicity"]
    one_pole_scout = parents["schur_x_given_source_one_pole_scout"]
    strict_kprime = parents["strict_kprime_pole_residue_certificate"]
    block121 = parents["block121_schur_finite_packet_pole_derivative_nonidentifiability"]
    block128 = parents["block128_strict_wz_source_row_construction_attempt"]

    series = field_series(complete_packet, "C_x_given_source")
    one_pole_test = one_pole_fit_from_first_two(series)
    loewner = loewner_stieltjes_summary(complete_packet)

    complete_packet_available = (
        complete_packet.get("higher_shell_complete_packet_monotonicity_gate_passed") is True
        and complete_packet.get("complete_packet_chunk_count") == 63
        and complete_packet.get("expected_chunk_count") == 63
        and len(series) == 5
    )
    prior_one_pole_was_scout_only = (
        one_pole_scout.get("schur_x_given_source_one_pole_scout_passed") is True
        and one_pole_scout.get("one_pole_model_class_authority_passed") is False
        and one_pole_scout.get("physical_pole_residue_authority_present") is False
    )
    one_pole_falsified = (
        one_pole_test.get("fit_valid") is True
        and one_pole_test.get("unused_level_failure_count_at_5sigma", 0) >= 1
    )
    no_loewner_stieltjes_survivor = (
        loewner.get("all_candidate_fields_fail_necessary_stieltjes_signs") is True
        and complete_packet.get("surviving_complete_monotonicity_fields") == []
    )
    strict_kprime_rows_absent = (
        strict_kprime.get("strict_pass") is False
        and strict_kprime.get("candidate_present") is False
    )
    block121_nonidentifiability_still_load_bearing = (
        block121.get("block121_schur_finite_packet_pole_derivative_nonidentifiability_passed") is True
        and block121.get("finite_node_vanishing_witness", {}).get("kprime_changes") is True
    )
    bridge_roots_still_absent_after_block128 = (
        block128.get("constructive_status", {}).get("strict_wz_constructible_from_current_raw_rows")
        is False
        and block128.get("constructive_status", {}).get(
            "strict_source_higgs_constructible_from_current_raw_rows"
        )
        is False
    )
    retained_open = parents["retained_route"].get("proposal_allowed") is False
    full_assembly_open = parents["full_positive_assembly"].get("proposal_allowed") is False
    campaign_open = parents["campaign_status"].get("proposal_allowed") is False
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposal_parents, f"proposal_allowed={proposal_parents}")
    report("complete-higher-shell-packet-available", complete_packet_available, f"levels={len(series)} chunks={complete_packet.get('complete_packet_chunk_count')}")
    report("prior-one-pole-result-was-scout-only", prior_one_pole_was_scout_only, statuses["schur_x_given_source_one_pole_scout"])
    report("one-pole-scout-falsified-by-unused-shells", one_pole_falsified, f"max_abs_z={one_pole_test.get('max_abs_z_score')}")
    report("loewner-stieltjes-finite-proxies-have-no-survivor", no_loewner_stieltjes_survivor, f"survivors={loewner.get('surviving_fields')}")
    report("strict-kprime-pole-rows-absent", strict_kprime_rows_absent, statuses["strict_kprime_pole_residue_certificate"])
    report("finite-node-nonidentifiability-still-load-bearing", block121_nonidentifiability_still_load_bearing, statuses["block121_schur_finite_packet_pole_derivative_nonidentifiability"])
    report("wz-and-source-higgs-bridges-still-absent-after-block128", bridge_roots_still_absent_after_block128, statuses["block128_strict_wz_source_row_construction_attempt"])
    report("retained-route-still-open", retained_open, statuses["retained_route"])
    report("full-positive-assembly-still-open", full_assembly_open, statuses["full_positive_assembly"])
    report("campaign-proposal-still-open", campaign_open, statuses["campaign_status"])
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    current_closure_satisfied = False
    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block129 completed higher-shell Schur "
            "packet falsifies the prior C_x|s one-pole scout as pole authority "
            "and no finite Loewner-Stieltjes proxy survives the necessary sign "
            "tests; strict Schur/Feshbach pole rows remain absent"
        ),
        "conditional_surface_status": (
            "Schur route can reopen only with same-surface strict pole rows or "
            "a theorem-grade analytic/model-class certificate fixing K'(pole), "
            "plus FV/IR/contact authority and a canonical O_H/source-overlap, "
            "W/Z, or neutral physical bridge"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The strongest finite Schur diagnostic is now overconstrained: the "
            "two-point one-pole scout misses unused higher-shell levels, all "
            "candidate finite Stieltjes proxies fail necessary signs, and the "
            "current surface has no strict K-prime pole rows or physical bridge."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "current_closure_satisfied": current_closure_satisfied,
        "block129_schur_one_pole_loewner_falsification_passed": FAIL_COUNT == 0,
        "complete_packet_available": complete_packet_available,
        "qhat_sq_levels": [row["x"] for row in series],
        "one_pole_test_field": "C_x_given_source",
        "one_pole_test": one_pole_test,
        "loewner_stieltjes_summary": loewner,
        "strict_kprime_rows_absent": strict_kprime_rows_absent,
        "finite_node_nonidentifiability_still_load_bearing": (
            block121_nonidentifiability_still_load_bearing
        ),
        "bridge_roots_still_absent_after_block128": bridge_roots_still_absent_after_block128,
        "exact_next_action": (
            "Stop treating finite Schur/Stieltjes proxies or one-pole endpoint "
            "fits as closure candidates.  Produce a strict Schur/Feshbach row "
            "artifact carrying pole coordinate, K'(pole) or lK'r, source "
            "projection numerator, FV/IR/contact/model-class authority, and a "
            "physical bridge; otherwise pivot to neutral H3/H4 physical "
            "transfer/source-coupling authority."
        ),
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": {
            "does_not_claim_retained_or_proposed_retained": True,
            "does_not_treat_one_pole_fit_as_physical_pole": True,
            "does_not_treat_finite_loewner_stieltjes_proxy_as_lsz_authority": True,
            "does_not_promote_finite_abc_rows_to_pole_rows": True,
            "does_not_use_forbidden_imports": firewall_clean,
        },
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote certificate: {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
PR #230 Block123 source-Higgs LSZ readout formula.

This is a stretch attempt on the cleanest positive route after Blocks120-122.
It asks whether the remaining kappa_s blocker can be converted into a strict,
same-surface source-Higgs pole-row formula rather than a convention.

Result: the formula is exact support, but not current closure.  If a future
certificate supplies same-pole C_ss/C_sH/C_HH residues, canonical O_H/LSZ
normalization, Gram purity or controlled orthogonal leakage, and top/source
covariance on the same ensemble, then

    y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH

is invariant under source-coordinate rescaling and does not set kappa_s=1.
The current PR230 surface still lacks the strict source-Higgs pole rows and
canonical action/O_H authority needed to evaluate it.
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
    / "yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json"
)

PARENTS = {
    "fh_lsz_invariant_readout": "outputs/yt_fh_lsz_invariant_readout_theorem_2026-05-01.json",
    "source_functional_lsz_identifiability": "outputs/yt_source_functional_lsz_identifiability_theorem_2026-05-03.json",
    "isolated_pole_gram": "outputs/yt_isolated_pole_gram_factorization_theorem_2026-05-03.json",
    "source_higgs_pole_contract": "outputs/yt_pr230_source_higgs_pole_row_acceptance_contract_2026-05-06.json",
    "source_higgs_overlap_kappa_contract": "outputs/yt_pr230_source_higgs_overlap_kappa_contract_2026-05-06.json",
    "canonical_higgs_gate": "outputs/yt_canonical_higgs_operator_certificate_gate_2026-05-03.json",
    "source_higgs_gram_gate": "outputs/yt_source_higgs_gram_purity_gate_2026-05-02.json",
    "source_higgs_postprocess": "outputs/yt_source_higgs_gram_purity_postprocess_2026-05-03.json",
    "block120_invariant_minimal_data": "outputs/yt_pr230_block120_source_reparam_invariant_minimal_data_2026-05-17.json",
    "block122_axis_action_lsz_gap": "outputs/yt_pr230_block122_hamming_axis_action_lsz_normalization_gap_2026-05-17.json",
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


def close(a: float, b: float, tol: float = 1.0e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def formula_witness() -> dict[str, Any]:
    """
    One-pole source-Higgs LSZ algebra.

    Let z_s=<0|O_s|phi>, z_H=<0|O_H|phi>, and r=dE_top/ds.  A source
    coordinate rescaling O_s -> c O_s sends z_s -> c z_s and r -> c r.
    The canonical-Higgs response inferred from source-Higgs pole rows is

        y_H = r * z_H / (z_s z_H) = r / z_s
            = r * sqrt(Res C_HH) / Res C_sH.

    If Gram purity holds, this also equals r/sqrt(Res C_ss), up to the pole
    sign convention.  If an orthogonal neutral scalar contributes to dE/ds,
    the source-Higgs rows alone do not identify y_H; that is the required
    top-coupling/covariance premise.
    """

    base_response = 0.685
    z_source = 0.324037034920393
    z_higgs = 1.75
    rows = []
    for source_scale in (0.25, 1.0, 4.0, 9.0):
        r = source_scale * base_response
        z_s = source_scale * z_source
        res_ss = z_s * z_s
        res_sh = z_s * z_higgs
        res_hh = z_higgs * z_higgs
        y_from_csh = r * math.sqrt(res_hh) / res_sh
        y_from_css = r / math.sqrt(res_ss)
        forbidden_kappa_one = r
        rows.append(
            {
                "source_scale": source_scale,
                "dE_top_ds": r,
                "Res_C_ss": res_ss,
                "Res_C_sH": res_sh,
                "Res_C_HH": res_hh,
                "readout_from_C_sH_C_HH": y_from_csh,
                "readout_from_C_ss_if_gram_pure": y_from_css,
                "forbidden_kappa_s_equals_one_readout": forbidden_kappa_one,
                "gram_determinant": res_ss * res_hh - res_sh * res_sh,
            }
        )

    orthogonal_rows = []
    for g_orth in (-0.4, 0.0, 0.55):
        r_total = base_response + 0.8 * g_orth
        res_ss = z_source * z_source + 0.8 * 0.8
        res_sh = z_source * z_higgs
        res_hh = z_higgs * z_higgs
        naive = r_total * math.sqrt(res_hh) / res_sh
        true_higgs = base_response / z_source
        orthogonal_rows.append(
            {
                "orthogonal_source_overlap": 0.8,
                "orthogonal_top_coupling": g_orth,
                "dE_top_ds_total": r_total,
                "Res_C_ss_total": res_ss,
                "Res_C_sH": res_sh,
                "Res_C_HH": res_hh,
                "naive_readout_if_orthogonal_ignored": naive,
                "true_higgs_readout": true_higgs,
                "bias": naive - true_higgs,
            }
        )

    readouts = [row["readout_from_C_sH_C_HH"] for row in rows]
    css_readouts = [row["readout_from_C_ss_if_gram_pure"] for row in rows]
    forbidden = [row["forbidden_kappa_s_equals_one_readout"] for row in rows]
    orth_biases = [abs(row["bias"]) for row in orthogonal_rows]
    return {
        "same_pole_formula": "y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH",
        "gram_pure_formula": "if Res C_sH^2 = Res C_ss Res C_HH, y_H = (dE_top/ds) / sqrt(Res C_ss)",
        "source_rescaling_rows": rows,
        "source_rescaling_invariant": max(readouts) - min(readouts) < 1.0e-12,
        "css_formula_matches_when_gram_pure": all(
            close(readout, css_readout)
            for readout, css_readout in zip(readouts, css_readouts)
        ),
        "forbidden_kappa_one_varies": max(forbidden) - min(forbidden) > 1.0,
        "gram_determinants_zero": all(abs(row["gram_determinant"]) < 1.0e-12 for row in rows),
        "orthogonal_top_coupling_counterexample": orthogonal_rows,
        "orthogonal_counterexample_changes_readout": max(orth_biases) > 0.5,
    }


def main() -> int:
    print("PR #230 Block123 source-Higgs LSZ readout formula")
    print("=" * 78)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    witness = formula_witness()

    exact_support_parents_present = (
        certs["fh_lsz_invariant_readout"].get("proposal_allowed") is False
        and "invariant readout" in statuses["fh_lsz_invariant_readout"]
        and certs["isolated_pole_gram"].get(
            "isolated_pole_gram_factorization_theorem_passed"
        )
        is True
        and certs["source_functional_lsz_identifiability"].get("proposal_allowed")
        is False
    )
    current_rows_absent = (
        "strict rows absent" in statuses["source_higgs_pole_contract"]
        and certs["source_higgs_pole_contract"].get("proposal_allowed") is False
        and certs["source_higgs_overlap_kappa_contract"].get("proposal_allowed")
        is False
        and certs["source_higgs_postprocess"].get("candidate_present") is False
    )
    canonical_oh_absent = (
        "canonical-Higgs operator certificate absent" in statuses["canonical_higgs_gate"]
        and certs["canonical_higgs_gate"].get("candidate_valid") is False
    )
    gram_gate_open = (
        "source-Higgs Gram purity gate not passed" in statuses["source_higgs_gram_gate"]
        and certs["source_higgs_gram_gate"].get(
            "source_higgs_gram_purity_gate_passed"
        )
        is False
    )
    no_finite_axis_shortcut = (
        certs["block120_invariant_minimal_data"].get("proposal_allowed") is False
        and certs["block122_axis_action_lsz_gap"].get(
            "block122_hamming_axis_action_lsz_normalization_gap_passed"
        )
        is True
        and certs["block122_axis_action_lsz_gap"].get("proposal_allowed") is False
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and certs["completion_audit"].get("proposal_allowed") is False
        and certs["assumption_import_stress"].get("proposal_allowed") is False
    )
    formula_exact = (
        witness["source_rescaling_invariant"]
        and witness["css_formula_matches_when_gram_pure"]
        and witness["forbidden_kappa_one_varies"]
        and witness["gram_determinants_zero"]
        and witness["orthogonal_counterexample_changes_readout"]
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())
    current_closure_satisfied = (
        exact_support_parents_present
        and not current_rows_absent
        and not canonical_oh_absent
        and not gram_gate_open
        and formula_exact
        and certs["retained_route"].get("proposal_allowed") is True
        and certs["campaign_status"].get("proposal_allowed") is True
    )

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("exact-support-parents-present", exact_support_parents_present, "FH/LSZ invariant and Gram theorems loaded")
    report("source-higgs-pole-rows-currently-absent", current_rows_absent, statuses["source_higgs_pole_contract"])
    report("canonical-oh-currently-absent", canonical_oh_absent, statuses["canonical_higgs_gate"])
    report("source-higgs-gram-gate-currently-open", gram_gate_open, statuses["source_higgs_gram_gate"])
    report("finite-axis-shortcut-still-blocked", no_finite_axis_shortcut, statuses["block122_axis_action_lsz_gap"])
    report("source-higgs-lsz-formula-exact", formula_exact, str(witness))
    report("orthogonal-top-coupling-premise-necessary", witness["orthogonal_counterexample_changes_readout"], "orthogonal counterexample changes readout")
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/audit/stress deny proposal")
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))
    report("current-closure-not-satisfied", current_closure_satisfied is False, "formula is not current row evidence")

    passed = FAIL_COUNT == 0
    result = {
        "actual_current_surface_status": (
            "exact-support plus open premise / Block123 source-Higgs LSZ readout "
            "formula derived; current PR230 surface lacks strict C_ss/C_sH/C_HH "
            "pole rows and canonical O_H/action authority"
        ),
        "conditional_surface_status": (
            "If a future same-surface certificate supplies canonical O_H/LSZ "
            "authority, same-pole C_ss/C_sH/C_HH residues with Gram/FV/IR/contact "
            "control, and excludes or measures orthogonal top coupling, the "
            "invariant readout is y_H=(dE_top/ds)*sqrt(Res C_HH)/Res C_sH."
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block123 supplies a formula/support theorem only.  It does not write "
            "strict source-Higgs pole rows, adopt a same-surface EW/Higgs action, "
            "certify canonical O_H/LSZ normalization, or pass retained-route gates."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block123_source_higgs_lsz_readout_formula_passed": passed,
        "current_closure_satisfied": current_closure_satisfied,
        "formula_support": witness,
        "required_future_packet": [
            "same-surface canonical O_H/action/LSZ normalization certificate",
            "same-ensemble dE_top/ds and covariance metadata",
            "same-pole Res_C_ss, Res_C_sH, Res_C_HH rows with uncertainties",
            "Gram-purity or controlled orthogonal-leakage certificate",
            "contact subtraction, FV/IR, threshold/model-class authority",
            "retained-route and campaign gates with proposal_allowed=true before proposal wording",
        ],
        "current_missing_packet": {
            "strict_source_higgs_pole_rows_absent": current_rows_absent,
            "canonical_oh_absent": canonical_oh_absent,
            "source_higgs_gram_gate_open": gram_gate_open,
            "retained_route_proposal_allowed": certs["retained_route"].get("proposal_allowed"),
            "campaign_status_proposal_allowed": certs["campaign_status"].get("proposal_allowed"),
        },
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not set kappa_s=1 or identify source coordinate with canonical Higgs by convention",
            "does not treat Block118 axis selection or Block119 finite Dirichlet support as accepted action",
            "does not relabel C_sx/C_xx rows as physical C_sH/C_HH pole rows",
            "does not use H_unit, yt_ward_identity, observed targets, alpha_LM, plaquette, or u0",
        ],
        "exact_next_action": (
            "Use the Block123 formula as the readout contract.  The next positive "
            "artifact must either produce strict same-surface C_ss/C_sH/C_HH pole "
            "rows with canonical O_H/action/LSZ authority, or pivot to W/Z response "
            "rows with allowed absolute g2 authority and matched top-W covariance."
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

#!/usr/bin/env python3
"""
PR #230 Block114 source-Higgs strict artifact resolver.

Block113 confirmed a real finite Schur A/B/C support packet but no closure.
The top-ranked positive route remains accepted same-surface O_H/action plus
strict physical C_ss/C_sH/C_HH pole rows.  This runner resolves the current
PR head against that exact contract and distinguishes real strict rows from
contracts, interface schemas, future examples, and taste-radial aliases.
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
    / "yt_pr230_block114_source_higgs_strict_artifact_resolver_2026-05-17.json"
)

PARENTS = {
    "canonical_higgs_operator_gate": "outputs/yt_canonical_higgs_operator_certificate_gate_2026-05-03.json",
    "canonical_higgs_realization_gate": "outputs/yt_canonical_higgs_operator_realization_gate_2026-05-02.json",
    "canonical_higgs_repo_authority_audit": "outputs/yt_canonical_higgs_repo_authority_audit_2026-05-03.json",
    "canonical_higgs_semantic_firewall": "outputs/yt_canonical_higgs_operator_semantic_firewall_2026-05-04.json",
    "source_higgs_pole_acceptance_contract": "outputs/yt_pr230_source_higgs_pole_row_acceptance_contract_2026-05-06.json",
    "source_higgs_pole_assembly": "outputs/yt_source_higgs_pole_row_assembly_2026-05-12.json",
    "source_higgs_production_readiness": "outputs/yt_source_higgs_production_readiness_gate_2026-05-04.json",
    "canonical_oh_action_lsz_interface": "outputs/yt_canonical_oh_action_lsz_source_higgs_interface_2026-05-12.json",
    "same_source_ew_higgs_action_ansatz": "outputs/yt_pr230_same_source_ew_higgs_action_ansatz_gate_2026-05-06.json",
    "fms_oh_candidate_action_packet": "outputs/yt_pr230_fms_oh_candidate_action_packet_2026-05-07.json",
    "block109_closure_root_selector": "outputs/yt_pr230_block109_closure_root_frontier_selector_2026-05-17.json",
    "block110_action_descent_obstruction": "outputs/yt_pr230_block110_cl3_z3_action_descent_obstruction_2026-05-17.json",
    "block112_helmholtz_obstruction": "outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json",
    "block113_schur_abc_refresh": "outputs/yt_pr230_block113_schur_abc_complete_packet_refresh_2026-05-17.json",
    "full_positive_assembly": "outputs/yt_pr230_full_positive_closure_assembly_gate_2026-05-04.json",
    "retained_route": "outputs/yt_retained_closure_route_certificate_2026-05-01.json",
    "campaign_status": "outputs/yt_pr230_campaign_status_certificate_2026-05-01.json",
    "completion_audit": "outputs/yt_pr230_positive_closure_completion_audit_2026-05-05.json",
}

EXPECTED_STRICT_PATHS = {
    "canonical_higgs_operator_certificate": "outputs/yt_canonical_higgs_operator_certificate_2026-05-03.json",
    "pr230_source_higgs_pole_rows": "outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json",
    "legacy_source_higgs_measurement_rows": "outputs/yt_source_higgs_cross_correlator_measurement_rows_2026-05-03.json",
    "source_higgs_production_certificate": "outputs/yt_source_higgs_cross_correlator_production_certificate_2026-05-03.json",
    "accepted_same_source_ew_higgs_action": "outputs/yt_pr230_same_source_ew_higgs_action_certificate_2026-05-06.json",
    "accepted_canonical_oh": "outputs/yt_pr230_canonical_oh_certificate_2026-05-07.json",
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
    "treated_c_sx_c_xx_as_c_sh_c_hh": False,
    "treated_contract_examples_as_rows": False,
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


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def walk(obj: Any, path: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], Any]]:
    rows: list[tuple[tuple[str, ...], Any]] = [(path, obj)]
    if isinstance(obj, dict):
        for key, value in obj.items():
            rows.extend(walk(value, path + (str(key),)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            rows.extend(walk(value, path + (str(index),)))
    return rows


def strict_numeric_pole_row(row: Any) -> bool:
    if not isinstance(row, dict):
        return False
    keys = {
        "Res_C_ss",
        "Res_C_sH",
        "Res_C_HH",
        "residue_C_ss",
        "residue_C_sH",
        "residue_C_HH",
    }
    numeric = {key for key in keys if is_number(row.get(key))}
    has_cross = bool({"Res_C_sH", "residue_C_sH"} & numeric)
    has_hh = bool({"Res_C_HH", "residue_C_HH"} & numeric)
    has_ss = bool({"Res_C_ss", "residue_C_ss"} & numeric)
    has_pole_marker = any(
        key in row for key in ("pole_mass", "pole_q2", "pole_location", "q2_pole")
    )
    return has_ss and has_cross and has_hh and has_pole_marker


def scan_source_higgs_candidates() -> dict[str, Any]:
    files: list[Path] = []
    for path in (ROOT / "outputs").glob("*.json"):
        name = path.name.lower()
        if any(
            token in name
            for token in (
                "source_higgs",
                "canonical_higgs",
                "canonical_oh",
                "oh_",
                "_oh",
                "pole_row",
                "fms",
                "same_source_ew_higgs",
            )
        ):
            files.append(path)

    reference_files: list[str] = []
    numeric_row_hits: list[dict[str, Any]] = []
    future_example_hits: list[dict[str, Any]] = []
    nonempty_pole_lists: list[dict[str, Any]] = []

    for path in sorted(files):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        text = json.dumps(data, sort_keys=True)
        if any(token in text for token in ("C_sH", "C_HH", "pole_residue_rows")):
            reference_files.append(rel(path))
        for node_path, value in walk(data):
            if node_path and node_path[-1] == "pole_residue_rows" and isinstance(value, list) and value:
                nonempty_pole_lists.append({"path": rel(path), "node_path": "/".join(node_path), "count": len(value)})
                for row in value:
                    if strict_numeric_pole_row(row):
                        numeric_row_hits.append(
                            {"path": rel(path), "node_path": "/".join(node_path), "row_keys": sorted(row)}
                        )
            if (
                isinstance(value, dict)
                and value.get("canonical_higgs_operator_identity_passed") is True
                and value.get("canonical_higgs_operator_normalization_passed") is True
            ):
                # Contracts may include a future-good schema row; these are not current rows.
                future_example_hits.append({"path": rel(path), "node_path": "/".join(node_path)})

    return {
        "candidate_file_count": len(files),
        "reference_file_count": len(reference_files),
        "reference_files_sample": reference_files[:40],
        "nonempty_pole_residue_lists": nonempty_pole_lists,
        "strict_numeric_pole_row_hits": numeric_row_hits,
        "future_example_or_schema_hits": future_example_hits,
    }


def main() -> int:
    print("PR #230 Block114 source-Higgs strict artifact resolver")
    print("=" * 72)

    certs = {name: load_json(path) for name, path in PARENTS.items()}
    statuses = {name: status(cert) for name, cert in certs.items()}
    missing = [name for name, cert in certs.items() if not cert]
    proposals = [name for name, cert in certs.items() if cert.get("proposal_allowed") is True]
    strict_presence = {
        name: (ROOT / path).exists() for name, path in EXPECTED_STRICT_PATHS.items()
    }
    scan = scan_source_higgs_candidates()

    canonical_oh_absent = (
        certs["canonical_higgs_operator_gate"].get("candidate_present") is False
        and certs["canonical_higgs_operator_gate"].get("candidate_valid") is False
        and certs["canonical_higgs_realization_gate"].get(
            "canonical_higgs_operator_realization_gate_passed"
        )
        is False
        and strict_presence["canonical_higgs_operator_certificate"] is False
        and strict_presence["accepted_canonical_oh"] is False
    )
    accepted_action_absent = (
        certs["same_source_ew_higgs_action_ansatz"].get("current_surface_adoption_passed")
        is False
        and certs["fms_oh_candidate_action_packet"].get("accepted_current_surface")
        is False
        and strict_presence["accepted_same_source_ew_higgs_action"] is False
    )
    strict_source_higgs_rows_absent = (
        certs["source_higgs_pole_acceptance_contract"].get("rows_present") is False
        and certs["source_higgs_pole_acceptance_contract"].get("canonical_oh_passed")
        is False
        and certs["source_higgs_pole_assembly"].get("strict_c_ss_c_sh_c_hh_rows_exist")
        is False
        and certs["source_higgs_pole_assembly"].get("blocked_by_missing_production_pole_rows")
        is True
        and certs["source_higgs_production_readiness"].get("future_rows_present") is False
        and certs["source_higgs_production_readiness"].get("future_production_certificate_present")
        is False
        and not strict_presence["pr230_source_higgs_pole_rows"]
        and not strict_presence["legacy_source_higgs_measurement_rows"]
        and not strict_presence["source_higgs_production_certificate"]
    )
    contract_examples_not_rows = (
        certs["canonical_oh_action_lsz_interface"].get("ready_for_source_higgs_rows")
        is False
        and certs["canonical_oh_action_lsz_interface"].get("strict_rows_compatible")
        is True
        and len(scan["strict_numeric_pole_row_hits"]) == 0
    )
    completion_audit = certs["completion_audit"]
    completion_audit_open = (
        completion_audit.get("proposal_allowed") is False
        and "retained closure not achieved"
        in str(completion_audit.get("actual_current_surface_status", ""))
        and completion_audit.get("completion_audit_passed") is True
        and completion_audit.get("closure_achieved") is False
    )
    aggregate_gates_open = (
        certs["full_positive_assembly"].get("proposal_allowed") is False
        and certs["retained_route"].get("proposal_allowed") is False
        and certs["campaign_status"].get("proposal_allowed") is False
        and completion_audit_open
    )
    prior_blocks_preserve_boundary = (
        "Block109 closure-root frontier selector" in statuses["block109_closure_root_selector"]
        and "does not derive accepted EW/Higgs action" in statuses["block110_action_descent_obstruction"]
        and "lacks Helmholtz mixed-derivative rows" in statuses["block112_helmholtz_obstruction"]
        and "strict Schur/Feshbach pole authority absent" in statuses["block113_schur_abc_refresh"]
    )
    firewall_clean = all(value is False for value in FORBIDDEN_FIREWALL.values())

    report("parent-certificates-present", not missing, f"missing={missing}")
    report("no-parent-authorizes-proposal", not proposals, f"proposal_allowed={proposals}")
    report("expected-strict-artifact-paths-absent", not any(strict_presence.values()), str(strict_presence))
    report("canonical-oh-certificate-absent", canonical_oh_absent, statuses["canonical_higgs_operator_gate"])
    report("accepted-same-source-action-absent", accepted_action_absent, statuses["same_source_ew_higgs_action_ansatz"])
    report("strict-source-higgs-pole-rows-absent", strict_source_higgs_rows_absent, statuses["source_higgs_pole_assembly"])
    report("contract-examples-not-counted-as-rows", contract_examples_not_rows, str(scan))
    report("aggregate-gates-remain-open", aggregate_gates_open, "assembly/retained/campaign/completion audit deny closure")
    report("prior-block-boundaries-preserved", prior_blocks_preserve_boundary, str(statuses))
    report("forbidden-firewall-clean", firewall_clean, str(FORBIDDEN_FIREWALL))

    passed = (
        not missing
        and not proposals
        and not any(strict_presence.values())
        and canonical_oh_absent
        and accepted_action_absent
        and strict_source_higgs_rows_absent
        and contract_examples_not_rows
        and aggregate_gates_open
        and prior_blocks_preserve_boundary
        and firewall_clean
    )

    result = {
        "actual_current_surface_status": (
            "exact negative boundary / Block114 current PR230 head contains no "
            "accepted O_H/action plus strict numeric C_ss/C_sH/C_HH pole-row artifact"
        ),
        "conditional_surface_status": (
            "source-Higgs closure support only after a future same-surface artifact "
            "supplies accepted EW/Higgs action or canonical O_H, numeric production "
            "C_ss/C_sH/C_HH pole rows, Gram/FV/IR/contact authority, and aggregate "
            "proposal gates"
        ),
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Block114 is an artifact resolver and exact boundary: it finds only "
            "contracts, schemas, conditional FMS/action packets, absent expected row "
            "paths, and support-only aliases. It does not supply accepted O_H/action "
            "or strict numeric source-Higgs pole rows."
        ),
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "block114_source_higgs_strict_artifact_resolver_passed": passed,
        "canonical_oh_certificate_absent": canonical_oh_absent,
        "accepted_same_source_action_absent": accepted_action_absent,
        "strict_source_higgs_pole_rows_absent": strict_source_higgs_rows_absent,
        "contract_examples_not_counted_as_rows": contract_examples_not_rows,
        "strict_artifact_presence": strict_presence,
        "candidate_scan_summary": scan,
        "parent_certificates": PARENTS,
        "parent_statuses": statuses,
        "forbidden_firewall": FORBIDDEN_FIREWALL,
        "strict_non_claims": [
            "does not claim retained or proposed_retained top-Yukawa closure",
            "does not treat interface examples or contracts as production rows",
            "does not treat C_sx/C_xx aliases as C_sH/C_HH",
            "does not treat FMS/action ansatz as accepted current-surface action",
            "does not set kappa_s, c2, Z_match, or g2 to one",
        ],
        "exact_next_action": (
            "Create a real row artifact at outputs/yt_pr230_source_higgs_pole_rows_2026-05-06.json "
            "or an accepted canonical O_H/action certificate first; the artifact must contain "
            "numeric production C_ss/C_sH/C_HH pole residues with Gram, FV/IR, contact, "
            "and covariance authority before any source-Higgs closure gate can pass."
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

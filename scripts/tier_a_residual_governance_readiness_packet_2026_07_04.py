#!/usr/bin/env python3
"""Verifier for the Tier-A residual governance readiness packet."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TIER_A_RESIDUAL_GOVERNANCE_READINESS_PACKET_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

SOURCES = {
    "ac_full_matter": DOCS / "ACPHILAMBDA_FULL_MATTER_ACTION_STATISTICS_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "ac_first_order": DOCS / "ACPHILAMBDA_FIRST_ORDER_DETERMINANT_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md",
    "ac_dynamical_index": DOCS / "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "ac_det_power": DOCS / "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md",
    "r_eta_current": DOCS / "ACPHILAMBDA_R_ETA_CURRENT_SURFACE_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-07-04.md",
    "r_eta_direct": DOCS / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
    "r_eta_hclass": DOCS / "ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md",
    "r_eta_hunit": DOCS / "ACPHILAMBDA_R_ETA_HUNIT_APPROVED_PRIMITIVE_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
    "theta_g1_carrier": DOCS / "THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "theta_g1_defect": DOCS / "THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "theta_g2": DOCS / "THETA_G2_PHYSICAL_SECTOR_REGISTRATION_STRETCH_NO_GO_NOTE_2026-07-04.md",
    "theta_g3": DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "theta_g4": DOCS / "THETA_G4_THETA_BAR_ASSEMBLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
    "theta_mass_w2": DOCS / "THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md",
    "theta_mass_readiness": DOCS / "THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md",
    "theta_action_entry": DOCS / "THETA_MASS_ACTION_DETERMINANT_ENTRY_EXACT_SUPPORT_SPLIT_NOTE_2026-07-04.md",
}

CLAIM_IDS = {
    "ac_full_matter": "acphilambda_full_matter_action_statistics_current_surface_no_go_note_2026-07-04",
    "ac_first_order": "acphilambda_first_order_determinant_retirement_readiness_no_go_note_2026-07-04",
    "ac_dynamical_index": "acphilambda_dynamical_index_occupancy_current_surface_no_go_note_2026-07-04",
    "ac_det_power": "acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04",
    "r_eta_current": "acphilambda_r_eta_current_surface_readout_identification_no_go_note_2026-07-04",
    "r_eta_direct": "acphilambda_r_eta_direct_license_hclass_hunit_non_supply_no_go_note_2026-07-04",
    "r_eta_hclass": "acphilambda_r_eta_hclass_first_principles_stretch_no_go_note_2026-07-04",
    "r_eta_hunit": "acphilambda_r_eta_hunit_approved_primitive_non_supply_no_go_note_2026-07-04",
    "theta_g1_carrier": "theta_g1_4d_carrier_supply_current_surface_no_go_note_2026-07-04",
    "theta_g1_defect": "theta_g1_defect_closure_current_surface_no_go_note_2026-07-04",
    "theta_g2": "theta_g2_physical_sector_registration_stretch_no_go_note_2026-07-04",
    "theta_g3": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "theta_g4": "theta_g4_theta_bar_assembly_current_surface_no_go_note_2026-07-04",
    "theta_mass_w2": "theta_mass_w2_physical_registrability_stretch_no_go_note_2026-07-04",
    "theta_mass_readiness": "theta_mass_determinant_bridge_retirement_readiness_no_go_note_2026-07-04",
    "theta_action_entry": "theta_mass_action_determinant_entry_exact_support_split_note_2026-07-04",
}

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("Tier-A residual governance readiness packet verifier")
    print("=" * 88)

    paths = [NOTE, TIER_A, AXIOM_NODES, LEDGER, MINIMAL, REGISTRY, *SOURCES.values()]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimal_flat = flat(texts[MINIMAL])
    registry_flat = flat(texts[REGISTRY])
    tier = json.loads(texts[TIER_A])
    axiom_nodes = json.loads(texts[AXIOM_NODES])
    ledger = json.loads(texts[LEDGER])["rows"]

    section("A - source presence and meta boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note declares Type meta", "**Type:** meta" in note)
    check("note declares Claim type meta", "**Claim type:** meta" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    for phrase in [
        "does not retire AC_phi_lambda or theta",
        "does not edit any Tier-A registry",
        "does not adopt any governance premise",
        "retirement requires retained theorem work or explicit governance",
    ]:
        check(f"note preserves meta boundary: {phrase}", phrase in note_flat)
    for forbidden in [
        "AC_phi_lambda is retired",
        "theta is retired",
        "registry is edited",
        "premise is adopted",
        "effective_status: retained",
        "audit_status: audited_clean",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B - approved axiom and primitive allowlist")
    expected_axiom_ids = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("approved premise canonical IDs are exactly the expected four", axiom_nodes["canonical_ids"] == expected_axiom_ids, axiom_nodes["canonical_ids"])
    check("approved premise node count is four", set(axiom_nodes["nodes"]) == set(expected_axiom_ids), sorted(axiom_nodes["nodes"]))
    for forbidden_id in [
        "orbit_occupancy",
        "r_eta",
        "h_class",
        "h_unit",
        "theta_gauge",
        "theta_mass",
        "sector_readout",
        "phase_source",
        "determinant_channel",
    ]:
        check(f"approved canonical IDs do not contain {forbidden_id}", all(forbidden_id not in cid for cid in axiom_nodes["canonical_ids"]))
    for phrase in [
        "Records form",
        "formation rule",
        "readout-context selection",
        "physical observable bridge",
        "source/action",
    ]:
        check(f"minimal axiom note keeps boundary: {phrase}", phrase in minimal_flat)

    section("C - Tier-A registry state")
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "Tier-A canonical IDs remain AC and theta",
        tier["canonical_ids"]
        == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("AC label is AC_phi_lambda", ac["label"] == "AC_phi_lambda", ac["label"])
    check("theta label is theta", theta["label"] == "theta", theta["label"])
    check(
        "AC minimum decomposition remains the two live atoms",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check(
        "theta minimum decomposition remains the two live atoms",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "per-lane",
        "registered realized-state data",
        "measure-side/dynamical realization binary",
        "density-read-as-angle",
        "gauge side",
        "mass side",
    ]:
        check(f"human registry contains residual wording: {phrase[:52]}", phrase in registry_flat)

    section("D - residual source rows are support/no-go, not retirement")
    no_go_expected = {
        "ac_full_matter",
        "ac_first_order",
        "ac_dynamical_index",
        "r_eta_current",
        "r_eta_direct",
        "r_eta_hclass",
        "r_eta_hunit",
        "theta_g1_carrier",
        "theta_g1_defect",
        "theta_g2",
        "theta_g3",
        "theta_g4",
        "theta_mass_w2",
        "theta_mass_readiness",
    }
    bounded_support_expected = {"ac_det_power", "theta_action_entry"}
    for label, claim_id in CLAIM_IDS.items():
        row = ledger.get(claim_id)
        check(f"ledger row resolves for {label}", row is not None)
        if not row:
            continue
        check(f"{label} remains unaudited effective status", row.get("effective_status") == "unaudited", row.get("effective_status"))
        if label in no_go_expected:
            check(f"{label} is claim_type no_go", row.get("claim_type") == "no_go", row.get("claim_type"))
        if label in bounded_support_expected:
            check(f"{label} is bounded support/theorem type", row.get("claim_type") == "bounded_theorem", row.get("claim_type"))

    source_blob = " ".join(flat(texts[path]) for path in SOURCES.values())
    for phrase in [
        "does not select",
        "not retired",
        "not a derivation",
        "future theorem",
        "owner governance",
        "physical readout",
        "physical sector/readout",
        "W2 physical registrability",
        "matter-action/statistics",
    ]:
        check(f"source packet exposes non-retirement phrase: {phrase}", phrase in source_blob)

    section("E - note readiness table and attack plan")
    for residual in [
        "AC(i) matter-action occupancy grain",
        "AC(ii) R-eta readout license",
        "theta gauge-side winding account",
        "theta mass-side determinant bridge",
    ]:
        check(f"readiness table names residual: {residual}", residual in note)
    for governance_candidate in [
        "orbit-occupancy",
        "h-class/h-unit",
        "gauge-sector/readout",
        "determinant-channel/W2",
    ]:
        check(f"governance candidate named: {governance_candidate}", governance_candidate in note)
    for attack_item in [
        "Theorem-first attempts",
        "Audit support before registry edits",
        "Prepare exact governance candidates",
        "Keep unavoidable primitives separate",
    ]:
        check(f"attack plan contains: {attack_item}", attack_item in note)

    print("\n" + "=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

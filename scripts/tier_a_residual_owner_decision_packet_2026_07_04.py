#!/usr/bin/env python3
"""Verifier for the Tier-A residual owner decision packet."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md"
READINESS = DOCS / "TIER_A_RESIDUAL_GOVERNANCE_READINESS_PACKET_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
DOC_AUTHORITY = DOCS / "audit" / "data" / "doc_authority_registry.json"
MINIMALITY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"

EXPECTED_AXIOM_IDS = [
    "minimal_axioms",
    "scale_reference_primitive",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
]

EXPECTED_TIER_A_IDS = [
    "staggered_dirac_realization_gate_note_2026-05-03",
    "strong_cp_theta_zero_note",
]

CANDIDATES = {
    "ac_orbit_occupancy_statistical_grain_premise": {
        "residual": "reading_occupancy_selection",
        "target": "AC_phi_lambda",
        "must_contain": [
            "K/CPT orbit or holomorphic-pair occupancy grain",
            "once per K/CPT orbit rather than once per sector or channel",
            "no value of `r`, `delta`, a charged-lepton mass",
        ],
    },
    "ac_reta_hclass_hunit_readout_premise": {
        "residual": "delta_readout_identification_R_eta",
        "target": "AC_phi_lambda",
        "must_contain": [
            "fixed-locus density class h",
            "identity-read in h-units as the eta angle",
            "No additional clock-rate, transport, or normalization factor",
        ],
    },
    "theta_gauge_sector_phase_source_premise": {
        "residual": "gauge_side_winding_account",
        "target": "theta",
        "must_contain": [
            "closed non-exact sector/readout surface",
            "central-sector character",
            "No independent multi-plaquette or large-gauge winding input",
        ],
    },
    "theta_mass_determinant_channel_w2_premise": {
        "residual": "mass_side_orientation_determinant_readout_bridge",
        "target": "theta",
        "must_contain": [
            "W2-registrable K-real determinant channel",
            "arg det(M_q) enters theta_bar",
            "No additional mass-surface selector or determinant-readout bridge",
        ],
    },
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
    print("Tier-A residual owner decision packet verifier")
    print("=" * 88)

    paths = [NOTE, READINESS, TIER_A, AXIOM_NODES, DOC_AUTHORITY, MINIMALITY]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    readiness_flat = flat(texts[READINESS])
    tier = json.loads(texts[TIER_A])
    axiom_nodes = json.loads(texts[AXIOM_NODES])
    doc_authority = json.loads(texts[DOC_AUTHORITY])
    minimality_flat = flat(texts[MINIMALITY])

    section("A - source presence and proposal boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note declares Type meta", "**Type:** meta" in note)
    check("note declares Claim type meta", "**Claim type:** meta" in note)
    check("note declares Class D proposal", "Class D proposal" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    for phrase in [
        "no premise weight until an owner channel explicitly consumes",
        "does not retire AC_phi_lambda or theta",
        "does not edit any Tier-A registry",
        "does not adopt any governance premise",
        "No registry deletion should occur from this packet alone",
    ]:
        check(f"proposal firewall present: {phrase}", phrase in note_flat)
    for forbidden in [
        "This document has premise weight",
        "has full premise weight",
        "is adopted by this packet",
        "AC_phi_lambda is retired",
        "theta is retired",
        "genuine_admitted_input_count` becomes `0` now",
        "effective_status: retained",
        "audit_status: audited_clean",
    ]:
        check(f"forbidden adoption overclaim absent: {forbidden}", forbidden not in note_flat)

    section("B - current registry state is unchanged")
    check("approved premise IDs remain exactly four", axiom_nodes["canonical_ids"] == EXPECTED_AXIOM_IDS, axiom_nodes["canonical_ids"])
    check("approved premise node keys remain exactly four", sorted(axiom_nodes["nodes"]) == sorted(EXPECTED_AXIOM_IDS), sorted(axiom_nodes["nodes"]))
    check("Tier-A canonical IDs remain AC and theta", tier["canonical_ids"] == EXPECTED_TIER_A_IDS, tier["canonical_ids"])
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2, tier["genuine_admitted_input_count"])
    check("Tier-A derivation target count remains two", sorted(tier["derivation_targets"]) == sorted(EXPECTED_TIER_A_IDS), sorted(tier["derivation_targets"]))
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("AC minimum decomposition unchanged", ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"], ac["minimum_decomposition"])
    check("theta minimum decomposition unchanged", theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"], theta["minimum_decomposition"])
    for candidate_id in CANDIDATES:
        check(f"candidate not in approved premise IDs: {candidate_id}", candidate_id not in axiom_nodes["canonical_ids"])
        check(f"candidate not a Tier-A derivation target: {candidate_id}", candidate_id not in tier["derivation_targets"])

    section("C - decision candidates are exact and scoped")
    for candidate_id, spec in CANDIDATES.items():
        check(f"candidate id appears: {candidate_id}", candidate_id in note)
        check(f"{candidate_id} names target {spec['target']}", spec["target"] in note)
        check(f"{candidate_id} names residual {spec['residual']}", spec["residual"] in note)
        for phrase in spec["must_contain"]:
            check(f"{candidate_id} contains scope phrase: {phrase[:58]}", phrase in note_flat)
    for phrase in [
        "Each candidate is independently selectable",
        "Adopting one candidate would not adopt the others",
        "no candidate should be broadened by title or summary",
        "AC_phi_lambda retires only if Candidate 1",
        "theta retires only if Candidate 3",
    ]:
        check(f"candidate compositional guardrail present: {phrase}", phrase in note_flat)

    section("D - policy and readiness cross-checks")
    for phrase in [
        "explicit owner approval",
        "Approval must be recorded in this policy and in the relevant machine registry",
        "Tier-A minimum-statement refinement",
        "selector for dimensionless physics content",
    ]:
        check(f"minimality policy contains required governance phrase: {phrase}", phrase in minimality_flat)
    for phrase in [
        "No approved primitive currently absorbs those four atoms",
        "Treating them as primitive content without an explicit owner-governance record",
        "Prepare exact governance candidates",
    ]:
        check(f"readiness packet justifies Block49: {phrase}", phrase in readiness_flat)
    rows = doc_authority["rows"]
    registry_rows = [
        row
        for row in rows
        if row.get("path") == "docs/TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md"
    ]
    check("document-authority registry has exactly one row for packet", len(registry_rows) == 1, registry_rows)
    if registry_rows:
        row = registry_rows[0]
        check("document-authority row is Class D", row.get("class") == "D", row)
        check("document-authority row status is landed", row.get("status") == "landed", row)
        check("document-authority row note preserves no-weight boundary", "No premise weight" in row.get("note", ""), row.get("note", ""))

    section("E - later adoption checklist remains non-executable")
    for phrase in [
        "The later adoption PR, if explicitly approved",
        "record the owner approval",
        "`genuine_admitted_input_count` becomes `0`",
        "This sketch is not executable authority",
    ]:
        check(f"later-only registry sketch phrase present: {phrase}", phrase in note_flat)

    print("\n" + "=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

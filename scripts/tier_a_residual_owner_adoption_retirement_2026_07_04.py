#!/usr/bin/env python3
"""Verifier for Tier-A residual owner adoption and retirement."""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md"
DECISION = DOCS / "TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
OWNER_NODES = DOCS / "audit" / "data" / "owner_governed_premise_nodes.json"
MINIMALITY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"
DOC_POLICY = DOCS / "audit" / "DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md"
HUMAN_REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
PREMISE_NODES = DOCS / "audit" / "scripts" / "premise_nodes.py"

EXPECTED_AXIOM_IDS = [
    "minimal_axioms",
    "scale_reference_primitive",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
]

FORMER_TIER_A_IDS = [
    "staggered_dirac_realization_gate_note_2026-05-03",
    "strong_cp_theta_zero_note",
]

EXPECTED_CANDIDATES = {
    "staggered_dirac_realization_gate_note_2026-05-03": [
        "ac_orbit_occupancy_statistical_grain_premise",
        "ac_reta_hclass_hunit_readout_premise",
    ],
    "strong_cp_theta_zero_note": [
        "theta_gauge_sector_phase_source_premise",
        "theta_mass_determinant_channel_w2_premise",
    ],
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


def load_premise_nodes_module():
    spec = importlib.util.spec_from_file_location("premise_nodes_for_block50", PREMISE_NODES)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load premise_nodes.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module._reset_cache_for_tests()
    return module


def main() -> int:
    print("Tier-A residual owner adoption and retirement verifier")
    print("=" * 88)

    paths = [
        NOTE,
        DECISION,
        TIER_A,
        AXIOM_NODES,
        OWNER_NODES,
        MINIMALITY,
        DOC_POLICY,
        HUMAN_REGISTRY,
        PREMISE_NODES,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    decision_flat = flat(texts[DECISION])
    minimality_flat = flat(texts[MINIMALITY])
    policy_flat = flat(texts[DOC_POLICY])
    human_flat = flat(texts[HUMAN_REGISTRY])
    tier = json.loads(texts[TIER_A])
    axiom_nodes = json.loads(texts[AXIOM_NODES])
    owner_nodes = json.loads(texts[OWNER_NODES])
    premise_nodes = load_premise_nodes_module()

    section("A - source presence and explicit adoption boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note declares Type meta", "**Type:** meta" in note)
    check("note declares Claim type meta", "**Claim type:** meta" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    for phrase in [
        "explicit owner adoption of the four exact Block49 residual candidates",
        "not as axioms and not as approved framework primitives",
        "does not derive AC_phi_lambda or theta as theorems",
        "does not add or amend an axiom",
        "does not add an approved framework primitive",
    ]:
        check(f"adoption firewall phrase present: {phrase}", phrase in note_flat)

    section("B - Tier-A registry is zeroed and historical data preserved")
    check("Tier-A genuine admitted input count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("Tier-A canonical_ids is empty", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("Tier-A derivation_targets is empty", tier["derivation_targets"] == {}, tier["derivation_targets"])
    retired = tier.get("retired_derivation_targets") or {}
    check("retired_derivation_targets preserves both former ids", sorted(retired) == sorted(FORMER_TIER_A_IDS), sorted(retired))
    for cid in FORMER_TIER_A_IDS:
        check(f"{cid} no longer live Tier-A", cid not in tier["derivation_targets"])
        check(f"{cid} historical retired entry has no_go_portfolio", bool(retired[cid].get("no_go_portfolio")))

    section("C - owner-governed registry is separate from axioms/primitives")
    check("approved axiom/primitive allowlist unchanged", axiom_nodes["canonical_ids"] == EXPECTED_AXIOM_IDS, axiom_nodes["canonical_ids"])
    check("owner-governed canonical ids are former Tier-A ids", owner_nodes["canonical_ids"] == FORMER_TIER_A_IDS, owner_nodes["canonical_ids"])
    check("owner-governed node keys match canonical ids", sorted(owner_nodes["nodes"]) == sorted(FORMER_TIER_A_IDS), sorted(owner_nodes["nodes"]))
    check("no overlap with axiom/primitive ids", not (set(owner_nodes["canonical_ids"]) & set(axiom_nodes["canonical_ids"])))
    for cid, expected in EXPECTED_CANDIDATES.items():
        node = owner_nodes["nodes"][cid]
        check(f"{cid} current_path points to adoption note", node.get("current_path") == "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md", node.get("current_path"))
        check(f"{cid} adopted candidates exact", node.get("adopted_residual_candidates") == expected, node.get("adopted_residual_candidates"))
        check(f"{cid} boundary present", bool(node.get("boundary")))
        for candidate in expected:
            check(f"{cid} candidate appears in note: {candidate}", candidate in note)
            check(f"{cid} candidate appears in decision packet: {candidate}", candidate in decision_flat)

    section("D - accepted-premise policy recognizes the new class")
    check("premise_nodes sees owner-governed ids", premise_nodes.owner_governed_premise_ids() == set(FORMER_TIER_A_IDS), premise_nodes.owner_governed_premise_ids())
    for cid in FORMER_TIER_A_IDS:
        check(f"{cid} accepted premise", premise_nodes.is_accepted_premise_dep(cid))
        check(f"{cid} owner-governed premise", premise_nodes.is_owner_governed_premise(cid))
        check(f"{cid} not live Tier-A admission", not premise_nodes.is_admitted_derivation_target(cid))
    for candidate in {c for values in EXPECTED_CANDIDATES.values() for c in values}:
        check(f"candidate id itself is not accepted premise: {candidate}", not premise_nodes.is_accepted_premise_dep(candidate))

    section("E - policy and human registry surfaces are updated")
    for phrase in [
        "owner-governed residual premises",
        "Tier-A residual owner adoption and registry retirement",
        "genuine admitted-target count is zero",
    ]:
        check(f"minimality policy records: {phrase}", phrase in minimality_flat)
    check("document policy names owner-governed residual premises", "owner-governed residual premises" in policy_flat)
    for phrase in [
        "Current live Tier-A admitted derivation targets: zero",
        "owner-governed residual premises",
        "retired_derivation_targets",
    ]:
        check(f"human Tier-A registry records: {phrase}", phrase in human_flat)

    section("F - overclaim guardrails")
    for forbidden in [
        "AC_phi_lambda is theorem-derived",
        "theta is theorem-derived",
        "added to axiom_premise_nodes",
        "approved framework primitive for theta",
        "approved framework primitive for AC_phi_lambda",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note_flat)
    for phrase in [
        "No axiom is added or amended",
        "No approved framework primitive is added or amended",
        "The source-side theorem/no-go packets retain their own audit statuses",
    ]:
        check(f"firewall present: {phrase}", phrase in note_flat)

    print("\n" + "=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

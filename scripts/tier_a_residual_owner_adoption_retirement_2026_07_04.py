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
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
OWNER_NODES = DOCS / "audit" / "data" / "owner_governed_premise_nodes.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
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
AC_ID = "staggered_dirac_realization_gate_note_2026-05-03"
THETA_ID = "strong_cp_theta_zero_note"
AC_CANDIDATES = [
    "ac_orbit_occupancy_statistical_grain_premise",
    "ac_reta_hclass_hunit_readout_premise",
]
THETA_CONTEXT_CANDIDATES = [
    "theta_gauge_sector_phase_source_premise",
    "theta_mass_determinant_channel_w2_premise",
]
AC_BOUNDARY = (
    "Retires only the current minimum AC_phi_lambda Tier-A atoms: AC(i) "
    "matter-action occupancy grain and AC(ii) R-eta h-class/h-unit readout "
    "license. It supplies no value of r, delta, charged-lepton mass, mixing "
    "angle, probability rule, above-C3 taste/Dirac/chirality content, CKM/PMNS "
    "alignment, or sector-weight law."
)

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
        TIER_A,
        AXIOM_NODES,
        OWNER_NODES,
        LEDGER,
        MINIMALITY,
        DOC_POLICY,
        HUMAN_REGISTRY,
        PREMISE_NODES,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimality_flat = flat(texts[MINIMALITY])
    minimality_lower = minimality_flat.lower()
    policy_flat = flat(texts[DOC_POLICY])
    human_flat = flat(texts[HUMAN_REGISTRY])
    tier = json.loads(texts[TIER_A])
    axiom_nodes = json.loads(texts[AXIOM_NODES])
    owner_nodes = json.loads(texts[OWNER_NODES])
    ledger = json.loads(texts[LEDGER])
    premise_nodes = load_premise_nodes_module()

    section("A - source presence and explicit adoption boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note declares Type meta", "**Type:** meta" in note)
    check("note declares Claim type meta", "**Claim type:** meta" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    for phrase in [
        "does not derive `AC_phi_lambda` or theta as theorems",
        "does not add or amend an axiom",
        "does not add an approved framework primitive",
        "does not set any audit verdict",
        "retiring live Tier-A admissions without treating them as axioms, primitives, or audit-ratified theorem closures",
    ]:
        check(f"adoption firewall phrase present: {phrase}", phrase in note_flat)

    section("B - Tier-A registry is zeroed and historical data preserved")
    check("Tier-A genuine admitted input count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("Tier-A canonical_ids is empty", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("Tier-A derivation_targets is empty", tier["derivation_targets"] == {}, tier["derivation_targets"])
    retired = tier.get("retired_derivation_targets") or {}
    check("retired_derivation_targets preserves AC and theta", sorted(retired) == sorted([AC_ID, THETA_ID]), sorted(retired))
    for cid in (AC_ID, THETA_ID):
        check(f"{cid} no longer live Tier-A", cid not in tier["derivation_targets"])
        check(f"{cid} historical retired entry has no_go_portfolio", bool(retired[cid].get("no_go_portfolio")))

    ac_retirement = retired[AC_ID].get("retirement") or {}
    theta_retirement = retired[THETA_ID].get("retirement") or {}
    check("AC retirement mechanism is owner-governance on audited surface", ac_retirement.get("mechanism") == "retired_by_owner_governance_on_audited_surface", ac_retirement)
    check("AC retirement records audited surface", "audited_clean / retained_bounded" in str(ac_retirement.get("audited_surface")), ac_retirement.get("audited_surface"))
    check("AC adopted candidates exact", ac_retirement.get("adopted_residual_candidates") == AC_CANDIDATES, ac_retirement.get("adopted_residual_candidates"))
    check("AC boundary exact in retired record", ac_retirement.get("boundary") == AC_BOUNDARY, ac_retirement.get("boundary"))
    check("theta remains retained-derivation retired", theta_retirement.get("mechanism") == "retired_by_retained_derivation", theta_retirement.get("mechanism"))

    section("C - owner-governed registry is separate from axioms/primitives")
    check("approved axiom/primitive allowlist unchanged", axiom_nodes["canonical_ids"] == EXPECTED_AXIOM_IDS, axiom_nodes["canonical_ids"])
    check("owner-governed canonical ids are AC only", owner_nodes["canonical_ids"] == [AC_ID], owner_nodes["canonical_ids"])
    check("owner-governed node keys match canonical ids", sorted(owner_nodes["nodes"]) == [AC_ID], sorted(owner_nodes["nodes"]))
    check("theta is not owner-governed", THETA_ID not in owner_nodes["nodes"], sorted(owner_nodes["nodes"]))
    check("no overlap with axiom/primitive ids", not (set(owner_nodes["canonical_ids"]) & set(axiom_nodes["canonical_ids"])))
    node = owner_nodes["nodes"][AC_ID]
    check("AC current_path points to adoption note", node.get("current_path") == "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md", node.get("current_path"))
    check("AC prior source path points to audited gate note", node.get("prior_tier_a_source_path") == "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md", node.get("prior_tier_a_source_path"))
    check("AC owner-governed candidates exact", node.get("adopted_residual_candidates") == AC_CANDIDATES, node.get("adopted_residual_candidates"))
    check("AC owner-governed boundary exact", node.get("boundary") == AC_BOUNDARY, node.get("boundary"))
    check("AC node records audited surface", "5d8df21fe" in str(node.get("retirement_surface")), node.get("retirement_surface"))

    section("D - accepted-premise policy recognizes only the current live owner-governed class")
    check("premise_nodes sees AC owner-governed id", premise_nodes.owner_governed_premise_ids() == {AC_ID}, premise_nodes.owner_governed_premise_ids())
    check("AC accepted premise", premise_nodes.is_accepted_premise_dep(AC_ID))
    check("AC owner-governed premise", premise_nodes.is_owner_governed_premise(AC_ID))
    check("AC not live Tier-A admission", not premise_nodes.is_admitted_derivation_target(AC_ID))
    check("theta not owner-governed premise", not premise_nodes.is_owner_governed_premise(THETA_ID))
    check("theta not live Tier-A admission", not premise_nodes.is_admitted_derivation_target(THETA_ID))
    for candidate in AC_CANDIDATES + THETA_CONTEXT_CANDIDATES:
        check(f"candidate id itself is not accepted premise: {candidate}", not premise_nodes.is_accepted_premise_dep(candidate))

    section("E - ledger, policy, and human registry surfaces are updated")
    rows = ledger.get("rows") or {}
    ac_row = rows.get(AC_ID) or {}
    theta_row = rows.get(THETA_ID) or {}
    ac_adoption_grade_recorded = any(
        audit.get("claim_type") == "bounded_theorem"
        and audit.get("audit_status") == "audited_clean"
        for audit in (ac_row.get("previous_audits") or [])
    )
    check(
        "AC adoption-time audited bounded surface is preserved in ledger history",
        ac_adoption_grade_recorded and ac_row.get("claim_type") == "bounded_theorem",
        (ac_row.get("claim_type"), ac_row.get("audit_status"), ac_row.get("effective_status")),
    )
    check("theta source row is audited retained-bounded", (theta_row.get("claim_type"), theta_row.get("audit_status"), theta_row.get("effective_status")) == ("bounded_theorem", "audited_clean", "retained_bounded"), theta_row)
    for phrase in [
        "owner-governed residual premises",
        "AC_phi_lambda retired from live Tier-A by owner-governance",
        "genuine_admitted_input_count",
    ]:
        haystack = minimality_lower if phrase == "owner-governed residual premises" else minimality_flat
        needle = phrase.lower() if phrase == "owner-governed residual premises" else phrase
        check(f"minimality policy records: {phrase}", needle in haystack)
    check("document policy names owner-governed residual premises", "owner-governed residual premises" in policy_flat)
    for phrase in [
        "Current live Tier-A admitted derivation targets: zero",
        "owner-governed residual premises",
        "retired_derivation_targets",
        "5d8df21fe",
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

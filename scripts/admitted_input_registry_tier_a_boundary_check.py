#!/usr/bin/env python3
"""Boundary runner for the Tier-A admitted-input registry note.

This runner checks source/registry alignment for the human Tier-A index and
machine `tier_a_admissions.json`. It does not audit, retire, add, remove, or
re-grade any admitted input.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
OWNER_GOVERNED = ROOT / "docs" / "audit" / "data" / "owner_governed_premise_nodes.json"
AXIOM_PREMISES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
RUNNER = "scripts/admitted_input_registry_tier_a_boundary_check.py"
CACHE = "logs/runner-cache/admitted_input_registry_tier_a_boundary_check.txt"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}

AC_ID = "staggered_dirac_realization_gate_note_2026-05-03"
THETA_ID = "strong_cp_theta_zero_note"
CONVENTION_IDS = {
    "hypercharge_identification_note": "Y0",
    "g_bare_rigidity_theorem_note": "g0",
}
RECLASSIFIED_PRIMITIVES = {
    "minimal_axioms_record": "Record axiom",
    "scale_reference_primitive": "scale-reference primitive",
}
AC_CANDIDATES = [
    "ac_orbit_occupancy_statistical_grain_premise",
    "ac_reta_hclass_hunit_readout_premise",
]
AC_BOUNDARY = (
    "Retires only the current minimum AC_phi_lambda Tier-A atoms: AC(i) "
    "matter-action occupancy grain and AC(ii) R-eta h-class/h-unit readout "
    "license. It supplies no value of r, delta, charged-lepton mass, mixing "
    "angle, probability rule, above-C3 taste/Dirac/chirality content, CKM/PMNS "
    "alignment, or sector-weight law."
)

PASS_COUNT = 0
FAIL_COUNT = 0


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return ok


def row_status(rows: dict, cid: str) -> tuple[str | None, str | None, str | None]:
    row = rows.get(cid) or {}
    return row.get("claim_type"), row.get("audit_status"), row.get("effective_status")


def main() -> int:
    print("=" * 78)
    print("TIER-A ADMITTED-INPUT REGISTRY BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: source/registry alignment only; no audit verdict changes.")
    print()

    note = read(NOTE)
    note_lower = normalize(note).lower()
    tier = load_json(TIER_A)
    owner = load_json(OWNER_GOVERNED)
    axiom_premises = load_json(AXIOM_PREMISES)
    ledger = load_json(LEDGER)
    conventions = tier.get("conventions") or {}
    reclassified = tier.get("reclassified_primitives") or {}
    retired_targets = tier.get("retired_derivation_targets") or {}
    owner_nodes = owner.get("nodes") or {}
    axiom_ids = set(axiom_premises.get("canonical_ids") or [])
    ledger_rows = ledger.get("rows") or {}

    check("source note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("machine Tier-A registry exists", TIER_A.exists(), TIER_A.relative_to(ROOT).as_posix())
    check("owner-governed registry exists", OWNER_GOVERNED.exists(), OWNER_GOVERNED.relative_to(ROOT).as_posix())
    check("axiom premise registry exists", AXIOM_PREMISES.exists(), AXIOM_PREMISES.relative_to(ROOT).as_posix())
    check("audit ledger exists", LEDGER.exists(), LEDGER.relative_to(ROOT).as_posix())
    check("source claim type is meta", "**Claim type:** meta" in note)
    check("source status authority is audit lane only", "independent audit lane only" in note)
    check("source says it sets no audit status", "sets **no** audit status" in note)
    check("source registers this primary runner", RUNNER in note)
    check("source registers this cached output", CACHE in note)

    check("machine schema version is 1", tier.get("schema_version") == 1, str(tier.get("schema_version")))
    check("genuine admitted input count is zero", tier.get("genuine_admitted_input_count") == 0, str(tier.get("genuine_admitted_input_count")))
    check("canonical ids are empty", tier.get("canonical_ids") == [], str(tier.get("canonical_ids")))
    check("derivation targets are empty", tier.get("derivation_targets") == {}, str(tier.get("derivation_targets")))
    check("retired target keys are AC and theta", set(retired_targets) == {AC_ID, THETA_ID}, str(sorted(retired_targets)))

    ac_retired = retired_targets.get(AC_ID, {})
    theta_retired = retired_targets.get(THETA_ID, {})
    check("AC retired row exists", bool(ac_retired), AC_ID)
    check("AC retired label matches", ac_retired.get("label") == "AC_phi_lambda", str(ac_retired.get("label")))
    check("AC no-go portfolio preserved", bool(ac_retired.get("no_go_portfolio")), str(ac_retired.get("no_go_portfolio")))
    check("AC historical minimum decomposition preserved", bool(ac_retired.get("minimum_decomposition")), str(ac_retired.get("minimum_decomposition")))
    ac_retirement = ac_retired.get("retirement") or {}
    check("AC retirement record present", bool(ac_retirement), "")
    check(
        "AC retirement mechanism is owner governance on audited surface",
        ac_retirement.get("mechanism") == "retired_by_owner_governance_on_audited_surface",
        str(ac_retirement.get("mechanism")),
    )
    check("AC retirement records owner-governed premise node", ac_retirement.get("owner_governed_premise_node") == AC_ID, str(ac_retirement.get("owner_governed_premise_node")))
    check("AC retirement records audited surface", "audited_clean / retained_bounded" in str(ac_retirement.get("audited_surface")), str(ac_retirement.get("audited_surface")))
    check("AC retirement candidates exact", ac_retirement.get("adopted_residual_candidates") == AC_CANDIDATES, str(ac_retirement.get("adopted_residual_candidates")))
    check("AC retirement boundary exact", ac_retirement.get("boundary") == AC_BOUNDARY, str(ac_retirement.get("boundary")))

    check("theta retired row exists", bool(theta_retired), THETA_ID)
    theta_retirement = theta_retired.get("retirement") or {}
    check("theta retirement mechanism is retained derivation", theta_retirement.get("mechanism") == "retired_by_retained_derivation", str(theta_retirement.get("mechanism")))
    check("theta no-go portfolio preserved", bool(theta_retired.get("no_go_portfolio")), str(theta_retired.get("no_go_portfolio")))
    check("theta not in owner-governed registry", THETA_ID not in owner_nodes, str(sorted(owner_nodes)))

    check("owner-governed schema version is 1", owner.get("schema_version") == 1, str(owner.get("schema_version")))
    check("owner-governed canonical ids are AC only", owner.get("canonical_ids") == [AC_ID], str(owner.get("canonical_ids")))
    check("owner-governed node keys match canonical ids", set(owner_nodes) == {AC_ID}, str(sorted(owner_nodes)))
    ac_owner = owner_nodes.get(AC_ID, {})
    check("owner-governed AC label matches", ac_owner.get("label") == "AC_phi_lambda", str(ac_owner.get("label")))
    check("owner-governed AC current path points to adoption note", ac_owner.get("current_path") == "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md", str(ac_owner.get("current_path")))
    check("owner-governed AC candidates exact", ac_owner.get("adopted_residual_candidates") == AC_CANDIDATES, str(ac_owner.get("adopted_residual_candidates")))
    check("owner-governed AC boundary exact", ac_owner.get("boundary") == AC_BOUNDARY, str(ac_owner.get("boundary")))
    check("owner-governed registry disjoint from axiom premises", not ({AC_ID} & axiom_ids), str(sorted({AC_ID} & axiom_ids)))

    check("Record lives in axiom-premise registry", "minimal_axioms" in axiom_ids, str(sorted(axiom_ids)))
    check("Scale reference lives in axiom-premise registry", "scale_reference_primitive" in axiom_ids, str(sorted(axiom_ids)))
    check("convention rows are present", set(CONVENTION_IDS).issubset(conventions), str(sorted(conventions)))
    check("reclassified primitives are present", set(RECLASSIFIED_PRIMITIVES).issubset(reclassified), str(sorted(reclassified)))

    ac_status = row_status(ledger_rows, AC_ID)
    theta_status = row_status(ledger_rows, THETA_ID)
    ac_previous_audits = ledger_rows.get(AC_ID, {}).get("previous_audits") or []
    ac_adoption_grade_recorded = any(
        audit.get("claim_type") == "bounded_theorem"
        and audit.get("audit_status") == "audited_clean"
        for audit in ac_previous_audits
    )
    check(
        "AC adoption-time audited bounded surface is preserved in ledger history",
        ac_adoption_grade_recorded and ac_status[0] == "bounded_theorem",
        str(ac_status),
    )
    check("theta source row remains audited retained-bounded bounded theorem", theta_status == ("bounded_theorem", "audited_clean", "retained_bounded"), str(theta_status))

    check("note states zero live Tier-A targets", "Current live Tier-A admitted derivation targets: zero" in note)
    check("note states theta retained-derivation retirement", "theta was retired from tier a on 2026-07-05 by retained derivation" in note_lower)
    check("note states AC owner-governance retirement", "AC_φλ was retired from live Tier A by owner-governance adoption" in note)
    check("note states historical audited AC surface", "audited-clean / retained-bounded gate surface at adoption commit" in note and "5d8df21fe" in note)
    check("note delegates current AC status to ledger", "Current effective status is always read from the ledger" in note)
    check("note names owner-governed registry", "owner_governed_premise_nodes.json" in note)
    check("note says no hand-maintained backlinks", "No back-links are maintained by hand" in note)
    check("note says audit status remains audit-lane-only", "audit status remains audit-lane-only" in note)

    forbidden_positive_phrases = (
        "sets audit status",
        "promotes rows to retained",
        "changes rows' effective_status",
        "Tier-A derivation targets chain-satisfy without bounding",
        "Record is a Tier-A admission",
        "scale-reference primitive is a Tier-A admission",
        "theta is owner-governed premise",
        "theta is theorem-derived",
        "AC_phi_lambda is theorem-derived",
    )
    for phrase in forbidden_positive_phrases:
        check(f"forbidden positive status claim absent: {phrase}", phrase not in note)

    print()
    print(f"SUMMARY: TIER-A REGISTRY BOUNDARY PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

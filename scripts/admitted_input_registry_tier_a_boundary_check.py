#!/usr/bin/env python3
"""Boundary runner for the Tier-A admitted-input registry note.

This runner checks source/registry alignment for the human Tier-A index after
the 2026-07-04 owner-governance retirement. It does not audit, derive, or
re-grade the retired residuals.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
AXIOM_PREMISES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
OWNER_GOVERNED = ROOT / "docs" / "audit" / "data" / "owner_governed_premise_nodes.json"
RUNNER = "scripts/admitted_input_registry_tier_a_boundary_check.py"
CACHE = "logs/runner-cache/admitted_input_registry_tier_a_boundary_check.txt"

FORMER_TARGET_IDS = {
    "staggered_dirac_realization_gate_note_2026-05-03": "AC_phi_lambda",
    "strong_cp_theta_zero_note": "theta",
}
CONVENTION_IDS = {
    "hypercharge_identification_note": "Y0",
    "g_bare_rigidity_theorem_note": "g0",
}
RECLASSIFIED_PRIMITIVES = {
    "minimal_axioms_record": "Record axiom",
    "scale_reference_primitive": "scale-reference primitive",
}
EXPECTED_AXIOM_IDS = {
    "minimal_axioms",
    "scale_reference_primitive",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
}

PASS_COUNT = 0
FAIL_COUNT = 0


def norm(text: str) -> str:
    return " ".join(text.split())


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def check(name: str, ok: bool, detail: object = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return ok


def main() -> int:
    print("=" * 78)
    print("TIER-A ADMITTED-INPUT REGISTRY BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: source/registry alignment only; no audit verdict changes.")
    print()

    note = read(NOTE)
    note_flat = norm(note)
    tier = load_json(TIER_A)
    axiom_premises = load_json(AXIOM_PREMISES)
    owner = load_json(OWNER_GOVERNED)
    derivation_targets = tier.get("derivation_targets") or {}
    retired = tier.get("retired_derivation_targets") or {}
    conventions = tier.get("conventions") or {}
    reclassified = tier.get("reclassified_primitives") or {}
    axiom_ids = set(axiom_premises.get("canonical_ids") or [])
    owner_ids = set(owner.get("canonical_ids") or [])

    check("source note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("machine Tier-A registry exists", TIER_A.exists(), TIER_A.relative_to(ROOT).as_posix())
    check("axiom premise registry exists", AXIOM_PREMISES.exists(), AXIOM_PREMISES.relative_to(ROOT).as_posix())
    check("owner-governed premise registry exists", OWNER_GOVERNED.exists(), OWNER_GOVERNED.relative_to(ROOT).as_posix())
    check("source claim type is meta", "**Claim type:** meta" in note)
    check("source status authority is audit lane only", "independent audit lane only" in note)
    check("source says it sets no audit status", "sets **no** audit status" in note)
    check("source registers this primary runner", RUNNER in note)
    check("source registers this cached output", CACHE in note)

    check("machine schema version is 1", tier.get("schema_version") == 1, tier.get("schema_version"))
    check("genuine admitted input count is zero", tier.get("genuine_admitted_input_count") == 0, tier.get("genuine_admitted_input_count"))
    check("canonical ids are empty", tier.get("canonical_ids") == [], tier.get("canonical_ids"))
    check("derivation target map is empty", derivation_targets == {}, derivation_targets)
    check("retired target keys preserve AC and theta", set(retired) == set(FORMER_TARGET_IDS), sorted(retired))
    check("owner-governed ids are the former target ids", owner_ids == set(FORMER_TARGET_IDS), sorted(owner_ids))
    check("owner-governed nodes match canonical ids", set(owner.get("nodes") or {}) == owner_ids, sorted((owner.get("nodes") or {}).keys()))

    for target_id, label in FORMER_TARGET_IDS.items():
        row = retired.get(target_id, {})
        node = (owner.get("nodes") or {}).get(target_id, {})
        check(f"{label} retired target row exists", bool(row), target_id)
        check(f"{label} retired label matches", row.get("label") == label, row.get("label"))
        check(f"{label} retained no-go portfolio preserved", bool(row.get("no_go_portfolio")), row.get("no_go_portfolio"))
        check(f"{label} no longer live derivation target", target_id not in derivation_targets)
        check(f"{label} owner-governed node exists", bool(node), target_id)
        check(f"{label} owner-governed boundary exists", bool(node.get("boundary")), node)
        check(
            f"{label} owner-governed source is adoption note",
            node.get("current_path") == "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md",
            node.get("current_path"),
        )

    check("approved axiom/primitive ids unchanged", axiom_ids == EXPECTED_AXIOM_IDS, sorted(axiom_ids))
    check("owner-governed ids are not axiom/primitive ids", not (owner_ids & axiom_ids), sorted(owner_ids & axiom_ids))
    check("former Tier-A targets are not axiom-premise ids", not (set(FORMER_TARGET_IDS) & axiom_ids), sorted(set(FORMER_TARGET_IDS) & axiom_ids))

    check("convention rows are present", set(CONVENTION_IDS).issubset(conventions), sorted(conventions))
    for convention_id, label in CONVENTION_IDS.items():
        row = conventions.get(convention_id, {})
        check(f"{label} convention label matches", row.get("label") == label, row.get("label"))
        check(f"{label} is vacuous convention", "vacuous" in row.get("class", "").lower(), row.get("class", ""))
        check(f"{label} not live derivation target", convention_id not in derivation_targets)
        check(f"{label} not owner-governed premise", convention_id not in owner_ids)

    check("reclassified primitives are present", set(RECLASSIFIED_PRIMITIVES).issubset(reclassified), sorted(reclassified))
    for primitive_id, label in RECLASSIFIED_PRIMITIVES.items():
        row = reclassified.get(primitive_id, {})
        check(f"{label} reclassification label matches", row.get("label") == label, row.get("label"))
        check(f"{label} not live derivation target", primitive_id not in derivation_targets)

    for phrase in [
        "Current live Tier-A admitted derivation targets: zero",
        "owner-governed residual premises",
        "genuine_admitted_input_count = 0",
        "canonical_ids = []",
        "derivation_targets = {}",
        "retired_derivation_targets",
        "zero live Tier-A admissions",
        "does not derive AC_phi_lambda or theta as theorems",
    ]:
        check(f"source records zero-retirement phrase: {phrase}", phrase in note_flat)

    for forbidden in [
        "Current live Tier-A admitted derivation targets: two",
        "two dimensionless Tier-A admissions",
        "stand as genuine admitted derivation targets",
        "AC_phi_lambda remains a Tier-A row",
        "theta remains a Tier-A row",
        "owner-governed residual premises are axioms",
        "owner-governed residual premises are approved primitives",
    ]:
        check(f"forbidden stale live-status phrase absent: {forbidden}", forbidden not in note_flat)

    print()
    print(f"SUMMARY: TIER-A REGISTRY BOUNDARY PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

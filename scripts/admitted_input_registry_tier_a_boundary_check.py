#!/usr/bin/env python3
"""Boundary runner for the Tier-A admitted-input registry note.

This runner checks source/registry alignment for the human Tier-A index and
machine `tier_a_admissions.json`. It does not audit, retire, add, remove, or
re-grade any admitted input.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
AXIOM_PREMISES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
RUNNER = "scripts/admitted_input_registry_tier_a_boundary_check.py"
CACHE = "logs/runner-cache/admitted_input_registry_tier_a_boundary_check.txt"

TARGET_IDS = {
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


def main() -> int:
    print("=" * 78)
    print("TIER-A ADMITTED-INPUT REGISTRY BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: source/registry alignment only; no audit verdict changes.")
    print()

    note = read(NOTE)
    tier = load_json(TIER_A)
    axiom_premises = load_json(AXIOM_PREMISES)
    derivation_targets = tier.get("derivation_targets") or {}
    conventions = tier.get("conventions") or {}
    reclassified = tier.get("reclassified_primitives") or {}
    axiom_ids = set(axiom_premises.get("canonical_ids") or [])

    check("source note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("machine Tier-A registry exists", TIER_A.exists(), TIER_A.relative_to(ROOT).as_posix())
    check("axiom premise registry exists", AXIOM_PREMISES.exists(), AXIOM_PREMISES.relative_to(ROOT).as_posix())
    check("source claim type is meta", "**Claim type:** meta" in note)
    check("source status authority is audit lane only", "independent audit lane only" in note)
    check("source says it sets no audit status", "sets **no** audit status" in note)
    check("source registers this primary runner", RUNNER in note)
    check("source registers this cached output", CACHE in note)

    check("machine schema version is 1", tier.get("schema_version") == 1, str(tier.get("schema_version")))
    check("genuine admitted input count is exactly two", tier.get("genuine_admitted_input_count") == 2, str(tier.get("genuine_admitted_input_count")))
    check("canonical ids are exactly the two Tier-A derivation targets", set(tier.get("canonical_ids") or []) == set(TARGET_IDS), str(tier.get("canonical_ids")))
    check("derivation target keys match canonical ids", set(derivation_targets) == set(TARGET_IDS), str(sorted(derivation_targets)))

    for target_id, label in TARGET_IDS.items():
        row = derivation_targets.get(target_id, {})
        check(f"{label} target row exists", bool(row), target_id)
        check(f"{label} label matches", row.get("label") == label, str(row.get("label")))
        check(f"{label} has no-go portfolio", bool(row.get("no_go_portfolio")), str(row.get("no_go_portfolio")))
        check(f"{label} has minimum decomposition", bool(row.get("minimum_decomposition")), str(row.get("minimum_decomposition")))
        check(f"{label} has sharpening source list", bool(row.get("sharpening_sources_status_set_by_audit_lane")), "")

    check(
        "AC_phi_lambda has three named minimum atoms",
        derivation_targets["staggered_dirac_realization_gate_note_2026-05-03"].get("minimum_decomposition")
        == ["reading_occupancy_selection", "delta_readout_identification_R_eta", "species_bridge"],
        "",
    )
    ac_row = derivation_targets["staggered_dirac_realization_gate_note_2026-05-03"]
    ac_statement = ac_row.get("statement", "")
    ac_reclass = (ac_row.get("partial_reclassifications") or {}).get("reading_occupancy_selection_value_face", {})
    check("AC_phi_lambda(i) value face is reclassified to realized-state registration in machine row", "value face retired to realized-state registration" in ac_statement)
    check("AC_phi_lambda(i) surviving residual is measure-side/dynamical realization", "measure-side doublet occupancy realization binary" in ac_statement)
    check("AC_phi_lambda(i) machine reclassification source is registered", ac_reclass.get("source") == "docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md", str(ac_reclass))
    check("AC_phi_lambda(i) machine reclassification keeps measure-side boundary", "measure-side/dynamical realization binary remains" in ac_reclass.get("boundary", ""))
    check(
        "theta has two named minimum atoms",
        derivation_targets["strong_cp_theta_zero_note"].get("minimum_decomposition")
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        "",
    )

    check("convention rows are present", set(CONVENTION_IDS).issubset(conventions), str(sorted(conventions)))
    for convention_id, label in CONVENTION_IDS.items():
        row = conventions.get(convention_id, {})
        check(f"{label} convention label matches", row.get("label") == label, str(row.get("label")))
        check(f"{label} is vacuous convention", "vacuous" in row.get("class", "").lower(), row.get("class", ""))
        check(f"{label} not admitted derivation target", convention_id not in derivation_targets, "")

    check("reclassified primitives are present", set(RECLASSIFIED_PRIMITIVES).issubset(reclassified), str(sorted(reclassified)))
    for primitive_id, label in RECLASSIFIED_PRIMITIVES.items():
        row = reclassified.get(primitive_id, {})
        check(f"{label} reclassification label matches", row.get("label") == label, str(row.get("label")))
        check(f"{label} not admitted derivation target", primitive_id not in derivation_targets, "")

    check("Record lives in axiom-premise registry", "minimal_axioms" in axiom_ids, str(sorted(axiom_ids)))
    check("Scale reference lives in axiom-premise registry", "scale_reference_primitive" in axiom_ids, str(sorted(axiom_ids)))
    check("Tier-A targets are not axiom-premise ids", not (set(TARGET_IDS) & axiom_ids), str(sorted(set(TARGET_IDS) & axiom_ids)))
    check("Tier-A conventions are not axiom-premise ids", not (set(CONVENTION_IDS) & axiom_ids), str(sorted(set(CONVENTION_IDS) & axiom_ids)))

    check("note states Record retired from Tier A", "Record is no longer a Tier-A admission" in note)
    check("note keeps observable-principle parent outside Record", "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not promoted" in note)
    check("note says scale primitive is not counted", "scale-reference primitive is likewise not counted here" in note)
    check("note says Y0 and g0 are not counted", "not** counted as admitted inputs" in note)
    check("note states two dimensionless Tier-A admissions", "two dimensionless Tier-A admissions" in note)
    check("note says sharpening adds/removes/regrades nothing", "No admission is\nadded, removed, adopted, or re-graded" in note)
    check("note records 2026-07-04 value-face reclassification", "2026-07-04 value-face reclassification" in note)
    check("note says per-lane r value is registered state data", "per-lane\nvalue of `r` is registered state data" in note)
    check("note says surviving residual is measure-side realization", "surviving Tier-A\nresidual in (i) is the measure-side/dynamical realization binary" in note)
    check("note says dependent rows stay bounded", "every\ndependent stays bounded" in note)
    check("note says audit status remains audit-lane-only", "audit status remains audit-lane-only" in note)
    check("note propagation says Tier-A accepted premise is bounded", "chain-satisfying **only at `retained_bounded`**" in note)
    check("note says no hand-maintained backlinks", "No back-links are maintained by hand" in note)

    forbidden_positive_phrases = (
        "sets audit status",
        "promotes rows to retained",
        "changes rows' effective_status",
        "Tier-A derivation targets chain-satisfy without bounding",
        "Record is a Tier-A admission",
        "scale-reference primitive is a Tier-A admission",
    )
    for phrase in forbidden_positive_phrases:
        check(f"forbidden positive status claim absent: {phrase}", phrase not in note)

    print()
    print(f"SUMMARY: TIER-A REGISTRY BOUNDARY PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

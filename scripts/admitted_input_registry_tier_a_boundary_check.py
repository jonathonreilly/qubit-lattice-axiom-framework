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
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
RUNNER = "scripts/admitted_input_registry_tier_a_boundary_check.py"
CACHE = "logs/runner-cache/admitted_input_registry_tier_a_boundary_check.txt"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}

TARGET_IDS = {
    "staggered_dirac_realization_gate_note_2026-05-03": "AC_phi_lambda",
}
# theta retired 2026-07-05 by retained derivation; preserved with its no-go
# portfolio under retired_derivation_targets (owner approval in PR #3511).
RETIRED_TARGET_IDS = {
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
THETA_DISCHARGE_BASIS_IDS = {
    "per_plaquette_from_adjacency_license_bounded_theorem_note_2026-06-09",
    "theta_cross_plane_term_absent_in_supplied_per_plaquette_class_bounded_theorem_note_2026-06-09",
    "theta_multi_plaquette_cross_plane_absence_narrowing_bounded_theorem_note_2026-06-11",
    "theta_gauge_native_positive_class_emergent_sector_weighting_narrow_theorem_note_2026-07-04",
    "theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10",
    "registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10",
    "strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12",
    "kcpt_orbit_constancy_and_determinant_character_boundary_supplied_context_bridge_note_2026-07-04",
}
THETA_POSITIVE_CLASS_ROW = (
    "theta_gauge_native_positive_class_emergent_sector_weighting_narrow_theorem_note_2026-07-04"
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


def main() -> int:
    print("=" * 78)
    print("TIER-A ADMITTED-INPUT REGISTRY BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: source/registry alignment only; no audit verdict changes.")
    print()

    note = read(NOTE)
    tier = load_json(TIER_A)
    axiom_premises = load_json(AXIOM_PREMISES)
    ledger = load_json(LEDGER)
    derivation_targets = tier.get("derivation_targets") or {}
    conventions = tier.get("conventions") or {}
    reclassified = tier.get("reclassified_primitives") or {}
    axiom_ids = set(axiom_premises.get("canonical_ids") or [])
    ledger_rows = ledger.get("rows") or {}

    check("source note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("machine Tier-A registry exists", TIER_A.exists(), TIER_A.relative_to(ROOT).as_posix())
    check("axiom premise registry exists", AXIOM_PREMISES.exists(), AXIOM_PREMISES.relative_to(ROOT).as_posix())
    check("audit ledger exists", LEDGER.exists(), LEDGER.relative_to(ROOT).as_posix())
    check("source claim type is meta", "**Claim type:** meta" in note)
    check("source status authority is audit lane only", "independent audit lane only" in note)
    check("source says it sets no audit status", "sets **no** audit status" in note)
    check("source registers this primary runner", RUNNER in note)
    check("source registers this cached output", CACHE in note)

    retired_targets = tier.get("retired_derivation_targets") or {}

    check("machine schema version is 1", tier.get("schema_version") == 1, str(tier.get("schema_version")))
    check("genuine admitted input count is exactly one", tier.get("genuine_admitted_input_count") == 1, str(tier.get("genuine_admitted_input_count")))
    check("canonical ids are exactly the one Tier-A derivation target", set(tier.get("canonical_ids") or []) == set(TARGET_IDS), str(tier.get("canonical_ids")))
    check("derivation target keys match canonical ids", set(derivation_targets) == set(TARGET_IDS), str(sorted(derivation_targets)))
    check("retired target keys are exactly theta", set(retired_targets) == set(RETIRED_TARGET_IDS), str(sorted(retired_targets)))

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
    theta_row = retired_targets.get("strong_cp_theta_zero_note", {})
    check("theta retired row exists", bool(theta_row), "retired_derivation_targets")
    check("theta retired label matches", theta_row.get("label") == "theta", str(theta_row.get("label")))
    check("theta retired no-go portfolio preserved", bool(theta_row.get("no_go_portfolio")), str(theta_row.get("no_go_portfolio")))
    check(
        "theta retired minimum decomposition preserved",
        theta_row.get("minimum_decomposition")
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        "",
    )
    retirement = theta_row.get("retirement") or {}
    check("theta retirement record present", bool(retirement), "")
    check("theta retirement mechanism is retained derivation", retirement.get("mechanism") == "retired_by_retained_derivation", str(retirement.get("mechanism")))
    check("theta retirement records owner approval location", "PR #3511" in str(retirement.get("owner_approval")), "")
    check("theta retirement records scope", "canonical" in str(retirement.get("scope", "")), "")
    discharge_basis = retirement.get("discharge_basis_rows_all_retained_grade") or {}
    check("theta retirement records discharge basis", bool(discharge_basis), "")
    check(
        "theta discharge basis categories are row-id lists",
        all(isinstance(value, list) for value in discharge_basis.values()),
        str({key: type(value).__name__ for key, value in discharge_basis.items()}),
    )
    discharge_ids = {
        row_id
        for row_ids in discharge_basis.values()
        if isinstance(row_ids, list)
        for row_id in row_ids
    }
    check(
        "theta discharge basis rows are exactly expected",
        discharge_ids == THETA_DISCHARGE_BASIS_IDS,
        str(sorted(discharge_ids)),
    )
    for row_id in sorted(THETA_DISCHARGE_BASIS_IDS):
        ledger_row = ledger_rows.get(row_id) or {}
        status = (ledger_row.get("audit_status"), ledger_row.get("effective_status"))
        check(
            f"theta discharge row retained-grade: {row_id}",
            status[0] == "audited_clean" and status[1] in RETAINED_GRADES,
            str(status),
        )
    source_row = ledger_rows.get("strong_cp_theta_zero_note") or {}
    check(
        "retired theta source row remains retained-bounded source theorem",
        source_row.get("claim_type") == "bounded_theorem"
        and source_row.get("audit_status") == "audited_clean"
        and source_row.get("effective_status") == "retained_bounded",
        str(
            (
                source_row.get("claim_type"),
                source_row.get("audit_status"),
                source_row.get("effective_status"),
            )
        ),
    )
    check("retired theta source row has no hidden deps", source_row.get("deps") == [], str(source_row.get("deps")))
    positive_row = ledger_rows.get(THETA_POSITIVE_CLASS_ROW) or {}
    cross_confirmation = positive_row.get("cross_confirmation") or {}
    check(
        "theta positive-class row has explicit second-seat confirmation",
        cross_confirmation.get("status") == "confirmed"
        and cross_confirmation.get("mode") == "explicit_second_seat",
        str({key: cross_confirmation.get(key) for key in ("status", "mode")}),
    )
    check(
        "theta retirement records cross-confirmation separately",
        "explicit second seat" in str(retirement.get("gauge_side_theta_value_cross_confirmation")),
        "",
    )
    check(
        "theta retirement records source-row boundary",
        "selected-action-surface source row" in str(retirement.get("retired_target_source_row")),
        "",
    )
    check(
        "theta retirement records PR #4995 artifact path",
        "PR #4995" in str(retirement.get("decision_artifact"))
        and "docs/THETA_RETIREMENT_BASIS_REMATCH_2026-07-04.md" in str(retirement.get("decision_artifact"))
        and "not shipped as a live source note" in str(retirement.get("decision_artifact")),
        str(retirement.get("decision_artifact")),
    )
    check("theta no longer an active derivation target", "strong_cp_theta_zero_note" not in derivation_targets, "")

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
    check("retired targets are not axiom-premise ids", not (set(RETIRED_TARGET_IDS) & axiom_ids), str(sorted(set(RETIRED_TARGET_IDS) & axiom_ids)))
    check("Tier-A conventions are not axiom-premise ids", not (set(CONVENTION_IDS) & axiom_ids), str(sorted(set(CONVENTION_IDS) & axiom_ids)))

    check("note states Record retired from Tier A", "Record was retired from Tier A on 2026-06-05" in note or "Record is no longer a Tier-A admission" in note)
    check("note states theta retired from Tier A", "θ retired from Tier A (2026-07-05" in note)
    check("note states count is one", "is now the **one** row below" in note)
    check("note keeps observable-principle parent outside Record", "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not promoted" in note)
    check("note says scale primitive is not counted", "scale-reference primitive is likewise not counted here" in note)
    check("note says Y0 and g0 are not counted", "not** counted as admitted inputs" in note)
    check("note preserves historical two-admission refinement as historical", "historical count only" in note)
    check("note says sharpening added/removed/regraded nothing historically", "no admission was added, removed, adopted, or re-graded" in note)
    check("note says historical dependent rows stayed bounded", "every dependent stayed bounded" in note)
    check("note has no active stale theta-admitted wording", "θ is admitted here exactly as" not in note)
    check("note has no active stale count-stays-two wording", "the count stays at two" not in note)
    check("note preserves theta source row as bounded source", "retained-bounded selected-action-surface theorem" in note)
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

#!/usr/bin/env python3
"""Boundary runner for AC_phi_lambda(iii) C3-grade owner ratification.

This runner checks that the new registry governance note, the human Tier-A
registry, and the machine Tier-A registry agree about one narrow move:
AC_phi_lambda(iii)'s C3-grade species bridge is retired from Tier-A by owner
ratification, while AC_phi_lambda remains a Tier-A row through its other two
residual atoms.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_C3_GRADE_OWNER_RATIFICATION_RETIREMENT_NOTE_2026-07-04.md"
HUMAN_REGISTRY = ROOT / "docs" / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
PARENT = ROOT / "docs" / "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
RATIFICATION = ROOT / "docs" / "SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md"
C3_CONTEXT = ROOT / "docs" / "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"

AC_ID = "staggered_dirac_realization_gate_note_2026-05-03"
THETA_ID = "strong_cp_theta_zero_note"

PASS_COUNT = 0
FAIL_COUNT = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def norm(text: str) -> str:
    return " ".join(text.split())


def has(text: str, phrase: str) -> bool:
    return norm(phrase) in norm(text)


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
    print("ACPHILAMBDA SPECIES-BRIDGE C3-GRADE OWNER RATIFICATION CHECK")
    print("=" * 78)
    print("Scope: registry-governance alignment only; no audit verdict changes.")
    print()

    note = read(NOTE)
    human = read(HUMAN_REGISTRY)
    policy = read(POLICY)
    parent = read(PARENT)
    ratification = read(RATIFICATION)
    c3_context = read(C3_CONTEXT)
    tier = load_json(TIER_A)
    targets = tier.get("derivation_targets") or {}
    ac = targets.get(AC_ID) or {}
    theta = targets.get(THETA_ID) or {}
    partial = ac.get("partial_reclassifications") or {}
    species = partial.get("species_bridge_c3_grade") or {}

    for path in (NOTE, HUMAN_REGISTRY, TIER_A, POLICY, PARENT, RATIFICATION, C3_CONTEXT):
        check(f"{path.relative_to(ROOT).as_posix()} exists", path.exists())

    check("new note is meta", "**Claim type:** meta" in note)
    check("new note records owner path-extension yes", "is answered yes for the narrow case below" in note)
    check("new note scopes to C3 grade only", "C3-structural grade only" in note)
    check("new note says AC row does not retire", "AC_phi_lambda itself does **not** retire" in note)
    check("new note lists the two surviving AC atoms", "measure-side doublet occupancy realization binary" in note and "delta readout identification R-eta" in note)
    check("new note conserves above-grade residue", "taste/Dirac/chirality" in note and "CKM/PMNS" in note)
    check("new note excludes audit-status change", "sets no audit verdict" in note)
    check("new note excludes axiom and primitive changes", "Does not add or amend an axiom" in note and "Does not create an approved primitive" in note)

    check(
        "parent source has no-number/no-selector witness",
        ("no tested" in parent and "number, selector, ordering, or" in parent and "weight" in parent),
    )
    check("parent source has contentlessness proof-strength caveat", "argued/strongly-supported, not exhaustively proven" in parent)
    check("ratification source records external-relatum failure", "second relatum is external nature" in ratification)
    check("ratification source records two-part owner decision", "two-part owner decision" in ratification)
    check("C3 context source is internal labeling precedent", has(c3_context, "naming ratification on already-landed surfaces"))

    check("policy records 2026-07-04 owner species-bridge decision", "2026-07-04 -- AC_phi_lambda(iii) species bridge C3-grade ratification" in policy)
    check("policy records no row retirement", "AC_phi_lambda remains a Tier-A row" in policy)

    check("genuine admitted target count remains two", tier.get("genuine_admitted_input_count") == 2, str(tier.get("genuine_admitted_input_count")))
    check("canonical ids unchanged", tier.get("canonical_ids") == [AC_ID, THETA_ID], str(tier.get("canonical_ids")))
    check("AC row still exists", bool(ac))
    check("theta row still exists", bool(theta))
    check(
        "AC minimum decomposition is now exactly two residual atoms",
        ac.get("minimum_decomposition") == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        str(ac.get("minimum_decomposition")),
    )
    check("machine statement says species bridge is not Tier-A target", "species bridge C3-grade leg is owner-ratified" in ac.get("statement", ""))
    check("machine statement conserves above-grade boundary", "Above-C3" in ac.get("statement", "") and "CKM/PMNS" in ac.get("statement", ""))
    check("species bridge partial reclassification row exists", bool(species), str(partial))
    check("species bridge partial reclassification status is owner ratified", species.get("status") == "owner_ratified_c3_grade_interpretive_identification", str(species))
    check("species bridge partial reclassification source is new note", species.get("source") == "docs/ACPHILAMBDA_SPECIES_BRIDGE_C3_GRADE_OWNER_RATIFICATION_RETIREMENT_NOTE_2026-07-04.md", str(species))
    boundary_lower = species.get("boundary", "").lower()
    check("species bridge boundary preserves non-covered residues", "taste/dirac/chirality" in boundary_lower and "ckm/pmns" in boundary_lower)

    check("human registry table no longer states three AC residual atoms", "three named residual atoms" not in human)
    check("human registry has two-residual AC heading", "minimum decomposition (two surviving Tier-A residual atoms" in human)
    check("human registry records species bridge owner ratification", "species bridge C3-grade owner ratification" in human)
    check("human registry says dependent rows stay bounded", has(human, "downstream rows depending on AC_phi_lambda remain bounded"))
    check("human registry keeps theta untouched", "theta row is untouched" in human)

    forbidden = (
        "AC_phi_lambda retires",
        "theta retires",
        "species bridge is an axiom",
        "species bridge is an approved primitive",
        "C3-grade ratification derives the species bridge",
        "CKM/PMNS alignment is covered",
    )
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note and phrase not in human)

    print()
    print(f"SUMMARY: ACPHILAMBDA SPECIES-BRIDGE C3-GRADE CHECK PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

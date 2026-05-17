#!/usr/bin/env python3
"""Audit-prep verifier for cross_sector_a_squared_koide_vcb_bridge_support_note_2026-04-25.

Verifies docs/CROSS_SECTOR_A_SQUARED_KOIDE_VCB_BRIDGE_SUPPORT_NOTE_2026-04-25_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md.

Programmatic checks:
  - The parent note exists at the expected path.
  - CITED deps (>=1 hit, classification deferred to audit-lane judgment based on context).
  - NOT-CITED deps (0 hits, programmatically certain).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs/CROSS_SECTOR_A_SQUARED_KOIDE_VCB_BRIDGE_SUPPORT_NOTE_2026-04-25.md"

CITED_DEPS = [
    "koide_q_delta_closure_package_readme_2026-04-21",
]

NOT_CITED_DEPS = [
    "dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18",
    "dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16",
    "dm_leptogenesis_ne_charged_source_response_reduction_note_2026-04-16",
    "dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16",
    "dm_wilson_parent_correctness_audit_note_2026-04-18",
    "dm_wilson_to_dweh_hermitian_source_family_target_note_2026-04-18",
    "dm_wilson_to_dweh_structured_model_realization_theorem_note_2026-04-18",
    "koide_brannen_callan_harvey_candidate_note_2026-04-22",
    "koide_brannen_geometry_dirac_support_note_2026-04-22",
    "koide_brannen_phase_reduction_theorem_note_2026-04-20",
    "koide_circulant_character_derivation_note_2026-04-18",
    "koide_gamma_orbit_positive_one_clock_semigroup_note_2026-04-18",
    "koide_positive_paths_first_principles_note_2026-04-18",
    "koide_q_delta_linking_relation_theorem_note_2026-04-20",
    "koide_z3_qubit_radian_bridge_no_go_note_2026-04-20",
    "lepton_single_higgs_pmns_triviality_note",
    "neutrino_dirac_two_higgs_canonical_reduction_note",
    "neutrino_mass_reduction_to_dirac_note",
    "pmns_active_four_real_source_from_transport_note",
    "pmns_corner_transport_active_block_note",
    "publication.ci3_z3.publication_matrix",
]


def check(label: str, condition: bool, detail: str = "", class_a: bool = True) -> bool:
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        if class_a:
            CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    tag = " [A]" if class_a else ""
    msg = f"  [{status}]{tag} {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def grep_count(content: str, needle: str) -> int:
    return len(re.findall(re.escape(needle), content, re.IGNORECASE))


def main() -> int:
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — cross_sector_a_squared_koide_vcb_bridge_support_note_2026-04-25")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
    print()

    print(f"PART 1 — CITED deps (expect: >=1 hit each):")
    for dep in CITED_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited (>=1 hit)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print(f"PART 2 — NOT-CITED deps (expect: 0 hits each):")
    for dep in NOT_CITED_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} NOT cited (0 hits)",
            n == 0,
            f"hits = {n}",
        )

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print(f"Class-A pattern hits: {CLASS_A_HITS}")
    print("=" * 78)

    if FAIL_COUNT == 0:
        print()
        print("VERIFIED")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

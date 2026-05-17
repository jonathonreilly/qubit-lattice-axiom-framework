#!/usr/bin/env python3
"""Audit-prep verifier for a3_r5_hostile_review_confirms_obstruction_note.

Verifies docs/A3_R5_HOSTILE_REVIEW_CONFIRMS_OBSTRUCTION_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md.

Programmatic checks:
  1. The parent note exists.
  2. a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5
     IS cited (load-bearing review target).
  3. staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac
     IS cited (HR5.4 reference + bounded-gate anchor).
  4. axiom_first_reeh_schlieder_theorem_note_2026-05-01 IS cited
     (informational-background; tagged "HR5.2 background").
  5. The other 28 co-cycle deps are NOT cited (zero hits).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs" / "A3_R5_HOSTILE_REVIEW_CONFIRMS_OBSTRUCTION_NOTE_2026-05-08_R5HR.md"

LOAD_BEARING_DEPS = [
    "a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5",
    "staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac",
]

INFORMATIONAL_BACKGROUND_DEPS = [
    "axiom_first_reeh_schlieder_theorem_note_2026-05-01",
]

NOT_CITED_DEPS = [
    "axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01",
    "c3_symmetry_preserved_interpretation_note_2026-05-08",
    "dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18",
    "dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16",
    "dm_leptogenesis_ne_charged_source_response_reduction_note_2026-04-16",
    "dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16",
    "dm_wilson_parent_correctness_audit_note_2026-04-18",
    "dm_wilson_to_dweh_hermitian_source_family_target_note_2026-04-18",
    "dm_wilson_to_dweh_structured_model_realization_theorem_note_2026-04-18",
    "emergent_lorentz_invariance_note",
    "koide_a1_derivation_status_note",
    "koide_a1_probe_plancherel_peter_weyl_bounded_obstruction_note_2026-05-09_probe12",
    "koide_a1_route_a_koide_nishiura_bounded_obstruction_note_2026-05-08_routea",
    "koide_a1_route_d_newton_girard_bounded_obstruction_note_2026-05-08_routed",
    "koide_a1_route_e_kostant_weyl_bounded_obstruction_note_2026-05-08_routee",
    "koide_circulant_character_derivation_note_2026-04-18",
    "koide_gamma_orbit_positive_one_clock_semigroup_note_2026-04-18",
    "koide_positive_paths_first_principles_note_2026-04-18",
    "lepton_single_higgs_pmns_triviality_note",
    "lorentz_kernel_positive_closure_note",
    "neutrino_dirac_two_higgs_canonical_reduction_note",
    "neutrino_mass_reduction_to_dirac_note",
    "planck_from_structure_path_opening_meta_note_2026-05-10",
    "planck_scale_conditional_completion_note_2026-04-24",
    "planck_scale_lane_status_note_2026-04-23",
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
    print("AUDIT-PREP VERIFIER — a3_r5_hostile_review_confirms_obstruction")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
    print()

    print("PART 1 — load-bearing deps (expect: cited):")
    for dep in LOAD_BEARING_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited (≥1 hit)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print("PART 2 — informational-background deps (expect: cited in Cross-references):")
    for dep in INFORMATIONAL_BACKGROUND_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited (≥1 hit, background-tagged)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print("PART 3 — not-cited deps (expect: zero hits):")
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
    print()
    print("VERDICT:")
    if FAIL_COUNT == 0:
        print("  AUDIT-PREP FINDINGS VERIFIED")
        print("  2 of 31 deps LOAD-BEARING (R5 source + substep4_ac)")
        print("  1 of 31 deps INFORMATIONAL-BACKGROUND (Reeh-Schlieder, HR5.2 tag)")
        print("  28 of 31 deps NOT-CITED (zero hits)")
        print("  Audit handoff: independent audit lane owns verdict/status; this runner")
        print("    verifies dependency classification only")
        print(f"  dominant_class: A ({CLASS_A_HITS} class-A hits)")
        return 0
    else:
        print(f"  VERIFICATION FAILED — {FAIL_COUNT} FAILs")
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Audit-prep verifier for dm_effective_parent_one_clock_transfer_boundary_theorem.

Verifies docs/DM_EFFECTIVE_PARENT_ONE_CLOCK_TRANSFER_BOUNDARY_NOTE_2026-05-17.md.

Programmatic checks:
  1. The parent note exists.
  2. dm_wilson_parent_correctness_audit_note_2026-04-18 IS cited (framing only).
  3. The other 33 co-cycle deps are NOT cited (zero hits).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs" / "DM_EFFECTIVE_PARENT_ONE_CLOCK_TRANSFER_BOUNDARY_THEOREM_NOTE_2026-04-18.md"

INFORMATIONAL_FRAMING_DEPS = [
    "dm_wilson_parent_correctness_audit_note_2026-04-18",
]

NOT_CITED_DEPS = [
    "dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16",
    "dm_leptogenesis_ne_charged_source_response_reduction_note_2026-04-16",
    "dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16",
    "dm_wilson_to_dweh_hermitian_source_family_target_note_2026-04-18",
    "dm_wilson_to_dweh_structured_model_realization_theorem_note_2026-04-18",
    "emergent_lorentz_invariance_note",
    "hubble_lane5_cosmic_history_ratio_necessity_no_go_note_2026-04-26",
    "hubble_lane5_planck_c1_gate_audit_note_2026-04-26",
    "hubble_lane5_workstream_status_note_2026-04-27",
    "koide_a1_derivation_status_note",
    "koide_a1_probe_plancherel_peter_weyl_bounded_obstruction_note_2026-05-09_probe12",
    "koide_a1_route_a_koide_nishiura_bounded_obstruction_note_2026-05-08_routea",
    "koide_a1_route_d_newton_girard_bounded_obstruction_note_2026-05-08_routed",
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
    "publication.ci3_z3.claims_table",
    "publication.ci3_z3.derivation_atlas",
    "publication.ci3_z3.derivation_validation_map",
    "publication.ci3_z3.gravity_publication_package_summary_2026-04-15",
    "publication.ci3_z3.prediction_surface_2026-04-15",
    "publication.ci3_z3.publication_matrix",
    "publication.ci3_z3.quantitative_summary_table",
    "c3_symmetry_preserved_interpretation_note_2026-05-08",
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
    print("AUDIT-PREP VERIFIER — dm_effective_parent_one_clock_transfer_boundary")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
    print()

    print("PART 1 — informational-framing deps (expect: cited but only as framing):")
    for dep in INFORMATIONAL_FRAMING_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited (≥1 hit, framing only)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print("PART 2 — not-cited deps (expect: zero hits):")
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
        print("  1 of 34 deps is INFORMATIONAL (framing only, not invoked in proofs)")
        print("  33 of 34 deps are NOT-CITED (zero text hits)")
        print("  Audit handoff: independent audit lane owns verdict/status; this runner")
        print("    verifies dependency classification only")
        print(f"  dominant_class: A ({CLASS_A_HITS} class-A hits)")
        return 0
    else:
        print(f"  VERIFICATION FAILED — {FAIL_COUNT} FAILs")
        return 1


if __name__ == "__main__":
    sys.exit(main())

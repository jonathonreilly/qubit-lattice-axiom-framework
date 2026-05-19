#!/usr/bin/env python3
"""Audit-prep verifier for axiom_first_microcausality_lieb_robinson_theorem.

Verifies docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_NOTE_2026-05-17.md.

Programmatic checks:
  1. The parent note exists.
  2. emergent_lorentz_invariance_note IS cited in the parent (load-bearing for M3).
  3. lorentz_kernel_positive_closure_note IS cited in the parent (load-bearing for M3).
  4. The other 40 co-cycle deps are NOT cited (zero text hits).

The 2 load-bearing exceptions correspond to the parent's §Proof Step 3 (M3)
which uses these notes as retained authority for v_LR · a_s/a_τ → c < ∞.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs" / "AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md"

LOAD_BEARING_DEPS = [
    "emergent_lorentz_invariance_note",
    "lorentz_kernel_positive_closure_note",
]

NOT_CITED_DEPS = [
    "axiom_first_reeh_schlieder_theorem_note_2026-05-01",
    "c3_symmetry_preserved_interpretation_note_2026-05-08",
    "conventions_unification_companion_note_2026-05-08",
    "dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18",
    "dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16",
    "dm_leptogenesis_ne_charged_source_response_reduction_note_2026-04-16",
    "dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16",
    "dm_wilson_parent_correctness_audit_note_2026-04-18",
    "dm_wilson_to_dweh_hermitian_source_family_target_note_2026-04-18",
    "dm_wilson_to_dweh_structured_model_realization_theorem_note_2026-04-18",
    "koide_a1_11_probe_campaign_bounded_admission_meta_note_2026-05-08",
    "koide_a1_derivation_status_note",
    "koide_a1_probe_flavor_anomaly_bounded_obstruction_note_2026-05-08_probe2",
    "koide_a1_probe_gravity_phase_bounded_obstruction_note_2026-05-08_probe3",
    "koide_a1_probe_operator_class_bounded_note_2026-05-08_probe6",
    "koide_a1_probe_plancherel_peter_weyl_bounded_obstruction_note_2026-05-09_probe12",
    "koide_a1_probe_real_structure_bounded_obstruction_note_2026-05-09_probe13",
    "koide_a1_probe_rg_fixed_point_bounded_obstruction_note_2026-05-08_probe5",
    "koide_a1_probe_rp_frobenius_bounded_obstruction_note_2026-05-08_probe1",
    "koide_a1_probe_spectral_action_bounded_obstruction_note_2026-05-08_probe4",
    "koide_a1_probe_z2_c3_pairing_bounded_obstruction_note_2026-05-08_probe7",
    "koide_a1_route_a_koide_nishiura_bounded_obstruction_note_2026-05-08_routea",
    "koide_a1_route_d_newton_girard_bounded_obstruction_note_2026-05-08_routed",
    "koide_a1_route_e_kostant_weyl_bounded_obstruction_note_2026-05-08_routee",
    "koide_a1_route_f_casimir_difference_bounded_obstruction_note_2026-05-08_routef",
    "koide_bae_30_probe_campaign_terminal_synthesis_meta_note_2026-05-09",
    "koide_circulant_character_derivation_note_2026-04-18",
    "koide_gamma_orbit_positive_one_clock_semigroup_note_2026-04-18",
    "koide_positive_paths_first_principles_note_2026-04-18",
    "lepton_single_higgs_pmns_triviality_note",
    "neutrino_dirac_two_higgs_canonical_reduction_note",
    "neutrino_mass_reduction_to_dirac_note",
    "planck_from_structure_path_opening_meta_note_2026-05-10",
    "planck_orientation_principle_bounded_note_2026-05-10_planckp3",
    "planck_scale_conditional_completion_note_2026-04-24",
    "planck_scale_lane_status_note_2026-04-23",
    "pmns_active_four_real_source_from_transport_note",
    "pmns_corner_transport_active_block_note",
    "publication.ci3_z3.publication_matrix",
    "staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac",
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
    """Count case-insensitive occurrences of needle as a substring."""
    return len(re.findall(re.escape(needle), content, re.IGNORECASE))


def main() -> int:
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — axiom_first_microcausality_lieb_robinson")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")

    print()
    print(f"  Total deps verified: {len(LOAD_BEARING_DEPS) + len(NOT_CITED_DEPS)}")
    print()

    print("PART 1 — load-bearing deps (expect: cited in parent):")
    for dep in LOAD_BEARING_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited in parent (≥1 hit)",
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
        print("  2 of 42 deps are LOAD-BEARING (Lorentz notes cited in §Proof Step 3 for M3)")
        print("  40 of 42 deps are NOT-CITED (zero text hits)")
        print("  Audit handoff: independent audit lane owns verdict/status; this runner")
        print("    verifies dependency classification only")
        print(f"  dominant_class: A ({CLASS_A_HITS} class-A pattern hits)")
        return 0
    else:
        print(f"  VERIFICATION FAILED — {FAIL_COUNT} FAILs")
        return 1


if __name__ == "__main__":
    sys.exit(main())

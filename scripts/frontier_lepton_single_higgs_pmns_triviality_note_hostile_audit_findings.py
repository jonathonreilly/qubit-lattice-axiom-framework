#!/usr/bin/env python3
"""Audit-prep verifier for lepton_single_higgs_pmns_triviality_note.

Verifies docs/LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md.

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
PARENT_PATH = REPO_ROOT / "docs/LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md"

CITED_DEPS = [
    "neutrino_mass_reduction_to_dirac_note",
]

NOT_CITED_DEPS = [
    "neutrino_dirac_pmns_retained_lane_packet_2026-04-16",
    "neutrino_dirac_two_higgs_canonical_reduction_note",
    "neutrino_mass_derived_note",
    "neutrino_retained_observable_bounds_theorem_note_2026-04-24",
    "neutrino_retained_status_note_2026-04-16",
    "pmns_active_four_real_source_from_transport_note",
    "pmns_branch_conditioned_quadratic_sheet_closure_note",
    "pmns_corner_transport_active_block_note",
    "pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem_note_2026-04-17",
    "pmns_sigma_zero_nogo_note",
    "pmns_theta23_upper_octant_chamber_closure_prediction_note_2026-04-17",
    "pmns_transfer_operator_dominant_mode_note",
    "publication.ci3_z3.claims_table",
    "publication.ci3_z3.derivation_atlas",
    "publication.ci3_z3.derivation_validation_map",
    "publication.ci3_z3.gravity_publication_package_summary_2026-04-15",
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
    print("AUDIT-PREP VERIFIER — lepton_single_higgs_pmns_triviality_note")
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

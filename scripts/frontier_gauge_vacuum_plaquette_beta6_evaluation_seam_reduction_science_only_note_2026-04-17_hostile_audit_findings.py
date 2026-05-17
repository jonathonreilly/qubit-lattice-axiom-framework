#!/usr/bin/env python3
"""Audit-prep verifier for gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17.

Verifies docs/GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md.

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
PARENT_PATH = REPO_ROOT / "docs/GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17.md"

CITED_DEPS = [
    "gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17",
    "gauge_vacuum_plaquette_first_symmetric_three_sample_current_stack_constraint_boundary_note_2026-04-17",
    "gauge_vacuum_plaquette_first_symmetric_three_sample_exact_radical_reconstruction_map_note_2026-04-17",
    "gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_note_2026-04-17",
    "gauge_vacuum_plaquette_spatial_environment_transfer_underdetermination_note_2026-04-17",
]

NOT_CITED_DEPS = [
    "gauge_vacuum_plaquette_beta6_scalar_value_insufficiency_note_2026-04-17",
    "gauge_vacuum_plaquette_conjugation_symmetric_retained_sampling_reduction_note_2026-04-17",
    "gauge_vacuum_plaquette_first_symmetric_three_sample_reconstruction_note_2026-04-17",
    "gauge_vacuum_plaquette_first_three_sample_local_wilson_partial_evaluation_note_2026-04-17",
    "gauge_vacuum_plaquette_retained_class_sampling_inversion_note_2026-04-17",
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
    print("AUDIT-PREP VERIFIER — gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17")
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

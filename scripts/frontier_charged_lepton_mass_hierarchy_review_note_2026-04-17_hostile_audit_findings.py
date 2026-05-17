#!/usr/bin/env python3
"""Audit-prep verifier for charged_lepton_mass_hierarchy_review_note_2026-04-17.

Verifies docs/CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md.

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
PARENT_PATH = REPO_ROOT / "docs/CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md"

CITED_DEPS = [
    "higher_order_structural_theorems_note",
    "hw1_second_order_return_shape_theorem_note",
    "structural_no_go_survey_note",
]

NOT_CITED_DEPS = [
    "charged_lepton_ue_identity_via_z3_trichotomy_note_2026-04-17",
    "hadron_lane1_sqrt_sigma_retention_gate_audit_support_note_2026-04-27",
    "hadron_mass_lane1_theorem_plan_support_note_2026-04-27",
    "lanes.open_science.03_quark_mass_retention_open_lane_2026-04-26",
    "lepton_single_higgs_pmns_triviality_note",
    "neutrino_dirac_z3_support_trichotomy_note",
    "neutrino_mass_reduction_to_dirac_note",
    "publication.ci3_z3.publication_matrix",
    "quark_lane3_bounded_companion_retention_firewall_note_2026-04-27",
    "yt_bottom_yukawa_retention_analysis_note_2026-04-18",
    "yt_uv_to_ir_transport_obstruction_theorem_note_2026-04-17",
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
    print("AUDIT-PREP VERIFIER — charged_lepton_mass_hierarchy_review_note_2026-04-17")
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

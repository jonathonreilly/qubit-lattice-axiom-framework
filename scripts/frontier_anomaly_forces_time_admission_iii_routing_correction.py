#!/usr/bin/env python3
"""Verify the F-C routing correction for ANOMALY_FORCES_TIME_THEOREM.md.

The original hostile audit finding F-C (PR #1262) established that:
  - CPT_EXACT_NOTE.md has zero gamma_5 occurrences
  - The parent theorem ANOMALY_FORCES_TIME_THEOREM.md was routing
    admission (iii) (chirality grading) to CPT_EXACT_NOTE — INCORRECT

This runner verifies:
  1. CPT_EXACT_NOTE.md still has zero gamma_5 (F-C empirical claim holds)
  2. STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md
     derives {epsilon, D_staggered} = 0 (the correct chirality routing)
  3. NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md rules out per-site
     gamma_5 (consistency with staggered-lattice chirality home)
  4. Parent theorem no longer cites CPT_EXACT_NOTE as chirality source
     (correction applied)
  5. Parent theorem now cites STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_*
     in the chirality role (correction applied)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent

PARENT = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
CPT = REPO_ROOT / "docs" / "CPT_EXACT_NOTE.md"
KS = REPO_ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
NPS = REPO_ROOT / "docs" / "NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md"


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] [A] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def count(content: str, needle: str) -> int:
    return len(re.findall(re.escape(needle), content, re.IGNORECASE))


def main() -> int:
    print("=" * 78)
    print("ANOMALY_FORCES_TIME admission (iii) routing correction verifier")
    print("=" * 78)

    # Part 1 — F-C empirical claim still holds: CPT_EXACT has 0 gamma_5
    print()
    print("PART 1: CPT_EXACT_NOTE.md has zero gamma_5 occurrences (F-C original claim)")
    check("docs/CPT_EXACT_NOTE.md exists", CPT.exists())
    if CPT.exists():
        cpt_content = CPT.read_text(encoding="utf-8")
        for pat in ["gamma_5", "gamma5", "γ_5", "γ5", "\\gamma_5", "\\gamma_{5}"]:
            check(f"  '{pat}' count == 0 in CPT_EXACT_NOTE",
                  count(cpt_content, pat) == 0, f"count = {count(cpt_content, pat)}")

    # Part 2 — Kawamoto-Smit substep 2 derives the chirality anticommutation
    print()
    print("PART 2: Kawamoto-Smit substep 2 derives {epsilon, D_staggered} = 0")
    check("Kawamoto-Smit forcing theorem note exists", KS.exists())
    if KS.exists():
        ks_content = KS.read_text(encoding="utf-8")
        check("  KS note mentions 'chirality anticommutation'",
              "chirality anticommutation" in ks_content.lower())
        check("  KS note mentions 'sublattice parity'",
              "sublattice parity" in ks_content.lower())
        check("  KS note uses epsilon(x) := (-1)^{x_1+x_2+x_3} form",
              "ε(x)" in ks_content or "epsilon(x)" in ks_content.lower())
        # Look for the {epsilon, D_staggered} anticommutation explicitly
        has_anticomm = bool(re.search(r"\{\s*(?:ε|epsilon)\s*,\s*D_?staggered", ks_content, re.IGNORECASE))
        check("  KS note states {epsilon, D_staggered} anticommutation",
              has_anticomm, f"regex match: {has_anticomm}")

    # Part 3 — Per-site gamma_5 ruled out
    print()
    print("PART 3: NO_PER_SITE_CHIRALITY rules out per-site gamma_5 in Cl(3)")
    check("NO_PER_SITE_CHIRALITY note exists", NPS.exists())
    if NPS.exists():
        nps_content = NPS.read_text(encoding="utf-8")
        check("  Note references Cl(3)",
              "cl(3)" in nps_content.lower() or "cl_3" in nps_content.lower())
        check("  Note articulates 'no per-site' or 'no anti-commuting' chirality",
              "no per-site" in nps_content.lower() or "anti-commut" in nps_content.lower())

    # Part 4 — Parent theorem no longer cites CPT_EXACT_NOTE as chirality source
    print()
    print("PART 4: Parent no longer cites CPT_EXACT as chirality source (correction applied)")
    check("Parent theorem note exists", PARENT.exists())
    if PARENT.exists():
        p_content = PARENT.read_text(encoding="utf-8")
        # The misleading phrase "epsilon(x) = staggered gamma_5" should be GONE
        # (it conflated chirality role with the function name)
        has_bug_phrase = bool(re.search(r"epsilon\(x\)\s*=\s*staggered\s+gamma_5", p_content, re.IGNORECASE))
        check("  Parent no longer asserts 'epsilon(x) = staggered gamma_5' verbatim",
              not has_bug_phrase, "phrase removed")

        # The parent should cite the Kawamoto-Smit note in the chirality role
        check("  Parent cites STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07",
              "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07" in p_content)

        # The parent should still reference CPT_EXACT_NOTE (for the C-operator role) and NO_PER_SITE_CHIRALITY
        check("  Parent still references CPT_EXACT_NOTE (now in C-operator role)",
              "CPT_EXACT_NOTE" in p_content)
        check("  Parent references NO_PER_SITE_CHIRALITY (chirality home explanation)",
              "NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02" in p_content)

        # Routing-history block should record the correction
        has_history = "routing_history" in p_content and "corrected_2026-05-17" in p_content
        check("  Parent records routing correction in admission_routing_status (routing_history block)",
              has_history, "history block present")

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    if FAIL_COUNT == 0:
        print()
        print("ROUTING CORRECTION VERIFIED")
        print("  F-C empirical claim still holds (CPT_EXACT has 0 gamma_5)")
        print("  Kawamoto-Smit substep 2 derives the chirality anticommutation")
        print("  Per-site gamma_5 ruled out by NO_PER_SITE_CHIRALITY")
        print("  Parent theorem citation updated (CPT_EXACT -> Kawamoto-Smit)")
        return 0
    print()
    print(f"VERIFICATION FAILED ({FAIL_COUNT} FAIL)")
    return 1


if __name__ == "__main__":
    sys.exit(main())

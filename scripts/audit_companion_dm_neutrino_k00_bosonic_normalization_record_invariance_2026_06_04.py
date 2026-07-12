#!/usr/bin/env python3
"""Synchronize the historical K00 Record-invariance companion.

The old companion asserted that the former positive parent did not use Record
content.  The live parent now uses the minimal-axiom scope as a nonsupply guard,
so this meta runner retires the stale invariance evidence and checks only the
new parent's source/runner boundary.  It does not make a physics claim.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = ROOT / "docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md"
PARENT_RUNNER = ROOT / "scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py"
COMPANION_NOTE = ROOT / "docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def main() -> int:
    print("=" * 72)
    print("DM neutrino K00 historical Record-invariance companion retirement hygiene")
    print("=" * 72)
    print("Scope: meta sibling synchronization; no theorem and no verdict change.")

    check("parent_note_exists", PARENT_NOTE.is_file())
    check("parent_runner_exists", PARENT_RUNNER.is_file())
    check("companion_note_exists", COMPANION_NOTE.is_file())

    parent = PARENT_NOTE.read_text(encoding="utf-8")
    check("parent_claim_type_is_no_go", "claim_type_author_hint: no_go" in parent)
    check("parent_keeps_audit_authority_external", "status_authority: independent_audit_lane_only" in parent)
    check("parent_preserves_kmass_projection_identity", "K00 = (K_mass)00" in parent)
    check("parent_derives_general_response_law", "K00 = c tau_+" in parent)
    check("parent_contains_embedding_countermodel", "c = 1" in parent and "c = 2" in parent)
    check("parent_contains_source_magnitude_countermodel", "tau_+ = 1/2" in parent and "tau_+ = 1" in parent)
    check("parent_contains_positive_falsifier", "Falsifier and exact repair target" in parent)
    check(
        "parent_links_all_approved_premise_sources",
        all(
            name in parent
            for name in (
                "MINIMAL_AXIOMS_2026-06-29.md",
                "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
                "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
                "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
            )
        ),
    )

    completed = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    check("parent_runner_exit_zero", completed.returncode == 0, f"returncode={completed.returncode}")
    match = re.search(r"SUMMARY:\s+PASS=(\d+)\s+FAIL=(\d+)", completed.stdout)
    check("parent_runner_summary_present", match is not None)
    check(
        "parent_runner_summary_current",
        match is not None and match.groups() == ("16", "0"),
        match.group(0) if match else "missing",
    )
    check(
        "parent_runner_reports_scoped_negative_boundary",
        "exact negative boundary on the restricted packet" in completed.stdout,
    )

    companion = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    check("companion_declares_meta_type", "**type:** meta" in companion)
    check("companion_retires_old_evidence", "retired as evidence" in companion)
    check("companion_disclaims_current_record_invariance", "does not claim current record invariance" in companion)
    check("companion_disclaims_new_theorem", "does not claim a new theorem" in companion)
    check("companion_disclaims_verdict", "does not set or predict an audit verdict" in companion)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

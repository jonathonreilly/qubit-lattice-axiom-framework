#!/usr/bin/env python3
"""Verifier for RP_TWO_STEP_DISCHARGE_VIA_C2_TIGHTENING_COMPANION_LINK_NOTE_2026-06-03.

This is a meta-scope ledger-pairing verifier, not a physics theorem runner.
It checks that the companion-link note stays inside its declared boundaries
and that the cross-referenced parent + companion (both on `origin/main`) are
actually present with the cited statuses.

Sections:
  A. Parent presence + audited_conditional status on origin/main.
  B. Companion presence on origin/main with paired runner + cache exit 0.
  C. C2-tightening statement in companion matches parent's named discharge
     re-audit instruction.
  D. Hostile-audit invariants: this note does not modify the parent or
     companion text, does not lift status, asserts no new science.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

PASS = 0
FAIL = 0


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "RP_TWO_STEP_DISCHARGE_VIA_C2_TIGHTENING_COMPANION_LINK_NOTE_2026-06-03.md"
)
PARENT_NOTE_REL = "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
COMPANION_NOTE_REL = (
    "docs/RP_TWO_STEP_TRANSFER_MATRIX_SINGULAR_MODE_C2_TIGHTENING_NOTE_2026-06-02.md"
)
COMPANION_RUNNER_REL = (
    "scripts/frontier_rp_two_step_transfer_matrix_singular_mode_c2_tightening_2026_06_02.py"
)
COMPANION_CACHE_REL = (
    "logs/runner-cache/"
    "frontier_rp_two_step_transfer_matrix_singular_mode_c2_tightening_2026_06_02.txt"
)
LEDGER_REL = "docs/audit/data/audit_ledger.json"

PARENT_LEDGER_ID = "axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28"
COMPANION_LEDGER_ID = (
    "rp_two_step_transfer_matrix_singular_mode_c2_tightening_note_2026-06-02"
)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def git_show(rel: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"origin/main:{rel}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    return result.stdout if result.returncode == 0 else None


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")

    # ------------------------------------------------------------------ A
    parent_text = git_show(PARENT_NOTE_REL)
    check("A1 parent note exists on origin/main", parent_text is not None)
    ledger_text = git_show(LEDGER_REL)
    check("A2 ledger exists on origin/main", ledger_text is not None)
    parent_row = {}
    if ledger_text:
        try:
            data = json.loads(ledger_text)
            parent_row = data.get("rows", {}).get(PARENT_LEDGER_ID, {})
        except json.JSONDecodeError:
            parent_row = {}
    check(
        "A3 parent row present in ledger",
        bool(parent_row),
        detail=f"id={PARENT_LEDGER_ID}",
    )
    check(
        "A4 parent effective_status = audited_conditional",
        parent_row.get("effective_status") == "audited_conditional",
        detail=str(parent_row.get("effective_status")),
    )
    check(
        "A5 parent audit_status = audited_conditional",
        parent_row.get("audit_status") == "audited_conditional",
        detail=str(parent_row.get("audit_status")),
    )
    notes_for_re_audit = (parent_row.get("notes_for_re_audit_if_any") or "")
    check(
        "A6 parent re-audit instruction names C2 tightening",
        "C2" in notes_for_re_audit
        and "sin(p)" in notes_for_re_audit
        and "real-spectrum" in notes_for_re_audit,
        detail="auditor names sin(p) != 0 tightening",
    )

    # ------------------------------------------------------------------ B
    companion_text = git_show(COMPANION_NOTE_REL)
    check("B1 companion note exists on origin/main", companion_text is not None)
    companion_runner = git_show(COMPANION_RUNNER_REL)
    check(
        "B2 companion runner exists on origin/main",
        companion_runner is not None,
    )
    companion_cache = git_show(COMPANION_CACHE_REL)
    check(
        "B3 companion cache exists on origin/main",
        companion_cache is not None,
    )
    check(
        "B4 companion cache exit_code: 0",
        bool(companion_cache and "exit_code: 0" in companion_cache),
    )
    check(
        "B5 companion cache scorecard PASS=20 FAIL=0",
        bool(companion_cache and "PASS=20" in companion_cache and "FAIL=0" in companion_cache),
    )
    companion_row = {}
    if ledger_text:
        try:
            data = json.loads(ledger_text)
            companion_row = data.get("rows", {}).get(COMPANION_LEDGER_ID, {})
        except json.JSONDecodeError:
            companion_row = {}
    check(
        "B6 companion row present in ledger",
        bool(companion_row),
        detail=f"id={COMPANION_LEDGER_ID}",
    )

    # ------------------------------------------------------------------ C
    check(
        "C1 companion claims sin(p)=0 singular-mode case",
        bool(companion_text and "sin(p)" in companion_text and "singular" in companion_text.lower()),
    )
    check(
        "C2 companion proves one-step indefinite at singular modes",
        bool(
            companion_text
            and "one-step matrix is" in companion_text
            and "indefinite" in companion_text
        ),
    )
    check(
        "C3 companion proves two-step square non-negative",
        bool(
            companion_text
            and "two-step" in companion_text
            and "non-negative" in companion_text
        ),
    )
    check(
        "C4 companion declares itself conditional algebraic companion to parent",
        bool(
            companion_text
            and "conditional algebraic companion" in companion_text
            and "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28"
            in companion_text
        ),
    )
    # Auditor's named discharge route: "real-spectrum exceptional modes are
    # still non-positive [in one-step]." Companion's one-step indefiniteness
    # (lambda_- < -1) covers this; the two-step non-negativity covers the
    # consistency with the parent's two-step claim. The note text in this PR
    # has to cite both halves explicitly.
    check(
        "C5 this note quotes the auditor's discharge instruction",
        "tighten the C2 p != 0 statement to sin(p) != 0" in text,
    )
    check(
        "C6 this note names parent ledger id",
        PARENT_LEDGER_ID in text,
    )
    check(
        "C7 this note names companion ledger id",
        COMPANION_LEDGER_ID in text,
    )

    # ------------------------------------------------------------------ D
    check("D1 note exists locally", NOTE.is_file())
    check("D2 claim_type is meta", "**Claim type:** meta" in text)
    check("D3 explicitly authors no audit verdict", "no audit verdict" in text)
    check(
        "D4 explicitly does not modify parent text",
        "modify the parent text" in text or "modify the parent note" in text,
    )
    check(
        "D5 explicitly does not modify companion text",
        "modify the companion text" in text or "modify the companion note" in text,
    )
    check(
        "D6 explicitly does not lift status",
        "does not lift any" in text
        or "does not assert a status lift" in text
        or "does not\nlift" in text,
    )
    check(
        "D7 does not hand-author retained/clean status",
        "retained_bounded" not in text and "audited_clean" not in text,
    )
    check(
        "D8 no PDG / external comparator import",
        "PDG" not in text and "Particle Data Group" not in text,
    )
    check(
        "D9 no new axiom or primitive",
        "no axiom" in text and "no theorem" in text,
    )

    # Precedent notes exist on origin/main
    precedents = [
        "docs/PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md",
        "docs/CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md",
        "docs/RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md",
    ]
    for rel in precedents:
        present = git_show(rel) is not None
        check(f"precedent on origin/main: {Path(rel).name}", present)

    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

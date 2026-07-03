#!/usr/bin/env python3
"""Paired runner for RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md

Verifies (text checks only, no verdicts):
  [NOTE] the note carries the proposal disclaimers and the H1-H4 clauses;
  [C1]   the four named field-content-pin instances currently contain the
         described pin pattern (reads audit_ledger.json AND asserts
         load_bearing_step_class equality);
  [C2]   the named exact-state-pin instance currently asserts the exact
         status strings the note describes;
  [EX]   the named compliant exemplars currently use the membership form /
         documented tier-exact form;
  [CEN]  a census scan of scripts/ for ledger-reading runners with equality
         pins contains the named instances (census printed as context; the
         count itself is NOT pinned, per the note's own H4).

Deterministic, no randomness, seconds. Exits non-zero on any FAIL.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    verdict = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}] {verdict}: {label}{suffix}")


def src(rel: str) -> str:
    p = ROOT / rel
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return ""


C1_INSTANCES = [
    "scripts/frontier_thales_right_angle_narrow.py",
    "scripts/frontier_half_plane_chart_equivalence_narrow.py",
    "scripts/frontier_ckm_magnitudes_structural_counts_narrow.py",
    "scripts/frontier_z3_conjugate_support_trichotomy_narrow.py",
]
C2_INSTANCE = "scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py"
EX_MEMBERSHIP = "scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py"
EX_TIER_EXACT = "scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py"
EX_REALIGNED = "scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py"

READS_LEDGER = re.compile(r"audit_ledger\.json|ledger_status")
EQ_PIN = re.compile(
    r"""load_bearing_step_class\s*.\s*\)?\s*==   # field-content equality
      | ==\s*["'](?:retained|retained_bounded|retained_no_go
                  |unaudited|audited_conditional|open_gate)["']
      | \{\s*["']retained["']\s*\}               # single-tier set pin
    """,
    re.X,
)


def main() -> int:
    print("runner ledger-field pin hygiene convention check (2026-07-02)")
    note = NOTE.read_text(encoding="utf-8")

    # [NOTE] proposal disclaimers and clauses
    for phrase in [
        "**Type:** meta",
        "**Claim type:** meta",
        "does not\nset or predict an audit outcome",
        "Convention adoption is audit-decided",
        "(H1) No equality pins on audit-authored field content",
        "(H2) Status freshness checks use the retained-grade membership set",
        "(H3) Report-only ledger reads are unrestricted",
        "(H4) Ledger-census snapshots need a maintenance pattern",
        "Sets, promotes, or changes **no** row's effective status",
        "a question to the owner\nor a landed PR is not adoption",
    ]:
        check("NOTE", f"note contains: {phrase.splitlines()[0]}",
              re.search(r"\s+".join(re.escape(w) for w in phrase.split()), note) is not None)

    # [C1] the four named field-content-pin instances
    for rel in C1_INSTANCES:
        text = src(rel)
        ok = (
            bool(text)
            and READS_LEDGER.search(text) is not None
            and "load_bearing_step_class" in text
            and re.search(r"load_bearing_step_class.\)\s*==\s*.A.", text) is not None
        )
        check("C1", f"named field-content pin present in {rel}", ok)
        check("C1", f"note names the instance {rel}", rel.split("/")[-1] in note)

    # [C2] the named exact-state-pin instance
    text = src(C2_INSTANCE)
    check("C2", "extensivity runner pins an exact open_gate state",
          '== "open_gate"' in text and READS_LEDGER.search(text) is not None)
    check("C2", "extensivity runner pins an exact audited_conditional state",
          '== "audited_conditional"' in text)
    check("C2", "note names the exact-state instance",
          C2_INSTANCE.split("/")[-1] in note)

    # [EX] compliant exemplars
    text = src(EX_MEMBERSHIP)
    check("EX", "lh_doublet companion uses the retained-grade membership set",
          'retained_grades = {"retained", "retained_bounded", "retained_no_go"}' in text
          and "in retained_grades" in text)
    text = src(EX_TIER_EXACT)
    check("EX", "GL(F) selection check is the documented tier-exact case",
          '== "retained_bounded"' in text)
    text = src(EX_REALIGNED)
    check("EX", "dirac_weyl companion carries the realigned retained-grade set",
          '"retained_bounded"' in text and '"retained"' in text)

    # [CEN] census: ledger-reading scripts with equality pins (context print)
    census = []
    for p in sorted((ROOT / "scripts").glob("*.py")):
        if p.name == Path(__file__).name:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if READS_LEDGER.search(text) and EQ_PIN.search(text):
            census.append(f"scripts/{p.name}")
    print(f"  census: {len(census)} ledger-reading scripts with equality-pin patterns (context, not pinned)")
    for rel in census[:40]:
        print(f"    - {rel}")
    if len(census) > 40:
        print(f"    ... and {len(census) - 40} more")
    named = set(C1_INSTANCES) | {C2_INSTANCE}
    missing = sorted(named - set(census))
    check("CEN", "every named instance appears in the live census",
          not missing, "missing: " + ", ".join(missing) if missing else "")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

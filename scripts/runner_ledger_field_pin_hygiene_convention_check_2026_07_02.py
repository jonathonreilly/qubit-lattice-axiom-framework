#!/usr/bin/env python3
"""Paired runner for RUNNER_LEDGER_FIELD_PIN_HYGIENE_CONVENTION_PROPOSAL_NOTE_2026-07-02.md

Verifies (text checks only, no verdicts):
  [NOTE] the note carries the proposal disclaimers and the H1-H4 clauses;
  [C1]   each named field-content-pin instance is in a state the note
         documents -- still pinning (reads the ledger AND asserts
         load_bearing_step_class equality), or narrowed per section 4 to a
         report-only read;
  [C2]   the named exact-state-pin instance is likewise in a documented
         state (exact-state pins, or narrowed);
  [EX]   the named compliant exemplars are in a state the note records;
  [CEN]  every named instance is accounted for against a live census scan of
         scripts/ (census printed as context; the count itself is NOT pinned,
         per the note's own H4).

The C1/C2/EX checks assert documented STATES rather than one frozen literal:
a runner pinning another file's current text goes stale by construction in
exactly the way the note says a ledger-field pin does -- which is how the
2026-07-02 tier-exact exemplar pin died when that file was rewritten on
2026-07-16. Accepting either documented state also keeps this runner from
freezing the named instances against section 4's own remediation path.

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
    # named from the proposal-time sweep
    "scripts/frontier_thales_right_angle_narrow.py",
    "scripts/frontier_half_plane_chart_equivalence_narrow.py",
    "scripts/frontier_ckm_magnitudes_structural_counts_narrow.py",
    "scripts/frontier_z3_conjugate_support_trichotomy_narrow.py",
    # added by the 2026-07-24 re-measurement of the same pattern
    "scripts/audit_companion_ckm_bernoulli_two_ninths_exact.py",
    "scripts/audit_companion_dm_neutrino_cascade_geometry_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_character_exact.py",
    "scripts/audit_companion_dm_neutrino_z3_circulant_nogo_exact.py",
    "scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py",
]
C2_INSTANCE = "scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py"
EX_MEMBERSHIP = "scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py"
EX_TIER_EXACT = "scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py"
EX_REALIGNED = "scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py"

READS_LEDGER = re.compile(r"audit_ledger\.json|ledger_status")
FIELD_PIN = re.compile(r"load_bearing_step_class.\)\s*==\s*.A.")
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

    # [C1] named field-content-pin instances, in either documented state.
    # Per the note's section 4 these get narrowed to report-only prints in
    # follow-up repair PRs, so pinning "still pins" here would freeze the class
    # against its own remediation path. Passing states: "pins" (as described)
    # and "narrowed" (field read, no equality pin). A file that vanished, or
    # that stopped handling the field entirely, is not a documented state.
    states = {}
    for rel in C1_INSTANCES:
        text = src(rel)
        base = rel.split("/")[-1]
        if not text:
            state = "gone"
        elif FIELD_PIN.search(text) and READS_LEDGER.search(text):
            state = "pins"
        elif "load_bearing_step_class" in text:
            state = "narrowed"
        else:
            state = "unhandled"
        states[rel] = state
        named = base in note
        why = state if state in ("pins", "narrowed") else f"UNDOCUMENTED STATE {state}"
        if not named:
            why += "; NOT NAMED IN NOTE"
        check("C1", base, state in ("pins", "narrowed") and named, why)
    tally = {s: sum(1 for v in states.values() if v == s) for s in sorted(set(states.values()))}
    print(f"  C1 states: {tally}")

    # [C2] the named exact-state-pin instance, in either documented state
    # (section 4 narrows it to membership checks or a justified exception).
    text = src(C2_INSTANCE)
    if not text:
        c2_state = "gone"
    elif '== "open_gate"' in text or '== "audited_conditional"' in text:
        c2_state = "exact-state pins, as named in 2026-07-02"
    else:
        c2_state = "narrowed (no exact non-retained pin)"
    check("C2", "extensivity runner state + named in note",
          c2_state != "gone" and C2_INSTANCE.split("/")[-1] in note, c2_state)

    # [EX] compliant exemplars
    text = src(EX_MEMBERSHIP)
    check("EX", "lh_doublet companion uses the retained-grade membership set",
          'retained_grades = {"retained", "retained_bounded", "retained_no_go"}' in text
          and "in retained_grades" in text)
    # The 2026-07-02 tier-exact exemplar was rewritten on 2026-07-16 and its
    # ledger reads removed, so the note records both states rather than the
    # literal that happened to hold when it was written.
    text = src(EX_TIER_EXACT)
    if not text:
        state = "gone"
    elif '== "retained_bounded"' in text:
        state = "tier-exact pin, as named in 2026-07-02"
    elif READS_LEDGER.search(text) is None:
        state = "no ledger read (repaired 2026-07-16)"
    else:
        state = "UNDOCUMENTED: reads ledger, no tier-exact pin"
    check("EX", "staggered substep-1 check is in a state the note records",
          state.startswith(("tier-exact", "no ledger")), state)
    text = src(EX_REALIGNED)
    check("EX", "dirac_weyl companion carries the realigned retained-grade set",
          '"retained_bounded"' in text and '"retained"' in text)

    # [CEN] census: ledger-reading scripts with equality pins (context print).
    # Per (H4) the count is printed, never pinned. The per-file listing is
    # omitted: the C1 inventory above names the field-content-pin members,
    # which is the subpopulation the note's section 1 is about.
    census = []
    field_pins = 0
    for p in sorted((ROOT / "scripts").glob("*.py")):
        if p.name == Path(__file__).name:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if READS_LEDGER.search(text) and EQ_PIN.search(text):
            census.append(f"scripts/{p.name}")
            if FIELD_PIN.search(text):
                field_pins += 1
    print(f"  census: {len(census)} ledger-reading scripts with equality-pin patterns; "
          f"{field_pins} carry the load_bearing_step_class field pin (context, not pinned)")
    # A named instance LEAVES this census when section 4 narrows it, so the
    # invariant is accounted-for, not present: either still in the census, or
    # still on disk with the pin removed. Only a vanished file is unaccounted.
    unaccounted = sorted(rel for rel in set(C1_INSTANCES) | {C2_INSTANCE}
                         if rel not in census and not src(rel))
    check("CEN", "every named instance accounted for (in census, or narrowed on disk)",
          not unaccounted, "unaccounted: " + ", ".join(unaccounted) if unaccounted else "")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

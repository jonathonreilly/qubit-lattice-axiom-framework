# Runner Ledger-Field Pin Hygiene — Convention Proposal

**Date:** 2026-07-02
**Type:** meta
**Claim type:** meta
**Status:** metadata proposal only; no theorem content or promotion. This
source does not set or predict an audit outcome. The independent audit lane
determines whether the convention is adopted, and the pipeline derives any
downstream status after that review.
**Primary runner:** [`scripts/runner_ledger_field_pin_hygiene_convention_check_2026_07_02.py`](../scripts/runner_ledger_field_pin_hygiene_convention_check_2026_07_02.py)
**Cached output:** [`logs/runner-cache/runner_ledger_field_pin_hygiene_convention_check_2026_07_02.txt`](../logs/runner-cache/runner_ledger_field_pin_hygiene_convention_check_2026_07_02.txt)

## 1. The observed failure class

A 2026-07-02 repo-wide sweep re-executed 1249 sibling-reading runners whose
caches in `logs/runner-cache/` were green and found 182 that fail on live
execution ("stale-green": the cache says PASS while the current tree does
not). A recurring mechanical cause is runners asserting **equality between
hard-coded literals and audit-lane-owned ledger data** — fields that the
independent audit lane rewrites at every re-audit, so the pin goes stale by
construction, silently, behind a green cache:

- **Field-content pins.** Runners asserting the verbatim content of
  audit-authored row fields (`load_bearing_step`, `load_bearing_step_class`,
  verdict/rationale text). Instances named from the proposal-time sweep:
  - `scripts/frontier_thales_right_angle_narrow.py`
  - `scripts/frontier_half_plane_chart_equivalence_narrow.py`
  - `scripts/frontier_ckm_magnitudes_structural_counts_narrow.py`
  - `scripts/frontier_z3_conjugate_support_trichotomy_narrow.py`
  (each reads `docs/audit/data/audit_ledger.json` and asserts
  `load_bearing_step_class == 'A'` for its parent row; all four failed the
  sweep after audit-side field updates while their rows remained retained).

  A 2026-07-24 re-measurement of the same pattern over `scripts/` finds nine
  runners carrying it, so the proposal-time list named four of nine. The other
  five follow the identical shape — read the ledger, assert
  `load_bearing_step_class == 'A'` for their own parent row:
  - `scripts/audit_companion_ckm_bernoulli_two_ninths_exact.py`
  - `scripts/audit_companion_dm_neutrino_cascade_geometry_exact.py`
  - `scripts/audit_companion_dm_neutrino_z3_character_exact.py`
  - `scripts/audit_companion_dm_neutrino_z3_circulant_nogo_exact.py`
  - `scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py`

  Checked against the repo state at the end of 2026-07-02 (commit
  `952647de06`), all nine already carried the pin then: the class did not grow
  after the proposal, the proposal-time listing was a partial selection from it.
- **Exact-tier / exact-state status pins.** Runners asserting one exact
  status string, including non-retained transition states. Instance:
  `scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py`
  asserts a dependency row `== "open_gate"` and a parent row
  `== "audited_conditional"` — so any audit-lane movement of either row,
  including a repair the framework wants, turns the runner red.

## 2. Proposed convention

- **(H1) No equality pins on audit-authored field content.** A source or
  companion runner must not assert equality between a hard-coded literal and
  audit-lane-owned row-field content (`load_bearing_step`,
  `load_bearing_step_class`, verdict rationale, re-audit notes, auditor
  metadata). Reading and PRINTING such fields as context is always
  permitted.
- **(H2) Status freshness checks use the retained-grade membership set.** A
  runner that needs a dependency to be retained-grade at run time asserts
  membership in `{"retained", "retained_bounded", "retained_no_go"}` rather
  than one exact tier. Asserting one exact tier (or a non-retained state) is
  permitted only when tier-exactness is itself load-bearing for the row's
  claim and the paired note says why.
- **(H3) Report-only ledger reads are unrestricted.** Printing statuses,
  counts, or fields for the reader carries no pin and is encouraged where it
  helps the auditor.
- **(H4) Ledger-census snapshots need a maintenance pattern.** Checks that
  equality-pin counts computed from ledger rows (bucket censuses) re-stale
  with every audit commit; lanes that keep them accept periodic re-snapshot
  maintenance, and SHOULD prefer structural invariants (partition sums,
  named-bucket presence, printed census) where the row's claim does not
  depend on the exact count.

## 3. Compliant exemplars already on main

- `scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py`
  uses the (H2) membership form
  (`retained_grades = {"retained", "retained_bounded", "retained_no_go"}`);
  when it runs red, that is the freshness contract working during a
  dependency's transition window, not a defect.
- `scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py`
  was named here on 2026-07-02 as the tier-exact case, its packet expectation
  being `== "retained_bounded"`. That runner was rewritten on 2026-07-16
  (commit `03ca2d51f4`), which removed its ledger reads entirely: it now
  asserts no status at all, so it is (H1)/(H2)-compliant by containing no pin
  rather than by taking the exception path. No live runner is named here as an
  exception-path exemplar. The (H2) exception is a clause of the convention,
  not a claim about the current contents of `scripts/`; a runner takes it by
  pinning one tier with its own note saying why, and the audit lane judges
  that pairing when such a row is reviewed.

  This bullet is also the note's own worked example of §1. From that rewrite
  until this repair the paired runner asserted the pre-rewrite literal and
  failed on live execution while its cached output stayed green — a runner
  pinning another file's internal text goes stale by construction in exactly
  the way a runner pinning ledger-field content does. The checks below are
  written to accept either documented state of a named instance rather than
  freezing the one that happened to hold when the note was written.
- `scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py`
  was realigned to the membership form in the 2026-07-02 repair wave after
  its `{"retained"}`-only pin went stale against a retained-grade tier move.

## 4. Remediation path (proposed, not executed here)

If this convention is adopted, the named Section-1 instances get narrowed in
follow-up repair PRs: the field-content pins move their
`load_bearing_step_class` assertions to report-only prints, and the
exact-state pins in the extensivity runner become either retained-grade
membership checks or note-documented justified exceptions. This note edits
no runner and proposes no wording for those rows' notes.

## 5. Declared boundaries

- Proposes a repo-workflow convention only; no physics claim, no theorem, no
  derivation content, and no new admitted-context input.
- Sets, promotes, or changes **no** row's effective status; does not edit
  audit-lane data; does not modify any named runner.
- Neither a question to the owner nor landing this note adopts the convention;
  adoption follows only from independent audit-lane review.
- The named-instance lists describe the proposal-time sweep plus the
  2026-07-24 re-measurement, and are verified by the paired runner; they are
  illustrative of the class, not an enumeration bound on it (the runner prints
  the current census size). A name appearing here is not a claim that the
  instance is still unrepaired: the runner accepts a named instance in either
  documented state — still pinning, or narrowed per §4 — and fails only if the
  file stops handling the field, so a §4 repair landing in a later PR does not
  require an edit to this note.

## 6. Command and expected output

```bash
python3 scripts/runner_ledger_field_pin_hygiene_convention_check_2026_07_02.py
```

Deterministic, < 5 s, syntax-aware text checks only. The runner also exercises
the production source-state classifier against ten synthetic positive and
adverse controls. Expected: `[NOTE]/[C1]/[C2]/[EX]/[CTL]/[CEN]`-tagged PASS
lines and the final line `TOTAL: PASS=N FAIL=0`.

The paired cache fingerprint binds this note and every named C1/C2/EX source.
The repo-wide census count is deliberately contextual rather than
load-bearing; it is recomputed on every live run and is not itself a cache
freshness assertion.

```yaml
claim_type_author_hint: meta
claim_scope: "Repo-workflow convention proposal: companion/source runners must not equality-pin audit-lane-owned ledger field content (H1); run-time dependency-freshness checks use the retained-grade membership set with a note-documented exception path for load-bearing tier-exactness (H2); report-only ledger reads are unrestricted (H3); ledger-census count pins require an owned maintenance pattern and should prefer structural invariants (H4). Named live instances and compliant exemplars are verified by the paired runner; adoption is audit-decided."
upstream_dependencies: []
admitted_context_inputs: []
```

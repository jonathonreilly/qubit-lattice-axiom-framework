# YT Microscopic Schur-Class Admissibility: Criticality-Bump Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / criticality-bump readiness evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent's substance and runner output are unchanged since the prior
`audited_clean` verdict that was invalidated by a criticality bump. It
is not a new theorem claim, not a status promotion, and not a re-audit.
If the audit pipeline seeds this file, it is a meta companion row; the
audit lane still sets `audit_status`, and pipeline-derived
`effective_status` remains downstream of that authority.
**Companion target:** `yt_microscopic_schur_class_admissibility_note`
(parent note
[`docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md`](YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md)).
**Primary companion runner:**
[`scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py`](../scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt)

---

## Why this companion exists

The parent bounded theorem
`yt_microscopic_schur_class_admissibility_note` was previously
audit-loop-resolved on 2026-05-01 as `audited_clean`
(`bounded_theorem`, class C, chain_closes=true) by
`auditor_family=codex-gpt-5` with `auditor_confidence=high` and
`independence=cross_family`. The recorded verdict's scope (verbatim
from the archived `previous_audits[]` entry):

> Within the current tested microscopic locality tube, every surviving
> exact Schur reduction in the constructed local positive family lands
> in the same Schur normal-form class and stays inside the conservative
> endpoint budget.

The recorded `verdict_rationale` reads:

> The bounded claim closes for the current finite tested-scale package:
> the runner performs the Schur reductions from constructed microscopic
> operators rather than hard-coding the conclusion, and all five checks
> pass with max response gap 5.144895e-03 below the 1.214751e-02
> budget. Residual risk is scoped, not hidden: the audit does not
> certify zero endpoint budget, unbounded y_t, or all conceivable
> microscopic realizations outside the tested locality tube.

That `audited_clean` snapshot was archived
(`archived_at=2026-05-04T15:35:10`) under
`invalidation_reason=criticality_increased:medium->critical`. The row
is currently `effective_status=unaudited` (reason `awaiting_audit`) and
sits at `criticality=medium` (same as at the original clean audit) with
`load_bearing_score=6.615` (up from `5.587` at the clean audit). A
subsequent fresh-context audit at `criticality=critical` (Audit 2 in
`previous_audits[]`, 2026-05-05, `codex-gpt-5.5`) was recorded as
`audited_conditional` on the basis of unprovided cited authorities for
the two upstream dependency notes; that conditional verdict was itself
later invalidated by note-hash drift before the parent settled to its
current text.

This companion records, for the audit lane, the narrow auditable
observations that:

1. the parent's note text (`note_hash`) is exactly the
   `b35c7d4f431d3ecabc3098a4266bf7c9aa901cf2be1e3c989b62a1519fc21956`
   value currently in `audit_ledger.json` — the substance is what the
   ledger reflects;
2. the parent's primary runner
   `scripts/frontier_yt_microscopic_schur_class_admissibility.py` still
   exits 0 with `5 PASS / 0 FAIL` and the same `max response gap
   5.144895e-03` and `conservative budget 1.214751e-02` reported in the
   archived clean rationale — the numerics underlying the prior clean
   verdict are reproducible;
3. the parent's currently registered `deps[]` array
   (`yt_exact_coarse_grained_bridge_operator_note`,
   `yt_exact_schur_normal_form_uniqueness_note`) matches the runner's
   actual one-hop imports
   (`scripts.frontier_yt_exact_coarse_grained_bridge_operator`,
   `scripts.frontier_yt_exact_schur_normal_form_uniqueness`) — the
   dependency edges named by the later conditional auditor are now
   wired;
4. the parent's `criticality` is currently `medium`, the same value
   under which the prior clean verdict was issued (the original
   criticality-bump trigger to `critical` was the invalidation event
   that archived that clean audit, but the row has since returned to
   `medium`).

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the criticality-bump
invalidation event. It is not a re-audit and does not promote status;
it documents reproducibility and the dependency-edge wiring in
machine-checkable form so the audit lane can decide whether to honor
or re-test the prior judicial verdict.

---

## Scope and boundary

This companion makes a narrow set of auditable observations:

**(C1) Note-hash stability.** The parent's current note hash matches
the `note_hash` value recorded in
[`docs/audit/data/audit_ledger.json`](audit/data/audit_ledger.json) for
the row `yt_microscopic_schur_class_admissibility_note`. The substance
that the prior clean verdict reviewed is the substance now on disk.

**(C2) Runner reproducibility.** The parent's primary runner
[`scripts/frontier_yt_microscopic_schur_class_admissibility.py`](../scripts/frontier_yt_microscopic_schur_class_admissibility.py)
runs cleanly, exits 0, and reports `5 PASS / 0 FAIL` together with the
exact figures cited in the archived clean rationale: 576 microscopic
operators tested, max response gap `5.144895e-03`, conservative budget
`1.214751e-02`. Numerics underlying the prior clean verdict are
reproducible on the current code state.

**(C3) Dependency-edge wiring.** The parent note's currently
registered `deps[]` entries
(`yt_exact_coarse_grained_bridge_operator_note`,
`yt_exact_schur_normal_form_uniqueness_note`) match the runner's
actual one-hop Python imports
(`scripts.frontier_yt_exact_coarse_grained_bridge_operator`,
`scripts.frontier_yt_exact_schur_normal_form_uniqueness`). The dep
edges named by the later conditional auditor's
`open_dependency_paths` are wired in both directions
(`deps[]` + `helper_runner_paths`).

**(C4) Criticality return.** The row's current `criticality` is
`medium`, the same value under which the prior `audited_clean` verdict
was recorded. The `criticality_increased:medium->critical` archival
trigger is no longer in force at the row's present state.

**(C5) No-substantive-edit since clean audit.** The parent's runner
file
[`scripts/frontier_yt_microscopic_schur_class_admissibility.py`](../scripts/frontier_yt_microscopic_schur_class_admissibility.py)
contains the same `CONSERVATIVE_REL_BUDGET` reference (`1.214751e-02`)
implied by the archived clean rationale, achieved via the upstream
constants in `frontier_yt_exact_schur_normal_form_uniqueness`. No
runner edit silently changed the budget against which the conservative
endpoint check is compared.

These five observations are the only auditable companion claims. The
prior clean verdict's explicit out-of-scope items (zero endpoint
budget, unbounded `y_t`, microscopic realizations outside the tested
locality tube) remain explicitly out of scope here as well.

This companion does **not**:

- re-audit `yt_microscopic_schur_class_admissibility_note` or modify
  its `audit_status`, `effective_status`, `criticality`, or any other
  pipeline-managed field;
- assert that the prior `audited_clean` verdict is automatically
  re-applicable — the audit lane retains sole authority over that
  decision;
- introduce new vocabulary or new claim types;
- modify the parent note text, the parent runner, or any upstream
  dependency note or runner;
- propose a derivation, repair theorem, or admission for the upstream
  rows `yt_exact_coarse_grained_bridge_operator_note` or
  `yt_exact_schur_normal_form_uniqueness_note` (both currently
  `unaudited`); chain-promotion to retained-grade remains blocked by
  those upstreams' status independently of this companion;
- address the parent's honest-boundary items (zero endpoint budget,
  unbounded `y_t`, outside-tube microscopic realizations) — those
  remain explicitly out of scope.

The audit lane decides whether the (C1)-(C5) evidence is sufficient to
honor the prior judicial verdict at the row's present `criticality=medium`
state, or whether a fresh per-site audit is warranted.

---

## Criticality bump does not change the parent's substance

Per [`docs/audit/README.md`](audit/README.md), the audit pipeline
invalidates a prior verdict on a `criticality_increased` event so a
fresh look can confirm the prior reasoning still suffices at the new
criticality level. The bump itself does not edit the source note, the
runner, or the numerical content — it changes only the bookkeeping
field that controls audit triage priority.

For this row specifically:

- the original clean audit was issued at `criticality=medium`;
- the invalidation event was a transition `medium -> critical`;
- the row has since returned to `criticality=medium` (the present
  state, as recorded in
  [`audit_ledger.json`](audit/data/audit_ledger.json));
- the parent's note hash (`b35c7d4f...`) and runner exit status
  (`5 PASS / 0 FAIL`) match what the prior clean auditor reviewed;
- the deps named by the later (now-invalidated) conditional audit are
  now wired in `deps[]` and `helper_runner_paths`.

This companion does not assert that the audit lane must honor the
prior verdict. It records, in machine-checkable form, that the
substantive conditions under which the prior clean verdict was issued
remain in force. The audit lane retains full authority to re-audit if
it decides the bump-history alone or the upstream dep status warrants
fresh review.

---

## Companion runner block plan

[`scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py`](../scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py)
verifies the five observations block-by-block. Each block runs as an
independent check against the live filesystem and ledger; nothing is
hard-coded against an expected target value beyond the explicit
`note_hash` and numerical figures cited in the archived clean verdict.

Block 1 — **Parent note exists at expected path.** Asserts
`docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md` is present.

Block 2 — **Ledger row exists with expected `runner_path`.** Asserts
`yt_microscopic_schur_class_admissibility_note` is present in
`audit_ledger.json` and its `runner_path` matches
`scripts/frontier_yt_microscopic_schur_class_admissibility.py`.

Block 3 — **Parent note hash matches the ledger.** Computes
`sha256(docs/YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md)` and
verifies it equals the `note_hash` field on the ledger row.

Block 4 — **Note hash matches the value covered by the latest
on-disk ledger row.** Confirms the file hash is the same on-disk
hex string `b35c7d4f431d3ecabc3098a4266bf7c9aa901cf2be1e3c989b62a1519fc21956`
that the ledger row carries — guards against an unnoticed silent edit
to the parent.

Block 5 — **Ledger declares an archived `audited_clean` verdict for
this row.** Walks `previous_audits[]` and confirms at least one entry
with `audit_status=audited_clean` exists, recording its
`auditor_family`, `audit_date`, `chain_closes`, `independence`, and
`auditor_confidence` for the companion log.

Block 6 — **Archived clean verdict's invalidation reason is a
`criticality_increased` event.** Confirms that the archived clean
entry's `invalidation_reason` is the exact string
`criticality_increased:medium->critical`. Localises the trigger to a
criticality bump, not a substance change.

Block 7 — **Archived clean verdict's `runner_check_breakdown.total_pass`
is positive.** Confirms the archived clean snapshot recorded a
non-trivial total of runner passes (the cited value is 5).

Block 8 — **Current `criticality` matches the criticality at which the
archived clean verdict was issued.** Asserts current `criticality` on
the row equals the `criticality` recorded in the archived
`audit_state_snapshot` of the clean entry (both should be `medium`).

Block 9 — **Current `claim_type` is unchanged from the clean entry.**
Asserts the row's current `claim_type` matches the `claim_type` field
on the archived clean entry. (Both should be `bounded_theorem`.)

Block 10 — **Dependency edges wired.** Asserts every entry in the
current row's `deps[]` is itself a `claim_id` present in
`audit_ledger.json`. Confirms the deps are not phantoms.

Block 11 — **Runner imports match registered deps.** Statically scans
the parent runner source for `import frontier_yt_*` /
`from frontier_yt_* import` statements and asserts the set of imported
upstream modules corresponds bijectively to the runner-script paths
recorded in the row's `helper_runner_paths`. (Confirms (C3): the
deps named by the later conditional audit are now wired.)

Block 12 — **Parent runner exits 0.** Invokes the parent runner via
`subprocess.run`, captures stdout, and asserts the return code is 0.

Block 13 — **Parent runner reports `5 PASS / 0 FAIL` final tally.**
Parses the runner stdout, locates the `FINAL TALLY:` line, and asserts
it reads `5 PASS / 0 FAIL`.

Block 14 — **Parent runner reports the cited max response gap.**
Parses the runner stdout for the `Max response-vs-kernel gap` line and
asserts the value equals `5.144895e-03` to numerical-print precision
(the figure cited in the archived clean rationale).

Block 15 — **Parent runner reports the cited conservative endpoint
budget.** Parses the runner stdout for the `Conservative package
budget` line and asserts the value equals `1.214751e-02` to
numerical-print precision (the figure cited in the archived clean
rationale).

Block 16 — **Max response gap is strictly inside the budget.**
Parses the two numerical figures and asserts strictly that
`max_response_gap < conservative_budget`.

Block 17 — **Runner counts the cited microscopic-operator sample
size.** Parses the runner stdout for the `Microscopic operators
tested` line and asserts the value equals `576` (the figure cited in
the archived clean chain-closure explanation).

Block 18 — **Runner reports `Coarse reductions in Schur class` equal
to the microscopic-operator count.** Confirms the
`Coarse reductions in Schur class` line in the runner stdout matches
the `Microscopic operators tested` line: every constructed local
positive operator survived the Schur reduction inside the Schur class.

Block 19 — **Companion runner is `claim_type=meta` by file naming
convention.** Asserts this companion's runner filename matches the
`audit_companion_*` prefix used throughout the repo for meta
audit-companion runners, distinguishing it from primary `frontier_*`
runners that carry bounded-theorem semantics.

Block 20 — **No status changes proposed.** Static-source scan of this
companion runner confirming it issues no writes to
`audit_ledger.json`, no `apply_audit` invocations, and no edits to
the parent note or parent runner. Confirms the companion is read-only
on the ledger surface.

Block 21 — **Parent's audit-dependency-repair section names the
currently registered deps.** Confirms the "Audit dependency repair
links" section of the parent note text mentions both
`yt_exact_coarse_grained_bridge_operator_note` and
`yt_exact_schur_normal_form_uniqueness_note`, which are also present
in the row's `deps[]`. Wiring is bidirectional (prose link +
machine-readable dep).

The exact PASS/FAIL count is printed at runtime. Cached output is
[`logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt).

---

## What this companion does NOT do

1. Promote `yt_microscopic_schur_class_admissibility_note` (or any
   other row) to retained, bounded, or closed.
2. Re-apply or assert that the prior 2026-05-01 `audited_clean` verdict
   is automatically valid at the row's current state. The audit lane
   retains sole authority over that decision.
3. Address the upstream dep status. Both
   `yt_exact_coarse_grained_bridge_operator_note` and
   `yt_exact_schur_normal_form_uniqueness_note` are currently
   `unaudited` themselves; chain-promotion of the parent to
   retained-grade remains structurally blocked by those upstream
   statuses, independent of this companion.
4. Modify the parent note text, the parent runner, the upstream notes,
   or the upstream runners.
5. Introduce a new axiom, claim_type, or framing.
6. Address the parent's honest-boundary items (zero endpoint budget,
   unbounded `y_t`, microscopic realizations outside the tested
   locality tube). Those remain explicitly out of scope, exactly as
   in the parent note's "Honest boundary" section.

---

## Cross-references

- Parent note: [`YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md`](YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md)
- Parent runner: [`scripts/frontier_yt_microscopic_schur_class_admissibility.py`](../scripts/frontier_yt_microscopic_schur_class_admissibility.py)
- Upstream dep notes (both currently `unaudited`):
  - [`YT_EXACT_COARSE_GRAINED_BRIDGE_OPERATOR_NOTE.md`](YT_EXACT_COARSE_GRAINED_BRIDGE_OPERATOR_NOTE.md)
  - [`YT_EXACT_SCHUR_NORMAL_FORM_UNIQUENESS_NOTE.md`](YT_EXACT_SCHUR_NORMAL_FORM_UNIQUENESS_NOTE.md)
- Audit-lane policy: [`docs/audit/README.md`](audit/README.md)
- Audit ledger row data: [`docs/audit/data/audit_ledger.json`](audit/data/audit_ledger.json)
- Sibling criticality-bump invalidation policy commits: PR-history
  records `audit: preserve clean audits on criticality bumps`,
  `audit: soft-reset on criticality bump to critical instead of full
  invalidation`, and `audit: scope criticality_increased invalidation
  to FRESH_LOOK_REQUIREMENTS §4 actually-required cases`.

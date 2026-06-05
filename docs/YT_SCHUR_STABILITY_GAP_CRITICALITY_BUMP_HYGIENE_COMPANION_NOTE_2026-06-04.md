# YT Schur Stability Gap: Criticality-Bump Audit-Readiness Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / hygiene)
**Status:** companion-only — supplies audit-friendly evidence that the
substance of the parent note
[`YT_SCHUR_STABILITY_GAP_NOTE.md`](YT_SCHUR_STABILITY_GAP_NOTE.md) is
unchanged since its prior `audited_clean` snapshot and that the prior
verdict-bearing runner output reproduces on the current `origin/main`
tree. It is not a new theorem claim, not a status promotion, and not
an attempt to perform re-audit work. If the audit pipeline seeds this
file, it is a meta companion row; the audit lane still sets
`audit_status`, and pipeline-derived `effective_status` remains
downstream of that authority.
**Companion target:** `yt_schur_stability_gap_note` (parent note
`docs/YT_SCHUR_STABILITY_GAP_NOTE.md`).
**Primary runner:**
[`scripts/audit_companion_yt_schur_stability_gap_criticality_hygiene_2026_06_04.py`](../scripts/audit_companion_yt_schur_stability_gap_criticality_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_schur_stability_gap_criticality_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_schur_stability_gap_criticality_hygiene_2026_06_04.txt)

---

## §0. Provenance summary (audit-lane convenience)

- Parent ledger row: `yt_schur_stability_gap_note`.
- The current `origin/main` ledger snapshot has the parent row waiting
  for independent audit-lane handling, with pipeline reason
  `awaiting_audit` and load-bearing score `6.615`. This companion
  records that context only; it does not set, request, or recommend
  any audit verdict or effective-status outcome.
- The archived audit history on `origin/main` contains two prior
  snapshots on this row (in insertion / chronological order):
  - `previous_audits[0]` is the 2026-05-01 clean bounded-theorem
    snapshot by `codex-audit-loop` (auditor family `codex-gpt-5`),
    archived on 2026-05-04 after the criticality bump
    `criticality_increased:medium->critical`. All four runner checks
    passed in that snapshot.
  - `previous_audits[1]` is the separate 2026-05-05 conditional
    bounded-theorem snapshot by `codex-cli-gpt-5.5-...`, archived on
    2026-05-08. All four runner checks passed in that snapshot as
    well.
- The criticality-bump invalidation that this companion targets is
  the archived clean snapshot at `previous_audits[0]`. The later
  conditional snapshot at `previous_audits[1]` is a separate audit
  cycle and is recorded here only for chronological transparency; it
  is not the load-bearing target of this hygiene companion.
- Parent note content hash on origin/main:
  `8119a5c437c4a0c5ddcd4be4c786a34cec2b60ff39aded95df915ed3ad7e83fd`
  (matches the `note_hash` recorded on the current ledger row).
- Parent runner content hash on origin/main:
  `b9688ba88dd8dbb7297241ea3163cbd18caeec6f90e99041063ae6f7d7213662`
  (matches the `audit_state_snapshot.runner_hash` recorded in
  `previous_audits[1]` from the 2026-05-05 audit cycle; the runner
  hash field is not populated on the earlier 2026-05-01
  `previous_audits[0]` snapshot but the runner content is unchanged
  between the two snapshots, as the live re-run in Block H3
  confirms).

---

## §1. Why this companion exists

The parent narrow theorem `yt_schur_stability_gap_note` was previously
audit-loop-resolved on 2026-05-01 as `audited_clean`
(`bounded_theorem`, class C, four runner checks passing) by
`codex-audit-loop` (auditor family `codex-gpt-5`). The clean verdict
covered the scoped bounded claim that "the admissible exact Schur
coarse-operator perturbation family remains inside the Schur
normal-form class throughout the scanned envelope, implying no escape
within radius 1 in that scan."

The audit pipeline subsequently invalidated that snapshot with the
criticality-bump reason `criticality_increased:medium->critical`.
This is a soft-reset class of invalidation: under the policy adopted in
PR #907 ("audit: criticality bumps don't force downstream re-audits;
bumped row requests 2nd audit only"; see also PR #925 restoration),
a criticality bump returns the bumped row to unaudited effective
status to request a fresh judicial pass on the heavier-weight version
of the same claim, without disturbing the substantive content of the
prior clean verdict.

A subsequent re-audit cycle on 2026-05-05 by
`codex-cli-gpt-5.5-...` recorded a conditional bounded-theorem
snapshot with four runner checks passing. That second cycle is
independently recorded on
`previous_audits[1]`; it is not the target of this hygiene companion
but is referenced for chronological completeness.

This companion records, for the audit lane, that:

1. The parent note's prose has not changed since the prior
   `audited_clean` snapshot (content hash match).
2. The parent runner's source has not changed since the same snapshot
   (runner hash match against the 2026-05-05 archived
   `audit_state_snapshot.runner_hash`).
3. The parent runner still reproduces 4 PASS / 0 FAIL on the current
   `origin/main` tree, with the same load-bearing observation as the
   prior audit (no out-of-class operator found in the scanned
   envelope; max in-class radius 3.535534; first escape beyond the
   scanned envelope).
4. The ledger row has the expected post-invalidation shape for a row
   awaiting independent audit-lane handling: the row is surfaced as
   unaudited, the archived clean snapshot remains in `previous_audits`,
   and the criticality-bump invalidation reason is recorded there.

This is audit-friendly evidence that the substantive content of the
prior clean snapshot survives the criticality bump unchanged, giving
the audit lane machine-checkable context for its independent handling
of the bumped row. The companion does not itself re-audit, promote, or
re-tier the parent.

---

## §2. Scope and boundary

This companion makes four narrow auditable observations, each
mechanically verified by the paired runner:

**(H1) Parent note presence and hash invariance.** The parent file
`docs/YT_SCHUR_STABILITY_GAP_NOTE.md` exists on the working tree, and
its content hash matches the `note_hash` field on the ledger row
`yt_schur_stability_gap_note`.

**(H2) Parent runner presence and hash invariance.** The parent
runner `scripts/frontier_yt_schur_stability_gap.py` exists on the
working tree, and its content hash matches the `runner_hash` recorded
in the most recent prior audit `audit_state_snapshot` on the ledger
row.

**(H3) Parent runner reproduces the prior verdict's PASS count.**
Running `scripts/frontier_yt_schur_stability_gap.py` on the current
tree returns exit code 0 with 4 PASS / 0 FAIL, matching the prior
audit's four runner PASS checks.

**(H4) Ledger-state invariants consistent with a criticality-bump
soft reset.** On the most recent `origin/main` ledger snapshot
shipped with this companion, the row `yt_schur_stability_gap_note`
satisfies:

  - the row is surfaced as unaudited by the ledger's audit-status and
    effective-status fields;
  - the effective-status reason is `awaiting_audit`;
  - `previous_audits` is non-empty;
  - there exists at least one prior audit on this row with
    audit status `audited_clean` and
    `invalidation_reason` matching the regex
    `^criticality_increased:` (this is the criticality-bump
    soft-reset target the companion exists to acknowledge);
  - that prior clean snapshot has four runner PASS checks, matching
    the live runner re-run from Block H3.

This companion does **not**:

- introduce a new theorem claim;
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about the auditor's appropriate next action on the
  bumped row;
- re-audit `yt_schur_stability_gap_note` or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides, on its own schedule and authority, whether
the substance-unchanged + runner-reproduces evidence is sufficient to
resolve the criticality-bumped row from the archived clean snapshot,
or whether a fresh per-site audit is warranted.

---

## §3. Why criticality-bump is a soft reset, not a substantive change

The criticality field on a ledger row records the audit lane's
operational priority weight for re-examining a row's verdict. A bump
from `medium` to `critical` means the audit lane judges that the
chain effects (transitive descendants count, load-bearing score) make
the prior clean verdict more consequential than originally
classified, not that the substantive content of the verdict is in
doubt.

The audit-criticality-bump policy in PR #907 explicitly says:

> Criticality bumps don't force downstream re-audits; the bumped row
> requests a 2nd audit only.

PR #925 then performed a one-shot restoration of audits that had
been over-aggressively invalidated by an earlier, stricter policy.

The current pipeline behavior on a criticality bump is therefore
expected to have this soft-reset shape:

1. Surface the row for audit-lane follow-up.
2. Preserve the prior snapshot, including the runner PASS count, in
   `previous_audits`.
3. Record the criticality-bump invalidation reason on the archived
   snapshot.
4. Leave downstream rows alone.

All four conditions are visible on the current ledger row
`yt_schur_stability_gap_note` and are explicitly verified by the
paired runner (Block §H4).

---

## §4. Companion runner block plan

The paired runner
`scripts/audit_companion_yt_schur_stability_gap_criticality_hygiene_2026_06_04.py`
verifies the four hygiene observations as independent blocks. Every
load-bearing arithmetic check is performed against (a) the file
contents on disk (for hash invariance), (b) the parent runner's
exit-code and PASS/FAIL count (for substance reproduction), and (c)
the JSON ledger row at
`docs/audit/data/audit_ledger.json` (for ledger-state invariants).

The runner is hermetic: it imports only the standard library
(`hashlib`, `json`, `pathlib`, `re`, `subprocess`, `sys`, `time`).
It does not import the parent runner module; it executes the parent
runner in a child process so that the in-class PASS count is observed
the same way the audit pipeline observes it. The runner reports
`PASS` / `FAIL` per check and a final tally; the cached output
records the run.

Block plan (one check per `record(...)` call):

- Block §H1.1: parent note path exists on the working tree.
- Block §H1.2: parent note content hash equals the canonical hash
  `8119a5c437c4a0c5ddcd4be4c786a34cec2b60ff39aded95df915ed3ad7e83fd`
  observed on origin/main as the current `note_hash`.
- Block §H2.1: parent runner path exists on the working tree.
- Block §H2.2: parent runner content hash equals the canonical hash
  `b9688ba88dd8dbb7297241ea3163cbd18caeec6f90e99041063ae6f7d7213662`
  observed in the most recent prior audit's
  `audit_state_snapshot.runner_hash`.
- Block §H2.3: parent runner is importable (compile-only check; no
  side effects).
- Block §H3.1: parent runner exits with status code 0.
- Block §H3.2: parent runner stdout contains a
  `FINAL TALLY: N PASS / 0 FAIL` line with `N = 4`.
- Block §H3.3: parent runner stdout reports the "open stability
  basin" PASS line (the prior verdict's load-bearing assertion).
- Block §H3.4: parent runner stdout reports the
  "first escape ... beyond the unit branch budget radius" PASS line
  (the prior verdict's load-bearing assertion #2).
- Block §H3.5: parent runner stdout reports the
  "in-class operators remain well separated" PASS line
  (the prior verdict's load-bearing assertion #3).
- Block §H3.6: parent runner stdout reports the
  "nearest escape ... real response-class failure" PASS line
  (the prior verdict's load-bearing assertion #4).
- Block §H4.1: ledger row exists for `yt_schur_stability_gap_note`.
- Block §H4.2: ledger row audit-status field surfaces the row as
  unaudited.
- Block §H4.3: ledger row effective-status field surfaces the row as
  unaudited.
- Block §H4.4: ledger row effective-status reason is
  `awaiting_audit`.
- Block §H4.5: ledger row `previous_audits` is non-empty.
- Block §H4.6: there exists a prior audit on the row with audit
  status `audited_clean` and
  `invalidation_reason` matching `^criticality_increased:`
  (the criticality-bump soft-reset target).
- Block §H4.7: that prior clean snapshot has four runner PASS checks
  (matches the live runner result from Block H3).
- Block §H4.8: that prior `audited_clean` snapshot has
  `claim_type == "bounded_theorem"`
  (matches the current row class).
- Block §H4.9: ledger row `claim_type == "bounded_theorem"`
  (parent class preserved).
- Block §H4.10: ledger row `runner_path` points at
  `scripts/frontier_yt_schur_stability_gap.py`.
- Block §H4.11: ledger row `note_path` points at
  `docs/YT_SCHUR_STABILITY_GAP_NOTE.md`.
- Block §H4.12: ledger row `deps` is non-empty and includes
  `yt_exact_schur_normal_form_uniqueness_note`
  (the parent's audit-dependency repair link).
- Block §H4.13: most-recent prior audit on the row has four runner
  PASS checks (substance reproduces across both prior audits).

Total: 24 checks across four blocks (2 + 3 + 6 + 13). The exact
PASS/FAIL count is printed at runtime and recorded in the SHA-pinned
cached runner output.

---

## §5. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR.

The audit lane decides how to handle the bumped criticality; this
companion only supplies machine-checkable evidence on whether the
substance has changed since the prior clean snapshot (it has not) and
whether the prior runner result reproduces (it does).

The criticality-bump observation here is structurally narrow: it does
not extend to any other invalidated row. Each row currently bumped
under `criticality_increased:*` is independent of this companion and
should be examined separately as the audit lane reaches it.

---

## §6. References

- Parent note:
  [`YT_SCHUR_STABILITY_GAP_NOTE.md`](YT_SCHUR_STABILITY_GAP_NOTE.md)
- Parent runner:
  [`scripts/frontier_yt_schur_stability_gap.py`](../scripts/frontier_yt_schur_stability_gap.py)
- Parent's upstream base helper module:
  [`scripts/frontier_yt_exact_schur_normal_form_uniqueness.py`](../scripts/frontier_yt_exact_schur_normal_form_uniqueness.py)
- Archived clean snapshot:
  `docs/audit/data/audit_ledger.json` row
  `yt_schur_stability_gap_note`, `previous_audits[0]`
  (clean bounded-theorem snapshot, class C, by `codex-audit-loop` /
  `codex-gpt-5`, audit date 2026-05-01, archived 2026-05-04 after
  `criticality_increased:medium->critical`)
- Audit-criticality-bump policy: PR #907
  ("audit: criticality bumps don't force downstream re-audits;
  bumped row requests 2nd audit only")
- One-shot restoration of over-aggressive invalidations: PR #925
- Audit ledger overview:
  [`docs/audit/AUDIT_LEDGER.md`](audit/AUDIT_LEDGER.md)
- Audit lane README:
  [`docs/audit/README.md`](audit/README.md)

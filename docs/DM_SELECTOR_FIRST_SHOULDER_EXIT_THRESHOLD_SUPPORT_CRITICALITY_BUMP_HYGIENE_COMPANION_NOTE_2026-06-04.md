# DM Selector First-Shoulder-Exit Threshold Support: Criticality-Bump Audit-Readiness Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / hygiene)
**Status:** companion-only — supplies audit-friendly evidence that the
parent note's substance (its scoped `open_gate` claim and its paired
runner) is unchanged in load-bearing content since the prior
cross-confirmed clean snapshot, and that the parent runner
still reproduces 11 PASS / 0 FAIL on the current `origin/main` tree.
It is not a new theorem claim, not a status promotion, not a request
that the parent's open gate be treated as closed, and not an attempt
to perform re-audit work. If the audit pipeline seeds this file, it is
a `meta` audit-readiness companion row. This companion writes no audit verdict
and does not supply a direct effective-status change.
**Companion target:** `dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`
(parent note
[`DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md`](DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md)).
**Primary runner:**
[`scripts/audit_companion_dm_selector_first_shoulder_exit_threshold_support_criticality_hygiene_2026_06_04.py`](../scripts/audit_companion_dm_selector_first_shoulder_exit_threshold_support_criticality_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_selector_first_shoulder_exit_threshold_support_criticality_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_selector_first_shoulder_exit_threshold_support_criticality_hygiene_2026_06_04.txt)

---

## §0. Why this companion exists (audit-readiness context)

The parent narrow note
`dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`
is intentionally an **open-gate row**: its `claim_type` is `open_gate`,
its scoped claim is exactly the algebraic open-gate statement that
"the canonical earliest middle-branch breakpoint of the exact
threshold-volume family is unique, belongs to the preferred recovered
lift, lies inside the prior stabilization window, and selects that
lift when the exact field is evaluated there," and the parent note
explicitly disavows promotion of `tau_b,min` to a physical threshold
law. Two prior independent audits on `origin/main` returned
clean verdicts (with cross-confirmation between fresh-context
auditors) explicitly **confirming the open-gate scope** —- they did
not close the gate; they confirmed that the open-gate claim, as
stated, is what the parent runner verifies.

The current `origin/main` ledger snapshot has the row surfaced as
generated audit status reset to `unaudited` with `effective_status_reason:
awaiting_audit`. The most-recent invalidation reason on the row's
archived audit history is `criticality_increased:leaf->critical`
(carried on the earlier 2026-05-02 archived clean snapshot).
This companion records the criticality-bump-soft-reset shape of the
invalidation, the substantive content reproduction of the parent
runner, and the runner-hash invariance against the most-recent prior
audit cycle — none of which change the parent's intentional open-gate
status.

The companion does **not** claim the gate has closed. It does **not**
re-audit, promote, or re-tier the parent. It supplies audit-friendly
evidence that the parent's runner-side substance is identical to what
the prior clean cycles evaluated.

---

## §1. Parent recap, open_gate confirmation, prior clean audits

### §1.1 Parent recap

The parent note proves four narrow algebraic facts on the recovered
bank of intrinsic threshold-volume lifts:

1. For each recovered lift `i`, the canonical middle-branch breakpoint
   is `tau_b(i) := log(1 + b_i)`, where `b_i` is the middle inverse
   eigenvalue of the common-shifted positive comparison window.
2. The minimum `tau_b,min = min_i tau_b(i) = 0.148036252277635...` is
   unique and belongs to the preferred recovered lift `0`.
3. It lies strictly inside the previously certified stabilization
   window `(tau_star, tau_zero(next))` with strict margins
   `tau_b,min - tau_star = 0.016398674056082 > 0` and
   `tau_zero(next) - tau_b,min = 0.123604890448858 > 0`.
4. Evaluating the exact threshold-volume field `V_tau` at
   `tau_b,min` already makes lift `0` the unique minimizer with
   minimum competitor gap `0.146091270049196 > 0`.

The parent's `## Boundary` section explicitly states the open gate:

> This is a support theorem only. It does **not** prove that the
> physical threshold law must be `tau_phys = tau_b,min`. It proves
> only that `tau_b,min` is now the cleanest intrinsic selector
> candidate already present on the exact family.

### §1.2 Open_gate type, two prior clean audit cycles

The parent ledger row's current `claim_type` is `open_gate` (the
audit-decided type from the most-recent prior audit cycle). The
ledger row's `previous_audits` array has two entries:

- **`previous_audits[0]`** — 2026-05-02 audit by
  `claude-opus-4.7-1m:open-gates-2026-05-02-c1-04`
  (auditor family `claude-opus`). Audit status clean,
  claim type `bounded_theorem` at the time, criticality `leaf`,
  runner check breakdown `total_pass = 2`. Archived 2026-05-05
  with `invalidation_reason: criticality_increased:leaf->critical`.
  The verdict rationale on that snapshot confirmed the open-gate
  framing explicitly: "Within the canonical-breakpoint
  identification scope, the chain closes by direct arithmetic on
  the bank. The note explicitly disclaims that
  `tau_phys = tau_b,min`, so the bounded interpretation as
  'cleanest currently-present intrinsic selector candidate' is
  exactly the source's safe read."
- **`previous_audits[1]`** — 2026-05-05 audit by
  `codex-fresh-second-dm_selector_first_shoulder_exit_threshold_support_note-20260505`
  (auditor family `codex-gpt-5`), cross-confirmed by a separate
  first-audit pass at 2026-05-05 from
  `codex-fresh-first-dm_selector_first_shoulder_exit_threshold_support_note-20260505`.
  Both auditors returned clean verdicts at `claim_type = open_gate`,
  criticality `critical`, with runner check breakdown
  `total_pass = 11`. Cross-confirmation `status: confirmed`.
  The 2026-05-06 archival on this snapshot recorded a note-hash
  change (`archived_for_note_hash` differs from the current
  on-disk note_hash) but no `invalidation_reason` — that archive
  was a substance-evolution capture, not an invalidation.

### §1.3 What the prior audits confirmed

Both prior cycles confirmed exactly the same thing later independent audit handling
sees today: the parent's four algebraic facts are runner-verified
(PASS=11 FAIL=0) and the parent's prose explicitly withholds the
stronger claim that `tau_phys = tau_b,min`. The 2026-05-05
cross-confirmed cycle re-audited the rescoped `open_gate` claim
(matching today's row class) at the heavier `critical` criticality
bucket, so the load-bearing-at-larger-scope verdict is on record.

Neither prior verdict closed the open selector gate. Neither prior
verdict promoted `tau_b,min` to a physical threshold law. Today's
audit-lane handling of the criticality-bump-invalidated row inherits
those scoping decisions; this companion only records that the
runner-side substance reproduces unchanged on the current tree.

---

## §2. Invalidation cause (criticality_increased:leaf->critical)

The `invalidation_reason` carried by the row's most-recent archived
audit snapshot is `criticality_increased:leaf->critical`. This is a
soft-reset class of invalidation: under the policy adopted in PR #907
("audit: criticality bumps don't force downstream re-audits; bumped
row requests 2nd audit only"; see also PR #925 for the one-shot
restoration of over-aggressively invalidated audits), a criticality
bump returns the bumped row to `unaudited` effective status to request
a fresh judicial pass on the heavier-weight version of the same claim,
without disturbing the substantive content of the prior verdict.

Concretely, the criticality bump on this row reflects upstream
ledger-graph growth (more descendants now depend, transitively, on
the open-gate row, so later independent audit handling treats the open-gate scope as more
consequential than originally classified). It does **not** signal a
substance change in the parent note or runner.

The current `origin/main` ledger snapshot on this row has shape:

- generated audit status reset to `unaudited`
- generated effective status reset to `unaudited`
- `effective_status_reason: awaiting_audit`
- `previous_audits` non-empty (two entries as detailed in §1.2)
- at least one prior clean snapshot with
  `invalidation_reason` matching `^criticality_increased:`
  (which this companion explicitly verifies via Block §H4)
- `claim_type: open_gate` (matches the most-recent prior audit's
  audited claim type)
- `criticality: medium` (the row's criticality field has since been
  re-evaluated relative to the post-bump `critical` state in
  `previous_audits[1].audit_state_snapshot.criticality`; that
  re-evaluation is a separate audit-pipeline judgement and is
  recorded here only for chronological transparency)

This shape is exactly what the audit pipeline produces under the
criticality-bump soft-reset policy on a row whose substantive content
has been re-audited at the heavier criticality bucket since the
original bump.

---

## §3. Substance-unchanged: the parent's open-gate characterization is preserved

Two substance-invariance facts are mechanically verifiable on the
current `origin/main` tree and are individually checked by the paired
runner:

**(S1) Runner-hash invariance to `previous_audits[1]`.** The current
on-disk content hash of
`scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py`
is
`08c7ae1063e4b211cf34086b6c94614358c4dd7ce9b5b0e4bc0155b474f18b86`,
which equals `previous_audits[1].audit_state_snapshot.runner_hash`
exactly. The runner later independent audit handling would re-execute today is the
identical script the 2026-05-05 cross-confirmed clean audit
cycle executed.

**(S2) Runner-result invariance.** Re-executing the parent runner on
the current `origin/main` tree returns exit code 0 with
`SUMMARY: PASS=11 FAIL=0`, matching the `runner_check_breakdown:
{total_pass: 11, ...}` recorded on `previous_audits[1]` and matching
the parent note's documented expected output. All four parts of the
parent note (PART 1–4) report their full PASS lines, including the
load-bearing four-fact algebraic chain (parts 1–3) and the
scientific-consequence framing (part 4).

These two facts mean the parent's open-gate characterization — the
four-fact algebraic claim, scoped exactly as the parent prose
describes, with explicit disavowal of `tau_phys = tau_b,min` — is
preserved under any reasonable audit-lane re-execution of the same
runner against the same parent prose claim. The runner-side substance
is identical to what the 2026-05-05 cross-confirmed clean audit
cycle evaluated.

### §3.1 Note-hash caveat (honest reporting)

The current parent note-hash
(`437c7445df083c750787babacc5186e15bf248b06e3d7ea86bd036a53b4ee9f9`)
differs from `previous_audits[1].archived_for_note_hash`
(`27974cf3d96605b26780884d27790446e927cdb5282711864c3e1b895b8cd745`).
This difference reflects a 2026-05-25 expansion of the parent prose and a
2026-07-26 derivation-certificate repair. Together they **sharpen the
open-gate disavowal** and **display the complete finite-bank certificate** —
without introducing any new claim, new admitted-context input, or new
promotion of the open-gate row.

The structural diff between the prior cross-confirmed note hash and
the current note hash is, per `git diff` on the parent file path,
exactly:

- the `Status:` line was updated from "selector-side support theorem
  on the open DM gate" to "exact support theorem on the open DM
  selector gate" (clarification, not scope change);
- backtick prose references to the two upstream notes were converted
  to relative markdown links;
- the explicit open-gate disavowal paragraph was added in
  full ("This note does not assert a physical threshold law. Its
  closed claim is the algebraic open-gate statement: ...");
- the explicit recovered-bank inverse-eigenvalue parameter table for
  lifts 0–4 was added;
- the strict-margin numerical expansions
  (`tau_b,min - tau_star = 0.016398674056082`,
  `tau_zero(next) - tau_b,min = 0.123604890448858`,
  `min_{j>0} V_tau_b,min(H_j) - V_tau_b,min(H_0) = 0.146091270049196`)
  were promoted from the runner output into the prose;
- the closing four-line algebraic-chain summary
  (`tau_b(i) = log(1+b_i) => ... => argmin V_tau_b,min = {0}`)
  was added.
- on 2026-07-26, the explicit `Type: open_gate` author hint and a
  load-bearing derivation certificate were added; the certificate records
  monotonicity, all four positive breakpoint margins, both positive window
  margins, every competitor's strict middle-branch inequalities, and all four
  positive selector gaps. It also names the two upstream dependencies and
  states that no observed threshold, fitted selector, or physical threshold
  law is used.

All of these are prose-side sharpenings of the same open-gate claim
that the 2026-05-05 cross-confirmed audit cycle evaluated. None of
them alter the four-fact algebraic chain, the runner that verifies
it, or the parent note's explicit refusal to promote `tau_b,min` to
the physical threshold law. Later independent audit handling owns the provenance
boundary for deciding whether the expanded prose calls for a fresh per-row read or
whether the prior cross-confirmed verdict can be reused at the
current criticality bucket given the runner-side substance
invariance documented in (S1)–(S2).

This companion does not assert that the note-hash change is
audit-irrelevant. It records, narrowly and verifiably, that:

- the four-fact algebraic chain is unchanged;
- the runner script and its PASS count are unchanged;
- the open-gate disavowal is preserved (and was made more explicit in the
  2026-05-25 expansion and the 2026-07-26 derivation certificate).

---

## §4. Verification block: parent runner still passes; parent's gate scope unchanged

The paired runner verifies all of the §3 substance-invariance facts
plus the §2 criticality-bump-soft-reset ledger-state invariants as
independent blocks, each checked by an explicit `record(...)` call.
Every load-bearing arithmetic check is performed against (a) the file
contents on disk (for hash invariance), (b) the parent runner's
exit-code and PASS/FAIL count (for substance reproduction), and (c)
the JSON ledger row at `docs/audit/data/audit_ledger.json` (for
ledger-state invariants).

The runner is hermetic: it imports only the standard library
(`hashlib`, `json`, `pathlib`, `re`, `subprocess`, `sys`, `time`).
It does not import the parent runner module; it executes the parent
runner in a child process so that the in-class PASS count is observed
the same way the audit pipeline observes it.

Block plan (one check per `record(...)` call):

- Block §H1.1: parent note path exists on the working tree.
- Block §H1.2: parent note content hash equals the canonical hash
  of the repaired source note (acknowledges the §3.1 note-hash changes).
- Block §H2.1: parent runner path exists on the working tree.
- Block §H2.2: parent runner content hash equals the canonical hash
  observed in `previous_audits[1].audit_state_snapshot.runner_hash`
  (Block §S1 invariance).
- Block §H2.3: parent runner is compile-only importable
  (`py_compile.compile`).
- Block §H3.1: parent runner exits with status code 0.
- Block §H3.2: parent runner stdout contains
  `SUMMARY: PASS=11 FAIL=0` (Block §S2 substance reproduction).
- Block §H3.3: parent runner stdout reports the PART 1 unique
  earliest middle-branch threshold PASS line (load-bearing
  algebraic fact #2).
- Block §H3.4: parent runner stdout reports the PART 2
  above-`tau_star` PASS line (load-bearing algebraic fact #3a).
- Block §H3.5: parent runner stdout reports the PART 2
  below-next-zero PASS line (load-bearing algebraic fact #3b).
- Block §H3.6: parent runner stdout reports the PART 3
  unique-minimizer-at-`tau_b,min` PASS line (load-bearing
  algebraic fact #4).
- Block §H3.7: parent runner stdout reports the PART 4
  open-gate-not-promoted PASS line (load-bearing scope discipline).
- Block §H4.1: ledger row exists for
  `dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`.
- Block §H4.2: ledger row generated audit status is `unaudited`.
- Block §H4.3: ledger row generated effective status is `unaudited`.
- Block §H4.4: ledger row `effective_status_reason` is
  `awaiting_audit`.
- Block §H4.5: ledger row `previous_audits` is non-empty.
- Block §H4.6: there exists a prior audit on this row with
  clean audit status and `invalidation_reason` matching
  `^criticality_increased:` (the soft-reset target).
- Block §H4.7: that criticality-bumped prior clean snapshot has its
  `audit_state_snapshot.criticality` field equal
  to `leaf` (the pre-bump bucket).
- Block §H4.8: there exists a prior clean snapshot on
  this row with `claim_type == "open_gate"` (the audit-decided
  current claim type).
- Block §H4.9: that `open_gate` clean snapshot reports
  cross-confirmation `status == "confirmed"`.
- Block §H4.10: that `open_gate` clean snapshot has
  `runner_check_breakdown.total_pass == 11` (matches the live
  runner re-run from Block §H3.2).
- Block §H4.11: ledger row `claim_type == "open_gate"`
  (current audit-decided type preserved).
- Block §H4.12: ledger row `runner_path` points at the parent
  runner.
- Block §H4.13: ledger row `note_path` points at the parent note.
- Block §H4.14: ledger row `deps` is non-empty and includes both
  declared upstream dependencies
  (`dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization_note_2026-04-18`
  and
  `dm_selector_threshold_stabilization_support_theorem_note_2026-04-21`).
- Block §H4.15: most-recent prior clean snapshot
  (the 2026-05-05 cross-confirmed cycle) has the runner hash
  recorded in §3 (S1) — pins the load-bearing runner identity.

Total: 22 checks across four blocks (2 + 3 + 7 + 10). The exact
PASS/FAIL count is printed at runtime and recorded in the SHA-pinned
cached runner output.

---

## §5. What this companion does NOT do

This companion explicitly does not:

- modify the parent note in any way;
- modify the parent runner in any way;
- modify the ledger row, its `audit_status`, its `effective_status`,
  its `claim_type`, its `criticality`, its `load_bearing_score`, or
  any other ledger field;
- assert that the open gate has closed (it has not — the parent
  prose, this companion, and both prior clean verdicts all
  preserve the open-gate scope);
- assert that `tau_b,min` is the physical threshold law (the parent
  explicitly disavows this; both prior audits explicitly preserved
  that disavowal; this companion preserves it as well);
- assert that the prior clean verdict must be reused at
  the criticality-bumped re-evaluation;
- assert that the 2026-05-25 prose expansion or the 2026-07-26
  derivation-certificate repair is audit-irrelevant
  (later independent audit handling decides whether the prose-side sharpening calls for a
  fresh per-row read or whether the prior runner-hash-invariant
  verdict can carry forward at the current criticality bucket);
- re-audit `dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`
  or any other ledger row;
- introduce a new minimal-axiom statement or accepted-premise import;
- close any other invalidated row currently surfaced as `unaudited`.

Later independent audit handling owns the provenance boundary for next steps on this row.

---

## §6. Audit-pipeline boundaries (handoff)

When later independent audit handling next picks up this row at the post-bump criticality
bucket, the companion runner is a one-shot precondition check: if it
returns `PASS=N FAIL=0` for the full block plan (N = 22 at the time of
writing; subject to drift only if the ledger structure or parent
prose load-bearing PASS-line text changes upstream), the runner-side
substance is provably identical to what the 2026-05-05 cross-confirmed
clean audit cycle evaluated.

The auditor can then either:

- reuse the prior cross-confirmed verdict at the higher rigor
  threshold (the runner-side substance has not changed; the
  prose-side change is a sharpening of the open-gate disavowal that
  the prior auditor confirmed in scope); or
- schedule a fresh per-row audit with full information about which
  specific facts have changed (only the §3.1-listed prose
  sharpenings) and which have not (the entire four-fact algebraic
  chain, the parent runner, and the parent's open-gate disavowal).

Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied or
requested by this PR.

The criticality-bump observation here is structurally narrow to this
single row. Each other row currently bumped under
`criticality_increased:*` is independent of this companion and should
be examined separately as later independent audit handling reaches it.

---

## §7. References

- Parent note:
  [`DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md`](DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md)
- Parent runner:
  [`scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py`](../scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py)
- Parent's upstream dependencies:
  - [`DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md`](DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md)
  - [`DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md`](DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- Archived clean snapshots on the parent row:
  `docs/audit/data/audit_ledger.json` row
  `dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21`,
  `previous_audits[0]` (bounded-theorem-class clean snapshot, audit
  date 2026-05-02, by
  `claude-opus-4.7-1m:open-gates-2026-05-02-c1-04`, archived
  2026-05-05 with `invalidation_reason:
  criticality_increased:leaf->critical`) and `previous_audits[1]`
  (open-gate-class cross-confirmed clean snapshot, audit date
  2026-05-05, by two independent codex-gpt-5 fresh-context auditors,
  archived 2026-05-06 for a note-hash change with no
  `invalidation_reason`).
- Audit-criticality-bump policy: PR #907
  ("audit: criticality bumps don't force downstream re-audits;
  bumped row requests 2nd audit only")
- One-shot restoration of over-aggressive invalidations: PR #925
- Sister criticality-bump hygiene companions for template precedent:
  PR #2655
  (`hubble_lane5_two_gate_dependency_firewall` criticality-bump
  hygiene) and the YT Schur
  (`yt_schur_stability_gap` criticality-bump hygiene) companion at
  `docs/YT_SCHUR_STABILITY_GAP_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md`.
- Audit ledger overview:
  [`docs/audit/AUDIT_LEDGER.md`](audit/AUDIT_LEDGER.md)
- Audit lane README:
  [`docs/audit/README.md`](audit/README.md)

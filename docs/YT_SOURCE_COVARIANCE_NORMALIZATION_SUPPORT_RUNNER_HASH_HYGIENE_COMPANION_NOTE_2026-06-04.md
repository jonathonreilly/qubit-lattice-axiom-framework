# Y_T Source-Covariance Normalization Support: Runner-Hash / Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / runner-hash + dep-resolution hygiene evidence)
**Status:** companion-only — supplies review-compatible evidence that the
load-bearing derivation of the parent note
[`YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md`](YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md)
is invariant under the two recorded archive events for the parent
(the earlier `runner_hash_changed:442eeaa8->2874560a` and the more
recent `dep_weakened` event for the parent's no-go dep
[`yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`](YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md)).
It is not a new theorem claim, not a direct status change, and not an
attempt to perform independent audit work. If the audit pipeline
seeds this file, it is a `meta` companion row only: review-loop
supplies no audit verdict and no direct generated-status change.
**Companion target:** `yt_source_covariance_normalization_support_note_2026-05-24`
(parent note
[`docs/YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md`](YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md)).
**Primary runner:**
[`scripts/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py`](../scripts/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.txt)

This is a review-compatible meta companion: the parent's load-bearing
finite-support Schwinger-Dyson / Feynman-Hellmann covariance identity
is independently re-verified by the parent's own runner Parts 2-4 on
the same elementary partition-function algebra, with no consumption
of any external audit grade. The companion records that
substance-vs-grade separation as machine-checkable evidence for later
independent audit handling; it does not re-audit the parent and does
not change status.

---

## 0. Why this exists

The parent had two prior clean audit snapshots and is currently
pending fresh independent handling on `origin/main`:

1. **2026-05-25 snapshot** (codex-cli-gpt-5.5; cross_family
   independence; verdict scope: "Exact finite-support source-side
   covariance normalization in the fixed PR230 RN signed-record source
   coordinate."); subsequently archived under
   `invalidation_reason: runner_hash_changed:442eeaa8->2874560a`
   (the parent runner was reworked between 2026-05-25 and 2026-05-27
   while keeping the same theorem statement).
2. **2026-05-28 snapshot** (codex-fresh-context-audit-loop;
   fresh_context independence; verdict scope: "Exact finite-support
   RN source-coordinate derivative identities fixing the source-side
   connected row in the fixed h coordinate; physical scalar/Higgs
   normalization, canonical O_H, LSZ, kappa_Y, m_t, and y_t are out
   of scope."); subsequently archived 2026-06-04 under a
   dep-weakened invalidation involving
   `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`.

On the current `origin/main` head, the parent's runner file at
`scripts/frontier_yt_source_covariance_normalization_support.py` has
SHA-256
`2874560a7d1ba1cbce2cc9fd0085dcbe8e8f3bdc9bf4a1a2f4f23d0aadf91c5b`,
identical to the runner hash recorded in the 2026-05-28 archived
snapshot. The parent's note text on `origin/main` is
unchanged from that snapshot. The parent's runner emits

```text
RESULT: PASS=33 FAIL=0
```

on the current head — identical to the
`runner_check_breakdown.total_pass == 33` recorded in both prior
clean snapshots. The earlier
`runner_hash_changed:442eeaa8->2874560a` event is subsumed by the
2026-05-28 fresh-context pass (which reviewed the new 2874560a runner
directly and arrived at the same clean treatment), and is not the
currently open question.

The currently open question is purely a grade-propagation event: the
parent's no-go dep
[`yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`](YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md)
moved out of its prior no-go treatment into pending-chain handling
(and then further into pending independent handling via a downstream
`dep_weakened` on
[`observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16`](OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md)).
The parent's other dep
[`yt_source_action_support_packet_note_2026-05-22`](YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md)
retains its own bounded-source treatment on `origin/main`.

The honest-stop question is then exactly:

> Does the parent's substantive claim — the finite-support
> Schwinger-Dyson / Feynman-Hellmann covariance identity
> `d^2 log Z / dh_x dh_y = Cov_h(epsilon_x, epsilon_y)` — load-bear
> on the *audit grade* of the no-go dep
> `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`
> (which was weakened) — or only on *textbook algebraic facts* about
> the finite RN partition function, which the parent's own runner
> re-verifies block-for-block, independently of the dep's grade?

This companion records that the second reading is the one supported
by the parent's runner and note text. The parent's runner Parts 2-4
verify the FH covariance identity and the source-rescaling boundary
from direct math-module computation on the finite signed-record
algebra, independent of any audit-status field. The parent's
load-bearing step is the elementary algebraic identity

> `d log Z / d h_x = <epsilon_x>_h`
> `d^2 log Z / d h_x d h_y = <epsilon_x epsilon_y>_h - <epsilon_x>_h <epsilon_y>_h
>                          = Cov_h(epsilon_x, epsilon_y)`

which is fully internal to the parent's runner Part 2 (finite-sum
differentiation of a strictly positive partition function on a
finite state space).

This companion is therefore review-compatible evidence that the prior
clean reading of the parent's substantive content survives the
no-go dep's audit-grade change. It is not a re-audit and does not
promote status; it documents the load-bearing-step dependency
surface in machine-checkable form so later independent audit handling
can decide how to treat the parent in light of the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md`](YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md)
proves the following narrow bounded support identity. Let `Omega` be
a finite signed-record block with a positive reference weight
`mu_0(epsilon) > 0`, and for source profile `h` define

```text
Z(h) = sum_epsilon mu_0(epsilon) exp(sum_x h_x epsilon_x),
mu_h(epsilon) = mu_0(epsilon) exp(sum_x h_x epsilon_x) / Z(h).
```

Then by direct finite-sum differentiation,

```text
d log Z / d h_x       = <epsilon_x>_h,
d^2 log Z / d h_x d h_y
  = <epsilon_x epsilon_y>_h - <epsilon_x>_h <epsilon_y>_h
  = Cov_h(epsilon_x, epsilon_y) =: C_ss(x,y; h).
```

In particular, under the uniform zero-source reference
`<epsilon_x>_0 = 0`, the origin score equals the primitive signed
record and `C_ss(x,y; 0) = <epsilon_x epsilon_y>_0`. The parent
records a rescaling boundary observation: rescaling
`epsilon_x -> lambda epsilon_x` while keeping the same `h`
coordinate changes the fixed-h origin score by `lambda`; the change
is absorbable into a coordinate redefinition `h -> lambda h`, which
is a different source-coordinate convention rather than a scalar /
Higgs normalization theorem.

The parent reaches the bounded conclusion

```text
source-side C_ss fixed by RN source coordinate
scalar-side C_HH and C_sH still require canonical O_H / LSZ
```

with the explicit scope-boundary

```yaml
claim_type_author_hint: bounded_theorem
status_boundary: independent_audit_handling_only
direct_generated_status_change_allowed_from_this_note: false
support_surface: source-side covariance normalization in the fixed source-action RN source coordinate
out_of_scope:
  - same-surface source/action source
  - canonical O_H
  - scalar LSZ
  - strict pole rows or W/Z bypass
  - matching/running
```

via the parent runner
[`scripts/frontier_yt_source_covariance_normalization_support.py`](../scripts/frontier_yt_source_covariance_normalization_support.py),
which on the current head produces

```text
RESULT: PASS=33 FAIL=0
```

— bit-for-bit identical to the `runner_check_breakdown.total_pass`
value of both prior clean snapshots (33 in each), under
the same 2874560a runner SHA-256 audited in the 2026-05-28 snapshot.

The most recent (2026-05-28) clean snapshot's
`chain_closure_explanation` reads:

> Finite support and positive mu_0 give Z(h)>0 and justify
> differentiating through the sum: d_x Z = Z <epsilon_x>_h, and
> d_y <epsilon_x>_h = <epsilon_x epsilon_y>_h - <epsilon_x>_h
> <epsilon_y>_h. The one-hop dependencies supply the
> RN source convention and the scalar-normalization boundary
> without importing a physical Higgs/LSZ normalization.

The 2026-05-28 snapshot's `verdict_rationale` records that the
identity was independently re-verified:

> Independent math check: direct differentiation of the finite
> partition function gives the stated expectation and connected-
> covariance identities with no missing sign, factor, or
> normalization. The uniform-origin statement follows only under
> the stated uniform signed-record reference, and source rescaling
> changes the fixed-h score unless treated as a different source-
> coordinate convention. The cached runner reports
> RESULT: PASS=33 FAIL=0 and checks the covariance identity, origin
> convention, source-rescaling boundary, and firewalls against
> scalar/Higgs overclaim.

This companion records that the load-bearing step is exactly the
finite-sum differentiation argument (Class A: 11 of 33 PASSes in the
2026-05-28 snapshot, plus 22 firewall / boundary Class B PASSes) and
that this argument does **not** consume the dep's audit grade.

---

## 2. The two archived invalidation events

### 2a. Earlier event — `runner_hash_changed:442eeaa8->2874560a`

The 2026-05-25 clean snapshot recorded
`runner_hash = 442eeaa8519a7c8d23c3daf29bf9718cc8a8d8b668ed96693ed5401b3eb62032`
and a `runner_check_breakdown` of `{A:26, B:7, C:0, D:0, total_pass:33}`.
This snapshot was archived on 2026-05-27 with
`invalidation_reason: runner_hash_changed:442eeaa8->2874560a`.

The parent runner was subsequently re-audited on 2026-05-28
(`fresh_context` independence, archived 2026-06-04) under the new
runner hash
`2874560a7d1ba1cbce2cc9fd0085dcbe8e8f3bdc9bf4a1a2f4f23d0aadf91c5b`
and reached the same clean verdict, with
`runner_check_breakdown = {A:11, B:22, C:0, D:0, total_pass:33}` (the
total PASS count is identical; the A/B re-classification reflects the
fresh-context auditor's bucketing of the same 33 checks). So the
earlier `runner_hash_changed:442eeaa8->2874560a` event is **subsumed**
by the 2026-05-28 re-audit and is no longer the open question.

This companion's Block 9 confirms the 2874560a runner hash is still
current on `origin/main` (i.e. there is no further unresolved runner-
hash drift since the 2026-05-28 audit).

### 2b. Current event — `dep_weakened` on the no-go dep

The 2026-05-28 clean snapshot was archived on 2026-06-04 with a
dep-weakened invalidation involving
`yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`.
The parent's other dep
`yt_source_action_support_packet_note_2026-05-22` remained
in its own bounded-source treatment throughout.

This is purely a propagation event from the dep's downstream chain.
The no-go dep
[`yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`](YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md)
itself was archived 2026-06-04 with
an upstream dep-weakened invalidation involving
`observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16`,
i.e. one step further upstream from the parent.

Neither weakening reflects a substantive change to the parent's
runner code, the parent's note text, or the parent's load-bearing
algebraic step. The parent's RUNNER HASH AND NOTE HASH ARE STABLE on
`origin/main` (see Block 9 and Block 8 of the companion runner).

---

## 3. Substance-vs-grade separation: what the parent really uses

The parent runner consumes only four kinds of inputs:

1. **File-existence anchors.** Part 1 confirms that the parent note,
   the two dep notes, and the audit ledger file all exist on disk.
   The audit ledger is opened as a `Path` and tested with
   `path.exists()` only; **no field of the ledger is read.**
2. **Note-text firewall phrases.** Parts 1 and 5 string-test the
   parent note for required boundary phrases and forbidden overclaim
   phrases. These are firewall guards over the **note text**; they
   do not consume any dep audit grade.
3. **Finite-state Schwinger-Dyson math.** Part 2 numerically
   differentiates `log Z(h)` over a 3-site `Omega = {-1, +1}^3`
   block at `h = (0.17, -0.23, 0.31)` with a non-uniform positive
   reference weight, and confirms the analytic gradient equals the
   numeric finite difference (and the analytic Hessian equals the
   centered finite-difference Hessian, and the Hessian is symmetric
   with strictly positive diagonal).
4. **Source-rescaling algebra.** Parts 3 and 4 confirm the uniform-
   origin zero-mean property of `epsilon` and the
   `epsilon -> lambda epsilon` vs `h -> lambda h` redefinition
   identity, both purely algebraic on `{-1, +1}^n`.

**None of these four input classes reads an audit-status field of
any dep.** The single use of the `LEDGER` Path is the file-existence
anchor in Part 1; no generated-status or verdict field is ever
fetched from the ledger by the parent runner.

The parent's load-bearing step is therefore independent of the
no-go dep's audit grade in a strictly machine-checkable sense:
flipping the no-go dep's grade (or the source-packet dep's grade)
between any of the audit-pipeline states does not change any line
of output from the parent runner.

The audit-pipeline-level `dep_weakened` event is **not** a
substantive runner change; it is exactly a grade-propagation event,
and the parent's algebraic certificate remains valid on its own
terms.

---

## 4. What this companion proves and does not prove

This companion proves the following narrow auditable observations:

- **C1.** The parent's runner SHA-256 on `origin/main` head is
  exactly `2874560a7d1ba1cbce2cc9fd0085dcbe8e8f3bdc9bf4a1a2f4f23d0aadf91c5b`,
  identical to the runner hash recorded in the 2026-05-28
  clean snapshot. The earlier `442eeaa8...` runner has
  been superseded and audited in its current form.
- **C2.** The parent's runner emits `RESULT: PASS=33 FAIL=0` on the
  current head, identical to the
  `runner_check_breakdown.total_pass == 33` in both prior
  clean snapshots.
- **C3.** The parent's runner contains no code path that reads any
  generated-status or verdict field of any dep row. The only ledger reference
  is a `Path.exists()` file-existence check.
- **C4.** The parent's note text contains no claim that the
  substantive FH covariance identity depends on the audit grade of
  the no-go dep
  `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23` or
  of the source-packet dep
  `yt_source_action_support_packet_note_2026-05-22`.
- **C5.** The parent's note text preserves every required boundary
  phrase and contains none of the forbidden overclaim phrases from
  the parent runner's Part 5 firewalls.
- **C6.** The finite-support FH covariance identity, the uniform-
  origin score identity, and the source-rescaling boundary identity
  are all re-verified by this companion runner from elementary
  primitives, independent of the parent runner.
- **C7.** This companion does not assert a status for the parent,
  the source-packet dep, or the no-go dep; it does not promote any
  of them; and it does not modify any parent / dep note or runner.

This companion does **not** prove:

- That the no-go dep
  `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23` has
  been restored to any prior no-go grade (it has not on
  `origin/main`).
- That the parent should be promoted back to any clean or bounded
  grade; that decision sits with later independent audit handling.
- Any change to the parent's stated scope. The parent's stated
  out-of-scope list (canonical `O_H`, scalar LSZ, `kappa_Y`, `m_t`,
  `y_t`, W/Z bypass, matching / running) is preserved verbatim.

---

## 5. Sister-PR alignment

This companion mirrors the structure of the recent runner-hash /
dep-resolution hygiene companion landed for the sibling parent
[`yt_lsp_signed_record_source_readout_support_note_2026-05-24`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md)
in PR #2673
(`science(meta): yt_lsp_signed_record_source_readout_support
runner-hash-change hygiene companion`).

Key differences from the sibling companion:

- The sibling parent's runner contains a
  `part2_ledger_status_boundary` function that *does* read the dep's
  `effective_status` (so the sibling parent's current runner output
  is `PASS=49 FAIL=1`, with the single FAIL being the procedural
  ledger-status watcher). This parent's runner has **no** equivalent
  ledger-grade watcher; the current output is `PASS=33 FAIL=0`. The
  substance-vs-grade separation is therefore even cleaner for this
  parent — there is no procedural FAIL at all, and no firewall
  forfeited.
- The sibling parent's most recent invalidation is itself a
  `dep_weakened` event into pending handling via the canonical
  `minimal_axioms` re-resolution. This parent's most recent
  invalidation is a `dep_weakened` event for a no-go dep
  no-go-dep propagation, which then cascaded further upstream into
  pending handling. Both reduce to the
  same hygiene question: *does the load-bearing math consume the
  weakened grade?* And both answer: *no*.

---

## 6. Companion runner block layout

See
[`scripts/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py`](../scripts/audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py)
for the executable verifier. The blocks are:

- **Block 1** — Re-execute the parent runner and confirm
  `RESULT: PASS=33 FAIL=0`; check that the totals match the
  `runner_check_breakdown.total_pass == 33` recorded in both prior
  clean snapshots.
- **Block 2** — Re-verify the finite-support Schwinger-Dyson /
  Feynman-Hellmann covariance identity at a fresh, independent
  source point on a 3-site signed-record block with an independent
  non-uniform positive reference weight (different from the
  parent's `0.13/-0.07/+0.05` weights and the parent's
  `h = (0.17, -0.23, 0.31)` evaluation point), independent of any
  dep grade.
- **Block 3** — Re-verify the uniform-origin zero-mean and origin-
  score identities directly from elementary algebra on
  `Omega = {-1, +1}^3`, independent of any dep grade.
- **Block 4** — Re-verify the source-rescaling boundary identity
  `epsilon -> lambda epsilon` vs `h -> lambda h` on
  `Omega = {-1, +1}^2`, independent of any dep grade.
- **Block 5** — Static source-scan of the parent runner: confirm
  that no generated-status or verdict field is read from any ledger row. The single
  `LEDGER` reference is a `Path.exists()` anchor.
- **Block 6** — Static source-scan of the parent note: confirm no
  claim that the substantive FH covariance identity depends on the
  audit grade of any dep, plus the parent's explicit `direct_
  effective_status_change_allowed_from_this_note: false` declaration.
- **Block 7** — Counterfactual independence: rerun the substantive
  Block 2-4 computations with no ledger access at all and confirm
  bit-for-bit identical numerical results.
- **Block 8** — Firewall preservation: confirm the parent note's
  required boundary phrases are present and the forbidden overclaim
  phrases are absent.
- **Block 9** — Runner-hash continuity: confirm the parent runner's
  current SHA-256 is identical to the runner hash recorded in the
  most recent clean snapshot (the 2026-05-28 `2874560a...`
  snapshot), and that no further unresolved
  runner-hash drift has occurred.
- **Block 10** — Companion self-discipline: confirm this companion
  note does not assert a status for the parent or the deps, does
  not promote either, and contains the required disclaimer
  phrases.

Expected runtime result:

```text
RESULT: PASS=90 FAIL=0
```

(the companion does not depend on a precise count, only on zero
FAILs; the recorded `90` is the current PASS-count across all 10
blocks).

---

## 7. Boundary

```yaml
companion_type: audit_companion
companion_purpose: runner_hash_and_dep_resolution_hygiene_evidence
companion_targets:
  - yt_source_covariance_normalization_support_note_2026-05-24
companion_does_not:
  - promote parent or dep status
  - modify parent note text
  - modify parent runner code
  - modify dep notes or dep runners
  - assert a current parent grade
  - assert a current dep grade
  - re-audit the parent
  - re-audit the dep
  - introduce any new theorem claim
  - introduce any new axiom or import
status_boundary: independent_audit_handling_only
direct_generated_status_change_allowed_from_this_note: false
audit_required_before_effective_status_change: true
```

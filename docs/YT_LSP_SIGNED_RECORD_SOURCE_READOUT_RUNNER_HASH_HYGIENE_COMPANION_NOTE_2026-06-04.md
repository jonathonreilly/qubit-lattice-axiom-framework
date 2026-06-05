# Y_T LSP Signed-Record Source-Readout Support: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing derivation of the parent note
[`YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md)
is invariant under the 2026-06-04 audit-grade move of its dep
[`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
from `retained_bounded` back to `unaudited` (an
`axiom_premise_changed`-driven cascade through the canonical
`minimal_axioms` re-resolution). It is not a new theorem claim, not a
status promotion, and not an attempt to perform re-audit work. If the
audit pipeline seeds this file, it is a `meta` companion row; the audit
lane still sets `audit_status`, and pipeline-derived `effective_status`
remains downstream of that authority.
**Companion target:** `yt_lsp_signed_record_source_readout_support_note_2026-05-24`
(parent note
[`docs/YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md)).
**Primary runner:**
[`scripts/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.py`](../scripts/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
finite/projective signed-record substance is independently re-verified
by the parent's own runner (Parts 3-7) on the same local qubit / Pauli
algebra, with no citation to any external audit grade. The companion
records that substance-vs-grade separation as machine-checkable
evidence for the audit lane; it does not re-audit the parent and does
not promote status.

---

## 0. Why this exists

The parent had two prior `audited_clean` snapshots:

1. **2026-05-25 snapshot** (codex-cli-gpt-5.5; verdict scope:
   "Narrow algebraic support that the PR230 primitive signed RN
   source record has a native one-site Pauli sharp-projective signed
   readout carrier ..."); subsequently archived under
   `invalidation_reason: runner_hash_changed:725f822a->a796ff28`.
2. **2026-05-28 snapshot** (meitner-fresh-context-codex-gpt-5.5;
   verdict scope: "Finite signed-record support only ..."); subsequently
   archived under
   `invalidation_reason: dep_weakened:lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:retained_bounded->unaudited`.

On the current `origin/main` head, the parent's runner file at
`scripts/frontier_yt_lsp_signed_record_source_readout_support.py` has
SHA-256 `a796ff28b71099137ffcc59118f2b240cabdfad5f6b54b5730b3963ce026ad01`,
identical to the runner hash recorded in the 2026-05-28 audited_clean
snapshot. The parent's note text on `origin/main` is unchanged from
that snapshot. The current invalidation is purely a grade-propagation
event: the dep
[`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
moved from `retained_bounded` back to `unaudited` because its own
upstream
[`minimal_axioms`](MINIMAL_AXIOMS_2026-06-04.md) axiom-premise hash
changed (the canonical-node re-resolution recorded in
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)).

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on *textbook algebraic facts*
> about the local qubit Pauli operator and a product-RN log-derivative
> identity, both of which the parent's own runner re-verifies
> block-for-block, independently of the dep's grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner Parts 3-6
verify the signed-readout carrier and source-family uniqueness from
direct numpy/math computation on the standard Pauli matrices and the
exponential RN family, independent of any audit-status field. The
parent's load-bearing step is the algebraic identification

> `d log R_h / d h_x |_{h=0} = epsilon_x = sigma_z(x) spectral readout`

which is fully internal to the parent's runner.

This companion is therefore audit-friendly evidence that the prior
clean reading of the parent's substantive content survives the dep's
audit-grade change. It is not a re-audit and does not promote status;
it documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane can decide how to treat the
parent in light of the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md)
proves the following narrow bounded support identity:

> Let the local qubit algebra at site `x` be generated by `sigma_z(x)`,
> with sharp spectral projections `P_+(x) = (I + sigma_z(x))/2` and
> `P_-(x) = (I - sigma_z(x))/2`. The signed binary spectral readout
> `E_x = (+1) P_+(x) + (-1) P_-(x) = sigma_z(x)` has outcome set
> `{-1, +1}`. For the Y_T source-action product-RN family
> `R_h(epsilon) = exp(sum_x h_x epsilon_x) / Z(h)`, the origin score
> equals the signed-record primitive
> `d log R_h / d h_x |_{h=0} = epsilon_x`, which coincides with the
> signed projective readout of `sigma_z(x)`.
> A source-family uniqueness corollary: under positivity, smoothness,
> normalized-composition `normalize(R_h R_k) = R_{h+k}`, and the
> origin-score condition, the only such family is the exponential
> product RN.

The parent reaches the bounded conclusion

```text
Y_T source-action primitive signed source record epsilon_x
  = LSP sharp-projective signed Pauli readout at site x.
```

with the explicit scope-boundary

```yaml
source_boundary: signed_record_readout_support_only
audit_required_before_effective_status_change: true
direct_effective_status_change_allowed_from_this_note: false
```

via the parent runner
[`scripts/frontier_yt_lsp_signed_record_source_readout_support.py`](../scripts/frontier_yt_lsp_signed_record_source_readout_support.py),
which on the current head produces

```text
RESULT: PASS=49 FAIL=1
```

The single FAIL is the runner's Part 2 ledger-status check on the
dep `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`,
which was set to require `effective_status in {retained_bounded, retained}`
but is currently `unaudited`. All other 49 checks pass identically to
the prior `audited_clean` snapshot. The 49 substantive PASSes are
distributed exactly as in the 2026-05-28 snapshot's
`runner_check_breakdown` (16 Class A + 33 Class B passes, modulo the
one Class B Part 2 dep-status check that flipped).

The prior clean snapshot's `chain_closure_explanation` reads:

> The finite Pauli projector algebra, the retained bounded LSP
> projective measurement rule, and the retained bounded product-RN
> source-action support packet are sufficient to identify the signed
> source record with a native projective readout and to prove the
> stated RN-family uniqueness under the given source semantics.

That explanation phrases the chain *as if* the LSP dep's audit grade
(retained_bounded) is load-bearing. The present companion's narrow
observation is that the parent's *runner* — which is what mechanically
demonstrates the substantive claim — only uses the LSP dep's text in a
single citation-presence check (Part 3 lines:
`LSP note records K_P = P`; `LSP note records P E P sequential effect`).
The actual signed-readout algebra (idempotency, orthogonality, spectrum
`{-1, +1}`, `P_+ - P_- = sigma_z`) is computed directly from the Pauli
matrices in numpy, without consulting the dep's audit grade (see §3
below).

---

## 2. Invalidation cause

The audit ledger records the most recent archived invalidation reason

```text
dep_weakened:lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:retained_bounded->unaudited
```

archived at `2026-06-04T16:59:09Z`. This invalidation moves the parent
from `audited_clean` back to `unaudited` not because of any change in
the parent's runner, note text, prose, or computed numerical outputs,
and not because of any change in the underlying mathematical content
of the dep. It is a grade-propagation event in the audit graph: the
dep's `effective_status` was downgraded (in turn because its own
upstream
[`minimal_axioms`](MINIMAL_AXIOMS_2026-06-04.md) axiom-premise hash
moved from `1d36a556` to `b8848fc8` during the canonical-axiom-node
re-resolution), and the dep-weakening rule re-opens the parent for
fresh re-audit work.

At the time of this companion, the dep had *not* been restored to the
retained-bounded effective view on `origin/main`. This companion
therefore does *not* use the "dep restored" angle; it uses the
"parent does not load-bear on the dep's weakened audit grade" angle.

Note that the runner-hash recorded in the most recent archived clean
snapshot
(`a796ff28b71099137ffcc59118f2b240cabdfad5f6b54b5730b3963ce026ad01`)
exactly matches the SHA-256 of the parent's runner on the current head;
the runner has not changed since the most recent clean snapshot. The
earlier `runner_hash_changed:725f822a->a796ff28` event (archived
2026-05-27) is a prior cycle entirely subsumed by the second
`audited_clean` snapshot and is not the current open question.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not
load-bear on the *audit grade* of
`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`.**

The parent's runner
[`scripts/frontier_yt_lsp_signed_record_source_readout_support.py`](../scripts/frontier_yt_lsp_signed_record_source_readout_support.py)
re-verifies the signed-readout carrier and source-family uniqueness
directly on the local qubit Pauli matrices, with no query, citation,
or consumption of any audit-status field of the dep beyond the single
Part 2 procedural ledger-status watcher (which is exactly the check
that flipped under the dep weakening and is therefore the only PASS
loss). The remaining substantive blocks
(Part 3 projective Pauli readout; Part 4 RN source-score = signed
readout; Part 5 independent-site tensor commutativity; Part 6
source-family uniqueness; Part 7 firewalls) are algebraic / textbook
operator-algebraic statements about the standard Pauli matrices and
the exponential RN family, computed entirely inside the parent's
runner from sympy/numpy/math primitives.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming all 49 substantive checks pass with PASS=49 FAIL=1, where
   the single FAIL is exactly the Part 2 ledger-status check on the
   LSP dep (Block 1 of this companion's runner);
2. Re-verifying the signed-readout algebra (`P_+`, `P_-` idempotent,
   orthogonal, sum to `I`, `P_+ - P_- = sigma_z`, spectrum `{-1, +1}`)
   directly from numpy primitives (Block 2);
3. Re-verifying the RN origin-score identity
   `d log R_h / d h_x |_{h=0} = epsilon_x` numerically at three sites
   independent of the dep grade (Block 3);
4. Re-verifying source-family uniqueness (normalized-composition gives
   `h + k` addition; log-odds linearity; reconstructed family is
   product RN) independent of the dep grade (Block 4);
5. Confirming via static source-scan that the parent's runner contains
   zero references to audit-status grade fields beyond the single
   Part 2 ledger-status watcher, i.e. no other block of the runner
   reads `audit_status`, `effective_status`, `intrinsic_status`,
   `retained_bounded`, `audited_clean`, or `audited_conditional` from
   the dep's ledger row (Block 5);
6. Confirming via static source-scan that the parent note contains no
   claim that the substantive transport / source-readout conclusion
   depends on the dep's audit grade (Block 6);
7. Counterfactual confirmation: the parent's runner Parts 3-7
   substantive PASS counts are identical before and after redacting
   the dep's grade to `unaudited` (the substantive Pauli/RN algebra
   does not consult ledger fields) (Block 7);
8. Forward-firewall preservation: all "What This Does Not Close"
   boundary phrases in the parent note remain literal substrings, and
   no forbidden overclaim phrases have been added (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner on the current `origin/main` head produces

```text
RESULT: PASS=49 FAIL=1
```

with the single FAIL being the Part 2 ledger-status check on
`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`
(currently `unaudited`, where the runner expects
`{retained_bounded, retained}`). The substantive Parts 3-7 produce
PASS counts identical to the prior `audited_clean` snapshot's
`runner_check_breakdown` (PASS=50 FAIL=0 when the dep grade is in the
expected set; PASS=49 FAIL=1 when the dep grade is `unaudited`,
purely a procedural ledger-watcher flip with no change to the
underlying signed-readout / RN-source algebra).

The parent's note text, runner code (SHA-256 unchanged), and runner
numerical outputs are unchanged relative to the snapshot under which
it was last `audited_clean`. The dep's underlying mathematical content
(the `K_P = P` canonical Naimark/Lüders frame for sharp projective
measurements, and the standard sequential-effect form `P E P`) is
also unchanged on `origin/main`; only the dep's audit-lane grade has
moved.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it
modulo the one Part 2 procedural ledger-status flip. The audit lane
retains exclusive authority to decide how the prior clean treatment
should be handled under the dep's current grade; the present companion
only provides the machine-checkable evidence above to support that
decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open `Y_T source-action authority`, canonical
  `O_H`, scalar LSZ, kappa_Y, or y_t gates (those remain open exactly
  as the parent's "What This Does Not Close" and "Relation To
  Existing No-Gos" sections state them);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently;
- propose a fix to the parent runner's Part 2 ledger-status check
  (the current PASS=49 FAIL=1 split is itself an honest signal that
  the dep's grade moved, and the audit lane may prefer that the
  parent's runner continue to surface it explicitly).

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit-lane handoff

The audit lane decides whether and how to re-audit the parent under
the dep's current `unaudited` grade. The present companion supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  Parts 3-7 with no audit-status dependency on the dep;
- a re-verification that the parent's runner produces PASS=49 FAIL=1 on
  the current `origin/main` head, with the single FAIL identified as
  the Part 2 ledger-status watcher on the weakened dep;
- a static source scan that confirms the parent's runner only consults
  the dep's audit grade in the single Part 2 procedural watcher;
- a static source scan that confirms the parent note does not load-bear
  on the dep's audit-status grade;
- a small set of self-checks (Pauli algebra, RN origin-score identity,
  tensor commutativity, source-family uniqueness, firewall preservation)
  that exercise the remaining substantive content of the parent
  independent of the dep grade;
- a runner-hash verification confirming the parent's runner SHA-256 is
  identical to the runner hash recorded in the most recent
  `audited_clean` snapshot, i.e. no substantive runner change has
  occurred since the dep weakening.

If the audit lane chooses to treat the prior clean analysis of the
parent as reusable under the present dep grade, this companion records
the basis on which that decision can be made. If the audit lane
chooses to re-audit from scratch or to escalate the dep re-audit, this
companion does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion's type is `meta`, with audit-companion scope. It is not
a status change.

---

## Review Boundary Certificate

```yaml
claim_type_author_hint: meta
companion_kind: dep_resolution_hygiene
companion_target: yt_lsp_signed_record_source_readout_support_note_2026-05-24
status_authority: independent_audit_lane_only
proposal_allowed: false
proposal_allowed_reason: |
  This companion is an audit-friendly meta record of the
  substance-vs-grade separation between the parent's load-bearing
  Pauli/RN algebra and the audit grade of its dep
  lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22.
  It does not promote status, does not modify the parent or dep, and
  does not propose a new theorem.
audit_required_before_effective_status_change: true
direct_effective_status_change_allowed_from_this_note: false
```

## Verification

Run:

```text
python3 scripts/audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.py
```

Expected: all blocks PASS, with the companion runner reporting the
substance-vs-grade separation in machine-checkable form.

The parent's own runner remains the canonical demonstration of the
substantive signed-readout / RN-source algebra; this companion records
the dep-weakening hygiene only.

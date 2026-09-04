# Source/Measure Sharp-Record Tangent-Space: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies review-compatible evidence that the
parent
[`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
does not load-bear on the specific *audit grade* of its dep
[`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
— only on that dep's *structural existence* as a projective-record
surface concept, with the parent's actual mechanical content being
finite-probability tangent-space algebra (Radon-Nikodym score, zero
reference mean, Fisher pairing, exponential chart, six-component top
source normalization). The parent's own runner re-verifies that
algebraic content block-for-block from sympy primitives, with the dep
referenced only by an `exists()` filesystem check. This is not a new
theorem claim, not a direct status change, and not an attempt to perform
independent audit work. If the audit pipeline seeds this file, it is a
meta companion row only: review-loop supplies no audit verdict and no
direct generated-status change.
**Companion target:** `source_measure_sharp_record_tangent_space_theorem_note_2026-05-30`
(parent note
[`docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)).
**Primary runner:**
[`scripts/audit_companion_source_measure_sharp_record_tangent_space_dep_resolution_2026_06_04.py`](../scripts/audit_companion_source_measure_sharp_record_tangent_space_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_source_measure_sharp_record_tangent_space_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_source_measure_sharp_record_tangent_space_dep_resolution_2026_06_04.txt)

This is a review-compatible meta companion: the parent's load-bearing
finite-probability tangent-space algebra is independently re-verified
by the parent's own runner on the same finite sharp-record sample
space, with no citation to any external audit grade. The companion
records that substance-vs-grade separation as machine-checkable
evidence for later independent audit handling; it does not re-audit
the parent and does not change status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04, audit dated
2026-05-31) treated the row as a clean bounded theorem, with
verdict scope

> Finite sharp-record probability tangent-space algebra: RN scores have
> zero P0-mean, the signed two-outcome record is unit in the Fisher
> pairing, the exponential chart normalizes by W=log E0 exp(hO), and
> the stated six-component equal normalized top vector has coefficient
> 1/sqrt(6).

That snapshot was invalidated with reason

```text
dep_weakened:lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:bounded->pending
```

The dep
[`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
later moved from its bounded effective view back to pending handling
on `origin/main` (the dep itself was invalidated by the `minimal_axioms`
premise-node hash change and has not been restored).

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *structural existence /
> projective-record-surface naming* (concept-pointer) that the
> parent's own runner re-verifies via finite-probability algebra
> entirely independently of the dep's grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner consults the
dep only via an `exists()` filesystem check on
[`docs/LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md);
the load-bearing parts (Parts 2-4) are pure sympy computations on a
two-outcome `{-1, +1}` reference probability `(1/2, 1/2)` and the
six-component top source unit vector.

This companion is therefore review-compatible evidence that the prior
reading of the parent's substantive content survives the dep's audit
grade change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so later independent audit handling can decide how to treat the
parent in light of the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
proves four exact-support claims on a finite sharp-record sample space:

1. **Radon-Nikodym score**: every smooth absolutely-continuous
   record-probability intervention `P_h` has density `R_h = dP_h/dP_0`
   and origin score `s = d log R_h / dh |_{h=0}` with
   `E_0[s] = 0` (forced by `E_0[R_h] = 1`).
2. **Fisher pairing as canonical quadratic form**: the inner product
   `<s, t>_F = E_0[s t]` is canonical on the score tangent space; for
   the primitive signed record `epsilon in {-1, +1}` under the
   uniform reference, `E_0[epsilon] = 0` and `E_0[epsilon^2] = 1`,
   so `epsilon` is a unit source tangent and `lambda epsilon` has
   Fisher norm `lambda^2`.
3. **Exponential chart**: every score tangent `O` has a canonical
   normalized positive exponential chart
   `R_h = exp(h O - W(h))` with `W(h) = log E_0 exp(h O)`, where
   `W` is forced (not imported) by `E_0[R_h] = 1`.
4. **Y_T source unit**: for the normalized six-component top source
   tangent `O_top = sum_i O_i / sqrt(6)`, the Fisher norm is one;
   `lambda O_top` has norm `lambda^2`; the unit-tangent condition
   selects `lambda = 1`, i.e. `y_33 = 1/sqrt(6)`.

The parent reaches the bounded conclusion

```text
SUMMARY: PASS=38 FAIL=0
```

via four content parts plus a boundary part and a firewall part:

- Part 1: document/status boundary (existence of note files, presence
  of required section headings, exact-support status marker,
  no-bare-retention gate preserved);
- Part 2: finite probability tangent space (two-outcome sharp record,
  score formula, zero reference mean, Fisher norm `4a^2`, primitive
  signed record with Fisher norm one);
- Part 3: scaled tangent and exponential chart (Fisher norm
  `lambda^2`, `W = log cosh(h)`, score retrieval);
- Part 4: Y_T source unit (six-component top tangent unit Fisher norm,
  `lambda^2` scaling, `1/sqrt(6)` coefficient);
- Part 5: firewall (forbidden imports `H_unit`, `yt_ward_identity`,
  `y_t_bare`, PDG, `alpha_LM`, plaquette, fitted selector — each
  must be named in the note's firewall list; forbidden overclaim
  phrases absent).

The prior clean snapshot
(`codex-cli-gpt-5.5-20260531-134537-569bd619-source_measure_sharp_rec`,
high confidence) recorded a class-A load-bearing step and the runner
breakdown, with chain_closure_explanation

> The finite-space RN, zero-mean score, Fisher norm, exponential
> normalization, and lambda scaling identities follow by direct
> algebra from the provided definitions and the bounded
> projective-record source. The Y_T statement closes only as the
> stated normalized six-component tangent, not as a downstream
> physical-source acceptance claim.

That explanation phrases the chain *as if* the dep's audit grade is
load-bearing for the algebraic identities. The
present companion's narrow observation is that the parent's *runner*
— which is what mechanically demonstrates the substantive claim —
does not depend on the dep's grade at all (see §3). The dep is
referenced only as the named source for the projective-record-surface
concept; the runner consults it via a single `exists()` check, and
Parts 2-4 compute the algebraic identities entirely from sympy on a
finite `{-1, +1}` sample space.

---

## 2. Invalidation cause

The audit ledger records the archived invalidation reason

```text
dep_weakened:lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:bounded->pending
```

This invalidation moves the parent from a clean treatment back to
pending handling not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the dep. It is a grade-propagation
event in the audit graph: the dep's generated status changed
(itself driven by an upstream `minimal_axioms` premise-node hash
change on the dep), and the dep-weakening rule re-opens the parent
for fresh independent audit handling.

At the time of this companion, the dep had **not** been restored to
the bounded effective view on `origin/main`. This companion
therefore does **not** use the "dep restored" angle; it uses the
"parent does not load-bear on the weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not
load-bear on the *audit grade* of
`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`.**
The parent's runner
[`scripts/frontier_source_measure_sharp_record_tangent_space.py`](../scripts/frontier_source_measure_sharp_record_tangent_space.py)
references the dep only by an `exists()` filesystem check on the dep's
note path inside Part 1 (document/status boundary); it does not query,
cite, or consume any audit-status field of the dep, and does not
re-execute or import the dep's runner. The mechanical content of the
parent (Parts 2-4) — Radon-Nikodym score on the two-outcome reference
`(1/2, 1/2)`, Fisher norm `4a^2`, primitive signed-record Fisher norm
one, `lambda^2` scaling, exponential-chart normalization
`W = log cosh(h)`, six-component top source coefficient `1/sqrt(6)` —
is computed entirely inside the parent's runner from sympy primitives,
using only the finite sample space and the uniform reference
probability.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming all 38 checks pass with identical `SUMMARY: PASS=38 FAIL=0`
   (Block 1 of this companion's runner);
2. Re-verifying the load-bearing finite-probability algebra (Parts 2-4)
   directly from sympy: RN score on `(1/2, 1/2)`, zero reference mean,
   Fisher norm `4a^2`, primitive signed-record Fisher norm one,
   `lambda^2` scaling, `W = log cosh(h)`, six-component top
   coefficient `1/sqrt(6)` (Block 2);
3. Confirming via static source-scan that
   [`scripts/frontier_source_measure_sharp_record_tangent_space.py`](../scripts/frontier_source_measure_sharp_record_tangent_space.py)
   contains zero references to generated-status or verdict fields
   (Block 3);
4. Confirming via static source-scan that the parent note
   [`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
   contains no claim that the substantive transport conclusion depends
   on the dep's audit grade (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner with
   the dep in current pending handling yields identical pass
   count and identical algebraic outputs (Block 5);
6. Exponential-chart self-check: the normalizer `W(h)` is forced by
   `E_0[R_h] = 1` on the two-outcome sample space (not imported),
   independent of any dep grade (Block 6);
7. Y_T source-unit self-check: the six-component equal normalized
   tangent has Fisher norm one with coefficient `1/sqrt(6)`,
   `lambda`-scaling consistent with `lambda^2`, independent of any dep
   grade (Block 7);
8. Status-boundary preservation across the runs: the parent's
   exact-support marker, no-bare-retention marker, and forbidden-import /
   forbidden-overclaim firewall content are all preserved verbatim, and
   the companion declares `claim_type=meta` and disclaims direct status change
   (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on independent audit decisions for the dep.

---

## 4. Substance-unchanged assertion

The parent's runner output on the current `origin/main` head is

```text
SUMMARY: PASS=38 FAIL=0
```

with the JSON cached at
[`outputs/source_measure_sharp_record_tangent_space_2026-05-30.json`](../outputs/source_measure_sharp_record_tangent_space_2026-05-30.json).
This matches the runner content recorded in the prior clean snapshot
(the `runner_hash` is unchanged on `origin/main`).

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it had clean treatment. The dep's
underlying mathematical content (the projective-record surface concept
named in the dep's narrow theorem) is also unchanged on `origin/main`;
only the dep's audit grade has moved (driven by an upstream
`minimal_axioms` hash change on the dep, not by a change to the dep's
own content).

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
later independent audit handling decides how the prior clean treatment
should be handled under the dep's current grade; the present
companion only provides the machine-checkable evidence above to
support that decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's generated status or audit verdict;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open `proposal_allowed: false` /
  no-bare-retention gates (those remain open exactly as
  the parent states them in its `Status boundary` block);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; review-loop sets no
  audit verdict.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Independent Audit Handoff

Later independent audit handling decides whether and how to re-audit
the parent under the dep's current pending handling. The present
companion supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  with no audit-status dependency on the dep;
- a verification that the parent's runner continues to pass at the
  current `origin/main` head with the dep pending
  (`SUMMARY: PASS=38 FAIL=0`);
- a static source scan that confirms zero audit-status references in
  the parent's runner;
- a static source scan that confirms the parent note does not load-bear
  on the dep's audit-status grade;
- a small set of self-checks (RN-score zero-mean, Fisher norm
  `lambda^2` scaling, exponential-chart `W = log cosh(h)` forced by
  normalization, six-component top coefficient `1/sqrt(6)`) that
  exercise the remaining substantive content of the parent
  independent of the named projective-record-surface dep.

If independent audit handling chooses to treat the prior clean analysis of the
parent as reusable under the present dep grade, this companion records
the basis on which that decision can be made. If independent audit handling
chooses to re-audit from scratch or to escalate the dep re-audit,
this companion does not block that path; it only documents the
parent's substance-vs-grade dependency surface.

This companion's type is meta, with audit-companion scope. It is not a
status change.

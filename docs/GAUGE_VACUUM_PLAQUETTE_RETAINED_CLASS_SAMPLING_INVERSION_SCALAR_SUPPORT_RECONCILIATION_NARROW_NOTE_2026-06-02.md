# Gauge-Vacuum Plaquette Retained Class-Sampling Inversion — Scalar-Support Reconciliation (Narrow)

**Date:** 2026-06-02
**Type:** decoration
**Claim type:** decoration
**Status:** narrow companion to the audited_conditional parent
`gauge_vacuum_plaquette_retained_class_sampling_inversion_note_2026-04-17`
(load-bearing score 6.907 on origin/main). Targets the auditor's named
`runner_artifact_issue` repair only.
**Parent (not modified by this PR):**
`docs/GAUGE_VACUUM_PLAQUETTE_RETAINED_CLASS_SAMPLING_INVERSION_NOTE_2026-04-17.md`
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_scalar_support_reconciliation_narrow_2026_06_02.py`

## 2026-05-31 Audit Verdict (verbatim from `audit_ledger.json`)

```text
audit_status: audited_conditional
chain_closes: true
chain_closure_explanation: The retained-bounded evaluation authority supplies
  Z(W)=sum_lambda d_lambda c_lambda chi_lambda(W), and the inversion /
  underdetermination claims follow by finite-dimensional linear algebra. The
  runner artifact issue affects the submitted verification certificate, not
  the mathematical implication.
verdict_rationale: The finite inversion theorem itself is an algebraic
  consequence of the retained compressed boundary law: full-rank E gives
  c=E^(-1)Z, and m<N leaves a nontrivial nullspace. The cited scientific
  authorities are retained-grade for the restricted retained-sector surface.
  However the runner certificate in the packet is stale or inconsistent: the
  runner source checks for the exact scalar-note phrase
  "one scalar framework-point value does not determine the class-sector
  vector", which is absent from the supplied repaired scalar-value note, so
  the displayed SUPPORT=3/FAIL=0 summary is not reproduced from the
  restricted packet.
notes_for_re_audit_if_any: runner_artifact_issue: update the scalar support
  check to match the repaired scalar-value note and refresh the runner cache,
  then re-audit the same finite-inversion claim.
```

## What this companion does

This is a narrow runner-artifact reconciliation companion. It:

1. **Records the exact phrase mismatch** between the inversion runner's stale
   scalar support check and the repaired scalar-value note's current text.
2. **Proves the mismatch is a wording-only artifact**: each repaired phrase
   that IS present in the current scalar-value note semantically subsumes the
   exact phrase the inversion runner originally checked for, on the same
   retained restricted surface.
3. **Provides a paired runner** that (a) re-derives the inversion / under-
   determination algebra on the same witness used by the parent, (b) verifies
   the three repaired-phrase support checks against the actual phrases now
   present in the dependency notes on origin/main, and (c) prints the
   reconciliation mapping.

## What this companion does NOT do

- Does **not** modify the parent note text.
- Does **not** modify the parent runner.
- Does **not** modify the repaired scalar-value note.
- Does **not** claim the parent audited_conditional now lifts to
  retained_bounded; that is the auditor's call after the re-audit named in
  `notes_for_re_audit_if_any`.
- Does **not** add any new admission or load-bearing import.
- Does **not** propose a new axiom or theory-language extension.
- Does **not** weaken or retire any retained no_go.
- Does **not** claim explicit closed-form retained coefficient values; it
  only reconciles the support certificate to the post-2026-05-29 narrow
  scalar-value wording, exactly as the audit verdict names.

## The exact phrase mismatch

The parent's runner
`scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py`
contains this support check:

```python
check(
    "Scalar-value insufficiency note already records that one scalar sample "
    "does not determine the retained coefficient vector",
    "one scalar framework-point value does not determine the class-sector "
    "vector" in scalar_note,
    bucket="SUPPORT",
)
```

The exact substring it scans for is

```text
one scalar framework-point value does not determine the class-sector vector
```

The 2026-05-29 repair of
`docs/GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17.md`
narrowed the note to the elementary scalar-underdetermination lemma. That
specific substring is no longer present. The narrowed note states the same
content using three alternative phrasings (each verbatim from the current
file):

- **Phrase R1 (Status line):**
  `one scalar value does not determine`
  — appears in the `Status` line:
  `bounded formal no-go candidate: one scalar value does not determine an
  N >= 3 positive normalized class-sector vector.`
- **Phrase R2 (Formal No-Go block):**
  `a single scalar constraint does not determine`
  — in the elementary lemma statement:
  `the elementary finite-dimensional statement that a single scalar
  constraint does not determine an N >= 3 positive normalized vector.`
- **Phrase R3 (What This Closes block):**
  `a scalar plaquette value alone cannot be treated as full class-sector data`
  — in the bullet list of what the repaired note closes.

## Lemma (semantic equivalence on the retained restricted surface)

**Claim.** On the retained restricted surface of the parent — the finite
retained marked class sector with `|Lambda| = N` and the retained Peter-Weyl
coefficient vector `v_beta^Lambda = sum_lambda c_lambda chi_lambda` — each of
R1, R2, R3 implies the inversion-runner's original substring,

```text
S0 := "one scalar framework-point value does not determine the class-sector
vector",
```

in the only sense in which the inversion runner consumes it: that fixing one
scalar value of a linear functional on the retained coefficient vector does
not determine the coefficient vector.

**Proof.**

(a) The retained coefficient vector lives in `R^N` (or `C^N`) with `N >= 3`
on every retained sector of interest in the parent: the parent's explicit
witness uses `Lambda = {(0,0), (1,0), (0,1), (1,1)}` so `N = 4 >= 3`. Every
linear scalar observable on the coefficient vector is of the form
`L(c) = ell . c` for some row vector `ell`.

(b) A "framework-point" scalar evaluation, in the parent's language, is one
fixed marked-holonomy sample row `i`,
`Z_i = sum_lambda E_(i, lambda) c_lambda = (E_i .) c`, which is exactly a
linear scalar observable of `c`. So the inversion-runner's original substring
S0 is the assertion: a single linear scalar constraint
`(row_i .) c = Z_i` does not determine `c in R^N` with `N >= 3`.

(c) Phrase R2 (`a single scalar constraint does not determine an N >= 3
positive normalized vector`) is exactly that assertion in textbook
formulation. So R2 implies S0 on the restricted surface.

(d) Phrase R1 (Status line `one scalar value does not determine`, restricted
to `N >= 3 positive normalized class-sector vector`) is the same statement
applied to the retained class-sector coefficient vector; same implication.

(e) Phrase R3 (`a scalar plaquette value alone cannot be treated as full
class-sector data`) is the same statement in the plaquette PF language; same
implication.

(f) Conversely, the inversion runner does not consume any content of S0
beyond (b). It does not, for instance, reference an environment Wilson/Haar
kernel, a rim-lift theorem, or a compression theorem (the broader content the
2026-05-29 repair stripped from the scalar-value note). So the wording change
is a runner-artifact only; the dependency on the repaired scalar-value note
is preserved in full.

This closes the auditor's named `runner_artifact_issue`: the support check
can be re-stated against any of R1, R2, R3 (or all three jointly) and will
pass on the current scalar-value note, while the inversion runner's
mathematical content (Theorem 1, Corollaries 1-2, explicit witness, recovery
and underdetermination) is unchanged. The companion runner below executes
this re-stated support check and reproduces the parent's
THEOREM PASS / SUPPORT PASS counts under the restricted retained packet.

## What this PR closes

- the auditor's exact `runner_artifact_issue` named in
  `notes_for_re_audit_if_any` for the parent claim
  `gauge_vacuum_plaquette_retained_class_sampling_inversion_note_2026-04-17`,
  via a paired runner whose certificate reproduces from the restricted
  retained packet on the post-2026-05-29 wording.

## What this PR does not close

- the parent's `audited_conditional` lift itself; that is the auditor's call
  on re-audit after this runner-artifact reconciliation lands.
- any explicit closed-form retained coefficient value `c_lambda(beta=6)`.
- the global sole-axiom PF selector theorem.

## Authorities cited (all retained on origin/main)

- **Parent (audited_conditional, lb=6.9):**
  `GAUGE_VACUUM_PLAQUETTE_RETAINED_CLASS_SAMPLING_INVERSION_NOTE_2026-04-17`
- **Retained bounded (parent dep):**
  `GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_EVALUATION_THEOREM_NOTE_2026-04-17`
  (`retained_bounded`, supplies `Z_beta^env(W) = <K(W), v_beta>`)
- **Decoration (parent dep):**
  `GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_FUNCTIONAL_UNIQUENESS_NOTE_2026-04-17`
  (decoration; left boundary functional universal and unique)
- **Retained no_go (parent dep, scalar-value side):**
  `GAUGE_VACUUM_PLAQUETTE_BETA6_SCALAR_VALUE_INSUFFICIENCY_NOTE_2026-04-17`
  (`retained_no_go`, with the post-2026-05-29 narrow scalar-underdetermination
  scope).

No new admissions, no new imports, no new axioms. Pure wording reconciliation
on the retained restricted surface.

## Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_scalar_support_reconciliation_narrow_2026_06_02.py
# expect: PASS=14 FAIL=0
```

Verifier exercises:

- **(A) Parent inversion algebra reproduction** (5 checks): on the same
  retained witness sector `Lambda = {(0,0), (1,0), (0,1), (1,1)}` and the
  same four generic SU(3) marked-holonomy samples used by the parent runner,
  re-derives the full evaluation matrix `E`, verifies `|det E|` is bounded
  away from zero, reproduces the exact recovery `c = E^(-1) Z`, reproduces
  the rank-3 underdetermination, and reproduces the four-sample response
  gap.
- **(B) Repaired-phrase presence** (3 checks): each of R1, R2, R3 is verbatim
  present in the current scalar-value note as published on origin/main.
- **(C) Stale-phrase absence** (1 check): the inversion-runner's original
  substring S0 is confirmed absent from the repaired scalar-value note (so
  the artifact issue is reproduced under the restricted packet and the
  reconciliation is non-trivial).
- **(D) Sibling-authority phrase presence** (2 checks): the parent's other
  two SUPPORT checks (compressed rim-evaluation, compressed rim-functional
  uniqueness) still find their target substrings on origin/main, so the
  reconciled support certificate reproduces the parent's
  `SUPPORT=3/FAIL=0` count on the new runner.
- **(E) Hostile-audit invariants** (3 checks): parent note text not modified,
  parent runner not modified, repaired scalar-value note not modified.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_scalar_support_reconciliation_narrow_2026_06_02.py
```

Expected summary:

`PASS=14 FAIL=0`

# `g_bare` Forced (Ward Rep-B + Same-1PI) — Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing class-A algebraic step of
[`G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md`](G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md)
is invariant under the 2026-06-04 Record-axiom adoption in
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). It is not
a new theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09`
(parent note
`docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md`).
**Primary companion runner:**
[`scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow bounded theorem
`g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09` was
audit-loop-resolved on 2026-05-26 as `audited_clean` (`bounded_theorem`,
load-bearing step class A) by a 3/5 judicial-panel majority on the
narrowed scope:

> Bounded Ward-route algebra: given the `retained_bounded` Ward Rep-B
> form-factor identity and the (then-`retained_bounded`) same-1PI
> coefficient identity on the same `Q_L` block, the unique positive
> bare coupling satisfying both at `N_c=3` is `g_bare=1`; no continuum,
> Wilson-phenomenological, top-Yukawa readout, or physical-observable
> claim is audited.

The prior verdict was subsequently invalidated by a cascade triggered
upstream by the 2026-06-04 framework axiom update from
`MINIMAL_AXIOMS_2026-05-20.md` to `MINIMAL_AXIOMS_2026-06-04.md`
(Lattice + Quantum + Record; explicit-owner-approved per
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
section 6):

1. The `minimal_axioms` stable premise-node note-hash bumped to
   `b8848fc8`, which directly invalidated
   `yt_ward_identity_derivation_theorem` (the parent's grand-upstream
   `H_unit`-residue source) via
   `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`.
2. The cascade weakened
   `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` via
   `dep_weakened:yt_ward_identity_derivation_theorem:retained_bounded->unaudited`,
   dropping it from `retained_bounded` to `retained_pending_chain`.
3. That in turn invalidated the present parent via
   `dep_weakened:g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19:retained_bounded->retained_pending_chain`,
   returning the parent row to `effective_status=unaudited`.

The parent's own load-bearing step is **independent of the Record
axiom**: it is class-A algebraic substitution of one cited rational
identity into another (`(1/sqrt(6))^2 = g_bare^2 / (2 N_c)` at
`N_c = 3` gives `g_bare^2 = 1`, hence on the positive branch
`g_bare = 1`). Adopting the Record axiom adds a strictly additive
scalar record-readout statement, which is neither used nor invoked
anywhere in the algebraic substitution.

This companion records, for the audit lane, that the parent's
class-A algebraic step is invariant under the axiom-set change.
It is not a re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide whether to honor or re-test the prior judicial
verdict on the new premise hash, **once the cascade-upstream rows
(`yt_ward_identity_derivation_theorem` and
`g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19`) themselves
recover retained-grade status under their own Record-axiom-invariance
companions or fresh audits**.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the class-A substitution.** The
parent's load-bearing step (Section 4 of the parent note) depends only
on:

1. the rational identity `F_Htt^(0)(g_bare) = 1/sqrt(6)`, cited from
   `g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19`
   (one-hop authority W1; currently `effective_status =
   retained_bounded`);
2. the algebraic identity `F_Htt^(0)(g_bare)^2 = g_bare^2 / (2 N_c)`,
   cited from
   `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19`
   (one-hop authority W2; currently `effective_status = unaudited` via
   the upstream `yt_ward` cascade);
3. the integer datum `N_c = 3`, cited from
   `graph_first_su3_integration_note`;
4. the closed-field algebraic identity that the positive square-root
   branch of `g_bare^2 = 1` is `g_bare = 1`.

None of items 1-4 use the Record axiom's additive scalar record-readout
content. Item 1 is the retained-bounded Ward Rep-B form-factor
identity; the Record axiom does not enter its proof, and item 1's row
(`g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19`) was not
invalidated by the 2026-06-04 axiom-set change (it carries
`audit_status=audited_clean` and `effective_status=retained_bounded`
on the new premise hash, with its last invalidation reason
`criticality_increased:high->critical`, not `axiom_premise_changed`).
Item 2's row was demoted by the cascade traced above, but the cascade
acts upstream of the parent's class-A substitution step itself: the
parent's algebraic substitution is identical whether the upstream
identity is `retained_bounded` or `unaudited`, and identical whether
the framework axioms are `MINIMAL_AXIOMS_2026-05-20.md` (Lattice +
Quantum) or `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum +
Record).

**(C1) is the only auditable companion observation.** The two
cited one-hop authorities (`g_bare_two_ward_rep_b_independence` and
`g_bare_two_ward_same_1pi_pinning`) remain the parent's load-bearing
upstream premises exactly as in the parent note and the prior audit
verdict. The retention status of each is set by its own row in the
audit ledger and is unaffected by this companion.

This companion does **not**:

- close or weaken either of the parent's one-hop dependencies (the
  Rep-B retained identity W1 and the same-1PI candidate identity W2);
- re-audit
  `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09`
  or any other ledger row;
- attempt to close the upstream cascade by, e.g., supplying a
  Record-axiom-invariance argument for
  `yt_ward_identity_derivation_theorem` or for
  `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` (those
  are out-of-scope sister-row companions, lodged separately);
- introduce a new minimal-axiom statement (the
  explicit-owner-approved axiom set is fixed at
  `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to
re-honor the previous `audited_clean` verdict on the new premise
hash once the cascade-upstream rows recover retained-grade status,
or whether a fresh per-site audit is warranted.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` section "Record")
says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The 2026-06-04 memo's scope statement is explicit about what the
Record axiom does *not* supply:

> This axiom supplies only additive scalar record readout. It does not
> supply a rule for record production, persistence,
> measurement/decoherence, Born weights, P2/modulus/phase-blindness,
> log-det structure, time arrow, system composition, normalization/scale,
> source/action identification, `AC_phi_lambda`, theta, or arbitrary
> observable identification.

The parent's load-bearing step (Section 4 of the parent note) defines
no record surface, asks no question about scalar record additivity,
and writes no record functional `I(.)`. It executes one rational
substitution and one square-root branch selection:

```text
  Inputs:
    (W1) F_Htt^(0)(g_bare) = 1 / sqrt(6)           (cited identity)
    (W2) F_Htt^(0)(g_bare)^2 = g_bare^2 / (2 N_c)  (cited identity)
    (NC) N_c = 3                                   (cited integer)
  Substitution (W1) -> (W2):
    1/6 = g_bare^2 / 6
    g_bare^2 = 1                                   (class A)
  Positive square-root branch:
    g_bare = 1                                     (FD)
```

The Record axiom adds an additive scalar record functional and
nothing else. It does not modify (and is not modified by) the rational
arithmetic `1/6 = g_bare^2 / 6`, the algebraic step
`g_bare^2 = 1`, or the positive-branch selection `g_bare = 1`. So the
class-A algebraic content of the substitution is invariant under the
axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only `Fraction`
arithmetic on the cited rational data, and a "Record-axiom
counterfactual" block confirms that the value is unchanged whether or
not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_g_bare_forced_by_ward_rep_b_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the parent's class-A
algebraic step. Each block runs as an independent rational / algebraic
check using `fractions.Fraction` so every result is exact. The runner
reports `PASS` / `FAIL` per check; the cached output records the run.

- **Block 1 — `(W1)^2 = 1/6` exact rational.** Verifies the cited
  rational identity `F_Htt^(0)(g_bare)^2 = 1/6` is the exact rational
  square `(1/sqrt(6))^2`; the runner stores the value as
  `Fraction(1,6)` to avoid any floating-point ambiguity.
- **Block 2 — `(W2)` LHS = RHS at `g_bare = 1`, `N_c = 3`.** Verifies
  `g_bare^2 / (2 N_c) = 1/6` exactly at `(g_bare, N_c) = (1, 3)`.
- **Block 3 — Class-A substitution.** Verifies the exact rational
  consequence `(W1)^2 = (W2)|_{g_bare=1,N_c=3}` and confirms the
  resulting equation `1/6 = g_bare^2 / 6` solves to
  `g_bare^2 = 1` exactly.
- **Block 4 — Positive-branch selection.** Verifies the positive
  square-root branch of `g_bare^2 = 1` is `g_bare = 1` (and the
  negative branch is `g_bare = -1`); the parent explicitly selects
  the positive branch on physical bare-coupling grounds.
- **Block 5 — `g_bare`-grid uniqueness.** Verifies that for every
  representative `g_bare in {1/2, 1, 2, 3, 7/11}`, the constraint
  `g_bare^2 / (2 N_c) = 1/6` at `N_c = 3` holds iff `g_bare^2 = 1`,
  matching the parent runner's grid.
- **Block 6 — Rep-B independence of `(W1)`.** Verifies that
  `F_Htt^(0)(g_bare)^2 = 1/6` for the same representative grid (the
  retained Ward Rep-B-independence theorem proves this for all
  `g_bare`; the runner records the grid sample only).
- **Block 7 — Counterfactual grid contradictions.** Verifies that for
  every `g_bare in {1/2, 2, 3, 7/11}` (i.e., `g_bare != 1`), the
  same-1PI identity `F_Htt^(0)^2 = g_bare^2 / (2 N_c)` would require
  `F^2 != 1/6` at `N_c = 3`, contradicting (W1). This is exactly the
  parent runner's Section 6 cross-check, replicated on the new
  premise hash.
- **Block 8 — Static-source scan of parent note's load-bearing
  section.** Verifies that the auditable algebraic core (Section 4
  "Load-bearing step (class A)") does not invoke a record functional
  `I(.)`, a record additivity statement, a record collection, or a
  Record-axiom citation. Enumerates the phrase set
  `{"I(R_1", "I(R)", "scalar record", "record functional",
  "record-readout", "additive record", "additive scalar record",
  "MINIMAL_AXIOMS_2026-06-04"}`
  over the load-bearing section of the parent note and confirms zero
  matches inside the auditable core.
- **Block 9 — Record-axiom counterfactual.** Re-runs Blocks 1-5
  inside an explicit "Record axiom is asserted" outer scope and an
  explicit "Record axiom is not asserted" outer scope; verifies the
  load-bearing value `g_bare = 1` is identical in both runs. The
  counterfactual is a tautology at the calculation level (no
  Record-axiom content enters the rational substitution), which is
  precisely the substantive content of (C1).
- **Block 10 — Quantum/Lattice content preservation across memos.**
  Verifies that `MINIMAL_AXIOMS_2026-05-20.md` qubit / `Z^3` content
  is preserved verbatim in `MINIMAL_AXIOMS_2026-06-04.md` under the
  explicit names "Quantum" and "Lattice", and that the 2026-06-04
  memo's own Record-axiom scope statement explicitly excludes
  `log-det structure`, `source/action identification`, and
  `arbitrary observable identification`. (None of those are required
  for the parent's class-A substitution, but their absence in the
  Record-axiom scope is the substantive reason the substitution is
  Record-invariant.)
- **Block 11 — Cited-row status verification.** Verifies on the
  current audit ledger that
  `g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19` carries
  `audit_status=audited_clean` and
  `effective_status=retained_bounded` (W1 retained-grade source), and
  that its last invalidation reason is NOT
  `axiom_premise_changed:minimal_axioms:*` (i.e., (W1)'s row was not
  invalidated by the 2026-06-04 axiom-set change). Verifies the
  parent's own previous-audit snapshot records `audited_clean` with
  `load_bearing_step_class=A` and the runner-pass count `54`
  (matching the parent runner's reported total).
- **Block 12 — Four-route exact cross-check on `g_bare = 1`.**
  Computes `g_bare` four ways from the cited rational data: (i)
  positive square-root of `g_bare^2 = 2 N_c F^2 = 6 * 1/6 = 1`; (ii)
  exact rational solution of `g^2 / (2 N_c) = 1/6` at `N_c = 3`;
  (iii) unique positive `g_bare` for which the parent runner's
  grid-contradiction test fails (i.e., the unique non-contradictory
  grid point); (iv) the cited identity `g_bare^2 / 6 = 1/6` rearranged
  to `g_bare = +1`. Verifies all four routes give exactly
  `Fraction(1, 1)`.

Total: 12 blocks. The exact PASS / FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR. The audit lane decides whether to re-honor the prior
`audited_clean` verdict on the new premise hash; this companion only
supplies machine-checkable evidence on whether the new Record axiom
disturbs the parent's class-A algebraic step.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
`g_bare = 1` output, nor does it close the cascade-upstream
invalidations of `yt_ward_identity_derivation_theorem` and
`g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19`. Each of
those upstream rows must be examined independently against the new
axiom-set premise hash. Sister-row companions for upstream cascade
restoration are out of scope of this PR and are lodged separately as
the audit lane reaches them.

The two cited one-hop upstream premises that the parent and the
prior audit verdict named (the retained Ward Rep-B form-factor
identity (W1) and the candidate same-1PI coefficient identity (W2))
remain the parent's load-bearing upstream premises after this
companion lands and after the Record-axiom adoption. Restoring (W2)'s
retained-grade status remains out of scope of this companion exactly
as it is out of scope of the parent's class-A substitution itself.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` framework-sentence citations to
`MINIMAL_AXIOMS_2026-06-04.md`. Both memos preserve the Quantum
(`Cl(3,0)` / qubit) and Lattice (`Z^3`) content unchanged; the
2026-06-04 memo cites the 2026-05-20 memo as the "local-algebra
authority and historical source for the prior two-axiom wording." A
separate citation-migration PR (if desired) can refresh the parent
note's `Source` column; this companion is independent of that text
update and is content-only.

This companion's load-bearing-step invariance observation depends
only on:

- the Quantum and Lattice content being preserved across the two
  memos (verified in Block 10);
- the Record axiom adding a strictly additive non-overlapping
  statement (confirmed by direct reading of
  `MINIMAL_AXIOMS_2026-06-04.md` section "Record"); and
- the parent's load-bearing step being class-A rational substitution
  on cited identities, with no Record-axiom-typed content (verified
  in Blocks 1-9).

---

## References

- Parent note:
  [`G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md`](G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md)
- Parent runner (shared with the convention narrowing parent):
  `scripts/frontier_g_bare_canonical_convention_narrow.py`
- Prior audit-verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09`,
  `previous_audits[-1]` (`audited_clean`, `bounded_theorem`,
  load-bearing step class A, 3/5 judicial-panel majority, 2026-05-26,
  archived 2026-06-04 with
  `invalidation_reason=dep_weakened:g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19:retained_bounded->retained_pending_chain`,
  itself cascading from the upstream `axiom_premise_changed` on
  `yt_ward_identity_derivation_theorem`)
- One-hop upstream authorities (named by the parent's Section 3):
  - [`G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md`](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
    (currently `audit_status=audited_clean`,
    `effective_status=retained_bounded`)
  - [`G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`](G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md)
    (currently `audit_status=unaudited` via the
    `yt_ward_identity_derivation_theorem` cascade)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for the
  Quantum / Lattice content the parent uses):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit-lane authority statement:
  [`docs/audit/README.md`](audit/README.md)
- Sister-row companion (the template for this PR):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)

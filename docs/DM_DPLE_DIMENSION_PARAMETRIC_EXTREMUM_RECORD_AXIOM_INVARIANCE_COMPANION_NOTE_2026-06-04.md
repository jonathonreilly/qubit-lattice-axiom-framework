# DM DPLE: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing matrix-analysis content of
[`DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md`](DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md)
is invariant under the 2026-06-04 Record-axiom adoption in
`MINIMAL_AXIOMS_2026-06-04.md`. It is not a new theorem claim, not a
status promotion, and not an attempt to perform re-audit work. If the
audit pipeline seeds this file, it is a meta companion row; the audit
lane still sets `audit_status`, and pipeline-derived `effective_status`
remains downstream of that authority.
**Companion target:** `dm_dple_dimension_parametric_extremum_theorem_note_2026-04-19`
(parent note
`docs/DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md`,
load-bearing score = 9.99).
**Primary companion runner:**
[`scripts/audit_companion_dm_dple_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_dm_dple_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_dple_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_dple_record_axiom_invariance_2026_06_04.txt)

---

## 0. Why this companion exists

The parent theorem `dm_dple_dimension_parametric_extremum_theorem_note_2026-04-19`
is a standalone matrix-analysis statement on linear Hermitian pencils
`H(t) = H_0 + t H_1`:

> Along the linear Hermitian pencil on `Herm(d, C)`, the observable
> `W(t) = log|det H(t)|` has at most `floor(d/2)` interior Morse-index-0
> critical points; at `d = 3` the upper bound is exactly 1, making the
> `F_d` selector a clean binary discriminator iff `d = 3`. On the
> retained DM A-BCC chart with `H_0 = H_base` and `H_1 = J_*`, the
> `F_3` selector reproduces the retained `F4` condition on all four
> basins `{1, N, P, X}`.

The parent's load-bearing arithmetic surface is pure finite-dimensional
matrix analysis: Jacobi's formula, the Faddeev-LeVerrier identity for
`det H(t)`, Sylvester signature counting on the Hermitian pencil, and
the elementary Morse-counting bound on the number of local minima of a
real polynomial of degree `d`. No record functional `I(.)`, no scalar
record-readout statement, no log-det record bridge appears anywhere in
the parent's load-bearing chain (Sections 1-4 and runner T1-T7 of the
parent note).

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) adds a strictly additive scalar record-readout statement to
the framework axiom set. This companion documents that the parent's
load-bearing matrix-analysis content is independent of the Record
axiom, so that any future audit verdict on the parent's current
`unaudited` row does not need to reconsider record-axiom content as
a possible source of arithmetic change. The companion is structural
evidence, not a re-audit.

This companion is therefore audit-friendly evidence that the parent's
substantive arithmetic content is unaffected by the Record axiom. It
is not a re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide whether (and at what scope) to evaluate the
parent under the new framework axiom set.

---

## 1. Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the DPLE load-bearing arithmetic.**
The parent's load-bearing arithmetic surface (Sections 1-4 and runner
T1-T7) depends only on:

1. the polynomial-degree identity `deg_t det(H_0 + t H_1) = d` for
   `H_0, H_1 in Herm(d, C)` (Jacobi / Faddeev-LeVerrier);
2. the elementary Morse-counting bound: a real polynomial of degree
   `d` has at most `floor(d/2)` interior local minima;
3. the Sylvester signature `sign(det H(t))` on the linear Hermitian
   pencil and its `d = 3` quadratic-discriminant specialization
   `Delta_ret = c_2^2 - 3 c_1 c_3`;
4. the fixed `H_base` and `J_*` numerical operators of the retained
   DM A-BCC chart (inputs to T3, T6; not modified by this companion).

None of items 1-4 use the Record axiom's additive scalar
record-readout content. They use only finite-dimensional matrix
analysis (Jacobi's formula, Faddeev-LeVerrier, Cayley-Hamilton,
Sylvester inertia, and the elementary one-variable Morse counting
theorem) plus the retained DM A-BCC chart inputs that the parent
itself imports.

**(C1) is the only auditable companion observation.** Bridges from
the matrix-analysis `F_3 = F4` reduction to the broader DM A-BCC
basin-selection physics, and to any downstream observable lane,
remain explicitly out of scope, exactly as in the parent note's
"Honest gap" Section 5.2.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the retained linear path from `H_base` to `H_base + J_*`
  remains inherited from the retained P3 Sylvester linear-path
  signature theorem);
- assert anything about Record-axiom content or its scope;
- re-audit `dm_dple_dimension_parametric_extremum_theorem_note_2026-04-19`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- change the parent's runner `scripts/frontier_dm_dple_theorem.py`
  or its expected PASS=19 FAIL=0 totals.

The audit lane decides whether (C1) is sufficient evidence to inform
a future verdict on the parent's row, and at what scope.

---

## 2. The Record axiom is not used by the load-bearing chain

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It works exclusively at the level of:

- `p(t) = det H(t)` as a degree-`d` polynomial in `t` (Section 1);
- `W(t) = log|det H(t)|` as a real function with interior critical
  points characterized by `W'(t) = Tr[H(t)^{-1} H_1]` (Section 2.1);
- the algebraic Morse bound `floor(d/2)` on interior local minima
  (Section 2.2);
- the cubic-discriminant `Delta_ret = c_2^2 - 3 c_1 c_3` for the
  `d = 3` specialization (Section 3.1);
- explicit numerical evaluation on the four DM A-BCC basins
  `{1, N, P, X}` (Section 3.2).

The `W(t) = log|det H(t)|` observable is a deterministic
matrix-analysis functional of `H(t)`; it is not a "record functional"
in the Record-axiom sense (no record collection, no record
sub-additivity question, no scalar-readout disjoint-union axiom is
invoked). The Record axiom adds an additive scalar functional over
record collections; it does not modify (and is not modified by) the
polynomial-degree identity, the Morse bound, the Sylvester signature,
or the four basin evaluations. So every arithmetic value computed in
Sections 1-4 and reproduced in runner tasks T1-T7 is invariant under
the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only the
finite-dimensional matrix-analysis content of the parent, and a
"Record-axiom counterfactual" block confirms that every parent value
(degree-`d` polynomial coefficients, Morse counts, basin-evaluation
F_3 outcomes, `d = 3` binary-selector histogram) is unchanged whether
or not a Record-axiom statement is appended.

---

## 3. Companion runner block plan

`scripts/audit_companion_dm_dple_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the DPLE load-bearing chain.
Each block runs as an independent numeric/algebraic check; nothing is
hard-coded against an expected target beyond standard matrix-analysis
identities and the parent's fixed DM A-BCC chart. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Polynomial-degree identity. Verifies
`deg_t det(H_0 + t H_1) = d` for `d in {2, 3, 4, 5}` over 50 random
Hermitian pairs per `d`. Reproduces parent's T1 logic under a
Record-axiom counterfactual scope.

Block 2 — Morse bound `floor(d/2)`. Verifies on 200 random
Hermitian pairs per `d` that the interior Morse-idx-0 count on
`(0, 1)` does not exceed `floor(d/2)`. Reproduces parent's T2 logic.

Block 3 — `F_3 = F4` on DM A-BCC basins. Re-runs parent's T3 on the
fixed `H_base, J_*` chart for all four basins; verifies the expected
pattern `{Basin 1: True, Basin N: False, Basin P: False,
Basin X: False}` and reproduces the basin-1 unique-True result.

Block 4 — `d = 3` quadratic discriminant. Computes
`Delta_ret = c_2^2 - 3 c_1 c_3` for each of the four basins; verifies
the parent's signs (`+7.80, -10.11, +458.7, -4.7e6`) to two
significant figures.

Block 5 — `d = 3` binary-selector histogram. Over 500 random pairs,
verifies that the interior Morse-idx-0 count is in `{0, 1}` for at
least 95% of pairs (the binary-selector property unique to `d = 3`).

Block 6 — `d = 2` vacuous-signature check. Verifies that both
`c_2 > 0` and `c_2 < 0` cases appear in random `d = 2` pairs (the
parent's T5 "F_2 vacuous" check).

Block 7 — `d = 4` fragmentation. Random-searches for a `d = 4`
Hermitian pair with `>= 2` interior Morse-idx-0 CPs in `(0, 1)`
(parent's T4). Pass if found within a bounded search budget.

Block 8 — Sylvester signature consistency. For each basin, computes
the sign of `p(t)` at `t = 0, 0.5, 1.0` and verifies that the parent's
`sign(p(t_*)) = sign(c_0)` consistency criterion can be evaluated
purely from matrix-analysis output (no record functional appears).

Block 9 — Static-source scan: zero Record-axiom tokens in parent's
load-bearing sections. Confirms the phrase set
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04", "record axiom"}` has zero matches in
Sections 1-4 and Section 6 (runner verification) of the parent note.

Block 10 — Record-axiom counterfactual. Recomputes parent's T1, T3,
T6 outputs inside an explicit "Record axiom is asserted" outer scope
and an explicit "Record axiom is not asserted" outer scope; verifies
identical numeric outputs in both scopes. The counterfactual is a
tautology at the calculation level (no Record-axiom content enters
the matrix-analysis steps), which is the substantive content of (C1).

Block 11 — Axiom-name vs axiom-content separation. Verifies that the
new `MINIMAL_AXIOMS_2026-06-04.md` memo preserves the Quantum and
Lattice content of the prior `MINIMAL_AXIOMS_2026-05-20.md` memo,
and that the Record axiom is explicitly an additive scalar
record-readout statement (non-overlapping with matrix-analysis
content). Reuses the YT-Ward companion's verification pattern.

Block 12 — `F_3` reduction sanity. Verifies that on the parent's
DM A-BCC chart the quadratic-discriminant test
`Delta_ret > 0  AND  t_* in (0, 1)  AND  p(t_*) > 0` agrees with the
direct interior Morse-idx-0 count (per parent's Section 3.3 "Formal
reduction" claim). Pure matrix analysis; no Record-axiom invocation.

Total: 12 blocks. The exact PASS/FAIL count is printed at runtime and
recorded in the SHA-pinned cached runner output.

---

## 4. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to honor or test the prior judicial
material on the new premise hash; this companion only supplies
machine-checkable evidence on whether the new Record axiom disturbs
the load-bearing chain (it does not).

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream consumer of the parent's `F_3`
selector or to the broader DM A-BCC closure question (the parent's
Section 5.2 explicit gap remains open and is unchanged by this
companion). Each downstream claim must be examined independently
against the new axiom-set premise hash. The cohort of other rows
recently affected by the same Record-axiom adoption are out of scope
of this companion; each is examined separately as the audit lane
reaches them.

---

## 5. Audit-ordering and integration

This companion does not migrate citations in the parent note; the
parent note does not cite either `MINIMAL_AXIOMS_*` memo directly
(it is a standalone matrix-analysis theorem). The Record-axiom
invariance of the parent's content is a content-level statement
about the parent's load-bearing chain, not a citation refresh.

This companion's invariance observation depends only on:

- the Quantum and Lattice content being preserved across the two
  memos (verified in Block 11; reuses YT-Ward companion's pattern);
- the Record axiom adding a strictly additive non-overlapping
  scalar-record statement (confirmed by direct reading of
  `MINIMAL_AXIOMS_2026-06-04.md` §"Record" and the explicit scope
  exclusions in that memo);
- the parent's load-bearing chain consisting exclusively of
  finite-dimensional matrix analysis on the DM A-BCC chart
  (verified by static-source scan in Block 9 and full numeric
  re-evaluation in Blocks 1-8, 10, 12).

No new admission, no new import, no axiom-set change is introduced
by this companion. The companion is content-only audit-friendly
evidence and obeys the same audit-lane discipline as PR #2616
(`yt_ward` Record-axiom-invariance companion).

---

## 6. References

- Parent note:
  [`DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md`](DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md)
- Parent runner:
  `scripts/frontier_dm_dple_theorem.py` (PASS=19 FAIL=0)
- Audit ledger row: `dm_dple_dimension_parametric_extremum_theorem_note_2026-04-19`
  in `docs/audit/data/audit_ledger.json`
- Sibling companion (pattern source):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Retained-path dependency (inherited by parent, unaffected by this
  companion):
  [`DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md`](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md)
- Uhlig 1982 (Linear Algebra Appl. 46 — sign-characteristic
  classification for Hermitian pencils; structural backbone of parent's
  `d = 3` reduction). Milnor, Morse Theory (1963), for the elementary
  one-variable Morse bound on interior local minima.

# DM A-BCC Five-Basin Chamber+DPLE Support: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing finite arithmetic in
[`DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md`](DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. The audit lane still sets `claim_type`, `audit_status`,
and the pipeline-derived `effective_status` independently of this
companion.
**Companion target:** `dm_abcc_five_basin_chamber_dple_support_theorem_note_2026-04-21`
(parent note `docs/DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md`).
**Primary companion runner:**
[`scripts/audit_companion_dm_abcc_five_basin_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_dm_abcc_five_basin_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_abcc_five_basin_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_abcc_five_basin_record_axiom_invariance_2026_06_04.txt)

---

## 0. Why this companion exists

The parent narrow theorem
`dm_abcc_five_basin_chamber_dple_support_theorem_note_2026-04-21`
records a finite arithmetic statement on five explicitly tabulated basin
coordinate tuples:

> On the corrected retained five-basin chart
> `{Basin 1, Basin N, Basin P, Basin 2, Basin X}`, the chamber filter
> `q_+ + delta >= sqrt(8/3)` admits exactly `{Basin 1, Basin 2, Basin X}`;
> the DPLE selector `F_4` admits exactly `{Basin 1}`; the composition
> `chamber ∩ F_4` selects Basin 1 uniquely.

This is a finite numeric / cubic-discriminant verification on five 3-tuples
of real numbers, evaluated against a Hermitian base `H_BASE` (a fixed
3x3 complex matrix), three structural translation directions
`(T_M, T_D, T_Q)`, and a fixed structural inequality
`q_+ + delta >= sqrt(8/3)`. The parent runner (`scripts/frontier_dm_abcc_five_basin_chamber_dple_support_2026_04_21.py`)
verifies each step by three independent routes (closed-form discriminant,
Newton iteration, direct sampling).

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash.
Any row whose chain depended on the previous `minimal_axioms` hash was
mechanically invalidated by the audit pipeline via
`invalidation_reason=axiom_premise_changed:minimal_axioms:...`,
returning the row to unaudited effective status.

This companion records, for the audit lane, that the parent's
load-bearing arithmetic is **independent of the Record axiom**: it
performs cubic-determinant evaluations, a linear inequality check, and
discriminant arithmetic on explicitly tabulated real 3-tuples. The
Record axiom — "the scalar record functional is additive over disjoint
record collections, `I(R_1 sqcup R_2) = I(R_1) + I(R_2)`, with
`I(empty) = 0`" — is neither used nor invoked anywhere in the chamber
filter, the DPLE discriminant, the Newton/sampling cross-checks, or the
final composition `chamber ∩ F_4 = {Basin 1}`. The numeric output is
identical under both "Record axiom asserted" and "Record axiom not
asserted" outer scopes.

This companion is therefore audit-friendly evidence that the prior
substantive content survives the axiom-set change. It is not a re-audit
and does not promote status; it documents the load-bearing-step
dependency surface in machine-checkable form so the audit lane can
decide whether to honor or re-test the prior verdict on the new premise
hash.

---

## 1. Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the corrected five-basin
`chamber ∩ F_4 = {Basin 1}` finite-arithmetic verification.**

The parent's load-bearing finite arithmetic depends only on:

1. five explicitly tabulated basin 3-tuples
   `(m, delta, q_+) ∈ R^3` for `{Basin 1, Basin N, Basin P, Basin 2, Basin X}`;
2. one explicit Hermitian 3x3 complex base matrix `H_BASE`;
3. three explicit real 3x3 structural translation matrices
   `(T_M, T_D, T_Q)`;
4. the explicit structural inequality `q_+ + delta >= sqrt(8/3)`
   (chamber filter);
5. the explicit cubic-discriminant condition `Delta := c_2^2 - 3 c_1 c_3 > 0`
   plus an interior Morse-index-0 critical point `t_* ∈ (0,1)` with
   `p(t_*) > 0` (DPLE selector `F_4`);
6. standard finite-dimensional linear algebra (determinant, real cubic
   discriminant, Newton iteration, linear inequality).

None of items 1-6 use the Record axiom's additive scalar record-readout
content. The chamber filter is a linear inequality on two coordinates
of the basin tuple; the DPLE selector is the sign of a real cubic
discriminant plus a localized critical-point check on a real cubic
polynomial `p(t) := det(H_BASE + t J_B)` whose coefficients are obtained
by standard 3x3 determinant evaluation at four sample points.

**(C1) is the only auditable companion observation.** The broader
five-basin source-chart derivation — i.e. *why* the chart contains
exactly these five basins, and *why* `F_4` has the structural form
written above — is explicitly out of scope of this companion, exactly
as in the parent note's "Honest auditor read" and "Open upstream gaps"
sections.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the corrected five-basin chart, the H_BASE matrix, the
  structural inequality, and the `F_4` selector form remain imported
  from upstream authorities cited in the parent's dependency-repair
  section);
- assert anything about Record-axiom content or its scope;
- re-audit `dm_abcc_five_basin_chamber_dple_support_theorem_note_2026-04-21`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to honor the
previous judicial verdict or whether a fresh per-row audit is warranted
on the new premise hash.

---

## 2. The Record axiom is not used by the load-bearing arithmetic

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing arithmetic defines no record-readout surface,
asks no question about scalar record additivity, and writes no record
functional `I(.)`. It performs three operations:

- **chamber filter** (Section 2 of the parent): evaluate the real
  scalar `q_+ + delta` for each basin tuple and compare to the constant
  `sqrt(8/3)`;
- **DPLE selector `F_4`** (Section 3 of the parent): build the cubic
  `p(t) = det(H_BASE + t J_B)` by evaluating the determinant at four
  sample points `t ∈ {-1, 0, 1/2, 1}`, solve for the four cubic
  coefficients `(c_0, c_1, c_2, c_3)` by inverting a 4x4 Vandermonde
  system, compute the discriminant `c_2^2 - 3 c_1 c_3`, and check for
  an interior Morse-index-0 critical point;
- **composition** (Section 4 of the parent): intersect the chamber
  survivor set with the `F_4` passer set.

All three operations are finite-dimensional linear-algebra and
elementary real-cubic identities. None of them invokes a record
collection, an additivity statement over disjoint collections, an
`I(.)` functional, or any record-readout structure.

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) determinant evaluation on a fixed
3x3 complex matrix, the sign of a real cubic discriminant, a Newton
iteration on a real cubic, direct sampling of a real cubic on `[0,1]`,
or a linear inequality on a 3-tuple of real numbers. So the corrected
chamber survivor set, the DPLE passer set, and the composition
`chamber ∩ F_4 = {Basin 1}` are invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only the parent's
explicitly tabulated finite data plus standard finite-dimensional
algebra, and a "Record-axiom counterfactual" block confirms that the
chamber survivor set, the `F_4` passer set, and the final composition
are identical whether or not a Record-axiom statement is appended.

---

## 3. Companion runner block plan

`scripts/audit_companion_dm_abcc_five_basin_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the corrected five-basin
chamber+DPLE composition. Each block runs as an independent
numeric/algebraic check; nothing is hard-coded against an expected
target value beyond the explicitly tabulated parent data and standard
finite-dimensional algebra. The runner reports `PASS` / `FAIL` per
check; the cached output records the run.

Block 1 — Parent data fingerprint. Verifies the five basin tuples and
the `(H_BASE, T_M, T_D, T_Q, GAMMA)` constants reproduce the
finger-printable values quoted in the parent note (Sections 1, 2, 3).
This is the standard-data sanity gate; no Record axiom content is
invoked.

Block 2 — Chamber filter on all five basins. Computes `q_+ + delta`
for each basin and compares to `sqrt(8/3)`. Verifies chamber survivor
set equals `{Basin 1, Basin 2, Basin X}` exactly. Uses only the
explicit basin tuples and the constant `sqrt(8/3)`; no Record axiom
content is invoked.

Block 3 — Cubic coefficients for every basin. Builds the cubic
`p(t) = det(H_BASE + t J_B)` by evaluating the determinant at the
four sample points `t ∈ {-1, 0, 1/2, 1}` and solving the resulting
4x4 Vandermonde system for `(c_0, c_1, c_2, c_3)`. Cross-checks the
reconstructed cubic against a finer-grid sampling
(`max |p(t) - sum c_k t^k| < 1e-10`). Uses only standard
finite-dimensional linear algebra; no Record axiom content is invoked.

Block 4 — Basin 2 discriminant negativity. Verifies
`Delta_2 := c_2^2 - 3 c_1 c_3 < 0` for Basin 2 (parent's Section 3
quoted value `-1.9392... x 10^7`). Confirms `F_4(Basin 2) = FALSE` by
discriminant alone; cross-checks the closed-form discriminant against
the no-real-roots property of `p'(t) = c_1 + 2 c_2 t + 3 c_3 t^2`.

Block 5 — F_4 on all five basins via three independent routes. For
each basin, evaluates `F_4` by (a) closed-form discriminant +
critical-point classification, (b) Newton iteration on `p'(t)` from
ten seed points, (c) direct sampling of `p(t)` on a fine grid. Verifies
all three routes agree with the parent's reference
`{Basin 1: TRUE, Basin N: FALSE, Basin P: FALSE, Basin X: FALSE,
Basin 2: FALSE}` exactly.

Block 6 — Corrected composition. Intersects chamber-survivor set with
`F_4`-passer set and verifies the result is `{Basin 1}`. Reproduces
the parent's Section 4 corrected composition theorem.

Block 7 — Static-source scan of parent note's load-bearing core. The
scan enumerates the phrase set `{"I(R_1", "I(R)", "scalar record",
"record functional", "record-readout", "additive record",
"additive scalar record", "MINIMAL_AXIOMS_2026-06-04"}` over the
parent note's Section 1 through Section 4 (chamber filter, basin 2
discriminant, composition theorem) and confirms zero matches inside
the load-bearing core. (The phrase "It records" in the parent's
Section 6 / dependency-repair sections is graph-bookkeeping prose,
not a Record-axiom functional invocation.)

Block 8 — Record-axiom counterfactual. Re-runs Blocks 2-6 inside an
explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies the chamber
survivor set, the `F_4` passer set, and the final composition
`chamber ∩ F_4` are identical in both runs. The counterfactual is a
tautology at the calculation level (no Record-axiom content enters
the determinant / discriminant / inequality / Newton / sampling
steps), which is precisely the substantive content of (C1).

Block 9 — Axiom-name vs axiom-content separation. Verifies that
`MINIMAL_AXIOMS_2026-06-04.md` preserves the Lattice (`Z^3` site set,
nearest-neighbor cubic adjacency) and Quantum (`A_x ~= M_2(C)`,
equivalently `Cl(3,0)`) content from `MINIMAL_AXIOMS_2026-05-20.md`,
and that the Record axiom is a third, strictly additive,
non-overlapping statement whose own scope-disclaimer explicitly
excludes log-det / source-action / measurement / Born / observable /
`AC_phi_lambda` / theta content. Confirms that none of the excluded
content is invoked by the load-bearing arithmetic above.

Block 10 — Composition uniqueness in three independent routings.
Computes the final composition `chamber ∩ F_4` three independent
ways: (a) using the closed-form `F_4` results; (b) using the Newton
`F_4` results; (c) using the sampled `F_4` results. Verifies all
three routes yield `{Basin 1}` exactly. Confirms the corrected
composition is robust against the route used to evaluate `F_4`.

Total: 10 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output. Target: 40-50 PASS, 0 FAIL.

---

## 4. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to honor the prior verdict on the new
premise hash; this companion only supplies machine-checkable evidence
on whether the new Record axiom disturbs the load-bearing finite
arithmetic.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output, nor to any of the parent's upstream-source authorities (the
chamber-bound source cubic, the four-basin chamber+DPLE authority, the
five-basin enumeration-completeness authority, all explicitly
registered as open upstream gaps in the parent's
"Audit dependency repair links" section). Each upstream-source row
must be examined independently against the new axiom-set premise hash.

This companion does **not** speak to:

- the derivation of the five-basin source chart from `Cl(3)/Z^3` alone
  (parent's open upstream gap);
- the finer right-sensitive microscopic selector law (parent's
  Section 5.2);
- the chamber-bound source cubic (parent's open upstream gap);
- the four-basin chamber+DPLE source authority (parent's open upstream
  gap);
- the five-basin enumeration completeness (parent's open upstream gap);
- any other ledger row.

---

## 5. Audit-ordering and integration

This companion does not migrate the parent's `MINIMAL_AXIOMS_2026-05-20.md`
references (if any) to `MINIMAL_AXIOMS_2026-06-04.md`. The parent note
does not cite either memo directly in its load-bearing core; its
content is finite arithmetic on explicitly tabulated data. A separate
citation-migration PR (if desired) can refresh the parent note's source
column; this companion is independent of that text update and is
content-only.

This companion's load-bearing-step invariance observation depends only
on:

- the Quantum and Lattice content being preserved across the
  2026-05-20 and 2026-06-04 minimal-axioms memos (verified in Block 9);
- the Record axiom adding a strictly additive non-overlapping
  statement (confirmed by direct reading of `MINIMAL_AXIOMS_2026-06-04.md`
  §"Record");
- the parent's load-bearing arithmetic using only finite-dimensional
  linear algebra on explicitly tabulated finite data (verified in
  Blocks 2-6, 10).

---

## 6. Cohort context

This is one row in the cohort of ledger rows mechanically invalidated
by the 2026-06-04 Record-axiom adoption via the
`axiom_premise_changed:minimal_axioms:...` invalidation. The remaining
rows in that cohort are out of scope of this PR; each should be examined
independently as the audit lane reaches them. The
`yt_ward_identity_derivation_theorem` row was the first such companion
landed (PR #2616, 48/0 PASS); this `dm_abcc_five_basin_chamber_dple_support_theorem_note_2026-04-21`
companion (load-bearing score 6.70) follows the same shape (one
companion note + one paired runner + one cached log, `claim_type=meta`,
no status promotion).

---

## 7. References

- Parent note:
  [`DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md`](DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- Parent runner:
  [`scripts/frontier_dm_abcc_five_basin_chamber_dple_support_2026_04_21.py`](../scripts/frontier_dm_abcc_five_basin_chamber_dple_support_2026_04_21.py)
- Sister Record-invariance companion (first landed):
  [`docs/YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for Lattice and
  Quantum content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/README.md`](audit/README.md)

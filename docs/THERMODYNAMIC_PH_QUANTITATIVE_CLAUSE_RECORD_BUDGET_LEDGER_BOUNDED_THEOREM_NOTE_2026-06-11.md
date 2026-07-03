# In the Broadcast Record Model, Realized Record Depth Lower-Bounds the Boundary Register-Sector Deficit: the Past Hypothesis's Quantitative Clause as a Consistency Relation Among Realized-State Data (Bounded)

**Date:** 2026-06-11
**Type:** bounded_theorem (owner-directed: the thermodynamic-PH strike)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_thermodynamic_ph_record_budget_ledger_2026_06_11.py`
**Cache:** `logs/runner-cache/frontier_thermodynamic_ph_record_budget_ledger_2026_06_11.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=18 FAIL=0` — exact,
deterministic, no MC, memory-trivial.

## The question — a quantitative clause of the past hypothesis

The PH dissection so far: the arrow's **direction** is derived
([`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md),
`retained_bounded` at this writing); the boundary's **existence** is structural
in-sector with non-emptiness self-instantiating
([`PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md`](PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md),
in review). What remains is the clause physicists usually *mean* by the past
hypothesis: the **quantitative/thermodynamic** content — the boundary was
*low-entropy*, with room to grow (Penrose's `10^10^123`). This note converts that
clause, within the broadcast record model, into a CONSISTENCY RELATION among
realized-state data: the realized record depth lower-bounds the SAME realized
boundary's register-sector deficit.

## The ledger (runner `PASS=18`)

**(L1) The full-alignment coincidence.** In the broadcast model, each clean record
(connected correlator > 1/2) consumes exactly one Z-aligned pure register: counts
`[0,1,2,3]`, blanks `[3,2,1,0]`, `ΣᵢSᵢ = [0,1,2,3]` bits; at full Z-alignment, record count and marginal-sum entropy coincide -- a FULL-ALIGNMENT coincidence, not a general identity: off full alignment the per-register production is the smooth binary entropy H(cos^2 t) while the count is a thresholded reading of the same correlator (divergence up to ~1.8 bits exhibited in-runner). Anti-aligned
(`|1⟩`) registers are equally consumable: the resource class is **Z-aligned
purity**, not the `|0⟩` label. Disclosure: it un-produces under the inverse step
-- generated total correlation, not Clausius/second-law production (no bath here).

**(L2) Deficit is necessary, not sufficient.** Load-bearing atom: deficit is NECESSARY, not sufficient -- alignment+purity is what cashes; this sharpens the entropy-only past-hypothesis reading. An X-aligned pure register carries the *same* 1-bit
deficit below max-mixed and yields **zero** records (CNOT-transparent; zero
marginal-sum entropy change). A maximally-mixed register (zero deficit) yields
zero. The specific clean-reset transfer channel (arbitrary old fragments -> clean broadcast, no sink) has rank 2, not 16. L2d: alignment is basis-relative and unitarily mutable: a closed Hadamard layer regenerates aligned blanks from X-pure registers (exhibited), so the invariant resource statement is the basis-free register DEFICIT below max-mixed; alignment is the form in which the fixed broadcast instrument can cash it.

**(L3) The sink escape conserves the ledger.** The landed reset-with-sink map
`(s,e,g) → (s, g⊕s, e)` is an exact permutation (re-proved), and the sink's blanks
are **consumed 1:1** (afterwards the sink holds the old fragment word). The regress
is priced: **total records <= total initial register deficit (cashable as aligned
blanks)** across the fragment + sink hierarchy, with the equality case exhibited
(budget 6 -> 6 records, exhausted).

**(L4) The quantitative clause as a consistency relation.** Across every tested
realized state (varying pointer and register preparations, including partial
superpositions, a partially mixed Z pointer, Hadamard-regenerated X-pure
registers, and a one-step strict-gap case), the one-directional implication
`N <= register_deficit(boundary)` holds invariantly while `N` itself varies and is
**registered data** (the primitive's slot, correctly). So:

> **A realized history with record depth `N` had a boundary whose register-sector deficit was at least `N` bits.** The boundary was wound up by AT LEAST as much as the world has registered — a one-directional bound (strict gap exhibited; the Penrose regime is the huge-gap case).

This is a CONSISTENCY RELATION among realized-state data: both `N` and the
boundary deficit are read off the same realized state, and the theorem is the
implication between them — which passes the realized-state primitive's
counterfactual test (it holds invariantly across every tested realized state)
while `N` and the deficit individually remain registered data. The thermodynamic
past hypothesis in its SPECIALNESS form — that the boundary is low-entropy
*among permitted states* (Penrose's room) — is NOT derived here: a specialness
claim needs a measure over permitted states, exactly what the realized-state
primitive forbids supplying. The existing carve-out ('the past hypothesis is a
separate, stronger input') stands unchanged; this note refines only the
BOOKKEEPING of its quantitative clause, mirroring the append-only reduction's
residual discipline (PR #3583).

**(L5) Disclosure — marginal-sum entropy versus fine-grained entropy.** Global
fine-grained entropy is constant throughout (unitary; checked at zero every
step). The thermodynamic reading is the register-sector **resource ledger**
(register deficit / marginal-sum entropy), and the coarse-fine gap is exactly the
generated correlations (marginal-sum 3 bits vs joint fragment entropy 1 bit at
full broadcast — nothing hidden). This is the standard Landauer-style coarse
accounting, stated as such.

## What this does and does not claim

- Not claimed: a heat bath, temperature, rate, cost law, or any dynamical
  *preparation* of the boundary; a derivation of `N`; global fine-grained entropy
  growth; anything outside the broadcast record model (model scope disclosed —
  the framework's record-formation exemplar, the arrow note's own system); any
  measure over permitted states; any specialness/atypicality of the realized
  boundary; equality (the bound is one-directional).
- The PH ledger after this note: **direction derived + existence structural
  in-sector + non-emptiness self-instantiating + the quantitative clause as a
  derived CONSISTENCY RELATION (deficit >= record depth) — with the specialness
  claim untouched and separately registered.** The named open residuals: the
  model scope (broadcast-class record formation), and the realized state itself.
- L1's monotone count and the max-mixed/generic controls reproduce the arrow
  note's points (R_tot growth; I/d flat; generic states form nothing) — the new
  atoms here are the alignment-vs-deficit separation (L2), the sink-ledger
  conservation (L3), and the deficit bound + consistency-relation reading (L4).
- Dependencies and statuses:
  [`RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md`](RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md)
  and
  [`RECORD_RESET_SINK_ENTROPY_LEDGER_2026-06-05.md`](RECORD_RESET_SINK_ENTROPY_LEDGER_2026-06-05.md)
  are **unaudited** at this writing — their load-bearing facts (the permutation,
  the bit accounting) are **re-proved in-runner**. The arrow note
  ([`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md))
  is `retained_bounded`; the append-only reduction
  ([`PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md`](PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md))
  is in review. Statuses are pipeline-derived.
- Standard math (method only): von Neumann entropy; partial traces; permutation
  maps; matrix rank; Landauer-style resource accounting.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout.
The audit lane grades.

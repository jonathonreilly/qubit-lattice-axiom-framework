# Record-Preservation Conserves the Within-Sector Measure: the Breaking Is Not a Relaxation Outcome (Bounded Theorem)

**Date:** 2026-06-15
**Type:** bounded theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:** [`scripts/frontier_record_preservation_conserves_within_sector_measure_2026_06_15.py`](../scripts/frontier_record_preservation_conserves_within_sector_measure_2026_06_15.py)
**Cached output:** [`logs/runner-cache/frontier_record_preservation_conserves_within_sector_measure_2026_06_15.txt`](../logs/runner-cache/frontier_record_preservation_conserves_within_sector_measure_2026_06_15.txt)

## Claim

Stage 1
([`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md))
forced the record-preserving generation generator to the circulant form `H = a I + b C + conj(b) C^T`
with `[H, C] = 0`, hence `[H, S] = 0` for the einselected pointer `S = C + C^2` (spectrum `{2, -1, -1}`).
This note works out the dynamical consequence for the within-sector measure.

> **Theorem.** A record-preserving generation dynamics — forced block-diagonal in the
> singlet (+) doublet decomposition by `[H, S] = 0` — **conserves** the realized state's
> singlet/doublet block weight under `H`-evolution (a genuine conservation law: a
> non-block-diagonal generator instead changes the weight). The einselected **2-sector
> record** `D_S` (dephasing onto `{P_singlet, P_doublet}`) does **not** resolve the
> 2-dimensional doublet, so it **preserves** the within-doublet structure (it does not
> erase the doublet-internal phase); only a finer character-basis record would touch it.
> **Corollary.** The within-sector measure `(r, delta)` is therefore conserved/preserved
> by the record-preserving dynamics, **not** a relaxation outcome of it.

The runner certifies this exactly (9/9): block weight conserved to `< 1e-9` (max spread `6e-15` over 8
states), while a non-record-preserving control `H'` (`[H', S] != 0`) changes the block weight by
`~0.70` — the conservation is special to record-preservation. The 2-sector record `D_S` leaves the
within-doublet coherence unchanged (`|D_S - raw| < 1e-15`), whereas a finer character-basis record
reduces it (`raw ~ 0.27` vs `~ 0.19`) — confirming `D_S` preserves the within-sector phase rather than
erasing it. `D_S` is trace-preserving and idempotent.

> **Correction note.** An independent verification pass flagged an earlier draft that claimed the record
> *erases* the within-sector phase: that holds only for the *finer character-basis* record, not for the
> einselected *2-sector* record `D_S`, which preserves it. Two tautological gates (spectrum-invariance,
> `r > 0`) were also removed. The corrected, narrower claim is **conservation + preservation**, certified above.

## Significance

This characterizes, from the dynamics side, what the record-preserving flow does to the within-sector
measure: it **conserves** it. Combined with Stage 1 (the form is forced; the couplings are the dial),
the within-sector measure `(r, delta)` is neither produced nor relaxed by the record dynamics — it is
the **registered/coupling data** the realized state carries. The breaking is thereby **localized**: it
lives in the forced-form **couplings** (the supplied sector dial) and the **initial condition** (the
past hypothesis), both registered/supplied — not in the record-formation dynamics. This is consistent
with, and gives a dynamical reading of, the `realized_state` primitive (the axioms select no state; the
within-sector pattern is registered).

## Boundary (honest)

- A **conservation/preservation** result for **record-preserving** (block-diagonal) dynamics and the
  **einselected 2-sector record**. It does **not** claim erasure (that is the finer-record statement),
  and it does **not** claim no dynamics of any kind can relax `(r, delta)` — only that record-preserving
  dynamics conserves the block weight and the 2-sector record preserves the within-doublet phase.
- It **does NOT force r=1/2** and **does NOT derive delta**: `r` and `delta` are free coupling labels,
  conserved/preserved but unfixed. The couplings (a, |b|, delta) are the supplied sector dial.
- Inputs: the Stage-1 forced form and the einselected pointer `S`. The localization to the initial
  condition is consistent with the past-hypothesis admission
  (`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`).

## No-Go discipline (corollary scope)

- **N1 (routes).** A relaxation derivation of `(r, delta)` from record-preserving dynamics is blocked at
  the conservation step (block weight conserved; the 2-sector record preserves the within-doublet phase).
  A non-block-diagonal route exists but is not record-preserving (control `H'`, `[H', S] != 0`).
- **N5 (rhetoric).** The corollary "not a relaxation outcome" is asserted only for **record-preserving**
  dynamics on the generation block; it is not a universal no-relaxation claim and not a claim about other
  sectors. "Conserves/preserves" is used at the certified resolution, never "erases".
- **N7 (steelman).** A weak symmetry-breaking coupling that moved the block weight or the within-doublet
  structure would break `[H, S] = 0` and so is not record-preserving — it changes which record forms.

## Dependencies and citations

**Load-bearing (markdown-link = dependency edge):**

- [`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md)
  — the forced form and `[H, S] = 0` (Stage 1).
- [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
  — the einselected pointer `S = C + C^2` and the 2-sector record.

**See-also (backticked, no dependency edge):**
`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11`, `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`.

## Forbidden-imports check

No new axiom. Uses the Stage-1 forced form and the retained einselected pointer. No fitted parameters;
`r` and `delta` are free coupling labels, conserved/preserved but never computed or forced. The result
is a conservation/preservation theorem plus a scoped no-relaxation corollary for record-preserving
dynamics.

## Runner

```bash
python3 scripts/frontier_record_preservation_conserves_within_sector_measure_2026_06_15.py
```

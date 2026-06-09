# Occupancy Readout Exponent Berezin Subsumption Under the Existing Staggered Gate

**Date:** 2026-06-09
**Claim type:** bounded_theorem (conditional subsumption of the occupancy atom into the existing premise surface)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.py`](../scripts/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.py)
(SCORECARD: PASS=20, FAIL=0; cached:
[`logs/runner-cache/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.txt`](../logs/runner-cache/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.txt))

> **Boundary.** This note proposes a bounded conditional subsumption. It does
> not derive the staggered realization gate, the physical-species bridge, a
> readout context, a probability rule, or the charged-lepton value from the
> baseline axioms. It shows that, once the existing staggered Tier-A gate
> supplies the complex/Dirac polarization and the cited K/CPT registration
> surface is available, the occupancy factor is determinant bookkeeping rather
> than a separate MAXENT-R or readout-weight admission.

---

## The chain (every link runner-verified)

1. **The fork is an exponent (B1):** `det_R(β on R²) = |det_C(β)|²` exactly; K
   maps `det_C → conj(det_C)`, so `|det_C|` is the orbit-invariant determinant
   atom. The two fork cells differ *only* by the exponent (`|det_C|¹` vs
   `|det_C|²` — the doublet entering once vs squared).
2. **Hostile check (B2):** orbit-invariance alone permits every exponent
   `|det_C|^s` — granularity (D1) cannot decide the cell, exactly as the
   independence theorem requires. The free object is one exponent bit.
3. **Berezin uniqueness (B3):** translation invariance forces the Grassmann
   functional to be unique up to scale (computed) — **no measure freedom exists
   in the fermionic realization.** A from-scratch Grassmann engine then shows:
   one Dirac mode → `a` (= `det_C`, exponent 1); two Dirac modes with *generic*
   `A` → `det_C(A)` including the off-diagonal cross-term (sign calibrated
   once); a Majorana pair → `Pf(M)` with `Pf² = det_R` (exponent 2).
4. **The subsumption (B4):** which Berezin cell applies is conditional on the
   **polarization of the matter realization** supplied by the existing
   staggered Tier-A gate (mechanically verified present in
   `tier_a_admissions.json`). Complex/Dirac realization → `det_C` → `r = 1/2`
   (`Q = 2/3`); K-fixed/Majorana → `Pf/det_R` → `r = 1` (`Q = 1`). The cell map
   is cross-checked against the fork table, but that upstream source still has
   its own audit status.
5. **Kraus closure (B5):** D1's classical-only gap is closed — for *arbitrary*
   K-covariant quantum channels (random Kraus sets, rank 1–4, symmetrized,
   CPTP) and all K-invariant effects, the registrable statistics of `e₁` and
   `e₂` are identical (max difference `2×10⁻¹⁶`; algebraically zero).
6. **Adversarial multiplicity (B6):** in the complex-mode realization the
   exponent-2 atom (`a²`) is obtainable *only* by doubling the field content
   (computed: two independent modes → `a²`) — i.e. by changing the
   *realization*, never by a readout choice.
7. **Stiffness-independence (B7):** the exponent structure is scale-free; the
   re-panel's "common stiffness" smuggle objection to MAXENT-R does not apply
   to this route (the clause is nowhere used).
8. **Canonical name + a new falsifier (B8):** Frobenius–Schur. `FS(Z₃) =
   (+1, 0, 0)`; the inter-cell factor is `dim_R(End_G) = 2^{(1−FS)} ∈ {1, 2}`.
   The quaternionic case (`Q₈` control, `FS = −1` computed from `g²` classes)
   predicts **factor 4** — a registered kill condition nobody chose. Jones-index
   `√2` is a named negative (matches neither cell).

## Net

```text
before:  occupancy atom = proposed extra admission (bare binary, then MAXENT-R)
after:   occupancy exponent = CONDITIONAL THEOREM under
             {staggered gate (existing Tier-A) , CPT-covariant registration}
         MAXENT-R: not consumed by this route
         Jaynes-vs-Liouville: moot in the realization (no measure freedom exists)
         additional Tier-A nodes introduced here: none
```

With the campaign's prior results, the orbit **granularity** is conditionally
supported by durability plus retained CPT, while the **exponent** is routed to
the existing staggered gate rather than a new occupancy-weight premise. The
charged-lepton `Q = 2/3` reading remains bounded by that gate and by the
upstream fork/granularity surfaces; this note does not turn it into an
unbounded framework derivation.

## What this note does NOT claim

- **Not** an unconditional derivation: the independence theorem (PR #3400)
  stands — it governs the *unconditional* surface; this subsumption is
  conditional on the existing gate.
- **Not** a change to the staggered gate's own Tier-A status, nor any audit
  status.
- **Not** a claim that the re-panel's Tier-A verdict on MAXENT-R was wrong —
  it was right for MAXENT-R as a probability/weighting principle. This note
  makes that candidate non-load-bearing for this conditional route.
- **Not** an edit to the Tier-A registry, primitive registry, or axiom set.
- **Not** a use of Record to supply a readout context, weighting rule,
  normalization rule, probability rule, or realization selector.
- Falsifiers registered: a quaternionic readout context with factor ≠ 4;
  staggered-gate closure contradicting the complex-mode realization; and the
  earlier neutrino kill conditions where independently relevant.

## Negative-boundary discipline

This note contains local negative statements, so the boundary is explicit:

- **Alternative routes separated:** orbit invariance, Berezin functional
  uniqueness, K-covariant channel statistics, doubled field content,
  source-measure/MAXENT-R, and quaternionic control are distinct tests.
- **Wall independence:** the existing staggered Tier-A gate and K/CPT
  registration condition are independent inputs; closing either one does not
  close the other.
- **Hidden-wall scan:** "polarization" means only the content supplied by the
  cited staggered gate. No new source measure, readout context, probability
  rule, or realization selector is introduced here.
- **Residual matching:** the negative statement is narrow: the tested Berezin
  realization has no measure freedom that can select the occupancy exponent.
  It is not a proof that no future weighting or dynamics route can exist.
- **Rhetoric audit:** "not a readout choice" means within the stated
  determinant/Berezin realization; changing field content or closing the
  staggered gate is a different route.
- **Partial-closure path:** if the existing gate is later retained, this row may
  inherit that closure through the audit graph. That is not an axiom,
  primitive, or new Tier-A admission.
- **Steelman:** a future theorem might derive the complex/Dirac polarization
  or source-measure selection directly from the baseline. This note leaves
  those routes open.
- **Cross-cycle echo:** the result is consistent with the durability/granularity
  note and the fork-mechanism note, but does not promote either upstream row.

## Provenance

The re-panel and wall-breaking exercise motivated this route but are not
load-bearing authority. The load-bearing surface is the note, the runner, and
the explicit dependencies below. Prior MAXENT-R material remains non-load-bearing
for this route; the route uses determinant/Berezin structure plus the existing
staggered gate and K/CPT registration condition.

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the fork cells and the open route
  ("the readout functional factors through the doublet complex-slot quotient").
  This note uses that source as an upstream surface to be audited, not as a
  retained theorem.
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  — the existing Tier-A gate that supplies the polarization for this bounded
  route (consumed, not modified; still bounded).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  orbit wording and durability clause. Record supplies no weighting or
  realization selector here.
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — the exact lattice CPT input used for
  the K/CPT covariance condition.
- [RECORD_DURABILITY_DERIVES_GRANULARITY_NOT_WEIGHT_BOUNDED_THEOREM_NOTE_2026-06-09.md](RECORD_DURABILITY_DERIVES_GRANULARITY_NOT_WEIGHT_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the granularity theorem (D1) and the weight boundary (D2) this note
  routes around conditionally; its MAXENT-R relocation section is not consumed
  by this proof.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.

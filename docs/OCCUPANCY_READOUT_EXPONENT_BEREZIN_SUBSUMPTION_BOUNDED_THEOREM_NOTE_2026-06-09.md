# The Occupancy Subsumption: the Factor 2 Is a Determinant Exponent, Fixed by the Existing Gate — Zero New Admissions

**Date:** 2026-06-09
**Claim type:** bounded_theorem (conditional subsumption of the occupancy atom into the existing premise surface)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.py`](../scripts/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.py)
(SCORECARD: PASS=20, FAIL=0; cached:
[`logs/runner-cache/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.txt`](../logs/runner-cache/frontier_occupancy_readout_exponent_berezin_subsumption_2026_06_09.txt))

> **What this closes, and how much.** A six-lens re-panel unanimously ruled the
> MAXENT-R relocation still Tier-A-class (a probability/weighting rule cannot be
> a primitive under the registry's purity language). A five-slice wall-breaking
> exercise (per the repo exercise skill) then found the deeper move, with three
> slices converging independently: **the occupancy factor 2 was never a measure
> — it is the determinant-bookkeeping exponent of the additive readout, and in
> the fermionic (Berezin) realization there is no measure freedom to postulate
> over at all.** The cell is decided by the **polarization of the matter
> realization — the content of the already-registered staggered Tier-A gate.**
> Consequence: the occupancy admission has **no standalone existence**; MAXENT-R
> is deleted as unnecessary; the admission inventory stays at its existing two
> nodes. The Koide weight becomes a **conditional theorem** under the existing
> premise surface.

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
4. **The subsumption (B4):** which Berezin cell applies is decided by the
   **polarization of the matter realization** — supplied by the **existing**
   staggered Tier-A gate (mechanically verified present in
   `tier_a_admissions.json`). Complex/Dirac realization → `det_C` → `r = 1/2`
   (`Q = 2/3`); K-fixed/Majorana → `Pf/det_R` → `r = 1` (`Q = 1`). Cell map
   cross-checked verbatim against the landed fork table.
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
before:  occupancy atom = a proposed THIRD admission (bare binary, then MAXENT-R)
after:   occupancy weight = CONDITIONAL THEOREM under
             {staggered gate (existing Tier-A) , C1 CPT-covariant registration}
         MAXENT-R: deleted (unnecessary)
         Jaynes-vs-Liouville: moot in the realization (no measure freedom exists)
         new admission nodes: ZERO   (Tier-A inventory unchanged: AC_phi_lambda, theta)
```

With the campaign's prior results: the orbit **granularity** is a theorem
(durability + retained CPT); the **weight** is now a conditional theorem under
the existing gate; the charged-lepton `Q = 2/3` (empirical to `6×10⁻⁶`) follows
from the framework's Dirac realization with **nothing new admitted**; and the
Majorana/Dirac dichotomy plus the `Σm_ν` band and the quaternionic factor-4 are
standing falsifiers.

## What this note does NOT claim

- **Not** an unconditional derivation: the independence theorem (PR #3400)
  stands — it governs the *unconditional* surface; this subsumption is
  conditional on the existing gate ("the node is deleted, not the
  conditionality").
- **Not** a change to the staggered gate's own Tier-A status, nor any audit
  status.
- **Not** a claim that the re-panel's Tier-A verdict on MAXENT-R was wrong —
  it was right, and this note makes the question moot by removing the candidate.
- Falsifiers registered: a quaternionic readout context with factor ≠ 4;
  staggered-gate closure contradicting the complex-mode realization of charged
  leptons; the #3404 neutrino kill conditions (unchanged).

## Provenance

Re-panel (6 lenses, unanimous Tier-A on MAXENT-R) and wall-breaking exercise
(5 slices per `docs/ai_methodology/skills/exercise/SKILL.md`; three slices
converged on this route; canonical-measure sweep found every harmonic-analysis
measure selects the empirically-excluded sector cell, isolating
rank-over-commutant counting as the orbit cell's canonical home). Hygiene debts
flagged by the re-panel are paid in this commit: the M4 Majorana branch of the
MAXENT runner is now a computed landed-table lookup (no `check(True)` prose),
and D1's classical-only channel gap is closed by B5.

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells; this note supplies the note's named positive route
  ("the readout functional factors through the doublet complex-slot quotient")
  in its sharpest form: the readout's det atom *is* the complex-slot object.
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  — the existing Tier-A gate that supplies the polarization (consumed, not
  modified).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  orbit wording and durability clause.
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — the C1 covariance input.
- [RECORD_DURABILITY_DERIVES_GRANULARITY_NOT_WEIGHT_BOUNDED_THEOREM_NOTE_2026-06-09.md](RECORD_DURABILITY_DERIVES_GRANULARITY_NOT_WEIGHT_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the granularity theorem (D1) and the weight boundary (D2) this note
  completes; its MAXENT-R relocation section is superseded by this subsumption.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.

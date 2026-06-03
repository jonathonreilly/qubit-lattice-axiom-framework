# Flavor — the native action axis predicts Q=1: the heat-kernel/Casimir/spectral action interior extremum is at r=1, and the {Wilson,HK,Manton} action-form degeneracy is r-irrelevant

**Date:** 2026-06-02
**Claim type:** an action-axis result (no native action delivers r=1/2; the native prediction is the dimension default Q=1). Not closure.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade.
**Runner:** `scripts/flavor_native_action_predicts_q1_2026_06_02.py` (SCORECARD 5/5).

## Question
Does the framework's candidate **native** action (heat-kernel / Casimir / Connes spectral action,
where the Wilson term is only an admitted import) geometrically fix the charged-lepton mass:kinetic
weighting at `r=1/2` (`|b|/a = 1/√2`), or does it give the dimension default `r=1`, or leave it free?

## Result — every native action gives r=1 (Q=1); r=1/2 is not a stationary point
For `H = aI + b(C+C²)` (δ=0; Q is δ-independent), eigenvalues `{a+2b, a−b, a−b}`:

- The Connes spectral action `S(b) = Σ f(λᵢ²/Λ²)` has its interior extremum at **|b|/a ≈ 1 (r=1)** for
  every monotone-decreasing cutoff — verified `exp(−x):1.00, exp(−x²):1.00, (1+x)⁻²:1.00, (1+x)⁻⁴:1.00,
  (1+x)⁻⁸:1.00` — **never near the target 1/√2 = 0.707**. At `b/a=1` the spectrum is `[0,0,3a]` (the
  doublet eigenvalue collapses to zero, where any decaying `f` peaks); this is the `r=1`,
  dimension/Plancherel point, `Q=1`. (This interior point is a *maximum* of `Tr f`, so under the
  Connes minimization principle it is degenerate/boundary-seeking — but either way `r=1/2` is provably
  not a stationary point of any native action.)
- The Casimir / heat-kernel variant (Z₃ cycle-graph Laplacian, Casimir-weighted `Tr(H²)`) slides
  `r ∈ [0, 1/4]` with the free Brownian time `t` — crossing neither `1/2` nor the target.

## The action-form degeneracy is r-irrelevant
The `{Wilson, HK, Manton}` forms are continuum-degenerate (the repo's
`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO` note): all three collapse to the **same bi-invariant `|X|²`
metric at quadratic order** and differ only at `O(X⁴)`. The on-site (`k=0` character mode) and hopping
(`k=1,2` modes) are **Hilbert–Schmidt orthogonal** (verified `⟨mass,hop⟩_HS = 0`), so the single
bi-invariant quadratic norm only rescales the overall kinetic weight — it **never relates the two
amplitudes**. Therefore breaking the action-form degeneracy at `O(X⁴)` provably **cannot move r**. No
native uniqueness/naturalness condition selects a form delivering `r=1/2`.

## Consequence
**The framework's native action-sector prediction is Q=1.** `r=1/2` is reached only by the equal-block
Hilbert–Schmidt partition `3a² = 6b²` of the single invariant `Tr(H²)` — a measure/reading
prescription (equal-power-per-block), i.e. the Tier-A admitted input `AC_φλ`, not a stationarity
condition any native action produces. This is the action axis joining the measure and structure axes:
all three give `r=1`, and `r=1/2` is the one unforced block-count import (which is **native**, i.e. it
does not depend on the Wilson import).

## The next paths this opens (not closing)
- The residual is one object — the trace/dimension (→ Q=1) vs sector/block-count (→ Q=2/3) weighting
  of the two C₃ isotypes. Whether any native principle (positivity, entropy, modular/KMS, records)
  selects block-count over dimension is the live question.
- The readout-class axis (signed Brannen vs singular-value Yukawa) is independent of the action axis
  and remains open.

## Provenance (verified 2026-06-02)
- HS block norms; equal-block ⇔ r=1/2; spectral-action critical |b|/a ≈ 1 across five cutoffs;
  spectrum `[0,0,3a]` at b/a=1 ⇒ Q=1; mass/hop HS-orthogonality: verified directly (runner 5/5). From
  the heat-kernel action-axis workflow (`wf_ccbf7f51`). Action-form degeneracy cross-checked against
  `origin/main:docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`.
- This note sets no audit status; it records the native action's r=1 prediction and the
  r-irrelevance of the action-form degeneracy.

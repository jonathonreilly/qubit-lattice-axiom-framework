# Flavor — value and chirality are genuinely SEPARATE on the lift, but share one common ROOT import (the order-3 complex / det_C structure)

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded result (confirms Correction 1; identifies a shared root) + flagged caveat.
**Runner:** `scripts/flavor_substrate_parent_separate_2026_05_30.py` (SCORECARD PASS=3).
**Source:** 4-agent build `wf_fa432c9c` (corner-lift, qubit-tensor, orbit-split-source + adjudication).

## Question
On R³ the value import `G_U1` (on-block, commutes `Γ_χ`) and the chirality gate (off-block, anticommutes)
are algebraically orthogonal — the prior "single shared gate" was retracted. Does a lifted
`M₂(ℂ)⊗(Z₂)³` substrate-parent project onto **both**, rehabilitating the unification?

## Result — genuinely separate (Correction 1 holds), with one common root
- **Tensor-factorization kills the naive lift.** Under the coin-blind grading `I₂⊗Γ_χ`, even/odd is fixed
  *entirely* by the generation factor's relation to `Γ_χ`, independent of the coin. So the assembled
  `K = I₂⊗G_U1 + sx⊗H_chi` is a **forced super-direct-sum** (G_U1 in the even slot, the chiral op in the
  odd slot, non-interchangeable) — a decomposable `G_U1 ⊕ H_chi`, **not** an indecomposable parent. The
  R³ orthogonality `comm(C) ∩ anticomm(Γ_χ) = {0}` is inherited verbatim.
- **A C₃-equivariant *native* parent reaches only the value.** With the qubit a C₃-singlet, the on-hw=1
  image is exactly the 3-dim circulant algebra: `G_U1` reachable, the Γ_χ-anticommuting (chiral) operator
  **not** reachable.
- **The one rehab channel is the value import itself.** The *only* way a C₃-equivariant parent folds to a
  chiral on-block operator is if the qubit carries an **order-3 charge `diag(1,ω)`** — order 3, `det=ω`
  (not in SU(2)), complex `I/Z` coefficients. That is **not native** to `M₂(ℂ)` as a `Z₂` spin factor —
  and it is the **same complex/order-3 structure as the det_C value import**.

## Interpretation
Value and chirality are **not the same gate** (orthogonal on R³, not unified by any native lift), so the
campaign has **two distinct pins on R³**. But they are **not independent either**: the single object that
would unify them — the order-3 complex phase `diag(1,ω)` — is the *same* `det_C`/complex-counting structure
that the value import requires. So the honest picture is:

> **One common ROOT import — a complex / order-3 (`det_C`) structure on the discrete `Z₂`-spin substrate —
> casts two orthogonal shadows on R³: the value generator `G_U1` (C₃-equivariant) and the chiral grading
> (orbit-splitting). The substrate (real, `C³=I`, `Z₂` spin) supplies neither; importing the one complex
> structure supplies both.**

Not "one gate," but "one root." This is the precise, corrected sense in which the value and chirality
questions are connected.

## Caveat (flagged for audit)
The "genuinely separate / not native" verdict hinges on reading `M₂(ℂ)` as the `Z₂` spin factor with **no
native order-3 charge**. Whether the complex `M₂(ℂ)` admits `diag(1,ω)` as native is the *same* question as
whether `det_C` is native (the full-exercise crux, answered "no" via the `(Z₂)³` real momenta + CPT). The
two are the same crux; recommend an independent audit row before treating settled.

## Stale-citation flags
- Anchors: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded, reinforced),
  `koide_c3_generator_rephasing_obstruction` (retained).

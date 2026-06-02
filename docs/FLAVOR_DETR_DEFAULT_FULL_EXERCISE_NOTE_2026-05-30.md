# Flavor — full exercise on "Q=1 default / r=1/2 import": CONFIRMED in its load-bearing half, with two corrections and one open gap

**Date:** 2026-05-30
**Claim type:** bounded confirmation + two corrections of prior overstatements + one named open gap.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_detR_default_full_exercise_2026_05_30.py` (SCORECARD PASS=5).
**Source:** 9-agent adversarial exercise `wf_b1f506df` (establish 5 links → 4 flip-attacks → adjudication), all numerics re-verified.

## The crux verdict — the conclusion does NOT flip
Tested whether the complex `M₂(ℂ)` qubit makes `det_C` native (which would make Q=2/3 the default,
r=1/2 *derived*). **All four flip-attacks confirm `det_R`/Q=1 default, high confidence.** The complex
structure does **not** descend as a doublet U(1):
- **Substrate `i` is generation-blind:** multiplication-by-`i` restricts to the scalar `i·I₃` on the
  hw=1 triplet (`[i·I₃, C]=0`); the doublet generator `G_U1=(C−C²)/√3` has **zero** HS-overlap with it.
- **`C³=I` quantizes** the doublet rephasing `C→e^{iα}C` to `α∈{0, 2π/3, 4π/3}` — the continuous `U(1)_b`
  is forbidden (retained `koide_c3_generator_rephasing_obstruction`).
- **The `(Z₂)³` momentum corners are `±1` (real)** + a CPT corner-reflection sends `J_b → −J_b`, so there
  is no holomorphic complex-line carrier either. The generation algebra is honestly real `ℝ[Z₃]`.

So `det_C` is not inherited; **`r=1/2` (Q=2/3) is a genuine, precisely-localized import.**

## What the import IS (correcting two prior overstatements)
**Correction #1 — it is NOT the chirality gate.** The `det_C`/U(1) generator `G_U1` **commutes** with
`Γ_χ=(2/3)J−I` and with `C` (it is on-block, C₃-equivariant); the chiral orbit-splitting grading is
**off-block and anticommutes** (`‖{G_U1,Γ_χ}‖=2.83≠0`). They are algebraically **orthogonal** — the
campaign's earlier "single shared gate" claim is **unsupported on R³**. (Whether a lifted
`M₂(ℂ)⊗(Z₂)³` substrate-parent projects onto *both* is untested — the genuine open frontier for unification.)

**Correction #2 — it is NOT a continuous symmetry or a holomorphic measure.** Once `U(1)_b`-as-symmetry
(forbidden by `C³=I`) and the holomorphic-measure route (forbidden by the real `(Z₂)³` characters + CPT)
are both excluded, the residual import is solely the **block-vs-dimension counting-measure choice** on
`ℝ[Z₃]=ℝ⊕ℂ`:
- `(1,1)` idempotent / **center-count** (doublet = 1 complex slot) → `r=1/2` → **Q=2/3**;
- `(1,2)` **Plancherel / dimension-count** (doublet = 2 real modes) → `r=1` → **Q=1**.

The retained trace τ **permits both and ranks neither** (Schur: the two real doublet modes cannot be
merged into one complex mode by any native operator). The substrate-forced *default* is the dimension
count (`Q=1`); the observed `Q=2/3` is the center-count, which the substrate does not supply.

## Precise one-sentence characterization
> Charged-lepton Koide `Q=2/3` (`r=1/2`) requires choosing the `(1,1)` block/idempotent-count measure on
> `ℝ[Z₃]=ℝ⊕ℂ` over the `(1,2)` dimension/Plancherel count — a measure choice the retained trace permits
> but does not rank, which is **neither** a continuous `U(1)_b` symmetry (forbidden by `C³=I`) **nor** a
> holomorphic complex-line carrier (forbidden by the `(Z₂)³` real characters and the CPT reflection
> `J_b→−J_b`), and which is **not** the chiral orbit-splitting grading (`G_U1` commutes with `Γ_χ`).

## The one open gap (Link 1, Half B)
The exercise found one genuine, un-closed assumption. Splitting Link 1:
- **Half A (which state is tracial):** airtight/retained — the UHF II_∞ trace is unique (`τ=Tr/3`,
  three equal real modes).
- **Half B (that the *physical generation vacuum* IS that tracial β=0 state):** **unaudited,
  user-approval-required** (the PRR no-extra-structure premise, `inner_automorphism_invariance_...`).
  The framework's own `axiom_first_kms_condition` note has physical equilibria as β>0 Gibbs states
  (non-tracial). A finite-β route cannot make `det_C` native (Schur again), so it does not flip the
  import — but A1+A2 do **not** force β=0, so "**Q=1 is THE default**" is conditional on the
  tracial-vacuum premise. Closing or refuting Half B (β=0 trace vs β>0 Gibbs for the generation
  reference, without the PRR premise) is the sharpest next computation; the second is building the
  `M₂(ℂ)⊗(Z₂)³` substrate-parent to test the Correction-#1 unification.

## Stale-citation flags (verified vs origin/main ledger)
- Retained: `koide_c3_generator_rephasing_obstruction` (retained), `koide_z3_equivariant_anticommuting_no_go`
  (retained_bounded), `powers_uhf_tracial_uniqueness` + `pre_record_reference_state` (retained, Half-A scope).
- Unaudited (load-bearing for Half B): `inner_automorphism_invariance_tracial_identification`,
  `axiom_first_kms_condition`, `koide_real_rep_block_count_permitted_not_forced` (no_go/unaudited).

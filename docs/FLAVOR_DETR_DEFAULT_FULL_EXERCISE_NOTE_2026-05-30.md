# Flavor — det_R/det_C counting fork bounded locator: finite algebra confirmed, default status conditional

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded finite-algebra locator + conditional default statement.
The trace/dimension read gives `r=1` and `Q=1` only after a beta=0 tracial
generation reference is supplied. This note does not derive that reference
state from the current framework.
**Runner:** `scripts/flavor_detR_default_full_exercise_2026_05_30.py` (SCORECARD PASS=6).
**Source:** 9-agent adversarial exercise `wf_b1f506df` (establish 5 links → 4 flip-attacks → adjudication), all numerics re-verified.

## 2026-06-07 boundary repair

The finite algebra in this packet is worth preserving, but the older wording
over-read it as a framework-native "Q=1 default" theorem. The current bounded
claim is sharper:

- the substrate `i`, `C^3=I` rephasing quantization, `(Z_2)^3` real-corner
  check, and `G_U1`/`Gamma_chi` distinction are finite carrier algebra;
- the `r`/`Q` endpoint dictionary is sourced to retained
  [`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md);
- the equal-block versus dimension/Plancherel split is sourced to audited
  bounded
  [`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md);
- the beta=0 tracial-vacuum premise is **not** derived here and is not promoted.

Thus the honest result is a bounded route-pruning statement: the tested native
structures do not make `det_C`/equal-block counting automatic, and the trace
read is the dimension/Plancherel read if the tracial generation reference is
supplied. The packet does not choose the physical generation reference state.

## The crux verdict — the finite counting fork does NOT flip
Tested whether the complex `M₂(ℂ)` qubit makes `det_C` native (which would make Q=2/3 the default,
r=1/2 *derived*). **All four flip-attacks confirm that the tested structures
do not supply `det_C`; under a supplied tracial reference they leave the
dimension/Plancherel `det_R` read.** The complex structure does **not** descend
as a doublet U(1):
- **Substrate `i` is generation-blind:** multiplication-by-`i` restricts to the scalar `i·I₃` on the
  hw=1 triplet (`[i·I₃, C]=0`); the doublet generator `G_U1=(C−C²)/√3` has **zero** HS-overlap with it.
- **`C³=I` quantizes** the doublet rephasing `C→e^{iα}C` to `α∈{0, 2π/3, 4π/3}` — the continuous `U(1)_b`
  is forbidden (retained `koide_c3_generator_rephasing_obstruction`).
- **The `(Z₂)³` momentum corners are `±1` (real)** + a CPT corner-reflection sends `J_b → −J_b`, so there
  is no holomorphic complex-line carrier either. The generation algebra is honestly real `ℝ[Z₃]`.

So `det_C` is not inherited by these tested structures; **`r=1/2` (Q=2/3)
remains a precisely localized counting/measure input unless another retained
selector supplies it.**

## What the import IS (correcting two prior overstatements)
**Correction #1 — it is NOT the chirality gate.** The `det_C`/U(1) generator `G_U1` **commutes** with
`Γ_χ=(2/3)J−I` and with `C` (it is on-block, C₃-equivariant); the chiral orbit-splitting grading is
the separate kind of object that would have to be **off-block and anticommuting**. The displayed
nonzero anticommutator (`‖{G_U1,Γ_χ}‖=2.83≠0`) confirms that `G_U1` is not that chiral splitter. They
are algebraically **orthogonal** — the
campaign's earlier "single shared gate" claim is **unsupported on R³**. (Whether a lifted
`M₂(ℂ)⊗(Z₂)³` substrate-parent projects onto *both* is untested — the genuine open frontier for unification.)

**Correction #2 — it is NOT a continuous symmetry or a holomorphic measure.** Once `U(1)_b`-as-symmetry
(forbidden by `C³=I`) and the holomorphic-measure route (forbidden by the real `(Z₂)³` characters + CPT)
are both excluded, the residual import is solely the **block-vs-dimension counting-measure choice** on
`ℝ[Z₃]=ℝ⊕ℂ`:
- `(1,1)` idempotent / **center-count** (doublet = 1 complex slot) → `r=1/2` → **Q=2/3**;
- `(1,2)` **Plancherel / dimension-count** (doublet = 2 real modes) → `r=1` → **Q=1**.

The retained trace τ **permits both and ranks neither** (Schur: the two real
doublet modes cannot be merged into one complex mode by any native operator).
If the beta=0 tracial generation reference is supplied, its dimension count is
`Q=1`; the observed `Q=2/3` is the center-count/equal-block read, which this
packet does not derive.

## Precise one-sentence characterization
> Charged-lepton Koide `Q=2/3` (`r=1/2`) requires choosing the `(1,1)`
> block/idempotent-count measure on `ℝ[Z₃]=ℝ⊕ℂ` over the `(1,2)`
> dimension/Plancherel count — a measure choice the trace permits but does not
> rank, which is **neither** a continuous `U(1)_b` symmetry (forbidden by
> `C³=I`) **nor** a holomorphic complex-line carrier (forbidden by the
> `(Z₂)³` real characters and the CPT reflection `J_b→−J_b`), and which is
> **not** the chiral orbit-splitting grading (`G_U1` commutes with `Γ_χ`).

## The one open gap (Link 1, Half B)
The exercise found one genuine, un-closed assumption. Splitting Link 1:
- **Half A (which state is tracial):** airtight/retained — the UHF II_∞ trace is unique (`τ=Tr/3`,
  three equal real modes).
- **Half B (that the *physical generation vacuum* IS that tracial β=0 state):** **open,
  not derived here** (the PRR/no-extra-structure premise, `inner_automorphism_invariance_...`).
  The framework's own `axiom_first_kms_condition` note has physical equilibria as β>0 Gibbs states
  (non-tracial). A finite-β route cannot make `det_C` native (Schur again), so it does not flip the
  import — but framework baseline do **not** force β=0, so "`Q=1` is the trace/det_R read" is conditional on the
  tracial-vacuum premise. Closing or refuting Half B (β=0 trace vs β>0 Gibbs for the generation
  reference, without the PRR premise) is the sharpest next computation; the second is building the
  `M₂(ℂ)⊗(Z₂)³` substrate-parent to test the Correction-#1 unification.

## Stale-citation flags (verified vs origin/main ledger)
- Retained: `koide_c3_generator_rephasing_obstruction` (retained), `koide_z3_equivariant_anticommuting_no_go`
  (retained_bounded), `powers_uhf_tracial_uniqueness` + `pre_record_reference_state` (retained, Half-A scope),
  `RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05` (retained), and
  `KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29` (retained_bounded).
- Open / not promoted (load-bearing only for a physical default claim, which this bounded packet does not make):
  `inner_automorphism_invariance_tracial_identification`, `axiom_first_kms_condition`, and
  `koide_real_rep_block_count_permitted_not_forced`.

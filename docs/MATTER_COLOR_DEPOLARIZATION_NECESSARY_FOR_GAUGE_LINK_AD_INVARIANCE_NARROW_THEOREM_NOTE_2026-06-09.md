# Matter Color Depolarization Is Necessary for Gauge-Link Step-Measure Ad-Invariance (ADM-2)

**Date:** 2026-06-09
**Type:** narrow theorem (a necessary-condition sharpening) — relocates ST2's ADM-2 onto a matter order parameter
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.txt`
**Status:** source proposal. The statements are exact finite-dimensional `su(3)`
representation-theory facts plus an exact Wick second-moment computation. Authority
role: source proposal; the independent audit lane sets any retained status.

## Context

The gauge-link / color-einselection dynamics frontier has four undelivered inputs
(the "four hats"): the static local-frame redundancy **ADM-1**, a continuous-time
gauge-link **generator R1** (arrow + rate), the mixing regime **R2** that delivers
the heat-kernel convolution attractor, and the **blocking-isometry** selection.

R2's premise was reduced (source proposals, both `unaudited` on the live ledger at
drafting — cited as proposals, not as retained) to **ADM-2**: *the emergent-time
gauge-link step measure is Ad-invariant (bi-invariant)*, whence any bi-invariant
per-step kernel flows under convolution to the heat kernel `exp(t Δ / 2)`
(`adm2_global_su3_symmetry_reduces_action_form_bi_invariance_narrow_theorem_note_2026-06-08`;
the `st1_st2_same_wall_gauge_dynamics_residual_convergence_narrow_theorem_note_2026-06-08`
capstone). The ADM-2 reduction note already records that an *equivariant drift with
isotropic noise* has a central increment, while a *quenched* background "picks a color
direction" and the single-link step is then **not** central. What that note leaves open
is the **physical order parameter**: which concrete matter datum controls whether the
step is central.

This note supplies it, for the necessary direction, with an exact and
model-independent argument.

## Retained grounds used (verified on the live ledger at drafting)

- `graph_first_su3_integration_note` — **retained**: global `SU(3)` is the commutant of
  the observables; color is the irreducible fundamental triplet. (Used: the increment
  generator lives in `su(3)`, the adjoint; conjugation `X -> g X g†` is the color action.)
- `record_classical_semigroup_boundary_2026-06-06` — **retained**, and
  `record_markov_generator_embeddability_boundary_2026-06-06` — **retained_no_go**: the
  Record axiom supplies no continuous Markov generator or rate. (Used: the relocation
  target — color depolarization — is not derivable from Record alone; it stays open.)

The `su(3)` representation facts (`3 ⊗ 3̄ = 1 ⊕ 8`; `su(3)` simple, trivial center) are
standard mathematics, cited as method and reproduced exactly by the runner.

## Setup

The matter sector couples to the color link through a gauge-covariant **drift**: a
linear map from the matter color density `ρ_color` (a `3×3` Hermitian one-body color
reduced density at the link, `tr ρ = 1`) into the `su(3)` increment generator `H` that
rotates the link one step, `U -> exp(i ε H) U`. Ad-invariance (centrality) of the
resulting step measure is ADM-2.

The canonical instance is the matter color charge, `H = traceless(φ φ†)` for a color
amplitude `φ` with `E[φ φ†] = ρ_color` — the minimal-coupling matter color current
sourcing the link.

## Theorem (necessary condition; exact, model-independent)

> **The emergent-time gauge-link step measure is Ad-invariant (ADM-2) only if the
> coupled matter color density is unpolarized, `ρ_color = I₃ / 3`.**

Proof, in three exact steps (runner checks in brackets):

1. **The gauge-covariant linear drift is unique up to scale.** The equivariant linear
   maps `Herm(3) -> su(3)` form a one-dimensional space: `Herm(3) = 1 ⊕ 8` and the
   target is the adjoint `8`, so by Schur `Hom_{SU(3)}(Herm(3), su(3))` is one
   dimensional — the traceless projection `X -> X - (tr X / 3) I`. Hence **every**
   nonzero gauge-covariant linear drift has mean a nonzero multiple of
   `traceless(ρ_color)`. [E0]

2. **`su(3)` has no nonzero Ad-invariant element.** The commutant of the eight
   Gell-Mann generators inside `3×3` is the scalars (the fundamental is irreducible,
   Schur); a traceless scalar is `0`. Equivalently, the adjoint `8` carries no invariant
   vector. [E1]

3. **Assemble.** For the canonical drift, the exact (Wick) mean increment generator is
   `E[H] = traceless(ρ_color)` [E2]. An Ad-invariant increment distribution has an
   Ad-invariant mean; by step 2 that mean is `0`; by step 1 (or directly) this forces
   `traceless(ρ_color) = 0`, i.e. `ρ_color = I₃ / 3`. A polarized `ρ_color` gives a
   nonzero `su(3)` mean force and hence a non-central increment. [E3]

The argument uses only the **first moment** of the increment and **no noise model**, so
it holds for every gauge-covariant drift in the minimal-coupling class.

## The order parameter

The color polarization is exactly the deviation that obstructs centrality:

```
|| traceless(ρ_color) ||_F^2  =  Tr(ρ_color^2) − 1/3
```

— the color purity above its floor — strictly monotone in purity, vanishing iff
`ρ_color = I₃ / 3`. [E4] So ADM-2's open dynamical premise is **equivalent, on the
first-moment obstruction, to a concrete matter observable: color depolarization to the
maximally-mixed (color-blind) density.**

## Converse (conditional; second moment)

Under a **named** isotropic-Gaussian fluctuation model for the matter source
(`φ = √ρ ξ`, `ξ ~ CN(0, I)`), the exact Wick covariance of `H = traceless(φ φ†)` is
isotropic (`∝ I₈`, the unique Ad-invariant quadratic form on `su(3)`) at
`ρ_color = I₃ / 3`, and anisotropic for polarized `ρ_color`, with anisotropy monotone
in purity (`0.000, 0.579, 0.842, 0.951, 0.991, 1.000` across the polarization sweep).
[E5] This is the second-moment refinement and is **conditional on the fluctuation model**
(a named admission); it is not part of the model-independent necessary direction.

## What this is not (boundaries and guards)

- **Does not deliver R1.** No gauge-link generator is constructed; the link increment's
  arrow and rate remain undelivered. This is a necessary condition on ADM-2's measure,
  not a dynamics.
- **Does not derive the depolarization.** That the framework's dynamics drives
  `ρ_color -> I₃ / 3` is **not** shown; the retained Record boundaries supply no such
  continuous generator. The open input is relocated, not closed: ADM-2 now reads
  "show the dynamics depolarizes the matter color density to the color-blind ensemble."
- **Discharges no other hat.** It does not touch ADM-1 (static local-frame redundancy)
  or the blocking-isometry selection, and it states no ranking between ST1 and ST2.
- **Not the refuted sufficiency claim.** The earlier "annealed-twirl = i.i.d.-central
  CLT" reading was a first-moment *sufficiency* over-claim and was refuted. The present
  statement is the opposite logical direction — a *necessary* first-moment obstruction
  (the mean su(3) force must vanish) — and the guard [E6] confirms the mean force is a
  genuine content condition (a polarized, fully equivariant source has a nonzero mean
  force), not a symmetry artifact.
- **Carrier conditionality.** `ρ_color` lives on the supplied `C³` color carrier
  (`MR_color` residual); the drift is the minimal-coupling matter color current. The
  statement is conditional on that carrier, as the rest of the program is.

## Relation to the campaign's other findings

The single-edge composite-link blocks established that the induced link `U_eff` is a
lossy coordinate (the genuine autonomous generator lives in the local color densities,
not the link). The present note works one level up, on the **step measure's** centrality
rather than the link trajectory, and identifies the matter datum (`ρ_color` polarization)
that the quenched non-centrality of the ADM-2 reduction note depends on. A literature
bridge (stochastic quantization, heat-bath, GKSL, gradient flow) independently names the
undelivered R1 input as a stationary action gradient plus a noise/bath rate datum —
consistent with ADM-2's centrality being a property of the supplied step measure, here
pinned to color depolarization.

## Reproduction

`python3 scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py`
→ `TOTAL: PASS=18 FAIL=0` (exact `su(3)` algebra; the only randomness samples linear
constraints for the representation-dimension counts, whose results are exact integers).

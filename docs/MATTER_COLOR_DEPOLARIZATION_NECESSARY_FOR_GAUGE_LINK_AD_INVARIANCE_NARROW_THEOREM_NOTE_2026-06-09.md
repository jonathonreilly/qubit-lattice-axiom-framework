# Matter Color Depolarization Is Necessary for Nonzero Matter-Current First-Moment Centrality

**Date:** 2026-06-09
**Type:** bounded_theorem (necessary-condition sharpening for the gauge-link
bi-invariant step-measure premise)
**Claim type:** bounded_theorem
**Primary runner:**
[`scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py`](../scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.txt`](../logs/runner-cache/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.txt)
**Status:** source proposal. The statements are exact finite-dimensional `su(3)`
representation-theory facts plus an exact Wick second-moment computation.
Authority role: source proposal; the independent audit lane sets any retained
status.

## Context

The gauge-link dynamics program has an undelivered step-measure premise: the
emergent-time gauge-link increment should be Ad-invariant/bi-invariant before
the heat-kernel convolution argument can apply. Earlier source proposals reduced
parts of that premise to global `SU(3)` equivariance plus an annealed/mixing
regime, but they did not derive the dynamics, the rate, or the central
per-step measure.

This note identifies a necessary first-moment obstruction for the
minimal-coupling matter-current channel. If the matter color density contributes
a nonzero gauge-covariant linear drift to the link increment, then centrality of
the step measure forces the matter color density to be unpolarized.

## Dependency And Status Boundary

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  is the retained-grade color-carrier source: global `SU(3)` is the commutant
  of the observables and color is the fundamental triplet. Used here only to
  place the increment generator in `su(3)` with conjugation
  `X -> g X g†` as the color action.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  and
  [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
  record that Record supplies no continuous Markov generator, rate, or
  relaxation law. Used here only as a boundary: this note does not derive the
  depolarizing dynamics.

The `su(3)` representation facts (`3 ⊗ 3̄ = 1 ⊕ 8`; `su(3)` simple, trivial center) are
standard mathematics, cited as method and reproduced exactly by the runner.

## Setup

Assume the matter sector contributes a **nonzero gauge-covariant linear drift**
to the color link: a linear map from the matter color density `ρ_color` (a
`3×3` Hermitian one-body color reduced density at the link, `tr ρ = 1`) into
the `su(3)` increment generator `H` that rotates the link one step,
`U -> exp(i ε H) U`. Ad-invariance/centrality of the resulting step measure is
the target premise.

The canonical instance is the matter color charge, `H = traceless(φ φ†)` for a color
amplitude `φ` with `E[φ φ†] = ρ_color` — the minimal-coupling matter color current
sourcing the link.

## Theorem

> **For any nonzero gauge-covariant linear minimal-coupling drift
> `Herm(3) -> su(3)`, Ad-invariance of the link-increment step measure forces
> the coupled matter color density to be unpolarized,
> `ρ_color = I₃ / 3`.**

Proof, in three exact steps (runner checks in brackets):

1. **The gauge-covariant linear drift is unique up to scale.** The equivariant linear
   maps `Herm(3) -> su(3)` form a one-dimensional space: `Herm(3) = 1 ⊕ 8` and the
   target is the adjoint `8`, so by Schur `Hom_{SU(3)}(Herm(3), su(3))` is one
   dimensional — the traceless projection `X -> X - (tr X / 3) I`. Hence every
   **nonzero** gauge-covariant linear drift in this class has mean a nonzero
   multiple of `traceless(ρ_color)`. [E0]

2. **`su(3)` has no nonzero Ad-invariant element.** The commutant of the eight
   Gell-Mann generators inside `3×3` is the scalars (the fundamental is irreducible,
   Schur); a traceless scalar is `0`. Equivalently, the adjoint `8` carries no invariant
   vector. [E1]

3. **Assemble.** For the canonical drift, the exact (Wick) mean increment generator is
   `E[H] = traceless(ρ_color)` [E2]. An Ad-invariant increment distribution has an
   Ad-invariant mean; by step 2 that mean is `0`; by step 1 (or directly) this forces
   `traceless(ρ_color) = 0`, i.e. `ρ_color = I₃ / 3`. A polarized `ρ_color` gives a
   nonzero `su(3)` mean force and hence a non-central increment. [E3]

The argument uses only the **first moment** of the increment and **no noise
model**, so it is independent of the fluctuation model once the nonzero
minimal-coupling drift channel is supplied.

## The order parameter

The color polarization is exactly the deviation that obstructs centrality:

```
|| traceless(ρ_color) ||_F^2  =  Tr(ρ_color^2) − 1/3
```

— the color purity above its floor — strictly monotone in purity, vanishing iff
`ρ_color = I₃ / 3`. [E4] On this first-moment obstruction, the open centrality
premise reduces to a concrete matter observable: color depolarization to the
maximally mixed color density.

## Converse (conditional; second moment)

Under a **named** isotropic-Gaussian fluctuation model for the matter source
(`φ = √ρ ξ`, `ξ ~ CN(0, I)`), the exact Wick covariance of `H = traceless(φ φ†)` is
isotropic (`∝ I₈`, the unique Ad-invariant quadratic form on `su(3)`) at
`ρ_color = I₃ / 3`, and anisotropic for polarized `ρ_color`, with anisotropy monotone
in purity (`0.000, 0.579, 0.842, 0.951, 0.991, 1.000` across the polarization sweep).
[E5] This is the second-moment refinement and is **conditional on the fluctuation model**
(a named admission); it is not part of the noise-model-independent
first-moment direction.

## What this is not (boundaries and guards)

- **Does not deliver a gauge-link generator.** No link generator, arrow, or rate
  is constructed. This is a necessary first-moment condition on a supplied
  step-measure channel, not a dynamics.
- **Does not derive the depolarization.** That the framework's dynamics drives
  `ρ_color -> I₃ / 3` is **not** shown; the retained Record boundaries supply no such
  continuous generator. The open input is relocated, not closed: the dynamics
  program still has to show depolarization of the matter color density.
- **Does not cover zero drift or unrelated central noise.** A zero
  matter-current drift, or a step measure whose centrality is supplied by an
  unrelated channel, is outside this theorem and would not force
  `ρ_color = I₃ / 3`.
- **Discharges no other dynamics premise.** It does not touch static local-frame
  redundancy, blocking-isometry selection, mixing, or any ranking between
  action-form routes.
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

The single-edge composite-link blocks established that the induced link `U_eff`
is a lossy coordinate: the autonomous generator belongs in the local color
densities, not only in the link trajectory. The present note works one level up,
on the **step measure's** centrality rather than the link trajectory, and
identifies the matter datum (`ρ_color` polarization) that obstructs first-moment
centrality in the minimal-coupling channel.

## Reproduction

`python3 scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py`
→ `TOTAL: PASS=18 FAIL=0` (exact `su(3)` algebra; the only randomness samples linear
constraints for the representation-dimension counts, whose results are exact integers).

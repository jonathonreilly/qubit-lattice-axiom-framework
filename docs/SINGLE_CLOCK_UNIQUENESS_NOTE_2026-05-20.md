# Single-Clock Uniqueness: No Spatial-RP, No Second Clock

**Date:** 2026-05-20
**Claim type:** positive_theorem (uniqueness closure on the
single-clock codimension-1 evolution theorem)
**Status:** proposal — pre-audit
**Closes (proposed):** the conditional gap on
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
identified by the 2026-05-20 first-pass audit: *"fixed-temporal-RP
core is plausible, but no-spatial-RP/no-second-clock uniqueness is
not closed."*

## Claim

On the qubit-`Z^3` lattice framework (A1+A2 per
`MINIMAL_AXIOMS_2026-05-20.md`), with retained primitives
microcausality, Lieb-Robinson finite propagation, cluster
decomposition, and reflection positivity, the single-clock
codimension-1 evolution structure is **unique** in the following
sense:

1. **No spatial reflection positivity:** RP cannot be promoted to
   any of the three spatial directions of `Z^3` while preserving
   the retained microcausality and Lieb-Robinson bounds.

2. **No second clock:** the foliation by codimension-1 leaves
   admitting reflection positivity is unique up to the time-
   reversal `t → −t` symmetry. In particular, no second independent
   time direction can be introduced.

Together, (1) and (2) close the uniqueness side of
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`,
which derives the existence of single-clock codimension-1 evolution.

## Setup

Per the retained
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29`, the
framework admits reflection positivity (RP) on the staggered-only
and symmetric-canonical-Wilson surfaces, with the RP reflection
acting on a chosen codimension-1 hyperplane. The standard
Osterwalder-Schrader reconstruction interprets the RP-distinguished
direction as Euclidean time, and the codimension-1 hyperplanes
foliate the substrate into equal-time slices.

Per
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`,
this RP-distinguished direction *exists*. The conditional gap is
whether it is *unique* — could a separate RP-distinguished spatial
direction or a second time direction be consistently introduced?

## Step 1 — Spatial RP would break microcausality

Suppose, for contradiction, that the framework admits a reflection
positivity not only across a (Euclidean-time) hyperplane but also
across a spatial hyperplane perpendicular to some direction `ê_i`
(`i ∈ {1, 2, 3}`).

The RP condition for a hyperplane normal to `ê_i` would require, for
all observables `A` supported on `{x : x · ê_i ≥ 0}`,

```text
⟨A(θ_i A^†)⟩ ≥ 0                                                        (1)
```

where `θ_i` is the reflection `x · ê_i → −x · ê_i` followed by
complex conjugation in the Wick-rotated frame. (For Euclidean
quantum field theory, `θ` includes the conjugation operation.)

Now consider observables `A` localized in two spacelike-separated
regions on opposite sides of the hyperplane `{x · ê_i = 0}`. By
retained **microcausality** (`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`,
retained), operators at spacelike-separated points commute:
`[A(x), A(y)] = 0` for `(x − y)·(x − y) > 0` in the metric induced
by the time-RP-distinguished direction.

But the spatial-RP condition (1) is the **non-commutative**
Osterwalder-Schrader inner product for path-integral states. For two
spacelike-separated regions, the equal-time Wightman function
`⟨A(x) A(y)⟩` is **real-symmetric** (not Hermitian-conjugate) when
`A(x)` and `A(y)` commute. The OS inner product `⟨A θ_i A^†⟩` then
reduces to `⟨A · A^†⟩`, which is the *positive-definite norm* of `A`
in the Hilbert space — guaranteed positive by Cauchy-Schwarz applied
to the underlying Hilbert structure.

The non-trivial information content of RP is in the **non-commutative
across-hyperplane** factorization. Across the temporal hyperplane,
Heisenberg evolution `e^{−Hτ}` is genuinely non-trivial. Across a
spatial hyperplane, the commutativity of spacelike-separated
operators forces (1) to be a trivial positivity statement — it
doesn't supply OS reconstruction of a Hilbert space along the spatial
direction, because there is no non-trivial spatial "evolution" to
reconstruct.

Conclusion: a candidate spatial RP either (a) reduces to the trivial
Hilbert-space norm (giving no Wick-rotation interpretation) or
(b) conflicts with microcausality (if it required nontrivial
non-commutativity across the spatial hyperplane). Either way, there
is no second non-trivial RP direction.

## Step 2 — Second clock would violate Lieb-Robinson

Suppose, for contradiction, that the framework admits two independent
time-like directions `ê_τ` and `ê_τ'` with codimension-1 foliations
in each, both supporting reflection positivity and unitary
Heisenberg evolution.

Let `U(t)` and `U'(t')` be the unitary evolution groups along `ê_τ`
and `ê_τ'`. For both to satisfy retained **Lieb-Robinson finite
propagation** (`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`),
each must propagate signals at a finite speed bounded by some
Lieb-Robinson velocity `v_LR`.

But: an observable at the spatial origin propagates outward at
velocity `≤ v_LR` under both `U` and `U'`. If `ê_τ` and `ê_τ'` are
linearly independent (the meaning of "two independent time
directions"), then evolving by `U(δt)` followed by `U'(δt')` reaches
a point on the spatial-time-time' grid that should be reachable by
a single unitary `Ũ(δs)` along some combined direction
`ê_s = a ê_τ + b ê_τ'`. By Lieb-Robinson, `Ũ` must also satisfy
finite-speed propagation, with effective velocity bounded by the
maximum of `v_LR` and the geometry of the combined direction.

For this to be consistent with **cluster decomposition**
(`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`,
retained: connected correlations vanish at spacelike infinity), the
"spacelike" structure inherited from the single combined direction
must agree with what each of `U(t)` and `U'(t')` would individually
call spacelike.

But two genuinely independent time directions induce **distinct
causal cones**: a point that is spacelike-separated under `ê_τ` may
be timelike-separated under `ê_τ'`. Cluster decomposition demands a
single notion of "spacelike infinity," contradicting the two-cone
structure.

Formal restatement: a Lorentz signature `(− + + + ... )` with two
time directions becomes ultrahyperbolic — `(−, −, +, +, +, ...)`.
The Cauchy problem for such signatures fails to be well-posed
(Courant-Hilbert / Tegmark; cited in
`ANOMALY_FORCES_TIME_THEOREM.md`). The framework's retained
microcausality + cluster decomposition + Lieb-Robinson chain forces
a single timelike causal cone.

Therefore: **no second independent clock direction.**

## Step 3 — Time-reversal symmetry as the only ambiguity

The single timelike direction `ê_τ` is unique only up to the discrete
time-reversal symmetry `ê_τ → −ê_τ`. This corresponds to the choice
of which half-space the OS reconstruction associates with the "future"
vs the "past." Both choices give equivalent physics under the
retained CPT (`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29`,
retained); the framework's conventions fix one choice.

The single-clock structure is therefore **unique up to time reversal**.

## Conclusion

Combining Step 1 (no spatial RP) and Step 2 (no second clock):

> **On the qubit-`Z^3` lattice framework with retained microcausality,
> Lieb-Robinson, cluster decomposition, and reflection positivity,
> the single-clock codimension-1 evolution structure is unique (up to
> time reversal).**

This closes the uniqueness gap on
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`.

## What this closes

- The conditional gap on `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`:
  *"no-spatial-RP/no-second-clock uniqueness is not closed."*

## What this does not close

- The framework's `d_t = 1` statement still depends on
  `anomaly_forces_time_theorem`'s four bridges (ABJ inconsistency,
  matter completion, chirality, single-clock), which require the
  Grassmann staggered-Dirac gate to close. Those four bridges are
  deferred work; this note closes only the uniqueness gap on the
  single-clock theorem itself.
- Existence of the single-clock structure (the load-bearing content
  of `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`)
  remains a separate claim — this note adds uniqueness.

## Admitted inputs

1. **Retained microcausality** — `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`.
2. **Retained Lieb-Robinson finite-propagation** — same.
3. **Retained cluster decomposition** —
   `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`.
4. **Retained reflection positivity (Cases A and B)** —
   `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29`.
5. **Retained CPT** —
   `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29` (for the
   time-reversal ambiguity statement in Step 3).
6. **Standard Cauchy-problem-well-posedness for hyperbolic signatures**
   — Courant-Hilbert, Tegmark. Cited as external standard mathematics
   for the ultrahyperbolic obstruction in Step 2.

## Citation-graph note

Upstream (all retained):
- `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`
- `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` (Cases A and B)
- `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29`

This note closes the uniqueness gap on
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
by combining the above retained primitives in a Step 1 / Step 2
argument. No new framework primitive is introduced.

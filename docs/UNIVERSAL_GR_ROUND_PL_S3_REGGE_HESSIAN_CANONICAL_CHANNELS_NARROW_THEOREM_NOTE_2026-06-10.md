# The Regge Hessian on the Round PL S³: an Exact Λ-Regge Critical Point with a Multiplicity-Free Canonical Channel Decomposition — the Geometric Route's Channel Structure on the Gate's Own Spatial Atlas

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.py`](../scripts/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.py) (PASS=6 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.txt`](../logs/runner-cache/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.txt)

## Scope

The polarization-frame gate (`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`, `open_gate`) lives
on the `PL S³ × R` scaffold, where the lane's `PL S³` is the boundary of the 4-simplex (5 vertices, 10
edges, 10 triangles, 5 tetrahedra; see
`FULL_PL_S3_ATLAS_COCYCLE_CLOSURE_THEOREM_NOTE_2026-05-03.md` for the lane convention). Its
obstruction: on the scalar route, the localized channel coefficients on the complement of the scalar
channel are **frame-dependent** — no canonical split without an extra bundle primitive. This note
tests the geometric (Regge) construction directly on the gate's own spatial atlas: the **round**
`∂Δ⁴` (all ten edges equal — the PL round S³), with the cosmological term that makes it a critical
point.

The `bounded_theorem` label is the narrow one: the theorem is conditional on the supplied
`Λ`-Regge action and the supplied finite `∂Δ⁴` spatial background. It does not derive action
selection, edge-length degrees of freedom, a `3+1` tick/prism extension, or physical GR dynamics from
the axioms.

## Theorem (runner-verified; structural facts machine-exact)

1. **The round background is an exact `Λ`-Regge critical point (R1).** Every edge of the regular `∂Δ⁴` has
   deficit `δ = 2π − 3·arccos(1/3) ≈ 2.5903 > 0` (positive curvature, exact closed form), and the
   single symmetric `Λ* = δ/(2·∂V/∂ℓ) ≈ 7.3265` makes the `Λ`-Regge equation of motion
   `δ_e = 2Λ·∂V/∂ℓ_e` hold on every edge **exactly** (residual `0.0`) — the closed
   positive-curvature PL analogue of a constant-curvature Einstein spatial slice.
2. **The true Hessian via the curved-background Regge identity (R2).** The complex-level Schläfli/Regge
   identity `∂S_Λ/∂ℓ_e = δ_e − 2Λ·∂V/∂ℓ_e` holds at any configuration, so the Hessian at the round
   point is `H = ∂δ/∂ℓ − 2Λ*·∂²V` — assembled directly from symbolic dihedral/volume gradients;
   `∂δ/∂ℓ` is **symmetric to machine zero** at the curved background, and `H` matches an end-to-end
   finite difference of the actual action.
3. **Multiplicity-free canonical channels (R3) — the round geometric-route obstruction is absent.** `H`
   commutes with the full `S₅` vertex-permutation action (machine zero), and the 10-dimensional edge
   representation decomposes **multiplicity-free**: `10 = 1 ⊕ 4 ⊕ 5` (uniform ⊕ standard ⊕ pair
   irrep). By **Schur's lemma** every equivariant operator is scalar on each channel and the split is
   **unique**: `H = h₁P₁ + h₄P₄ + h₅P₅` exactly (residual `9e-16`). The scalar-route frame ambiguity
   — *which valid frame to use on the degenerate complement* — **does not arise for this supplied
   round geometric route**: there is no degenerate complement at the round point.
4. **The channel spectrum (R4, reported as measured).**

   | channel | dimension | eigenvalue | continuum-S³ reading (qualitative context) |
   |---|---|---|---|
   | uniform | 1 | **`−5.1806`** | the conformal/breathing direction — **negative**, the conformal-factor structure at the critical background |
   | standard | 4 | `+7.9694` | the discrete ℓ=1 / conformal-Killing-type direction (not an exact zero at this coarseness — honest) |
   | pair | 5 | `+9.9644` | the discrete ℓ=2-type (physical) direction — positive |

   The negative conformal channel at the critical background matches the textbook continuum structure
   qualitatively; the coarse 5-vertex complex is not expected to reproduce continuum eigenvalues
   numerically, and the standard channel's nonzero value is the measured discreteness of the
   conformal-Killing remnant.
5. **Isometry control (R5).** The embedded regular 4-simplex has all edges equal and orthogonal
   rotations change no edge length (machine): the configuration's exact invariances are isometries only
   (the complete graph is rigid), so the canonical channel structure is a property of the Hessian's
   symmetry decomposition, not residual gauge freedom.

## What is and is not claimed

- **Is:** the exact `Λ`-Regge critical point on the gate's own spatial atlas; the true curved-background Hessian
  with machine-exact gates; the multiplicity-free canonical channel decomposition (Schur-unique — the
  scalar-route frame-ambiguity mechanism absent for the supplied geometric route at the round point); the
  measured channel spectrum with its qualitative continuum reading.
- **Is not:** the `3+1` prism/tick extension on `S³ × Z_τ` (the gate's full kinematic scaffold) — not
  built; off-round backgrounds (where the `S₅` symmetry breaks and multiplicities could reappear) —
  not analyzed; any continuum-limit statement (the atlas-refinement obstruction of the PL S³ rows
  stands); any retagging of the gate row (audit lane's authority); any derivation of action selection
  or physical GR dynamics; any claim that the standard channel is an exact gauge zero (it is measured
  nonzero at this coarseness). Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **The round point only.** Multiplicity-freeness is a property of the `S₅`-symmetric background; the
  canonicity statement is exactly as strong as the symmetry. Off-round, the question reopens — that is
  the honest residual, named.
- **Spatial slice only** (3D Regge with `Λ`); time remains the emergent record tick, not built here
  (3D+1 framing respected).
- The continuum channel identifications are qualitative context; only the PL facts are check targets.
- Every fact claimed here is computed from the `∂Δ⁴` geometry in-runner; no sibling row is consumed as
  a premise.

## Load-bearing inputs

- Supplied finite background: the round `∂Δ⁴` spatial complex with all ten edge lengths equal.
- Supplied action class: the 3D `Λ`-Regge action `S_Λ = Σ_e ℓ_e δ_e − 2Λ Σ_T Vol_T`.
- Context only, not graph dependencies: `UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`,
  `FULL_PL_S3_ATLAS_COCYCLE_CLOSURE_THEOREM_NOTE_2026-05-03.md`, and
  `CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The complex, its exact background (`2π − 3arccos(1/3)`,
`Λ*`), the Hessian, the projectors, and the spectrum are computed in-runner from the `∂Δ⁴` geometry;
continuum-S³ channel language is qualitative context only and enters no check.

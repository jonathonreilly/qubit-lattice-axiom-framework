# The Regge Hessian on the Round PL S³: an Exact Einstein Background with a Multiplicity-Free Canonical Channel Decomposition — the Geometric Route's Channel Structure on the Gate's Own Spatial Atlas

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.py`](../scripts/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.py) (PASS=6 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.txt`](../logs/runner-cache/frontier_universal_gr_round_pl_s3_regge_hessian_2026_06_10.txt)

## Scope

The polarization-frame gate
([`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md),
`open_gate`) lives on the `PL S³ × R` scaffold, where the lane's `PL S³` is the boundary of the
4-simplex (5 vertices, 10 edges, 10 triangles, 5 tetrahedra —
[`FULL_PL_S3_ATLAS_COCYCLE_CLOSURE...`](FULL_PL_S3_ATLAS_COCYCLE_CLOSURE_THEOREM_NOTE_2026-05-03.md)).
Its obstruction: on the scalar route, the localized channel coefficients on the complement of the
scalar channel are **frame-dependent** — no canonical split without an extra bundle primitive. The
in-review flat-atlas connector row (PR #3492, context) showed the obstruction fails for the geometric
(Regge) generator on `Z³ × Z_τ`. **This note transplants the geometric construction to the gate's own
spatial atlas**: the **round** `∂Δ⁴` (all ten edges equal — the PL round S³), with the cosmological
term that makes it a critical point.

## Theorem (runner-verified; structural facts machine-exact)

1. **The round background is an exact Einstein point (R1).** Every edge of the regular `∂Δ⁴` has
   deficit `δ = 2π − 3·arccos(1/3) ≈ 2.5903 > 0` (positive curvature, exact closed form), and the
   single symmetric `Λ* = δ/(2·∂V/∂ℓ) ≈ 7.3265` makes the `Λ`-Regge equation of motion
   `δ_e = 2Λ·∂V/∂ℓ_e` hold on every edge **exactly** (residual `0.0`) — the PL analogue of the
   Einstein static S³.
2. **The true Hessian via the off-flat Regge identity (R2).** The complex-level Schläfli/Regge
   identity `∂S_Λ/∂ℓ_e = δ_e − 2Λ·∂V/∂ℓ_e` holds at any configuration, so the Hessian at the round
   point is `H = ∂δ/∂ℓ − 2Λ*·∂²V` — assembled from the same symbolic dihedral/volume gradients as the
   landed flat rows; `∂δ/∂ℓ` is **symmetric to machine zero** off-flat, and `H` matches an end-to-end
   finite difference of the actual action.
3. **Multiplicity-free canonical channels (R3) — the gate's obstruction structurally absent.** `H`
   commutes with the full `S₅` vertex-permutation action (machine zero), and the 10-dimensional edge
   representation decomposes **multiplicity-free**: `10 = 1 ⊕ 4 ⊕ 5` (uniform ⊕ standard ⊕ pair
   irrep). By **Schur's lemma** every equivariant operator is scalar on each channel and the split is
   **unique**: `H = h₁P₁ + h₄P₄ + h₅P₅` exactly (residual `9e-16`). The gate's frame ambiguity —
   *which valid frame to use on the degenerate complement* — **cannot arise**: there is no degenerate
   complement on the geometric route at the round point.
4. **The channel spectrum (R4, reported as measured).**

   | channel | dimension | eigenvalue | continuum-S³ reading (qualitative context) |
   |---|---|---|---|
   | uniform | 1 | **`−5.1806`** | the conformal/breathing direction — **negative**, the conformal-factor structure on the Einstein background |
   | standard | 4 | `+7.9694` | the discrete ℓ=1 / conformal-Killing-type direction (not an exact zero at this coarseness — honest) |
   | pair | 5 | `+9.9644` | the discrete ℓ=2-type (physical) direction — positive |

   The negative conformal channel on the Einstein background matches the textbook continuum structure
   qualitatively; the coarse 5-vertex complex is not expected to reproduce continuum eigenvalues
   numerically, and the standard channel's nonzero value is the measured discreteness of the
   conformal-Killing remnant.
5. **Isometry control (R5).** The embedded regular 4-simplex has all edges equal and SO(4) rotations
   change no edge length (machine): the configuration's exact invariances are isometries only (the
   complete graph is rigid), so the canonical channel structure is a property of the Hessian's
   symmetry decomposition, not residual gauge freedom.

## What is and is not claimed

- **Is:** the exact Einstein background on the gate's own spatial atlas; the true off-flat Hessian
  with machine-exact gates; the multiplicity-free canonical channel decomposition (Schur-unique — the
  frame-ambiguity mechanism structurally absent for the geometric route at the round point); the
  measured channel spectrum with its qualitative continuum reading.
- **Is not:** the `3+1` prism/tick extension on `S³ × Z_τ` (the gate's full kinematic scaffold) — not
  built; off-round backgrounds (where the `S₅` symmetry breaks and multiplicities could reappear) —
  not analyzed; any continuum-limit statement (the atlas-refinement obstruction of the PL S³ rows
  stands); any retagging of the gate row (audit lane's authority); any claim that the standard channel
  is an exact gauge zero (it is measured nonzero at this coarseness). Adds no axiom, no primitive, no
  fitted value.

## Boundaries (honest)

- **The round point only.** Multiplicity-freeness is a property of the `S₅`-symmetric background; the
  canonicity statement is exactly as strong as the symmetry. Off-round, the question reopens — that is
  the honest residual, named.
- **Spatial slice only** (3D Regge with `Λ`); time remains the emergent record tick, not built here
  (3D+1 framing respected).
- The continuum channel identifications are qualitative context; only the PL facts are check targets.
- The flat-atlas connector row (PR #3492) is in-review **context**, not a load-bearing dependency —
  every fact here is computed from the `∂Δ⁴` geometry in-runner.

## Load-bearing inputs

- [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md) — the open gate whose atlas and obstruction this note engages.
- [`FULL_PL_S3_ATLAS_COCYCLE_CLOSURE_THEOREM_NOTE_2026-05-03.md`](FULL_PL_S3_ATLAS_COCYCLE_CLOSURE_THEOREM_NOTE_2026-05-03.md) — the lane's PL S³ definition (`∂Δ⁴`, 5/10/10/5).
- [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md) — the landed flat-atlas geometric machinery whose symbolic dihedral-gradient method is reused here (off-flat).

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The complex, its exact background (`2π − 3arccos(1/3)`,
`Λ*`), the Hessian, the projectors, and the spectrum are computed in-runner from the `∂Δ⁴` geometry;
continuum-S³ channel language is qualitative context only and enters no check.

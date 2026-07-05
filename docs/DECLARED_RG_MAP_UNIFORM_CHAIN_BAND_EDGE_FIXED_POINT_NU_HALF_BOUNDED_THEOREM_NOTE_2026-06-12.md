# A Declared Projective Fixed-Energy Schur RG Convention on the Uniform Free Chain: the Quotient Coupling |g| Flows as g²/|1−2g²|, the Unstable Fixed Point 1/2 Sits at the E=0 Resolvent Threshold, and ν = 1/2 Governs the Named Decay Length ξ = 1/arccosh(1/2g) (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (ST4 continuation: the named rescaling-convention follow-on of the landed decimation note; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_declared_rg_map_uniform_chain_band_edge_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_declared_rg_map_uniform_chain_band_edge_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=13 FAIL=0` — exact
dense linear algebra; map agreements at the double-precision floor (measured `0.0` in
these instances, a numerical statement, not an exact-arithmetic claim).

## The declared convention

The landed
[`fixed-energy Schur decimation` note](EXACT_FIXED_ENERGY_SCHUR_DECIMATION_FREE_CHAIN_FORM_MIGRATION_ONE_STEP_MAP_BOUNDED_THEOREM_NOTE_2026-06-11.md)
was panel-corrected to say *not yet RG*: no rescaling convention, no declared
flow space. This note supplies that declared structure — and
the panel's algebra lens then corrected *this* note's first draft (a missed signed
fixed point, an undisclosed pole, the unnamed diverging length); all corrections are
in-runner:

- **Flow space (the sign quotient):** `t → −t` is a unitary equivalence (the staggered
  gauge transformation `c_j → (−1)^j c_j` — verified exactly), so the declared
  coordinate is the **quotient `|g|`, `g = t/μ`**, on the **chart `|g| < 1/√2`**
  (poles at `±1/√2` disclosed; both theorem fixed points and the resolvent threshold
  lie inside).
- **The step:** odd-sublattice Schur decimation at `E = 0` (`b = 2`), normalized by the
  new on-site scale — a **projective fixed-energy Schur RG convention**, not a claim
  of generic Wilsonian RG.

## The findings (runner `PASS=13`)

**(R1) Closure and the map.** The uniform family closes (`diag′ = μ − 2t²/μ`,
`|t′| = t²/|μ|`, no staggered or longer-range terms); the quotient map is
`|g′| = g²/|1 − 2g²|`, verified against the actual Schur output on disjoint grids at
the double-precision floor; evenness in the sign of `g` verified.

**(R2) The signed fixed-point set, complete.** `g = g²/(1−2g²)` ⟺
`g(2g² + g − 1) = 0` ⟺ `g ∈ {0, 1/2, −1}` (all three verified). On the quotient,
the signed point `−1` reads `|g| = 1`, which is a fixed point of the **continued**
quotient map — probed and labeled **outside the declared chart**, not a theorem
claim.

**(R3) The unstable fixed point is the E=0 resolvent threshold.** `|g| ≥ 1/2` iff
`E = 0` lies in the uniform chain's band: below `g* = 1/2` the `E=0` resolvent is
gapped; above it the smallest eigenvalue collapses with size (`6×10⁻³ → 3×10⁻¹⁷`,
`N = 64 → 128` — **a commensurate finite-`N` witness, not the proof**). The
eigenvalue at `g*` is `dg′/dg = 4` exactly (analytic; numeric agreement `4×10⁻¹²`).

**(R4) ν = 1/2 governs a named length.** Below the threshold the `E=0` resolvent
decays with `ξ(g) = 1/arccosh(1/2g)` — **measured** on `N = 128`
(`|[(h)⁻¹]_{0,r}|` log-slope, matched to the analytic form at `2×10⁻¹⁶` relative),
with the near-edge form `ξ ≈ (1/2)/√(1/2 − g)` and the composition law
`ξ(g′) = ξ(g)/2` verified to `1×10⁻¹⁵` at `g → g*`. So
`ν = ln b / ln(dg′/dg) = 1/2` is the exponent of **this** length under **this**
map.

**(R5) The chamber boundary.** From `|g| = 0.45` the iteration flows monotonically to
`0`; from `0.55` it grows and **exits the declared chart** — an `E=0`
spectral/resolvent **chamber boundary** at the unstable fixed point (not a claim of
two thermodynamic phases).

**(R6) Composition with the landed step.** The staggered family decimates into this
closed family in one step (staggered mass exactly `0`; parameters land in the uniform
parameterization at the floor): the landed migration is **step one of this flow**,
with per-step resolvent exactness inherited.

## Scope

Free sector, one dimension, the `E = 0` slice, **this declared convention** (`b = 2`,
quotient `|g|`, chart `|g| < 1/√2`, on-site normalization). **Not claimed:**
universality beyond the declared convention; generic Wilsonian RG; thermodynamic
phases; behavior beyond the chart except as labeled probes; interacting RG; `d = 3`;
gauge sectors; continuum limits. Named next paths: other declared slices (`E ≠ 0`),
`d > 1` block conventions, the gauge-dressed chain (conditional, background-link).
Standard math (method only): Schur complements; staggered gauge transformations;
fixed-point linearization; `arccosh` dispersion lengths.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout. The
audit lane grades.

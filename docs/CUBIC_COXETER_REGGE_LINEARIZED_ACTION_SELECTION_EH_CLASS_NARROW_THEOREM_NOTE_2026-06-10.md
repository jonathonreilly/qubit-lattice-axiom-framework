# Linearized Action-Selection Certificate on the 3+1 Cubic-Coxeter Complex: Embedding-Inert Locality Lands in the Background-Metric EH Class; Regge Realizes the Isotropic Background with c = -1/2

**Date:** 2026-06-10
**Type:** bounded_theorem
**Scope:** conditional linearized `O(k^2)` action-selection certificate for
quadratic edge-length forms satisfying the stated embedding-inertness hypothesis
and declared locality; continuum polynomial ansatz plus sampled declared-stencil
lattice family and direct Regge instantiation. This is not a nonlinear
action-selection theorem.
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.py`](../scripts/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.py) (PASS=9 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.txt`](../logs/runner-cache/frontier_cubic_coxeter_regge_linearized_action_selection_2026_06_10.txt)

## The question (the named-open "action selection" item)

The Regge second-variation source rows
([`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md),
[`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md))
left "action selection — why `S_R`?" as a named-open item. This note answers a
conditional linearized version of that question, on the framework's own complex
(`Z³ × Z_τ`, the tick extension of the retained chain; 3D+1 framing throughout: space = `Z³` by the
Lattice axiom, time = the emergent record tick, `c_t = c_s` per the registered
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)).

**Selection hypothesis, not axiom text:** the Lattice axiom supplies **adjacency,
not an embedding** — vertex positions are not part of the axiom data. This note
studies the additional embedding-inertness hypothesis: flat-space vertex
displacements are exact zero modes at every momentum. Locality = declared finite
stencil. The hypothesis is load-bearing and is not derived here from the Lattice
axiom alone.

## Theorem (runner-verified)

1. **Continuum nullspace, no isotropy assumed.** Among **all** quadratic forms on the 10
   metric components with entries quadratic in `k` and arbitrary constant coefficients (550
   parameters; cubic-anisotropic structures included), the gauge-annihilation condition
   `M(k)·hvec(k∘ξ) = 0 ∀(k,ξ)` has exact coefficient rank `540` on the
   `550`-parameter ansatz, hence a ten-dimensional nullspace, containing the
   in-runner-derived linearized EH pairing.
2. **Background-metric identification.** Under `h → LᵀhL` the gauge family
   at wavevector `k` maps to the gauge family at `Lᵀk` (verified), so the GL(4) pullbacks
   `F_L(k) = T_Lᵀ M_EH(Lᵀk) T_L` are all gauge-annihilating — **one linearized EH form per constant
   flat background metric** `g = LᵀL` (10 parameters). The span of random pullbacks has rank 10 and
   **coincides** with the continuum nullspace (joint rank 10). Within this
   declared `O(k²)` ansatz, mass terms are excluded and the only leading freedom
   beyond one overall constant is **which** flat background metric
   (= anisotropy/units data).
3. **Lattice bridge.** (a) The embedding-inertness hypothesis implies flatness:
   expanding `Q'(k)Γ(k) = 0` at `O(k)`, the
   small-k gauge family spans the constant-`h` metric image, forcing `Q'(0)M(0) = 0` — verified at
   `1.4e-14` on every constructed embedding-inert form. (b) By the line-average lemma (`M(k)h_gauge = Γ(k)ξ`
   **exactly**), the direct metric pullback `P(k)` of any embedding-inert form
   annihilates the continuum gauge family exactly at every `k`; its `O(k²)`
   coefficient therefore lies in the background-metric EH class.
4. **Declared-stencil family probe.** The sampled local lattice quadratic forms
   on the 15 edge classes with stencil `{0, ±e_μ, ±(e_μ+e_ν)}` satisfying the
   embedding-inertness constraints form a four-dimensional nullspace in the
   sampled constraint system. Random elements' `P₂` are fit by a **single**
   element of the ten-dimensional EH class **across tick, space, and mixed
   directions simultaneously** (worst residual `3.3e-7`).
5. **Regge instantiation.** `S_R` is an embedding-inert form
   (exact gauge zeros — the second-variation rows), and its direct `P₂ = −½ × M_EH` at the **isotropic
   background `g = δ`** — the complex's own flat metric (edge lengths `{1,√2,√3,2}` realize `δ`, with
   the tick on equal footing per the kinetic-isotropy primitive) — in the tick, space, **and a
   previously untested mixed direction** `(1,1,0,1)/√3` (`c = −0.5000000` in all three). The constant
   is the textbook `δ²S_R = ½δ²∫√gR` with the variational sign.
6. **Higher-order freedom witness.** The **deficit-squared form** `Σ_t |δδ_t|²` (the
   discrete curvature-squared term, built from the same hinge data as `S_R`) is local, **exactly**
   gauge-annihilating at every momentum (deficits are inert under flat re-embeddings), nonzero at
   finite `k`, and has **zero** leading metric-sector content (relative `4e-9` — pure `O(k⁴)`):
   higher-curvature lattice terms exist, so the selection fixes the **leading order only**.
7. **Mass-term control.** The edge-length mass term (a perfectly local functional) violates
   embedding-inertness at `O(1)` — the hypothesis is load-bearing; the theorem is not vacuous.

## Net (what "why S_R" now means)

Any local edge-length action that satisfies the embedding-inertness hypothesis
and declared locality has **EH-class leading-order linearized physics** in this
scope. The leading freedom is:

- **one overall constant** — its sign/orientation and magnitude are not fixed
  here; the sign residual and the scale-reference units bridge remain context
  only;
- **the flat background metric** — fixed by the complex's own flat geometry (the retained chain's edge
  lengths) with the tick on equal footing (the kinetic-isotropy primitive's structural grant);
- the **O(k⁴) tail** (the lattice-fingerprint sector) and the **nonlinear completion** — both named
  open.

The measured facts of the second-variation rows (isotropy including tick-mixed
directions, the flatness zero modes, `c = −½`) are thereby explained by the
linearized conditional theorem, not left as isolated numerical coincidences.

## What is and is not claimed

- **Is:** the continuum nullspace, the background-metric identification, the
  lattice bridge, the declared-stencil family probe, the Regge instantiation
  including a new direction, the higher-order freedom witness, and the mass-term
  control — all runner-verified at the stated precisions.
- **Is not:** does **not** select the action at the **nonlinear** level (open); does **not** derive
  the edge-length degrees of freedom (they are the supplied dynamical variables, as in the retained
  row's premise); does **not** fix the overall constant's orientation or magnitude (the located sign
  residual + the scale reference, unchanged); does **not** characterize the O(k⁴) sector (the
  companion fingerprint work); the embedding-inertness hypothesis is a framework-native reading of the
  Lattice axiom's adjacency-only character, stated as a hypothesis and not derived from the axiom text
  itself. Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **Linearized / quadratic order around flat only.**
- **Locality = the declared stencils** (550-parameter continuum space; the
  `{0,±e_μ,±(e_μ+e_ν)}` sampled lattice family). The Regge form itself has a
  longer hinge-star stencil and is handled directly.
- **The direct pullback is the theorem object.** A naive pseudo-inverse Schur reduction over the
  non-metric complement is unreliable here (the exactly-decoupled fifth branch leaks an `O(k²)`
  eigenvalue into the complement, faking an `O(1)` shift in special directions — a diagnosed numerical
  artifact, excluded from the claims); the direct pullback is gauge-exact by the line-average lemma
  and is what the theorem constrains.
- Continuum comparator operators are derived in-runner from the curvature definitions; Lovelock,
  Fierz–Pauli, Regge, Rocek–Williams are cited as context only.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — the retained complex whose tick extension carries the construction (and whose flat lengths supply the selected background).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the `c_t = c_s` structural grant (the tick's equal footing in the selected background; nothing beyond the declared grant is used).
- Context only, not load-bearing: the Regge second-variation rows and the 3+1
  target-operator row; the sign-residual note; the scale-reference primitive as
  a units remark.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The classification spaces, constraint systems,
pullback representations, lattice family, and all comparator operators are constructed/derived
in-runner; Lovelock/Fierz–Pauli/Regge/Rocek–Williams appear as context only and enter no check. The
`c = −1/2` and the rank-10 identification are outputs.

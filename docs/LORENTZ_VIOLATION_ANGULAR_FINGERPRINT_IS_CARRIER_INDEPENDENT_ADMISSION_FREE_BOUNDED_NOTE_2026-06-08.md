# The Lorentz-Violation Angular Fingerprint (dim-6, ℓ=4 Cubic Harmonic) Is Carrier-Independent and Admission-Free

**Date:** 2026-06-08
**Type:** bounded scoping theorem (elevates the angular fingerprint from staggered-conditional to admission-free; NOT a new dispersion derivation, NOT a magnitude claim)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_lorentz_fingerprint_carrier_independent_admission_free_exact.py`](../scripts/audit_companion_lorentz_fingerprint_carrier_independent_admission_free_exact.py) (sympy/numpy, 6/6)

## Result

The framework's leading Lorentz-violation (LV) signature — a **dimension-6, `ℓ=4` cubic-harmonic
(`A₁g` of `O_h`), CPT-even, parity-even** operator with a falsifiable `[100]/[111]` factor-3 angular
anisotropy — is established on the **staggered** `Cl(3)/Z³` carrier
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](./EMERGENT_LORENTZ_INVARIANCE_NOTE.md), `retained_bounded`,
"Conditional"), and separately on the **bosonic graph Laplacian**
([`LORENTZ_VIOLATION_DERIVED_NOTE.md`](./LORENTZ_VIOLATION_DERIVED_NOTE.md), `retained_bounded`). The
staggered carrier is one of the framework's two registered Tier-A admissions (`AC_φλ`), which has made the
flagship presentation look *conditional on that admission*.

**This note records the narrow scoping theorem the parent notes do not state: the *angular* fingerprint is
carrier-independent, and therefore admission-free** — where **"admission-free" means free of the registered
Tier-A `AC_φλ` staggered-realization admission** (it remains conditional on the retained nearest-neighbor
kinetic / graph-Laplacian dispersion surface; it is *not* axiom-free or dynamics-free). The angular pattern is
*identical* on the bosonic graph Laplacian and on the `AC_φλ` staggered Dirac — the two carriers differ **only**
in a scalar coefficient. Hence, **within the two nearest-neighbor dispersion primitives, the angular shape is
independent of the carrier coefficient and does not consume `AC_φλ`**: it is fixed by the cubic point-group
structure (`O_h` + exact lattice parity) acting on the nearest-neighbor dispersion, so the `AC_φλ` admission is
**not load-bearing** for it. Only the overall **magnitude** is carrier-dependent (and additionally rides the
un-derived Planck-pin), which stays out of scope.

**Computed (exact, runner):**

- Both nearest-neighbor dispersions expand to `a²p²` (isotropic, Lorentz-invariant) plus an `O(a⁴)` LV term
  that is **purely the cubic invariant `Σ pᵢ⁴`** (the isotropic `|p|⁴` coefficient is zero), with **no
  `a³`/`a⁵` odd term** (exact lattice parity → no dimension-5 operator):
  - bosonic Laplacian `Σ 2(1−cos pᵢa)` → `c₄ = −1/12`;
  - staggered Dirac `Σ sin²(pᵢa)` → `c₄ = −1/3`.
- The two LV terms are `c₄ · (Σ pᵢ⁴)` with the **same angular operator** `Σ pᵢ⁴`; only the scalar `c₄`
  differs (ratio 4). So the angular content is **coefficient-independent**.
- The falsifiable **`[100]/[111]` anisotropy ratio = 3** (`Σnᵢ⁴ = 1` along an axis vs `1/3` along the body
  diagonal) is identical for both carriers — it depends only on the angular operator, not on `c₄`.

**Cited from the parent notes (comparators, cross-checked here, not re-claimed):** the spherical-harmonic
decomposition `Σ nᵢ⁴ = 3/5 + (4√π/15) K₄` with `K₄ = Y₄₀ + √(5/14)(Y₄₄ + Y₄,₋₄)` (only `ℓ=0` and `ℓ=4`, no
`ℓ=2`/`ℓ=6` — cross-checked: isotropic average `3/5`, zero `ℓ=2` projection); the dimension-6 classification;
CPT-exactness; and the experimental bounds (≥7 orders below current sensitivity).

**Conclusion.** The angular LV fingerprint (`ℓ=4` `K₄` shape, `[100]/[111]=3`, parity-even, CPT-even, no
dim-5) is **carrier-independent and `AC_φλ`-admission-free** — fixed by the cubic point-group structure (`O_h` +
exact lattice parity) acting on the nearest-neighbor dispersion, independent of which of the two carrier symbols
is used. The `AC_φλ` staggered admission affects only the magnitude, which — together with the Planck-pin
`a = ℓ_Planck` — remains the un-derived, out-of-scope part.

## Why this matters

This is one of the framework's most distinctive structural predictions: the Standard Model *postulates* exact
Lorentz invariance, whereas here a cubic lattice produces a specific anisotropic LV **shape** distinct from the
comparator classes discussed in the parent notes (the dimension-5/isotropic and isotropic/stochastic forms).
Establishing the angular fingerprint as **`AC_φλ`-admission-free** removes the
one cosmetic dependence (`AC_φλ`) from the result that matters — the falsifiable angular pattern — and isolates
the open part cleanly to the magnitude (the Planck-pin). Any future detection of LV with this cubic `ℓ=4`
pattern would be a structural signature of the lattice; the framework's prediction of the *pattern* does not
depend on its (admitted) fermion realization.

## Scope — what this is and is not

- **Is:** a scoping theorem — the cross-carrier identity (both nearest-neighbor dispersions give the same
  `Σ pᵢ⁴` angular operator) and its consequence (the angular fingerprint is coefficient-/carrier-independent,
  hence admission-free), with the magnitude explicitly fenced as carrier-dependent + Planck-pin-conditional.
- **Is not:** a new derivation of either dispersion (those are the parent notes); a magnitude/number claim
  (the coefficient `c₄` and the Planck-pin are out of scope and un-derived); a claim of full emergent Lorentz
  invariance (this is a Lorentz-*violation* shape); a change to the parent notes' status. It does not assert
  the Planck-pin or any experimental number as a derivation input.
- **Residual:** the overall magnitude `|δE²/E²| ∼ |c₄|(E/M_Pl)²` rides the carrier coefficient and the
  un-derived Planck-pin (`planck_scale_lane`, unaudited); only the angular pattern is admission-free.

## Forbidden-import / reprove-and-cite discipline

- The cross-carrier dispersion expansions, the purity of the `O(a⁴)` term as `Σ pᵢ⁴`, the absence of an
  odd-order (dim-5) term, and the coefficient-independence of the `[100]/[111] = 3` angular ratio are
  **reproven** from the nearest-neighbor dispersion primitives in the runner (sympy/numpy, exact).
- The `K₄` spherical-harmonic identity, the dimension-6 classification, CPT-exactness, and the experimental
  bounds are **comparators** cited to the two parent notes — cross-checked (isotropic `3/5`, zero `ℓ=2`),
  never re-claimed as new. No PDG/experimental value is a derivation input; the magnitude/Planck-pin is
  out of scope and un-derived.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](./EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [`LORENTZ_VIOLATION_DERIVED_NOTE.md`](./LORENTZ_VIOLATION_DERIVED_NOTE.md)

**Independent audit required.** This note asserts no effective-status change.

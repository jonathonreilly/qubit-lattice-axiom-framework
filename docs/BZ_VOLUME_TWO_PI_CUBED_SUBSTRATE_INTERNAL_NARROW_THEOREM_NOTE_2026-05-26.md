# Brillouin-Zone Haar Normalization in the `e^{ik·n}` Coordinate — Bounded Theorem

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note states an
author-side claim boundary; it does not set or predict an audit outcome.
**Primary runner:**
[`scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py`](../scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py)

## Claim

Let the additive group `Z³` be written in its supplied integer basis, and make
the following coordinate choices explicit:

1. characters are parameterized by the angular coordinate `k` through
   `χ_k(n) = exp(i k·n)` for `n ∈ Z³`;
2. the displayed reciprocal coordinate uses that standard full-rank basis
   (equivalently `A = I` in `L = A Z³`); and
3. Haar measure on the compact dual group is probability-normalized.

Then `χ_{k+2πm} = χ_k` for every `m ∈ Z³`, so in this declared coordinate the
dual group is represented as

```text
R³ / (2π Z³).
```

A half-open fundamental cell `[-π, π)³` has coordinate volume `(2π)³`, and
normalized Haar probability is

```text
μ_Haar(dk) = d³k / (2π)³.                                  (1)
```

This is a coordinate-conditioned algebraic statement. The abstract dual group
and its normalized Haar probability are canonical up to isomorphism; the
written factor `(2π)³` is not fixed by bare `Z³` alone. With the equally valid
coordinate `ξ = k/(2π)` and pairing `exp(2π i ξ·n)`, the same measure is

```text
μ_Haar(dξ) = d³ξ.                                           (2)
```

Equations (1) and (2) are the same probability measure in different
coordinates.

## Premises and imports

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic `Z³` lattice and its integer translation structure. It does not select
  an absolute physical lattice spacing or a Fourier-coordinate normalization.
- The pairing `χ_k(n) = exp(i k·n)`, the standard coordinate basis, and Haar
  probability normalization are explicit normalization/boundary conditions of
  this theorem.
- Pontryagin duality, finite-product duality, Haar existence/uniqueness, and
  product Lebesgue measure are disclosed textbook harmonic-analysis inputs.
  They are not claimed as framework-derived results.

No measured, fitted, observational, PDG, or cosmological value is used.

## Proof

### Character-period lemma

For `m,n ∈ Z³`,

```text
χ_{k+2πm}(n)
  = exp(i(k+2πm)·n)
  = exp(ik·n) exp(2π i m·n)
  = χ_k(n),
```

because `m·n` is an integer. Thus the declared angular coordinate is periodic
under `k → k + 2πm` and represents the dual torus as `R³/(2πZ³)`.

### Product-covolume identity

The half-open one-axis cell `[-π,π)` has length `2π`. Product Lebesgue measure
therefore gives

```text
vol([-π,π)³) = (2π)³.                                      (3)
```

Opposite faces represent the same torus points. A closed cube can be used for
integration because its duplicated boundary has measure zero, but the
half-open cell is the one-to-one representative used in the theorem.

### Haar-density corollary

Haar probability on a compact group has total mass one. In the declared
Lebesgue-compatible coordinate its constant density is therefore the reciprocal
of (3), which proves (1).

### Coordinate-change check

For `k = 2πξ`, the Jacobian is `d³k = (2π)³ d³ξ`. Substitution into (1) gives
(2). This explicitly exposes the coordinate dependence of the written
denominator while preserving the invariant normalized Haar measure.

## Full-rank lattice covariance

The same calculation makes the role of the coordinate basis explicit. For a
full-rank real matrix `A` and `L = A Z³`, use physical coordinate `x = An` and
pairing `exp(i k·x)`. A reciprocal basis is

```text
B = 2π A^{-T}.
```

Its cell volume and normalized Haar density are

```text
|det B| = (2π)³ / |det A|,
μ_Haar(dk) = |det A| d³k / (2π)³.                         (4)
```

Their product is one. Formula (4) requires `det A ≠ 0`; it makes no
three-dimensional reciprocal-cell claim for a rank-deficient embedding. For
`A = aI`, it reduces to cell volume `(2π/a)³` and density
`a³ d³k/(2π)³`.

## Scope guard

This note does not claim that:

- bare `Z³` selects the angular coordinate, an absolute lattice spacing, or
  the numerical denominator `(2π)³` without the stated convention;
- a fundamental cell is unique as a subset of `R³`;
- a three-dimensional identity supplies a four-dimensional loop measure,
  Wick rotation, or temporal regulator;
- the result derives `α_bare`, a `4π` coupling factor, Wilson matching,
  generator normalization, a hierarchy primitive, or any empirical value; or
- the continuum placement of Fourier-normalization factors is derived rather
  than chosen.

The theorem is only the exact conditional algebra of the dual-torus coordinate,
reciprocal covolume, and normalized Haar density under the named pairing and
full-rank coordinate hypotheses.

## Verification

The runner declares this note through `AUDIT_INPUT_PATHS`, so its canonical
cache binds both runner content and note content. It checks the character
period, half-open boundary identification, coordinate reparameterization,
variable spacing, a non-orthogonal full-rank basis, and rank-deficient
exclusion using exact symbolic arithmetic. Output labels contain no
platform-dependent floating residuals.

Run:

```bash
PYTHONPATH=scripts python3 scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py
```

Expected terminal lines:

```text
TOTAL: PASS=<count> FAIL=0
CHECK RESULT: coordinate-conditioned Haar algebra passes.
```

The independent audit lane alone decides the claim's audit and effective
status after landing.

# Cosmological Constant — Spectral-Gap Companion

**Claim type:** bounded_theorem (supplied conditional scope; no audit status change)
**Primary runner:** `scripts/frontier_cosmological_constant_spectral_gap.py`

**Date:** 2026-04-12  
**Status:** bounded/conditional cosmology companion. Canonical positive
`Lambda` surface on `main`.

**Current publication disposition:** bounded/conditional cosmology companion
only. Not on the retained flagship claim surface.

## Safe Theorem Surface

**Radius boundary (2026-10-21).** The de Sitter curvature radius ell is
constant, but its global spatial S³ radius is `a(t)=ell cosh(ct/ell)`.
Consequently `lambda_1(S³_a(t))=3/a(t)²` equals `Lambda=3/ell²` only at
the minimum-radius slice, or when an auxiliary sphere is assigned radius ell.
The shared coefficient 3 does not derive the physical identification or
select Lambda. This is a conditional consistency comparison.

For a supplied round metric on `S^3_R`, the first nonzero scalar Laplacian eigenvalue
is

`lambda_1(S^3_R) = 3 / R^2`.

If the vacuum scale is identified with the de Sitter curvature radius
`R_Lambda = c / H_inf`, the same-surface relation is

`Lambda = 3 H_inf^2 / c^2`.

The older present-epoch comparison

`Lambda_pred = 3 H_0^2 / c^2 = 1.59 x 10^-52 m^-2`

is therefore the pure de Sitter limit `H_inf = H_0`, not the general mixed
matter-vacuum relation.

Against the historical numerical comparator supplied in this note

`Lambda_obs = 1.11 x 10^-52 m^-2`,

the ratio is `Lambda_pred / Lambda_obs ~ 1.44`, an `O(1)` comparison after inserting the supplied H_0 scale. This is not an
independent prediction of Lambda or a solution of the vacuum-energy problem.

## What Is Exact vs Conditional

### Exact on the retained internal surface

1. The coefficient `3` is the exact `d = 3` first-eigenvalue coefficient on
   `S^3`.
2. With the additional identification `R=ell`, the conditional IR/geometric
   comparison is `Lambda = lambda_1(S^3_R) = 3 / R^2`. It is not inferred
   from the spectrum alone.
3. The same spectral-gap mechanism is the one used by the bounded dark-energy
   EOS companion:
   [DARK_ENERGY_EOS_NOTE.md](./DARK_ENERGY_EOS_NOTE.md).

### Still conditional

1. The cosmological radius identification is not yet derived on the same
   theorem surface. The current companion now distinguishes the vacuum/de
   Sitter scale `R_Lambda = c/H_inf` from the observed present scale `c/H_0`.
2. The remaining `O(1)` factor is the same matter-fraction issue that appears
   in the bounded `Omega_Lambda` chain:
   [OMEGA_LAMBDA_DERIVATION_NOTE.md](./OMEGA_LAMBDA_DERIVATION_NOTE.md).
3. This is not yet a full FRW / expansion-history derivation.

## What This Is Not

This is **not** the claim that finite lattice vacuum-energy sums automatically
solve the cosmological-constant problem.

That broader vacuum-energy audit is recorded separately in
`COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*)
with
[frontier_cosmological_constant.py](../scripts/frontier_cosmological_constant.py).

That audit is useful because it rules out the wrong mechanism. The controlling
positive companion surface is the `S^3` spectral-gap route.

## Interpretation

The comparison identifies a chosen inverse-square radius with a cosmological
parameter. Roundness and the radius are metric data, not consequences of
S³ topology alone. Substitution of H_0 supplies an observed scale; numerical
agreement cannot establish the spectral-to-vacuum identification. No
calculation here controls ultraviolet vacuum contributions or their coupling
to gravity. The conditional de Sitter relation is `Lambda=3 H_inf²/c²`,
with H_inf the asymptotic de Sitter expansion scale.

## Relationship To Other Cosmology Companions

- [DARK_ENERGY_EOS_NOTE.md](./DARK_ENERGY_EOS_NOTE.md):
  a separately supplied constant vacuum density and conservation law give
  `w=-1`; an evolving spatial spectral gap is not constant
- [OMEGA_LAMBDA_DERIVATION_NOTE.md](./OMEGA_LAMBDA_DERIVATION_NOTE.md):
  matter fraction and flatness convert the same mechanism into the bounded
  `Omega_Lambda` chain
- [COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md](./COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md):
  unifies the vacuum scale, `w = -1`, and present-day `Omega_Lambda`
  reduction on one cosmology-lane surface
- [GRAVITON_MASS_DERIVED_NOTE.md](./GRAVITON_MASS_DERIVED_NOTE.md):
  historical mass-identification proposal; an inverse-square spatial
  eigenvalue alone is not a rest-mass parameter

## Falsifiability

The clean failure modes are:

- if dark energy is not a cosmological constant (`w != -1`) on the final
  cosmology surface, the fixed spectral-gap identification fails
- if the relevant cosmological radius is shown not to be Hubble/formation
  scale on the same route, this companion must be revised

## Canonical Validation

- [frontier_cosmological_constant_spectral_gap.py](../scripts/frontier_cosmological_constant_spectral_gap.py)
- [frontier_dark_energy_eos.py](../scripts/frontier_dark_energy_eos.py)
- [frontier_omega_lambda_derivation.py](../scripts/frontier_omega_lambda_derivation.py)

# Free-Sector Relativistic-QFT Support Diagnostics

**Date:** 2026-06-09
**Claim type:** bounded_theorem (support diagnostics; free-sector and
perturbative checks)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/free_sector_relativistic_qft_support_diagnostics_2026_06_09.py`](../scripts/free_sector_relativistic_qft_support_diagnostics_2026_06_09.py)
**Runner cache:** [`logs/runner-cache/free_sector_relativistic_qft_support_diagnostics_2026_06_09.txt`](../logs/runner-cache/free_sector_relativistic_qft_support_diagnostics_2026_06_09.txt)

## Summary

This note preserves the runner-backed support content from the submitted
free-sector "dominoes" PR while removing the unsupported campaign-closure claims.
It provides four bounded diagnostics:

- sampled Wick-built free-Gaussian `4`-point and `6`-point expressions inherit
  the same `O(a^2)` convergence rate as the covariance in the tested setup;
- the free `4D` Dirac Hamiltonian samples have the expected Hermitian
  `+/-E(p)` spectrum and a positive two-step transfer built from `|H|`;
- equal-time spacelike parity checks show the antisymmetric two-point
  combination vanishes while the symmetric one is nonzero in the sampled free
  target, which is useful input for a spin-statistics route;
- a one-loop symmetric-surface sample gives `z_t = z_s` within numerical
  tolerance.

These are diagnostics, not domino closures. They do not establish full
free-Gaussian measure convergence, a `4D` reflection-positivity theorem,
statistics selection, interacting Lorentz covariance to all orders, or
non-perturbative interacting continuum existence.

## Runner-Verified Result

`TOTAL: PASS=8 FAIL=0`.

The runner uses finite matrix/numerical checks. It is intentionally scoped to
support facts that can be tested directly.

## What This Establishes

- In the sampled free-Gaussian setup, Wick-built higher-point expressions track
  covariance convergence at the expected `O(a^2)` rate.
- The sampled free `4D` Hamiltonian/transfer construction satisfies necessary
  positivity conditions.
- The equal-time spacelike parity check gives the expected vanishing/nonvanishing
  split needed by a spin-statistics argument.
- A one-loop representative calculation is symmetric between time and space on
  the supplied kinetic-isotropic surface.

## What This Does Not Establish

This note does **not** establish:

- the full lattice-measure to continuum-measure bridge;
- the `1+1d` to `4D` arena bridge;
- full `4D` free-fermion reflection positivity;
- a completed OS/Wightman reconstruction;
- spin-statistics selection or CAR as a retained framework result;
- interacting Lorentz covariance to all perturbative orders;
- non-perturbative interacting continuum existence;
- any dimensionless observable, empirical input, or audit status.

## Dependencies

- [FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)
  — conditional reconstruction context and named open gates.
- [EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md](EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — bounded free-continuum assembly support.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — approved primitive for the structural `c_t = c_s` kinetic-form ratio.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — free-continuum two-point context.
- [FREE_SECTOR_SPIN_STATISTICS_LEVEL1_MECHANISM_AND_RECONSTRUCTION_REDUCTION_BOUNDED_NOTE_2026-05-30.md](FREE_SECTOR_SPIN_STATISTICS_LEVEL1_MECHANISM_AND_RECONSTRUCTION_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
  — spin-statistics reduction context; not discharged here.

## Audit Note

The submitted PR said the remaining free-sector dominoes fell, the statistics
antecedent was discharged, the interacting theory was Lorentz-covariant
order-by-order, and the only hard remaining wall was non-perturbative
interacting existence. Those claims are not landed here. The landed claim is
only the bounded support-diagnostic package above.

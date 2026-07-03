# Free-Continuum Poincare Assembly Support from the Kinetic-Isotropy Primitive

**Date:** 2026-06-09
**Claim type:** bounded_theorem (conditional assembly support; free continuum
Gaussian sector)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.py`](../scripts/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.txt`](../logs/runner-cache/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.txt)

## Summary

This note records a bounded assembly check for the **free continuum Gaussian**
target used by the reconstruction chain. The approved
`kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md))
supplies only the structural kinetic-form isotropy `c_t = c_s`, equivalently the
OS0 kinetic normalization of the Euclidean regulator block. It is not a Lorentz
theorem and does not by itself supply boost generators, a measure bridge,
reflection positivity, statistics, interacting dynamics, or empirical content.

With that premise explicitly separated from the theorem work, the runner checks
standard free-continuum algebra used by the conditional reconstruction:

- the free Euclidean Dirac two-point is Spin(4)/SO(4)-covariant in both a
  spatial plane and the mixed `tau-x` plane;
- the mixed Euclidean rotation has the expected Wick-continuation target, a
  metric-preserving Lorentz boost;
- the finite-dimensional Lorentz/Poincare generator algebra closes in the
  standard representation used as the continuum target;
- the forward massive shell remains in the forward cone under sampled boosts;
- the note keeps the lattice-to-continuum measure bridge and interacting
  continuum-existence problem explicit.

The durable result is therefore an **assembly support lemma**: once the free
continuum OS/Wightman hypotheses and the standard OS reconstruction theorem are
available, the kinetic-isotropy primitive removes the specific anisotropic
kinetic-form obstruction for the boost-direction target. The runner does not
prove that the framework's lattice measure has converged to that continuum
Gaussian field, and it does not ratify the abstract OS reconstruction theorem.

## Runner-Verified Result

`TOTAL: PASS=19 FAIL=0`.

The pass count covers algebraic and numerical consistency checks in the free
continuum target. The checklist items are boundary checks, not audit verdicts.

## What This Establishes

- The free continuum Dirac kernel used as the reconstruction target has the
  expected SO(4) covariance, including the mixed time-space Euclidean plane.
- The Wick-continuation target preserves the Minkowski metric and the massive
  on-shell invariant.
- The standard Lorentz/Poincare generator algebra and positive-energy forward
  cone behavior are internally consistent.
- The approved kinetic-isotropy primitive can be cited as the explicit
  structural `c_t = c_s` premise, without treating it as a bounded import or
  Tier-A admission.

## What Remains Open

- The lattice-measure to continuum-measure bridge beyond the two-point level.
- The `1+1d`-to-`4D` arena bridge named in the reconstruction chain.
- Full non-perturbative interacting continuum existence.
- Any claim that the primitive itself derives Lorentz/Poincare covariance.
- Any statistics-selection, reflection-positivity, or interacting-theory result
  not independently supplied by its own source note and audit chain.

## Dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — approved primitive for the structural kinetic-form ratio `c_t = c_s`.
- [AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  — existing single-clock/Wightman-structure context.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — free-continuum SO(4) two-point context.
- [FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)
  — conditional reconstruction surface and named open gates.
- [LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md)
  — free-scalar SO(4) to SO(3,1) companion context.

## Audit Note

The submitted PR phrased the primitive as supplying the missing Lorentz
boost/rotation generators and as assembling a Poincare-covariant Wightman QFT.
That is not landed here. The landed claim is the bounded free-continuum assembly
support lemma above. The independent audit lane remains the only status
authority.

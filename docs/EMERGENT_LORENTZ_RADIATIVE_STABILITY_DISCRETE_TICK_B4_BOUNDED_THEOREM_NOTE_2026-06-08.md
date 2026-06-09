# B4 Hypercubic Velocity-Anisotropy Boundary on the Framework's Kinetic-Isotropy Surface

**Date:** 2026-06-08 (surface-supply update 2026-06-09)
**Claim type:** theorem — premises are the framework axioms plus the approved
`kinetic_isotropy_primitive` (an approved primitive chain-satisfies without
bounding; effective status is set by the audit lane).
**Type:** theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

## 2026-06-09 surface-supply update

The isotropic-hypercubic surface this theorem was previously written to *assume*
is now an **approved framework primitive**: `kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
registered in `docs/audit/data/axiom_premise_nodes.json`, owner-approved in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §6). It supplies the matter kinetic-form
isotropy `c_t = c_s` (the OS0 / hypercubic-symmetric Euclidean regulator). The
companion spacing ratio `a_tau/a_s` is separately fixed by the `LATTICE` axiom's
no-diagonal clause plus retained reachability
([`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)).
Therefore the theorem below is no longer conditional on an *externally supplied*
surface: its surface premise is an approved primitive that chain-satisfies
without bounding. The primitive is owner-approved and independent of
`Lattice + Quantum + Record` + emergent-time + reflection positivity; this note
consumes it, it does not derive it.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py`](../scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt`](../logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt)

## Role

This is a group-theory and finite-lattice theorem. The framework's
kinetic-isotropy surface is now supplied by an approved primitive (see the
surface-supply update above), so the theorem applies to the framework's adopted
surface rather than to a merely hypothetical one.

On the isotropic-hypercubic surface supplied by `kinetic_isotropy_primitive`
(temporal axis on the same nearest-neighbor footing as the three spatial axes,
`c_t = c_s`), the 4D hypercubic group `B4` forbids a marginal velocity-anisotropy
operator of the form

```text
c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2),  c_t != c_s.
```

Equivalently, the diagonal quadratic kinetic form has one invariant
coefficient under `B4`, while the spatial cubic group alone leaves two
coefficients. Therefore any Lorentz-violating residue on that supplied surface
begins at the dimension-6 cubic operator, not at the marginal dimension-4
velocity coefficient.

## Theorem

The `kinetic_isotropy_primitive` supplies the isotropic `Z4` hypercubic surface:

- four nearest-neighbor axes and the full signed-permutation symmetry `B4`;
- a hypercubic-symmetric fermion action, such as the canonical isotropic
  staggered central-difference action (`c_t = c_s`);
- no deliberate temporal/spatial form breaking such as `r_t != r_s` (excluded by
  the primitive's kinetic-form isotropy).

Then:

1. The `B4` invariant space of diagonal quadratic kinetic forms is
   one-dimensional, so `c_t = c_s` is forced.
2. A one-loop self-energy integral with a `B4`-invariant measure has
   `Sigma_t = Sigma_s` by finite relabeling of axes. The runner checks this
   to machine precision across several lattice resolutions.
3. The statement is representation-blind: a gauge representation factor
   multiplies the same zero spacetime difference, so species differences also
   vanish at the marginal operator level.
4. The leading remaining lattice Lorentz-violation term is the dimension-6
   hypercubic dispersion correction. With the approved scale-reference
   primitive `a^-1 = M_Pl`, its size at `E = 1 GeV` is of order
   `(1/3)(E/M_Pl)^2`.

## Boundary

The isotropic surface is supplied by the approved `kinetic_isotropy_primitive`
(the kinetic-form isotropy `c_t = c_s`), not derived here from the Lattice,
Quantum, and Record axioms — those alone supply no kinetic normalization. The
primitive is owner-approved and chain-satisfies without bounding; this theorem
consumes it. The earlier "a future theory note may connect this surface to
physical time" gap is closed by that primitive (form) together with the
no-diagonal/reachability spacing tie (`MIN_TIME_STEP...`); what remains genuinely
open is only the absolute clock rate, which is the records' clock-rate boundary
supplied by the scale-reference primitive.

This note does not itself introduce the primitive (landed separately), does not
compute or audit a continuous-time Lorentz-velocity obstruction (that obstruction
is confined to the non-isotropic surface the primitive declines; see
[`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)),
and does not set a Standard-Model Extension bound comparison.

## Dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the approved primitive supplying the isotropic surface (`c_t = c_s`) this
  theorem's premise; chain-satisfies without bounding.
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  — fixes the companion spacing ratio `a_tau/a_s` from the no-diagonal clause.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) is cited only
  for the axiom boundary: it does not supply time dynamics.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  supplies the approved units conversion `a^-1 = M_Pl` used in the optional
  dimension-6 size estimate.
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
  records the dimension-6 cubic dispersion surface.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  supplies the existing isotropic staggered-action context.
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  is the complementary spatial-cubic boundary: with spatial `O_h` alone, the
  marginal anisotropy is allowed.

## Runner Summary

The runner verifies:

- spatial `O_h` gives two diagonal kinetic coefficients, while `B4` gives one;
- the `B4` self-energy relabeling gives `Sigma_t - Sigma_s = 0` to machine
  precision;
- representation factors cannot turn that zero into a species-dependent
  marginal velocity difference;
- isotropic actions pass and an explicit `r_t != r_s` deformation fails;
- the remaining dimension-6 estimate is Planck-suppressed when the scale
  primitive is used as a units conversion.

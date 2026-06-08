# B4 Hypercubic Velocity-Anisotropy Boundary on a Supplied Z4 Surface

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py`](../scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt`](../logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt)

## Role

This is a bounded group-theory and finite-lattice support theorem. It does
not choose the framework's physical time surface.

If a four-dimensional isotropic hypercubic action is supplied, with a temporal
axis on the same nearest-neighbor footing as the three spatial axes, then the
4D hypercubic group `B4` forbids a marginal velocity-anisotropy operator of
the form

```text
c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2),  c_t != c_s.
```

Equivalently, the diagonal quadratic kinetic form has one invariant
coefficient under `B4`, while the spatial cubic group alone leaves two
coefficients. Therefore any Lorentz-violating residue on that supplied surface
begins at the dimension-6 cubic operator, not at the marginal dimension-4
velocity coefficient.

## Theorem

Assume a supplied isotropic `Z4` hypercubic surface with:

- four nearest-neighbor axes and the full signed-permutation symmetry `B4`;
- a hypercubic-symmetric fermion action, such as the canonical isotropic
  staggered central-difference action;
- no deliberate temporal/spatial form breaking such as `r_t != r_s`.

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

This note does not derive physical UV time, a record tick, a temporal lattice,
or a causal dynamics from the axioms. The Lattice, Quantum, and Record axiom
baseline supplies no time metric or dynamics. A future theory note may try to
connect this supplied `Z4` surface to the framework's physical time; this note
does not do that.

This note also does not compute or audit a continuous-time Lorentz-velocity
obstruction, does not set a Standard-Model Extension bound comparison, and
does not introduce a new Tier-A admission, primitive, or axiom.

## Dependencies

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

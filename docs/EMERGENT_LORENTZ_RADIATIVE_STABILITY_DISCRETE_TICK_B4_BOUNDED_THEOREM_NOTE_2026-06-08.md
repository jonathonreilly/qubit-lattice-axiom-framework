# B4 Hypercubic Velocity-Anisotropy Boundary on the Kinetic-Isotropy Primitive Surface

**Date:** 2026-06-08 (surface-supply update 2026-06-09)
**Claim type:** positive_theorem
**Type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

## 2026-06-09 surface-supply update

The OS0 kinetic-form surface this theorem was previously written to *assume* is
now an approved framework primitive: `kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
registered in `docs/audit/data/axiom_premise_nodes.json`, owner-approved in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6). It supplies only the
matter kinetic-form isotropy `c_t = c_s` (OS0). That removes the old
"externally supplied kinetic-form surface" premise as a bounded import: the
surface premise now chain-satisfies as an approved primitive. This note consumes
that primitive; it does not derive it and does not grant any extra dynamics,
spacing-ratio theorem, physical-time theorem, Lorentz-closure theorem, or audit
verdict.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py`](../scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt`](../logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt)

## Role

This is a group-theory and finite-lattice theorem about the quadratic kinetic
form on the OS0 surface. The surface is now supplied by an approved primitive
(see the surface-supply update above), so it is no longer an unapproved
externally supplied premise.

On the kinetic-form surface supplied by `kinetic_isotropy_primitive`
(`c_t = c_s`, OS0), the corresponding 4D hypercubic kinetic-form symmetry `B4`
forbids a marginal velocity-anisotropy operator of the form

```text
c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2),  c_t != c_s.
```

Equivalently, the diagonal quadratic kinetic form has one invariant coefficient
under `B4`, while the spatial cubic group alone leaves two coefficients. Within
the checked kinetic-form model, any residue on that surface begins at the
dimension-6 cubic operator, not at the marginal dimension-4 velocity
coefficient.

## Theorem

Assume the OS0 kinetic-form surface supplied by `kinetic_isotropy_primitive`:

- the diagonal quadratic kinetic form is invariant under the four-axis
  signed-permutation symmetry `B4`;
- the fermion kinetic action is hypercubic-symmetric in form, such as the
  canonical isotropic staggered central-difference action (`c_t = c_s`);
- no deliberate temporal/spatial kinetic-form breaking such as `r_t != r_s` is
  added.

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

The approved `kinetic_isotropy_primitive` supplies only kinetic-form isotropy
`c_t = c_s`. It does not supply a spacing-ratio theorem, absolute clock rate,
dynamics, physical-time theorem, Lorentz-closure theorem, Standard-Model
Extension bound comparison, or empirical match. Those surfaces remain separate.
This note also does not compute or audit the continuous-time Lorentz-velocity
obstruction; it only records that the obstruction belongs to the non-OS0 surface
not chosen by the primitive.

## Dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the approved primitive supplying the kinetic-form premise (`c_t = c_s`);
  chain-satisfies without bounding.
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

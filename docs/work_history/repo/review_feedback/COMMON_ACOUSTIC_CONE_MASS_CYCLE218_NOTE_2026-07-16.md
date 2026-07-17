# Common-acoustic-cone mass — Cycle 218

**Date:** 2026-07-16

**Authority:** none

**Status:** conditional unit-covariant mass normalization and correction

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/common_acoustic_cone_mass_cycle218_2026_07_16.py
```

## Why this correction is needed

Cycle 210 aligned the numerical rest phase and curvature mass in lattice units.
Cycle 215 later selected an exact field cone whose acoustic speed is

```text
c^2=1/3.
```

Once matter and field are placed on one common acoustic cone, the unit-covariant
relation is not `E_rest=m`.  It is

```text
E_rest=m_inertial c^2.
```

The source quantity with mass units is correspondingly the exchange charge
`E_rest/c^2`.  The earlier numerical equality was a `c=1` convention.  It is
not the invariant equality appropriate to the selected cubic field cone.
This is the unit-covariant correction tested below.  In plain text, the
exchange charge E_rest/c^2 is used throughout.

## Corrected candidate family

The Cycle-210 curvature calculation gives

```text
m_inertial = -3 tan(beta/2).
```

The common-cone condition therefore fixes

```text
E_rest = m_inertial/3 = -tan(beta/2).
```

Together with the existing `det C=1` condition,

```text
6 E_rest + 2 alpha + 3 beta = 0,
```

this fixes

```text
alpha = 3 [tan(beta/2)-beta/2].
```

For the tested low-energy branch, `alpha` is a small higher-order correction
instead of the large phase used by the earlier `E_rest=m` coordinate tuning.

## Result up front

The corrected common-cone family succeeds conditionally.

- The field acoustic slope is isotropic with `c^2=1/3` along axes, face
  diagonals, and body diagonals.
- For beta `-0.2,-0.3,-0.4`, the principal vacuum-relative rest mass
  `E_rest/c^2`, independent dispersion mass, and forced inertia
  agree.  The held-out beta `-0.35` agrees as well.
- Every matter coin and contact correction remains unitary, `det C=1`, and
  covariant in all 24 proper-cubic frames.
- The molecular dispersion shares the field-cone relativistic tangent through
  order `p^2`.  No exact all-momentum Lorentz dispersion is claimed.
- Using exchange charge `E_rest/c^2` in the Cycle-216 kernel gives
  species-independent exchange response for the actual molecular packets.
- Two-object composition adds rest energy and inertial mass.  Spectator records
  do not change either quantity.
- A `2 pi` phase-coordinate lift changes neither the physical coin nor the
  principal rest mass.

Reference rows:

```text
beta       E_rest          m=E_rest/c^2
-0.2       0.1003346721    0.3010040163
-0.3       0.1511352181    0.4534056542
-0.4       0.2027100355    0.6081301065
```

## What changed conceptually

The common scalar is mass, but its appearances carry units:

```text
rest generator:       E_rest = m c^2
dispersion curvature: d^2E/dp^2 = 1/m
forced response:      F/a = m
exchange charge:      Q = E_rest/c^2 = m.
```

Thus the framework should not demand literal equality between a phase/energy
and inertia after a nontrivial cone speed has been selected.  It should demand
the unit-covariant conversion through the same cone.

The old `E_rest=m` family still gives a constant source-to-inertia ratio across
species, so its weak universality tests were not numerically spurious; the
factor can be absorbed into coupling.  But it assigns rest mass
`E_rest/c^2=3m_inertial` on the Cycle-215 cone and therefore does not give one
unit-consistent mass across the rest and inertia lanes.

## Conditions and controls

The common-cone condition remains supplied candidate physics.  Locality,
unitarity, cubic covariance, and `det C=1` do not force it: a phase-shifted
family preserves all those properties while changing `E_rest/(m c^2)` across
species.  The runner includes that ablation.

There is a new and explicit scale cost.  The determinant condition makes the
even-sector phase

```text
alpha = 3 [tan(beta/2)-beta/2] = O(beta^3),
```

so the scalar band is close to an even internal band.  The exact curvature is
recovered only inside a narrower momentum window than the Cycle-210 packet
used.  Cycle 218 therefore uses `10^-5` tangent differences and a
`0.0012`-wide, 8,192-site forced packet.  Broader packets legitimately see
nonquadratic/internal-band corrections; they are not counted as mass
measurements of the tangent theory.

This result also assumes:

- the Cycle-215 acoustic field cone is the cone matter must share;
- the principal vacuum-relative phase is the physical rest energy;
- low-momentum curvature defines inertial mass;
- the Cycle-210 forced-packet test operationalizes inertia; and
- static exchange couples to `E_rest/c^2`.

It is not an empirical Lorentz theorem, an exact continuum dispersion, or a
derivation of the common-cone condition from the four axioms.  It does not add
tensor geometry, nonlinear gravity, radiation, stress energy, occurrence,
record formation, Born frequencies, or a clock-rate theorem.  There is no
axiom conclusion.

## Attribution and scope

The relation `E=mc^2` and relativistic tangent matching are standard physics;
no novelty is claimed for them.  The result here is the internal correction
and exact composition across the selected cubic matter and field candidates.
Global novelty has not been established.

The one-dimensional Thirring-QCA molecule used in Cycles 205–209 is published
prior work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini:

<https://arxiv.org/abs/1804.08508>

The Thirring-QCA is not the proper-cubic common-cone mechanism used here.

This work remains on the draft parking branch and changes no foundation,
axiom, primitive, registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/common_acoustic_cone_mass_cycle218_2026_07_16.py
```

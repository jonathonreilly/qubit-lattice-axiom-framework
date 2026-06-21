# Emergent Lorentz Spatial-BZ Power-Mixing Boundary Theorem

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome, and it does not edit audit/status surfaces.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`](../scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py)
**Cached runner:**
[`logs/runner-cache/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.txt`](../logs/runner-cache/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.txt)

## Claim Scope

On the continuous-time / spatial-`Z^3` surface, the leading
central-difference lattice artifact is a spatial quartic term. Its local
quadratic projection has:

1. zero time-time and time-space components, because the artifact has no `p0`
   dependence; and
2. one `O_h` scalar spatial component, because the signed-permutation orbit
   average of the spatial Hessian is proportional to the spatial identity.

This supplies exact source-side support for the **spatial-only channel** in the
interacting emergent-Lorentz open gate. It does not derive the one-loop
coefficient, the physical fixed-point anomalous dimension, or sufficiency
against Lorentz-violation bounds.

## Statement

Let the time kinetic term be continuous, `p0^2`, and let the spatial kinetic
term be the central-difference lattice expression

```text
sum_i (2/a sin(a k_i/2))^2.
```

Then its small-`a` expansion is

```text
|k|^2 - (a^2/12) sum_i k_i^4 + O(a^4).
```

The leading artifact

```text
A4(k) := k_x^4 + k_y^4 + k_z^4
```

is independent of `p0`. Therefore the second variation of `A4` in the
four-vector variables `(p0, kx, ky, kz)` has zero time row/column. The
`O_h` orbit average of the spatial Hessian is

```text
< Hess_k A4 >_O_h = 4 (kx^2 + ky^2 + kz^2) I_3.
```

Thus the marginal quadratic channel induced by this artifact is spatial-only
and `O_h` scalar:

```text
delta c_t = 0,        delta c_s = lambda,
```

where the coefficient `lambda` is not fixed by this theorem.

## Proof

The runner verifies the expansion

```text
(2/a sin(a k/2))^2 = k^2 - a^2 k^4/12 + a^4 k^6/360 + O(a^6).
```

Since the time kinetic term is `p0^2`, differentiating with respect to `a`
shows there is no lattice-spacing artifact in `p0`.

For `A4 = kx^4 + ky^4 + kz^4`, the four-variable Hessian has zero
`p0,p0` entry and zero mixed `p0,ki` entries. The spatial Hessian is diagonal
before projection. Averaging that spatial Hessian over all signed permutations
of the three spatial axes gives exactly

```text
4 (kx^2 + ky^2 + kz^2) I_3.
```

This proves the structural support statement: a spatial-BZ artifact can feed
the marginal kinetic term only through an `O_h` scalar spatial channel on this
surface. It does not calculate the loop coefficient multiplying that channel.

## What This Claims

- The spatial central-difference artifact begins at `sum_i k_i^4`.
- The artifact has no time component on the continuous-time surface.
- Its quadratic projection is one spatial scalar after the `O_h` orbit average.
- This is exact support for the spatial-only structural part of the Lorentz
  naturalness blocker.

## What This Does Not Claim

- It does not derive the interacting one-loop velocity RG.
- It does not derive the physical value or sign of the power-divergent mixing
  coefficient.
- It does not derive the physical fixed-point anomalous dimension.
- It does not show that the resulting suppression beats experimental
  Lorentz-violation bounds.
- It does not add a custodial symmetry, axiom, primitive, admission, or
  observational comparator.

## Relation To The Interacting Lorentz Open Gate

The parent trace target
`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`
has an audited conditional blocker asking for one-hop support for three
ingredients: the interacting one-loop velocity RG, the spatial-only
power-divergent mixing input, and the physical fixed-point
anomalous-dimension / LV-bound sufficiency comparison. This note addresses only
the second ingredient's **structural channel**. The coefficient and the other
two ingredients remain open.

## Validation

Run:

```bash
python3 scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=13 FAIL=0
VERDICT: exact support for a spatial-only O_h-scalar marginal mixing channel; one-loop coefficient/gamma/LV sufficiency remain open.
```

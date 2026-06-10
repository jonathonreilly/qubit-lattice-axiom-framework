# Spatial Cubic Time-Anisotropy Gate No-Go

**Date:** 2026-06-06
**Claim type:** no-go / scope-repair boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_spatial_cubic_time_anisotropy_gate_2026_06_06.py`](../scripts/frontier_spatial_cubic_time_anisotropy_gate_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_spatial_cubic_time_anisotropy_gate_2026_06_06.txt`](../logs/runner-cache/frontier_spatial_cubic_time_anisotropy_gate_2026_06_06.txt).

## 2026-06-09 premise-supplied update

This note's salvage path — "add an explicit Euclidean kinetic-normalization /
4D-hypercubic premise" — now has an approved premise source: the
`kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)),
which supplies `c_t = c_s`. The no-go below is unchanged as a statement about
what spatial `O_h` *alone* leaves open (two coefficients). Downstream notes may
now cite the primitive as the approved kinetic-form premise; this note itself
does not set any audit verdict or prove broader Lorentz closure. With that
premise, the B4 kinetic-form invariant space collapses to one coefficient
(`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`).
No audit verdict is changed by this pointer.

## Targeted Review Gate

This block targets the active review item
`2026-05-29-pr2203-so4-power-counting-marginal-anisotropy-gate` in
[`docs/repo/ACTIVE_REVIEW_QUEUE.md`](repo/ACTIVE_REVIEW_QUEUE.md).

The review finding is that exact spatial `O_h` / cubic-harmonic
power-counting checks are useful, but they do not imply a full SO(4)
all-`n`-point continuum result on a `Z^3 x Z_tau` surface. A marginal
time-vs-space kinetic anisotropy remains allowed unless an explicit Euclidean
kinetic-normalization or 4D-hypercubic premise is added.

## Result

On a `Z^3 x Z_tau` surface with spatial signed-permutation symmetry `O_h` and
time parity, the quadratic kinetic form has two independent invariant
coefficients:

```text
Q(p) = c_t p_tau^2 + c_s (p_x^2 + p_y^2 + p_z^2).
```

Spatial cubic symmetry allows `c_t != c_s`. This is a marginal kinetic
anisotropy. It is invisible to a quartic/cubic-harmonic artifact check because
it lives at degree two.

Full SO(4) or 4D hypercubic symmetry collapses the invariant space to one
coefficient:

```text
c_t = c_s.
```

Therefore the salvage path is exactly the review finding:

- add an explicit Euclidean kinetic-normalization / 4D-hypercubic premise; or
- narrow the theorem to spatial cubic artifact power counting and avoid full
  SO(4) continuum wording.

## Exact Checks

The runner verifies with exact rational algebra:

- the spatial signed-permutation group has `48` elements;
- the 4D signed-permutation group has `384` elements;
- diagonal quadratic invariants under spatial `O_h` have dimension `2`;
- diagonal quadratic invariants under 4D hypercubic symmetry have dimension
  `1`;
- the anisotropic form `2 p_tau^2 + |p_spatial|^2` is invariant under every
  spatial `O_h` operation;
- the same form fails a time-space swap and a 45-degree SO(4) rotation;
- the isotropic form survives the tested SO(4) rotation;
- a spatial quartic cubic artifact can remain exact while the marginal
  `c_t/c_s` coefficient changes.

## Dynamics Implication

This is a dynamics normalization gate. Spatial lattice artifact control is not
the same as time normalization. A continuum or boost/SO(4) claim needs a
separate bridge that aligns temporal and spatial kinetic coefficients.

This is parallel to the record-dynamics firewall developed elsewhere in the
campaign: the framework can keep exact support for what a runner checks, but it
must not launder an unchecked dynamics premise through a different exact
artifact.

## What This Unlocks

- A direct branch-local answer to the active review item.
- A narrow salvage route for spatial cubic power-counting artifacts.
- A clean premise label for future SO(4) claims: `c_t = c_s`,
  4D-hypercubic symmetry, or equivalent Euclidean kinetic normalization.
- A no-go against full SO(4) continuum wording from spatial cubic checks alone.

## Boundaries

- Does not derive SO(4), Lorentz invariance, OS reconstruction, continuum
  existence, or interacting all-`n`-point covariance.
- Does not reject existing free two-point SO(4) notes that explicitly take a
  continuum/free-theory limit.
- Does not update the active review queue or repo-wide authority surfaces.
- Does not supply the missing Euclidean kinetic-normalization premise; it only
  identifies why that premise is needed.

## Runner Summary

Expected scorecard:

```text
PASS=18 FAIL=0
```

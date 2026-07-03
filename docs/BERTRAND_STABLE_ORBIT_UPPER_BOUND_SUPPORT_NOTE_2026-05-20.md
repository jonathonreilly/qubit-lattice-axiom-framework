# Bertrand Stable-Orbit Upper-Bound Support

**Date:** 2026-05-20
**Type:** bounded_theorem
**Status:** source-side proposal; independent audit lane only
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py)
(SCORECARD: PASS=8, FAIL=0)
**Cached runner output:** [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge_2026_05_29.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge_2026_05_29.txt)
**Related wrapper:** `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`

## 2026-05-29 Non-Narrowing Audit Repair (native Green-kernel bridge)

The 2026-05-28 audit record identified this conditional repair target:

> *"The algebraic stability step closes under the assumed continuum potential. The restricted packet does not close the general continuum dimensional-gravity law beyond the cache-backed d = 3 and d = 4 rows, so the d >= 5 instability portion de"*

with repair: *"missing_bridge_theorem: provide a retained derivation or authority for the continuum V(r) = -k/r^(d-2) law across the integer d >= 5 cases used by the upper-bound argument."*.

This revision takes the direct repair path rather than narrowing to only
`d = 3,4`. The missing continuum law is derived in this packet from the
radial Green kernel of the `d`-dimensional continuum Laplacian:

- for `d >= 3`, the radial function `r^(2-d)` is harmonic away from
  the source under the `d`-dimensional radial Laplacian;
- the normalized Green kernel
  `G_d(r)=1/((d-2)S_{d-1}) r^(2-d)` has unit outward `-grad` flux
  through every sphere `S_r^{d-1}`;
- multiplying by an attractive source strength and absorbing the
  positive normalization into `k` gives exactly
  `V(r) = -k/r^(d-2)`;
- substituting this potential into the radial effective potential gives
  the stability sign `k(d-2)(4-d)/r_c^d`.

No new axiom, observed value, fitted selector, or external physics
constant is introduced. The prior cache-backed `DIMENSIONAL_GRAVITY_TABLE`
rows remain useful context, but the `d >= 5` potential law used here is no
longer a load-bearing extrapolation from that table.

## Claim Boundary

This note records a bounded support argument for the stable-orbit half of the
D=3 upper-bound route. It does not claim a repo-wide axiom change and it does
not claim a complete framework-internal proof of Bertrand's theorem.

The landable support claim is:

> Given a continuum central potential of the form `V(r) = -k/r^(d-2)` with
> `k > 0`, where that form is derived in this packet as the attractive
> Green-kernel shape of the `d`-dimensional continuum Laplacian for
> `d >= 3`, the effective-potential stability calculation gives stable
> circular orbits only for integer `d = 3`; `d = 4` is marginal and
> `d >= 5` is unstable.

This supports the existing upper-bound wrapper by making the elementary
stability part explicit. The current finite-set composition consumes this
stable-circular-orbit edge; the all-bounded-orbits-are-closed part of
Bertrand's theorem remains broader classical context unless separately derived
and audited.

## Inputs

1. **Continuum Laplacian Green-kernel bridge derived here.** The only
   potential law used below is the in-packet radial solution of the
   `d`-dimensional continuum Laplacian for `d >= 3`. The old
   `DIMENSIONAL_GRAVITY_TABLE.md` table is context, not a load-bearing
   dependency for the all-`d >= 5` shape.
2. **Central-force effective potential.** The reduction to
   `V_eff(r)=V(r)+L^2/(2mr^2)` is the standard fixed-angular-momentum
   radial Hamiltonian for a central potential. The differentiations and
   sign test are written out and runner-checked below.
3. **Bertrand closure theorem.** The exact all-`L` closed-orbit theorem is
   not consumed. This note only supplies the stable-circular-orbit
   upper-bound support step.

## Continuum Green-Kernel Derivation

For a radial function `f(r)=r^q` in `d` spatial dimensions,

```text
    Δ_d f = f''(r) + ((d-1)/r) f'(r)
          = q(q+d-2) r^(q-2).
```

Taking `q = 2-d` gives `Δ_d r^(2-d)=0` for `r > 0`.
Let

```text
    S_{d-1} = 2π^(d/2)/Γ(d/2)
```

be the area of the unit `(d-1)`-sphere in `R^d`, and define

```text
    G_d(r) = 1 / ((d-2) S_{d-1}) · r^(2-d),     d >= 3.
```

Then

```text
    -∂_r G_d(r) = 1 / (S_{d-1} r^(d-1)),
```

so the outward flux of `-grad G_d` through any sphere of radius `r` is

```text
    S_{d-1} r^(d-1) · 1/(S_{d-1} r^(d-1)) = 1.
```

Thus `G_d` is the normalized radial Green kernel for the continuum
Laplacian convention used in this support calculation. An attractive
central source has the shape

```text
    V(r) = -K G_d(r) = -k / r^(d-2),     k > 0,
```

after absorbing the positive normalization `K/((d-2)S_{d-1})` into the
single strength parameter `k`. This proves the all-`d >= 3` potential
shape used by the effective-potential calculation below, including the
integer cases `d >= 5`.

## Effective-Potential Calculation

For a central potential

```text
V(r) = -k / r^(d-2),      k = GMm > 0,      d >= 3,
```

the radial effective potential is

```text
V_eff(r) = -k / r^(d-2) + L^2 / (2 m r^2).
```

A circular orbit at `r_c` requires

```text
dV_eff/dr = k(d-2)/r_c^(d-1) - L^2/(m r_c^3) = 0.        (1)
```

The second derivative is

```text
d^2V_eff/dr^2 = -k(d-2)(d-1)/r^d + 3L^2/(m r^4).         (2)
```

Using (1) to eliminate `L^2` gives

```text
d^2V_eff/dr^2 |_{r_c} = k(d-2)(4-d) / r_c^d.             (3)
```

So stable circular orbits require

```text
(d-2)(4-d) > 0.
```

For integer `d >= 3`, this holds only at `d = 3`. The `d = 4` case is
marginal and `d >= 5` is unstable.

## Relation To Dimension Selection

This note can support the upper-bound side of `DIMENSION_SELECTION_NOTE.md`
only in the bounded sense above. It does not by itself prove that the physical Cl(3) local
algebra on the `Z^3` lattice should be replaced by a `Z^d` lattice,
and it does not close the D=3 chain.

The companion bounded support note
`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` records the
atomic-stability route. The lower-bound bridge and single-clock uniqueness
gaps remain open as described in `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`.

## What This Does Not Close

- It does not prove the full Bertrand closed-orbit theorem; that stronger
  theorem is not consumed by the current finite-set composition.
- It does not claim an interacting framework gravity derivation or a
  physical-dimensional substrate replacement; it proves the continuum
  Green-kernel shape used by this support note.
- It does not settle `d = 1` or `d = 2`; those belong to the separate
  lower-bound bridge.
- It does not promote any parent row or audit status.

## Validation

```bash
python3 scripts/bertrand_stable_orbit_green_kernel_bridge.py
# SCORECARD: PASS=8  FAIL=0
```

The runner checks the radial harmonic identity, unit-flux normalization,
potential shape, effective-potential second derivative, and the integer
dimension sign classification (`d=3` stable, `d=4` marginal, all checked
`d>=5` unstable).

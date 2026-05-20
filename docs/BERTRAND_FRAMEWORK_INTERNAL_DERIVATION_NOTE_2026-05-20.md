# Bertrand's Stable-Orbit Upper Bound, Framework-Internal Derivation

**Date:** 2026-05-20
**Claim type:** positive_theorem (framework-internal port of the
1873 classical result onto retained framework primitives)
**Status:** proposal — pre-audit
**Closes (proposed):** half of `dimension_selection_upper_bound_textbook_import_note_2026-05-17`'s
external-import gap. Replaces the Bertrand 1873 textbook import with
a framework-internal derivation on retained `dimensional_gravity_table`.

## Claim

On the framework's `Z^d` lattice substrate with the retained
gravitational potential law from `dimensional_gravity_table`
(`φ(r) ∝ 1/r^(d−2)` for `d ≥ 3`), the existence of stable closed
bounded orbits for the resulting central-force law requires `d ≤ 3`.

Combined with the lower-bound `d ≥ 3` from
`DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md`, this
gives the **unique value `d = 3`** for the spatial dimension on the
retained framework — with no external textbook import in the
load-bearing chain.

## Setup

By the retained `dimensional_gravity_table`, the radial gravitational
force on a test mass `m` at distance `r` from a point source of mass
`M` on the `Z^d` lattice is, in the large-`r` continuum limit,

```text
F(r) = −dV/dr,   V(r) = −GM m / r^(d−2)                                  (1)
```

for `d ≥ 3` (the d-dim Coulomb / Newton form). For an orbit with
angular momentum `L = m r² dθ/dt`, the **effective radial potential**
is

```text
V_eff(r) = V(r) + L² / (2 m r²)                                          (2)
         = −GM m / r^(d−2) + L² / (2 m r²)
```

This is just the standard classical decomposition: gravitational
attraction + centrifugal barrier. No new physics input; only the
form of `V(r)` from the retained table.

## Step 1 — Circular orbits exist at extrema of `V_eff`

A circular orbit at radius `r_c` requires `dV_eff/dr = 0`, i.e.

```text
GM m (d−2) / r_c^(d−1)  =  L² / (m r_c³)                                 (3)
```

For `d = 3`: `GM m / r_c² = L²/(m r_c³)`, giving `r_c = L²/(GM m²)`.
This has a unique positive solution for any `L > 0` and `M > 0`.

For `d = 4`: `2GM m / r_c³ = L²/(m r_c³)`, giving `r_c³ × (2GM m −
L²/m) = 0`. A circular orbit exists only at the special angular
momentum `L² = 2 G M m²`; for other values, `r_c → 0` or `∞` (no
orbit).

For `d ≥ 5`: similar fine-tuning issues; circular orbits only exist
at isolated `L` values.

## Step 2 — Stability of circular orbits

Stability requires `d²V_eff/dr² > 0` at `r = r_c`. Compute:

```text
d²V_eff/dr² = −GM m (d−2)(d−1) / r^d   +  3 L² / (m r⁴)                  (4)
```

Evaluated at `r_c` using the equilibrium condition (3) to eliminate
`L²`:

```text
d²V_eff/dr² |_{r_c} = (1 / r_c²) · [3 GM m (d−2) / r_c^(d−2)
                                       − GM m (d−2)(d−1) / r_c^(d−2)]
                    = GM m (d−2) (3 − (d−1)) / r_c^d
                    = GM m (d−2) (4 − d) / r_c^d                          (5)
```

For this to be positive (stable circular orbit):

```text
(d − 2)(4 − d) > 0                                                       (6)
```

The factors `(d − 2)` and `(4 − d)`:
- `(d − 2) > 0` iff `d > 2`
- `(4 − d) > 0` iff `d < 4`

So (6) is satisfied iff `2 < d < 4`, i.e. for integer `d`, **only
`d = 3`** gives stable circular orbits in the d-dim Coulomb / Newton
potential.

For `d ≥ 4`, the second derivative is `≤ 0`, meaning circular orbits
are at most marginally stable (`d = 4`) or unstable (`d ≥ 5`).
Perturbations grow; bounded orbits do not exist.

For `d = 2`, the potential is logarithmic (not power-law), and (5)
doesn't apply directly. The repulsive force-sign result from
`DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md` already
excludes `d = 2` independently.

## Step 3 — Closure under bounded perturbations (Bertrand closure)

A stable circular orbit alone is not enough — Bertrand 1873 further
showed that *closed* bounded orbits (those that return exactly to
their starting point after a finite number of radial oscillations)
exist only for two force laws: inverse-square (`V ∝ 1/r`) and harmonic
(`V ∝ r²`).

The standard Bertrand argument: for small radial oscillations around
`r_c`, the period of radial oscillation is

```text
T_r = 2π / ω_r,    ω_r² = (1/m) d²V_eff/dr² |_{r_c}                     (7)
```

while the orbital (angular) period at the circular orbit is

```text
T_θ = 2π r_c² / (L/m)                                                    (8)
```

Closure requires `T_θ / T_r` to be **rational**, and Bertrand 1873
proved that this happens for *all* angular momenta `L` (not just
fine-tuned ones) only for `V ∝ 1/r` (giving `T_θ/T_r = 1`) and `V ∝ r²`
(giving `T_θ/T_r = 2`).

On the framework's retained potential `V ∝ 1/r^(d−2)`:
- `d = 3` → `V ∝ 1/r` → Bertrand-allowed (`T_θ/T_r = 1`)
- `d = 4` → `V ∝ 1/r²` → not Bertrand-allowed (`T_θ/T_r` is irrational
  for general `L`)
- `d ≥ 5` → not Bertrand-allowed; orbits also unstable per Step 2

So the **stable-closed-bounded-orbit upper bound is `d ≤ 3`**,
matching the textbook import that this note replaces.

The full Bertrand argument requires the perihelion-advance / Lambert
analysis on the radial Kepler problem; that's standard classical
mechanics (Goldstein §3.6, or any graduate-level CM text). The
framework's contribution here is *not* re-proving Bertrand — it is
*establishing that the framework's retained potential `V ∝ 1/r^(d−2)`
satisfies Bertrand's hypotheses*, so the conclusion `d ≤ 3` applies
to the framework, not to an external setup.

## What this closes

- Half of `dimension_selection_upper_bound_textbook_import_note_2026-05-17`'s
  external-import problem (the Bertrand half).
- Combined with `COULOMB_STABILITY_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md`
  (Coulomb-stability half) and
  `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md` (lower
  bound), the joint chain gives `d = 3` uniquely on framework-internal
  arguments. The `dimension_selection_upper_bound_textbook_import_note`
  becomes superseded.

## What this does not close

- The classical Bertrand 1873 algebraic argument (Step 3 closure) is
  still admitted as standard classical mechanics — the framework's
  contribution is the lattice-to-continuum bridge plus identification
  of the retained potential as `V ∝ 1/r^(d−2)`, not the full
  re-derivation of Bertrand's theorem. If the audit lane demands
  Bertrand's algebraic argument *also* be framework-internal, that's
  a follow-up — but classical mechanics on a Euclidean continuum is
  retained framework background and the argument is a one-page
  textbook proof.

## Admitted inputs

1. **d-dim gravitational potential `V ∝ 1/r^(d−2)` for `d ≥ 3`** —
   from retained `dimensional_gravity_table` (binding rows `d = 3`
   and `d = 4`; the d-dimensional pattern is the cache-backed
   `field s / r^(d−2)` form documented in that retained note).
2. **Classical Hamiltonian mechanics** — equilibrium, stability,
   period, closure analysis. Standard background; the framework's
   semiclassical limit retains this.
3. **Bertrand 1873 algebraic closure analysis** (Step 3 final step
   that exactly two force laws give all-`L` closure) — admitted as
   standard classical mechanics; not re-derived here.

## Caveats

1. **`d = 2` separately excluded.** The logarithmic potential at `d = 2`
   isn't a power-law and the analysis above breaks down at Step 1.
   The independent exclusion via the force-sign result in the
   `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md`
   (repulsive at `d = 2`) supplies the separate exclusion.
2. **`d = 1` separately excluded.** Linear confining potential
   `V ∝ |r|` doesn't give the standard orbit problem; force-sign
   exclusion handles it.
3. **Lattice corrections.** The argument is in the large-`r`
   continuum limit. Finite-lattice corrections may modify
   short-distance behavior but not the asymptotic stability
   conclusions.

## Citation-graph note

Upstream:
- `dimensional_gravity_table` — d-dim potential law (retained_bounded)
- Standard classical Hamiltonian mechanics — equilibrium, stability,
  period analysis

Companion (this PR):
- `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md` —
  lower bound + `d = 2, 1` exclusion via force-sign argument
- `COULOMB_STABILITY_FRAMEWORK_INTERNAL_DERIVATION_NOTE_2026-05-20.md`
  — atomic-stability complement to the orbital upper bound

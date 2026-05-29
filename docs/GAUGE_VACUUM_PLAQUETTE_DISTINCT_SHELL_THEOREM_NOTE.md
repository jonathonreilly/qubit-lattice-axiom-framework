# Gauge-Vacuum Plaquette Distinct-Shell Finite Geometry Packet

**Date:** 2026-04-16
**Type:** bounded_theorem
**Status:** bounded support theorem on the finite four-coordinate Wilson cubical surface
**Script:** `scripts/frontier_gauge_vacuum_plaquette_distinct_shell_theorem.py`

## Load-bearing claim scope

This packet proves only the finite mod-2 cubical-boundary geometry checked by
the runner. The load-bearing inputs are:

- a marked plaquette in a four-coordinate Wilson cubical lattice patch;
- distinct action plaquettes counted by shared lattice edges;
- mod-2 cancellation of plaquette edge boundaries;
- exhaustive enumeration of the one-per-observed-edge four-action candidates
  in the local patch;
- one explicit five-action cube shell witness.

No staggered-Dirac realization, `g_bare` normalization, physical Wilson
coupling value, plaquette reduction law, or beta-effective continuation is a
premise of this bounded theorem.

The exact finite mod-2 cube-shell **geometry** half of this packet — the
four-plaquette lower bound (Theorem 1), the exhaustive `625`-case
four-action exclusion, and the explicit five-action cube-shell witness,
giving minimal distinct connected shell size `6` — is isolated as a
standalone narrow theorem in
[`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md).
The physical strong-coupling **order-in-`beta`** reading of that geometry
(the `beta^5` numerator and `beta^6` vacuum distinct-shell orders in
Corollaries 1-2), together with the still-open full reduction law and its
nonperturbative continuation, stays **bounded** in this packet and is
**not** part of the extracted exact-core note's scope.

## Question

What exact geometric strong-coupling statement can already be proved for the
full interacting plaquette after the naive constant-lift law has been ruled out?

## Answer

The finite distinct-shell statement is:

> On the finite four-coordinate Wilson cubical surface, the minimal
> distinct connected shell containing a marked plaquette is the six-face
> elementary cube boundary.

Equivalently:

- the first **distinct connected** nonlocal numerator shell uses five action
  plaquettes;
- the first connected vacuum shell uses six action plaquettes.

This is a real reusable finite-geometry theorem, but it is **not** by itself
the full onset theorem for `beta_eff(beta)`. Mixed-cumulant onset is a
downstream application, not a premise of this packet.

## Theorem 1: the minimal distinct shell around a marked plaquette is the cube boundary

Fix the observed plaquette `p0` in the `(0,1)` plane.

Any **distinct** plaquette sharing the boundary of `p0` shares exactly one of
its four edges. A distinct plaquette cannot share two edges with `p0`; that
would force it to be the same plaquette.

Therefore any distinct shell closing the four marked edges must use at least
four action plaquettes.

The script exhaustively checks all `5^4 = 625` one-per-edge distinct choices on
the finite local four-coordinate patch and finds:

`no four-action shell closes the boundary of p0`.

An explicit five-action shell does close it: the other five faces of an
elementary cube containing `p0`.

So the minimal distinct connected shell containing a marked plaquette has total
size `6`, i.e. one observed face plus five action faces.

## Corollary 1: the first distinct connected numerator shell is order `beta^5`

> **Bounded strong-coupling reading.** Corollaries 1-2 layer a physical
> strong-coupling-expansion interpretation (one power of `beta` per action
> plaquette) on top of the exact finite geometry of Theorem 1. This
> `beta`-order reading is the **bounded** physical content of this packet
> and is explicitly **out of scope** of the extracted exact-core narrow
> theorem
> [`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md),
> which carries only the mod-2 cube-shell geometry.

In the plaquette numerator, the marked plaquette is already supplied by the
observable insertion. A distinct connected shell therefore first appears when
the action contributes the other five faces of the cube boundary.

So the first distinct connected nonlocal numerator shell is order `beta^5`.

## Corollary 2: the first connected vacuum shell is order `beta^6`

For the vacuum partition function there is no marked face supplied in advance.
Any connected closed shell must therefore contain a seed plaquette plus at least
five others.

The same cube boundary realizes that minimum.

So the first connected vacuum shell is order `beta^6`.

## What this closes

- the exact minimal distinct-shell geometry around a marked plaquette
- the exact first distinct-shell orders for the numerator and vacuum sectors
- a reusable finite strong-coupling shell-geometry packet

## What this does not close

- the full analytic reduction law `P_full(beta) = P_1plaq(beta_eff(beta))`
- the full nonperturbative continuation of `beta_eff(beta)` to `beta = 6`
- repo-wide replacement of the current canonical same-surface plaquette value
- any derivation of the physical Wilson gauge action from staggered fermions
- any `g_bare = 1` normalization theorem
- any new axiom or axiom-reset gate closure

The open coefficient problem is therefore sharper, but it is still open:

> extend the now-closed onset theorem beyond its first exact nonlinear
> coefficient and derive the full nonperturbative reduction law at `beta = 6`.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_distinct_shell_theorem.py
```

Expected summary:

- `THEOREM PASS=6 SUPPORT=1 FAIL=0`

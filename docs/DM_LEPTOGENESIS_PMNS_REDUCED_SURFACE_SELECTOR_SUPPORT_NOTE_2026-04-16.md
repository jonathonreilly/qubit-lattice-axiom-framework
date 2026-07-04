# DM Leptogenesis PMNS Reduced-Surface Selector Support

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16
**Script:** `scripts/frontier_dm_leptogenesis_pmns_reduced_surface_selector_support.py`
**Framework convention:** “axiom” means only `Cl(3)` on `Z^3`

## Question

The existing PMNS-assisted `N_e` selector theorem already found the lowest-action
closure branch on the exact reduced surface by a multistart constrained scan.
The remaining review question was whether that lower-action branch can be
supported as the unique lowest-action branch recovered on the exact reduced
domain by a more systematic optimization argument, rather than just a branch
scan.

This note answers that question on the reduced surface only, but it is kept as
strong optimization support rather than a live theorem-grade certification.

**2026-07-04 repair:** the archived cache's middle candidate no longer survives
live polishing as a distinct stationary branch. The live support statement is
therefore narrowed to the recovered KKT-stable low/high pair and an explicit
negative check that the archived middle point polishes into the low branch.

## What the reduced domain is

The reduction-exhaustion theorem already eliminated all admissible closure
components beyond the fixed native `N_e` seed surface. On that exact domain we
use the compact chart

`(u_1, u_2, v_1, v_2, delta) in [0,1]^4 x [-pi, pi]`

with

`x = 3 XBAR_NE * (u_1, (1-u_1)u_2, (1-u_1)(1-u_2))`

`y = 3 YBAR_NE * (v_1, (1-v_1)v_2, (1-v_1)(1-v_2))`

This chart is exact and surjective onto the fixed native `N_e` seed surface.
So optimization over this compact chart is optimization over the admissible
PMNS-assisted closure domain for this scoped runner.

## What is supported

The runner performs a deterministic compact-chart search plus local polishing
on that exact compact chart.

1. a deterministic compact-chart lattice cover with constrained local
   minimization;
2. a direct branch-polishing pass on the converged stationary representatives.

The live searches recover the same low/high reduced-surface branches already
seen on the refreshed branch. The support result is:

- two recovered stationary closure branches on the reduced surface
- the lower branch is the lowest-action branch in the current reduced-surface search
- the lower branch satisfies favored-column closure exactly
- the lower branch is separated from the next branch by a finite action gap
- the archived middle candidate is explicitly live-polished and is not retained
  as a distinct stationary branch

The lower-action branch is the same exact branch already seen in the earlier
selector theorem:

- `x = (0.471675, 0.553810, 0.664515)`
- `y = (0.208063, 0.464382, 0.247555)`
- `delta ~ 0`
- `S_rel = 0.240906701390`
- `eta / eta_obs = 1`

The archived middle candidate from the stale cache was:

- `x = (0.460724, 0.560504, 0.668773)`
- `y = (0.211572, 0.455054, 0.253373)`
- `delta ~ -1.0e-3`
- `S_rel = 0.242719075805`

On the 2026-07-04 live rerun, polishing that point moves it into the low branch
instead of retaining it as an independent stationary branch. It is therefore a
negative-control / archived-candidate check, not branch evidence.

The higher stationary branch is:

- `x = (0.790189, 0.406763, 0.493048)`
- `y = (0.586185, 0.167566, 0.166248)`
- `delta ~ 0`
- `S_rel = 1.110657539338`

So the finite action gap is:

`Delta S_pair ~= 0.869750837948`

## Scope

This file is kept as **support** rather than live theorem authority because
the current deterministic search still uses previously known branch anchors and
local polishing. So the safe live statement is:

- the reduced-surface search support recovers the KKT-stable low/high pair
  with the same low-action branch
- the low branch remains separated by a finite action gap
- this materially strengthens the PMNS-assisted route
- it is not yet promoted here as a theorem-grade global selector certificate

## Upstream authorities

The runner imports four PMNS-side modules; each has a framework wrapper note:

- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md) — flavor-column functional theorem (`func` module).
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md) — active-projector reduction (`act` module).
- [DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md) — observable-relative action law (`rel` module).
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md) — projector interface supplying `canonical_h`.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_reduced_surface_selector_support.py
```

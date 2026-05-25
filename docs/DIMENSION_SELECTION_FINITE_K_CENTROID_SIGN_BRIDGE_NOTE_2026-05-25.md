---
claim_id: dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Dimension-Selection Finite-k Centroid-Sign Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Scope:** exact runner-support bridge for the current finite-k geometry.
**Status:** finite-k support for the lower-bound runner; no repo-wide
dimension-axiom rewrite and no repo-wide axiom rewrite.
**Primary runner:** `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
**Generated output:** `outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json`

## Purpose

The audit of `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md`
left one precise blocker. This is context for why this bridge exists, not a
load-bearing dependency of the finite-k derivative below:

```text
missing_bridge_theorem:
provide a discrete-to-eikonal bridge theorem, or an independent finite-k sign
proof, showing the runner's normalized centroid shift has the claimed sign for
the stated potential family.
```

This note takes the second route.  It does **not** use Fermat, WKB, or
stationary phase as the load-bearing sign argument.  It differentiates the
actual finite-k, finite-lattice, layer-normalized propagator used by
`scripts/frontier_dimension_selection.py`.

## Runner Surface

The dimension-selection runner measures a final-detector centroid

```text
C(M) = sum_y y |psi_{L_x-1}(M, y)|^2
```

after layer-by-layer propagation through

```text
phi_M(x, y) = -M f_d(r),
r = sqrt((x - x_mass)^2 + (y - y_mass)^2),
```

where

```text
f_1(r) = r,
f_2(r) = log(r),
f_d(r) = r^{-(d-2)}  for d >= 3.
```

The one-step update from layer `x` to `x+1` is the finite matrix

```text
A_x(M)[y+dy, y]
  = exp(i k L_dy [1 + M f_avg]) / L_dy,
L_dy = sqrt(1 + dy^2),
dy in {-1, 0, 1},
```

with `f_avg` the endpoint average of `f_d`.  After every layer, the runner
normalizes the state vector.

## Exact Finite-k Derivative

Let `psi_x(M)` be the normalized state on layer `x`, and let

```text
z_{x+1}(M) = A_x(M) psi_x(M),
psi_{x+1}(M) = z_{x+1}(M) / ||z_{x+1}(M)||.
```

At `M = 0`, the derivative of one edge amplitude is exact:

```text
dA_x/dM |_{M=0}
  = A_x(0) i k L_dy f_avg.
```

Writing `dot psi_x = d psi_x/dM |_{M=0}`, the normalized derivative recursion
is

```text
dot z = A'_x(0) psi_x + A_x(0) dot psi_x,
dot psi_{x+1}
  = [dot z - psi_{x+1} Re <psi_{x+1}, dot z>] / ||z||.
```

The detector centroid derivative is then

```text
dC/dM |_{M=0}
  = sum_y y * 2 Re(conj(psi_{L_x-1}(0,y)) dot psi_{L_x-1}(y)).
```

These are finite-dimensional matrix identities for the exact runner
update.  No eikonal limit or ray approximation enters.

## Result

For the runner constants `k=6.0`, `L_x=40`, `L_y=60`, source at
`y_mid`, and mass offset `+7`, the exact finite-k first derivative is:

| d | `dC/dM at M=0` | sign |
|---|---:|---|
| 1 | `-6178.064177806486` | away |
| 2 | `-693.5367985302938` | away |
| 3 | `+137.43355955069325` | toward |
| 4 | `+119.62276629484603` | toward |
| 5 | `+145.12754503252833` | toward |

The signs match the lower-bound transition:

```text
d <= 2  ->  negative centroid response
d >= 3  ->  positive centroid response.
```

The same runner also checks the finite probe value used by the parent runner
(`M = 0.005`) and recovers the same sign table:

| d | `C(0.005)-C(0)` | sign |
|---|---:|---|
| 1 | `-3.8672175352803855` | away |
| 2 | `-2.151826031186392` | away |
| 3 | `+0.7271976977843124` | toward |
| 4 | `+0.6596476488010232` | toward |
| 5 | `+0.8307846758016488` | toward |

This supplies the finite-k sign bridge that the V2 lower-bound note was
missing for the actual runner surface.

## What This Closes

- It removes WKB/eikonal reasoning as the load-bearing sign argument for the
  `frontier_dimension_selection.py` finite runner's centroid-sign transition.
- It gives an independent finite-k derivative certificate for the sign
  `d <= 2` negative and `d >= 3` positive at the runner's baseline geometry.
- It verifies that the finite probe value `M = 0.005` used by the runner has
  the same sign as the exact first derivative.

## What Remains Open

This note still does **not** prove full retained spatial `d = 3` closure:

- It is runner-specific: it fixes the finite-k sign on the current
  `frontier_dimension_selection.py` geometry, not every lattice size,
  detector, source width, or `k`.
- It does not prove a uniform sign interval for all `M > 0`; it proves the
  exact first derivative at `M = 0` and directly verifies the parent runner's
  finite probe value.
- It does not derive the all-d continuum potential family from A1 plus a
  dimension-free A2.  The potential family remains inherited from the runner
  specification and the existing dimension-selection lane.
- It does not close the upper-bound side (`d <= 3`), where the Bertrand and
  Coulomb packets remain conditional on all-d potential/Coulomb assumptions.
- It does not authorize changing the minimal axiom line from `Z^3` to `Z^d`.

## Review-Loop Bounded-Wall Gate

This is not a no-go theorem. The gate here is applied only to keep the
remaining blockers from being overstated as impossibility claims.

- **N1 alternative routes:** the finite-k derivative route is the route closed
  by this note for the current runner. Uniform `k`/lattice-size control,
  deriving the all-d potential family, closing the upper-bound
  Bertrand/Coulomb side, and proving the coupled self-consistency claim remain
  distinct open routes.
- **N2 wall independence:** the remaining blockers are not presented as an
  inflated independent wall count. The all-d potential authority, upper-bound
  authority, and uniform-parameter generalization are separate residual tasks
  unless a future source note derives one from another.
- **N3 hidden-wall scan:** the runner constants, potential family, source
  placement, layer normalization, and finite probe value are explicit imports
  from `scripts/frontier_dimension_selection.py`, not silently derived
  framework facts.
- **N4 residual match:** this note targets only the auditor's finite-k /
  eikonal bridge blocker on
  `dimension_selection_lower_bound_bridge_v2_2026-05-20`. It does not claim to
  repair the parent dimension-selection upper-bound residuals.
- **N5 rhetoric audit:** negative wording is restricted to the non-claims
  below. No universal statement is made about all runners, all source widths,
  all lattice sizes, all `k`, or all positive `M`.
- **N6 partial-closure path:** the legitimate import-retirement path is a
  retained finite-runner bridge followed by independent audit. The open all-d
  potential and upper-bound tasks should be repaired by source work, not by a
  new axiom.
- **N7 steelman:** a hostile reviewer can still object that an exact
  derivative at `M = 0` for one runner geometry need not control finite
  positive `M` uniformly or prove the full D=3 theorem. This note accepts that
  objection and limits itself to the derivative plus the parent finite-probe
  replay.
- **N8 cross-cycle echo:** prior dimension-selection repairs failed when
  runner support was promoted into retained D=3 language. This note uses the
  narrower bounded-support pattern and leaves downstream promotion to the
  independent audit/dependency process.

Gate result: **PASS for bounded runner support only**. It would fail as a
retained dimension-selection theorem, an axiom rewrite, or a no-go against
alternate D=3 derivation routes.

## Non-Claims

This note does not:

- claim retained D=3 closure;
- claim a repo-wide axiom rewrite;
- claim that `Z^3` has been derived from A1 alone;
- use observed physical dimensions or empirical constants;
- use WKB, Fermat, stationary phase, or ray optics as the load-bearing
  sign argument;
- promote `DIMENSION_SELECTION_NOTE.md` or downstream rows.

## Verification

Run:

```text
python3 scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

The green result certifies the finite-k runner-sign bridge only.  It is a
lower-bound repair artifact, not full retained dimension selection.

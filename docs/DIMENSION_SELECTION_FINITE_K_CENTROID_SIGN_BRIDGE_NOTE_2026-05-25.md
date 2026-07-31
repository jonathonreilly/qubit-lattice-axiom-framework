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
remaining blockers from being overstated as impossibility claims. In the
tables below, `ATTEMPTED` means exercised by this note's exact runner and
`OPEN/UNTESTED` means that the route is not counted as closed.

### N1 — Alternative-route enumeration

| Route | Distinct object / mechanism / terminal obligation | Status and evidence |
| --- | --- | --- |
| Exact finite-`k` tangent recursion | Differentiate the normalized detector centroid for the runner's fixed update, geometry, and `d=1,...,5`; terminate at the sign of `dc_y/dM` at `M=0` plus the parent `M=0.005` replay. | `ATTEMPTED`: this note and `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`; closes only the stated finite certificate. |
| Uniform runner-parameter control | Prove the same sign over a stated interval of `k`, lattice sizes, source widths, detector locations, and positive `M`. | `OPEN/UNTESTED`: the present finite grid and one finite probe do not supply uniform estimates. |
| Framework-internal all-`d` potential derivation | Derive the potential family used by the runner from A1 and dimension-free retained authority instead of importing it as the tested profile family. | `OPEN/UNTESTED`: neither this note nor the runner derives that family. |
| Upper-bound Bertrand/Coulomb closure | Derive the `d <= 3` side from framework-retained Bertrand/Coulomb authority with its all-`d` assumptions discharged. | `OPEN/UNTESTED`: this is outside the finite centroid-sign calculation. |
| Coupled self-consistency closure | Show that the lower sign certificate and upper-bound packet coexist in one framework-internal model without circularly selecting `d=3`. | `OPEN/UNTESTED`: no coupled fixed-point or consistency theorem is provided here. |

Only one of five distinct routes was attempted here. Therefore N1 **fails for
any route-exhaustive negative claim or full dimension-selection closure**. It
does not invalidate the positive fixed-runner certificate actually computed.

### N2 — Collapsed wall-independence audit

Let `W1` be framework-internal all-`d` potential authority, `W2` the
Bertrand/Coulomb upper-bound closure, and `W3` uniformity in the runner
parameters and positive `M`.

| Pair | Closing first closes second? | Closing second closes first? | Collapsed result |
| --- | --- | --- | --- |
| `W1`, `W2` | No: deriving the tested potential family does not prove the orbital/Coulomb upper bound. | No: an upper-bound theorem need not derive the runner's all-`d` potential family. | Independent. |
| `W1`, `W3` | No: a potential derivation alone gives no finite-grid uniform error/sign bound. | No: a numerical uniformity theorem can remain conditional on an imported potential. | Independent. |
| `W2`, `W3` | No: the upper-bound mechanism does not control this detector-centroid discretization. | No: uniform centroid signs do not prove Bertrand/Coulomb closure. | Independent. |

No pair collapses on present authority, so the honest wall count is three.
The coupled self-consistency route is a terminal integration obligation, not a
fourth independent primitive wall.

### N3 — Hidden-wall scan

The phrases `we assume`, `by construction`, `as is standard`, `the framework
provides`, `bridge context`, `background`, `naturally`, `obviously`,
`standard QFT`, `registered`, and `canonical` were scanned in the load-bearing
derivation. There is no load-bearing appeal to standard lore. The runner
constants, potential family, source placement, layer normalization, and
finite probe value are explicit imports from
`scripts/frontier_dimension_selection.py`; they are precisely the bounded
test specification, not framework-derived facts. Uses of "exact" refer only
to differentiation of that declared finite update. Thus no hidden admission
changes the three-wall count above.

### N4 — Residual matching

| Witness | Witness residual | Residual addressed here | Match? |
| --- | --- | --- | --- |
| `docs/DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md`, audit-repair section | Missing discrete finite-`k` sign bridge from the normalized centroid observable, replacing the admitted eikonal/WKB step. | Exact tangent recursion and finite-probe replay for that same normalized centroid and fixed runner geometry. | Yes, for the scientific finite-`k` bridge only. |
| Current audit handoff for this source row | Primary runner could not execute in the isolated audit checkout because its audit-ledger inputs were undeclared. | This repair declares the canonical ledger shards and checks row identity without treating mutable audit status as physics. | Yes, for the runner-artifact defect only. |
| `docs/D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`, upper-bound packet | Conditional all-`d` Bertrand/Coulomb authority on the upper side. | Fixed-runner lower centroid-sign certificate. | No; it is retained only as an open wall, not cited as support. |

The scientific bridge residual and current transport residual must not be
conflated: the runner repair makes the existing finite certificate auditable;
it does not newly close `W1`, `W2`, or `W3`.

### N5 — Rhetoric audit

| Resolution | Tested? | Permitted statement |
| --- | --- | --- |
| Per listed dimension on the fixed runner | Yes, for `d=1,...,5`. | The derivative/probe sign split is certified for these five cases. |
| Per positive mass | No; only the derivative at zero and `M=0.005` are checked. | No all-`M>0` claim. |
| Per runner parameter or lattice geometry | No. | No uniform-parameter claim. |
| Framework-wide / dimension-selection theorem | No. | No retained `d=3` selection or axiom rewrite. |

Every negative phrase is limited to these non-claims; no untested resolution
is turned into an impossibility statement.

### N6 — Partial-closure paths

The existing import-retirement path is to keep the potential and geometry
explicit, prove the finite-runner bound, obtain independent audit, and then
attempt uniform estimates. The upper-bound plan separately permits bounded
Bertrand/Coulomb notes with their imports named; that is a partial-closure
route, not proof that a new axiom is required. Neither path authorizes silently
promoting the present certificate to a framework-internal theorem.

### N7 — Steelman

A hostile reviewer has a live route against any broader conclusion: the sign
of a normalized centroid derivative on one finite lattice can change under
finite positive mass, source-width, detector, lattice-size, or `k` variation,
and even a uniform numerical sign would not derive the all-`d` potential or
the independent Bertrand/Coulomb upper bound. The lower-bound repair itself
shows that changing the load-bearing object—from an admitted eikonal rule to
the exact finite-`k` tangent—can retire a previously named wall. This is a
convincing counter-route, so N7 **fails for a no-go or full closure claim** and
forces the present bounded scope.

### N8 — Cross-cycle echo

`docs/DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md` records that
the older classical-force/WKB route was repaired by changing the
load-bearing object to the exact normalized finite-`k` tangent recursion; that
same mechanism is already used here. `docs/D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`
records a second salvage mechanism: keep upper-bound results bounded and name
their imported all-`d` assumptions rather than advertise a full internal
theorem. That mechanism applies to `W2` as an honest bounded route, but does
not close it. These echoes support narrowing and continued source work, not a
no-go.

Gate result: **FAIL for any negative, route-exhaustive, or full retained
dimension-selection claim (N1 and N7)**. The shippable result is instead the
positive, fixed-runner derivative/probe certificate with three named open
walls. It does not authorize an axiom rewrite or foreclose alternate `d=3`
derivation routes.

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

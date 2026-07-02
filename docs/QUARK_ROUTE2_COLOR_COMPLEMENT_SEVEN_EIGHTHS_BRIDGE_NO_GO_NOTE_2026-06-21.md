# Quark Route-2 Color-Complement Seven-Eighths Bridge No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary / no-go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_color_complement_seven_eighths_bridge_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_color_complement_seven_eighths_bridge_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_color_complement_seven_eighths_bridge_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_color_complement_seven_eighths_bridge_no_go_2026_06_21.txt)
**Authority links:** [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md), [`QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block prunes only the SU(3)-invariant color-complement route to route2_e_E_7_8; it does not compute the Route-2 E-side readout datum."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope

The previous seven-eighths boundary isolates the remaining E-side target as

```text
e_E := q_E - 1 = rho_E / 6 = 7/8.
```

This note tests the color-side candidate

```text
(N_c^2 - 2) / (N_c^2 - 1) = 7/8  at  N_c = 3.
```

That candidate can be read as "all but one" of the eight SU(3) adjoint
directions:

```text
(dim(adj) - 1) / dim(adj) = 7/8.
```

The question is whether the current SU(3)/Fierz/Rconn support surface already
supplies an invariant color-complement selector that can be typed to the
Route-2 E-center excess.

Result: it does not. In fact, the SU(3)-invariant route is obstructed by the
adjoint representation itself. The adjoint has no invariant one-dimensional
line and no invariant rank-seven projector. Therefore the color-complement
`7/8` candidate would require a new adjoint-line selector, a non-invariant
orientation choice, or a separate Route-2 readout bridge.

## Exact Arithmetic

The Fierz/color support surface supplies the standard channel split

```text
N_c x N_c-bar = 1 + adj,
dim(adj) = N_c^2 - 1.
```

At `N_c = 3`,

```text
dim(total) = 9,
dim(adj) = 8,
F_adj = dim(adj) / dim(total) = 8/9.
```

The new color-complement candidate is a different fraction:

```text
C_adj_minus_one := (dim(adj) - 1) / dim(adj) = 7/8.
```

This matches the Route-2 E-center excess target numerically:

```text
e_E = rho_E / 6 = 7/8.
```

But the match is not yet a typed bridge. It would need a reason why the
Route-2 E-center excess sees a seven-dimensional complement inside the
eight-dimensional SU(3) adjoint.

## Adjoint-Line Selector Obstruction

Let `ad(su(3))` act on the eight-dimensional adjoint carrier. The runner
constructs the adjoint matrices from the exact SU(3) structure constants and
checks:

```text
intersection_i ker(ad(T_i)) = 0,
commutant({ad(T_i)}) = scalar multiples of I_8.
```

Consequences:

1. There is no invariant one-dimensional adjoint line.
2. There is no invariant seven-dimensional adjoint complement.
3. Any invariant projector on the adjoint commutes with the adjoint action;
   since the commutant is scalar, an invariant idempotent is either `0` or
   `I_8`, with rank `0` or `8`, never rank `7`.

Thus the candidate fraction `(8 - 1)/8` cannot be produced by an SU(3)
invariant color-complement selector on the current Fierz/Rconn support
surface.

## Relation To The Existing Rconn Boundary

The current Rconn/Fierz route supplies

```text
F_adj = 8/9.
```

Prior Route-2 bridge work already shows that `F_adj` alone is not a Route-2
center readout coefficient. This note attacks the nearby color-complement
variant `7/8` and finds a different obstruction: to get `7/8` from the adjoint
itself, one must remove a single adjoint direction, but the current SU(3)
support surface does not identify such a direction invariantly.

The obstruction is therefore narrower than a global color-route no-go. It
only prunes the route:

```text
SU(3)-invariant Fierz/Rconn color data
  -> invariant adjoint one-line removal
  -> route2_e_E_7_8.
```

It leaves open:

- a non-invariant but physically typed adjoint-line selector;
- a Route-2 tensor/readout primitive that computes `e_E` directly;
- a bridge from a different seven-eighths anchor;
- an approved explicit convention, if later adopted outside this branch.

## No-Go Discipline Gate

**N1 alternative routes.**

| Route | Attempt | Result |
|---|---|---|
| Use `F_adj=8/9` directly | Already tested by the Rconn typed bridge packet | `F_adj` is not typed as the signed Route-2 center ratio. |
| Use `(dim(adj)-1)/dim(adj)=7/8` | Tested here | Requires a distinguished adjoint line; no invariant line exists. |
| Use an invariant rank-seven projector | Tested here | Impossible because the adjoint commutant is scalar. |
| Use a non-invariant adjoint orientation | Not ruled out | Would be new selector content, not current SU(3)-invariant support. |
| Use a direct Route-2 source/readout primitive | Not ruled out | It would bypass the color-complement route. |

**N2 wall independence.**

The block35 wall is independent of the prior `F_adj -> c_TE` wall. The old
wall says `8/9` is not typed as the signed center ratio. This wall says
`7/8` cannot be sourced as an invariant "adjoint minus one" complement without
a new line selector.

**N3 hidden-wall scan.**

The only granted structure is SU(3) Fierz/channel algebra plus the Route-2
readout definitions. No physical `kappa_EW` selector, observed endpoint value,
nearest-rational choice, or new line orientation is used.

**N4 residual matching.**

The residual matches the active S3/Route-2 endpoint blocker because
`e_E=7/8` is exactly equivalent to the remaining E-side datum under the
center-excess denominator `6`.

**N5 rhetoric audit.**

"No-go" means no SU(3)-invariant adjoint-complement bridge from the current
color support surface. It is not a statement against other color routes,
future non-invariant selectors, or direct Route-2 readout primitives.

**N6 partial-closure path scan.**

If a future theorem supplies a physically typed adjoint line, or a Route-2
readout primitive computes `e_E` directly, this no-go would not apply. The
missing object should be recorded explicitly as the new selector or bridge.

**N7 steelman.**

The strongest color-complement steelman is that a specific physical current,
boundary condition, or Route-2 orientation might single out one adjoint
direction. That would evade this invariant no-go, but it is not present in the
current Fierz/Rconn authority surface.

**N8 cross-cycle echo.**

This matches the prior pattern: exact same-rational arithmetic is available,
but the role-typing edge is the theorem content. Block35 adds an invariant
representation-theory obstruction for one concrete color-side `7/8` source.

## Boundary

This note does not establish:

- `rho_E = 21/4` from current primitives;
- `e_E = 7/8` from current primitives;
- a typed bridge from SU(3) color-complement arithmetic to Route-2 E-center
  excess;
- a physical adjoint-line selector;
- a physical `kappa_EW` weighting rule;
- quark-mass, CKM, or S3-time closure;
- any audit verdict.

It records that the SU(3)-invariant adjoint-complement route cannot supply the
needed seven-eighths E-center excess without new selector or bridge content.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_complement_seven_eighths_bridge_no_go_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=51 FAIL=0
```

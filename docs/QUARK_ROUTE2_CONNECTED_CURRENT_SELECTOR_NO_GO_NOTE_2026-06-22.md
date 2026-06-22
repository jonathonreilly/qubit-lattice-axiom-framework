# Quark Route-2 Connected-Current Selector No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for connected-current selector from equivariant two-channel data
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_connected_current_selector_no_go_2026_06_22.py`

Actual current-surface status: no-go for connected-current selector from equivariant two-channel data.

## Scope

Block68 reduced the oriented Rconn bridge magnitude to the connected-current
selector:

```text
kappa = 0
```

in

```text
R_phys(kappa) = F_adj + kappa(1 - F_adj).
```

This block asks whether the exact SU(3) two-channel packet, channel
normalization, CMT scaling, positivity, or bounded OZI-size control derives
`kappa=0`.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Two-Channel Readout Family

The exact color packet supplies two orthogonal channel fractions:

```text
F_adj = 8/9
F_singlet = 1/9.
```

A channel-respecting scalar readout normalized on the adjoint channel has the
form

```text
R_phys(kappa) = F_adj + kappa F_singlet.
```

Thus normalization fixes the adjoint coefficient but leaves `kappa` free.

Representative exact completions are:

| `kappa` | `R_phys(kappa)` | `K_EW=1/R_phys` |
|---:|---:|---:|
| `0` | `8/9` | `9/8` |
| `1/2` | `17/18` | `18/17` |
| `1` | `1` | `1` |

All three respect the same exact Fierz/channel-count decomposition.  The
choice `kappa=0` is the connected-current projector, because it annihilates
the singlet/disconnected channel.  That annihilation is the missing theorem;
it is not implied by the two-channel decomposition itself.

## Control Frames

The runner checks five control frames:

| Frame | Result |
|---|---|
| Channel normalization | Sets adjoint coefficient to one; leaves singlet coefficient `kappa`. |
| CMT scaling | Multiplying both channels by the same factor preserves every sampled `kappa`. |
| Positivity | Admits the interval including `kappa=0`, `1/2`, and `1`. |
| Monotonicity | Orders the family but does not select an endpoint. |
| OZI-size bound | Can make `kappa` small, but exact zero requires a zero bound or an annihilation theorem. |

So bounded singlet suppression is not the same as a connected-current
projection.

## Route-2 Consequence

Using Block68 orientation support, the Route-2 magnitude chain is

```text
c_TE = -R_phys(kappa)
q_E = (5/3) / R_phys(kappa)
rho_E = 6(q_E - 1).
```

Then:

| `kappa` | `q_E` | `rho_E` |
|---:|---:|---:|
| `0` | `15/8` | `21/4` |
| `1/2` | `30/17` | `78/17` |
| `1` | `5/3` | `4` |

Thus the endpoint target is exactly the connected selector endpoint.  The
current two-channel packet does not select that endpoint.

## Result

The direct selector route is blocked:

```text
Fierz/channel-count support
+ adjoint normalization
+ CMT scaling
+ positivity
+ bounded OZI-size control
=> kappa = 0
```

is not a current-surface theorem.

The remaining positive target is a connected-current projector or equivalent
singlet-annihilation theorem:

```text
P_conn(singlet/disconnected channel) = 0.
```

Without that theorem, `R_conn=8/9` remains exact support for a conditional
bridge, not a current-surface derivation of the Route-2 E-center magnitude.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_current_selector_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=53, FAIL=0
```

# Quark Route-2 Rconn Typed-Bridge Factorization No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for typed R_conn bridge closure
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_rconn_typed_bridge_factorization_no_go_2026_06_22.py`

Actual current-surface status: no-go for typed R_conn bridge closure.

## Scope

This block attacks the next source-domain bridge target left by Block66:

```text
c_TE := gamma_T(center)/gamma_E(center) = -R_conn = -8/9.
```

It does not re-run the graph no-path result as the main point.  Instead it
factorizes the tempting bridge into the two independent switches that a typed
theorem would have to supply.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Minimal Bridge Ansatz

The repaired Rconn packet gives the exact SU(3) adjoint fraction

```text
F_adj = 8/9.
```

It also leaves a connected/disconnected selector:

```text
R_phys(kappa) = F_adj + kappa (1 - F_adj).
```

The most economical typed bridge to the Route-2 center ratio has the form

```text
c_TE = sigma * R_phys(kappa),
```

where `sigma` is an endpoint orientation sign.  The target requires two
independent switches:

```text
connected-trace selector `kappa=0`
orientation sign `sigma=-1`
```

Only then does the bridge give

```text
c_TE = -8/9
q_E = (-2)(5/6)/(-8/9) = 15/8
rho_E = 6(q_E - 1) = 21/4.
```

## Exact Classifier

| `sigma` | `kappa` | `c_TE` | `rho_E` | Result |
|---:|---:|---:|---:|---|
| `-1` | `0` | `-8/9` | `21/4` | Target, if both switches are supplied. |
| `+1` | `0` | `+8/9` | `-69/4` | Connected selector with wrong orientation. |
| `-1` | `1` | `-1` | `4` | Orientation sign without connected selector. |
| `+1` | `1` | `+1` | `-16` | Neither target switch. |
| `-1` | `1/2` | `-17/18` | `78/17` | Intermediate disconnected coefficient. |

Solving the target equation over the selector line gives:

```text
sigma = -1 => kappa = 0
sigma = +1 => kappa = -16
```

So the physical selector interval contains only the negative-orientation
connected-trace solution.

## Result

The current support stack proves the conditional algebra, but it does not
derive either switch:

```text
kappa=0
sigma=-1
```

The first is the physical connected-trace selector left open by
`RCONN_DERIVED_NOTE.md`.  The second is a signed endpoint-orientation map
between the SU(3) color channel and the Route-2 `T/E` center readout.  Neither
is supplied by the current Route-2 endpoint carrier or by the repaired Rconn
packet.

Thus the bridge is sharper than a single missing edge:

```text
R_conn -> c_TE=-8/9
```

really means

```text
derive kappa=0 and sigma=-1, then apply endpoint algebra.
```

This block does not rule out those future theorems.  It records that without
both switches, `R_conn=8/9` remains exact support for a conditional bridge,
not a current-surface derivation of the E-center endpoint.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_factorization_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=35, FAIL=0
```

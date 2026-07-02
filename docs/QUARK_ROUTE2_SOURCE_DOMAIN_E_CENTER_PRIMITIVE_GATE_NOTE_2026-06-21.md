# Quark Route-2 Source-Domain E-Center Primitive Gate Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go / source-domain selector boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / source-domain selector boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py`](../scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

## Claim Boundary

The exact Route-2 readout reduction leaves the endpoint target:

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

After the T-side candidates are granted, the irreducible open entry is:

```text
rho_E := beta_E / alpha_E = 21/4.
```

This block asks whether the current source-domain scalar
`delta_A1(center) = 1/6`, `delta_A1(shell) = 0` can itself supply the missing
E-center primitive.

## Result

The scalar is necessary but not sufficient.

The source scalar separates shell from center:

```text
delta_A1(shell) = 0,
delta_A1(center) = 1/6.
```

But in the current Route-2 carrier,

```text
K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T),
```

the same scalar multiplies both channel coordinates. A channel-independent
source law `q = f(delta_A1)` has one value at `delta_A1 = 1/6`; it cannot
simultaneously produce the granted T-center value

```text
q_T = 5/6
```

and the target E-center value

```text
q_E = 15/8.
```

Equivalently, a common affine source law calibrated to the T side gives

```text
q_E = 1 - (1/6) = 5/6,
```

not `15/8`. Calibrating the same common law to the E target gives
`q_T = 15/8`, not `5/6`.

## Channel-Specific Boundary

If the source law is allowed to be channel-specific,

```text
q_X = 1 + sigma_X delta_A1,
```

then the T side fixes only

```text
sigma_T = -1.
```

The E coefficient remains a free channel coefficient:

```text
sigma_E = 0      -> q_E = 1,
sigma_E = -1     -> q_E = 5/6,
sigma_E = 1      -> q_E = 7/6,
sigma_E = 21/4   -> q_E = 15/8.
```

So the positive theorem target is not the existence of `delta_A1`; it is a
typed rule selecting the E-channel coefficient

```text
sigma_E = beta_E / alpha_E = 21/4.
```

## Simple Source-Scaling Probe

The runner also checks nearby simple channel scalings from the T slope
`sigma_T = -1`. These are useful because they avoid observed endpoint data
while testing whether a low-complexity source-domain channel weight is already
enough.

| Candidate source scaling | `sigma_E` | `q_E` |
|---|---:|---:|
| same slope as T | `-1` | `5/6` |
| dimension ratio `d_E/d_T = 2/3` | `-2/3` | `8/9` |
| inverse dimension ratio `d_T/d_E = 3/2` | `-3/2` | `3/4` |
| weight ratio `w_E/w_T = 2/3` | `-2/3` | `8/9` |
| inverse weight ratio `w_T/w_E = 3/2` | `-3/2` | `3/4` |
| same-sign inverse-square weight ratio | `-9/4` | `5/8` |
| sign-flipped inverse-square weight ratio | `9/4` | `11/8` |

None gives `sigma_E = 21/4` or `q_E = 15/8`. This is not an exhaustive no-go
over all future source laws; it is a boundary for the current scalar and these
simple source-domain channel scalings.

## Current-Surface Firewall

This block does not close the parent endpoint triple. It sharpens the missing
primitive:

```text
derive a channel-specific E source coefficient, or an equivalent typed
source/readout bridge, that selects sigma_E = 21/4.
```

The current bank already contains the shell/center source scalar and the
restricted carrier. What remains absent is a typed rule that turns that common
source scalar into the E-channel coefficient rather than a shared scalar law or
a free channel parameter.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=42, FAIL=0
```

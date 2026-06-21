# Quark Route-2 Theta-Slice Channel-Density No-Go

**Date:** 2026-06-21
**Type:** no-go / negative route pruning
**Primary runner:** [`scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py)
**Runner output:** [`outputs/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.txt`](../outputs/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.txt)

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block prunes the exact rank-one theta-to-slice semigroup route as a source of the missing channel-density normalization. It does not rule out source/readout-side primitives."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Question

The Route-2 endpoint target remains the exact readout triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
= (-1, -2, 21/4).
```

Recent blocks sharpened the missing `E` entry to an inverse-square
channel-density primitive. This note asks whether the named
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` surface can supply that primitive
from the exact slice law itself.

## Exact Theta-Slice Family

The current theta-to-slice surface has the exact conditional family

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t),
V_R(t) = exp(-t Lambda_R) u_*.
```

The key structural fact is that `V_R(t)` is common to all source channels.
Therefore every source-side ratio in `P_R c` is preserved by the rank-one
transport.

For example, with the exact reduced family

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]],
```

the runner checks

```text
rho_E=-1   -> q_E/q_T = 1
rho_E=0    -> q_E/q_T = 6/5
rho_E=1    -> q_E/q_T = 7/5
rho_E=21/4 -> q_E/q_T = 9/4
rho_E=6    -> q_E/q_T = 12/5
```

and verifies that all these ratios survive the theta-to-slice transport
unchanged at the tested times.

## No Channel-Density Generation

A common slice factor cannot convert a source-side one-pole rule into the
two-pole inverse-square rule:

```text
(3/2 * s(t)) / s(t) = 3/2, not 9/4.
```

Likewise raw-amplitude response stays raw:

```text
(1 * s(t)) / s(t) = 1.
```

So the exact `Lambda_R` semigroup cannot create the missing channel-dependent
factor. It transports whatever source/readout ratio was already supplied.

## What This Prunes

This block prunes the route:

```text
exact theta-to-slice coupling family
=> channel-density normalization
=> q_E/q_T = 9/4.
```

The current theta-to-slice law is exact and useful, but it is ratio-preserving.
It cannot supply the missing `D_X=A_X/w_X` normalization or an
inverse-square covariance primitive by itself.

## What Remains Open

The remaining target is source/readout-side:

- derive channel-density normalization before theta-to-slice transport;
- derive a density-covariance readout from the tensor primitive;
- prove that the current polynomial carrier cannot supply that normalization;
- develop a different source/readout primitive.

This note does not use observed quark masses, CKM/J targets, live endpoint
proximity, fitted selectors, or a new adopted axiom.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py
```

Expected result:

```text
PASS=16 FAIL=0 TOTAL=16
```

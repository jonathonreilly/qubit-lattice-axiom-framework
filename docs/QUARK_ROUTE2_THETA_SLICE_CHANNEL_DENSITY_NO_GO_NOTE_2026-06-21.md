# Quark Route-2 Theta-Slice Channel-Density No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go / negative route pruning
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / negative route pruning
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.txt)
**Authority links:** [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)


## Question

The Route-2 endpoint target remains the exact readout triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
= (-1, -2, 21/4).
```

Recent blocks sharpened the missing `E` entry to an inverse-square
channel-density primitive. This note asks whether the named
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) surface can supply that primitive
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

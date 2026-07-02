# Quark Route-2 Time-Coupling Direct Consumer Ambiguity Gate

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go / exact support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / exact support boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py`](../scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.txt)
**Authority links:** [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)

## Safe Statement

This packet narrows the direct consumer of the Route-2 readout ambiguity in
the `Theta_R -> Lambda_R` row.

The upstream time-coupling note already supplies the exact conditional family

```text
Xi_P(t ; c) = (P_R c) otimes exp(-t Lambda_R) u_*.
```

The upstream readout-map note already reduces the unresolved endpoint to the
dimensionless readout triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4),
```

with the remaining E-side entry written as `rho_E = beta_E / alpha_E` after
the T-side candidates are granted.

This packet proves the direct-consumer boundary:

> In the exact conditional time-coupling family, changing `rho_E` changes only
> the E-center source factor `1 + rho_E / 6`. The E-shell coupling, T-shell
> coupling, T-center coupling, slice generator `Lambda_R`, transfer, and seed
> law are unchanged.

Therefore the downstream time-coupling ambiguity is exactly readout-local and
one-dimensional on the restricted carrier class. It is not a new slice-dynamics
ambiguity, and it is not removable inside `Lambda_R` once the same nonzero
slice seed is used.

## Exact Algebra

Grant the T-side candidates in the reduced readout family:

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

On the four restricted carrier columns,

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6),
```

the readout outputs are

```text
P(rho_E) E-shell  = (1, 0)
P(rho_E) E-center = (1 + rho_E/6, 0)
P(rho_E) T-shell  = (0, -2)
P(rho_E) T-center = (0, -5/3).
```

So the difference between `rho_E = 0` and `rho_E = 21/4` is exactly

```text
Delta q_E = (1 + (21/4)/6) - 1 = 7/8.
```

It appears only at the E-center source factor.

## Time-Coupling Consequence

For any time `t`, the same exact slice factor is used:

```text
V_R(t) = exp(-t Lambda_R) u_*.
```

Thus

```text
Xi_{21/4}(t ; E-center) - Xi_0(t ; E-center)
  = (7/8, 0) otimes V_R(t),
```

while

```text
Xi_{21/4}(t ; E-shell) - Xi_0(t ; E-shell) = 0,
Xi_{21/4}(t ; T-shell) - Xi_0(t ; T-shell) = 0,
Xi_{21/4}(t ; T-center) - Xi_0(t ; T-center) = 0.
```

Since `V_R(t)` is nonzero on the checked exact slice backbone, the E-center
difference cannot be canceled by reusing the same `Lambda_R` dynamics. The
direct consumer inherits the unresolved E-center readout selector rather than
creating an independent dynamics selector.

## Claim Boundary

This is not an endpoint-triple derivation. It does not prove

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

It only proves where the missing `rho_E = 21/4` entry lands downstream:
exactly as the E-center source multiplier in the conditional
time-coupling family.

The parent [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) should therefore remain
an open gate until the upstream readout-map entry is derived. A future positive
result should attack the upstream readout selector, not invent another
slice-semigroup law.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py
```

Current expected result on this branch:

- `TOTAL: PASS=38, FAIL=0`

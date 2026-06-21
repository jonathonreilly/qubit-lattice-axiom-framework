# Quark Route-2 Polynomial-Carrier Density-Normalization No-Go

**Date:** 2026-06-21
**Type:** no-go / negative route pruning
**Primary runner:** [`scripts/frontier_quark_route2_polynomial_carrier_density_normalization_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_polynomial_carrier_density_normalization_no_go_2026_06_21.py)
**Runner output:** [`outputs/frontier_quark_route2_polynomial_carrier_density_normalization_no_go_2026_06_21.txt`](../outputs/frontier_quark_route2_polynomial_carrier_density_normalization_no_go_2026_06_21.txt)

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block prunes the current class-A polynomial carrier K_R as a source of channel-density normalization. It does not rule out adding a new source/readout primitive that supplies channel weights."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Question

The positive two-pole route needs channel-density normalization:

```text
D_X = A_X / w_X,
q_X proportional to D_X^2.
```

For the `O_h` Route-2 channel weights

```text
w_E = 1/3,
w_T = 1/2,
```

this supplies the density factor

```text
(1/w_E)/(1/w_T) = 3/2
```

and hence the inverse-square covariance

```text
q_E/q_T = (3/2)^2 = 9/4.
```

This note asks whether the current class-A polynomial carrier

```text
K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)
```

already contains enough structure to derive that channel-density
normalization.

## Exact Carrier Symmetry

On the endpoint columns, the runner verifies that the current carrier is
channel-blind up to relabeling:

```text
E-shell  = (1, 0)
T-shell  = (1, 0)
E-center = (1, 1/6)
T-center = (1, 1/6)
```

There is no carrier coordinate carrying `w_E=1/3`, `w_T=1/2`, or the density
factor `3/2`.

Therefore any channel-blind polynomial rule applied to the current endpoint
carrier sees identical E and T data. The runner checks representative shared
polynomial endpoint responses and finds

```text
q_E/q_T = 1
```

for every shared degree tested.

## Free Coefficients Are Not A Derivation

The current restricted readout family allows independent E and T coefficients:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

With the T-side candidates granted, the family

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]]
```

admits many exact values on the same carrier:

| `rho_E` | `q_E` | `q_T` | `lambda=q_E/q_T` |
|---:|---:|---:|---:|
| `-1` | `5/6` | `5/6` | `1` |
| `0` | `1` | `5/6` | `6/5` |
| `1` | `7/6` | `5/6` | `7/5` |
| `21/4` | `15/8` | `5/6` | `9/4` |
| `6` | `2` | `5/6` | `12/5` |

So `rho_E=21/4` can be represented only by supplying the readout coefficient.
The current carrier does not select it.

## What Would Be Needed

The missing normalization is exactly:

```text
1/w_E = 3,
1/w_T = 2.
```

If these channel weights are supplied by a new source/readout primitive, then

```text
(3/2)^2 = 9/4
```

and the endpoint algebra gives

```text
q_E = 15/8,
rho_E = 21/4.
```

But those weights are not produced by the class-A polynomial carrier itself.

## What This Prunes

This block prunes the route:

```text
current polynomial K_R carrier
=> channel-density normalization
=> q_E/q_T = 9/4.
```

It also clarifies the status of independent readout coefficients:

```text
independent P_R coefficients can fit the target,
but fitting P_R is the unresolved map entry, not a derivation.
```

## What Remains Open

Open routes:

- derive channel weights from a new source/readout primitive;
- derive density-covariance readout after an explicit normalization;
- prove a broader no-go over a larger carrier/readout grammar;
- develop the signed source/readout escape from earlier blocks.

This note does not use observed quark masses, CKM/J targets, live endpoint
proximity, fitted selectors, or a newly adopted axiom.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_polynomial_carrier_density_normalization_no_go_2026_06_21.py
```

Expected result:

```text
PASS=24 FAIL=0 TOTAL=24
```

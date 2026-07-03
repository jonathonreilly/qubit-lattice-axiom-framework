# Route-2 Endpoint-Blind Renormalization No-Go: Size-Stable Reparameterizations Cannot Rescue the E-Center Lift

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go / exact negative boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the endpoint-blind finite-box renormalization rescue route for the open `rho_E = 21/4` endpoint.
**Primary runner:** [`scripts/frontier_quark_route2_endpoint_blind_renormalization_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_endpoint_blind_renormalization_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_endpoint_blind_renormalization_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_endpoint_blind_renormalization_no_go_2026_06_21.txt)

## Target

The Route-2 readout endpoint still needs

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

After the T-side candidates are granted, the missing entry is

```text
rho_E = beta_E/alpha_E = 21/4,
q_E = 1 + rho_E/6 = 15/8,
lambda = q_E/q_T = 9/4.
```

The existing box-size scan rules out the naive bulk-limit promotion of the `N=15` measured match. This block asks a narrower follow-up: could a harmless size-stable finite-box renormalization rescue the target without adding a new readout primitive?

## Exact Boundary

Let a finite-box reparameterization be endpoint-blind and separable:

```text
gamma_X(endpoint;N) -> c_X(N) r_endpoint(N) gamma_X(endpoint;N),
X in {E,T}.
```

Then

```text
q_E' = (r_center/r_shell) q_E,
q_T' = (r_center/r_shell) q_T,
lambda' = q_E'/q_T' = q_E/q_T.
```

So this entire class preserves `lambda`. It can hit both `q_E = 15/8` and `q_T = 5/6` only when the unrenormalized `lambda` is already `9/4`.

The box-scan cache has `lambda` near `9/4` only at the pinning box:

| N | `q_T` | `q_E` | `lambda=q_E/q_T` | `(9/4)/lambda` |
|---:|---:|---:|---:|---:|
| 11 | `+0.90206` | `+0.84613` | `+0.9380` | `+2.398` |
| 13 | `+0.87009` | `-0.03887` | `-0.0447` | `-50.35` |
| 15 | `+0.83333` | `+1.87625` | `+2.2515` | `+0.999` |
| 17 | `-0.19680` | `-5.83700` | `+29.6596` | `+0.0759` |
| 19 | `-0.81228` | `-7.45520` | `+9.1769` | `+0.2452` |
| 21 | `-1.31647` | `-8.67461` | `+6.5880` | `+0.3415` |
| 25 | `-2.08540` | `-10.37720` | `+4.9761` | `+0.4522` |
| 29 | `-2.65468` | `-11.52705` | `+4.3422` | `+0.5182` |

The bulk rows miss `9/4`, and for `N >= 17` the required direct `q_E` endpoint factor `15/8 / q_E(N)` is negative. Thus a positive normalization cannot even repair the E lift orientation in the bulk.

## What a Rescue Would Have to Import

The only algebraic rescue is nonseparable:

```text
gamma_E(center)/gamma_E(shell)
```

must be changed relative to

```text
gamma_T(center)/gamma_T(shell).
```

Equivalently, one must supply an E-specific center/shell counterterm with

```text
C_lambda(N) = (9/4) / lambda(N),
```

or directly impose `q_E -> 15/8`. That is not a harmless size-stable reparameterization. It is the missing E-center readout primitive in different notation.

## Scope

This no-go only prunes endpoint-blind and separable finite-box renormalization rescues. It does not prove impossibility over arbitrary future nonlinear observables, a new tensor functional, or an explicitly derived nonseparable E-center primitive. Such a future route would be new science, not a normalization of the current finite-box scan.

## Net

The size-stable-family target is now sharper:

1. a valid positive route must derive a nonseparable E/T center-shell covariance rule, not just rescale finite boxes;
2. any proposed finite-box reparameterization must show whether it preserves `lambda`; if it does, it cannot close the endpoint triple unless `lambda` already equals `9/4`;
3. any proposal that changes `lambda` must name the new readout primitive and prove it rather than hiding it as a renormalization.

## Forbidden-Imports Check

No observed masses, fitted targets, or PDG values are consumed. The runner uses exact endpoint algebra and the existing stack-internal box-size scan cache as a finite-box comparator. The rationals `5/6`, `15/8`, `9/4`, `-8/9`, and `21/4` appear only as the already-named Route-2 endpoint targets.

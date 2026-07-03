# Quark Route-2 Channel Determinant Quotient Gate Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go / conditional support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / conditional support boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py`](../scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.txt)
**Authority links:** [OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md](OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md), [OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md), [OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

## Claim Boundary

The Route-2 readout target is still the missing E-center datum

```text
rho_E = beta_E / alpha_E = 21/4,
```

equivalently, under the granted T-side candidates,

```text
lambda := q_E / q_T = 9/4.
```

The current Schur/quadratic no-go isolates the exact shape of a possible
positive law:

```text
C_X proportional to w_X^-2.
```

A determinant quotient is a tempting way to select a logarithmic scalar. This
block asks whether the existing determinant-context machinery already supplies
a Route-2 channel determinant quotient for the channel weights

```text
w_E = 1/3,
w_T1 = 1/2.
```

## Conditional Positive Map

If the Route-2 channel weights are supplied as positive diagonal determinant
coordinates

```text
S_R = diag(w_E, w_T1),
```

then the determinant scalar

```text
W(S_R) = -log det(S_R) = -log w_E - log w_T1
```

has diagonal-coordinate Hessian coefficients

```text
C_E = 1 / w_E^2 = 9,
C_T1 = 1 / w_T1^2 = 4,
```

so

```text
lambda = C_E / C_T1 = 9/4.
```

With the T-side candidates, the endpoint arithmetic closes exactly:

```text
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

Thus a Route-2 channel determinant quotient plus a diagonal-coordinate Hessian
readout bridge would be sufficient.

## No-Go For The Current Surface

The current determinant-context notes do not supply the Route-2 channel
context. They say that if a determinant-sector readout context is supplied,
then the determinant quotient can select the logarithmic family. They do not
identify `O_h` projector weights as positive diagonal determinant coordinates
of a Route-2 source block, and they do not say that the readout lift is the
diagonal-coordinate Hessian of that determinant scalar.

There is a sharper reason the quotient alone is not enough. The determinant
value does not select the channel coordinate split. These positive diagonal
blocks all have determinant `1/6`:

```text
diag(1/3, 1/2),
diag(1/4, 2/3),
diag(1/6, 1).
```

The determinant-only scalar `-log det` has the same value on all three, but
the diagonal Hessian ratios are different:

```text
(1/3)^-2 / (1/2)^-2 = 9/4,
(1/4)^-2 / (2/3)^-2 = 64/9,
(1/6)^-2 / 1^-2 = 36.
```

So using a coordinate Hessian reintroduces within-fiber data that the
determinant scalar value has intentionally quotiented away. A positive theorem
must supply not only determinant-only log selection, but also the specific
Route-2 channel-coordinate assignment and the Hessian-to-E-center readout map.

## Relation To The Parent S3/Route-2 Gate

This block does not derive the parent endpoint triple. It narrows the next
positive target:

1. prove that the Route-2 `E` and `T1` channel weights are the supplied
   determinant coordinates of a positive diagonal source context;
2. prove that the quotient excludes non-logarithmic one-site readouts; and
3. prove that the diagonal-coordinate Hessian coefficients are the Route-2
   E-center/T-channel readout lifts.

Without those bridges, the parent [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
remains open.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=24, FAIL=0
```

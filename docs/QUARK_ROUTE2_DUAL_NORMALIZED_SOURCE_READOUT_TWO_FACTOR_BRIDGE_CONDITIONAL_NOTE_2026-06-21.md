# Route-2 Dual-Normalized Source/Readout Two-Factor Bridge

**Date:** 2026-06-21  
**Claim type:** bounded_theorem
**Claim scope:** conditional support / exact source-readout normalization boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional-support  
**Trace class:** upstream_support  
**Reachability to target:** supports the open Route-2 endpoint by proving the
two-factor dual-normalization mechanism that would supply `lambda = 9/4`, while
showing current Route-2 source/readout notes do not yet license the two
independent factors.  
**Conditional surface status:** exact-support if a later theorem derives or
licenses two independent dual-normalized source/readout factors on the named
Route-2 tensor primitive surface.  
**Proposal allowed:** false  
**Primary runner:** [`scripts/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.py`](../scripts/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.txt)

## Boundary

This note does not derive `rho_E = 21/4`, does not close the Route-2 endpoint
triple, does not update an audit verdict, and does not claim a unique exact
`Theta_R -> Lambda_R` coupling theorem.

It attacks the remaining positive target exposed by the inverse-square and
factor-degree no-go stack:

```text
q_X proportional to w_X^-2.
```

The result is a conditional support theorem. A finite-frame Riesz dual
normalization of a local arm functional supplies exactly one reciprocal local
projector-weight factor. Therefore two independent dual-normalized legs, one
on source preparation and one on readout evaluation, supply the total
reciprocal degree two needed for `lambda = 9/4`. The current Route-2 notes do
not yet prove that both legs are present in the physical tensor primitive
chain; that is the remaining license gap.

No observed masses, fitted targets, PDG values, nearest-rational selection, or
live endpoint fit is used.

## Current Inputs

The exact six-arm `O_h` star gives per-arm projector weights

```text
w_A1 = 1/6,   w_E = 1/3,   w_T1 = 1/2,
kappa = w_T1 / w_E = 3/2.
```

The Route-2 readout-map reduction leaves, after granting the two T-side
candidates, one missing E-channel map entry:

```text
q_T = 5/6,
q_E = 1 + rho_E / 6,
lambda = q_E / q_T,
center T/E = -2 q_T / q_E.
```

The endpoint target is

```text
lambda = 9/4,
q_E = 15/8,
rho_E = 21/4,
center T/E = -8/9.
```

The current tensor/readout source notes still leave the exact endpoint theorem
open:

- [`S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md`](S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md) defines a staging object under
  named admitted inputs and says it does not derive those inputs, including
  the exact reduced shell amplitude or physical tensor-primitive bridge.
- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) defines a bilinear carrier under
  named inputs and explicitly does not derive the physical tensor primitive.
- [`S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md) gives a bounded
  response Jacobian, not an exact tensor observable or exact endpoint
  coefficient theorem.
- [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) imports the missing readout-map
  endpoint triple as the blocker for uniqueness.

## Finite-Frame Dual-Normalization Lemma

Let `H` be a finite real Hilbert space, `P_X` an orthogonal projector, and `a`
a unit local arm vector. Define the local projector weight

```text
w_X = <a, P_X a> = ||P_X a||^2.
```

Assume `w_X != 0`. Let `v_X = P_X a`. The unique minimum-norm covector on the
projected channel whose response to the local arm is one is, by the Riesz
identification,

```text
ell_X(y) = <v_X, y> / w_X.
```

Indeed,

```text
ell_X(a) = <P_X a, a> / w_X = 1,
||ell_X||^2 = ||v_X||^2 / w_X^2 = 1 / w_X.
```

So a dual-normalized unit-local-arm source or readout leg carries one
reciprocal local projector-weight factor. This is not a new Route-2 axiom; it
is finite-frame Riesz algebra. The physics question is whether the Route-2
source/readout chain has one such leg or two independent such legs.

## Source/Readout Consequence

If a single leg is dual-normalized, the induced E/T covariance is

```text
lambda_single = (1 / w_E) / (1 / w_T1)
              = w_T1 / w_E
              = 3/2.
```

With `q_T = 5/6`, this gives

```text
q_E = 5/4,
rho_E = 3/2,
center T/E = -4/3.
```

So one dual normalization is not enough.

If source preparation and readout evaluation are independently
dual-normalized, the response product has two reciprocal factors:

```text
lambda_double = (1 / w_E^2) / (1 / w_T1^2)
              = (w_T1 / w_E)^2
              = 9/4.
```

Then the endpoint algebra gives exactly

```text
q_E = 15/8,
rho_E = 21/4,
center T/E = -8/9.
```

This is the positive-side bridge: the target value is not merely numerically
present as `kappa^2`; it is exactly the output of two independent local Riesz
dual normalizations.

## License Gap On The Current Surface

The current Route-2 surface does not yet license the two-factor bridge as a
theorem about the physical tensor primitive.

The existing notes provide:

1. an exact restricted carrier/readout reduction;
2. a bounded or definition-only tensor staging surface;
3. exact endpoint algebra showing which map entry remains missing;
4. no theorem that source preparation and readout evaluation are independently
   Riesz-dual-normalized against the local `E` and `T1` arm projectors.

Therefore the current exact status is:

```text
finite-frame dual normalization + independent source/readout dual legs
  => lambda = 9/4
  => rho_E = 21/4
```

but

```text
current Route-2 tensor/readout grammar
  does not yet derive the independent source/readout dual legs.
```

The missing theorem is now narrower than "find an inverse square." It is:

> derive, from the named Route-2 tensor primitive/source/readout structure,
> that both the source leg and the readout leg are independently normalized as
> local Riesz duals for the relevant projected channel; or derive an equivalent
> nonseparable primitive with the same total reciprocal degree two.

## Stuck Fan-Out

The first-principles fan-out now has five exact frames:

| frame | reciprocal degree | result |
|---|---:|---|
| raw restricted carrier/readout | 0 | misses endpoint |
| source leg dual-normalized only | 1 | misses endpoint |
| readout leg dual-normalized only | 1 | misses endpoint |
| independent source and readout dual legs | 2 | closes conditionally |
| nonseparable primitive with total degree 2 | 2 | still open, not licensed here |

This block removes a conceptual ambiguity from the prior no-go stack. The
needed two reciprocal factors have a standard finite-frame origin, but current
Route-2 notes still lack the theorem identifying both factors inside the
physical source/readout chain.

## Net

The conditional bridge is exact:

```text
two independent Riesz-dual local source/readout factors
  -> q_X proportional to w_X^-2
  -> lambda = 9/4
  -> q_E = 15/8
  -> rho_E = 21/4
  -> center T/E = -8/9.
```

The current-surface result is not endpoint closure. It is a sharper positive
target and license audit:

```text
prove the two dual-normalized legs,
or the Route-2 endpoint remains an open readout-map datum.
```

## What Is / Is Not Claimed

- **Is:** finite-frame Riesz dual normalization supplies exactly one
  reciprocal projector-weight factor; two independent source/readout dual
  factors produce the endpoint algebra exactly; one factor misses.
- **Is:** current Route-2 notes do not yet license those two independent
  source/readout factors.
- **Is not:** does not derive `rho_E = 21/4`; does not close the endpoint
  triple; does not adopt a fitted value; does not claim a unique exact
  `Theta_R -> Lambda_R` theorem; does not update any audit status.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.py
```

Expected result:

```text
PASS=19 FAIL=0
```

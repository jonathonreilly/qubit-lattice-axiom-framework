# Quark Route-2 Two-Pole Density-Covariance Primitive Candidate

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** conditional support / primitive-target refinement
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional support / primitive-target refinement
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py`](../scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)


## Question

After the one-pole no-go, a positive channel-volume origin for the Route-2
endpoint must produce the exact inverse-square rule

```text
q_X proportional to w_X^-2.
```

This note packages a concrete same-domain primitive that would do so:

```text
D_X = A_X / w_X,
q_X proportional to D_X^2.
```

That is: first convert a channel amplitude to a channel density by dividing by
the channel volume/weight, then use a quadratic covariance readout of that
density.

## Exact Construction

The exact `O_h` channel weights are

```text
w_E = 1/3,
w_T = 1/2,
w_E/w_T = 2/3.
```

If a common channel amplitude `A_X` is first normalized to density

```text
D_X = A_X / w_X,
```

and the readout covariance is quadratic in that density,

```text
q_X proportional to D_X^2,
```

then

```text
q_X proportional to w_X^-2,
q_E/q_T = (w_E/w_T)^-2 = 9/4.
```

The endpoint arithmetic then gives

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

## Variant Firewall

The runner compares nearby pipelines:

| Pipeline | Exponent `p` | `lambda=q_E/q_T` | `rho_E` |
|---|---:|---:|---:|
| raw amplitude response | `0` | `1` | `-1` |
| single channel-density response | `-1` | `3/2` | `3/2` |
| raw channel-volume quadratic response | `2` | `4/9` | `-34/9` |
| channel-density covariance response | `-2` | `9/4` | `21/4` |

So neither raw polynomial response nor a merely linear density response is
enough. The exact positive pipeline is:

```text
one channel-volume division before a quadratic response.
```

Equivalently, in the simple normalize-then-power family

```text
q_X proportional to (w_X^-d)^m,
```

the target condition is

```text
d m = 2.
```

For a covariance route `m=2`, this requires exactly one channel-volume
division.

## Current-Surface Firewall

The current Route-2 surface does not supply this primitive.

- The exact readout map still names the E-channel ratio as the missing map
  entry.
- The `kappa^2` covariance note leaves the covariance bridge open and points
  to future nonlinear tensor/readout structure.
- The quadratic Schur note says no named current functional produces an
  inverse-square-of-projector-weight center lift.
- The current bilinear carrier note defines a polynomial object and does not
  assert a positive primitive theorem for `K_R`.

In typed-graph terms, the current surface has no path

```text
O_h channel weights -> channel-density normalization -> density covariance readout -> rho_E=21/4.
```

Adding exactly the channel-density covariance primitive creates that path.
This is conditional support, not a current-surface derivation.

## What This Moves

The missing same-domain primitive is now sharper than "derive
inverse-square." A positive derivation can try to prove:

```text
Route-2 readout forms a quadratic covariance of channel densities D_X=A_X/w_X.
```

The load-bearing missing pieces are exactly:

1. a channel-volume normalization of the relevant amplitude;
2. a quadratic covariance readout after that normalization.

## What Remains Open

Open routes:

- derive the channel-density normalization from support/readout structure;
- derive the density-covariance readout from the current tensor primitive;
- prove that current polynomial/bilinear surfaces cannot supply either step;
- develop the signed-cancellation escape identified by the one-pole no-go.

This note does not use observed quark masses, CKM/J targets, live endpoint
proximity, fitted selectors, or a newly adopted axiom.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py
```

Expected result:

```text
PASS=18 FAIL=0 TOTAL=18
```

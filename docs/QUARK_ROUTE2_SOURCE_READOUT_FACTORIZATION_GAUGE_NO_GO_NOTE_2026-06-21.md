# Route-2 Source/Readout Factorization Gauge No-Go

**Date:** 2026-06-21  
**Claim type:** no-go / exact factorization boundary  
**Actual current-surface status:** no-go  
**Trace class:** negative_route_pruning  
**Reachability to target:** prunes the route that tries to certify two
independent source/readout dual-normalized legs from the endpoint product
algebra or the current restricted readout map alone.  
**Primary runner:** [`scripts/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.py)  
**Runner cache:** `logs/runner-cache/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.txt`

## Boundary

This note does not derive `rho_E = 21/4`, does not close the Route-2 endpoint
triple, does not update an audit verdict, and does not claim a unique exact
`Theta_R -> Lambda_R` theorem.

It proves a narrow obstruction for the next positive route. Even if the target
total reciprocal degree is known to be two, the current endpoint/readout
surface only sees a product of any source and readout leg normalizations. It
does not identify the source leg and readout leg separately. Therefore the
current readout algebra cannot certify that the two factors are two independent
dual-normalized legs; it can only certify a total product if such a product is
derived elsewhere.

No observed masses, fitted targets, PDG values, nearest-rational selection, or
live endpoint fit is used.

## Current Product-Level Readout

The exact restricted readout-map surface writes the bright readout as

```text
gamma_E = alpha_E u_E + beta_E delta_A1 u_E
gamma_T = alpha_T u_T + beta_T delta_A1 u_T.
```

Equivalently, on the endpoint columns,

```text
q_X = gamma_X(center) / gamma_X(shell)
    = 1 + rho_X / 6.
```

After granting the two T-side candidates, the endpoint target can be phrased as

```text
q_T = 5/6,
lambda = q_E / q_T = 9/4,
q_E = 15/8,
rho_E = 21/4.
```

This is product-level information. It determines the channel response ratio
`lambda`, but it does not tell the current grammar whether that ratio came from
a source leg, a readout leg, or a product of both.

## Factorization Gauge

Suppose a future source/readout theorem factorizes a channel response as

```text
Q_X = S_X R_X
```

where `S_X` is a source-side scalar and `R_X` is a readout-side scalar. The
observable endpoint algebra only sees `Q_X`.

For any nonzero channel gauges `h_X`, the transformation

```text
S_X -> h_X S_X,
R_X -> h_X^-1 R_X
```

leaves every product `Q_X` unchanged. Therefore it leaves `q_E`, `q_T`,
`lambda = q_E/q_T`, and the current endpoint readout outputs unchanged. But it
changes the apparent source/readout attribution.

So a product theorem cannot certify a two-leg theorem unless it also fixes this
factorization gauge by deriving leg-level source and readout observables or a
canonical normalization rule for each leg.

## Degree Split No-Go

Let the local projector weights be

```text
w_E = 1/3,
w_T1 = 1/2,
kappa = w_T1 / w_E = 3/2.
```

If the source leg has reciprocal degree `a` and the readout leg has reciprocal
degree `b`, the endpoint product degree is

```text
d = a + b,
lambda = (w_T1 / w_E)^d.
```

The endpoint target fixes

```text
lambda = 9/4 = (3/2)^2,
```

so it fixes only

```text
a + b = 2.
```

The product data cannot distinguish any of the following exact splits:

| source degree `a` | readout degree `b` | total `d` | `lambda` |
|---:|---:|---:|---:|
| `0` | `2` | `2` | `9/4` |
| `1` | `1` | `2` | `9/4` |
| `2` | `0` | `2` | `9/4` |
| `-1` | `3` | `2` | `9/4` |
| `3` | `-1` | `2` | `9/4` |

Only the middle split is the desired "one source dual leg and one readout dual
leg" story. The endpoint product algebra itself does not select it.

## Current-Surface Check

The current Route-2 surfaces have exactly the product-level structure above:

- `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` reduces the readout to
  the channelwise matrix `P_R` and says the endpoint ratios are algebraic once
  that readout is reduced.
- `QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md` says selecting
  the target endpoint ratio is an extra source/readout rule and that no current
  typed edge supplies the required bridge.
- `S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md` and
  `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` define staging/carrier objects
  under named inputs; they do not define leg-level Riesz-dual source and
  readout observables.

Therefore the current surface cannot certify independent dual legs from the
readout product alone.

## Net

The following route is pruned:

```text
endpoint product algebra or P_R matrix alone
  -> two independent source/readout dual-normalized legs.
```

The correct remaining target is stricter:

```text
derive a leg-level factorization primitive that fixes source/readout gauges
and proves both legs are local Riesz duals,
```

or derive an equivalent nonseparable total-degree-2 primitive that does not
pretend to have independently certified source and readout legs.

## What Is / Is Not Claimed

- **Is:** the endpoint product fixes total reciprocal degree two, not a unique
  source/readout degree split.
- **Is:** channelwise factorization gauges leave all current readout products
  invariant while changing leg attribution.
- **Is:** current Route-2 notes do not provide leg-level Riesz-dual
  source/readout observables that fix this gauge.
- **Is not:** does not rule out a future source/readout factorization theorem;
  does not rule out a future nonseparable total-degree-2 primitive; does not
  derive or adopt `rho_E = 21/4`.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.py
```

Expected result:

```text
PASS=13 FAIL=0
```

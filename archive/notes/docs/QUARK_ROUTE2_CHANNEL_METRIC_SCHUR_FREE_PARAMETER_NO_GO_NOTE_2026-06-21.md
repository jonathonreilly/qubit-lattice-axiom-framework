# Route-2 Channel-Metric No-Go: `O_h`-Invariant Metrics on `E (+) T1` Have a Schur-Free Ratio, So the Endpoint Factor `lambda = 9/4` Remains an Extra Normalization Primitive

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** negative route boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the pure `O_h` channel-metric route to the Route-2 endpoint triple
**Primary runner:** [`scripts/frontier_quark_route2_channel_metric_schur_free_parameter_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_channel_metric_schur_free_parameter_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_channel_metric_schur_free_parameter_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_channel_metric_schur_free_parameter_no_go_2026_06_21.txt)

## Target

The exact Route-2 readout reduction compresses the endpoint target to

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

After granting the two `T`-side entries, the remaining datum is

```text
rho_E := beta_E / alpha_E = 21/4.
```

Equivalently,

```text
q_T = 5/6,
q_E = 15/8,
lambda := q_E / q_T = 9/4.
```

The previous same-domain covariance no-go derived the `O_h` shell leverage
`kappa = w_T / w_E = 3/2`, observed that `kappa^2 = 9/4`, and showed that
plain equivariance does not supply the bridge `lambda = kappa^2`. The
quadratic-invariant follow-on then sharpened the gap: the missing law is an
inverse-square projector-weight lift `q_X proportional to w_X^-2`, and no
named functional on `main` supplies it.

This note attacks the nearest remaining steelman:

> perhaps a positive `O_h`-invariant channel metric on the `E (+) T1`
> readout space canonically fixes the `E:T1` normalization ratio.

## Result

It does not. On the six-arm octahedral star, the `O_h` representation
decomposes as

```text
A1 (+) E (+) T1,
```

with per-arm projector weights

```text
w_A1 = 1/6,  w_E = 1/3,  w_T = 1/2.
```

The positive symmetric `O_h`-invariant metrics on the bright channel space
`E (+) T1` form the two-parameter cone

```text
G(c_E, c_T) = c_E P_E + c_T P_T1,    c_E, c_T > 0.
```

The ratio `c_E/c_T` is free. This is just Schur's lemma with the multiplicity
one `E` and `T1` irreducible blocks: there is no cross block, and each block
gets its own independent scalar. The runner verifies this directly in exact
rational arithmetic:

- the full arm-space invariant symmetric metric dimension is `3`
  (`A1`, `E`, `T1`);
- the restricted `E (+) T1` metric dimension is `2`;
- Reynolds projection of a generic symmetric form has zero `E:T1` cross block
  and scalar blocks on `E` and `T1`;
- the example ratios `1`, `3/2`, and `9/4` are all positive invariant channel
  metrics.

So an invariant channel metric is a family, not a selector.

## Endpoint Consequences

If one uses the channel-metric ratio as the proposed covariance bridge
`lambda = q_E/q_T`, then the granted `T`-side algebra gives

```text
q_E = lambda * (5/6),
rho_E = 6(q_E - 1),
c_TE = -2 * (5/6) / q_E.
```

The exact consequences are:

| channel normalization | `lambda` | `q_E` | `rho_E` | `c_TE` | status |
|---|---:|---:|---:|---:|---|
| ambient Euclidean metric | `1` | `5/6` | `-1` | `-2` | not the endpoint |
| one reciprocal projector/dimension power | `3/2` | `5/4` | `3/2` | `-4/3` | not the endpoint |
| inverse-square projector-weight law | `9/4` | `15/8` | `21/4` | `-8/9` | target, but inserted |

Thus the channel-metric route lands exactly on the same missing primitive
identified by the quadratic no-go: it needs the inverse-square law

```text
c_X proportional to w_X^-2.
```

Declaring a channel metric does not derive that law. It simply exposes the
free scalar ratio where the law would have to be supplied.

## No-Go Discipline Gate

- **N1 (alternative routes).** This note targets only the pure
  `O_h`-invariant channel-metric route. It is distinct from the earlier
  equivariance-only, carrier-linear, positivity, bulk-limit, cross-domain
  color, and quadratic-invariant routes.
- **N2 (wall independence).** The wall is independent: even after accepting a
  positive channel metric, Schur leaves `c_E/c_T` free. Closing the
  carrier-linear or quadratic-functional route does not fix this metric
  scalar.
- **N3 (hidden-wall scan).** The runner derives the projectors, ranks,
  weights, invariant metric dimensions, block-scalar form, and endpoint
  consequences in exact arithmetic. No observed mass, fitted endpoint, or
  live readout selector is used.
- **N4 (residual matching).** The residual is exactly the same Route-2
  `E`-center datum: `rho_E = beta_E/alpha_E`, equivalently
  `lambda = q_E/q_T`. This packet prunes one possible source for that datum.
- **N5 (rhetoric).** "No-go" means the pure invariant channel-metric route does
  not select `9/4`. It does not prove that every future nonlinear or
  nonseparable tensor primitive is impossible.
- **N6 (partial closure).** The useful positive content is the exact
  classification of the channel metric cone. It sharpens the import: any
  successful metric route must derive `c_E/c_T = (w_T/w_E)^2 = 9/4`, not merely
  name an invariant metric.
- **N7 (steelman).** A future primitive outside this scope could still work:
  for example a non-`O_h`-only normalization principle, a separately justified
  finite-frame dual construction, or a nonseparable source/readout tensor law.
- **N8 (cross-cycle echo).** This is consistent with the same-domain
  covariance and quadratic no-go packets: they locate the target as an
  inverse-square projector-weight law; this note shows a channel metric does
  not make that law automatic.

## What Is and Is Not Claimed

**Is claimed.** The exact `O_h` channel-metric classification on the six-arm
star leaves the `E:T1` metric scalar ratio free. Ambient and one-reciprocal
normalizations miss the endpoint. The inverse-square normalization hits the
endpoint only because it supplies the missing ratio.

**Is not claimed.** This note does not derive `rho_E=21/4`, does not adopt
`lambda=9/4` as an input, does not rule out future nonlinear/nonseparable
primitives, and does not change any repo-wide status surface.

## Load-Bearing Inputs

- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) -
  the restricted readout reduction and endpoint algebra.
- [[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md) -
  the same-domain `kappa=3/2` relocation and equivariance no-go.
- [[`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) -
  the quadratic-invariant no-go and inverse-square gap statement.
- [[`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) -
  the current definition-only carrier boundary; no physical primitive bridge
  is imported from it.

## Forbidden-Imports Check

No PDG value, observed quark mass, fitted target, nearest-rational selector, or
box-endpoint live fit is used. The target rationals `5/6`, `15/8`, `-2`,
`-8/9`, `9/4`, and `21/4` enter only as the exact comparison targets already
named by the Route-2 readout map and follow-on no-go packets.

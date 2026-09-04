# Route-2 Nonseparable Quadratic Primitive No-Go: `Sym^2(E (+) T1) -> E (+) T1` Has Three `O_h` Reduced Coefficients, So the Endpoint Factor Is Still Not Selected

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** negative route boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the pure `O_h` nonseparable quadratic primitive route to the Route-2 endpoint triple
**Primary runner:** [`scripts/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.txt)

## Target

The exact Route-2 readout map reduces the endpoint target to

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

With the two `T`-side entries granted, the remaining datum is

```text
rho_E := beta_E / alpha_E = 21/4,
```

equivalently

```text
q_T = 5/6,
q_E = 15/8,
lambda := q_E / q_T = 9/4.
```

The scalar quadratic route on current `main` already shows that an
`O_h`-invariant quadratic form has a free `E:T1` ratio. This note tests a
stronger nearby route:

> maybe the missing primitive is not a scalar quadratic form or separable
> source-side Gram contraction, but a genuinely nonseparable equivariant
> quadratic map
>
> ```text
> Q : Sym^2(E (+) T1) -> E (+) T1.
> ```

## Exact Representation Result

On the six-arm octahedral star, the bright channel representation is

```text
V := E (+) T1,
dim E = 2,
dim T1 = 3.
```

Character arithmetic gives the exact decomposition relevant to readout
channels:

```text
Sym^2(E)     contains A1 (+) E,
E tensor T1  contains one T1 channel,
Sym^2(T1)   contains A1 (+) E.
```

Therefore

```text
Sym^2(E (+) T1)
```

contains

```text
2*A1 (+) 2*E (+) 1*T1
```

plus non-readout `T2`-type pieces. Equivalently,

```text
dim Hom_Oh(Sym^2(E (+) T1), E (+) T1) = 3.
```

There are two independent `E`-output reduced coefficients and one independent
`T1`-output reduced coefficient.

## Consequence For the Endpoint

This is a real nonseparable route, because the mixed product

```text
E tensor T1 -> T1
```

exists. But it is not a selector. `O_h` supplies the channel inventory, not
the reduced matrix elements. Even if one fixes a `T1` output normalization,
two `E`-output coefficients remain free.

Under the granted `T`-side endpoint algebra,

```text
q_E = lambda * (5/6),
rho_E = 6(q_E - 1),
c_TE = -2 * (5/6) / q_E.
```

The same representation content allows comparison choices such as:

| `lambda` | `rho_E` | endpoint status |
|---:|---:|---|
| `1` | `-1` | not the target |
| `3/2` | `3/2` | not the target |
| `9/4` | `21/4` | target, but coefficient-selected |
| `7/3` | `17/3` | not the target |

So the nonseparable quadratic route sharpens the remaining gap rather than
closing it: a future positive result must derive a coefficient-selection or
normalization principle inside the three-dimensional reduced-coefficient
space. `O_h` symmetry alone cannot do it.

## No-Go Discipline Gate

- **N1 (alternative routes).** This note targets the pure `O_h` equivariant
  quadratic map route `Sym^2(E (+) T1) -> E (+) T1`. It is not the scalar
  invariant quadratic route and not a pure channel metric route.
- **N2 (wall independence).** The wall is the reduced-coefficient freedom:
  symmetry permits a three-dimensional map space. This remains even after the
  scalar quadratic and metric routes are pruned.
- **N3 (hidden-wall scan).** The runner derives the six-arm projectors,
  characters, symmetric-square/tensor-product multiplicities, readout Hom
  dimension, and endpoint consequences in exact arithmetic.
- **N4 (residual matching).** The residual is the same Route-2
  `E`-center datum `rho_E = beta_E/alpha_E`, equivalently
  `lambda = q_E/q_T`.
- **N5 (rhetoric).** The no-go says `O_h` representation content alone does
  not select the endpoint coefficient. It does not rule out an additional
  physical primitive that selects one point in the allowed map space.
- **N6 (partial closure).** The positive content is useful: a genuinely mixed
  nonseparable channel `E tensor T1 -> T1` exists. The closure failure is
  precise: its coefficient is independent of the two `E`-output coefficients.
- **N7 (steelman).** A future primitive could still work if it supplies a
  coefficient-selection law, a variational principle, or a typed source/readout
  boundary condition beyond pure `O_h` equivariance.
- **N8 (cross-cycle echo).** This matches the prior same-domain covariance and
  scalar quadratic no-gos: the structural number `9/4` is visible, but the
  bridge selecting it is not supplied by symmetry.

## What Is and Is Not Claimed

**Is claimed.** The exact `O_h` decomposition gives a three-dimensional
reduced-coefficient space for nonseparable quadratic maps from
`Sym^2(E (+) T1)` to `E (+) T1`. Therefore pure representation content does
not derive the endpoint value `rho_E = 21/4`.

**Is not claimed.** This note does not derive the endpoint triple, does not
adopt `lambda=9/4`, does not rule out future coefficient-selection primitives,
and does not change any repo-wide status surface.

## Load-Bearing Inputs

- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) -
  the restricted readout reduction and endpoint algebra.
- [[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md) -
  the same-domain `kappa=3/2` relocation and equivariance no-go.
- [[`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) -
  the scalar quadratic no-go and inverse-square gap statement.
- [[`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) -
  the definition-only carrier boundary; no physical primitive bridge is
  imported from it.

## Forbidden-Imports Check

No PDG value, observed quark mass, fitted endpoint, nearest-rational selector,
or live readout fit is used. The target rationals `5/6`, `15/8`, `-2`,
`-8/9`, `9/4`, and `21/4` enter only as comparison targets from the exact
Route-2 readout map and follow-on no-go packets.

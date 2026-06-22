# Quark Route-2 Observable-Hessian Readout Identification No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for scalar observable-Hessian to Route-2 readout identification
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_observable_hessian_readout_identification_no_go_2026_06_22.py`

Actual current-surface status: no-go for scalar observable-Hessian to Route-2
readout identification.

## Scope

Block76 reduced the connected selector theorem to a sharper conditional
source/readout primitive:

```text
Route-2 physical readout = D^2 log Z for the relevant source
```

plus a pure-disconnected typing of the singlet term.  This block asks whether
the existing S3 observable-Hessian surface already supplies that primitive.

It does not.  No endpoint value is used.

This is not an audit verdict.  It does not resolve the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Existing Observable-Hessian Surface

The existing authority
[`S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md`](S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md)
does contain the scalar generator:

```text
W[J] = log|det(D+J)| - log|det D|.
```

It also explicitly scopes the route as scalar-only.  Its Hessian is a scalar
source Hessian over scalar source projectors.  The note says this surface does
not generate the missing tensor/time-coupling law.

That scalar Hessian is useful support for scalar source-response lanes, but it
is not a color/channel-resolved Route-2 source.

## Route-2 Readout Surface

The Route-2 exact readout authority is a finite carrier/readout reduction:

```text
K_R -> P_R -> E/T shell and center readout.
```

It reduces the admissible map to:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

That surface does not type `P_R` as a source Hessian of `log Z`, nor does it
identify the singlet channel as a pure disconnected product for the same source.

## Rank And Domain Mismatch

A scalar source `j I` has one Hessian component:

```text
W(j) = sum_i log(d_i + j) - log(d_i)
W''(0) = -sum_i 1 / d_i^2.
```

The connected selector target needs at least:

```text
adjoint channel
singlet/disconnected channel
```

and the Route-2 readout surface itself has four endpoint slots:

```text
E-shell, E-center, T-shell, T-center.
```

Thus a scalar Hessian cannot by itself identify the `E/T` readout map or the
singlet-purity coefficient.

## Missing Primitive

The exact missing primitive is stronger than "use the observable Hessian":

```text
a color/tensor-resolved source functional whose connected Hessian is the
Route-2 physical readout
```

with:

```text
same-source identification
connected-Hessian physical readout
pure-disconnected singlet identification
```

Only after those are supplied can the Block76 cumulant theorem force
`kappa=0`.

## Result

The scalar observable-Hessian route is pruned for this selector:

```text
scalar logdet Hessian => Route-2 color/E-T connected readout
```

is not a current-surface theorem.

The next positive target is now precise:

```text
derive a color/tensor-resolved source functional,
prove it is the same source as Route-2 P_R,
prove the physical readout is D^2 log Z,
prove the 1/9 singlet term is pure disconnected.
```

Without that source/readout identification, the scalar observable-Hessian
surface remains support context, not a derivation of `kappa=0`.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_observable_hessian_readout_identification_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=47, FAIL=0
```

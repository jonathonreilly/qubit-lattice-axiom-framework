# Quark Route-2 Nonlinear E-Center Tensor Observable Gate

**Date:** 2026-06-21
**Claim type:** no_go
**Status:** exact branch-local negative boundary for same-scalar nonlinear
dressings of the current rank-1 Route-2 carrier. This note does not derive the
Route-2 endpoint triple and does not apply an audit verdict.
**Primary runner:**
[`scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py`](../scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py)
**Output:**
[`outputs/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.txt`](../outputs/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.txt)

## Scope

This block attacks the next positive escape route after the measured
calibration, bulk-limit, and quadratic-covariance no-gos:

> Can a genuinely nonlinear E-center tensor observable built from the current
> Route-2 carrier derive or sharply constrain `q_E=15/8`, `q_T=5/6`, and
> `q_E/q_T=9/4` without observed targets, fitted selectors, or an audit
> verdict?

The answer is a sharp boundary. Nonlinearity by itself is not enough. At the
bright-linear endpoint readout, a nonlinear observable has the normal form

```text
gamma_E = u_E H_E(delta_A1),
gamma_T = u_T H_T(delta_A1),
```

where `delta_A1(shell)=0` and `delta_A1(center)=1/6`.

Pure carrier invariants have zero bright-linear response at the A1 background.
A common scalar dressing has `H_E = H_T`, hence `q_E/q_T = 1`. The target
requires `q_E/q_T = 9/4`. Therefore a successful nonlinear observable must
include a channel-selecting law with `H_E` and `H_T` different between shell
and center.

That channel-selecting observable remains open. This block only closes the
same-scalar nonlinear escape.

Forbidden inputs in this block are observed quark masses, fitted Yukawa
entries, CKM/J targets, nearest-rational endpoint selection, selecting the
`N=15` measured box as a proof input, and any fitted endpoint selector.

## Current Carrier Facts

The exact Route-2 carrier/readout reduction uses

```text
K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).
```

The rank-1 factorization note rewrites this as

```text
K_R(q) = w(q) v(q)^T,
w(q) = (1, delta_A1(q))^T,
v(q) = (u_E(q), u_T(q))^T.
```

At the A1 background, `v=0`. Thus any pure invariant built only from
`||v||^2`, `det K_R`, singular values, or other even rank-1 carrier invariants
has zero first variation in the bright direction. Such an invariant can be a
scalar control, but it cannot itself be the bright-linear endpoint readout.

To produce the endpoint readout, the observable must carry a bright factor
`u_E` or `u_T`. The most general bright-linear endpoint form is therefore

```text
gamma_E = u_E H_E(delta_A1),
gamma_T = u_T H_T(delta_A1).
```

## Theorem

**Theorem (nonlinear E-center tensor observable gate).** On the current
rank-1 Route-2 carrier, any nonlinear observable whose bright-linear endpoint
readout is produced by a common scalar dressing

```text
H_E(delta_A1) = H_T(delta_A1) = H(delta_A1)
```

has

```text
q_E = H(1/6) / H(0) = q_T,
q_E/q_T = 1.
```

It therefore cannot derive the Route-2 target covariance

```text
q_E/q_T = (15/8) / (5/6) = 9/4.
```

In affine endpoint form,

```text
H_X(delta_A1) = a_X + b_X delta_A1,
rho_X := b_X/a_X,
q_X = 1 + rho_X/6.
```

The target values require

```text
rho_T = -1,
rho_E = 21/4.
```

So the nonlinear route can succeed only if it supplies an independent
E/T channel law. But that is exactly the missing readout selector exposed by
the exact readout-map and naturality no-gos. It is not obtained from the
rank-1 carrier or from nonlinearity alone.

## Fan-Out

| Route | Result |
|---|---|
| Pure rank-1 invariant | No bright-linear endpoint readout; first variation at `v=0` vanishes. |
| Same-scalar nonlinear dressing `H(delta_A1)` | Forces `q_E=q_T`, so `q_E/q_T=1`, not `9/4`. |
| Shared affine E-center slope | Forces one common `rho`; cannot equal both `-1` and `21/4`. |
| Independent affine channel slopes | Can fit the endpoint, but the slopes are exactly the missing readout entries. |
| Inverse-square projector-weight law | Would be a real channel selector; no current named functional supplies it. |

## What This Moves

This prunes the route:

```text
rank-1 K_R + generic nonlinear scalar dressing
  -> E-center tensor observable
  -> q_E/q_T = 9/4.
```

It sharpens the remaining positive route:

```text
derive a channel-selecting nonlinear observable
  -> H_E(1/6)/H_E(0) = 15/8
  -> H_T(1/6)/H_T(0) = 5/6
```

without fitting the endpoint values. In affine form, that is exactly the
readout law `(rho_E,rho_T)=(21/4,-1)`.

This note does not claim that all future nonlinear observables fail. It says
that a successful one must contain more than a scalar nonlinear dressing of
the rank-1 carrier: it must derive a non-common E/T channel law from a named
source/readout primitive.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=53, FAIL=0
VERDICT: rank-1-carrier nonlinear scalar dressings and pure carrier invariants cannot derive the Route-2 endpoint covariance q_E/q_T=9/4.
```

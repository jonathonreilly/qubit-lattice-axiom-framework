# Quark Route-2 Log-Barrier Record Primitive Gate Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go / conditional support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / conditional support boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_log_barrier_record_primitive_gate_2026_06_21.py`](../scripts/frontier_quark_route2_log_barrier_record_primitive_gate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_log_barrier_record_primitive_gate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_log_barrier_record_primitive_gate_2026_06_21.txt)
**Authority links:** [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md), [OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md), [OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md), [OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)

## Claim Boundary

The Route-2 endpoint target can be compressed to one missing second-dual
channel law. With the T-side candidates granted, the parent readout target is

```text
q_T = 5/6,
q_E = 15/8,
rho_E = beta_E / alpha_E = 21/4,
c_TE = -8/9.
```

Equivalently,

```text
lambda := q_E / q_T = 9/4.
```

On the seven-site `O_h` star the Route-2 channel weights are

```text
w_E = 1/3,
w_T1 = 1/2.
```

A pure log-barrier Hessian on those positive channel weights would give

```text
Phi_X(w_X) = -log w_X,
d^2 Phi_X / dw_X^2 = 1 / w_X^2,
lambda = (w_E^-2) / (w_T1^-2) = 9/4.
```

That conditional primitive is strong enough to close the arithmetic target.
This block asks whether it is already forced by the current Record/log-det
surfaces.

## Result

It is not forced by Record/log-det additivity alone.

The current Record axiom supplies finite scalar additivity after a readout
context and scalar surface are supplied. The observable-principle log-det
family closes only after a determinant-sector readout context or equivalent
quotient is supplied. Those surfaces do not by themselves identify the
Route-2 channel weights `w_E, w_T1` as determinant-sector coordinates, do not
select the scalar `Phi_X = -log w_X` on those weights, and do not say that the
Route-2 readout coefficient is the second derivative of that scalar with
respect to the `w` coordinate.

The runner verifies a concrete additive countermodel family:

```text
Phi_epsilon({w_X}) = sum_X [-log w_X + epsilon w_X^2].
```

The `epsilon w_X^2` term is additive over disjoint supplied channel records,
but it changes the channel-weight Hessian:

```text
d^2 Phi_epsilon / dw_X^2 = 1 / w_X^2 + 2 epsilon.
```

For `epsilon = 0`, the target ratio is recovered:

```text
lambda = 9/4.
```

For `epsilon = 1`, the same supplied-channel additivity gives

```text
lambda = (9 + 2) / (4 + 2) = 11/6,
```

and the endpoint is no longer `rho_E = 21/4`. Therefore additivity by itself
does not select the pure log barrier. A determinant-only quotient or another
readout-context rule must exclude the additive polynomial term.

## Coordinate Gate

Even after choosing `Phi_X = -log w_X`, the Hessian readout is
coordinate-dependent. In the `w` coordinate,

```text
d^2(-log w) / dw^2 = 1 / w^2.
```

In the logarithmic coordinate `u = log w`,

```text
Phi = -u,
d^2 Phi / du^2 = 0.
```

So the candidate also needs a coordinate/readout bridge saying that the
Route-2 coefficient is the Hessian with respect to the channel weight `w`
itself, and that this coefficient is the E-center readout lift.

## Exact Conditional Support

If three extra premises are supplied,

1. Route-2 channel weights are positive determinant-sector coordinates of a
   supplied readout context;
2. the determinant quotient excludes additive channel counterterms and selects
   the pure log-barrier scalar on those weights; and
3. the Route-2 readout coefficient is the `w`-coordinate Hessian and maps to
   the E-center lift;

then the endpoint arithmetic closes exactly:

```text
lambda = 9/4,
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

Those premises are not present in the checked current bank, so this block is
a no-go for deriving the log-barrier primitive from Record/log-det additivity
alone, plus a precise support map for what a future positive theorem would
need to supply.

## Relation To The S3/Route-2 Parent

The parent [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) remains open because the
readout-map endpoint triple is not derived. This block sharpens one live
positive route: a Route-2 log-barrier Hessian would be sufficient, but the
current Record and observable-principle surfaces do not force it.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_log_barrier_record_primitive_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=26, FAIL=0
```

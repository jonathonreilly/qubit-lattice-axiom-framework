# Quark Route-2 One-Pole Channel-Volume No-Go

**Date:** 2026-06-21
**Type:** no-go / negative route pruning
**Primary runner:** [`scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py)
**Runner output:** [`outputs/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.txt`](../outputs/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.txt)

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block prunes positive polynomial and one-pole channel-volume source/readout cones. It does not derive the endpoint triple and does not prove impossibility over all future nonlinear observables."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Question

The Route-2 endpoint target, after the T-side values are granted, is

```text
rho_E = 21/4,
q_E = 15/8,
q_E/q_T = 9/4,
c_TE = -8/9.
```

Prior covariance work located the same-domain target at the inverse-square
channel law

```text
q_X proportional to w_X^-2,
```

where the exact `O_h` channel weights are

```text
w_E = 1/3,
w_T = 1/2,
w_E/w_T = 2/3.
```

This block asks whether a broad but still natural current-surface class can
produce the needed law: positive channel-volume rules built from polynomial
monomials and at most one inverse channel-volume normalization.

## The Scoped Class

Let a channel lift be a positive cone

```text
q_X = sum_i a_i w_X^p_i,  a_i >= 0,
```

with every monomial exponent satisfying

```text
p_i >= -1.
```

This includes:

- polynomial channel-volume contractions, `p_i >= 0`;
- single-normalized or one-pole channel averages, `p_i >= -1`;
- positive sums of such terms.

It excludes:

- a genuine two-pole inverse-square channel metric, `p=-2`;
- signed cancellations;
- a different primitive that is not expressible as this positive
  channel-volume cone.

This is intentionally scoped. It is not a theorem about every possible future
nonlinear observable.

## Exact Bound

For one monomial,

```text
lambda(p) = q_E/q_T = (w_E/w_T)^p = (2/3)^p.
```

The endpoint target solves

```text
(2/3)^p = 9/4,
```

only at

```text
p = -2.
```

For every one-pole monomial `p >= -1`,

```text
lambda(p) <= (2/3)^-1 = 3/2 < 9/4.
```

For a positive cone, the ratio is a weighted average of the monomial ratios:

```text
q_E/q_T =
  sum_i a_i w_T^p_i (w_E/w_T)^p_i
  / sum_i a_i w_T^p_i.
```

Because all weights `a_i w_T^p_i` are nonnegative, the same upper bound holds:

```text
lambda <= 3/2.
```

Therefore every positive polynomial or one-pole channel-volume rule satisfies

```text
q_E <= (5/6)(3/2) = 5/4,
rho_E = 6(q_E - 1) <= 3/2,
```

which is far below the required `21/4`.

## Escapes Identified By The Runner

The runner verifies two exact escape mechanisms:

1. A true two-pole inverse-square monomial reaches the target:

```text
q_X proportional to w_X^-2
lambda = (2/3)^-2 = 9/4.
```

2. A signed cancellation can also synthesize the target, for example

```text
q_X proportional to 5 w_X^-1 - 6,
```

because

```text
E: 5(3) - 6 = 9,
T: 5(2) - 6 = 4,
lambda = 9/4.
```

That signed mechanism is outside the positive source/covariance cone and
would need its own derivation and positivity/firewall checks before it could
be used as a source primitive.

## What This Prunes

This block prunes the positive-cone family:

```text
positive polynomial channel-volume rules
positive one-pole channel-volume rules
positive sums of those rules
```

as origins for the exact Route-2 endpoint triple. In this class, the best
possible one-pole endpoint is

```text
lambda = 3/2,
rho_E = 3/2,
c_TE = -4/3.
```

So the remaining same-domain positive route is not "some nonlinear
functional." It must supply a true two-pole/double-dual inverse-square
channel metric or a different primitive.

## What Remains Open

Open routes:

- derive the two-pole inverse-square primitive from current support/readout
  structure;
- derive and police a signed-cancellation mechanism;
- find a non-channel-volume primitive that reaches the E-center lift without
  tuning;
- prove a larger no-go over a wider nonlinear class.

This note does not use observed quark masses, CKM/J targets, live endpoint
proximity, fitted selectors, or an adopted inverse-square axiom.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py
```

Expected result:

```text
PASS=19 FAIL=0 TOTAL=19
```

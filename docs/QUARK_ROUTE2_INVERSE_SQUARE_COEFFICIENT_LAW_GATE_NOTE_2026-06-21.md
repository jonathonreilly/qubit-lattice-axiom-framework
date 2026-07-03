# Quark Route-2 Inverse-Square Coefficient-Law Gate

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go / exact negative boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_inverse_square_coefficient_law_gate_2026_06_21.py`](../scripts/frontier_quark_route2_inverse_square_coefficient_law_gate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_inverse_square_coefficient_law_gate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_inverse_square_coefficient_law_gate_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

No audit verdict is applied. This note is a source note
for the independent review process.

## Safe Claim

The current Route-2 target

```text
lambda := q_E/q_T = 9/4
```

is exactly the second reciprocal power of the E/T projector-weight ratio:

```text
w_E = 1/3,
w_T = 1/2,
x := w_E/w_T = 2/3,
x^-2 = 9/4.
```

This block proves a narrow grammar gate:

- nonnegative polynomial coefficient laws in the projector weight cannot hit
  `9/4`;
- nonnegative one-pole reciprocal laws cannot hit `9/4`;
- a nonnegative grammar using powers `{0,-1,-2}` hits `9/4` exactly only when
  the lower-order `{0,-1}` terms vanish;
- signed-cancellation alternatives can be written down, but they import
  negative/background terms and specific A1 coefficients.

So the remaining positive target is a pure inverse-square coefficient law, or
an equivalent theorem explaining the signed-cancellation structure. This note
does not rule out future nonlinear or denominator-bearing observables.

## Parent Blocker

The parent s3-time row remains blocked by the readout-map endpoint triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

Under the T-side values, this is equivalent to

```text
q_T = 5/6,
q_E = 15/8,
lambda = q_E/q_T = 9/4,
rho_E = beta_E/alpha_E = 21/4,
c_TE = -8/9.
```

The covariance no-go already identified `q_X` proportional to `w_X^-2` as the
sharp missing bridge. This note asks how much of that bridge is forced by
simple coefficient grammars.

## One-Hop Sources

- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  gives the endpoint algebra and the missing `beta_E/alpha_E=21/4` map entry.
- [[QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  identifies the inverse-square projector-weight law as the exact gap.
- [[QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)
  keeps `rho_E` as the E-row readout direction.
- [[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  inherits the unresolved endpoint triple as the s3-time coupling blocker.

## Positive Polynomial Gate

For a nonnegative polynomial coefficient law

```text
c(w) = a_0 + a_1 w + a_2 w^2 + ...
```

with all `a_i >= 0`, the E/T ratio is a weighted average of

```text
x^0, x^1, x^2, ...
```

where `x=2/3`. Every term is at most `1`, so every nonnegative polynomial
ratio is at most `1`. It cannot reach the target `9/4`.

This covers the direct positive-weight and forward-quadratic grammars. In
particular, the pure forward quadratic gives

```text
x^2 = 4/9,
```

the wrong direction.

## One-Pole Reciprocal Gate

For a nonnegative one-pole reciprocal law

```text
c(w) = a_0 + a_1 / w,
```

with `a_0,a_1 >= 0`, the E/T ratio is a weighted average of

```text
x^0 = 1,
x^-1 = 3/2.
```

So it is at most `3/2`, still below `9/4`. A single reciprocal power gives
the known leverage `kappa=3/2`, not `kappa^2`.

## Two-Pole Reciprocal Gate

For the nonnegative grammar

```text
c(w) = a_0 + a_1 / w + a_2 / w^2,
```

the E/T ratio is a weighted average of

```text
1,
3/2,
9/4.
```

It can equal `9/4` only when all weight is on the second reciprocal term:

```text
a_0 = 0,
a_1 = 0,
a_2 > 0.
```

Thus the exact target is not a generic reciprocal-law consequence. It is the
pure inverse-square coefficient law.

## Signed-Cancellation Alternatives

If signs are allowed, lower-order laws can be fitted to the two endpoint
weights. That does not derive the target; it moves the import into a
signed-cancellation principle.

For a signed one-pole reciprocal law

```text
c(w) = a + b/w
```

with `c(w_T)=1` and `c(w_E)=9/4`, the unique solution is

```text
a = -3/2,
b = 5/4,
c(w_A1) = 6.
```

For a signed direct affine law

```text
c(w) = a + b w
```

with the same endpoint values, the unique solution is

```text
a = 19/4,
b = -15/2,
c(w_A1) = 7/2.
```

Both are possible algebraic fits. Neither is a derivation unless a future
theorem explains the negative/background term and the implied A1 coefficient.

## Result

This block prunes the route:

```text
simple positive coefficient law on projector weights
=> lambda = 9/4.
```

The implication fails for positive polynomial and one-pole reciprocal laws.
The exact target forces a pure inverse-square coefficient law inside the
tested nonnegative reciprocal grammar, or else a signed-cancellation theorem
with additional A1 data.

The remaining direct positive target is:

```text
derive c_X proportional to w_X^-2
```

from current same-surface Route-2 primitives, or supply an equivalent
denominator-bearing observable whose reduced coefficients are fixed before the
target is read off.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_coefficient_law_gate_2026_06_21.py
```

Current expected result:

```text
TOTAL: PASS=43, FAIL=0
```

# Formation-Rate Logarithmic Chain Rule At A Positive Reference Point

**Date:** 2026-07-08
**Type:** bounded_theorem
**Primary runner:**
[`scripts/formation_rate_law_class_reduction_2026_07_08.py`](../scripts/formation_rate_law_class_reduction_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/formation_rate_law_class_reduction_2026_07_08.txt`](../logs/runner-cache/formation_rate_law_class_reduction_2026_07_08.txt)

## Claim

Let a supplied local comparator have availability profile `A(r)` and
formation-rate law `F(A)`. Fix `r0` and write `A0 = A(r0)`. If

- `A` is differentiable at `r0`,
- `A0 > 0`,
- `F` is differentiable at `A0`, and
- `F(A0) > 0`,

then the normalized first-order response obeys the chain-rule identity

```text
(d/dr F(A(r)) / F(A(r)))|r0
  = [F'(A0) A0 / F(A0)] [A'(r0) / A0].
```

Thus, at that supplied positive reference point, the dependence on the
rate-law shape is summarized by the dimensionless logarithmic derivative

```text
g_F(A0) = F'(A0) A0 / F(A0).
```

This is a conditional calculus identity. It does not select `A`, `F`, a
formation process, a clock, or a gravitational coupling.

## Check

The runner evaluates the identity for three supplied smooth availability
profiles and five supplied rate-law examples. It compares the analytic
right-hand side with a five-point finite-difference derivative of the composed
function `F(A(r))`. It separately checks the closed-form values

```text
linear:      g_F = 1
square root: g_F = 1/2
quadratic:   g_F = 2
saturating:  g_F = 1/(1+A0)
exponential: g_F = A0/(exp(A0)-1).
```

These examples test the identity; they do not establish a physical rate-law
class or promote any example to framework content.

## Boundary

The framework says that records form while leaving the rate and formation rule
downstream. That context does not supply the differentiability or positivity
hypotheses above. No finite-contrast extrapolation, stochastic clock
measurement, frozen-pocket result, time metric, or gravity conclusion is
retained here.

## Dependency

- `MINIMAL_AXIOMS_2026-06-29.md` — context for the downstream formation-rate
  slot only; the displayed identity is ordinary calculus conditional on the
  hypotheses stated above.

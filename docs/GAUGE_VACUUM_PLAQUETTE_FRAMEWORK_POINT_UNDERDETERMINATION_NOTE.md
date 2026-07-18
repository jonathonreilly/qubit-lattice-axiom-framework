# Gauge-Vacuum Plaquette Finite-Jet Witness Separation

**Date:** 2026-04-16; finite-jet rescope 2026-07-18
**Type:** positive_theorem
**Status:** proposed_retained exact finite-jet witness-separation theorem on
the typed surface below
**Status authority:** source-note proposal only; audit verdict and effective
status remain owned by the independent audit lane
**Script:** `scripts/frontier_gauge_vacuum_plaquette_framework_point_underdetermination.py`

## Question

Can the exact order-`beta^5` onset coefficient, a compact positive interval,
and a strictly increasing local one-plaquette block support an explicit pair
of separated analytic witnesses at `beta = 6`?

## Answer

Yes. Two rational polynomials give a complete positive construction. They
agree coefficient-by-coefficient through degree five, have derivatives bounded
below by `1` throughout `[0,6]`, and differ at the right endpoint by the exact
positive rational `729/156250 = 0.0046656`. Strict increase of the local
one-plaquette block preserves that order under composition.

## Typed inputs and authority

| Input | Exact value or statement | Authority and role |
|---|---|---|
| onset coefficient | `a = 1/26244 > 0` | [Gauge-vacuum plaquette mixed-cumulant audit](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md), Corollary 2; the runner imports its exact `Fraction` calculation |
| evaluation interval | `beta in [0,6]` | the interval is stipulated here; its endpoint is the selected finite Wilson coordinate used in the [plaquette self-consistency finite diagnostic](PLAQUETTE_SELF_CONSISTENCY_NOTE.md), without importing the diagnostic's comparator value |
| separation coefficient | `c = 1/10^7 > 0` | an explicit rational construction choice in this theorem; it is not fitted data or a physical input |
| local composition block | `P_1plaq'(x) = Var_x(X) > 0` for the displayed positive arguments | [Gauge-vacuum plaquette reduction existence theorem](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md), Theorem 1; the variance proof is restated below and the Bessel helper evaluates only the local block |

These four rows are the complete input surface of this construction.

## Construction

Define

`f_-(beta) = beta + a beta^5`,

`f_+(beta) = beta + a beta^5 + c beta^6`.

Both are polynomials over the rationals, hence entire real functions.

## Theorem 1: exact common jet and endpoint separation

The coefficient lists through degree five are identical:

`[beta^k] f_- = [beta^k] f_+` for every `0 <= k <= 5`.

Their first differing coefficient is at degree six, where

`[beta^6](f_+ - f_-) = c = 1/10^7`.

At the right endpoint,

`f_-(6) = 170/27 = 6.296296296296...`,

`f_+(6) = 26582183/4218750 = 6.300961896296...`,

and therefore

`f_+(6) - f_-(6) = c 6^6 = 46656/10^7 = 729/156250 = 0.0046656`.

## Theorem 2: exact derivative certificate on `[0,6]`

The derivatives are

`f_-'(beta) = 1 + 5 a beta^4`,

`f_+'(beta) = 1 + 5 a beta^4 + 6 c beta^5`.

For every `beta in [0,6]`, all nonconstant terms on the right are
nonnegative. Thus the exact analytic lower bounds are

`f_-'(beta) >= 1` and `f_+'(beta) >= 1`.

Both derivatives are therefore strictly positive throughout the full
interval. For an endpoint cross-check,

`f_-'(6) = 101/81`,

`f_+'(6) = 15840299/12656250`.

The derivative certificate is coefficient-based and exact; sampled values
are not used to prove interval positivity.

## Theorem 3: strict order after local one-plaquette composition

For

`X(U) = (1/3) Re Tr U`

and the one-plaquette density proportional to `exp(x X)`, differentiation
gives

`P_1plaq'(x) = Var_x(X)`.

The density is strictly positive for finite real `x`, while `X` is not
constant on `SU(3)`: `X(I) = 1` and
`X(exp(2 pi i/3) I) = -1/2`. Hence the variance is strictly positive on the
relevant positive domain. Since

`0 < f_-(6) < f_+(6)`,

strict increase gives

`P_1plaq(f_-(6)) < P_1plaq(f_+(6))`.

The runner's independently formulated Bessel and Weyl evaluations give

`P_1plaq(f_-(6)) = 0.441402699435447...`,

`P_1plaq(f_+(6)) = 0.441694136647056...`.

These are local one-plaquette block values at the constructed arguments.

## Output surface and division of labor

The theorem output is the explicit ordered pair

`(f_-, f_+)`

on the finite order-`beta^5` jet plus interval-monotonicity surface, together
with the exact endpoint separation and the strictly ordered local-block
compositions above.

Connected-hierarchy compatibility, compact spectral-measure compatibility,
finite Wilson reduction-law realizability, and the physical full-surface
symbol `P(6)` belong to their own source packages. They are not inputs or
outputs of this finite polynomial construction, and the functions here are
not registered as realizations of those structures.

## Executable evidence

The runner checks seven theorem statements and two independent numerical
support statements. Five hostile mutations execute the same load-bearing
validators and are rejected:

1. moving the perturbation from degree six to degree five breaks the common
   jet;
2. setting `c = 0` removes endpoint separation;
3. changing the linear sign breaks the exact derivative lower bound;
4. swapping the two local plaquette values breaks strict output ordering;
5. deleting the positive composition factor breaks the exact input-order
   certificate.

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_framework_point_underdetermination.py
```

Expected summary:

- `THEOREM PASS=7 SUPPORT=2 CONTROL PASS=5 FAIL=0`

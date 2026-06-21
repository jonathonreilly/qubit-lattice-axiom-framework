# Route-2 Double-Local Projector Normalization: Exact Conditional Bridge to `rho_E = 21/4`, with Falsifiers for the Nearby Weaker Laws

**Date:** 2026-06-21
**Claim type:** conditional-support / exact support boundary
**Actual current-surface status:** conditional-support
**Trace class:** upstream_support
**Reachability to target:** supports the open Route-2 endpoint by isolating the exact nonseparable primitive that would close it; does not derive that primitive.
**Status authority:** branch-local physics-loop artifact only. This is not a retained-status claim, writes no audit verdict, retags no ledger row, and updates no repo-wide authority surface.
**Primary runner:** [`scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py`](../scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.txt)

## Problem

The Route-2 endpoint target reduces to

```text
q_T = 5/6,
q_E = 15/8,
lambda := q_E/q_T = 9/4,
rho_E = 6(q_E - 1) = 21/4.
```

The existing same-domain shell leverage result gives

```text
w_E = 1/3,
w_T1 = 1/2,
kappa = w_T1/w_E = 3/2,
kappa^2 = 9/4.
```

The existing covariance no-go stack shows that the value `9/4` is present, but the bridge `lambda = kappa^2` is not forced by `O_h` equivariance, the channel-blind carrier, positivity, the box-size limit, or a generic quadratic invariant.

## Stretch Attempt

This block asks what exact local projector-weight law would close the bridge if it were supplied as a named primitive.

For a monomial local-weight law

```text
q_X proportional to w_X^p,
```

the covariance is

```text
lambda = q_E/q_T = (w_E/w_T1)^p = (2/3)^p.
```

The runner checks the nearby candidate laws:

| candidate law | exponent `p` | `lambda` | endpoint result |
|---|---:|---:|---|
| channel-blind lift | `0` | `1` | misses |
| raw local projector weight | `1` | `2/3` | misses |
| raw quadratic projector weight | `2` | `4/9` | misses |
| single reciprocal local normalization | `-1` | `3/2` | misses |
| double reciprocal local normalization | `-2` | `9/4` | closes conditionally |

Thus the exact conditional bridge is:

```text
q_X proportional to w_X^-2.
```

Equivalently, the missing primitive is a double-local projector normalization: one reciprocal local projector weight is not enough; the target needs two reciprocal local-weight factors.

## Conditional Consequence

If a future proof derives that double-local projector normalization from named Route-2 source/tensor/readout structure, then the endpoint chain closes exactly:

```text
lambda = (w_E/w_T1)^-2 = 9/4,
q_E = lambda q_T = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
center T/E = -2 q_T/q_E = -8/9.
```

This is conditional support, not an actual current-surface derivation. The primitive is not derived here.

## Falsifiers

The runner records three sharp falsifiers:

1. all one-factor/raw local projector-weight variants miss `lambda=9/4`;
2. among monomial laws `q_X proportional to w_X^p` with `|p| <= 6`, the unique target exponent is `p=-2`;
3. nearby center-excess denominator slips (`5`, `7`, `12` instead of the exact `6`) do not close the endpoint chain.

## Net

The open target is no longer vague. A positive proof must derive the double-local reciprocal projector-weight law, or an equivalent nonseparable E/T center-shell covariance primitive. Any route that supplies only one local normalization factor, a raw projector weight, a raw quadratic weight, or a generic equivariant quadratic form cannot close the endpoint.

## Scope

This does not prove that the double-local normalization primitive is true. It also does not prove impossibility over arbitrary future nonlinear observables. It isolates the exact primitive that would close the current endpoint algebra and records which nearby local-weight laws fail.

## Forbidden-Imports Check

No observed masses, fitted targets, or PDG values are consumed. The calculation uses the exact six-arm `O_h` projector weights and exact endpoint algebra. The rationals `5/6`, `15/8`, `9/4`, `-8/9`, and `21/4` appear only as the already-named Route-2 endpoint targets.

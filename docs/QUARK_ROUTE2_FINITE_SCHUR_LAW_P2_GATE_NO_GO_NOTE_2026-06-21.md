# Quark Route-2 Finite Schur-Law P2 Gate No-Go

**Date:** 2026-06-21
**Actual current-surface status:** no-go for coefficient-free finite projector-polynomial p=2 gate
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_finite_schur_law_p2_gate_no_go_2026_06_21.py`

Actual current-surface status: no-go for coefficient-free finite projector-polynomial p=2 gate

## Scope

This note tests whether the new dual-compliance target can be obtained from an
ordinary finite projector-polynomial law on the six-arm Schur weights.
This is not an audit verdict and does not resolve the parent Route-2 endpoint gate.

The tested shortcut is:

```text
finite projector-polynomial source/readout law
```

with no extra coefficient selector and no inverse powers of the projector
weights.

## Exact Data

The same-domain Schur weights are

```text
w_E = 1/3
w_T = 1/2
```

The endpoint target, after the T-side conditional premises are granted, is

```text
q_E / q_T = 9/4.
```

Equivalently this gives

```text
q_E = 15/8
rho_E = beta_E / alpha_E = 21/4
gamma_T(center) / gamma_E(center) = -8/9.
```

## Monomial Gate

A coefficient-free finite projector monomial has

```text
q_X proportional to w_X^d,     d >= 0.
```

Then

```text
q_E / q_T = (w_E / w_T)^d = (2/3)^d.
```

No nonnegative degree gives `9/4`. The target ratio is instead

```text
(w_E / w_T)^-2 = (2/3)^-2 = 9/4.
```

So the endpoint needs an inverse-square law, not an ordinary positive-degree
projector-power law.

## Polynomial Gate

Allowing an arbitrary finite polynomial

```text
P(w) = a_0 + a_1 w + ... + a_d w^d
```

does not solve the problem by itself. The target condition is one linear
equation:

```text
P(1/3) = (9/4) P(1/2).
```

For degree `d >= 1`, this leaves `d` free coefficient directions. For example,

```text
P(w) = 19 - 30w
```

fits the ratio because

```text
P(1/3) = 9
P(1/2) = 4
P(1/3) / P(1/2) = 9/4.
```

That is a hidden coefficient selector, not a derivation from the finite Schur
polynomial class. Different coefficients give different exact endpoints.

## Consequence

The finite projector-polynomial shortcut is pruned:

```text
ordinary finite Schur projector powers or arbitrary finite polynomials
=> p = 2
```

is not a theorem. Positive work must instead derive inverse-square
dualization, or provide an equivalent source/readout coefficient theorem that
fixes the polynomial coefficients without using endpoint targets.

This does not rule out inverse-square dualization. It says only that ordinary
finite projector-polynomial data do not already derive it.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_finite_schur_law_p2_gate_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=26, FAIL=0
```

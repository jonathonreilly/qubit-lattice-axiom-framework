# Quark Route-2 Dual-Compliance Bridge Conditional Support Note

**Date:** 2026-06-21
**Claim type:** conditional_support
**Actual current-surface status: open / conditional-support.**
**Audit boundary:** This source note does not set, predict, estimate, or apply
any audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_dual_compliance_bridge_conditional_2026_06_21.py](../scripts/frontier_quark_route2_dual_compliance_bridge_conditional_2026_06_21.py)
**Runner output:** [outputs/frontier_quark_route2_dual_compliance_bridge_conditional_2026_06_21.txt](../outputs/frontier_quark_route2_dual_compliance_bridge_conditional_2026_06_21.txt)
**TRACE:** upstream_support

This is not an audit verdict. It is a physics-loop stretch attempt on the
same-domain E/T2 source/readout bridge behind the Route-2 endpoint triple.

## Scope

The parent target is still the restricted Route-2 readout triple:

```text
(rho_T, mu, rho_E) = (-1, -2, 21/4).
```

After the T-side candidates are granted, the exact remaining target is:

```text
rho_E = beta_E / alpha_E = 21/4
```

or equivalently:

```text
q_E = gamma_E(center)/gamma_E(shell) = 15/8,
c_TE = gamma_T(center)/gamma_E(center) = -8/9.
```

This block asks what exact same-domain readout primitive would force that
entry without importing color fractions, observed endpoint values, fitted
selectors, or comparator closeness.

The result is conditional on the dual-compliance premise.

## Conditional Premise

The prior covariance no-go sharpened the positive shape: the needed bridge is
not ordinary projector weight, not one-power dual weight, and not a generic
quadratic Oh-invariant form. It must behave like inverse-square channel
compliance:

```text
q_X proportional to w_X^-2,
```

where `w_X` is the channel's own per-arm projector weight on the six-arm
Oh support surface.

This note packages the exact consequence of that premise. The premise is not
derived or adopted by the current surface.

## Exact Derivation Under The Premise

On the six-arm Oh support representation:

```text
6 arms = A1 (1) + E (2) + T1 (3).
```

The per-arm projector weights are:

```text
w_A1 = 1/6,
w_E  = 2/6 = 1/3,
w_T  = 3/6 = 1/2.
```

Thus the same-domain leverage is:

```text
kappa = w_T / w_E = (1/2)/(1/3) = 3/2.
```

The dual-compliance premise uses inverse-square scaling:

```text
lambda_E/T := q_E / q_T = (w_E / w_T)^-2 = kappa^2 = 9/4.
```

Grant the T-side candidate:

```text
q_T = gamma_T(center)/gamma_T(shell) = 5/6.
```

Then:

```text
q_E = q_T * lambda_E/T = (5/6) * (9/4) = 15/8.
```

Since the Route-2 E-center lift is:

```text
q_E = 1 + rho_E / 6,
```

the E-channel readout entry is forced conditionally:

```text
rho_E = 6 * (15/8 - 1) = 21/4.
```

With the granted shell ratio `gamma_T(shell)/gamma_E(shell) = -2`, this also
gives:

```text
c_TE = -2 * (5/6) / (15/8) = -8/9.
```

## Falsifiers

The runner checks wrong-exponent alternatives:

| Exponent `p` in `q_X proportional to w_X^-p` | `q_E/q_T` |
|---:|---:|
| `0` | `1` |
| `1` | `3/2` |
| `2` | `9/4` |
| `-2` | `4/9` |

Only `p=2` produces the target ratio. Therefore this support result is not
a disguised consequence of ordinary dimension counting or of generic
quadratic invariance. It isolates a precise missing source/readout law:

```text
dual-compliance exponent p=2.
```

## Boundary

This block does not close the parent S3/Route-2 gate and does not derive the endpoint triple on the current surface. It supplies a conditional exact bridge:

```text
dual-compliance p=2 premise
=> q_E/q_T = 9/4
=> rho_E = 21/4
=> c_TE = -8/9.
```

The next proof obligation is not arithmetic. It is to derive, reject, or
replace the dual-compliance premise from the accepted same-domain Route-2
source/readout primitives.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_dual_compliance_bridge_conditional_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=51, FAIL=0
```

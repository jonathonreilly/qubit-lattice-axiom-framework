# Quark Route-2 Dual-Frame Compliance Conditional Support

**Date:** 2026-06-21
**Actual current-surface status:** conditional-support
**Trace class:** upstream_support
**Runner:** `scripts/frontier_quark_route2_dual_frame_compliance_conditional_2026_06_21.py`

Actual current-surface status: conditional-support

## Scope

This note tests a constructive same-domain route for the open Route-2
readout endpoint. The route is a precise new source/readout premise:

```text
two-sided canonical-dual Schur compliance
```

It says that source preparation and readout registration both use the
canonical dual of the same `O_h` projector-weight frame on the six-arm star.
Under that premise the channel lift scales as

```text
q_X proportional to w_X^-2.
```

This is not an audit verdict. The note does not close the parent
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` row and does not derive the T-side candidates.
It proves only the conditional consequence of the stated
same-domain premise.

## Exact Schur Data

On the six-arm `O_h` star the antipodal split gives

```text
A1 rank = 1,  w_A1 = 1/6
E  rank = 2,  w_E  = 1/3
T  rank = 3,  w_T  = 1/2
```

The same-domain leverage is therefore

```text
kappa = w_T / w_E = 3/2.
```

The existing quadratic-invariant no-go already shows that `kappa^2 = 9/4` is
not forced by generic `O_h` covariance. The present block asks a narrower
constructive question: what follows if both sides of the source/readout
interface are canonical-dual with respect to the Schur weights?

## Conditional Theorem

Assume the two-sided canonical-dual Schur compliance law:

```text
q_X = C / w_X^2
```

for the `E` and `T` channel lifts on the same six-arm Schur frame. Then

```text
q_E / q_T = (w_E / w_T)^-2 = (2/3)^-2 = 9/4.
```

With the existing conditional T-side normalization

```text
q_T = 5/6
gamma_T(shell) / gamma_E(shell) = -2
```

this gives

```text
q_E = 15/8
rho_E = beta_E / alpha_E = 6(q_E - 1) = 21/4
gamma_T(center) / gamma_E(center) = -2 * (5/6) / (15/8) = -8/9.
```

So the conditional law supplies exactly the missing `E`-center lift. The
endpoint triple follows only on the conditional surface that already grants
the T-side candidates and adopts the new two-sided dual-compliance premise.

## Controls

The runner checks the neighboring exponents:

```text
p = 0   channel-neutral law      -> rho_E = -1
p = 1   one-sided dual law       -> rho_E = 3/2
p = 2   two-sided dual law       -> rho_E = 21/4
p = -2  projector-square law     -> rho_E = -34/9
```

Thus the result is not produced by ordinary channel neutrality, one-sided
duality, or a projector-square construction. The exponent `p=2` is the exact
signature of dualizing both source preparation and readout registration.

## What This Moves

This block gives a sharp positive target for the next proof:

```text
derive two-sided canonical-dual Schur compliance from current source/readout
primitives, or prove that the current primitives cannot supply it.
```

It does not claim that the premise is already on `main`. The actual current
surface remains open because the new source/readout premise is not yet
derived from retained framework primitives.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_dual_frame_compliance_conditional_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=22, FAIL=0
```

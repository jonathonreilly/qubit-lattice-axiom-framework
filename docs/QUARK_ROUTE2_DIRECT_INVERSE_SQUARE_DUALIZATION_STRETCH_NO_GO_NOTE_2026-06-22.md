# Quark Route-2 Direct Inverse-Square Dualization Stretch No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for the minimal direct dualization derivation
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_direct_inverse_square_dualization_stretch_no_go_2026_06_22.py`

Actual current-surface status: no-go for the minimal direct dualization derivation.

## Scope

This block attacks the open Route-2 readout endpoint from first principles.
The target is the same-domain inverse-square law

```text
q_X proportional to w_X^-2
```

on the six-arm `O_h` Schur frame. The prior conditional block showed that this
law would give the missing endpoint exactly. This note asks whether the law is
forced by a minimal source/readout premise set rather than by adding the
two-sided dual-compliance premise.

This is not an audit verdict. It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row. In short, it does not derive the endpoint triple on the actual current surface.

## Minimal Premise Set

The stretch attempt uses:

```text
A_min = {
  six-arm O_h Schur weights w_E = 1/3, w_T = 1/2,
  same-domain factorized source/readout law,
  source/readout exchange symmetry,
  channel-label covariance,
  normalization at q_T = 5/6,
  dual involution consistency
}
```

Forbidden proof inputs:

```text
rho_E = 21/4 as an input,
q_E = 15/8 as an input,
q_E/q_T = 9/4 as a selector,
gamma_T(center)/gamma_E(center) = -8/9 as a selector,
fitted polynomial coefficients,
measured finite-box calibration values
```

## Exact Obstruction

Write the most direct factorized same-domain law as

```text
source factor      S_X proportional to w_X^-a
readout factor     R_X proportional to w_X^-b
channel lift       q_X proportional to S_X R_X
```

Then the only exponent seen by the endpoint is

```text
p = a + b.
```

Channel-label covariance and log-additivity allow this power-law family but do
not fix `p`. Normalization at `q_T = 5/6` fixes the overall constant for any
chosen `p`, not the exponent.

Source/readout exchange symmetry gives only

```text
a = b.
```

It still leaves `a` free:

```text
a = b = 0       -> p = 0
a = b = 1/2     -> p = 1
a = b = 1       -> p = 2
```

Only the last line is the needed inverse-square law. The equality
`a = b = 1` is exactly the two-sided canonical-dual source/readout premise; it
is not derived by exchange symmetry alone.

## Controls

With `w_E/w_T = 2/3` and `q_T = 5/6`, the exponent controls are:

```text
p = 0   -> rho_E = -1
p = 1   -> rho_E = 3/2
p = 2   -> rho_E = 21/4
p = -2  -> rho_E = -34/9
```

One-sided canonical duality gives `p = 1`, so it misses. Ordinary
projector-square scaling has the wrong direction. The correct target is the
two-sided dual law, not generic dual language.

## Stuck Fan-Out Synthesis

The attempt tried four orthogonal frames.

| Frame | Result |
|---|---|
| Minimal algebraic factorization | Leaves only the total exponent `p = a + b`; no selector. |
| Exchange/self-adjointness | Forces `a = b` only; `a` remains free. |
| Dual-involution consistency | Makes reciprocal controls exact but does not choose an exponent. |
| Endpoint target inversion | Solves `p = 2`, but only by using the target ratio as a selector. |

Thus the direct derivation stalls at one exact missing premise:

```text
source side has unit canonical-dual charge
and
readout side has unit canonical-dual charge
```

or an equivalent theorem fixing total dual exponent `p = 2` without importing
the endpoint.

## Consequence

The pruned route is:

```text
A_min above => inverse-square dualization p=2.
```

The remaining positive target is sharper:

```text
derive the two unit dual charges from a physical source/readout theorem,
or replace them with another same-domain theorem that fixes p=2 without using
the endpoint target.
```

This result does not rule out future nonlinear source laws, two-sided
canonical-dual compliance, or a direct physical E-center readout theorem. It
only shows that the minimal symmetry and normalization package does not force
the inverse-square law.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_direct_inverse_square_dualization_stretch_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=58, FAIL=0
```

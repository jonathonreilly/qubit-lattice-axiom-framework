# Depth Laurent Roots: the Scalar Root-Moduli Closed Form Is REFUTED; the Depth Tail Follows the Full Principal-Branch Phase Law and the Root-Set Ordering (Bounded Refutation)

**Date:** 2026-06-12
**Type:** bounded refutation note
**Claim type:** bounded_theorem
**Runner:** `scripts/frontier_depth_laurent_root_closed_form_2026_06_12.py`

## Claim

For the realized zB `L=3` states, the scalar root-moduli closed form
`T_ge3 = (1/3) sum_j rho_j^3/(1-rho_j^3)` is **REFUTED** (with large
residuals and the wrong ordering; it ignores phase cancellations and branch
wrapping). What the root configuration DOES determine is the depth tail via the
full measured
principal-branch Laurent determinant phase law, and the depth ORDERING:

```text
F_s(q) = det B_s(theta), q = exp(i theta)
g_s(theta) = Arg(F_s(exp(i(theta+delta))) / F_s(exp(i theta))) - mean
delta = 3*tau = 1.05
T_ge3 = sum_{k>=3} w_k
```

The runner mirrors zB's raw determinant site-`0/1` machinery, reconstructs the
degree-3 Laurent determinant on held-out samples, factors the six numerator
roots, and verifies that the per-root principal-branch phase sum reproduces the
measured ladder weights.

## Measured Anchors

The measured `T_ge3` values are recomputed from the determinant-polar phase
increments, then compared to the landed full-precision zB values:

| state | measured `T_ge3` |
| --- | ---: |
| `K3` | `0.3664213175435252` |
| `K4` | `0.8162088439982206` |
| `K5` | `0.22542121070372184` |
| `K6` | `0.010321210053125331` |

Ascending measured order is:

```text
K6 < K5 < K3 < K4
```

## Root-Power Residual

The scalar unwrapped root-power expression

```text
T_ge3_closed = (1/3) sum_j rho_j^3 / (1 - rho_j^3)
rho_j = min(|r_j|, 1/|r_j|)
```

is not promoted as an equality. It is evaluated and compared honestly against
the measured `T_ge3`:

| state | measured `T_ge3` | root-power closed | residual |
| --- | ---: | ---: | ---: |
| `K3` | `0.3664213175435252` | `14.11207062535964` | `13.745649307816116` |
| `K4` | `0.8162088439982206` | `1.6041354413852444` | `0.7879265973870239` |
| `K5` | `0.22542121070372184` | `12.401070795856908` | `12.175649585153186` |
| `K6` | `0.010321210053125331` | `0.780889473926965` | `0.7705682638738396` |

The root-power ordering is `K6 < K4 < K5 < K3`, so the unwrapped positive
root-power scalar is branch-incomplete. The retained ordering statement is the
measured principal-branch determinant law, not this scalar approximation.

## Dominant Root

The determinant-root datum

```text
rho_* = max( |r| for |r|<1, 1/|r| for |r|>1 )
```

sets the asymptotic root-power envelope. The runner gates
`W_{3(m+1)}/W_{3m} -> rho_*^3` at `m=512`, where
`W_{3m}=(1/3) sum_j rho_j^(3m)`. It also reports the subdominant root-power
tail fraction as measured from the determinant roots, not as a designed split.

## Scope

This is an exact finite `L=3` realized-state result. It does not assert an
all-`L` theorem, rule out every possible scalar built from the roots, or treat
the tested unwrapped root-power scalar as a closed formula for the measured
principal-branch depth tail. The audit lane grades.

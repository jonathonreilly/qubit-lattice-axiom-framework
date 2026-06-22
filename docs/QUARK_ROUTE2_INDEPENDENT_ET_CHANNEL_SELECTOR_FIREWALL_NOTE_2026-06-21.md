# Quark Route-2 Independent E/T Channel Selector Firewall

**Date:** 2026-06-21
**Claim type: no_go**
**Status:** exact negative boundary for selector-existence and standard
coefficient-law routes; not a global no-go over future nonlinear observables.
**Primary runner:** [`scripts/frontier_quark_route2_independent_et_channel_selector_firewall_2026_06_21.py`](../scripts/frontier_quark_route2_independent_et_channel_selector_firewall_2026_06_21.py)

No audit verdict is applied. This note is a branch-local physics-loop artifact
for the independent review process.

## Safe Claim

The current six-arm `O_h` surface already has exact central projectors that
distinguish the `E` and `T1` channels. That is not the missing Route-2 theorem.
After the T-side normalization is fixed, an invariant channel selector still
has a free `E:T1` reduced coefficient ratio.

The target

```text
lambda := q_E / q_T = 9/4
```

is one allowed invariant selector value in that family. It is not derived by
projector existence alone. The missing positive theorem is a coefficient-law
selector for the `E:T1` ratio.

Equivalently:

```text
projector existence is not coefficient selection.
```

## Parent Blocker

The parent s3-time row remains blocked by the unresolved readout-map endpoint
triple:

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

Under the granted T-side endpoint values, the remaining E-side datum can be
written as any of these equivalent targets:

```text
rho_E := beta_E / alpha_E = 21/4
q_E := 1 + rho_E/6 = 15/8
c_TE := gamma_T(center)/gamma_E(center) = -8/9
lambda := q_E/q_T = 9/4.
```

This note attacks the proposed independent `E/T` channel-observable route to
`lambda = 9/4`.

## One-Hop Sources

- [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  names the inherited readout-map endpoint triple as the open theorem target.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  gives the restricted channelwise readout form and exact endpoint algebra.
- [`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  shows that the quadratic invariant route leaves the `E:T1` ratio free.
- [`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)
  proves that repairs blind to the E-center column cannot select `rho_E`.
- [`QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)
  identifies `rho_E` as the E-row projective direction, with positivity only
  giving the one-sided family.
- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md)
  supplies the rank-1 carrier factorization context.

## Exact Projector Fact

The six-arm `O_h` permutation representation decomposes as

```text
A1 + E + T1
```

with central projectors `P_A1`, `P_E`, and `P_T1` of ranks `(1,2,3)`. The
runner verifies:

- each projector is symmetric and idempotent;
- the three projectors are mutually orthogonal and sum to identity;
- `P_E` and `P_T1` commute with every signed-permutation action;
- `P_E P_T1 = 0`.

So an independent `E/T` channel observable exists in the weak sense:

```text
O(c_A,c_E,c_T) = c_A P_A1 + c_E P_E + c_T P_T1.
```

But this is exactly the Schur freedom. It distinguishes channels while leaving
the reduced coefficients free.

## Coefficient-Family Firewall

Normalize the T channel coefficient to `c_T=1`. Then

```text
O_lambda = P_A1 + lambda P_E + P_T1
```

is an `O_h`-invariant channel selector for every positive rational `lambda`.
The runner checks four inequivalent examples:

| Name | `lambda` | Endpoint consequence |
|---|---:|---|
| neutral | `1` | `q_E=q_T` |
| one inverse power | `3/2` | `lambda=kappa` |
| target | `9/4` | `rho_E=21/4`, `c_TE=-8/9` |
| forward quadratic weight | `4/9` | wrong channel magnitude |

All four are equally invariant after T normalization. Therefore the target
observable can be written down, but writing it down is not a derivation of the
coefficient ratio.

## Exponent-Law Diagnostic

The per-arm projector weights are

```text
w_A1 = 1/6
w_E  = 1/3
w_T1 = 1/2
kappa = w_T1 / w_E = 3/2.
```

For the coefficient law

```text
c_X proportional to w_X^p,
```

the E/T coefficient ratio is `(w_E/w_T1)^p`. The runner checks:

| `p` | `lambda` |
|---:|---:|
| `-2` | `9/4` |
| `-1` | `3/2` |
| `0` | `1` |
| `1` | `2/3` |
| `2` | `4/9` |

Inside this tested integer-power grammar, only the inverse-square coefficient
law hits the target. That is the theorem target, not an existing derivation:
the current bank does not supply a named same-surface law requiring
`c_X proportional to w_X^-2`.

## Affine-Law Import

If one tries to use a first-degree channel-weight law

```text
c(w) = a + b w
```

and fits it through

```text
c(w_T1)=1,
c(w_E)=9/4,
```

the unique law is

```text
a = 19/4,
b = -15/2.
```

It then predicts

```text
c(w_A1) = 7/2.
```

So the affine route does not remove the selector premise. It replaces the
target ratio with a non-neutral decreasing slope and an additional implied
A1 coefficient `7/2`. A future positive theorem would have to derive that
whole affine law, not merely observe that the interpolation exists.

## Result

This block prunes a tempting route:

```text
same-domain E/T channel observable exists
=> lambda = 9/4
=> rho_E = 21/4.
```

The implication fails. Same-domain channel projectors exist, but their
coefficient ratio is free. To move the parent readout endpoint triple, a
future route must supply at least one of:

1. an inverse-square coefficient law for channel weights;
2. a derived affine law with the implied A1 coefficient `7/2`;
3. a non-quadratic tensor observable whose reduced coefficients are fixed
   before the target is read off;
4. an independent E-center lift/source-readout primitive.

This note does not prove impossibility over future nonlinear observables. It
sharpens the blocker to the coefficient-law selector.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_independent_et_channel_selector_firewall_2026_06_21.py
```

Current expected result:

```text
TOTAL: PASS=47, FAIL=0
```

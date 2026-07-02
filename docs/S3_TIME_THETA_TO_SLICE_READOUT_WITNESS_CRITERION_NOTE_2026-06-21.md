# s3-Time Theta-to-Slice Readout Witness Criterion

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** bounded support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** bounded support / direct-consumer narrowing.
This note does not derive the Route-2 endpoint triple and does not close the
parent `s3_time_theta_to_slice_coupling_note` open gate.
**Primary runner:** [`scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py`](../scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.txt`](../logs/runner-cache/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.txt)

## Scope

The parent row
[[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
has an exact conditional family

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t),
V_R(t) = exp(-t Lambda_R) u_*,
```

but no unique theorem because the Route-2 readout endpoint triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4)
```

is not derived. Existing notes already rule out the direct shortcuts: raw
`F_adj = 8/9`, E-center-blind constraints, endpoint-fitted eta-floor
membership, and quadratic `O_h` covariance do not supply the missing
`rho_E := beta_E/alpha_E`.

This note is a direct-consumer packet for the s3-time parent row. It proves
the exact witness criterion a future downstream primitive must satisfy to
select `rho_E`. The result is deliberately narrower than a derivation:
it isolates the only direction the s3-time family can test.

## Setup

After granting the current T-side candidates used throughout the Route-2
readout notes,

```text
beta_T/alpha_T = -1,
alpha_T/alpha_E = -2,
```

the normalized admissible family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

The endpoint carrier columns are

```text
E-shell  = (1, 0, 0,   0),
E-center = (1, 0, 1/6, 0),
T-shell  = (0, 1, 0,   0),
T-center = (0, 1, 0, 1/6).
```

For every time `t`, write

```text
V_t = V_R(t).
```

The only coordinate where changing `rho_E` enters is the third carrier
coordinate, the E-channel center-excess coordinate.

## Theorem: Readout Witness Criterion

For any two values `rho` and `rho'`, any restricted carrier column `c`, and
any rank-one spacetime dual functional

```text
Phi_{a,b}(X) = a^T X b
```

with `a` a two-channel row dual and `b` a slice-vector dual, the conditional
s3-time family satisfies

```text
Phi_{a,b}(Xi_{rho'}(t ; c) - Xi_rho(t ; c))
  = (rho' - rho) c_3 a_E <V_t, b>,
```

where `c_3` is the E-center-excess carrier coordinate and `a_E` is the E-row
component of the channel dual.

Consequently, a rank-one downstream linear witness can distinguish two values
of `rho_E` on this family only if all three witness factors are nonzero:

```text
c_3 != 0,
a_E != 0,
<V_t, b> != 0.
```

If any factor vanishes, the primitive is blind to `rho_E` on the restricted
Route-2 family.

For a general linear downstream witness, decompose the dual into rank-one
terms. The same statement applies termwise: the witness can distinguish
`rho_E` only through its total contraction with the ambiguity vector
`(1, 0)^T tensor V_R(t)` on the `E-center - E-shell` carrier direction.
This note does not claim an impossibility theorem for arbitrary nonlinear
future primitives.

## Proof

For any carrier column `c`,

```text
P(rho') c - P(rho)c = ((rho' - rho) c_3, 0)^T.
```

Therefore

```text
Xi_{rho'}(t ; c) - Xi_rho(t ; c)
  = (P(rho')c - P(rho)c) tensor V_t
  = ((rho' - rho)c_3, 0)^T tensor V_t.
```

Applying `Phi_{a,b}` gives the stated scalar product.

## Consequences For The Parent Gate

1. Shell-only tests cannot select `rho_E`. For `E-shell`, `T-shell`, and
   `T-center`, the E-center-excess coordinate `c_3` is zero, so every
   rank-one spacetime dual sees the same value for all `rho_E`.

2. T-row tests cannot select `rho_E`. Once the T-side candidates are granted,
   changing `rho_E` changes only the E row. Any channel dual with `a_E = 0`
   is blind to the remaining open entry.

3. Time-only tests cannot select `rho_E`. Norm attenuation ratios and
   semigroup transport identities consume only the shared `V_R(t)` factor.
   They can verify the conditional family and the factor-rigidity theorem,
   but they cannot set the spatial E-center coefficient.

4. An E-center witness would be sufficient if supplied by a source theorem.
   Taking `c = E-center`, `a = (1, 0)`, and a normalized slice dual `b` with
   `<V_t, b> = 1`, the witness reads

   ```text
   Phi(Xi_rho(t ; E-center)) = 1 + rho/6.
   ```

   Thus the target value is exactly

   ```text
   Phi(Xi_{21/4}(t ; E-center)) = 15/8.
   ```

   This is not a derivation of `15/8`; it is the exact form a future
   E-center-evaluating source primitive must justify.

## Relation To `c_TE = -8/9`

The witness value is equivalent to the usual Route-2 endpoint target. With

```text
q_T = 5/6,
s_TE = -2,
q_E = 1 + rho_E/6,
```

the center ratio is

```text
c_TE = s_TE q_T / q_E.
```

Therefore

```text
rho_E = 21/4
<=> q_E = 15/8
<=> c_TE = -8/9.
```

This note does not identify `c_TE` with `-F_adj` or `-R_conn`. It says any
valid route to that identification must pass through a non-blind E-center
witness in the exact s3-time family.

## What This Adds

The factor-rigidity note showed that readout ambiguity is localized in a
rank-one spatial prefactor. This note gives the dual criterion for downstream
consumers: a proposed primitive must have nonzero overlap with the exact
ambiguity vector

```text
(1, 0)^T tensor V_R(t)
```

on the `E-center - E-shell` carrier direction. This sharpens the fallback
target for the parent open gate. Future work should not spend cycles on
shell-only, T-row-only, or time-ratio-only consumers as candidate derivations
of `21/4`; those routes are exactly blind on the current family.

## What Is Not Claimed

- This note does not derive `rho_E = 21/4`.
- This note does not derive `beta_T/alpha_T = -1` or `alpha_T/alpha_E = -2`.
- This note does not close the parent `s3_time_theta_to_slice_coupling_note`.
- This note does not prove no future nonlinear or source-domain primitive can
  supply the required E-center witness.
- This note does not update repo-wide authority surfaces.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py
```

Expected summary:

```text
TOTAL: PASS=16, FAIL=0
```

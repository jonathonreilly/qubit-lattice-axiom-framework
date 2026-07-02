# Quark Route-2 W1 Sign-Magnitude Split Support

**Date:** 2026-06-21
**Status:** exact support for splitting W1 into an already forced sign branch
and an open magnitude selector
**Primary runner:** `scripts/frontier_quark_route2_w1_sign_magnitude_split_support_2026_06_21.py`

## Purpose

The W1 bridge target is:

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
```

Equivalently, after the T-side stretch values,

```text
c_TE := gamma_T(center)/gamma_E(center) = -8/9.
```

This block asks which part of that statement is still load-bearing. The
answer is narrower than W1 as previously stated: in the positive E-center
branch, the sign is already fixed by the T-side orientation. The missing
content is the magnitude selector

```text
|c_TE| = 8/9.
```

## Exact Split

With the T-side candidates granted,

```text
q_T = 5/6,
s_TE = gamma_T(shell)/gamma_E(shell) = -2,
c_TE = s_TE q_T / q_E = (-5/3)/q_E.
```

Therefore:

- if `q_E > 0`, then `c_TE < 0`;
- if `q_E < 0`, then `c_TE > 0`;
- if `q_E = 0`, the center ratio is undefined.

The W1 target lives in the positive E-center branch because its target lift is

```text
q_E = 15/8 > 0.
```

On that branch, the minus sign in `c_TE=-8/9` is not a new source-domain
bridge. It follows from the already granted T-side sign:

```text
s_TE q_T = -5/3 < 0.
```

The remaining condition is magnitude:

```text
|c_TE| = 8/9
  <=> (5/3)/q_E = 8/9
  <=> q_E = 15/8
  <=> rho_E = 6(q_E - 1) = 21/4.
```

## Consequence

This block refines the W1 blocker:

```text
derive c_TE = -F_adj
```

should be attacked as:

```text
derive |c_TE| = F_adj
```

inside the positive E-center branch. The sign is support already available
from the T-side orientation; the magnitude is exactly the same open E-center
lift.

## Boundary

This is not a proof of W1 and not a selected `P_R`. It does not prove
`q_E=15/8`, `rho_E=21/4`, a physical `R_conn` selector, or a new source-domain
bridge. It only narrows the bridge by showing that the sign is not the
load-bearing missing primitive once the positive E-center branch is fixed.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_w1_sign_magnitude_split_support_2026_06_21.py
```

Expected:

```text
TOTAL: PASS=39, FAIL=0
Status: exact support for W1 sign/magnitude split; W1 magnitude remains open.
```

# Quark Route-2 Source-Domain Sign Support And Typecast Remainder

**Date:** 2026-06-21
**Status:** exact support / source-domain split narrowing
**Runner:** `scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py`
**Primary parents:**
`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md`,
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`,
`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`,
`RCONN_DERIVED_NOTE.md`,
`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`,
`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md`

## Scope

This note narrows the source-domain E-center bridge target by separating sign
support from magnitude/typecast support.

It does not select rho_E. It also does not supply the typed readout landing
edge. The result is only:

1. under the current positivity frame, the positive-lift family has
   `q_E > 0`;
2. under the granted T-side values, `q_T = 5/6` and `s_TE = -2`;
3. therefore
   ```text
   c_TE = s_TE q_T / q_E
   ```
   is negative throughout the positive-lift family;
4. matching the magnitude `|c_TE|` to the color-domain `F_adj = 8/9` remains
   an additional source-domain/typecast theorem.

The negative sign is support, not selection.

## Sign support

The positivity note states that positivity gives the one-sided domain

```text
rho_E > -6.
```

Equivalently,

```text
q_E = 1 + rho_E / 6 > 0.
```

The granted T-side endpoint values give

```text
q_T = 5/6 > 0,
s_TE = gamma_T(shell)/gamma_E(shell) = -2 < 0.
```

For every positive-lift member,

```text
c_TE = gamma_T(center)/gamma_E(center)
     = s_TE q_T / q_E
     < 0.
```

Thus the sign of the candidate `-F_adj` is compatible with the current
Route-2 positivity and T-side orientation data.

## Magnitude/typecast remainder

The exact color-domain support gives

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9
```

at `N_c = 3`. The sign result above can orient a signed scalar candidate

```text
signed scalar candidate = -F_adj = -8/9.
```

But the current source bank still lacks both of these stronger statements:

```text
|c_TE| = F_adj
scalar_signed_minus_8_9 -> route2_center_TE_minus_8_9.
```

Equivalently, it still lacks a typed landing edge into one of

```text
route2_center_TE_minus_8_9
route2_q_E_15_8
route2_rho_E_21_4.
```

That is the typed typecast remainder.

## Non-Uniqueness Under Sign Support

Many admissible positive-lift values have the correct negative sign but not
the `F_adj` magnitude:

| `rho_E` | `q_E` | `c_TE` | `|c_TE| = 8/9`? |
|---:|---:|---:|---:|
| `-1` | `5/6` | `-2` | no |
| `0` | `1` | `-5/3` | no |
| `1` | `7/6` | `-10/7` | no |
| `21/4` | `15/8` | `-8/9` | yes |
| `12` | `3` | `-5/9` | no |

So the sign alone leaves a continuum of admissible E-center readout entries.

## Exact Magnitude Consequence

If the missing magnitude/typecast statement is supplied as

```text
|c_TE| = F_adj = 8/9
```

inside the positive-lift family, then the sign support above fixes

```text
c_TE = -8/9.
```

The existing endpoint algebra then gives

```text
q_E = (-2)(5/6)/(-8/9) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

The arithmetic after the magnitude/typecast statement is exact. The missing
work is the magnitude/typecast statement itself.

## Handoff

This note narrows the next source-domain target:

- sign/orientation is supported under positivity plus the granted T-side
  values;
- the remaining positive theorem must supply `|c_TE| = F_adj`, or directly
  land in `route2_center_TE_minus_8_9`, `route2_q_E_15_8`, or
  `route2_rho_E_21_4`;
- a scalar `8/9` match without a Route-2 typecast is still insufficient.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=45, FAIL=0
VERDICT: positivity fixes the Route-2 center-ratio sign but not the F_adj magnitude/typecast.
```

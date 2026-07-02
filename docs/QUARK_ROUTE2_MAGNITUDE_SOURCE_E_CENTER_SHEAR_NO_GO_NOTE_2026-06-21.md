# Quark Route-2 Magnitude Source E-Center Shear No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary for shear-invariant magnitude source rules
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_magnitude_source_e_center_shear_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_magnitude_source_e_center_shear_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_magnitude_source_e_center_shear_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_magnitude_source_e_center_shear_no_go_2026_06_21.txt)
**Authority links:** [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [`QUARK_ROUTE2_W1_SIGN_MAGNITUDE_SPLIT_SUPPORT_NOTE_2026-06-21.md`](QUARK_ROUTE2_W1_SIGN_MAGNITUDE_SPLIT_SUPPORT_NOTE_2026-06-21.md), [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md)

## Purpose

Block32 narrowed W1 to the positive-branch magnitude condition:

```text
|c_TE| = F_adj = 8/9.
```

This block tests whether that magnitude can be selected by data that do not
evaluate the E-center lift. The answer is no: there is an exact E-center shear
freedom that leaves the shell normalization, granted T-side values, and color
fraction unchanged while changing `|c_TE|`.

## Exact Shear

With the T-side candidates granted,

```text
q_T = 5/6,
s_TE = -2,
q_E = 1 + rho_E/6,
c_TE = (-2)(5/6)/q_E = (-5/3)/q_E.
```

For positive `q_E`,

```text
|c_TE| = (5/3)/q_E.
```

The E-center shear is:

```text
q_E -> q_E + delta
rho_E -> rho_E + 6 delta.
```

It leaves the E-shell normalization and all granted T-side quantities fixed.
It also leaves the SU(3) color fraction `F_adj=8/9` fixed, because that
fraction lives on the color channel-count surface rather than the Route-2
E-center readout.

But the shear changes the magnitude:

| `q_E` | `rho_E` | `|c_TE|` |
|---:|---:|---:|
| `1` | `0` | `5/3` |
| `15/8` | `21/4` | `8/9` |
| `2` | `6` | `5/6` |
| `5/3` | `4` | `1` |

All four witnesses share the same shell/T-side/color data. Only the second
witness has `|c_TE|=F_adj`.

## Consequence

This prunes the route:

```text
shell normalization + T-side signs + color fraction
  -> |c_TE| = F_adj.
```

Any positive magnitude source rule must break the E-center shear by evaluating
or typing the E-center lift itself. Equivalently, it must supply:

```text
q_E = 15/8
```

or an equivalent source-domain rule for the Route-2 center ratio magnitude.

## Boundary

This is not a no-go against every future magnitude theorem. It only says that
shear-invariant current data cannot select the magnitude. A future theorem may
still supply a genuine E-center primitive, a typed source-domain rule, or an
explicit non-shear-invariant readout principle.

This block does not prove W1, a selected `P_R`, a physical `R_conn` selector,
or the endpoint triple. It narrows the remaining target to an E-center
shear-breaking primitive.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_magnitude_source_e_center_shear_no_go_2026_06_21.py
```

Expected:

```text
TOTAL: PASS=51, FAIL=0
Boundary classification: exact negative boundary for shear-invariant magnitude source rules.
```

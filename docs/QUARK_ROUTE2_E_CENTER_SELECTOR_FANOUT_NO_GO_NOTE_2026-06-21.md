# Quark Route-2 E-Center Selector Fan-Out No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary for E-center-visible natural selectors
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_selector_fanout_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_selector_fanout_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_selector_fanout_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_e_center_selector_fanout_no_go_2026_06_21.txt)
**Authority links:** [`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)

## Purpose

The prior E-center-blind no-go proves that shell-only and T-side constraints
cannot fix

```text
rho_E := beta_E / alpha_E.
```

This block tests the next harder route: allow selectors that do see the
E-center lift

```text
q_E = gamma_E(center)/gamma_E(shell) = 1 + rho_E/6,
```

but restrict them to exact endpoint-matrix symmetries and low-degree
relations among

```text
E_shell = 1,
T_shell = -2,
T_center = -5/3,
E_center = q_E.
```

The target remains

```text
q_E = 15/8,
rho_E = 21/4,
gamma_T(center)/gamma_E(center) = -8/9.
```

## Result

The E-center-visible fan-out does not select the target unless the missing
signed center-ratio bridge is supplied.

The runner solves a family of exact selector equations:

- row-sum equality;
- T-ratio reuse;
- equal signed center shift;
- opposite center shift;
- row-product equality;
- zero determinant;
- determinant equals shell product;
- equal row norm;
- signed center-ratio bridge;
- direct target quotient insertion.

The non-bridge selectors all see `q_E`, but none lands

```text
q_E = 15/8.
```

The only target-landing selectors are bridge-equivalent:

```text
T_center/q_E = -8/9
```

or

```text
q_E = 15/8.
```

Those are restatements of the missing E-center bridge, not derivations from
endpoint-matrix symmetry.

## Exact arithmetic

With the T-side candidates granted,

```text
q_T = gamma_T(center)/gamma_T(shell) = 5/6,
gamma_T(shell)/gamma_E(shell) = -2.
```

The target is equivalent to

```text
q_E = 15/8
rho_E = 6(q_E - 1) = 21/4
gamma_T(center)/gamma_E(center) = (-5/3)/(15/8) = -8/9.
```

The sign of the center ratio is not the main issue: for positive `q_E`,
`T_center/q_E` is automatically negative because `T_center = -5/3`. The
load-bearing issue is the magnitude selection

```text
|T_center/q_E| = 8/9.
```

That magnitude is the same missing typed bridge isolated by the source-domain
and scalar-typecast no-go packets.

## Scale-family check

If one writes the signed bridge as

```text
|T_center/q_E| = nu * (8/9),
```

then exact arithmetic gives

```text
q_E = 15/(8 nu).
```

The target appears only at

```text
nu = 1.
```

Thus a positive route must still explain the normalization `nu=1`, not merely
notice the color fraction `8/9` or the support denominator `6`.

## Consequence

This block prunes a stronger false repair than the E-center-blind no-go:

```text
E-center-visible endpoint-matrix naturality
  -> rho_E = 21/4
```

The endpoint matrix can be made to see `q_E`, but endpoint-matrix symmetry by
itself still does not choose the target. The remaining positive target is a
typed bridge:

```text
source-domain rule
or signed center-ratio theorem
or equivalent readout primitive
  -> gamma_T(center)/gamma_E(center) = -8/9.
```

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_selector_fanout_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=26, FAIL=0
Boundary classification: exact negative boundary for E-center-visible natural selectors.
```

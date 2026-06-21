# Quark Route-2 Rconn Two-Gate Source Bridge Factorization

**Date:** 2026-06-21
**Status:** exact negative boundary for conflating the Rconn source bridge
with the physical `kappa_EW` selector
**Primary runner:** `scripts/frontier_quark_route2_rconn_two_gate_source_bridge_factorization_2026_06_21.py`

## Purpose

The S3/Route-2 endpoint campaign has isolated the same target in several
forms:

```text
q_E = gamma_E(center)/gamma_E(shell) = 15/8
rho_E = beta_E/alpha_E = 21/4
c_TE = gamma_T(center)/gamma_E(center) = -8/9
```

The visible color scalar is also exact:

```text
F_adj = (N_c^2 - 1)/N_c^2 = 8/9 at N_c=3.
```

This block separates two gates that are easy to collapse in prose:

```text
W1: algebraic source-domain bridge
    su3_R_conn_8_9 -> route2_center_TE_minus_8_9

W2: physical connected-trace selector
    kappa_EW = 0 -> R_phys = F_adj = 8/9
```

The result is a finite factorization certificate. W2 by itself reaches the
color scalar but does not type that scalar as the Route-2 signed center ratio.
W1 by itself gives the Route-2 endpoint chain from the color scalar but does
not prove the physical connected-trace selector. The two gates are independent.

## Minimal Premises

Allowed:

1. exact Route-2 endpoint algebra and the current W9 typed inventory;
2. granted T-side stretch values `q_T=5/6` and
   `gamma_T(shell)/gamma_E(shell)=-2`;
3. exact SU(3) adjoint channel count `F_adj=8/9`;
4. the current `R_phys(kappa_EW)=F_adj+kappa_EW(1-F_adj)` family;
5. exact rational arithmetic.

Forbidden:

1. observed quark masses or fitted Yukawa entries;
2. CKM/J or endpoint-data target fitting;
3. nearest-rational selection from live data;
4. treating a color scalar as a Route-2 endpoint ratio without W1;
5. treating `kappa_EW=0` as available without W2.

## Four Case Table

Let the current W9 inventory be

```text
CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES.
```

Then:

| Case | Added gate(s) | Reachability |
|---|---|---|
| current inventory | none | `su3_R_conn_8_9` does not reach the Route-2 center ratio |
| W2 only | `kappa_EW=0 -> su3_R_conn_8_9` | the physical selector reaches the color scalar but not the Route-2 center ratio |
| W1 only | `su3_R_conn_8_9 -> route2_center_TE_minus_8_9` | the color scalar reaches the endpoint target chain, but no physical selector is supplied |
| W1 and W2 | both gates | the physical selector reaches the endpoint target chain |

The W2-only route is therefore not a discharge of the endpoint blocker. It
needs W1 in addition to the physical selector.

## Exact Algebra

With the T-side values granted,

```text
q_E = (-2)(5/6)/c_TE.
```

If W1 supplies

```text
c_TE = -F_adj = -8/9,
```

then exact arithmetic gives

```text
q_E = 15/8
rho_E = 6(q_E - 1) = 21/4.
```

For the physical selector family,

```text
R_phys(kappa_EW) = 8/9 + kappa_EW/9.
```

If an extra typing rule sets `c_TE=-R_phys(kappa_EW)`, then sampled values are:

| `kappa_EW` | `R_phys` | `q_E` | `rho_E` |
|---:|---:|---:|---:|
| `0` | `8/9` | `15/8` | `21/4` |
| `1/2` | `17/18` | `30/17` | `78/17` |
| `1` | `1` | `5/3` | `4` |

This table is not a proof of the selector. It only shows that even after a
physical `kappa_EW` value is chosen, a separate Route-2 typing step is still
load-bearing.

## Consequence

This block prunes the shortcut

```text
kappa_EW = 0
  -> endpoint target
```

unless the algebraic source-domain bridge W1 is also supplied. It also prunes
the reverse conflation

```text
F_adj = 8/9
  -> physical connected-trace selection
```

unless W2 is independently supplied. The remaining positive work is therefore
sharper:

```text
either prove W1 from the current source/readout surface,
or prove W2 and W1 as separate theorems,
or find an equivalent E-center primitive.
```

## Boundary

This is not a repo-wide status change and does not apply an audit verdict. It
does not prove a selected `P_R`, a physical EW-current readout, a `kappa_EW`
selector, or the S3/Route-2 endpoint triple. It narrows the open endpoint
work by showing that the physical selector and the algebraic Route-2 source
bridge are independent gates.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_two_gate_source_bridge_factorization_2026_06_21.py
```

Expected:

```text
TOTAL: PASS=49, FAIL=0
Status: exact negative boundary for W1/W2 gate conflation.
```

# Quark Route-2 Source-Augmented E-Center Functor No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary / functoriality no-go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_source_augmented_e_center_functor_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_source_augmented_e_center_functor_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_source_augmented_e_center_functor_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_source_augmented_e_center_functor_no_go_2026_06_21.txt)
**Primary parents:**
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md),
[`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md),
[`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md),
[`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md),
[`QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)

## Scope

This is a first-principles attack on the E-center typed landing theorem. It
asks whether adding the accepted source scalar

```text
F_adj = 8/9
```

to the E-center-blind Route-2 endpoint data can select the E-center lift.

It cannot. The source-augmented blind signature

```text
(F_adj, R_conn, E-shell readout, T-shell readout, T-center readout)
```

is identical for many exact readout maps with different E-center lifts. Thus
the source scalar by itself does not select the E-center lift. A future
positive theorem must add a typed landing edge that evaluates the E-center
column, or an equivalent readout primitive.

## A_min

Allowed minimal premises:

1. exact source-domain support
   ```text
   F_adj = (N_c^2 - 1) / N_c^2 = 8/9
   ```
   at `N_c = 3`;
2. exact Route-2 restricted endpoint carrier;
3. granted T-side values `beta_T/alpha_T = -1` and
   `alpha_T/alpha_E = -2`;
4. endpoint algebra:
   ```text
   q_E = 1 + rho_E/6
   c_TE = (-2)(5/6) / q_E;
   ```
5. exact rational arithmetic;
6. current quote-derived typed-edge inventory.

Forbidden proof inputs:

- observed masses;
- fitted Yukawa or CKM/J targets;
- live endpoint nearest-rational selection;
- physical connected-trace selector;
- untyped identification of a source scalar with a Route-2 center readout.

## Source-Augmented Blind Signature

For the reduced readout family

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0,-2, 0,     2]],
```

the E-center-blind endpoint columns give

```text
P(rho_E) E-shell  = (1, 0)
P(rho_E) T-shell  = (0,-2)
P(rho_E) T-center = (0,-5/3).
```

These values do not depend on `rho_E`. Adding the source scalar

```text
F_adj = R_conn = 8/9
```

also does not depend on `rho_E`.

The runner checks the samples

```text
rho_E = -1, 0, 1, 21/4, 9.
```

All have the same source-augmented blind signature, but they have different
E-center lifts

```text
q_E = 1 + rho_E/6
```

and different center magnitudes

```text
|c_TE| = (5/3) / q_E.
```

Therefore any selector or functor that factors only through the
source-augmented blind signature must assign the same output to all these
maps. It cannot select the target E-center lift.

## Missing Typed Landing

The target value is still exactly equivalent to the center landing:

```text
rho_E = 21/4
q_E = 15/8
|c_TE| = 8/9 = F_adj.
```

Inside endpoint algebra, adding

```text
|c_TE| = F_adj
```

would select the target. But that statement is precisely the typed landing
edge: it maps a source-domain scalar into a Route-2 E/T center magnitude. It
is not supplied by the source-augmented blind signature.

The current typed-edge inventory still has no path

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_rho_E_21_4.
```

Adding the named missing typed landing makes the path immediate, so the missing
object is sharply identified.

## Consequence

This block prunes the tempting route:

```text
F_adj = 8/9
+ E-center-blind Route-2 endpoint data
+ functoriality/naturality through that data
=> target E-center lift.
```

That implication is false. The same source-augmented blind signature supports
several exact E-center lifts.

The next positive theorem must supply at least one of:

```text
typed landing edge: F_adj -> |c_TE|
typed center ratio: su3_R_conn_8_9 -> route2_center_TE_minus_8_9
E-center evaluator: a source/readout primitive that sees P_R E-center
direct q_E theorem: gamma_E(center)/gamma_E(shell) = 15/8
```

Anything weaker leaves the E-center coordinate free.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_augmented_e_center_functor_no_go_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=31, FAIL=0
VERDICT: adding source scalar F_adj to E-center-blind data still leaves the E-center lift free; a typed landing edge is required.
```

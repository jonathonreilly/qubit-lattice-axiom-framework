# Quark Route-2 Gravity-Metric Rho_E Value Packet

**Date:** 2026-06-21
**Claim type:** bounded_support
**Status:** branch-local support/demotion boundary for the gravity-metric
`rho_E ~= 5.2575` value. This note does not derive the Route-2 endpoint
triple and does not apply an audit verdict.
**Primary runner:**
[`scripts/frontier_quark_route2_gravity_metric_rhoe_value_packet_2026_06_21.py`](../scripts/frontier_quark_route2_gravity_metric_rhoe_value_packet_2026_06_21.py)
**Output:**
[`outputs/frontier_quark_route2_gravity_metric_rhoe_value_packet_2026_06_21.txt`](../outputs/frontier_quark_route2_gravity_metric_rhoe_value_packet_2026_06_21.txt)

## Scope

Prior Route-2 notes name two shell-vs-center distinguishing leads:

```text
color-clean bridge:      rho_E = 21/4
gravity-metric response: live rho_E ~= 5.2575
```

This block asks what the current gravity-metric/live value can honestly do for
the exact endpoint target. It uses only current repo endpoint/readout data and
exact rational arithmetic. It forbids observed quark masses, fitted endpoint
selectors, nearest-rational proof moves, `N=15` proof selection, and audit
verdicts.

## Exact Target

The exact target chain is:

```text
rho_E = 21/4,
q_E = 1 + rho_E/6 = 15/8,
q_T = 5/6,
q_E/q_T = 9/4,
c_TE = -8/9.
```

This is the color-clean target if the typed signed bridge supplies the Route-2
center ratio `c_TE=-8/9`.

## Live Gravity-Metric / Readout Value

The current endpoint/readout surface gives:

```text
q_E   = 1.876246130347...
rho_E = 6(q_E - 1) = 5.257476782081...
c_TE  = -0.890683778231...
```

That live value is close to the exact target `21/4 = 5.25`, but it is not the
same number. The gap is small and real:

```text
rho_E live - 21/4 ~= +0.007476782081
relative gap ~= 0.1424 percent.
```

The live center ratio similarly misses `-8/9` by about `0.2 percent`.

## Theorem

**Theorem (gravity-metric value boundary).** On the current repo surface, the
live gravity-metric/readout value near

```text
rho_E ~= 5.2575
```

is a positive-family comparator/support datum, not an exact derivation of

```text
rho_E = 21/4.
```

It sits inside the positive E-row projective family `rho_E > -6`, so it is a
non-vacuous shell-vs-center distinguishing datum. But adopting it would select
the live value, not the color-clean exact target. Rounding it to `21/4` is a
nearest-rational endpoint selector unless a new theorem supplies the equality.

Therefore this route does not close the endpoint triple. It produces a
decision boundary:

- derive a selector theorem that moves the live value to exact `21/4`;
- explicitly admit a readout convention, if the project chooses that route;
- or demote the live gravity-metric value to comparator/support evidence
  against exact closure.

## What This Moves

This prunes the route:

```text
gravity-metric live rho_E ~= 5.2575
  -> exact rho_E = 21/4
```

unless an additional selector theorem or explicit readout convention is
supplied.

It also prevents a false merger of two different candidates:

```text
live gravity-metric branch: rho_E ~= 5.2575
color-clean branch:         rho_E = 21/4
```

Both remain useful as comparison targets. They are not the same current-bank
claim.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_gravity_metric_rhoe_value_packet_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=42, FAIL=0
VERDICT: the live gravity-metric/readout value rho_E~=5.2575 is a real positive-family comparator/support datum, but it is not the exact color-clean target 21/4.
```

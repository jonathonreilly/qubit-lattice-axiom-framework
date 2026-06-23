# Quark Route-2 Two-Outcome Probability Surface No-Go

**Date:** 2026-06-22
**Type:** no-go / two-outcome probability surface obstruction
**Actual current-surface status:** no-go for a two-outcome `{E,T}` sharp-record probability surface supplying the Route-2 shell/center `P_R/E-T` probability contract
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_two_outcome_probability_surface_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_two_outcome_probability_surface_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_two_outcome_probability_surface_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_two_outcome_probability_surface_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block131 asks for a Route-2 sharp-record probability surface `Omega_R`, `P0`,
and `P_h`. Can the smallest candidate

```text
Omega_R = {E,T}
```

carry the physical Route-2 readout needed by the probability-surface contract?

## Result

No. The exact Route-2 readout surface is not just an E/T label set. It has four
typed endpoint carrier slots:

```text
E-shell, E-center, T-shell, T-center.
```

The center-ratio readout uses shell/center structure:

```text
q_T = gamma_T(center) / gamma_T(shell)
q_E = gamma_E(center) / gamma_E(shell)
c_TE = gamma_T(center) / gamma_E(center).
```

A two-outcome `{E,T}` sharp record can encode an E/T sign or label. It cannot,
by itself, distinguish shell from center inside each channel, so it cannot type
the physical center-ratio scalar line required by Block131.

## Missing Primitive

The next construction target is therefore at least:

```text
Route-2 shell/center probability-surface theorem:

construct a typed probability surface with E/T and shell/center structure,
for example Omega_R carrying E-shell, E-center, T-shell, and T-center events;
construct P0 and P_h on that surface; prove the RN score line reads the same
physical center-ratio scalar as P_R/E-T; and prove the Block121 source scalar
and physical readout scalar are same-source Fisher-unit Riesz lines.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=75, FAIL=0
```

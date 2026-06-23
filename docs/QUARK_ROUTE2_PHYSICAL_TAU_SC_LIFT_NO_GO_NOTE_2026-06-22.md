# Quark Route-2 Physical Tau_sc Lift No-Go

**Date:** 2026-06-22
**Type:** no-go / formal carrier reflection to physical source-measure lift
**Actual current-surface status:** no-go for the current carrier/readout surface proving tau_sc is a physical source-measure automorphism
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_physical_tau_sc_lift_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_physical_tau_sc_lift_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_physical_tau_sc_lift_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_physical_tau_sc_lift_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block136 gives a conditional selector theorem: a physical shell/center
reflection `tau_sc`, invariant `P0`, and odd physical center score would select
the canonical four-slot source measure. Does the current exact
`K_R -> P_R -> E/T` surface already supply that physical `tau_sc` lift?

## Formal Carrier Reflection

On each channel carrier plane with coordinates `(u, delta u)`, the exact shell
and center endpoint columns are:

```text
shell  = (1, 0)
center = (1, 1/6).
```

There is a formal linear involution

```text
T_sc(u, d) = (u, u/6 - d)
```

that swaps these two columns. It also makes the row

```text
s(u,d) = -u + 12 d
```

odd:

```text
s(T_sc(u,d)) = -s(u,d).
```

So the carrier algebra contains a formal reflection and a formal odd
shell/center score row.

## Boundary

That is not yet a physical source-measure automorphism. The current exact
readout rows are endpoint-fixed carrier/readout rows, not the odd score row
`-u + 12 d`. The current surface does not prove:

```text
T_sc is an automorphism of a Route-2 source-measure sample space,
P0 is invariant under T_sc,
the physical center-ratio covariance readout is the T_sc-odd score row,
and that odd score is same-source Fisher-unit Riesz with Block121.
```

Therefore the formal carrier reflection supports the Block136 theorem target,
but it does not instantiate that theorem on the current surface.

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=68, FAIL=0
```

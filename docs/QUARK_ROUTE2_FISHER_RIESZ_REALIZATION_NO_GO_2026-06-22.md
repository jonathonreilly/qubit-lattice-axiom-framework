# Quark Route-2 Fisher-Riesz Realization No-Go

**Date:** 2026-06-22
**Type:** no-go / current finite readout to Fisher-Riesz realization obstruction
**Actual current-surface status:** no-go for the current finite `P_R` readout surface plus generic Fisher support instantiating the Block129 Route-2 Fisher-Riesz realization
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_fisher_riesz_realization_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_fisher_riesz_realization_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_fisher_riesz_realization_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_fisher_riesz_realization_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block129 gives a sufficient theorem:

```text
Route-2 Fisher-Riesz realization => Phi_ET^* g_readout = g_source => mu=1.
```

Does the current Route-2 finite `K_R -> P_R -> E/T` readout surface, together
with generic finite Fisher/RN support, already supply that realization?

## Result

No. The current finite Route-2 readout surface supplies linear carrier/readout
data:

```text
K_R -> P_R -> E/T shell-center readout.
```

The Fisher-Riesz realization requires different typed data:

```text
Omega_R: finite Route-2 sharp-record sample space
P_0: positive reference probability on Omega_R
P_h: normalized source path with P_h << P_0
s = d log(dP_h/dP_0)/dh |_{h=0}: zero-mean score tangent
<s,t>_F = E_0[s t]: Fisher metric
unit Riesz vectors for the source scalar line and physical readout scalar line
```

The finite `P_R` packet does not provide `Omega_R`, `P_0`, `P_h`, the RN score,
or the Riesz unit-line identification. Generic Fisher support supplies the
geometry once those objects are supplied; it does not supply the Route-2
objects by itself.

## Reference-Measure Dependence

Even the two-outcome signed-score pattern is not a Route-2 unit statement
until a reference probability is fixed. For a reference weight
`p in (0,1)`, the zero-mean signed score

```text
s_p = (1, -p/(1-p))
```

has Fisher norm square:

```text
||s_p||_F^2 = p + p^2/(1-p).
```

For rational choices:

```text
p = 1/3 -> ||s_p||_F^2 = 1/2
p = 1/2 -> ||s_p||_F^2 = 1
p = 2/3 -> ||s_p||_F^2 = 2
```

Thus unit normalization and hence the physical source/readout scale depend on
the missing Route-2 reference probability and RN source path. No endpoint value
is used.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 sharp-record Fisher-Riesz realization theorem:

construct Omega_R, P_0, and a normalized RN source path P_h for the physical
P_R/E-T readout; prove the Block121 connected scalar and the physical
center-ratio scalar are same-source zero-mean score directions; prove their
Riesz representatives are Fisher-unit vectors; and identify Phi_ET with the
unit Fisher-Riesz map between those lines.
```

Expected runner result:

```text
TOTAL: PASS=88, FAIL=0
```

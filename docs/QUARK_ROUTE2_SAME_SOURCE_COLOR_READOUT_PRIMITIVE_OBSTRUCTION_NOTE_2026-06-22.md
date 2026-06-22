# Quark Route-2 Same-Source Color-Readout Primitive Obstruction

**Date:** 2026-06-22
**Type:** no-go / primitive obstruction packet
**Actual current-surface status:** no-go for the current `P_R` feature carrier as a same-source full color readout
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_same_source_color_readout_primitive_obstruction_2026_06_22.py`](../scripts/frontier_quark_route2_same_source_color_readout_primitive_obstruction_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_same_source_color_readout_primitive_obstruction_2026_06_22.txt`](../outputs/frontier_quark_route2_same_source_color_readout_primitive_obstruction_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block82 sharpened the missing primitive to:

```text
MR_color + Route-2 same-source full color-record readout theorem.
```

This block attacks that primitive directly on the exact Route-2 `P_R` surface.
Can the current exact `P_R` feature carrier itself serve as a same-source
readout over a full trace-one `End(C^3)` color-record ensemble?

## Result

No. The current exact `P_R` surface has the wrong representation slot.

The exact Route-2 readout map reduces the restricted bright carrier to four
scalar features:

```text
K_R = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

These are `E/T` endpoint features with no color index and no adjoint color
slot. The full color source required by the connected/disconnected selector is

```text
End(C^3) = C I_3 + sl_3,
dim End(C^3) = 9,
dim sl_3 = 8.
```

On the minimal current surface, the Route-2 `K_R` features are SU(3)-trivial
scalars. An SU(3)-equivariant same-source color readout would need a nonzero
map

```text
sl_3_adjoint -> trivial^4.
```

There is no such nonzero equivariant map. If equivariance is dropped, the map
is a non-invariant selector import; in any case a map through four scalar
features has centered rank at most four, not the eight-dimensional full
`sl_3` tangent.

Therefore the current `P_R` feature carrier cannot be the same-source full
trace-one `End(C^3)` color-record ensemble.

## What This Adds Beyond Blocks 80-82

- Block80 pruned finite endpoint lifts of four Route-2 endpoint labels.
- Block81 pruned generic source-measure/Fisher/RN transfer.
- Block82 pruned color-SU3 record-invariance support transfer.
- This block prunes the direct primitive on the exact `P_R` carrier itself:
  the current Route-2 feature carrier is SU(3)-trivial and too low-rank for
  full color-source variation.

## Missing Primitive After This Block

The missing theorem is now sharper:

```text
Route-2 adjoint color-source carrier theorem:

extend or identify the Route-2 source/readout surface so that it contains a
same-source `End(C^3)` color-record variable with scalar-line/disconnected and
sl_3/connected typing, and prove that the physical `P_R/E-T` readout consumes
that same source.
```

Equivalently, a future closure must add one of:

1. an actual SU(3)-adjoint color-source slot inside the Route-2 carrier;
2. a theorem that the current `E/T` scalar feature carrier is not SU(3)-trivial
   after all;
3. a different connected/disconnected theorem that does not require full
   `sl_3` same-source variation.

Without one of those, `MR_color` alone is not enough. It can assign color
matter and color records, but the current `P_R` features still have no place to
carry the full connected color tangent.

## No Endpoint Value

No endpoint value is used. This packet does not insert `c_TE`, `rho_E`, a
target comparator, or a fitted readout entry. It is a representation-domain
and rank obstruction.

## Runner Certificate

The runner verifies:

- the exact Route-2 readout map is a four-feature scalar `E/T` carrier;
- `End(C^3)` decomposes into a scalar line plus the eight-dimensional adjoint
  `sl_3` tangent;
- `Hom_SU3(sl_3, trivial^4) = 0`;
- non-equivariant maps through the current features have rank at most four;
- the `P_R` output has rank at most two;
- no reachability path exists from the current `P_R` carrier to the full
  same-source color ensemble;
- adding an explicit adjoint color-source carrier is the named primitive that
  would reopen the constructive route.

Expected result:

```text
TOTAL: PASS=68, FAIL=0
```

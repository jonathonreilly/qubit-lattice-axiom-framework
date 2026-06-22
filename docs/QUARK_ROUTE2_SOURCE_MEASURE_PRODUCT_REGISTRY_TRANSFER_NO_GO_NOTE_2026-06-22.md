# Quark Route-2 Source-Measure Product-Registry Transfer No-Go

**Date:** 2026-06-22
**Type:** no-go / Pcal product-registry transfer obstruction packet
**Actual current-surface status:** no-go for generic source-measure Pcal/Mobius support supplying the Route-2 product registry
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block99 sharpened the missing primitive to a typed source-action/product
registry. The source-measure Pcal/Mobius theorem already proves the abstract
identity:

```text
D_A D_B log Z = D_A D_B Z - (D_A Z)(D_B Z).
```

Does that generic theorem already supply the Route-2 product registry needed
to type the E/T-symmetric singlet line as pure disconnected?

## Result

No. The Pcal/Mobius theorem supplies the abstract finite-record cumulant
formula once the record variables, moment generator, raw moments, and one-point
moments are supplied. It does not itself instantiate the Route-2 physical
record variables or prove that the finite `P_R/E-T` slots are the raw moment
registry for those variables.

The obstruction is load-bearing. For a two-point source response,

```text
connected = raw_second - one_point_A * one_point_B.
```

The same raw second moment can give different connected Route-2 selectors
depending on the one-point product:

```text
raw_second = 1, one_point_A * one_point_B = 0   -> connected = 1
raw_second = 1, one_point_A * one_point_B = 1/9 -> connected = 8/9
```

Only the second line is the `kappa=0` selector. Therefore the one-point product
registry is not decorative bookkeeping; it is the theorem that identifies the
singlet line as pure disconnected for the same Route-2 source/readout.

## Relation To Existing Source-Measure Support

The existing source-measure stack remains useful support:

```text
finite sharp-record RN/tangent geometry
Pcal/Mobius connected-response generator
record-intervention source-sector theorem
```

Those packets do not name the Route-2 record variables, do not map `P_R/E-T`
slots to raw `D_A D_B Z` moments, and do not prove the E/T-symmetric `1/9`
singlet coefficient is `(D_A Z)(D_B Z)` for that same source.

This block is narrower than the earlier full color-ensemble transfer no-go. It
does not ask whether source-measure support supplies all of `End(C^3)`. It asks
whether the source-measure cumulant theorem alone supplies the product registry
needed after Block99. It does not.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 Pcal product-instantiation theorem:

construct the Route-2 physical record variables and reference source measure;
prove the physical E/T readout slots are the raw D_A D_B Z moment registry for
those variables; prove the one-point products D_A Z D_B Z exist on the same
source and equal the E/T-symmetric singlet line; and then identify D_A D_B log Z
with the connected Route-2 readout.
```

Together with antisymmetric adjoint typing, that would let the existing
connected-cumulant theorem force `kappa=0` without endpoint input.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=72, FAIL=0
```

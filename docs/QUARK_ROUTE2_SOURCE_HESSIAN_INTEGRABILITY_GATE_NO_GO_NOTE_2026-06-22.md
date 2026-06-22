# Quark Route-2 Source-Hessian Integrability Gate No-Go

**Date:** 2026-06-22
**Type:** no-go / source-Hessian integrability gate obstruction packet
**Actual current-surface status:** no-go for assigning current finite P_R slots to a source Hessian without a symmetric source-index registry
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block97 showed that the finite `K_R -> P_R` readout is not itself a
same-source two-jet. A positive source-jet lift still might exist. What extra
gate must such a lift pass?

## Result

Any source-Hessian lift must provide a symmetric source-index two-jet:

```text
H_AB = D_A D_B log Z = H_BA.
```

The current exact `P_R` surface gives channelwise finite endpoint slots:

```text
E-shell, E-center, T-shell, T-center.
```

It does not provide a registry that says which slot is which unordered source
pair `{A,B}`. Without that registry, a proposed assignment can violate mixed
partial reciprocity:

```text
slot(A,B) != slot(B,A).
```

This is a source-Hessian integrability gate, not an endpoint-value gate. It
does not rule out all future source-Hessian lifts. It rules out the shortcut
that the current finite `P_R` slot data alone already supplies a valid
`D_A D_B log Z` readout.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 source-Hessian integrability registry theorem:

construct the source coordinate set J_A for the physical Route-2 E/T readout,
assign each physical readout slot to a symmetric source-index pair {A,B},
prove the mixed-partial reciprocity constraints H_AB = H_BA, and then identify
that symmetric two-jet with D_A D_B log Z for the same source/readout.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=53, FAIL=0
```

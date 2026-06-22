# Quark Route-2 Domain-Graded Typed-Edge Inventory Support

**Date:** 2026-06-22
**Claim type:** bounded_support
**Actual current-surface status:** bounded-support for generated typed-edge inventory
**Trace class:** upstream_support + negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_domain_graded_typed_edge_inventory_2026_06_22.py`

Actual current-surface status: bounded-support for generated typed-edge inventory.

## Scope

The Route-2 source-domain bridge no-go has an audit-facing residual: its
finite current-bank typed-edge inventory is a configured runner constant,
even though later repairs quote-anchor every edge against one-hop authority
files.

This block narrows that residual.  It builds a domain-graded generated inventory
from the quote-anchor authority schema and verifies that the
generated edge keys match the configured edge keys used by
`frontier_quark_route2_source_domain_bridge_no_go.py`.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Domain-Graded Generated Inventory

The runner separates the finite bank into typed domains:

| Domain | Nodes |
|---|---|
| Route-2 support | `delta_A1`, bright `E/T`, `K_R` |
| Route-2 readout/algebra | restricted readout, endpoint algebra, `c_TE`, `q_E`, `rho_E` |
| SU(3) color | color trace, `R_conn=8/9` |

It regenerates the current and derived edge sets from the quote-anchor schema
already present in the source-domain runner.  The generated edge keys match:

```text
CURRENT_TYPED_EDGES
DERIVED_ADDITIONAL_EDGES
```

and the missing bridge is not generated:

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9.
```

Equivalently, the missing bridge remains absent from the generated inventory.

## Domain Invariant

Every generated edge stays inside its declared domain family:

- Route-2 support/readout/algebra edges stay on the Route-2 side.
- The SU(3) color edge stays on the color side.
- No generated edge crosses from SU(3) color into a Route-2 endpoint node.

The absent edge is exactly such a cross-domain edge:

```text
R_conn -> c_TE=-8/9.
```

That edge is therefore still a theorem target, not a consequence of the
generated current-bank inventory.

## Reachability Result

On the generated domain-graded bank:

```text
R_conn=8/9
```

does not reach

```text
rho_E=21/4.
```

If the missing bridge is added as a new premise, the endpoint algebra creates
the path immediately:

```text
R_conn=8/9 -> c_TE=-8/9 -> q_E=15/8 -> rho_E=21/4.
```

So this block supports the finite inventory side of the source-domain no-go,
but it keeps the bridge import explicit.

## Relation To Blocks69-73

Blocks69-73 narrowed the endpoint obstruction to two equivalent forms:

```text
kappa=0
```

or

```text
connected-cumulant / disconnected-subtraction readout.
```

This block does not derive that selector.  It only removes a bookkeeping
weakness around the source-domain graph by showing that the current finite
edge bank can be regenerated from quote-anchored authority schemas without
creating the missing color-to-Route-2 bridge.

## Result

The configured-inventory residual is narrowed:

```text
quote-anchored authority schema -> generated typed-edge inventory
```

with no reachability flip.

The remaining positive target is unchanged:

```text
derive the cross-domain bridge R_conn -> c_TE=-8/9
```

or derive the equivalent connected-cumulant selector from another accepted
typed source/readout theorem.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_domain_graded_typed_edge_inventory_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=102, FAIL=0
```

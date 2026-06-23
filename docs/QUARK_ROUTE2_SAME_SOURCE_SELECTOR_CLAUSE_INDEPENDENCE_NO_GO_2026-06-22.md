# Quark Route-2 Same-Source Selector Clause-Independence No-Go

**Date:** 2026-06-22
**Type:** no-go / weakened same-source selector bridge clause-independence
**Actual current-surface status:** no-go for weakened same-source selector bridge clauses proving `kappa=0` or `c_TE=-8/9`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_same_source_selector_clause_independence_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_same_source_selector_clause_independence_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_same_source_selector_clause_independence_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_same_source_selector_clause_independence_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block147 mapped the endpoint-free selector atlas:

```text
same-source E[XY]=1 and E[X]E[Y]=1/9
  -> D^2 log Z = 8/9
  -> kappa=0.
```

Earlier blocks supplied conditional sufficient theorems and pruned many
shortcuts. The remaining issue is whether the physical Route-2 bridge can use a
weakened version of the same-source selector theorem.

## Result

No. The exact primitive cannot drop any of the following clauses:

```text
C1. same-source surface:
    X and Y are readouts on one physical Route-2 source.

C2. raw moment registry:
    the physical same-source raw moment is E[XY]=1.

C3. connected-subtraction typing:
    the physical readout consumes E[XY]-E[X]E[Y], not the raw Hessian alone.

C4. one-point product selector:
    the same source proves E[X]E[Y]=1/9.

C5. physical readout unit:
    the normalized connected source unit maps to the Route-2 physical
    center-ratio magnitude with mu=1.

C6. orientation sign:
    the endpoint orientation sign is consumed after the connected selector is
    fixed.
```

Clauses `C1-C4` force `kappa=0`. Clauses `C5-C6` then convert the internal
connected selector to the signed physical readout:

```text
c_TE = sigma * mu * (8/9 + kappa/9) = (-1) * 1 * (8/9) = -8/9.
```

The runner gives an endpoint-free witness for every single-clause omission.
The table below lists the single-clause omissions:

| Omitted clause | Endpoint-free witness |
|---|---|
| `C1` same-source surface | matching numbers on two unrelated sources do not define a physical Route-2 cumulant |
| `C2` raw moment registry | `E[X]E[Y]=1/9` with raw moment `2/3` gives connected value `5/9` |
| `C3` connected-subtraction typing | raw Hessian readout with raw moment `1` gives `kappa=1` even when the product is `1/9` |
| `C4` one-point product selector | raw moment `1` with product `1/4` gives connected value `3/4` |
| `C5` physical readout unit | `kappa=0` with `mu=1/2` gives `c_TE=-4/9` |
| `C6` orientation sign | `kappa=0`, `mu=1`, and `sigma=+1` gives `c_TE=+8/9` |

Thus no weakened selector theorem is enough. The proof primitive must be the
full typed bridge:

```text
Route-2 same-source selector bridge theorem:

construct the physical same-source P_R/E-T source/readout variables X,Y;
prove the raw moment E[XY]=1;
prove the connected-subtraction typing;
prove the same-source one-point product E[X]E[Y]=1/9;
prove the source/readout unit calibration mu=1; and consume the existing
orientation sign only after kappa=0 is fixed.
```

## Boundary

This packet does not rule out that theorem. It rules out weakened substitutes
for it. In particular it does not reopen the already-pruned routes through
binary bias, scalar normalization, finite `P_R` row labels, direct
readout-family algebra, same-rational comparators, or endpoint-value reversal.

No endpoint value is used as an input. The packet does not import `rho_E`,
`q_E`, observed quark values, fit-derived weights, or a target comparator.

Expected runner result:

```text
TOTAL: PASS=79, FAIL=0
```

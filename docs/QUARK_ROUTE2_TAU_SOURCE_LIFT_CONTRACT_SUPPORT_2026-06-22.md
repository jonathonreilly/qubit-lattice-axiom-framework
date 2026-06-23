# Quark Route-2 Tau Source-Lift Contract Support

**Date:** 2026-06-22
**Type:** exact-support / conditional tau_sc source-measure lift contract
**Actual current-surface status:** exact-support for a conditional tau_sc source-measure lift contract; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_tau_source_lift_contract_support_2026_06_22.py`](../scripts/frontier_quark_route2_tau_source_lift_contract_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_tau_source_lift_contract_support_2026_06_22.txt`](../outputs/frontier_quark_route2_tau_source_lift_contract_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block137 pruned formal carrier `tau_sc` alone as a physical source-measure
automorphism. What exact lift theorem would be sufficient?

## Tau Source-Lift Contract

The missing primitive is supplied by the following clauses:

```text
L1. source_space:
    construct a finite Route-2 source-measure sample space Omega_S.

L2. slot_lift:
    construct a typed lift iota: Omega_R -> Omega_S for the four shell/center
    slots E-shell, E-center, T-shell, T-center.

L3. source_tau:
    construct an involution tau_S on Omega_S.

L4. lift_commutes:
    prove tau_S iota = iota tau_sc on the four Route-2 slots.

L5. invariant_reference:
    construct a positive normalized P0 on Omega_S with P0 tau_S-invariant.

L6. odd_physical_score:
    prove the physical center-ratio covariance score is tau_S-odd and
    restricts to the shell/center contrast on iota(Omega_R).

L7. same_source_riesz:
    identify this score with the Block121 connected scalar source through a
    same-source Fisher-unit Riesz line.
```

Then the formal carrier reflection from Block137 becomes a physical
source-measure automorphism, Block136 selects canonical `P0`, and the Route-2
probability-surface path can consume the unit center score without endpoint
input.

## Boundary

This packet is a contract, not a construction. It does not prove `Omega_S`,
`iota`, `tau_S`, or the odd physical score exist on the current surface.

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=75, FAIL=0
```

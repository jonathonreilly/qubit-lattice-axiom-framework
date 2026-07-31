# Assumptions And Imports

## Existing mathematical premises

- P1: the named ABSS equivariant fixed-point formula.
- P2: APS fractional-part invariance.
- P3: the declared `Z_3` tangent class `(1,2)`.

This block neither proves nor weakens those premises. It changes only evidence
transport.

## Packet assumptions checked

- The primary cache is identity-fresh for
  `scripts/frontier_koide_aps_topological_robustness.py`.
- Its cache body is larger than the legacy 6,000-character excerpt but no
  larger than the current 20,000-character stdout budget.
- The cited block-by-block authority is 12,320 bytes, larger than the generic
  10,000-character authority cap but below the scoped 20,000-character cap.
- The target has two one-hop dependencies, so the 60,000-character total
  authority budget does not reduce the scoped override.

## Counterfactual pass

- If the cache body grows beyond 20,000 characters, the packet becomes
  explicitly clipped again and cannot support `audited_clean`.
- If the named authority grows beyond 20,000 characters, the regression test
  fails rather than silently accepting a clipped packet.
- If the audit runs live instead of using the cache, the same 20,000-character
  stdout limit applies; the present 9,802-character stdout fits.
- Replacing the named authority with another dependency could change the
  claim graph. This block does not take that route.
- No metric law, PL compactification, spin/global APS bridge, or physical
  readout is inferred from packet completeness.

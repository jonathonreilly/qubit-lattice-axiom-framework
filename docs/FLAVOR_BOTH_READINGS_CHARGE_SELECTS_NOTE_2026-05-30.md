# Flavor Both Readings: Charge Selection Does Not Close the Pin

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "a generation-scalar charge `U(1)` selects the `det_C` doublet reading".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_both_readings_charge_selects_2026_05_30.py` (SCORECARD PASS=6).

## Closed Packet

This repaired packet keeps only the finite checks and explicitly bounded
comparator statements:

1. On the real `C3` circulant family, the `r=1` point has spectrum
   `{3a,0,0}` and is the rank-one/democratic endpoint.
2. If a physical charge `U(1)` acts as a scalar on the generation triplet, it
   commutes with `C` and cannot orient the generation doublet or select the
   `det_C` reading.
3. A continuous doublet rephasing of `C` is incompatible with `C^3=I` except at
   the three discrete `C3` phases.
4. The displayed charged-fermion and neutrino mass tables are empirical
   comparators only. They organize the finite readout axis but do not derive a
   framework selector.

## What This Does Not Claim

This packet intentionally does not derive:

- that the physical Standard Model gauge `U(1)` actions are generation-scalar
  in the framework;
- that electric charge is unable to participate in any other future flavor
  mechanism;
- that the observed charged-fermion sector ordering is a framework theorem;
- a physical `det_C` or `det_R` selector;
- a charged-lepton `Q=2/3` derivation.

The remaining frontier question is a genuine flavor/readout selector for how
the doublet is counted.

## Direct Checks

- `H=aI+bC+bC^T` at `b=a` has eigenvalues `{0,0,3a}` and `Q=1`.
- A scalar generation action `iI` commutes with `C`.
- Generic continuous rephasing `C -> exp(i alpha)C` violates `C^3=I`; only
  `alpha=0,2pi/3,4pi/3` survives.
- The embedded mass-comparator table gives
  `Q_leptons < Q_down < Q_up < 1`, while neutrino positive-root scans stay
  below `2/3` in the tested normal-ordering range.

## Provenance

- The paired runner verifies the finite spectral, scalar-commutation,
  order-three rephasing, and comparator arithmetic.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.

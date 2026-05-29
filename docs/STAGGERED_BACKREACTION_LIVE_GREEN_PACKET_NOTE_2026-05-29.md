# Staggered Backreaction Live Green Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit, not effective retained.
**Claim type:** positive_theorem
**Primary runner:** [`scripts/staggered_backreaction_live_green_packet_check.py`](../scripts/staggered_backreaction_live_green_packet_check.py)

## Purpose

The archived staggered Green-closure note is failed because its numerical
table is stale against the live runner. This packet does not restore the old
near-order-of-magnitude closure or clean calibrated-holdout claim. It records
the narrower positive surface that the current live runner supports.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## Live Finite Result

The runner imports the current
[`scripts/frontier_staggered_backreaction_green_closure.py`](../scripts/frontier_staggered_backreaction_green_closure.py)
comparison and asserts the following bounded facts:

- `resistance_yukawa` is the best holdout-aware map in the frozen comparison.
- Raw cycle-bearing gap improves by more than `2.5x` over screened Poisson.
- Raw holdout gap is below `2e-2`.
- Source-linearity, two-body additivity, TOWARD, and norm checks remain tight.
- Calibrated holdout gap remains large, so the old clean calibrated-transfer
  claim is not restored.
- Cycle-bearing self-gap remains open, so endogenous refresh is still a seam.

Current live readout:

```text
best map: resistance_yukawa
raw cycle-gap improvement over screened Poisson: 2.81x
raw holdout gap: 1.534e-02
calibrated holdout gap remains large: 5.371e-01
cycle-bearing self-gap remains open: 1.339e-01
ASSERTIONS: PASS
```

## Claim Boundary

This packet supports only a finite bounded comparison on the current
staggered graph-Green runner. It does not claim:

- the archived near-order-of-magnitude cycle closure;
- clean calibrated holdout transfer;
- endogenous self-refresh closure;
- a continuum backreaction theorem;
- physical gravitational closure;
- effective retained status before independent audit.

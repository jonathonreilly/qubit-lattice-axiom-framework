---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Green-Closure Note

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner graph-Green boundary.
**Runner:**
[`scripts/frontier_staggered_backreaction_green_closure.py`](../scripts/frontier_staggered_backreaction_green_closure.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_green_closure.txt`](../logs/runner-cache/frontier_staggered_backreaction_green_closure.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The live runner supports `resistance_yukawa` as the best current
holdout-aware map in the frozen comparison. It preserves the source-linearity,
additivity, TOWARD, and norm checks, improves the raw cycle-bearing gap, and
has a small raw holdout gap. It does not support the archived calibrated
holdout closeout.

Wrapper-asserted facts:

- promoted map: `resistance_yukawa`;
- raw cycle-bearing mean gap: `3.425e-01`;
- raw improvement factor over screened Poisson: `2.81x`;
- raw holdout gap: `1.534e-02`;
- calibrated holdout gap for the promoted map: `5.371e-01`.

## Boundary

The live result keeps a graph-native Green map as a useful source-sector lead,
but the calibrated holdout caveat and self-gap remain open.

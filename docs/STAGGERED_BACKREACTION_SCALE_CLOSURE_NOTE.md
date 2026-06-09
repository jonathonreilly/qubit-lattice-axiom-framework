---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Scale-Closure Note

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner scale-normalization boundary.
**Runner:**
[`scripts/frontier_staggered_backreaction_scale_closure.py`](../scripts/frontier_staggered_backreaction_scale_closure.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_scale_closure.txt`](../logs/runner-cache/frontier_staggered_backreaction_scale_closure.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The current scale-closure runner supports a material calibrated cycle-bearing
gap reduction, but not the archived near-closure or a universal scale law.

Wrapper-asserted facts:

- best map: `invheat_b3p00`;
- fitted gain: `0.621`;
- raw cycle gap: `4.314e-01`;
- calibrated cycle gap: `2.053e-01`;
- improvement factor: `4.69x`;
- best holdout gap: `7.249e+00`;
- best-map source-response `R^2` mean: `0.9945`.

## Boundary

The live row supports only a cycle-bearing calibrated reduction with severe
holdout divergence. It does not close a universal source-to-field scale.

---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Capture-Closure Note

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner capture-closure boundary.
**Runner:**
[`scripts/frontier_staggered_backreaction_capture_closure_harness.py`](../scripts/frontier_staggered_backreaction_capture_closure_harness.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt`](../logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The current capture-closure harness preserves both cycle-bearing `9/9`
batteries and improves the cycle and holdout force gaps by about a factor of
two. It does not support the archived near-capture or larger improvement
factors.

Wrapper-asserted facts:

- cycle battery scores: `[9, 9]`;
- cycle mean gap: `9.828e-01 -> 4.734e-01`;
- cycle improvement factor: `2.08x`;
- holdout gap: `9.191e-01 -> 4.559e-01`;
- holdout improvement factor: `2.02x`.

## Boundary

The live result supports a real but limited endogenous closure improvement.
It is not a retained near-capture of the external-kernel force scale and not a
full self-gravity closure.

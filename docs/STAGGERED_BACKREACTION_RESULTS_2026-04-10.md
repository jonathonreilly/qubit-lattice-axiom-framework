---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Prototype Results

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner prototype boundary; no audit-status movement
claimed.
**Runner:**
[`scripts/frontier_staggered_backreaction_prototype.py`](../scripts/frontier_staggered_backreaction_prototype.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_prototype.txt`](../logs/runner-cache/frontier_staggered_backreaction_prototype.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The live prototype still supports exact zero-source reduction, exact two-body
additivity, TOWARD force sign, and one-step endogenous TOWARD behavior across
the three tested graph families. The current cache does not support the archived
all-family machine-precision linearity or frozen force table.

Current cache facts asserted by the wrapper:

- source-response linearity: `1/3` families with `R^2 > 0.99`;
- force gap: mean `9.353e-01`, max `9.624e-01`;
- self-update gap: mean `2.887e-01`, max `3.953e-01`;
- one-step endogenous backreaction: `3/3` families TOWARD.

## Boundary

This is not a self-gravity closure. It is a current bounded prototype packet
showing that source-generated fields preserve the sign/control battery while
leaving a large force-scale gap on the cycle-bearing families.

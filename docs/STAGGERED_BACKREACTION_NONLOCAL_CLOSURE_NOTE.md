---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Nonlocal Closure Note

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner nonlocal-source boundary.
**Runner:**
[`scripts/frontier_staggered_backreaction_nonlocal_closure.py`](../scripts/frontier_staggered_backreaction_nonlocal_closure.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_nonlocal_closure.txt`](../logs/runner-cache/frontier_staggered_backreaction_nonlocal_closure.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The current fractional-Green source sector improves the calibrated
cycle-bearing rows at `alpha=0.40` while preserving TOWARD, linearity,
additivity, and norm checks. The layered holdout remains poor and shell/spectral
readout still shows low-mode bias.

Wrapper-asserted facts:

- baseline calibrated cycle gap: `3.881e-02` at `alpha=1.00`;
- best calibrated cycle gap: `1.620e-02` at `alpha=0.40`;
- improvement factor: `2.40x`;
- best layered holdout gap: `7.035e-01`;
- shell-fit `R^2`: `0.7857` and `0.8291` on the two cycle-bearing families.

## Boundary

This is not a nonlocal closure theorem. The live result is a cycle-row
improvement with a failing holdout and remaining spectral-shape bias.

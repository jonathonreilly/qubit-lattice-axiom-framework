---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Staggered Backreaction Iterative Source-Mapping Note

**Date:** 2026-06-08 live replacement for the archived 2026-04-10 note
**Status:** bounded current-runner source-mapping boundary.
**Runner:**
[`scripts/frontier_staggered_backreaction_iterative.py`](../scripts/frontier_staggered_backreaction_iterative.py)
**Runner cache:**
[`logs/runner-cache/frontier_staggered_backreaction_iterative.txt`](../logs/runner-cache/frontier_staggered_backreaction_iterative.txt)
**Assertion wrapper:**
[`scripts/staggered_backreaction_live_packet.py`](../scripts/staggered_backreaction_live_packet.py)

## Current Safe Claim

The current runner finds no clean cycle-bearing closure from linear source
preconditioning. All rows keep TOWARD sign and stability, but the best current
map is `invheat_b3p00`, with much larger self-update failure than the archived
note froze.

Wrapper-asserted facts:

- baseline cycle-bearing mean gap: `9.618e-01`;
- best cycle-bearing mean gap: `4.314e-01` at `invheat_b3p00`;
- gap improvement factor: `2.23x`;
- best-map self-gap mean: `1.581e+01`;
- TOWARD and norm-stability checks remain intact in the current cache.

## Boundary

This is not a closure theorem. The live result says linear source
preconditioning helps the force-scale gap but does not deliver a stable
endogenous self-refresh.

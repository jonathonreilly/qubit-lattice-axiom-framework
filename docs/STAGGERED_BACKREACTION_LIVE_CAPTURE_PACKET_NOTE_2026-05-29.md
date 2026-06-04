# Staggered Backreaction Live Capture Packet

**Date:** 2026-05-29
**Date of live-readout repair:** 2026-06-04
**Status:** bounded-support positive packet; proposed for independent audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/staggered_backreaction_live_capture_packet_check.py`](../scripts/staggered_backreaction_live_capture_packet_check.py)

## Purpose

The archived staggered capture-closure note is failed because its numerical
force/gap/gain table is stale against the live runner. This packet does not
restore the stale table. It records the narrower positive surface that the
current live capture-closure harness supports.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## Live Finite Result

The runner imports the current
[`scripts/frontier_staggered_backreaction_capture_closure_harness.py`](../scripts/frontier_staggered_backreaction_capture_closure_harness.py)
and asserts:

- both cycle-bearing batteries score `9/9`;
- cycle mean gap improves from `9.828e-01` to `4.734e-01`;
- the cycle improvement factor is `2.08x`;
- cycle mean linearity remains above `0.99`, with two-body residual below
  numerical tolerance;
- the layered holdout gap improves from `9.191e-01` to `4.559e-01`;
- the holdout improvement factor is `2.02x`;
- zero-source, TOWARD, and norm guardrails survive.

Current live readout:

```text
cycle battery scores: [9, 9]
cycle mean gap: 9.828e-01 -> 4.734e-01
cycle gap improvement factor: 2.08x
cycle mean R2: 0.996306; two-body max <1e-12
holdout gap: 9.191e-01 -> 4.559e-01 (2.02x)
ASSERTIONS: PASS
```

## Claim Boundary

This packet supports only a finite bounded comparison on the current
staggered capture-closure runner. It does not claim:

- the archived stale force/gap/gain table;
- exact force-scale closure;
- clean calibrated transfer;
- continuum backreaction;
- physical gravitational closure;
- effective retained status before independent audit.

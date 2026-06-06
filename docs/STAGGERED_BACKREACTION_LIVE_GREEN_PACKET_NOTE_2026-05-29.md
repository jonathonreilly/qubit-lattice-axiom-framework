# Staggered Backreaction Live Green Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit;
no effective grade is assigned here.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/staggered_backreaction_live_green_packet_check.py`](../scripts/staggered_backreaction_live_green_packet_check.py)
**Cached runner output:** [`logs/runner-cache/staggered_backreaction_live_green_packet_check.txt`](../logs/runner-cache/staggered_backreaction_live_green_packet_check.txt)
**Source packet verifier:** [`scripts/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.py`](../scripts/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.py)
(SUMMARY: STAGGERED GREEN SOURCE PACKET PASS=40 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.txt`](../logs/runner-cache/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.txt)
**Source packet verifier JSON:** [`outputs/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.json`](../outputs/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.json)

## Purpose

The archived staggered Green-closure note is failed because its numerical
table is stale against the live runner. This packet does not restore the old
near-order-of-magnitude closure or clean calibrated-holdout claim. It records
the narrower positive surface that the current live runner supports.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## 2026-06-04 Source Packet Exposure Repair

The current audit blocker asks for the complete source of
`scripts/frontier_staggered_backreaction_prototype.py` and a rerun of the
restricted packet. The source packet is now explicit:

- Restricted packet checker: [`scripts/staggered_backreaction_live_green_packet_check.py`](../scripts/staggered_backreaction_live_green_packet_check.py)
- Restricted packet cache: [`logs/runner-cache/staggered_backreaction_live_green_packet_check.txt`](../logs/runner-cache/staggered_backreaction_live_green_packet_check.txt)
- Green-closure source: [`scripts/frontier_staggered_backreaction_green_closure.py`](../scripts/frontier_staggered_backreaction_green_closure.py)
- Green-closure cache: [`logs/runner-cache/frontier_staggered_backreaction_green_closure.txt`](../logs/runner-cache/frontier_staggered_backreaction_green_closure.txt)
- Prototype helper source: [`scripts/frontier_staggered_backreaction_prototype.py`](../scripts/frontier_staggered_backreaction_prototype.py)
- Prototype helper cache: [`logs/runner-cache/frontier_staggered_backreaction_prototype.txt`](../logs/runner-cache/frontier_staggered_backreaction_prototype.txt)

The source packet verifier above checks that every path is linked from this
note, that the packet checker imports the Green-closure source, that the
Green-closure source imports the prototype helper, that the load-bearing helper
functions are present in the complete source files, and that the caches are
SHA-fresh. This does not set an audit verdict; it makes the same bounded packet
reauditable with the missing helper source exposed.

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
- Cycle-bearing self-gap remains open, so endogenous refresh is still an open
  boundary.

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
- audit-derived effective status before independent audit.

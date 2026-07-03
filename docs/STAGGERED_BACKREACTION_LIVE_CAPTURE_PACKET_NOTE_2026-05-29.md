# Staggered Backreaction Live Capture Packet

**Date:** 2026-05-29
**Date of live-readout repair:** 2026-06-04
**Status:** bounded-support positive packet; proposed for independent audit,
not audit-effective.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/staggered_backreaction_live_capture_packet_check.py`](../scripts/staggered_backreaction_live_capture_packet_check.py)
**Cached runner output:** [`logs/runner-cache/staggered_backreaction_live_capture_packet_check.txt`](../logs/runner-cache/staggered_backreaction_live_capture_packet_check.txt)
**Source packet verifier:** [`scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py`](../scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py)
(SUMMARY: STAGGERED CAPTURE SOURCE PACKET PASS=91 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.txt)
**Source packet verifier JSON:** [`outputs/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.json`](../outputs/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.json)

## Purpose

The archived staggered capture-closure note is failed because its numerical
force/gap/gain table is stale against the live runner. This packet does not
restore the stale table. It records the narrower positive surface that the
current live capture-closure harness supports.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## 2026-06-06 Source Packet Exposure Repair

The current audit blocker asks for the complete untruncated source of
`scripts/frontier_staggered_backreaction_prototype.py` and a rerun of the
restricted packet, including the transitive helper chain. The source packet is
now explicit:

- Restricted packet checker: [`scripts/staggered_backreaction_live_capture_packet_check.py`](../scripts/staggered_backreaction_live_capture_packet_check.py)
- Restricted packet cache: [`logs/runner-cache/staggered_backreaction_live_capture_packet_check.txt`](../logs/runner-cache/staggered_backreaction_live_capture_packet_check.txt)
- Capture-closure harness source: [`scripts/frontier_staggered_backreaction_capture_closure_harness.py`](../scripts/frontier_staggered_backreaction_capture_closure_harness.py)
- Capture-closure harness cache: [`logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt`](../logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt)
- Iterative source-map source: [`scripts/frontier_staggered_backreaction_iterative.py`](../scripts/frontier_staggered_backreaction_iterative.py)
- Iterative source-map cache: [`logs/runner-cache/frontier_staggered_backreaction_iterative.txt`](../logs/runner-cache/frontier_staggered_backreaction_iterative.txt)
- Cycle-battery source: [`scripts/frontier_staggered_cycle_battery.py`](../scripts/frontier_staggered_cycle_battery.py)
- Cycle-battery cache: [`logs/runner-cache/frontier_staggered_cycle_battery.txt`](../logs/runner-cache/frontier_staggered_cycle_battery.txt)
- Layered holdout source: [`scripts/frontier_staggered_layered_backreaction.py`](../scripts/frontier_staggered_layered_backreaction.py)
- Layered holdout cache: [`logs/runner-cache/frontier_staggered_layered_backreaction.txt`](../logs/runner-cache/frontier_staggered_layered_backreaction.txt)
- Prototype helper source: [`scripts/frontier_staggered_backreaction_prototype.py`](../scripts/frontier_staggered_backreaction_prototype.py)
- Prototype helper cache: [`logs/runner-cache/frontier_staggered_backreaction_prototype.txt`](../logs/runner-cache/frontier_staggered_backreaction_prototype.txt)

The source packet verifier above checks that every path is linked from this
note, that the packet checker imports the capture harness, that the capture
harness and its transitive helpers contain load-bearing source markers such as
`_source_density`, `_solve_phi`, `_build_hamiltonian`, and `_force_from_phi`,
and that all listed caches are SHA-fresh. This does not set an audit verdict; it
makes the bounded packet reauditable with the missing helper source exposed.
The primary packet checker now also prints `PROTOTYPE_SOURCE_PACKET` and checks
the prototype helper's untruncated source markers and SHA-fresh cache directly
inside the primary stdout packet.

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

Current source-packet output:

```text
SUMMARY: STAGGERED CAPTURE SOURCE PACKET PASS=91 FAIL=0
```

## Claim Boundary

This packet supports only a finite bounded comparison on the current
staggered capture-closure runner. It does not claim:

- the archived stale force/gap/gain table;
- exact force-scale closure;
- clean calibrated transfer;
- continuum backreaction;
- physical gravitational closure;
- audit-effective status before independent audit.

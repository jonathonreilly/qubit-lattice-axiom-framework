# Causal Propagating Field Live Packet Note

**Date:** 2026-06-05
**Status:** bounded-support live packet; independent audit required before any effective status change
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/causal_propagating_field.py`](../scripts/causal_propagating_field.py)
**Cached runner output:** [`logs/runner-cache/causal_propagating_field.txt`](../logs/runner-cache/causal_propagating_field.txt)
**Source packet verifier:** [`scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py`](../scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py)
(SUMMARY: CAUSAL PROPAGATING FIELD SOURCE PACKET PASS=30 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt)
**Source packet verifier JSON:** [`outputs/causal_propagating_field_source_packet_manifest_2026_06_05.json`](../outputs/causal_propagating_field_source_packet_manifest_2026_06_05.json)
**Re-audit bridge:** [`docs/CAUSAL_PROPAGATING_FIELD_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md`](CAUSAL_PROPAGATING_FIELD_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md)
with verifier
[`scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py`](../scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py).

## Scope

This note repairs the live support surface for the archived
`causal_propagating_field_note` row. It does not unarchive the old note, edit
the audit ledger, or restore the stale `0.63 / 0.45` positive table.
The 2026-06-18 re-audit bridge makes that split explicit: the archived row is
historical failed evidence, while this live packet is the bounded finite replay
surface to inspect if the lane is re-audited.

The current packet is a finite configured replay:

- center grown family: `drift = 0.20`, `restore = 0.70`
- helper source: [`scripts/evolving_network_prototype_v6.py`](../scripts/evolving_network_prototype_v6.py)
- helper cache: [`logs/runner-cache/evolving_network_prototype_v6.txt`](../logs/runner-cache/evolving_network_prototype_v6.txt)
- seeds: `0, 1, 2, 3, 4, 5`
- source layer: `8`
- field strengths: `1e-5`, `5e-5`, `1e-4`
- field cases: zero, instantaneous, forward-only, dynamic `c=1.0`, dynamic `c=0.5`

This packet does not claim a physical wave speed, derived field carrier,
self-consistent retarded field, or cross-family portability law.

## Live Result

The primary runner now executes and asserts the current finite facts:

```text
   strength     inst delta        forward   fwd/inst  dyn1/inst  dyn0.5/inst
----------------------------------------------------------------------------------------------------------------
    1.0e-05 +5.841e-08+/-1.4e-07 +3.902e-08+/-3.6e-08      0.668      1.456        0.939
    5.0e-05 +2.921e-07+/-6.8e-07 +1.951e-07+/-1.8e-07      0.668      1.456        0.938
    1.0e-04 +5.845e-07+/-1.4e-06 +3.903e-07+/-3.6e-07      0.668      1.456        0.938
```

The asserted safe read is:

```text
SAFE READ
  [PASS] exact zero-source control
  [PASS] instantaneous response scales with 5x strength
  [PASS] instantaneous response scales with 2x strength
  [PASS] forward ratio is stable across strengths
  [PASS] dynamic c=1 ratio is stable across strengths
  [PASS] dynamic c=0.5 ratio is stable across strengths
  [PASS] forward-only center ratio remains near 2/3
  [PASS] dynamic c=1 is distinct from forward-only
  [PASS] dynamic c=0.5 is not the archived 0.45 row
  [PASS] dynamic c=1 response exceeds dynamic c=0.5
ASSERTIONS: PASS
```

## Boundary Against The Archived Table

The old archived note claimed dynamic `c=1` approximately matched the
forward-only row and dynamic `c=0.5` gave a ratio near `0.45`. The live runner
does not reproduce that table:

- current forward-only ratio: `0.668`
- current dynamic `c=1` ratio: `1.456`
- current dynamic `c=0.5` ratio: `0.938`

The live bounded conclusion is therefore not the old positive claim.
The safe statement is that, in this configured center-family runner, finite
cone fields produce stable strength-independent proxy ratios, and the archived
`0.45` dynamic row is stale.

## Source Packet Exposure

The source-packet verifier checks that this note links the primary runner,
primary cache, helper source, helper cache, manifest runner, manifest cache,
and manifest JSON. It also checks that the helper source exposes the
load-bearing growth, propagation, and centroid routines and that the primary
and helper caches are SHA-fresh.

## Boundaries

This packet does not claim:

- the archived `0.63 / 0.45` table;
- geometry independence;
- cross-family portability;
- a physical field-speed measurement;
- a self-consistent retarded-potential field equation;
- a derived framework carrier/readout theorem;
- an audit-derived effective status before independent audit.

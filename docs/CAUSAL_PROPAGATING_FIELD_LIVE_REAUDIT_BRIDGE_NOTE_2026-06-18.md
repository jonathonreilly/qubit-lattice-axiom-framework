# Causal Propagating Field Live Re-Audit Bridge

**Date:** 2026-06-18
**Claim type:** meta
**Bridge role:** source-side dispatch/readiness bridge; independent audit owns
any verdict or effective-status propagation.
**Archived row:** `causal_propagating_field_note`
**Live dispatch target:** `causal_propagating_field_live_packet_note_2026-06-05`
**Dispatch sidecar:**
[`docs/audit/data/causal_field_live_reaudit_queue_2026-06-18.json`](audit/data/causal_field_live_reaudit_queue_2026-06-18.json)
**Primary runner:**
[`scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py`](../scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py)

## Result

The archived `causal_propagating_field_note` failed correctly as a retained
positive claim. Its historical `0.63 / 0.45` table, geometry-independence
language, and physical field-speed language are not live evidence.

The source-side repair is a different, narrower re-audit target:

- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
- [`scripts/causal_propagating_field.py`](../scripts/causal_propagating_field.py)
- [`logs/runner-cache/causal_propagating_field.txt`](../logs/runner-cache/causal_propagating_field.txt)
- [`scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py`](../scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py)
- [`logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt)
- [`outputs/causal_propagating_field_source_packet_manifest_2026_06_05.json`](../outputs/causal_propagating_field_source_packet_manifest_2026_06_05.json)

That live packet repairs the audit blocker at the source-artifact level: the
primary runner now executes, rebuilds the center grown family, computes the
zero, instantaneous, forward-only, dynamic `c=1.0`, and dynamic `c=0.5` cases,
sweeps three field strengths over seeds `0..5`, and archives deterministic
output.

## Safe Re-Audit Scope

The live re-audit target is only this bounded finite configured replay:

- center grown family with `drift = 0.20`, `restore = 0.70`;
- source layer `8`;
- field strengths `1e-5`, `5e-5`, `1e-4`;
- six seeds;
- exact zero-source control;
- linear strength scaling of the instantaneous row;
- stable ratio readouts across the three tested strengths;
- forward-only ratio near `2/3` on the configured center family;
- current dynamic-cone ratios distinct from the archived table.

The primary cache reports:

```text
current live c=1 ratio: 1.456
current live c=0.5 ratio: 0.938
current live forward ratio: 0.668
ASSERTIONS: PASS
```

## Boundary

This bridge does not edit audit results, re-open the archived note as
authority, or restore the archived `0.63 / 0.45` table. In particular, it
does not restore the archived positive table as live evidence.
The dispatch sidecar is target-selection metadata only and is not evidence for
the live packet.

It does not claim:

- geometry independence;
- cross-family portability;
- a physical wave-speed measurement;
- a self-consistent retarded-potential field equation;
- a derived framework carrier/readout theorem;
- a retained or retained-bounded effective status.

The correct source-side reading is:

> the old archived row remains a failed historical positive, while the live
> packet is now an executable bounded finite replay that can be independently
> re-audited under its narrowed claim scope.

## Verification

Run:

```bash
python3 scripts/causal_propagating_field.py
python3 scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py
python3 scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py
```

Expected bridge result:

```text
SUMMARY: CAUSAL FIELD LIVE REAUDIT BRIDGE PASS=39 FAIL=0
```

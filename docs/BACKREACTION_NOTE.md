# Backreaction Live Threshold Wrapper

**Date:** 2026-04-05; live-source repair 2026-06-08
**Status:** bounded-support live threshold packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary packet note:** [`POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md`](POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md)
**Primary runner:** [`scripts/backreaction_poisson_live_threshold_check.py`](../scripts/backreaction_poisson_live_threshold_check.py)
**Primary runner cache:** [`logs/runner-cache/backreaction_poisson_live_threshold_check.txt`](../logs/runner-cache/backreaction_poisson_live_threshold_check.txt)
**Source packet verifier:** [`scripts/backreaction_poisson_live_threshold_source_packet_manifest_2026_06_04.py`](../scripts/backreaction_poisson_live_threshold_source_packet_manifest_2026_06_04.py)

## Purpose

This note restores a current source surface for the legacy claim id
`backreaction_note`. The archived note failed because its quantitative
threshold table and `G_crit ~= 0.011` claim are stale relative to the live
Poisson self-gravity harness.

The live packet does not restore the old threshold claim. It keeps only the
bounded finite grid certified by
[`POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md`](POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md).

## Live Claim

On the current finite Poisson self-gravity grid

```text
G = 0.000, 0.001, 0.005, 0.010, 0.011, 0.012, 0.020, 0.050, 0.100
```

the live runner certifies:

```text
baseline external-field delta = +1.073461e-02 TOWARD
first sub-unit escape on this grid: G=0.05
TOWARD deflection is preserved through G=0.100 on this grid
ASSERTIONS: PASS
```

The source packet verifier certifies that the primary runner, helper source,
runner cache, and helper cache are linked and fresh:

```text
SUMMARY: POISSON BACKREACTION SOURCE PACKET PASS=27 FAIL=0
```

## Boundary

This row does not claim:

- the archived `G_crit ~= 0.011` threshold;
- a smooth monotone collapse law;
- convergence for every listed `G`;
- continuum horizon formation;
- physical Schrodinger-Newton closure;
- retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/poisson-self-consistency-stale-runners-2026-04-30/BACKREACTION_NOTE.md`](../archive_unlanded/poisson-self-consistency-stale-runners-2026-04-30/BACKREACTION_NOTE.md).

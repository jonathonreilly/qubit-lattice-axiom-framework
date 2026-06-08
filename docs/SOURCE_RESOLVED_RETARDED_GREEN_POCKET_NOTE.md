# Source-Resolved Retarded Green Pocket Live Packet

**Date:** 2026-04-05; live-source repair 2026-06-08
**Status:** bounded-support finite-lag pocket; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/source_resolved_retarded_green_pocket.py`](../scripts/source_resolved_retarded_green_pocket.py)
**Primary runner cache:** [`logs/runner-cache/source_resolved_retarded_green_pocket.txt`](../logs/runner-cache/source_resolved_retarded_green_pocket.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`source_resolved_retarded_green_pocket_note`. The archived note failed because
the runner's `ret/same` column was actually `ret/inst`, and the note froze that
mislabeled ratio.

The repaired runner now prints both ratios separately and asserts the intended
finite-lag bounded packet.

## Live Claim

On the compact exact `h=0.25`, `W=3`, `L=6` lattice with the fixed source
cluster and source strengths `0.001, 0.002, 0.004, 0.008`, the retarded-like
finite-lag rule satisfies:

- zero-source same-site and retarded shifts are exactly zero;
- all four retarded rows keep the `TOWARD` sign;
- instantaneous, same-site, and retarded-like fitted source-strength exponents
  are all approximately one;
- `ret - same` is positive on every sampled row;
- true `ret/same` is small, about `1.026`, not the old mislabeled `~1.20`;
- support fraction is unchanged, while detector `N_eff` increases slightly.

Current bounded read:

```text
true ret/same range: 1.026 .. 1.026
ASSERTIONS: PASS
```

## Boundary

This row claims only a small finite-lag correction in a compact exact-lattice
pocket. It does not claim a full retarded field equation, support-fraction
broadening, continuum behavior, or effective retained status before independent
audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/source-resolved-green-stale-runners-2026-04-30/SOURCE_RESOLVED_RETARDED_GREEN_POCKET_NOTE.md`](../archive_unlanded/source-resolved-green-stale-runners-2026-04-30/SOURCE_RESOLVED_RETARDED_GREEN_POCKET_NOTE.md).

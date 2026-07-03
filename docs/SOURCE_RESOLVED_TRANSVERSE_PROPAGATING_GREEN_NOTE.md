# Source-Resolved Transverse Propagating Green Boundary Live Packet

**Date:** 2026-04-05; live-source repair 2026-06-08
**Status:** bounded-support negative-boundary packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/source_resolved_transverse_propagating_green.py`](../scripts/source_resolved_transverse_propagating_green.py)
**Primary runner cache:** [`logs/runner-cache/source_resolved_transverse_propagating_green.txt`](../logs/runner-cache/source_resolved_transverse_propagating_green.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`source_resolved_transverse_propagating_green_note`. The archived note failed
because the old positive transverse-correction table is stale and the runner's
`trans/same` column was actually `trans/inst`.

The repaired runner now prints both ratios separately and asserts the current
negative-boundary packet.

## Live Claim

On the compact exact `h=0.25`, `W=3`, `L=6` lattice with the fixed source
cluster and source strengths `0.001, 0.002, 0.004, 0.008`, the transverse
propagating rule satisfies:

- zero-source same-site and transverse shifts are exactly zero;
- all four transverse rows keep the `TOWARD` sign;
- instantaneous, same-site, and transverse fitted source-strength exponents
  are all approximately one;
- `trans - same` is negative on every sampled row;
- true `trans/same` is about `0.990`, not the old mislabeled `~1.16`;
- support fraction is unchanged.

Current bounded read:

```text
true trans/same range: 0.990 .. 0.990
ASSERTIONS: PASS
```

## Boundary

This row no longer claims a positive transverse correction relative to same-site
memory. It is a bounded negative boundary for that positive-correction route in
this compact pocket. It does not claim a full propagating field theory,
continuum behavior, or effective retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/source-resolved-green-stale-runners-2026-04-30/SOURCE_RESOLVED_TRANSVERSE_PROPAGATING_GREEN_NOTE.md`](../archive_unlanded/source-resolved-green-stale-runners-2026-04-30/SOURCE_RESOLVED_TRANSVERSE_PROPAGATING_GREEN_NOTE.md).

# Fifth Family Radial F~M Transfer Live Packet

**Date:** 2026-04-06; live-source repair 2026-06-08
**Status:** bounded-support positive packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py`](../scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py)
**Primary runner cache:** [`logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`fifth_family_radial_fm_transfer_note`. The old archived note failed audit
because the runner could not import the radial helper API and because the base
radial-family packet was not current.

The base finite packet is now
[`FIFTH_FAMILY_RADIAL_NOTE.md`](FIFTH_FAMILY_RADIAL_NOTE.md), with the fuller
manifest in
[`FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md`](FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md).

## Live Claim

On the two historically cited positive radial-shell rows,

- `drift = 0.05`, `seed = 0`
- `drift = 0.30`, `seed = 1`

the live weak-field mass-scaling replay gives near-unit `F~M`:

```text
passed rows: 2/2
mean F~M among passes: 0.999439
ASSERTIONS: PASS
```

This is a finite transfer check inside the same no-restore grown-slice harness.
It says the sampled radial-shell positives preserve weak-field linearity under
the declared source-strength doubling test.

## Boundary

This note does not claim a family-wide F~M law, continuum transfer theorem,
physical mass observable, or retained status before independent audit. It
depends on the bounded radial-shell packet in `FIFTH_FAMILY_RADIAL_NOTE.md`.

The archived stale note remains historical provenance only:
[`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_FM_TRANSFER_NOTE.md).

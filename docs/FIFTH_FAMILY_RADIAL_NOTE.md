# Fifth Family Radial Live Packet

**Date:** 2026-04-06; live-source repair 2026-06-08
**Status:** bounded-support positive packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/FIFTH_FAMILY_RADIAL_SWEEP.py`](../scripts/FIFTH_FAMILY_RADIAL_SWEEP.py)
**Primary runner cache:** [`logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`fifth_family_radial_note` after the archived note was moved under
`archive_unlanded/fifth-family-stale-runners-2026-04-30/` because the old
helper imports were stale.

The helper API is now live through
[`scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py`](../scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py),
and the broader repaired packet is recorded in
[`FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md`](FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md).
This row should be re-audited as a finite sampled packet, not as a family-wide
theorem.

## Live Claim

In the no-restore grown-slice harness, the radial-shell fifth-family
connectivity rule has two historically cited sampled rows satisfying the
declared finite gates:

- `drift = 0.05`, `seed = 0`
- `drift = 0.30`, `seed = 1`

The gates are:

- exact zero-source baseline;
- exact same-point `+1/-1` neutral cancellation;
- positive-source and negative-source sign orientation;
- weak-source exponent near one.

The runner also reports the interior boundary row:

- `drift = 0.20`, `seed = 0`

At that row, exact zero and neutral controls remain clean, but sign orientation
flips (`plus < 0`, `minus > 0`). This is a structural orientation boundary, not
a control leak.

## Runner Certificate

Current cached runner output:

```text
passed rows: 2/3
drift coverage: [0.05, 0.3]
mean exponent among passes: 0.999439
ASSERTIONS: PASS
```

The paired basin packet additionally checks ten `(drift, seed)` rows and records
four positive sampled rows:

```text
passed rows: 4/10
drift coverage: [0.05, 0.1, 0.3]
mean exponent among passes: 0.999495
ASSERTIONS: PASS
```

## Boundary

This note claims only a bounded finite sampled radial-shell packet. It does not
claim family-wide survival, continuum or architecture universality, a physical
mass-observable derivation, or retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md).

# Claim Status Certificate

## Current Claim Surface

Actual current-surface status:

```text
bounded-support artifact repair
```

This PR does not promote the 4pi row. It repairs the runner/source/cache mismatch named by audit.

## Repaired

- Replaces stale minimal-block demotion markers with the current `MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06` retained-no-go wording.
- Updates the 4pi source note's source table to consume the landed statuses:
  - temporal count packet: `retained_bounded`
  - minimal-block readout selection: `retained_no_go`
- Refreshes the primary cache from `PASS=59 FAIL=3` / nonzero exit to `PASS=62 FAIL=0` / `status: ok`.

## Still Open

- Static-source readout I1.
- Alpha convention I2.
- Cl3 normalization I3.
- Per-mode dressing/value-gate P3.

Those residuals remain explicitly open and unaudited in the source note.

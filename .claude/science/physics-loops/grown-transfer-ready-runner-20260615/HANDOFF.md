# Handoff

This PR attaches the existing grown-transfer live packet verifier to `GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md`.

Local regeneration confirmed the row's primary runner becomes:

```text
scripts/grown_transfer_basin_live_packet.py
```

with helper:

```text
scripts/runner_cache.py
```

The runner cache was refreshed because the verifier checks the repair note text and the note changed. Generated audit/publication outputs were restored and are not included.

The branch does not broaden the finite row-grid claim and does not change audit verdicts.

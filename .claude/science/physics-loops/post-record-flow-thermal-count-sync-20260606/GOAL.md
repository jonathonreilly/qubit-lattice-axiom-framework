# Goal

Repair the direct blocker on `post_record_flow_thermal_stable_setting_certificate_2026-06-06`.

The audit failed because the note and runner asserted stale current-snapshot
counts. The runner itself recomputes the live rows, so the repair is to sync
the expected constants and note prose to the current ledger snapshot, refresh
the cache, and leave the row ready for independent re-audit.

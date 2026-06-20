# Opportunity Queue

Current block closed:

1. `qcd_low_energy_running_bridge_note_2026-05-01`
   - before: `Type: bounded_theorem` present, `Claim type:` missing.
   - after: source-authored `Claim type: bounded_theorem` plus a runner
     manifest check for canonical metadata and audit authority.
   - queue state: ready, zero-based queue position 8 after pipeline
     regeneration, no serialized `queue_index` field in the JSON entry.

Next action:

Refresh from current `origin/main` and select another ready source note whose
audit row is blocked or degraded by missing/noncanonical source metadata.


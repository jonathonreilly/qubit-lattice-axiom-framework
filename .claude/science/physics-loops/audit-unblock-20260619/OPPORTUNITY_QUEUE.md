# Opportunity Queue

Current block closed:

1. `dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16`
   - before: `Type: open_gate` present, `Claim type:` missing, no source-local
     audit authority line.
   - after: source-authored `Claim type: open_gate` and independent audit
     authority, with runner guard.
   - queue state: ready, zero-based queue position 11 after pipeline
     regeneration, no serialized `queue_index` field in the JSON entry.

Next action:

Refresh from current `origin/main` and select another ready source note whose
audit row is blocked or degraded by missing/noncanonical source metadata.


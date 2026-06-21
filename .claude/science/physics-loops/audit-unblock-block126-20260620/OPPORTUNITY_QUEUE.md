# Opportunity Queue

## Current Block

1. `dm_neutrino_source_surface_perturbative_uniqueness_theorem_note_2026-04-17`
   - Action: refresh missing runner stdout in canonical cache.
   - Movement: supports future audit review by replacing empty `ok` evidence with the full
     `PASS=46 FAIL=0` transcript.
   - Status after pipeline: open; unaudited; `queue_ready: false`; still dependency-blocked.

## Next Candidates

1. Scan `runner_breakage_inventory.json` and live-probe high-fanout pending rows whose old
   broken-runner records are stale.
2. Prefer candidates where a small cache/source repair changes a row from runner-blocked to
   reviewable without touching audit verdict surfaces.
3. Skip any candidate that requires a human science judgment or audit verdict; record it as an
   audit-side dependency and pivot.

## Deprioritized For This Block

- Hand-authored audit queue, ledger, or publication status edits.
- Publication-facing status surfaces.
- Runners that already have complete, current cache evidence.

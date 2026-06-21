# Opportunity Queue

## Current Block

1. `frozen_stars_rigorous_note`
   - Action: refresh missing runner stdout in canonical cache.
   - Movement: supports future audit review by replacing empty `ok` evidence with the full
     generated transcript.
   - Status after pipeline: open; unaudited; `queue_ready: false`; still dependency-blocked.
   - Scope: leaf; not load-bearing for retained-grade downstream chains.

## Next Candidates

1. Continue scanning for high/critical pending rows with stale, empty, or incomplete runner
   caches not already covered by PR #4496.
2. Prefer candidates where a small cache/source repair changes a row from runner-blocked to
   reviewable without touching audit verdict surfaces.
3. Skip any candidate that requires a human science judgment or audit verdict; record it as an
   audit-side dependency and pivot.

## Deprioritized For This Block

- Duplicate work on `dm_neutrino_source_surface_perturbative_uniqueness_theorem_note_2026-04-17`,
  already covered by PR #4496.
- Hand-authored audit queue, ledger, or publication status edits.
- Runners that already have complete, current cache evidence.

# Opportunity Queue

## Current Block

1. Meson OS transfer source-completeness repair
   - Direct blocker closure probability: high
   - Import count: artifact/source visibility only
   - Runner availability: existing primary runner, cache, and two source-packet
     manifests
   - Landability: narrow branch; no audit ledger edits

## Next Scan Targets

After this PR, rescan current `origin/main` conditional rows for remaining
artifact-completeness or compute-blocked lanes not already covered by open
review PRs. Prefer rows where the repair can expose an existing proof/runner
without narrowing the scientific claim.

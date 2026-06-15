# Opportunity Queue

1. `dm_neutrino_weak_vector_theorem_note_2026-04-15`
   - Critical retained-bounded row.
   - Existing exact runner passes.
   - Missing cache and parser-visible primary runner.
   - Implemented in this block.

2. Remaining no-runner rows with live scripts
   - Continue scanning after this PR and after currently open runner/cycle PRs
     land.
   - Skip meta/context notes whose scripts are downstream-fix diagnostics
     rather than primary claim verifiers.

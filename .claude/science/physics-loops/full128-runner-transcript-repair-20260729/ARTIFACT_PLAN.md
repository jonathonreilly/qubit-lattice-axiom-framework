# Artifact plan

1. Change the primary runner's passing-output policy without changing check predicates.
2. Emit the complete all-128 diagnostic and a compact terminal `SUMMARY_JSON`.
3. Refresh the source-bound runner cache.
4. Refresh note, runner, cache, and input-fingerprint fields in the receipt.
5. Validate transcript length, all 13 passes, audit requeue visibility, strict lint, and generated-output stripping.


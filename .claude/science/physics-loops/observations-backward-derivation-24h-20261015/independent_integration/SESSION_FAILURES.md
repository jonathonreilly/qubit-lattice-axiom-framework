# Actual failures and source movement

No failed run is counted as a successful final check. All owned calculations
had an external 120-second timeout; no timeout occurred and no owned job is
left running after completion.

1. `OWN_ATTEMPT01.json` preserves the exact initial checker source and hash.
   `independent_math_attempt01_stdout.txt` preserves 14 completed mathematical
   identities followed by the real `TypeError` from an unfactored positive
   inverse-weight integral. Its execution record reports exit 1 after
   0.9483914161100984 seconds. The factorable integral is
   `((a+w)^2-a^2)/2`, with positive `a,w`. The author accepted this as a helper
   interface limitation and repaired the sign guard. The final checker passes
   the original expression without caller preprocessing.

2. A temporary checker factored that expression at the call site. It completed
   the mathematics, but its expected note hash was stale after the author's
   claim-type metadata addition. It returned exit 1 after
   0.9928964166902006 seconds: 24 successful checks and one source-identity
   failure. `OWN_ATTEMPT02.json`, `independent_math_attempt02_evidence.json`,
   its stdout and execution record preserve this state. The within-run source
   stability check succeeded. This is a detected binding change, not a failed
   theorem. `NOTE_SOURCE_MOVEMENT_02.json` preserves its exact metadata delta.

The final checker removes the temporary caller-side factor and tests the
author's repaired implementation directly. It also contains the independent
reference-length checks added for the subsequent dimensional clarification.
The successful pre-dimensional checker and its receipts are preserved in
`pre_dimension/`; its source is stored losslessly as a JSON UTF-8 string.

The author had already preserved two earlier operational failures in canonical
output files: a `min` comparison of independently positive symbolic integrals,
then a bin interval whose endpoint ordering was not supplied. Their record
hashes, exact execution envelopes and verified embedded-source identities are
stored in `HISTORICAL_AUTHOR_FAILURES.json`. Those old programs were not rerun.
They are historical development evidence, not active runner results or cache
authority for the current milestone.

All source deltas and old checker sources are stored in JSON, preserving raw
UTF-8 content and hashes without creating raw diff files whose significant
context spaces would fail whitespace checks. Author source files were never
edited by this checker. No Git, audit, lock, runtime-ownership, model-setting,
network or external-application actions were performed.

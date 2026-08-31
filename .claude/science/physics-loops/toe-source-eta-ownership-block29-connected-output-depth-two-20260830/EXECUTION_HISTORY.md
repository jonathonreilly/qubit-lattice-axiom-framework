# Block29 execution history

No entry below carries a science inference unless it records a complete green
terminal bound to the named source and input fingerprint.

## Attempt A — wrapper identity rejection

- runner SHA-256:
  `5b032c62daedd05373ae2d2737986f06aaeef91f455e0d72ec1ad2142d42efc8`
- 25-input fingerprint:
  `d0e5559b1fc376ca5870d3f6fc5ae39a859ad17001fc3fb9aed1dbfd37fb2ed6`
- result: no cache and no certified stdout
- classification: orchestration-only, no science inference

The first wrapper invocation created the previously absent ignored directory
`logs/runner-cache/.in-progress` after capturing its pre-run filesystem
identity.  That changed the parent `logs/runner-cache` stat token while every
runner and declared-input content hash remained identical.  The wrapper
failed closed and deleted the live log.  Three independent reviewers then
authorized one unchanged reproduction after verifying that the empty live-log
directory already existed.

## Attempt B — preregistered timeout

- runner SHA-256:
  `5b032c62daedd05373ae2d2737986f06aaeef91f455e0d72ec1ad2142d42efc8`
- 25-input fingerprint:
  `d0e5559b1fc376ca5870d3f6fc5ae39a859ad17001fc3fb9aed1dbfd37fb2ed6`
- elapsed: `900.02 s`
- exit code: `-9`
- status: `timeout`
- classification: incomplete, no science inference

Before timeout the runner reported three positive geometry/binding/projector
checks, but its first frozen-input check failed.  Static diagnosis found a
two-character transcription error in the runner's expected SHA-256 for the
unchanged minimal-axioms file.  The next check did not finish within the
declared ceiling because immutable append/product validation was redundantly
recomputed across equivalent prefix axes.  Neither partial output is a
scientific result.  The timeout cache is intentionally removed before the
next exact-byte review; this history preserves the incident classification.

## Attempt C — optimized content-bound timeout

- runner SHA-256:
  `5d323a00cff49b2be9f87eaf7f7cc49195b55c1b81013d4e46f36b193a835db8`
- 25-input fingerprint:
  `d1da30a68f761de015eedfdf9e83af001383d3000992dcd06bc806d852b77902`
- elapsed: `900.07 s`
- exit code: `-9`
- status: `timeout`
- classification: incomplete, no science inference

The exact optimized source passed the frozen-input/source-pin check and then
completed the geometry, literal output-to-input binding, physical pair-output
active sum, full 12,544-control/705,600-term future channel plus STOP, and
imported Block28 pair-Kraus template binding checks.  It timed out before the
`fixed_prefix_depth_two_cylinders` check returned.  The complete prefix
cylinder, continuation, history/QND, debit, covariance, reference, mutation,
scope, and final summary checks therefore remain uncertified.  Relative to
Attempt B this localizes the live runtime bottleneck downstream to the
factorized prefix-cylinder sweep; the partial PASS lines are diagnostic only
and carry no Block29 theorem, retention, obligation retirement, or TOE-score
movement.

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

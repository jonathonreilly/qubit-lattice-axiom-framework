# Batched index comparison — PASS

Exact stage-0 byte checks and both freshness boundaries are preserved. Ten focused controls passed independently; the existing47-test receipt suite passed in the author run.

The measured33.84× improvement applies only to the1024-file synthetic byte-comparison stage.8MiB is a working-size batch target, not a memory guarantee.

Candidate only: the active science preflight and installed helper remain unchanged.

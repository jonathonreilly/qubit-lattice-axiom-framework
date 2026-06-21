# No-Go Ledger

## Do Not Flatten Nested Absolute Paths First

Observation: absolute paths from old worktrees can point to
`scripts/corrections/<runner>.py`. Trying only `scripts/<basename>.py` misses
the checked-out nested runner and preserves a stale absolute path.

Status: blocked by this PR's embedded `scripts/...` suffix recovery.

## Do Not Refactor Canonicalization Broadly In This Stack

The PR keeps the existing helper copies synchronized. A shared module can be a
later cleanup, but this block targets the observed unblock defect directly.

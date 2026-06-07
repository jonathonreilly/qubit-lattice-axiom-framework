# Route Portfolio

## Route A: Default Frozen-Log Verifiers

Status: executed.

Replace default live replay with frozen-log verification and preserve live
execution behind `--recompute`. This closes the audit-runner cache blocker
while keeping the original scientific harness available.

## Route B: Recompute All Logs

Status: rejected for this block.

This would spend wall-clock time but would not improve the audit replay
contract. The frozen logs are the cited artifacts and are sufficient for the
bounded claims.

## Route C: Promote Status Language

Status: rejected.

No audit retagging or retained promotion is allowed on this branch. The output
is an exact-support runner certificate for existing bounded artifacts.

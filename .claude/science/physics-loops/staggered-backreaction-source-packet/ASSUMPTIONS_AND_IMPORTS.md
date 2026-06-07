# Assumptions And Imports

## Allowed Current Inputs

- Existing staggered live-capture runner output.
- Existing prototype helper source: `scripts/frontier_staggered_backreaction_prototype.py`.
- Existing helper cache: `logs/runner-cache/frontier_staggered_backreaction_prototype.txt`.
- File SHA checks and runner-marker checks as artifact integrity checks.

## Retired Import

- The restricted packet no longer asks the auditor to infer or separately import the untruncated prototype helper. The primary runner now checks helper source markers and SHA-fresh cache linkage in its own stdout.

## Still Open

- Independent audit remains required before the repo can use the claim as effective retained status.
- This branch does not strengthen the underlying physical result beyond the existing live-capture packet; it removes the artifact-completeness blocker.

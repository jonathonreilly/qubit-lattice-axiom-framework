# Artifact Plan

Artifacts in this PR:

- Source-note repairs only.
- Runner source repairs only.
- Physics-loop handoff pack only.

Deliberately excluded:

- `docs/audit/*`
- `docs/audit/data/*`
- publication effective-status matrices
- repo status boards
- runner-cache rewrites, because `precompute_audit_runners.py --check-only` found no relevant stale cache.

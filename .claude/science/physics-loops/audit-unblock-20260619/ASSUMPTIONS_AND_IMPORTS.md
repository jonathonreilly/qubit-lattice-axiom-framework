# Assumptions And Imports

## Scope Assumptions

- This block is a source-side unblock, not an audit.
- The target row must remain `unaudited` until an independent audit lane acts.
- Canonical source metadata should match the existing author hint:
  `positive_theorem`.
- The companion runner may check source-boundary metadata, but it must not
  promote the claim to retained status.

## Code Imports

The runner change imports `Path` from the Python standard library and reads the
target note from the repository tree. No third-party dependency is added.

## Science Imports

No new physics premise, numerical constant, or literature-derived value is
introduced in block121. The branch only makes the existing algebraic
equivalence theorem metadata machine-visible and guarded by the exact runner.

## Lock Assumption

`python3 scripts/automation_lock.py status` fails locally with:

```text
[Errno 13] Permission denied: '/Users/jonreilly'
```

This packet records degraded branch-local lock discipline.

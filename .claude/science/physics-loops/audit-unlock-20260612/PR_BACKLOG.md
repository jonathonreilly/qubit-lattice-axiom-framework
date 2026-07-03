# PR Backlog

No PR backlog is expected. The branch is intended to be pushed as:

```text
physics-loop/audit-unlock-20260612
```

If GitHub PR creation is unavailable, run:

```bash
gh pr create --base main --head physics-loop/audit-unlock-20260612 --title "[physics-loop] audit-unlock bounded-support source repairs" --body-file /tmp/audit-unlock-20260612-pr-body.md
```

The PR must remain review-only. Do not merge from this worker.

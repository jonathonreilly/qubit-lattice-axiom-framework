# PR Backlog

PR creation is pending for Block105.

Expected command:

```bash
gh pr create \
  --base main \
  --head physics-loop/audit-unblock-block105-20260620 \
  --title "[physics-loop][review-loop] audit-unblock block105: bounded-support Lorentz spatial-BZ boundary" \
  --body-file .claude/science/physics-loops/audit-unblock-20260619/PR_BODY.md
```

If GitHub auth or network fails, keep this file as the recovery backlog and
record the failure in `HANDOFF.md`. Do not push to `main`.

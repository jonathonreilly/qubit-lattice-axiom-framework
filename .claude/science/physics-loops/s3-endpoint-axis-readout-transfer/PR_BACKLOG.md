# PR Backlog

PR creation is pending branch push.

Intended head:

```text
physics-loop/s3-endpoint-axis-readout-transfer-block154-20260626
```

Intended base: prior Block153 branch.

If GitHub is unavailable, create the PR with:

```bash
gh pr create \
  --base <prior Block153 branch> \
  --head physics-loop/s3-endpoint-axis-readout-transfer-block154-20260626 \
  --title "[physics-loop] s3 endpoint axis-readout transfer block154 exact-support" \
  --body-file .claude/science/physics-loops/s3-endpoint-axis-readout-transfer/PR_BODY.md
```

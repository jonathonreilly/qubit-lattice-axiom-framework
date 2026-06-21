# PR Backlog

PR not opened yet.

Planned command:

```bash
gh pr create \
  --base main \
  --head physics-loop/s3-route2-readout-endpoint-block27-20260621 \
  --title "[physics-loop] s3-route2-readout-endpoint block27 exact-support" \
  --body-file .claude/science/physics-loops/s3-route2-readout-endpoint/PR_BODY.md
```

After PR creation, verify only:

```bash
gh pr view <number> --json number,url,title,headRefName,baseRefName,state
```

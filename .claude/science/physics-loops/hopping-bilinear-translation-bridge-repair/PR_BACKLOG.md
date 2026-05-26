# PR Backlog

## 2026-05-25 - PR creation blocked by GitHub API rate limit

Branch pushed:

```bash
physics-loop/hopping-bilinear-translation-bridge-repair-20260525
```

Open the PR when GitHub API quota recovers:

```bash
gh pr create \
  --base main \
  --head physics-loop/hopping-bilinear-translation-bridge-repair-20260525 \
  --title "[physics-loop] hopping bilinear translation bridge repair proposed_retained" \
  --body-file .claude/science/physics-loops/hopping-bilinear-translation-bridge-repair/PR_BODY.md
```

Attempted command:

```bash
gh pr create --base main --head physics-loop/hopping-bilinear-translation-bridge-repair-20260525 --title "[physics-loop] hopping bilinear translation bridge repair proposed_retained" --body-file .claude/science/physics-loops/hopping-bilinear-translation-bridge-repair/PR_BODY.md
```

Failure:

```text
GraphQL: API rate limit already exceeded for user ID 246726392.
```

REST fallback also failed:

```text
gh: API rate limit exceeded for user ID 246726392. Request ID E945:1FD50C:3337B57:C3787E8:6A14E436, timestamp 2026-05-26 00:07:18 UTC.
```

# PR Backlog

No PR backlog is expected. If GitHub PR creation fails, use:

```bash
gh pr create \
  --repo jonathonreilly/qubit-lattice-axiom-framework \
  --base main \
  --head physics-loop/s3-route2-inverse-square-origin-block42-20260621 \
  --title "[physics-loop] s3-route2-one-pole-channel-volume block42 no-go" \
  --body-file .claude/science/physics-loops/s3-route2-one-pole-channel-volume-no-go/PR_BODY_BLOCK42.md
```

If branch publishing via `git push` is unavailable, publish the exact local
tree through the GitHub Git API and then run the same PR creation command.

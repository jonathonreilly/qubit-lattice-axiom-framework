# PR Backlog

PR creation is pending until the verified Block146 packet is committed and
pushed.

Expected command:

```bash
gh pr create --repo jonathonreilly/qubit-lattice-axiom-framework \
  --base physics-loop/s3-route2-source-measure-bias-no-go-block145-20260622 \
  --head physics-loop/s3-route2-source-measure-bias-stretch-block146-20260622 \
  --title "[physics-loop] s3-route2 source-measure bias stretch block146 no-go" \
  --body-file .claude/science/physics-loops/s3-route2-source-measure-bias-stretch/PR_BODY.md
```

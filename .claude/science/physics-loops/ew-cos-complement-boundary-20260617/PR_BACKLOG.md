# PR Backlog

PR creation is expected for this block.

If `gh pr create` fails because of transient network/auth state, recover with:

```bash
git push -u origin physics-loop/ew-cos-complement-boundary-20260617
gh pr create --base main --head physics-loop/ew-cos-complement-boundary-20260617 \
  --title "[physics-loop] EW cos complement bridge bounded-support" \
  --body-file .claude/science/physics-loops/ew-cos-complement-boundary-20260617/HANDOFF.md
```

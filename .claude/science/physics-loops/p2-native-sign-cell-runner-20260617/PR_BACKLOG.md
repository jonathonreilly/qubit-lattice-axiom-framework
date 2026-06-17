# PR Backlog

No expected backlog. This branch should be pushed and opened as one ready PR:

```bash
git push -u origin codex/p2-native-sign-cell-runner-20260617
gh pr create \
  --title "[physics-loop] p2 native sign-cell runner bounded-support" \
  --body-file /tmp/p2-native-sign-cell-pr-body.md \
  --base main \
  --head codex/p2-native-sign-cell-runner-20260617
```

If GitHub access fails, use the command above after network/auth recovery.

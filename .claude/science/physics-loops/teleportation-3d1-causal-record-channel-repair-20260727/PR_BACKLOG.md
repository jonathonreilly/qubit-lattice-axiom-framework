# PR Backlog

PR delivery was attempted after the review-loop passed, but staging failed
before any index change:

```text
fatal: Unable to create '/Users/jonreilly/Projects/Physics/.git/worktrees/teleportation_3d1_causal_record_channel_note-75f2c482/index.lock': Operation not permitted
```

Use the following from a writable clone or after granting this worktree write
access to its Git metadata:

```bash
git add docs/TELEPORTATION_3D1_CAUSAL_RECORD_CHANNEL_NOTE.md \
        scripts/frontier_teleportation_3d1_causal_record_channel.py \
        logs/runner-cache/frontier_teleportation_3d1_causal_record_channel.txt \
        .claude/science/physics-loops/teleportation-3d1-causal-record-channel-repair-20260727/
git commit -m "fix: refresh teleportation 3D+1 causal record evidence"
git push -u origin HEAD
gh pr create --base main \
  --title "[physics-loop] teleportation-3d1 block01 open" \
  --body-file .claude/science/physics-loops/teleportation-3d1-causal-record-channel-repair-20260727/HANDOFF.md
```

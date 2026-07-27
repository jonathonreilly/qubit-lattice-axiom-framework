# PR Backlog

PR delivery has not been attempted. This science-fix worktree cannot refresh
remote refs because its linked parent git directory is outside the writable
sandbox. Review is complete; if delivery is later authorized and the prior
matching branch is still open, update that landing path instead of opening a
duplicate PR.

Recovery commands from a writable clone, after confirming the prior branch/PR
status:

```bash
git fetch origin
git switch claude/science-fix/teleportation_initial_state_preparation_probe_note-fa4df0dc
git add docs/TELEPORTATION_INITIAL_STATE_PREPARATION_PROBE_NOTE.md \
  scripts/frontier_teleportation_initial_state_preparation_probe.py \
  logs/runner-cache/frontier_teleportation_initial_state_preparation_probe.txt \
  .claude/science/physics-loops/teleportation-initial-state-preparation-closure
git commit -m "physics-loop: certify teleportation initial-state open gate"
git push -u origin HEAD
```

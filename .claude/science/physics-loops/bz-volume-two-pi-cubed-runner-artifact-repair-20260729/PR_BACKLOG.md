# PR Backlog

The worker did not push or open a PR because the autonomous science-fix
supervisor owns commit/push/PR creation after the worker returns, and this
managed worktree cannot create the parent repository's Git index lock.

Recovery commands for the supervisor:

```bash
git add docs/BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md \
  scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py \
  logs/runner-cache/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.txt \
  .claude/science/physics-loops/bz-volume-two-pi-cubed-runner-artifact-repair-20260729/
git commit -m "fix: provide complete BZ Haar runner evidence"
git push -u origin claude/science-fix/bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_not-28946fe6
gh pr create --base main \
  --head claude/science-fix/bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_not-28946fe6 \
  --title "[physics-loop] bz-volume evidence repair — bounded theorem" \
  --body-file .claude/science/physics-loops/bz-volume-two-pi-cubed-runner-artifact-repair-20260729/HANDOFF.md
```

# PR backlog

No separate physics-loop PR is opened: the Promotion Value Gate records that
this block is an auditor-requested artifact repair, not a new derivation.  The
existing science-fix branch is
`claude/science-fix/full128_local_m64_seam_m2_bare_frame_intertwiner_bounded_the-f5e9fa72`.

After the autonomous science-fix supervisor creates its commit, the recovery
commands are:

```bash
git push origin claude/science-fix/full128_local_m64_seam_m2_bare_frame_intertwiner_bounded_the-f5e9fa72
gh pr create --base main --head claude/science-fix/full128_local_m64_seam_m2_bare_frame_intertwiner_bounded_the-f5e9fa72 --title "[physics-loop] full128 transcript repair — bounded theorem" --body-file .claude/science/physics-loops/full128-runner-transcript-repair-20260729/HANDOFF.md
```


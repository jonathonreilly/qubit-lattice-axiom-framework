# Branch-local supervisor lock — computation-connection-20260727

- Holder: physics-loop supervisor session (Claude), block01 branch
  `physics-loop/computation-connection-block01-20260727`, independent
  worktree `.claude/worktrees/cleanup-local-worktrees-5f598b`.
- Acquired: 2026-07-27T21:50 local. TTL: campaign end (~2026-07-28T09:37).
- Reason for branch-local mode: `python3 scripts/automation_lock.py status`
  and `acquire` both fail on this machine with
  `[Errno 13] Permission denied: '/Users/jonreilly'` (lock path resolves to
  a different user's home). Recorded per
  physics-loop references/long-running-execution.md preflight step 7.
- Non-overlap survey at acquisition: owner automation active on
  frontier-certificate repair (cl3-compute-exceptions-20260727),
  N5 certificates (cl3-n5-certificates-even-20260727), record-campaign
  review worktrees (wf_7bbd095a: rl-5610-integrate, narrow-5606,
  review-5694), poisson lanes (PRs #5693, #5695). None touch Cycle 721,
  the recurrent-companion lane, or `frontier_cycle72*` artifact names.
- Claimed scope: Cycle 721+ artifacts in the computation-connection lane
  (`frontier_cycle721_*` and successors this campaign), this pack dir, and
  the block branches `physics-loop/computation-connection-block*-2026072*`.

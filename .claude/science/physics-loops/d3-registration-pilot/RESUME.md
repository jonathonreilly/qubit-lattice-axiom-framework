# d3-registration-pilot — resume brief (written before the 2026-07-09 connectivity gap)

The overnight full run was launched as a DETACHED OS process
(nohup-orphaned to launchd + caffeinate) before the owner's red-eye.
It needs no network and checkpoints every 10 steps. This file is the
recovery map for any fresh session.

## Check status (any time, any session)

```bash
cd /Users/jonBridger/tp-matter-mass-wep
tail -5 logs/runner-cache/d3_pilot_checkpoints/full_run_progress.log
pgrep -fl d3_registration_onset_pilot   # is it still running?
ls -la logs/runner-cache/d3_pilot_checkpoints/ | tail -8
```

## If it finished

```bash
python3 scripts/d3_registration_onset_pilot_2026_07_09.py --report
```
prints the final six-line block from the streamed observables without
recomputing. Cache that output to
`logs/runner-cache/d3_registration_onset_pilot_2026_07_09.txt`.

## If it was interrupted (sleep, power, crash)

```bash
zsh scripts/d3_pilot_launch_detached.sh
```
auto-resumes from the newest valid checkpoint (checksummed; refuses
mismatched state rather than silently repairing).

## Then (block02 shipping, per the campaign pattern)

1. Supervisor line-review of the --report output against the five
   checks in docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md.
2. Bounded note: D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md
   (verdict semantics: BAR-DERIVED-EFFECTIVE / BAR-NOT-PINNED;
   BAR-BELOW-WINDOW is a CHECK-05 flag; physics absence is never
   MACHINERY-FAIL). Include the two predeclared risk signatures
   exactly as measured (empty QND window; correlated-channel fake).
3. vocab_lint; commit runner cache + note on THIS branch
   (physics-loop/d3-registration-pilot-block01-20260709); PR base =
   registration-bar-block03 branch.
4. Pack close + handoff after owner sees the verdict.

## Campaign state at the gap

- Engine (block01a): committed + pushed, ENGINE-VALID, slab
  cross-check 4e-13.
- Pilot runner (block01b): worker-delivered; supervisor --validate
  PASS expected (see logs/runner-cache/
  d3_registration_onset_pilot_validate.txt once cached); committed +
  pushed with this brief.
- Everything else this season: see the season review brief (#5093),
  the audit-readiness findings (#5095), and
  .claude/science/physics-loops/*/HANDOFF.md.

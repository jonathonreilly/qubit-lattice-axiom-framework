# d3-bar-window — resume brief (any fresh session)

The full measurement runs as a DETACHED OS process (nohup-orphaned to
launchd + caffeinate) launched by
`scripts/d3_bar_window_launch_detached.sh`. It needs no network and
checkpoints every 10 steps. Owner authorization on record
(2026-07-11): "go and then also execute it" — covers freezing the
delta protocol AND executing the run.

## Check status (any time, any session)

```bash
cd /Users/jonBridger/tp-matter-mass-wep
tail -5 logs/runner-cache/d3_bar_window_checkpoints/full_run_progress.log
pgrep -fl d3_bar_window_measurement   # is it still running?
ls -la logs/runner-cache/d3_bar_window_checkpoints/ | tail -8
```

## If it finished

```bash
python3 scripts/d3_bar_window_measurement_2026_07_11.py --report
```
regenerates the final six-line verdict block from the streamed
observables without recomputing (exit 0 = BAR-DERIVED-EFFECTIVE,
1 = BAR-NOT-PINNED, 2 = MACHINERY-FAIL). Cache that output to
`logs/runner-cache/d3_bar_window_measurement_2026_07_11.txt`.

## If it was interrupted (sleep, power, crash)

```bash
zsh scripts/d3_bar_window_launch_detached.sh
```
auto-resumes from the newest valid checkpoint (checksummed; refuses
mismatched state or a protocol-hash mismatch rather than repairing).

## Then (shipping, per the campaign pattern)

1. Supervisor line-review of the --report output against the gates in
   docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md (the FROZEN delta —
   its SHA-256 is every artifact's protocol_hash; the parent memo
   docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md is recorded as
   parent_protocol_hash; edit neither).
2. Bounded note: D3_BAR_WINDOW_BOUNDED_NOTE_<date>.md. Verdict
   semantics inherited; BAR-BELOW-WINDOW is a CHECK-05 flag; physics
   absence is never MACHINERY-FAIL. Report all six risk signatures
   exactly as measured (the parent's five plus window noncontiguity),
   the boundary bracket, the doublet diagnostic chi_GS^(2), and the
   theta* field-stability numbers.
3. vocab_lint; commit runner caches + note on THIS branch
   (physics-loop/d3-bar-window-block01-20260711); PR base = the
   d3-bar-location branch (stacks above PR #5144).
4. Pack close + handoff after the owner sees the verdict.

## Campaign state markers

- Frozen protocol: docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md
  (supervisor-authored and frozen at commit 72432fb40e).
- Block02 deliverable: scripts/d3_bar_window_measurement_2026_07_11.py
  — a fork of scripts/d3_bar_location_measurement_2026_07_10.py; the
  review surface is the diff between the two. The engine and the
  engine-extension module are unchanged imports.
- Validate cache (once run):
  logs/runner-cache/d3_bar_window_validate_2026_07_11.txt. First
  validate is cold: four ground-doublet Lanczos builds including the
  new lambda = 0.02 (declared 30-minute allowance).
- Everything else: STATE.yaml and HANDOFF.md beside this file, and
  the parent packs at .claude/science/physics-loops/d3-bar-location/
  and .../d3-registration-pilot/.

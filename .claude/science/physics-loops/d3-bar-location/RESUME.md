# d3-bar-location — resume brief (any fresh session)

The full measurement runs as a DETACHED OS process (nohup-orphaned to
launchd + caffeinate) launched by
`scripts/d3_bar_location_launch_detached.sh`. It needs no network and
checkpoints every 10 steps. Owner authorization on record
(2026-07-10): "launch the overnight run once validate passes".

## Check status (any time, any session)

```bash
cd /Users/jonBridger/tp-matter-mass-wep
tail -5 logs/runner-cache/d3_bar_location_checkpoints/full_run_progress.log
pgrep -fl d3_bar_location_measurement   # is it still running?
ls -la logs/runner-cache/d3_bar_location_checkpoints/ | tail -8
```

## If it finished

```bash
python3 scripts/d3_bar_location_measurement_2026_07_10.py --report
```
regenerates the final six-line verdict block from the streamed
observables without recomputing (exit 0 = BAR-DERIVED-EFFECTIVE,
1 = BAR-NOT-PINNED, 2 = MACHINERY-FAIL). Cache that output to
`logs/runner-cache/d3_bar_location_measurement_2026_07_10.txt`.

## If it was interrupted (sleep, power, crash)

```bash
zsh scripts/d3_bar_location_launch_detached.sh
```
auto-resumes from the newest valid checkpoint (checksummed; refuses
mismatched state or a protocol-hash mismatch rather than repairing).

## Then (shipping, per the campaign pattern)

1. Supervisor line-review of the --report output against the five
   checks in docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md (the
   FROZEN protocol — its SHA-256 is bound into every artifact; do not
   edit that file).
2. Bounded note: D3_BAR_LOCATION_BOUNDED_NOTE_<date>.md. Verdict
   semantics: BAR-DERIVED-EFFECTIVE / BAR-NOT-PINNED / MACHINERY-FAIL;
   BAR-BELOW-WINDOW is a CHECK-05 flag, not a verdict class; physics
   absence is never MACHINERY-FAIL. Report all five risk signatures
   exactly as measured (empty write/QND window; correlated-channel
   fake; seam leakage; contrast loss / reflected wavefront; capacity
   without coarse gain) plus the doublet diagnostic chi_GS^(2).
3. vocab_lint; commit runner caches + note on THIS branch
   (physics-loop/d3-bar-location-block01-20260710); PR base = the
   d3-registration-pilot branch (stacks above PR #5116).
4. Pack close + handoff after the owner sees the verdict.

## Campaign state markers

- Frozen protocol: docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md
  (committed fe6486a2cc; supervisor baseline correction applied at
  freeze — excess gate anchored at verified t=0, doublet = control +
  diagnostic only).
- Block02 deliverables: scripts/d3_bar_location_engine_ext_2026_07_10.py
  and scripts/d3_bar_location_measurement_2026_07_10.py.
- Validate cache (once run):
  logs/runner-cache/d3_bar_location_validate_2026_07_10.txt.
- Everything else: STATE.yaml and HANDOFF.md beside this file, and
  the pilot campaign pack at
  .claude/science/physics-loops/d3-registration-pilot/.

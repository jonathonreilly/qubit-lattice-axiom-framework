# Handoff

## Result

The first science block now probes every named `r=1/2` open item with 57 exact
checks.  The main new structural reduction is that `w=1/3` versus `w=1/2`
is uniform formation on two different event resolutions.  This couples the
formation selector to the K-stage question and points the next cycle at an
explicit formation generator and its relative hazards.

## Artifacts

- `docs/R_HALF_OPEN_BACKLOG_FORMATION_LAW_PROBE_BATCH_EXACT_SUPPORT_NOTE_2026-07-13.md`
- `scripts/frontier_rhalf_open_backlog_probes_2026_07_13.py`
- `logs/runner-cache/frontier_rhalf_open_backlog_probes_2026_07_13.txt`

## Important live-state correction

PR 5326 is closed and unmerged.  Its licensing convention is not current-main
authority and is not consumed by this block.

## Review disposition

Branch-local review-loop result: `PASS WITH BOUNDED CLAIMS`.  The exact runner
passes 57 checks; independent formula checks and the audit-compatibility
pipeline pass; the new claim seeds as an unaudited `bounded_theorem` with nine
dependencies.  No audit verdict is requested or applied by this branch.

## Exact next action

Construct two minimal record-formation generators: one whose primitive jumps
are carrier-member events and one whose primitive jumps are K-orbit-cell
events.  Derive their stationary formation measures and identify an
environment/readout observable that distinguishes the generators without
fitting `r`.

# d3-bar-location — campaign handoff (measurement complete 2026-07-10)

## PR (one block PR; stacks above the pilot)

**d3-bar-location blocks 01-04** — frozen design memo, engine
extensions + measurement runner, supervisor validate, and the full
measurement. Base = the d3-registration-pilot branch (PR #5116's
branch), so review order is: registration-bar stack (#5089-#5091) →
pilot (#5116) → this.

Verify:
- `python3 scripts/d3_bar_location_measurement_2026_07_10.py`
  (validate mode, ~2 min warm / ~10 min cold) — diff against
  `logs/runner-cache/d3_bar_location_validate_2026_07_10.txt`.
- `python3 scripts/d3_bar_location_measurement_2026_07_10.py --report`
  (seconds; reads the committed JSONL streams) — diff against
  `logs/runner-cache/d3_bar_location_measurement_2026_07_10.txt`
  (exit 1 = BAR-NOT-PINNED by frozen wiring).
- The frozen protocol is
  `docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`; its SHA-256 is
  recorded in every JSONL row and both caches (protocol_hash) — the
  memo must byte-match or `--report` refuses.
- The 4.95 h full run needs no re-execution: the committed streams
  are its output.

## One-paragraph result

The first certified registration onset in this program: on the open
3^3 cube with coarse disjoint fragments and a class-uniform
pointer-contrast preparation (frozen before launch), excess-gated,
conditionally independent, finite-time persistent redundancy onset
occurs at weak transverse field — lambda = 0.05 at Jt = 0.6 (all
three tolerances) and lambda = 0.10 at Jt = 0.7,
resolution-converged, both through the geometrically independent
opposite five-qubit pair, with the pointer's own stability gates
passing whole. Where the bar can be read it reads theta* ~ 0.50,
inside the sparse window with a factor-two margin and
tolerance-insensitive where all tolerances fire. At lambda = 0.20 the
opposite-pair conditional dependence crosses the 0.02-bit
independence gate before the tighter content gates certify (measured
lambda-trend C_55 = 0.005 / 0.017 / 0.060 at the content peak), so
one headline cell is missing and the frozen completeness gates return
BAR-NOT-PINNED — reported exactly as wired, no retuning. The quiet
shells stay quiet (locality exact to 2e-5 bits), the coarse blocks'
capacity gain is small (contrast did the lifting; coarseness supplied
the independent witness), and the run's own doublet diagnostic
(chi_GS^(2) ~ 0.999 bits) validates the freeze-time baseline
correction without which zero events could ever have fired.

## What it buys the derivation

Existence on the framework's own Z^3, with a measured location where
the criterion fires. The chain of obstructions is now: d = 1 geometry
(measured, structural) → d = 3 single-qubit capacity (measured,
pilot) → BOTH absent here (measured). What remains between this and a
protocol-complete bar location is one design choice about the
lambda-completeness gate, not a physics unknown: the certified window
is the weak-field side, and the closure at stronger field is itself a
measured boundary (the correlated-channel risk signature realized as
a lambda-trend).

## Named successor (not commissioned)

A bar-location protocol frozen on lambda in {0.02, 0.05, 0.10}, or
with the completeness gate restated as window-plus-boundary (certify
where independence permits; report the closure lambda as a measured
boundary). Either is a NEW frozen protocol; neither rescues this one.
Same machinery, same gates, same Z^3.

## Ops notes

- Full run: detached (launchd + caffeinate), 4.95 h wall, RSS peak
  4.43 GiB / 10 GiB guard, no resume needed. Owner authorization for
  the launch is on record in RESUME.md.
- Committed evidence: four JSONL streams + preflight artifact +
  report cache + validate cache. The ~180 MB ground-doublet NPZs and
  rolling state checkpoints are gitignored (regenerable; the doublet
  rebuild is ~10 min total).

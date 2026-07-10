# d3-registration-pilot — campaign handoff (measurement complete 2026-07-10)

## PR (one block PR; stacks on the registration-bar campaign)

**d3-registration-pilot block01+02** — engine + pilot runner + the
overnight measurement. Base = registration-bar-block03 branch (#5091's
branch), so it lands after the registration-bar stack in review order.

Verify:
- `python3 scripts/d3_cubic_orbit_engine_2026_07_09.py` — engine
  self-validation (orbit count 5,605,504 asserted; dense 3x3x2 slab
  cross-check 3.94e-13; ~10 min, rebuilds its tables in ~1 min).
- `python3 scripts/d3_registration_onset_pilot_2026_07_09.py`
  (validate mode, ~13 min) — diff against
  `logs/runner-cache/d3_registration_onset_pilot_validate_2026_07_09.txt`.
- `python3 scripts/d3_registration_onset_pilot_2026_07_09.py --report`
  (seconds; reads the committed JSONL streams, no recompute) — diff
  against `logs/runner-cache/d3_registration_onset_pilot_2026_07_09.txt`
  (exit 1 = BAR-NOT-PINNED by design; site-class table prints sorted
  in report mode vs dict-order live, values identical).
- The full 11.2 h run needs no re-execution: the committed streams ARE
  its output, and `--report` regenerates the verdict from them.

## One-paragraph result

On the smallest lattice with the branching geometry the d=1 block said
permanence needs — an open 3^3 cube, uniform transverse-field Ising
quench, all constants predeclared — certified redundant registration
of the center pointer NEVER onsets: zero events at every coupling and
every tolerance over the whole grid Jt <= 10, not one certifying
fragment (R_ind = 0 throughout). The imprint exists and is transient:
per-fragment pointer information peaks at 0.051 bits at Jt = 0.3
(coupling-independent to three digits — the ZZ bond alone sets it) and
recoheres, a factor ~13 below the certification content gate. The
pointer itself stays QND-stable the whole window and the six channels
are measured nearly independent (max conditional dependence 0.023
bits) — so the d=1 geometric obstruction is genuinely absent in d=3,
and the failure moves to register capacity: a single qubit in a
uniform quench is too small an antenna to hold a certifiable copy.
Bar location remains unpinned (BAR-NOT-PINNED; BAR-BELOW-WINDOW not
raised — that flag needs an onset). Both predeclared risk signatures
reported exactly as measured; machinery green including dt-halving.

## What it buys the derivation

The registration-bar synthesis left the bar's LOCATION as the d=3
measurement. This pilot bounds how that measurement must be made: not
with single-qubit registers under a uniform symmetric quench. That is
a measured design constraint, not a failure of the derivation — the
shape (redundancy onset, R >= 2, small delta) is untouched, and the
d=1 -> d=3 comparison now shows the obstruction MOVING (geometry ->
capacity) rather than persisting, which is itself evidence the
criterion is probing real structure.

## Named successor (not commissioned)

Same Z^3 cube, two predeclared changes, separately or together:
(i) coarser registers — multi-qubit fragment blocks (faces/shells);
the conditional-independence machinery and all five checks carry over
unchanged; (ii) pointer-contrast preparation — a local excitation on
the uniform background, mirroring the d=1 kicked-charge protocol, so
the bond has a distinguished value to copy. d=2 remains at most a
method stepping stone (owner reminder retained: bar location can be
dimension-dependent; the target is the framework's own Z^3).

## Ops notes

- The overnight run was engineered for the owner's connectivity gap:
  nohup-orphaned to launchd + caffeinate, checkpoint/resume every 10
  steps, SIGTERM-safe. It completed with no resume needed. The rolling
  ~92 MB state checkpoints and live logs are gitignored as transient;
  the JSONL observable streams and the --report cache are committed.
- Engine tables (.npz) regenerate in ~1 min and are gitignored.

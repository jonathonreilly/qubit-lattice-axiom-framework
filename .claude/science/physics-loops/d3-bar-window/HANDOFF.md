# d3-bar-window — campaign handoff (CLOSED 2026-07-11)

## PR (one block PR; top of the registration stack)

**d3-bar-window blocks 01-04** — frozen delta memo, runner fork,
supervisor validate, the full measurement, bounded note. Base = the
d3-bar-location branch (PR #5144's branch). Review order for the
whole registration arc: #5089-#5091 (shape + d=1 obstruction) →
#5116 (d=3 pilot negative) → #5144 (first onset, near-miss) → this
(BAR-DERIVED-EFFECTIVE).

Verify:
- `python3 scripts/d3_bar_window_measurement_2026_07_11.py`
  (validate; diff vs
  `logs/runner-cache/d3_bar_window_validate_2026_07_11.txt`).
- `python3 scripts/d3_bar_window_measurement_2026_07_11.py --report`
  (seconds; exit 0 = BAR-DERIVED-EFFECTIVE; diff vs
  `logs/runner-cache/d3_bar_window_measurement_2026_07_11.txt`).
- `diff scripts/d3_bar_location_measurement_2026_07_10.py
  scripts/d3_bar_window_measurement_2026_07_11.py` — the complete
  protocol delta as code (233 lines, every hunk attributable to the
  frozen delta memo's numbered items).
- The 6.73 h full run needs no re-execution; the committed streams
  are its output and both protocol hashes are bound into every row.

## One-paragraph result

The registration bar's location is measured: theta* = 0.500752
(median; range 0.500104-0.504731) across a certified window
lambda in {0.02, 0.05, 0.10}, with tolerance-stability factor 1.00089,
field-stability factor 1.00925, and dt-convergence 0.17% — a bar that
sits still while the coupling changes five-fold and the redundancy
depth changes three-fold. Every event is inside the deposition-sparse
window with a factor-2.5 margin. The noise boundary is bracketed at
(0.10, 0.20): what strong transverse field destroys first is the
INDEPENDENCE of the copies, not the copies (at lambda = 0.02 all six
fragments certify pairwise-independently — the full Darwinism plateau,
fifteen pair dependences all <= 0.00113 bits; at 0.05/0.10 the
geometric minimum R = 2 via the opposite pair; at 0.20 nothing at
headline tolerance). The doublet diagnostic (~0.999 bits at all four
couplings) confirms the vacuum's static record content saturates the
pointer entropy, validating the trajectory-t0 excess anchor.

## Chain position (what Jon's review is deciding)

With this note the registration arc closes at comparator level: shape
derived from the Record axiom's clauses (2026-07-09), d = 1 geometric
obstruction measured, d = 3 capacity obstruction measured, existence
+ location + stability + noise boundary measured. The gravity chain's
registration threshold is now a measured number with a measured
validity window, conditional on the declared comparator and the
standing record-reading convention — the same conditionality the
whole chain already carries. Supplied residue unchanged: comparator
inputs, the QD convention, the theta normalization across
comparators.

## Named successors (not commissioned)

- Gauge-native substrate: repeat the protocol with Gauss-law link
  registers (the d = 1 block's substrate) on Z^3 — removes the
  "plain qubits" comparator caveat, at a real engine cost.
- Boundary refinement: one lambda = 0.15 point would halve the
  boundary bracket; only worth it if the boundary number itself
  becomes load-bearing.
- theta-normalization bridge: connect this comparator's theta to the
  deposition campaign's theta so the 0.50-vs-0.2 comparison is
  quantitative rather than declared.

## Ops notes

- Full run detached 6.73 h, RSS peak 4.40 GiB / 10 GiB guard, no
  resume needed, survived one owner-side SSH loss mid-run.
- Committed evidence: five JSONL streams, preflight artifact, report
  + validate caches. Ground-doublet NPZs (~180 MB x 4) and rolling
  checkpoints gitignored (regenerable, ~15 min total).

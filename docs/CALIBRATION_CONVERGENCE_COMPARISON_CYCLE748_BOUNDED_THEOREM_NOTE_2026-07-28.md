# The calibration convergence comparison — data approaching the weight, never claiming it — Cycle 748

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem (comparison data only; the
weight-claim boundary never crossed)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle748_calibration_convergence_comparison_2026_07_28.py`](../scripts/frontier_cycle748_calibration_convergence_comparison_2026_07_28.py)
- [`frontier_cycle748_convergence_independent_check_2026_07_28.py`](../scripts/frontier_cycle748_convergence_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The campaign's calibration grounding drew the honest line: counts and
simplexes are data; promotion to `w(E)` or selection of the trace law
is the weight claim, and the occurrence-derived version depends on
Track A. This cycle builds everything on the data side of that line:

- **nested declared run families** on a size ladder 8 → 32 → 128 → 512
  typed rows (each row declared data per the grounding's operational
  definition — no realized-outcome claim), with a tolerance ladder
  0.06 → 0.02 → 0.002 → 0.001;
- **the convergence table, as observed data**: per (size, tolerance)
  the Cycle-744 port's exact simplex compared against the frozen
  supplied `w(E)` values — the aggregate rows read
  `ADDD → AADD → AAAD → AAAA`: agreement spreads down the tolerance
  ladder as the family grows, and the per-tolerance disagreement
  counts are observed non-increasing at every step. Reported as
  observation, not law;
- **the miscalibrated control** diverges at all 16 size–tolerance
  pairs — the comparison machinery is demonstrably not vacuous;
- **firewalls, both directions**: no weight written, no trace-law
  selection, comparison verdicts only; the Track A dependency (the
  run family itself must eventually come from derived occurrence)
  recorded in the boundary keys.

## Supplied / derived / open

### Supplied

- the declared nested families and both ladders (typed data; zero
  fitted parameters); everything the Cycle-317/744 packages declare.

### Derived

- the exact per-family simplexes; the frozen comparison table and its
  reproducibility; the monotonicity observation as data; the control
  divergence; the firewall properties.

### Open

- the weight claim itself (crossing the line requires Track A's
  derived occurrence — recorded, not attempted);
- the orbit-occupancy no-go scope interaction (Track A's reading);
  everything inherited at original scopes.

## Negative-claim discipline

No negative claim ships. The convergence pattern is an observation
about declared data through landed machinery; nothing about the Born
law follows from it and nothing is claimed to.

## Verdict

The Born lane now has the exact experiment shape waiting for its
missing input: when Track A (or a future campaign) produces derived
occurrence data, this cycle's machinery will say — with tolerances,
controls, and frozen expectations already in place — whether the
framework's occurrence statistics approach the supplied weights. Until
then, the table is data and the boundary holds. Independent audit
still required.

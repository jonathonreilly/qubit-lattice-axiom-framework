# Campaign Goal — audit-unlock-toe-20260724

Owner directive (2026-07-24): "I want high value work to either unlock the audit
or complete our TOE — run a physics-loop campaign to drive the maximum value to
the repo." Runtime: until the science backlog is exhausted.

## Lane A — audit-unlock (backlog drain)

Ledger recon at campaign start (regenerated monolith, tree == origin/main
e6d1070adf at recon time): 3,857 rows; 2,954 unaudited, of which **551 are
root-ready** (every dependency already in a valid state) and 2,403 are blocked
behind unaudited dependencies. The audit DAG is a drain problem: each root-ready
row audited unblocks its dependents.

Contract: independent codex audit-loop workers on clean origin/main clones run
`docs/audit/scripts/orchestrate_audit_loop.py` (the coordinator owns target
selection, worker dispersal, and collision handling via
`remote_state_superseded`). This session NEVER runs the coordinator or authors
grades — it dispatches workers per the standing owner grant and reads exits.

Success measure: unaudited count falls; blocked rows become root-ready; the
KCPT chain (26 rows, none root-ready at campaign start) gains auditable rows.

## Lane B — TOE-completion (derivation obligations)

The live frontier is the THREE open derivation obligations in
`docs/audit/data/derivation_obligations.json`:

1. `ac_orbit_occupancy_statistical_grain_derivation_obligation`
2. `ac_reta_hclass_hunit_readout_derivation_obligation`
3. `theta_quark_determinant_cross_sector_readout_derivation_obligation`

Contract: workhorse science units (Fable designs/spec/reviews; Opus 5 executes;
codex review-loop lands; independent audit grades). The KCPT
symmetry-algebra lane serves obligation #1 directly (orbit/occupancy structure
of the record-registered decomposition) and #3 through the U14 CP-completion
and U17 Dirac-radius grading structures. Each unit is a bounded_theorem note +
paired runner + cache, landing via worktree PR.

Success measure: landed bounded theorems that shrink an obligation's residual
surface, with honest boundaries; no new imports, axioms, or comparators.

## Non-goals

- No audit-grade authorship or prediction (grades come exclusively from the
  independent audit lane on origin/main).
- No new axioms/imports/literature comparators without explicit owner approval.
- No universal r=1/2 forcing (lane-scoped registration remains the route).

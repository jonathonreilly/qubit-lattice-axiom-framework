# Handoff

## What moved

Three stale-frame runner paths now align with their archived source notes:

- `scripts/frontier_cl4c_carrier_axiom_consequence_map.py`
- `scripts/frontier_hubble_c1_a5_minimal_carrier_axiom_audit.py`
- `scripts/frontier_hubble_c1_stuck_fanout_synthesis.py`

Each now verifies the archive-firewall/source-boundary contract instead of
asserting old Axiom* cascade, carrier minimality, or global fan-out exhaustion
claims.

## What did not move

- No audit result was changed.
- No ledger, queue, publication effective-status surface, front-door status, or
  lane registry was edited.
- No retained/promoted status is proposed.
- No new axiom is introduced.

## Reviewer/auditor next action

Review this PR as source-side cleanup. If accepted, the audit runner surface for
the three stale-frame rows should no longer conflict with their archived failed
source boundary.

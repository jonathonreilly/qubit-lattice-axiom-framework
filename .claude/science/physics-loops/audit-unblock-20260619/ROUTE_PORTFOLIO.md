# Route Portfolio

## Selected Route: Generated Front-Door Exclusion

Repair `scripts/frontier_koide_q_delta_formal_ratio_repair.py` so its source
firewall skips the generated front-door status snapshot.

Score:

- Audit-unblock value: high, because the target is ready, critical, and direct
  runner execution failed before the patch.
- Science risk: low, because the branch does not change the formal identity.
- Blast radius: low after rebase narrowing, because generated audit and
  publication surfaces are excluded from the PR diff.

## Rejected Route: Treating Front Door As Formal Context

Rejected because the generated front-door queue entry is not source evidence
and should not be made load-bearing by wording tricks.

## Deferred Route: Broader Generated-Snapshot Firewall Sweep

Other ready rows may have the same false-positive pattern. The next block
should search direct runner failures before patching any candidate.

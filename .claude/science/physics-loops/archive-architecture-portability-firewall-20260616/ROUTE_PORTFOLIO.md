# Route Portfolio

## Route 1: Evidence firewall for archived packet

Status: selected.

Move the archived failed audit packet to unambiguous historical / diagnostic
provenance, remove its stale evidence links from work-history surfaces, and add
a guard runner.

## Route 2: Rebuild the full portability science

Status: not selected here.

This would rerun and possibly extend `frontier_architecture_portability_sweep`.
The separate live sweep row is already audited clean on `origin/main`; this PR
does not need a new physics run.

## Route 3: Ledger retagging

Status: rejected.

The author-side PR must not retag audit ledger fields. The independent audit
lane owns verdict and effective-status changes.

# Route Portfolio

## Route 1: Restore Declared Runner Paths

Status: executed.

The audit blocker text named exact missing scripts.  Recreating those scripts
from current one-hop helpers directly targets the blocker without changing
ledger status.

## Route 2: Replace Archived Prose With New Source Notes

Status: not executed.

This would increase review surface and risk vocabulary/status churn.  The
archived notes already point to the script names; the narrower move is to
restore those script paths and let audit decide.

## Route 3: Modify Audit Ledger Rows

Status: rejected.

The user explicitly separated author repair from audit retagging.  This branch
does not edit `docs/audit/**`.

## Route 4: Repair Nearby Existing Helper Runners

Status: deferred.

Two nearby helpers have stale prose substring checks, but those are separate
rows from this missing-runner blocker.  The restored runners import only their
computational helpers and assert the relevant math directly.

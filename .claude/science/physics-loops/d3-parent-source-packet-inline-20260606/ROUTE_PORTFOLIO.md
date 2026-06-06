# Route Portfolio

## R1: Inline Packet Completeness Into Parent Runner

Status: executed.

Move the artifact exposure checks into `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`, so a restricted parent packet can inspect bridge source, original runner source/cache, cache SHA freshness, and source-packet JSON directly.

Expected movement: direct closure of the runner-artifact/source-packet blocker.

## R2: Rewrite The Parent Theorem

Status: rejected.

This would risk changing the scientific claim rather than repairing the audit blocker. The current lower-bound theorem is already scoped correctly.

## R3: Edit Audit Ledger Helper Paths

Status: rejected.

The user explicitly does not want ledger retagging or audit-result edits in science PRs. The source packet must be repaired instead.

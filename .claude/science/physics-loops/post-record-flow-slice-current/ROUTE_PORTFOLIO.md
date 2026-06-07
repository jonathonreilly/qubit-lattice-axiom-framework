# Route Portfolio

## Route A: Exact current ledger slice

Status: chosen.

Update the runner and note to the latest main snapshot, verify the exact
flow/thermal lane counts, and print every row grouped by lane. This directly
addresses the audit blocker about missing packet/source context.

## Route B: Selector-rule derivation

Status: not attempted in this block.

Derive a native selector rule that turns stable settings into selected dials.
This is a deeper science problem and is intentionally not bundled with the
source-packet repair.

## Route C: Demotion-only packet

Status: rejected.

A demotion would be too weak because the row-map runner is already structurally
available; the tractable blocker is packet completeness.

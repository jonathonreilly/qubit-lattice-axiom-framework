# Route Portfolio

## Route A: Unit And Threshold Repair

Status: executed.

Patch the source note, runner labels, and runner cache so binary memory
quantities consistently use `GiB`; repair the truncation threshold to about
`1.91`.

Expected claim-state movement: closes the known wording/arithmetic blocker
while preserving bounded-support status.

## Route B: Stronger Treewidth Certificate

Status: deferred.

Attempt a lower-bound certificate or exhaustive search over contraction paths.
This would be a larger science block and is not needed for the present
unit/threshold repair.

## Route C: Rank-Aware Contractor

Status: deferred.

Move beyond the naive node-elimination obstruction by keeping the rank-8
projector decomposition alive during contraction. This is higher leverage for
future gauge-scalar bridge work but not part of this small repair.

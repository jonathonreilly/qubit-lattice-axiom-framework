# Route Portfolio

## Route A: Exact/certified permutation-null p95

Status: not used.

This would require a stronger null calculation than the runner implements.

## Route B: Narrow to fixed sampled-null protocol

Status: used.

The source note and runner now state that the null statistic is a fixed
300-permutation deterministic sampled-null p95 and add source-note checks for
that boundary.

## Route C: Retain inherited record-conditioning authorities

Status: still open.

This repair does not close the inherited #3554/#3555 dependency edges.

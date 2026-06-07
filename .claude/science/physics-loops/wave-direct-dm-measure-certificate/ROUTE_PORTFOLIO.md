# Route Portfolio

## Route A: Independent measure_dm certificate in target runner

Status: chosen.

Add source-marker and cache-SHA checks for `measure_dm` and the continuum
helper directly to the row-specific target runner, then refresh the target
cache and manifest.

## Route B: Full helper source dump

Status: not used.

The helper source is large. The audit blocker explicitly allowed an
independent certificate for the `measure_dm` computation.

## Route C: Claim widening

Status: rejected.

The branch keeps the bounded replay boundary.

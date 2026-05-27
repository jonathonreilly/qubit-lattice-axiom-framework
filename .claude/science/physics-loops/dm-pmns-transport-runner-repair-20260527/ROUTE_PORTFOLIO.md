# Route Portfolio

## Route A: Restore Legacy Helpers

Rejected.  Re-expanding the raw projector-interface runner would undo the
recent raw-interface scope repair and would risk resetting already audited
upstream rows.

## Route B: Patch All Dependent Helper Runners

Deferred.  Several unaudited PMNS/DM frontier runners still reference the old
helper surface.  That is a broader repair campaign and is not required for this
conditional row.

## Route C: Make The Conditional Row Self-Contained

Selected.  This row only needs the narrow compatibility layer for the interval
witness.  Implementing that layer inside the primary runner closes the exact
import blocker while preserving the narrowed raw-interface authority surface.

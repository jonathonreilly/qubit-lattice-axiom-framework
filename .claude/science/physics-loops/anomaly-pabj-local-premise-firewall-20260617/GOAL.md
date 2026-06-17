# Goal

Unlock the `anomaly_forces_time_theorem` audit lane without auditing or
retagging the ledger.

The concrete source-side blocker is that the parent theorem declared P-ABJ
locally but also carried a markdown dependency edge to the separate
`ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`
child row. That child is independently audited conditional and already has
separate repair PRs for its gamma5 and hypercharge/completion sides.

This block keeps P-ABJ external and local to the parent theorem, removes the
child-row markdown dependency edge from the parent, and adds a runner guard so
the source-graph firewall is executable.

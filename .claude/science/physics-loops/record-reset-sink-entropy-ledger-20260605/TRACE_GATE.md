trace_class: upstream_support
target_claim_id: null
target_blocker_text: "reset-with-sink exports old fragment memory; future reset dynamics must account for discard/reblanking rather than treating clean reset as free"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "Route future work to sink blankness/preparation or physical reset dynamics with explicit handling of exported memory."

# Trace Gate

If true, this artifact supports the reset-production lane by making the sink
memory ledger explicit. It does not close physical dynamics or thermodynamic
cost. It supplies a branch-local review gate: any future clean-reset proposal
that drops the sink must declare a many-to-one erase/reblank step.

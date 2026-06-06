trace_class: upstream_support
target_claim_id: "record-pre-record-instrument-kernel-gate"
target_blocker_text: "How does the pre-record qubit state feed probabilities without turning post-record information back into probability?"
source_of_blocker_text: "user_goal / record dynamics premise classifier"
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Either derive/admit the instrument and Born trace rule, or pursue an IID/typicality firewall for frequency claims."

# Trace Gate

This artifact supports the record dynamics stack by giving a conditional
pre-record probability interface. It does not close the probability-origin
bridge because the instrument and Born trace rule are premises.

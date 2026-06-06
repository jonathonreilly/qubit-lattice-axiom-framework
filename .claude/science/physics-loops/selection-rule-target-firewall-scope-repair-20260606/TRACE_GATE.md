trace_class: direct_blocker_closure
target_claim_id: post_record_selection_rule_target_vector_firewall_2026-06-06
target_blocker_text: "Include the retained Record axiom and the supplied selection-rule interface authority, or narrow the claim to the finite supplied-rule witness only."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Independent audit can re-check the narrowed finite witness and clean supplied-selection dependency."

# Trace Explanation

This PR closes the blocker by taking the second allowed repair path. It does
not attempt a broad Record-alone theorem. It supplies the finite witness that
the same rational target can choose different kernels under different supplied
weights, so target vectors and weights are rule inputs inside this finite
interface.

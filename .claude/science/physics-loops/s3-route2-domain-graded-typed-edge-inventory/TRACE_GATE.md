trace_class: upstream_support
target_claim_id: quark_route2_source_domain_bridge_no_go_note_2026-04-28
target_blocker_text: "runner hard-codes CURRENT_TYPED_EDGES rather than deriving the inventory"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "review whether the generated domain-graded inventory certificate is enough to retire the configured-inventory dependency in later audit handling"

## Explanation

This block supports a known audit-facing dependency of the Route-2
source-domain bridge no-go.  It does not derive the missing cross-domain
bridge or the endpoint triple.

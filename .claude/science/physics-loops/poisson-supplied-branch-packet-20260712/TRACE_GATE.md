trace_class: direct_blocker_closure
target_claim_id: poisson_self_field_supplied_branch_core_bounded_note_2026-06-18
target_blocker_text: "include scripts/poisson_self_field.py and its SHA-pinned cache in the restricted packet, then re-audit the primary runner's load-bearing dynamic helper calls"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independently re-audit the same bounded note with the repaired restricted packet"

# Trace explanation

Both dependency resolvers now register the helper explicitly. A rendered audit
prompt contains the complete helper source and fresh cache, exposing `grow`,
`_make_poisson_field`, `_solve_poisson_2d`, `_prop_beam`, `_cz`, `_dp`, and the
constants used by the primary certificate. The artifact reaches the exact
auditor blocker; it does not reach any broader gravity derivation claim.

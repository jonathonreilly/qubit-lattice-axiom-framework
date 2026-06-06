trace_class: direct_blocker_closure
target_claim_id: rp_rho_ref_radon_nikodym_compatibility_note_2026-05-20
target_blocker_text: "missing_bridge_theorem: audit a retained bridge identifying rho_ref|_Lambda with tau_Lambda and, for Wilson use, a carrier representation H_Wilson,Lambda in A_Lambda."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem_source_repair
next_trace_action: "Send to Codex reviewer and independent re-audit; downstream rho_ref/Wilson bridges remain open."

# Explanation

This branch does not attempt the downstream bridge. It instead removes those
bridge premises from the load-bearing theorem and provides a runner-backed
finite theorem relative to `tau_Lambda`.

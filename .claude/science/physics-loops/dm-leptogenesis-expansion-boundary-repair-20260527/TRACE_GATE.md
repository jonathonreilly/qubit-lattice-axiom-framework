trace_class: direct_blocker_closure
target_claim_id: dm_leptogenesis_expansion_axiom_boundary_note_2026-04-16
target_blocker_text: "missing_bridge_theorem: supply a retained theorem or non-hard-coded runner proving eta is uniquely fixed by H_rad(T) after the listed ingredients are closed."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should check whether the repaired runner's direct ODE computation satisfies the requested non-hard-coded uniqueness certificate; upstream transport/Hrad theorem rows still require audit."

# Trace Explanation

The prior runner asserted the decisive boundary-collapse checks with `True`.
This branch computes `eta[H]` from a supplied expansion profile, verifies
repeatability for the same profile, and verifies sensitivity to a different
normalized profile. That directly addresses the non-hard-coded runner part of
the blocker.

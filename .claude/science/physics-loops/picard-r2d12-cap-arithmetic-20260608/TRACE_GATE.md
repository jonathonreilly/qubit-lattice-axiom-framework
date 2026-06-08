trace_class: direct_blocker_closure
target_claim_id: plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_theorem_note_2026-05-17
target_blocker_text: "correct the ORDER=52 cap arithmetic from min(47,47) to min(47,48), then rerun the same restricted audit."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem_note_correction
next_trace_action: "Submit the corrected note for reviewer extraction and independent re-audit."

The correction is non-load-bearing for the rank result because `min(47,48)` still equals `47`, matching the runner's displayed `47 x 39` matrix and full rank.

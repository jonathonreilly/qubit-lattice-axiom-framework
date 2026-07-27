trace_class: direct_blocker_closure
target_claim_id: dm_selector_first_shoulder_exit_threshold_support_note_2026-04-21
target_blocker_text: >-
  For each recovered lift, tau_b(i) = log(1 + b_i); on the recovered bank the
  minimum is unique, belongs to lift 0, lies inside the stabilization window,
  and V_tau at that breakpoint makes lift 0 the unique minimizer.
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: >-
  Independently re-audit the source note at claim_type open_gate; do not infer
  a physical threshold law.

The closure applies exactly to the quoted algebraic step. It does not reach the
stronger physical-selector residual `tau_phys=tau_b,min`.

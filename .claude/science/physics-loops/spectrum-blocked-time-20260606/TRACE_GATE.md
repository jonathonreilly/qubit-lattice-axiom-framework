trace_class: direct_blocker_closure
target_claim_id: axiom_first_spectrum_condition_theorem_note_2026-04-29
target_blocker_text: "missing_bridge_theorem: add an explicit blocked-time-spacing normalization bridge identifying a_tau as the two-step block spacing, or change H and m_gap to use 1/(2 a_tau), then align the runner with T_hat^2."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem_and_runner_repair
next_trace_action: "Independent review/audit should verify the repaired note and runner, then decide whether the row can move from audited_conditional."

closure_argument: >
  The source note now uses H = -(1/(2 a_tau)) log(T/M_T) and
  m_gap = -(1/(2 a_tau)) log(lambda_1/M_T) for T := T_hat^2. The primary
  runner constructs T = exp(-2 a_tau H_lat), reconstructs H with the same
  factor, and checks that the old 1/a_tau normalization is exactly 2H.

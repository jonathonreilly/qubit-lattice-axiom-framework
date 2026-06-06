trace_class: direct_blocker_closure
target_claim_id: sm_gstar_i12_nur_thermal_exclusion_bounded_note_2026-05-29
target_blocker_text: "also correct the 100 GeV margin and replace the O(1)-only phrasing with y_nu >= y_thr"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem_source_repair
next_trace_action: "Send to Codex reviewer and independent re-audit; do not change audit status on this branch."

# Explanation

The branch directly addresses the quoted source-level blocker:

- The 100 GeV margin is now about 4.3 decades, not about 4.6 decades.
- The `Gamma/H` value at 100 GeV is now `2.35e-9`.
- The route to `g_* = 112` is now the threshold condition
  `y_nu >= y_thr`, with the O(1) Yukawa case preserved only as a stronger
  steelman subcase.

This partially closes the audited source blocker. It does not retire the
empirical small-neutrino-mass import or assert an effective audit status change.

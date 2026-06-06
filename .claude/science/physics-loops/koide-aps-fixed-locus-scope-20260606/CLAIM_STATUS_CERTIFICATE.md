# Claim Status Certificate

target_claim_id: koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05
current_ledger_status_before_reaudit: audited_conditional
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: "The branch takes the audit-allowed narrowing route to the closed A/B fixed-locus/local-density algebra."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Verification:

- `python3 scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py`
  reports `TOTAL: 25 PASS / 0 FAIL`.
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py --check-only --allow-non-main`
  reports the cache fresh.

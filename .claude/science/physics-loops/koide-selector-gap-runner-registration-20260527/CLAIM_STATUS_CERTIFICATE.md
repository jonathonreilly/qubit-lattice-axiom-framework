# Claim Status Certificate

claim_id: `koide_cl3_selector_gap_note_2026-04-19`

actual_current_surface_status: `open`

trace_class: `direct_blocker_closure`

reachability_to_target: `partially_closes`

conditional_surface_status: `open_gate_after_reaudit`

hypothetical_axiom_status: `null`

admitted_observation_status: `m_* / kappa_* comparator admitted for route-miss diagnostics`

proposal_allowed: `false`

proposal_allowed_reason: this PR only makes the open-gate inventory
runner-backed and re-auditable; it does not close the selector gap.

audit_required_before_effective_retained: `true`

bare_retained_allowed: `false`

## Queue Result

After `bash docs/audit/scripts/run_pipeline.sh`:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `claim_type`: `open_gate`
- `runner_path`: `scripts/frontier_koide_cl3_selector_gap.py`
- `helper_runner_paths`: `scripts/frontier_higgs_dressed_propagator_v1.py`, `scripts/frontier_koide_selected_line_cyclic_response_bridge.py`
- `ready`: `true`


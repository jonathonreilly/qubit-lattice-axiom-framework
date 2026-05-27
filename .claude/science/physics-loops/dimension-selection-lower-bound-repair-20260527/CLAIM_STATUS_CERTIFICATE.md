# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The PR queues a narrowed lower-bound row for independent audit; it does not propose retained status or an axiom rewrite."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Target Row

- Claim id: `dimension_selection_note`
- Source: `docs/DIMENSION_SELECTION_NOTE.md`
- Runner: `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
- Claim type after pipeline: `bounded_theorem`
- Audit status after pipeline: `unaudited`
- Effective status after pipeline: `unaudited`
- Direct dependency: `dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25`
  (`retained_bounded`)

## Status Firewall

No retained/proposed-retained wording is used. Unique spatial `d = 3` remains
open pending a separate framework-internal upper-bound derivation.

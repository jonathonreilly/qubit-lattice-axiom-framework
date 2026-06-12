actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "mass-determinant-channel determinant-character phase erasure under supplied Record/readout interface"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch supplies the source-side determinant-readout bridge for re-audit, but audit owns effective status movement and the bridge is limited to the mass-determinant channel."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

- Record axiom boundary from `MINIMAL_AXIOMS_2026-06-05.md`: used only after a
  determinant readout context is supplied.
- Theta P2/K-CPT determinant-character lemma: parent row that consumes this
  bridge.
- Strong-CP selected-surface parent: cited as the mass-side target context, not
  promoted.

## Open Imports

- The determinant readout channel is supplied; this block does not derive that
  channel from bare baseline axioms.
- The gauge/action theta residual remains outside scope.
- The real-positive Wilson action surface remains outside scope.
- Arbitrary action-level observables are not shown to factor through the mass
  determinant.

## Firewalls

- No `docs/audit/data/**` edits.
- No Tier-A registry edit.
- No audit status update.
- No branch-local retained promotion.

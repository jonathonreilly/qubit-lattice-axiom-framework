---
trace_class: direct_blocker_closure
target_claim_id: work_history.ckm.ckm_mass_basis_nni_note
target_blocker_text: "The runner performs real matrix and ratio computations, but those computations are over hard-coded external quark masses, PDG comparator values, and fitted geometric coefficients. The quoted 1.14x |V_ub| agreement is therefore a numerical match after importing calibrated inputs, not a first-principles closure from the axiom."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: no_go
next_trace_action: "Independent re-audit should test the coordinate reconstruction identity, the legacy mixed-reconstruction matrix invariant, and the narrowed no-go scope."
---

The artifact directly reaches the named target. It finds that retiring the
auditor-listed numerical imports would still not close the positive claim:
the operation called normalization changes the texture because the converted
coefficient is inserted with the geometric rather than converted
reconstruction law. The exact no-go
therefore closes the same-texture reparameterization route and exposes the
open positive continuation as a separately interpreted and derived texture
deformation.

This is not frontier-only support and does not claim positive `V_ub` closure.

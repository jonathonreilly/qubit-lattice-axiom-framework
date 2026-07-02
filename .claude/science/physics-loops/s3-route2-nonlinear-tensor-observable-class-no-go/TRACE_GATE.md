trace_class: negative_route_pruning
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: >-
  unresolved readout exactness blocks a unique exact Theta_R -> Lambda_R
  coupling law on the current carrier.
source_of_blocker_text: user_goal_and_parent_note
reachability_to_target: prunes
artifact_role: no_go
route_pruned: >-
  finite tensor-polynomial nonlinear observables generated only from
  E-center-blind endpoint readout images and scalar contractions.
why_pruned: >-
  the blind generators have zero rho_E coefficient, and finite tensor powers,
  contractions, and polynomials cannot create rho_E dependence from constant
  generators.
not_pruned: >-
  nonblind nonlinear observables, source-domain rules, or readout primitives
  that actually evaluate E-center.
next_trace_action: >-
  Attack the nonblind E-center lift primitive directly, or package the exact
  remaining ambiguity for the theta-to-slice consumer.

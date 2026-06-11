trace_class: direct_blocker_closure
target_claim_id: gravity_clean_derivation_note
target_blocker_text: "missing_bridge_theorem: provide retained bridge theorems for L^{-1}=G_0, the gravitational source readout rho=|psi|^2, and the weak-field test-mass response S=L(1 - phi)."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Independent audit should audit the new weak-field source-response bridge first; if clean, re-audit gravity_clean_derivation_note with the new one-hop dependency."

notes: |
  The bridge supplies the three named weak-field pieces on the bounded linear
  response surface. It does not claim nonlinear gravity, physical G_Newton, or
  a strong-field/geodesic theorem.

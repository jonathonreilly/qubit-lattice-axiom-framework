trace_class: direct_blocker_closure
target_claim_id: generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06
target_blocker_text: "missing_bridge_theorem: add a one-hop retained theorem deriving the periodic translation-invariant Hartree-Fock plane-wave mutual-energy readout Vq(q)=-G/(eps(q)+mu^2), including boundary/normalization, from the retained staggered two-body mediator."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem_and_runner_certificate
next_trace_action: "Independent audit reviews whether the new exact-support bridge satisfies the missing-bridge requirement and may retag the target if it passes."

## Trace Explanation

The bridge proves the exact finite periodic formula required by the blocker:

- `Lap phi_q = eps(q) phi_q` on `Lambda_L=(Z/LZ)^3`;
- `K=-G(Lap+mu^2 I)^-1` has multiplier `Vq(q)=-G/(eps(q)+mu^2)`;
- the two-corner Slater density-density mutual energy is
  `(Vq(0)-Vq(k_i-k_j))/N`.

That is the missing source step named by the auditor. The PR does not perform the audit verdict.

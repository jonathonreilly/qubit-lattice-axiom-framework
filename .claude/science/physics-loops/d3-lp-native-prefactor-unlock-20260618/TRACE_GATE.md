trace_class: direct_blocker_closure
target_claim_id: d3_orbital_response_decomposition_bounded_theorem_note_2026-06-13
target_blocker_text: "The finite Peierls reference and LP integral are computed, but the note explicitly imports the standard Landau-Peierls formula and its -1/12 normalization rather than deriving or citing a retained accepted authority for them."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem_dependency_wiring
next_trace_action: "Reviewer/auditor should grade the native-prefactor companion first, then re-grade D3 as a consumer of that companion plus its independent finite-torus reference."

Explanation:

This block removes the raw scalar import from the D3 runner by consuming the
companion symbolic prefactor derivation. It does not by itself audit the
companion or assert retained status. The remaining blocker is now explicit:
whether the companion source theorem is accepted as bounded support for the
single-band lattice setting.

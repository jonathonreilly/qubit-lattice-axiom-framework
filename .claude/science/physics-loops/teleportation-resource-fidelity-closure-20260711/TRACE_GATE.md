trace_class: direct_blocker_closure
target_claim_id: teleportation_resource_fidelity_note
target_blocker_text: "For this fixed Bell-basis measurement and fixed Pauli-correction convention, the exact average fidelity obeys F_avg = (1 + 2 * <Phi+|rho|Phi+>) / 3, so the fixed-protocol threshold is <Phi+|rho|Phi+> > 1/2."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Run local review, then send the note/runner/cache to independent re-audit."

The note derives Bell-coherence cancellation, the resulting Pauli channel, and
the Haar average directly. The runner exhausts a linear basis for both the
resource and input operators, so arbitrary physical resources follow by
linearity. This reaches only the quoted bounded blocker.

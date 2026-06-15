trace_class: direct_blocker_closure
target_claim_id: axiom_first_kms_condition_theorem_note_2026-05-01
target_blocker_text: "the detailed bookkeeping is identical to Bratteli-Robinson Vol. II, Lemma 5.3.4"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Independent reviewer/auditor should inspect whether the native K1/K4 repairs remove the textbook-import objection for the finite KMS row; upstream RP and spectrum dependencies still require their own audit status."

## Notes

The exact source weakness also included the literal `(??)` line in the old K1
proof. This branch removes that gap by proving the insertion identity directly:

`tr(T^(L_tau-j) O T^j) = tr(T^L_tau O)`.

It also replaces the old K4 appeal to Bratteli-Robinson Theorem 5.3.30 with a
finite matrix-unit proof. This is source-side unlock work only, not a verdict.

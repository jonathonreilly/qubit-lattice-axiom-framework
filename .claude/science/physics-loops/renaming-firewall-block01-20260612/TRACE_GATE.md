trace_class: direct_blocker_closure
target_claim_id: multiple_audited_renaming_rows
target_blocker_text: "audited_renaming rows whose source content is a definition, alias, status handle, compatibility representation, or formal identity rather than theorem-grade derivation."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "For promotion, provide independent theorem-grade derivations instead of consuming these rows as retained theorem closures."

This block covers the highest-load uncovered renaming rows by making the
source-use boundary explicit. It does not edit generated audit results.

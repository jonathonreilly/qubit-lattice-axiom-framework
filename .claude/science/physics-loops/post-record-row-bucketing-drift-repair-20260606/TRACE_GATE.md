trace_class: direct_blocker_closure
target_claim_id: post_record_audit_evidence_ladder_row_bucketing_2026-06-06
target_blocker_text: "The source note claims stale bucket counts and the completed runner output reports SUMMARY: PASS=37 FAIL=2 after ledger growth and row renaming."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent review can check that the read-only row-bucketing runner now exits 0 and that no audit data or verdict files changed."

# Trace Gate

The failing audit row is a source/runner mismatch. The runner's classification core was already bucket-complete and read-only, but two guard assertions were stale:

- exact total row count pinned to an older ledger size;
- forced nonempty append/count or record-type support bucket after row renaming made both buckets empty.

This PR changes those checks to stable invariants and refreshes the cache. It does not write audit data or apply audit verdicts.

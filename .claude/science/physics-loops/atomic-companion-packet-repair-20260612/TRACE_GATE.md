trace_class: direct_blocker_closure
target_claim_id: work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18
target_blocker_text: "runner_artifact_issue: include the full helium Hartree and Jastrow runner sources and complete runner-cache certificates in the restricted packet, then rerun the audit under the narrowed diagnostic finite-box scope."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Submit for review/re-audit; no audit-ledger edits."

## Trace Explanation

The branch adds a source/cache verifier that checks the full hydrogen,
helium Hartree, helium Jastrow, and dependency-repair runner sources, verifies
their cache metadata against live source SHA-256 hashes, and asserts the quoted
readouts are present in completed zero-exit runner caches.

The artifact closes the stated runner-packet blocker only. It does not promote
the atomic companion beyond diagnostic finite-box work-history numerics.

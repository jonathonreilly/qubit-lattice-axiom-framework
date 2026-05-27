# Goal

Repair the current `audited_conditional` blocker for
`dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`.

The audit blocker said the primary runner could no longer be imported because
its transitive helper stack expected `canonical_h` from the raw PMNS projector
interface after that interface was narrowed.  The goal is to restore a
source-verifiable bounded interval witness without expanding the already
retained raw-interface row.

The target outcome is not a direct ledger retag.  The target outcome is a clean
source edit plus regenerated audit artifacts that make the row ready for a fresh
independent audit.

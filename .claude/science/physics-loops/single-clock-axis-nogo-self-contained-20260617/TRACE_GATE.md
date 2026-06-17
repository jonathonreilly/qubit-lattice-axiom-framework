trace_class: negative_route_pruning
target_claim_id: single_clock_axis_selection_from_record_durability_narrow_no_go_note_2026-06-11
target_blocker_text: "source graph directly consumed conditional/unready parent, cone, and anomaly sources for a no-go whose decisive steps can be recomputed locally"
source_of_blocker_text: audit_queue_selector
reachability_to_target: supports
artifact_role: no_go
next_trace_action: >
  Reviewer should extract the source repair, then the independent audit lane can
  decide whether the row is audit-ready and whether the no-go is accepted.

Reasoning:

The artifact does not prove B-AXIS or retire the single-clock parent. It prunes
the axis-label supplier routes by making the no-go packet native: exchange,
cone transport, chirality invariance, and source-edge discipline are checked in
the runner without direct reliance on the conditional parent, external cone
note, downstream anomaly row, or convention-example rows.

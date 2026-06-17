# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: quark_mass_ratio_note_2026-04-18
target_blocker_text: "queue row has runner_path=null even though scripts/frontier_quark_mass_ratio_review.py exists and passes"
source_of_blocker_text: audit_queue_selector
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Rebuild graph/queue after review so the primary runner path is visible to audit tooling."
```

If accepted, this should move the row from missing-runner blocked to
runner-backed/auditable. It does not claim full quark-spectrum closure.

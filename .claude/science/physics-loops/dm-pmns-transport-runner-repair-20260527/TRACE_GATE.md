# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16
target_blocker_text: "runner_artifact_issue -- direct import of scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py currently fails with ImportError for canonical_h from scripts/frontier_dm_leptogenesis_pmns_projector_interface.py. After repair, recheck whether the scoped interval witness is clean bounded computation or audited_numerical_match because the eta/eta_obs = 1 point is chosen by interpolation against ETA_OBS."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Fresh independent audit must decide the repaired bounded interval witness status."
```

The exact blocker was a stale transitive helper import.  The repaired primary
runner imports only `dm_leptogenesis_exact_common.py`; the generated audit queue
now lists that single helper and marks the row ready for audit.

# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - graph_braid_n3_fermion_sign_stays_nonfibered_narrow_theorem_note
  - koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_narrow_no_go_note_2026-06-02
target_blocker_text:
  - "runner_artifact_issue: rerun scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py in an environment with networkx installed and include the completed stdout/cache certificate for the 26 checks."
  - "runner_artifact_issue rerun scripts/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.py in an environment with networkx installed and attach the completed PASS/FAIL transcript."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should re-check both rows against the completed caches."
```

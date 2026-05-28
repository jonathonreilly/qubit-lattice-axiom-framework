# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - audit_backlog_note_2026-05-02
  - beyond_lattice_qcd_note
  - born_rule_from_gleason_busch_derivation_note_2026-05-20
  - cluster_decomposition_spatial_slab_bridge_theorem_note_2026-05-17
  - cross_sector_a_squared_koide_vcb_bridge_promoted_via_v8_theorem_note_2026-04-29
  - dimension_selection_lower_bound_bridge_v2_2026-05-20
target_blocker_text: "Latest audit conditionals cite missing bridge theorem, missing dependency edge, or dependency-not-retained blockers for these rows."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "Independent auditor re-audits the changed, narrowed rows from the generated unaudited queue."
```

The closure is not retained-positive closure. It is blocker-compatible
narrowing: the live claim no longer asks the current source surface to prove a
bridge it does not contain.

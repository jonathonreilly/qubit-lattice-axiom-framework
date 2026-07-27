# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: koide_frobenius_isotype_split_uniqueness_note_2026-04-21
target_blocker_text: "The uniqueness argument for the Frobenius inner product is incomplete, since checking that (tr A)(tr B) alone is degenerate does not exclude positive combinations with Tr(AB)."
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: no_go
next_trace_action: "Independently re-audit the narrowed no-go; do not restore the unconditional kappa=2 or Q=2/3 claim."
```

The repair reaches the quoted blocker directly. It exhibits the excluded
positive combination `B_{1,1}`, proves its global properties, and shows that
the AM-GM output varies with the surviving relative weight. It closes the
failed uniqueness framing by replacing it with the exact negative boundary;
it does not close the physical Koide value lane.

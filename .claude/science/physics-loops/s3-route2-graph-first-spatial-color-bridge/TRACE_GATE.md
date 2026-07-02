trace_class: negative_route_pruning
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "missing typed bridge from readout/source structure to c_TE=-8/9 / rho_E=21/4"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: >-
  Attack the same-domain signed E/T2 source/readout functional directly,
  forbidding observed endpoint values, fitted selectors, and color-fraction
  imports.

## Explanation

If true, this block prunes the route:

```text
graph-first SU(3) already types F_adj=8/9 as c_TE=-8/9.
```

It does not close the parent endpoint. The exact trace movement is narrower:
the block shows that graph-first `SU(3)` routes `8/9` to total
traceless-adjoint over total `End(R^3)`, while Route-2 `c_TE` lives inside the
spin-2 E/T2 readout and needs a signed functional.

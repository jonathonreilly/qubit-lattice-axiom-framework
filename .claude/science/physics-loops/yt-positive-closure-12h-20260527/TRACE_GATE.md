# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: yt_positive_closure_pr1980
target_blocker_text: "derive accepted same-surface radial generator dynamics fixing lambda_top=1/sqrt(2), physical zero-singlet top-readout/sign law excluding P_0, or accepted strict same-source top/W pole-row data with contact/FV/IR/model-class controls"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "derive allowed same-surface radial/readout/backend laws without forbidden anchors, or produce accepted strict top/W pole rows"
```

Cycle 29 tests whether a reversible C3 Markov/Laplacian source law can be
promoted into the current campaign's same-surface top row.

It cannot. The finite witness uses

```text
Q_r = r(C+C^2-2I),        L_r = -Q_r.
```

The Markov semigroup has `P_0` as the stationary/Perron line, while the
nontrivial modes are exactly degenerate. Removing the identity part and
normalizing the connected generator gives the already-derived `B_x` ray up to
sign. The first open gate remains an accepted physical top-readout law
excluding `P_0`, accepted `lambda_top=1/sqrt(2)` radial generator dynamics
with backend/projectors/matrix elements, or strict top/W pole rows with
controls.

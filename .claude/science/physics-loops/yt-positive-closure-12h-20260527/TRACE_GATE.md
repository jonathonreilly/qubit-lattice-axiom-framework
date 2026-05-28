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

Cycle 28 tests whether ordinary one-Higgs generation-matrix normalization can
be promoted into the current campaign's same-surface C3 coefficient/radial law.

It cannot. The finite witness preserves the one-Higgs carrier skeleton,
neutral Higgs radial factor, W denominator, and granted C3 response while
varying the matrix-norm convention:

```text
C3-unit coefficient:     eta=1
unit singular/Frobenius: eta=sqrt(6)
unit three-gen average:  eta=sqrt(2)
```

Only the first convention gives the target row. Selecting it is therefore the
missing coefficient-to-C3-source law, not a consequence of generic
normalization. The first open gate remains an accepted law fixing
`eta=1`/`lambda_top=1/sqrt(2)`, an accepted zero-singlet top-readout law with
backend/projectors/matrix elements, or strict top/W pole rows with controls.

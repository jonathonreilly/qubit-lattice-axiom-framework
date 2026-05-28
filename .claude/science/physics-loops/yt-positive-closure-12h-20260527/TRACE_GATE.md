# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: yt_positive_closure_pr1980
target_blocker_text: "derive/certify the coefficient-bearing same-surface top sector matrix element dM_t/dell = A/sqrt(12)"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "derive accepted same-surface radial generator dynamics plus a physical top-readout law excluding P_0, or produce accepted strict top/W pole rows with controls"
```

Cycle 21 tests whether the information geometry behind the C3
hard-boundary/readout support candidates can do what the bare block-rank
shortcut could not: derive the physical radial generator factor
`lambda_top=1/sqrt(2)`.

```text
q(s) = (s,(1-s)/2,(1-s)/2)    versus    (s,1-s).
```

The fine reflection-even C3 line-simplex curve and the binary `P_0/P_nt`
quotient have the same Fisher metric:

```text
ds^2 / [s(1-s)].
```

So coarse-graining the two nontrivial lines into `P_nt` does not introduce a
root-rank factor. Fisher-unit normalization of the C3 line-score vector does
produce a nontrivial-line score magnitude `1/sqrt(2)`, but that is a
source-coordinate unit. Applied only to the top row it changes the model
surface and gives the wrong same-source readout; applied to the whole source
it cancels from the top/W ratio. Inside `P_nt`, `B_x` is scalar, so the
centered internal Fisher score is zero:

```text
B_x P_nt = -P_nt/sqrt(6).
```

This trace prunes only the shortcut from C3 RN/Fisher quotient/source geometry
to radial generator factorization. It does not close the target. Positive
closure still requires accepted radial/readout/sign laws on the same surface,
or accepted strict same-source top/W pole rows with contact, FV/IR, and
model-class controls.

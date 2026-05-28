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

Cycle 22 tests whether finite real C3 representation theory can supply the
remaining zero-singlet top-block law. The exact decomposition is:

```text
R[C3] = P_0 + P_nt.
```

Here `P_0` is the one-dimensional trivial real irrep and `P_nt` is the
faithful two-dimensional real irrep. Representation theory therefore makes
the desired block visible, but it does not identify the physical Y_T top block
with the faithful/nontrivial summand. That identification is an added
top-readout law.

The source responses are:

```text
Tr(P_0 B_x)       =  2/sqrt(6)
Tr((P_nt/2) B_x)  = -1/sqrt(6)
```

Even after importing the `P_nt` readout law, the top generator family

```text
V_top(lambda_top) = lambda_top A B_x
```

still leaves `lambda_top` free. The target row needs
`lambda_top=1/sqrt(2)`. This trace prunes only the shortcut from real
irrep/dimension/faithfulness facts to the accepted top block and coefficient
row. Positive closure still requires accepted radial/readout/sign laws on the
same surface, or accepted strict same-source top/W pole rows with contact,
FV/IR, and model-class controls.

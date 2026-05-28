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

Cycle 20 tests the block-rank shortcut after the Fisher/LSZ radial-generator
shortcut was pruned. It grants the best C3 support premise for the sake of
argument:

```text
support(top) <= P_nt,    rank(P_nt)=2,    B_x P_nt = -P_nt/sqrt(6).
```

The root-rank number is visible:

```text
1/sqrt(rank(P_nt)) = 1/sqrt(2).
```

But the actual matrix elements are rank-blind:

```text
|<psi|A B_x|psi>| = A/sqrt(6)        for unit psi in P_nt,
|Tr((P_nt/2) A B_x)| = A/sqrt(6).
```

Hilbert-Schmidt block conventions give `A/sqrt(3)` or return `A/sqrt(6)`;
the target `A/sqrt(12)` appears only after adding the root-rank response
average itself. That added average is the missing physical radial generator
law, not a derivation from current block algebra.

This trace prunes only the shortcut from block rank to radial generator
factorization. It does not close the target. Positive closure still requires
accepted radial/readout/sign laws on the same surface, or accepted strict
same-source top/W pole rows with contact, FV/IR, and model-class controls.

# Trace Gate

```yaml
trace_class: negative_route_pruning
target_claim_id: yt_positive_closure_pr1980
target_blocker_text: "Forbidden proof inputs include old Ward authority, plaquette/u0, alpha_LM, fitted selectors, target insertion, and observed top/W/Z masses"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "derive allowed same-surface radial/readout/backend laws without forbidden anchors, or produce accepted strict top/W pole rows"
```

Cycle 24 tests whether the newly noticed `origin/main` declared-anchor Y_T
bounded subchain can be imported as a proof input for this campaign.

It cannot. The origin/main packet is retained-bounded only over declared
anchors, including:

```text
<P>, plaquette/u0, alpha_LM, kappa_EW, Ward-boundary/Clebsch inputs.
```

Those anchors are forbidden or still open for this campaign. The origin/main
zero-import row is decoration under the declared-anchor bounded subchain and
keeps the plaquette and `kappa_EW`/selector dependencies outside full closure.

This prunes only the shortcut:

```text
use origin/main declared-anchor Y_T bounded subchain as current campaign
closure proof.
```

It does not challenge the origin/main retained-bounded audit status and does
not use the declared anchors as proof inputs. The allowed routes remain new
strict top/W pole rows, accepted same-surface backend/projector/matrix-element
dynamics, or accepted radial/readout dynamics for `P_nt`.

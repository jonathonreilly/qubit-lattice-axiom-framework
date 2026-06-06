# Handoff

This branch salvages the eta-holonomy lane by landing the exact base
`Z_2` area-flux theorem and refusing the unsupported braid-invariant no-go from
closed PR #2207.

Reviewer focus:

- Confirm the note does not assert the compared detour swaps are the same
  element of `B_2(Z^3)`.
- Confirm the runner checks the spin-diagonal identity, uniform `-1`
  curvature, rectangular area law, and graph-as-1-complex boundary.
- Confirm the remaining blocker is explicit: supply a retained-grade or
  packet-contained `UD_2(Z^3)` homotopy bridge, or keep eta scoped to base flux.

PR URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2805

PR verification:

- Base: `main`
- Head: `physics-loop/eta-holonomy-base-flux-scope-boundary-20260606`
- Mergeability: `MERGEABLE`
- Merge state at verification: `UNSTABLE` because `audit_pipeline` was still
  `IN_PROGRESS`, not because of a merge conflict.

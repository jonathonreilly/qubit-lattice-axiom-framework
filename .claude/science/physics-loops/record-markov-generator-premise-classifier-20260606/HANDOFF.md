# Handoff

This branch is stacked on PR #2800. It adds a premise classifier for record
Markov-generator dynamics.

Reviewer focus:

- Confirm the PR base is `physics-loop/record-markov-generator-embeddability-boundary-20260606`.
- Confirm the classifier does not derive a kernel, generator, clock, rate unit,
  Born/IID bridge, or dial setting.
- Confirm it makes the post-record information vs pre-record probability
  interface explicit.

PR URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2807

PR verification:

- Base: `physics-loop/record-markov-generator-embeddability-boundary-20260606`
- Head: `physics-loop/record-markov-generator-premise-classifier-20260606`
- Mergeability: `MERGEABLE`
- Merge state at verification: `UNSTABLE` because `audit_pipeline` was
  `IN_PROGRESS`, not because of a merge conflict.

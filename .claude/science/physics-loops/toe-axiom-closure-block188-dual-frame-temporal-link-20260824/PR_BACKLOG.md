# PR Backlog

At campaign freeze:

- PR #7349 is this Block-188 branch, opened at `1389ae17a3...` and stacked on
  the exact Block-187 head;
- PR #7348 is the exact Block-187 parent at `add760976c...`;
- PR #7347 is parallel fresh context and remains non-authoritative;
- PR #7346 is the gravity stack below Block 187;
- no review or landing action is part of this campaign;
- no review-loop invocation is permitted by the user's instruction.

Before successor work consumes Block 188, refresh PR #7349 and the exact
parent head. If either moves, rebind authority only after confirming that the
scientific inputs are unchanged.

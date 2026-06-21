# Opportunity Queue

## After Block139

1. Pick fresh source notes whose runner metadata is still missing or whose
   runner path cannot be replayed, excluding stale-cache items already covered
   by open PRs.
2. Inspect newly ready dispatch targets from the regenerated dispatch queue
   for source-side runner or dependency hygiene, without running audit-loop.
3. Prefer narrow source repairs over generated-surface refreshes unless a
   generated surface is stale relative to current source.

## Skip List

Do not refresh older open PRs onto fast-moving `main`. The reviewer lane will
update or cherry-pick useful science/tooling from them.

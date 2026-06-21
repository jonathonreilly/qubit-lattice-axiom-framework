# Opportunity Queue

1. Continue mining unaudited high-priority rows whose source notes mention a
   single dedicated runner but lack `runner_path` in the regenerated graph.
2. Consider audited runner-metadata misses only when the metadata repair is
   worth forcing independent re-audit.
3. Skip generated pipeline refreshes already represented by open PRs unless a
   new source edit needs regenerated surfaces.
4. Do not refresh old PR branches onto fast-moving `main`; reviewer lane owns
   cherry-pick/update.

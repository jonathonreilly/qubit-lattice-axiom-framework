# Opportunity Queue

After this block:

1. Re-scan conditional rows on latest `origin/main` and skip rows already
   covered by open repair PRs.
2. Prefer blockers that ask for missing source packets, stale runner caches,
   dependency links, or narrow theorem corrections.
3. Defer rows requiring new topology/geometry bridges unless no source-side
   unblocks remain.

# Opportunity Queue

## Current Ranking After Block123

1. Rescan current `origin/main` for live audit-queue rows whose source note or
   paired runner can be repaired without applying audit verdicts.
2. Inspect packet diagnostics for remaining helper-import gaps that are not
   solved by literal `load_frontier` parsing.
3. Prefer source-side runner metadata or packet-completeness repairs that can
   be verified by direct runner, pipeline, strict lint, and generated-clean
   checks.

## Skip List

Already-open audit-unblock PR targets must be skipped unless explicitly
stacking on that branch:

- #4486 block116 causal impact
- #4487 block117 QCD running
- #4488 block118 DM PMNS mininfo
- #4489 block119 LH traceless
- #4490 block120 Koide r-half no-go metadata
- #4491 block121 Koide lightcone metadata
- #4492 block122 alpha_s universal beta metadata
- #4493 block123 dynamic helper runner paths
- #4476 alpha_s Sommer static potential root kernel
- #4478 alpha_s heavy threshold matching kernel

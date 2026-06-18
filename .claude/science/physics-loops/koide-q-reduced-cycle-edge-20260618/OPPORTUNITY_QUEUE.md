# Opportunity Queue

| Rank | Target | Status | Reason |
|---:|---|---|---|
| 1 | Koide Q-reduced 2-node cycle edge | Done in this branch | Current queue has a cycle-break target with `max_transitive_descendants=83`; repair is source-side and non-duplicate. |
| 2 | Larger CKM/quark cycle families | Covered by PR #4230 | Do not duplicate existing source-edge repair PR. |
| 3 | Remaining seven audited conditionals | Covered or hard-open | Existing PRs cover R-eta, single-clock, Lorentz, Koide toy, plaquette beta6, P-dep, and partial DM Schur blockers. |
| 4 | Physical Koide reduced-carrier theorem | Open frontier science | Could unlock more than this source-edge repair but requires a real new bridge, not a quick hygiene patch. |

Next action after this PR: let review/audit process cycle-edge repairs, then
re-scan the committed queue for remaining cycles and conditionals.

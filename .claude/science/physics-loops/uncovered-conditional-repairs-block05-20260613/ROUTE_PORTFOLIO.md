# Route Portfolio

## Route A: Preserve Narrowed Source Repairs

Keep the three still-relevant conditional repair targets from the old block05
branch and discard unrelated stale branch contents.

Result: selected. This avoids reviving broad stale conflicts while preserving
the useful source-side repairs.

## Route B: Rebase The Old Broad Branch

Rejected locally. The old branch conflicted across unrelated files after main
moved, including broad generated/cache surfaces. Replaying it would add audit
noise rather than unlock the current remaining conditionals.

## Route C: Split Into Three New PRs

Possible but lower leverage because PR #3825 already exists for this coherent
block and the three targets share the same post-audit conditional repair role.

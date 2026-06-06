# Handoff

## Current Status

Bounded-support / finite sink-memory entropy-ledger block ready for stacked
review. This block is stacked on PR #2775.

## Result

Reversible reset with a blank sink preserves full finite label entropy by
moving old fragment memory into the sink. Ignoring, discarding, or reblanking
the sink is a separate many-to-one operation.

Checks:

- Runner: `SCORECARD PASS=70 FAIL=0`
- Compile: pass
- `git diff --check`: pass
- Targeted wording sweep: pass

## Boundaries

- Does not derive sink blankness or thermodynamic cost.
- Does not derive physical reset dynamics, rates, clock, probabilities, or a
  dial setting.
- Does not update repo-wide authority surfaces.

## Next Action

Commit, push, open a stacked PR, and then pivot to the next reset residual or
another high-value dynamics lane.

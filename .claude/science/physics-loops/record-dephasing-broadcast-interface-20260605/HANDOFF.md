# Handoff

## Current Status

Bounded-support / dephasing-broadcast interface block ready for stacked review.
This block is stacked on PR #2788.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2790

## Intended Result

The nonselective broadcast/dephasing state preserves probabilities as weights
and local marginals, while a selective event remains necessary for a single
post-record atom/history append.

Checks:

- Runner: `SCORECARD PASS=33 FAIL=0`
- Compile: pass
- `git diff --check`: pass
- Targeted wording sweep: pass

## Boundaries

- Does not derive outcome selection, Born frequencies, physical collapse,
  clock/rate, reset cost, probabilities, or a dial setting.
- Does not update repo-wide authority surfaces.

## Next Action

Continue to selective instrument atom criteria or another dynamics target.

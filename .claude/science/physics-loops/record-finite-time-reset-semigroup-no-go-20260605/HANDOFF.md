# Handoff

## Current Status

No-go / finite-time reset semigroup block ready for stacked review. This block
is stacked on PR #2781.

## Intended Result

The exact reset channel is singular as a superoperator. A finite-time
exponential of a finite bounded generator is invertible. Therefore exact reset
cannot be claimed as finite-time bounded-generator dynamics.

Checks:

- Runner: `SCORECARD PASS=43 FAIL=0`
- Compile: pass
- `git diff --check`: pass
- Targeted wording sweep: pass

## Boundaries

- Does not derive a Hamiltonian, bath, thermodynamic cost, finite-time rate,
  clock, low-record boundary, probabilities, or a dial setting.
- Does not block asymptotic damping, discrete reset channels, singular limits,
  or non-Markovian/open-boundary dynamics.
- Does not update repo-wide authority surfaces.

## Next Action

Commit, push, open a stacked PR, and then pivot to an asymptotic reset ledger
or another high-value lane.

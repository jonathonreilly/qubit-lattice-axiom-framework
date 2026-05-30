# Goal-Mode Attack Plan: 3+1 Positive Closure Repair

## Target Outcome

Repair the anomaly-forces-time lane from stale "bare ABJ admission" wording to
the strongest honest current-surface closure.

## First-Principles Decomposition

The desired parent conclusion is:

```text
d_s = 3 and d_t = 1
```

The proof splits into two independent pins:

1. **Odd-time pin:** ABJ anomaly-to-inconsistency plus chiral completion plus
   Clifford chirality parity gives `d_t in {1, 3, 5, ...}`.
2. **Single-clock pin:** single-clock codimension-1 evolution excludes
   `d_t > 1`.

The intersection is exactly `{1}`.

## Current Repo Facts

- The old parent note is stale: it says the ABJ premise has no successor
  internalization after PR 402 closed.
- Current main has a successor accepted-premise bridge:
  `ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`.
- Current main also has partial internalization of the U(1) Jacobian branch and
  a retained-bounded correction of the residual.
- This branch added the square-block no-go showing the standard finite
  even-torus `epsilon` index cannot retire the residual.

## Execution Order

1. Add a current-surface closure repair note that composes:
   - the accepted ABJ premise bridge,
   - retained Clifford volume chirality parity,
   - single-clock codimension-1 exclusion,
   - the existing exact anomaly arithmetic.
2. Add a runner that checks the composition, current artifact presence, and
   claim boundary.
3. Update the parent theorem's top claim-scope prose so it no longer claims
   there is no successor to PR 402.
4. Keep status bounded unless ABJ and single-clock are both derived/audited
   without accepted premises.
5. Run the theorem runner, existing parent/ABJ runners, audit pipeline, strict
   lint, and git hygiene checks.

## Escalation Rule

If accepted-premise bounded closure is not enough, the next unbounded route is
the taste-singlet/Adams staggered index permission theorem.  That is a new
science route, not a repair job.

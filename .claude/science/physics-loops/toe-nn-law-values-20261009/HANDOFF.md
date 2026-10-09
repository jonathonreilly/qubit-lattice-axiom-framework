# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Done this cycle

Cycle 1, conditional on a two-qubit density, is unchanged. Full proper-cubic
covariance leaves dimension 2 and does not force the singlet. Runner there
remains `TOTAL: PASS=31 FAIL=0`.

Cycle 2 searches `origin/main` at `17a95e60d85` before the new computation.
Docs naming `(p, q, r)` and docs naming `CHSH` have empty intersection.
The September formation census leaves the weights free and does not evaluate
CHSH. No exact comparison with squares 4 and 8 was found.

On the declared six-axis product-class pair, with nonnegative `(p,q,r)` not
all zero and no density:

- coordinate CHSH square is exactly `8(p-q)^2/(9(p+q+4r)^2)`, at most `8/9`,
  never 4 and never 8
- setting-blind global sign has square `4(p-q)^2/(p+q+4r)^2`, equal to 4
  exactly when `r=0` and `pq=0`, and never 8
- every local readout with values in `[-1,1]` has magnitude at most 2, so
  its square is at most 4 and is not 8
- one-axis conditional signs have square `4(p-q)^2/(p+q)^2` when `p+q>0`,
  equal to 4 exactly when `pq=0`, and never 8

The classical value 2 is attained by the global sign on that boundary. The
value `2√2` is not attained. Weights stay free. This does not derive the
dynamics clause.

Runner: `TOTAL: PASS=55 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Cycle 1 commit `9f7ab95597` is already on the branch. Cycle 2 is pushed onto
the same branch for PR 9475. Do not merge it. Do not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

The menu comparison is now on this branch. Compute the exact CHSH maximum
of the directed six-parameter family inside the density representation.
Keep the density hypothesis explicit. Push onto PR 9475.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

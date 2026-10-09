# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Formation sentence, still present

`origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`, in
`docs/MINIMAL_AXIOMS_2026-06-29.md`, reading note (2):

> Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

That sentence is still the axiom text. No note was opened that only repeats
it. No hazard law was invented. The same memo's open-gate list still places
source/action outside the axioms. Cycle 5 does not close that gate.

## Done this cycle

Cycles 1–4 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`, and
`TOTAL: PASS=61 FAIL=0`. Do not repeat the CHSH specializations or the
readout split.

Cycle 5 searched that same `origin/main` commit for a quadratic scalar
action of one bond correlation. The 2026-06-17 cubic-anisotropy note counts
weights on the traceless symmetric block only. It is not this nine-entry
count. No merge with `origin/main` was made: the one newer main commit is
audit metadata, and `git merge-tree` reported no content conflict.

On a real `3×3` matrix with the signed-permutation action:

- the proper group has order `24` and the full group has order `48`
- both groups leave the same `4`-dimensional space of quadratic invariants
- a basis is the trace square, the traceless-diagonal square, the
  symmetric-off-diagonal square, and the antisymmetric square
- a `3-4-5` rotation, not a signed permutation, forces the middle ratio
  `9/2` on one tested pair
- on the directed pattern the symmetric-off-diagonal square is `0`, the
  antisymmetric square is `4 t^2`, and every invariant quadratic is even
  in `t`
- the two pure twists `t = ±1` give the same four values

The four ratios are not selected. The sign of `t` is not selected. The
matrix stays declared. This does not derive a source identification, the
derivative-dependent action, or the formation triple.

Runner: `TOTAL: PASS=44 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits `9f7ab95597`, `caa947d12d`, `a242b4a1f2`, and `2c87950822` are
already on the branch. Cycle 5 is pushed onto the same branch for PR 9475.
Do not merge it. Do not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

Do not repeat the formation sentence, the CHSH evaluations, the readout
split, or this four-channel count. The sign of `t` and the four quadratic
ratios stay unselected. A degree-3 count is not implied; search before
writing one. Do not invent a hazard law.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

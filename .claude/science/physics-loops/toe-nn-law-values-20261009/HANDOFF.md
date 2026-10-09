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
source/action outside the axioms. Cycle 7 does not close that gate.

## Done this cycle

Cycles 1–6 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`, and
`TOTAL: PASS=16 FAIL=0`. Do not repeat the CHSH specializations, the
readout split, the four quadratic channels, or the achiral-orbit path
factor.

Cycle 7 is unchanged. Its runner remains `TOTAL: PASS=30 FAIL=0`. Do not
repeat the linear split of `1 + kappa F`.

Cycle 8 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a quadratic partner-cap pencil on this alphabet. The `kappa^2` hits are
Majorana and curvature comparators, not this bond factor. No merge with
`origin/main` was made: `git merge-tree` reported no content conflict.

On pencils `1 + t (a X + b Y) + t^2 (c X + d Y)` with `X` and `Y` the odd
cap lines, coefficients in `{-2,-1,0,1,2}`, and partial neighbour
conditions:

- determinant `0` is the old shape `1 + kappa H` and is excluded (`129` tuples)
- the other `496` tuples always normalise at `t = 0`
- a nonzero rational is never the unique normalised value
- the counts are `32` only at `0`, `256` at two rationals, and `208` at three
- `(1, 0, 0, 1)` is only at `0`
- `(1, 1, 0, -2)` is exactly `{0, 1/2}`, and both are strictly positive
- `(1, 1, -1, -2)` is exactly `{0, 1/2, 1}`

`t = 1/2` is not a selected interaction. The constant rule remains. This
does not derive a source identification or the formation triple. A factor
that is not `1` at the parameter origin stays open.

Runner: `TOTAL: PASS=31 FAIL=0`.

## Earlier cycle 7, unchanged

Cycle 7 searched that same `origin/main` commit for a result that already
decides whether soldered covariance forces `kappa` on the orbit of
`(0, 1, 2)`. It does not. The order-blind note still leaves generic orbits
unclassified, and its exhibited factors leave `kappa` as a supplied scale.
No merge with `origin/main` was made: the one newer main commit is audit
metadata, and `git merge-tree` reported no content conflict.

On bond factors `1 + kappa F` with `F` independent of `kappa`, and with
partial neighbour conditions:

- covariance at a nonzero `kappa` does not contain `kappa`
- normalisation at one nonzero `kappa` holds if and only if it holds for
  every `kappa`
- no such product is normalised exactly on a nonempty finite set of
  nonzero values
- on the proper orbit of `(0, 1, 2)`, nonzero even quarter-turn families
  normalise only at `kappa = 0`
- each odd pure quarter-turn orbit line normalises for every `kappa`
- the unit positive-cap line is the axis-role bond product of cycle 6,
  and strict positivity on it is the interval `|kappa| < 1`
- the bond factor of a pure line depends on `kappa c^2`, not on a
  preferred pair `(kappa, c)`

`kappa` is not selected. This does not derive a source identification or
the formation triple. Cycle 8 takes the second-power steelman inside one
box and does not select a unique nonzero `t`. The orbits of `(1, 1, 2)`
and `(1, 2, 2)` stay open.

Runner: `TOTAL: PASS=30 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits `9f7ab95597`, `caa947d12d`, `a242b4a1f2`, `2c87950822`,
`9bd6713a1b`, `caff82f0cf`, and `5eb33f7edf` are already on the branch.
Cycle 8 is pushed onto the same branch for PR 9475. Do not merge it. Do
not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

Do not repeat the formation sentence, the CHSH squares, the readout split,
the four-channel count, the achiral-orbit path factor, the linear kappa
split, or this quadratic box. No unique nonzero `t` was selected. A factor
that is not `1` at the parameter origin stays open. Do not invent a hazard
law. Do not identify a cap line with a mass density.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

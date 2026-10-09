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
source/action outside the axioms. Cycle 6 does not close that gate.

## Done this cycle

Cycles 1–5 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, and `TOTAL: PASS=44 FAIL=0`. Do not repeat the
CHSH specializations, the readout split, or the four quadratic channels.

Cycle 6 searched that same `origin/main` commit for a record alphabet that
is not the bond correlation. The order-blind note of 2026-09-22 still says
that generic orbits beyond the exhibited rules are not classified. Its
chiral pair is the mirror union of `(1, 2, 3)`. No merge with `origin/main`
was made: the one newer main commit is audit metadata, and `git merge-tree`
reported no content conflict.

On the proper cubic orbit of `(0, 1, 2)`:

- the orbit has `24` points and equals its full signed-permutation orbit
- the transverse-sign factor of `(1, 2, 3)` is identically `0`
- the axis-role sign defines a bond product fixed by `diag(1, 1, -1)`
- at `kappa = 1/2` the three-site path is order-blind, the ends are
  independent, and the adjacent correlation is `1/72`
- `kappa` is not selected, and the alphabet is not a chiral pair

The matrix of cycles 1–5 is not used. This does not derive a source
identification or the formation triple. The orbits of `(1, 1, 2)` and
`(1, 2, 2)`, mixed alphabets, and higher-rank bond spaces stay open.

Runner: `TOTAL: PASS=16 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits `9f7ab95597`, `caa947d12d`, `a242b4a1f2`, `2c87950822`, and
`9bd6713a1b` are already on the branch. Cycle 6 is pushed onto the same
branch for PR 9475. Do not merge it. Do not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

Do not repeat the formation sentence, the CHSH evaluations, the readout
split, the four-channel count, or this achiral-orbit factor. `kappa` stays
unselected. Other 24-point orbits and higher-rank bond spaces stay
unclassified. Do not invent a hazard law. Do not identify a polynomial
channel with a mass density.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

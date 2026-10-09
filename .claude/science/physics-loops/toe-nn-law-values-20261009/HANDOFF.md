# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Done this cycle

Cycle 1, conditional on a two-qubit density, is unchanged. Full proper-cubic
covariance leaves dimension 2 and does not force the singlet. Runner there
remains `TOTAL: PASS=31 FAIL=0`.

Cycle 2 is unchanged. On the six-axis product-class pair, with no density,
the coordinate CHSH square is at most `8/9`, and no local `[-1,1]` readout
has square `8`. Runner there remains `TOTAL: PASS=55 FAIL=0`.

Cycle 3 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
before the new computation. A `git grep` for the directed stabilizer and for
`c_21-c_12` did not find a CHSH evaluation. The directed square is not on
`origin/main`.

On the declared directed pattern, with the density hypothesis kept explicit,
`r^2 = u^2 + t^2`:

- the Gram eigenvalues are `r^2`, `r^2`, and `v^2`
- positivity holds exactly when `|p+q| ≤ 1+v` and
  `(p-q)^2 + 4 r^2 ≤ (1-v)^2`
- the elementary CHSH square is `8 r^2` or `4(r^2+v^2)`, according as
  `r^2` or `v^2` is larger
- on the positive set that square is at most `8`, with equality exactly on
  the circle `p = q = 0`, `v = -1`, `u^2 + t^2 = 1`
- signed coordinate-axis settings also have square at most `8`; they attain
  `8` at the four points where `|u| = |t| = 1/√2`, and at the singlet their
  magnitude is at most `2`

Square `8` is attained and is not exceeded. It is not forced, and the
singlet is not the only point that attains it. The value `2√2` is the
elementary maximum on this conditional family. Weights and the twist stay
free. This does not derive the dynamics clause or the density.

Runner: `TOTAL: PASS=102 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits `9f7ab95597` and `caa947d12d` are already on the branch. Cycle 3 is
pushed onto the same branch for PR 9475. Do not merge it. Do not open a
second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

Do not repeat the directed square. The formation site, probability, and rate
are still unsupplied. Do not invent a hazard law. The next block should
search the axiom text first and stop if that text still does not provide
the triple.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

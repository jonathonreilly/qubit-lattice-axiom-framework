# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Formation sentence, still present

`origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`, in
`docs/MINIMAL_AXIOMS_2026-06-29.md`, reading note (2):

> Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

That sentence is still the axiom text. No note was opened that only repeats
it. No hazard law was invented.

## Done this cycle

Cycles 1–3 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, and `TOTAL: PASS=102 FAIL=0`. Do not repeat the
CHSH specializations.

Cycle 4 searched that same `origin/main` commit for a readout-weight or
chirality evaluation of the directed pattern. The handed-rule census is a
six-letter menu. The Moriya note is a supplied dynamics-clause ground
state. Neither states the partial trace of this pattern. The parent CHSH
note on this branch says a one-site reduction was not tested.

On the declared directed density:

- wing 1 reduces to `(I + q Z)/2` and wing 2 to `(I + p Z)/2`
- local projective Born weights are `(1 ± q n_z)/2` and `(1 ± p n_z)/2`
  and do not depend on `u`, `t`, or `v`
- a coordinate weight `W` contracts to
  `u(W_xx+W_yy) + v W_zz + t(W_yx-W_xy)`
- symmetric weights, including every same-direction weight, miss `t`
- `W_yx=1`, `W_xy=-1` equals `2t`
- `P = diag(1,-1,1)` has determinant `-1`, so it is not in the proper
  group of the bond-invariants note, and it replaces `t` by `-t`
- the positive pure twists `t = ±1` are separated by that readout, at
  `+2` and `-2`, and not by the local weights

The sign of `t` is not selected. The density and the instrument stay
supplied. This does not derive the dynamics clause or the formation triple.

Runner: `TOTAL: PASS=61 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits `9f7ab95597`, `caa947d12d`, and `a242b4a1f2` are already on the
branch. Cycle 4 is pushed onto the same branch for PR 9475. Do not merge
it. Do not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

Do not repeat the formation sentence, the three CHSH evaluations, or this
readout split. Gravity source and action remain the open supplier that
does not overlap the live Codex branches. Do not invent a hazard law. The
sign of `t` is still unselected.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

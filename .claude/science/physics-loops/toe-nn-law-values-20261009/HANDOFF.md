# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Done this cycle

Conditional on a two-qubit density and simultaneous proper-cubic Bloch
action, the invariant families are:

- full group, order 24: dimension 2, span of `I` and `σ·σ`
- directed axis stabilizer, order 4: dimension 6
- undirected axis stabilizer, order 8: dimension 3, span of `I`, `XX+YY`, `ZZ`

On `ρ_w = (I + w σ·σ)/4`, positivity is `w ∈ [-1, 1/3]` and the CHSH square
is `8 w^2`. The value `2√2` sits at `w=-1` only. The undirected family
achieves CHSH square 8 only at `(u,v)=(-1,-1)` and `(1,-1)`.

Runner: `TOTAL: PASS=31 FAIL=0`.

This prunes the route "cubic covariance forces the singlet." It does not
derive the dynamics clause, and it does not show that the admissibility
distribution is a density.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Disk was about 24Gi free after this
checkout. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commit `9f7ab95597` is on `origin/physics-loop/toe-nn-law-values-20261009`.
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475
Do not merge it. The citation manifest was regenerated from a fresh graph
(6870 nodes, 15419 edges) and `citation_graph.json` was deleted.

## Next exact action

1. Search `origin/main` for an exact CHSH value of the product-class menu
   laws `(p,q,r)`. The September formation census already leaves those weights
   free. Do not repeat that census.
2. If no exact comparison with CHSH squares 4 and 8 exists, compute one
   finite menu or records-only law on this same branch, without assuming a
   two-qubit density. Push onto PR 9475. Do not open a second PR unless the
   result is a different claim family.
3. If that comparison already exists, pivot to the directed six-parameter
   CHSH maximum inside the density family and keep the density hypothesis
   explicit.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.

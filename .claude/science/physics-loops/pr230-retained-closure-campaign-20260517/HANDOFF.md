# Handoff

Current branch: `physics-loop/pr230-retained-closure-campaign-20260517`.

Current base: `origin/claude/yt-direct-lattice-correlator-2026-04-30` at
`a7179acb5ce21f9fdf2e05af1139c8b6a6785699`.

Stacked review PR for Blocks120-121: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1439

PR #230 is open and draft.  Latest current-surface block is base Block119.
Base Block117 records absence of strict Schur/scalar-LSZ pole authority.  Base
Block118 gives exact Hamming-Dirichlet support for the finite taste-radial
`O_H` axis, but keeps accepted EW/Higgs action, scalar LSZ/source-overlap, and
strict `C_ss/C_sH/C_HH` pole rows absent.
Base Block119 adds a native finite Dirichlet action/LSZ probe as support plus
boundary; it still does not supply accepted action, scalar LSZ/source-overlap,
or physical pole rows.

Block120 has landed locally as an exact negative boundary.  It narrows the
remaining blocker to one strict same-surface positive disjunct and rules out
source-only or finite-row promotion as invariant `y_t` data on the current head.

Block121 adds a Schur/Feshbach finite-packet boundary: complete finite A/B/C
rows at the current qhat^2 nodes do not determine `K'(pole)` or the residue.
The Schur route still requires strict pole derivative/residue rows or an
accepted analytic continuation/model-class plus FV/IR/contact bridge.

Active next work: rerun gates after the base Block119 rebase, force-push PR
#1439, then rebase and renumber the follow-on Hamming-axis action/LSZ
normalization branch to Block122.

Do not claim proposed_retained unless the closure/retained/audit/status gates
pass and the claim certificate explicitly allows a proposal.

Refresh the loop-local lock before expiry with:

```sh
python3 scripts/automation_lock.py \
  --lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/campaign.lock.json \
  --meta-lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/.campaign.lock.guard \
  refresh --owner physics-loop --purpose pr230-retained-closure-campaign-20260517 --ttl-hours 1
```

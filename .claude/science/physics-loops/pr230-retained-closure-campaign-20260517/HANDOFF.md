# Handoff

Current branch: `physics-loop/pr230-retained-closure-campaign-20260517`.

Current base: `origin/claude/yt-direct-lattice-correlator-2026-04-30` at
`4d56838ce6f2ab668c3987fe664043fd1c8084b4`.

Stacked review PR for Blocks117-118: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1439

PR #230 is open and draft.  Latest current-surface block is Block116.  Block115
does not make W/Z executable; it records absence of the strict W/Z packet.
Block116 records absence of strict neutral H3/H4 transfer/coupling authority.

Block117 has landed locally as an exact negative boundary.  It narrows the
remaining blocker to one strict same-surface positive disjunct and rules out
source-only or finite-row promotion as invariant `y_t` data on the current head.

Block118 adds a Schur/Feshbach finite-packet boundary: complete finite A/B/C
rows at the current qhat^2 nodes do not determine `K'(pole)` or the residue.
The Schur route still requires strict pole derivative/residue rows or an
accepted analytic continuation/model-class plus FV/IR/contact bridge.

Active next work: pivot to a non-duplicate neutral H3/H4 physical-transfer or
source-coupling route.  Avoid re-recording Block116/heat-kernel support unless
the new artifact proves a narrower transfer/coupling nonidentifiability theorem
or finds a strict same-surface artifact after a fresh fetch.

Do not claim proposed_retained unless the closure/retained/audit/status gates
pass and the claim certificate explicitly allows a proposal.

Refresh the loop-local lock before expiry with:

```sh
python3 scripts/automation_lock.py \
  --lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/campaign.lock.json \
  --meta-lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/.campaign.lock.guard \
  refresh --owner physics-loop --purpose pr230-retained-closure-campaign-20260517 --ttl-hours 1
```

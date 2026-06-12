# Handoff

## What Changed

- Updated the GL(F) conditional discriminator to reflect current `main`:
  04-29 spin-statistics is `retained_bounded`, and the 05-16 Grassmann/free-CCR
  bridge is `retained`.
- Added runner [E] source-packet checks so stale status language and missing
  dependency ambiguity are machine-visible.
- Refreshed the runner cache.

## Why It Matters

The current audit ledger marks this high-descendant row `audited_conditional`
with a `missing_dependency_edge` note. This PR supplies the current one-hop
packet and preserves the honest conclusion: conditional on `GL(F)` only.

## Remaining Work

- Independent audit/review must decide whether this packet repair is enough to
  move the row out of missing-dependency conditional status.
- `GL(F)/FS` is still not derived, retained, or admitted.

## Verification

- `python3 scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py`
  returned `TOTAL: PASS=24 FAIL=0`.

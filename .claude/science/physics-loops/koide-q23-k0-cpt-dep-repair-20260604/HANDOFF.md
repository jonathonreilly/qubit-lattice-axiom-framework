# Handoff

## What Changed

- Removed the CPT exact real anti-Hermitian `D` packet from the load-bearing
  authority list.
- Added a dated repair note explaining that CPT is not used by the finite K0
  block-equivalence proof or runner.

## Why It Matters

The row was blocked by a sign issue in an unrelated cited authority. The
targeted equivalence is checked directly by the runner and does not depend on
that CPT corollary. Removing the unused authority closes this packet-level
dependency defect without broadening the claim.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.py`
- `python3 -m py_compile scripts/frontier_koide_q23_k0_real_block_equivalence_2026_05_30.py`
- `git diff --check`

## Remaining Blocker

- The physical per-block versus trace/dimension measure selector remains open.

## Next Action

Open this as a review PR.

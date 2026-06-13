# ACPHILAMBDA Hamming-Complementation Handoff

**Date:** 2026-06-13
**Branch:** `physics-loop/acphilambda-hw-equivariance-open-gate-20260613`
**Scope:** source-only open-gate unblock; no audit result or ledger edits.

## What changed

- The R-A relabeling universe is now stated as the order-48
  coordinate-permutation/bit-flip cube automorphism group
  `x_i -> x_{pi(i)} xor f_i`.
- The note explicitly says this is not `AGL(3,2)` and not arbitrary Boolean
  maps.
- The runner verifies that source-boundary statement and now reports
  `SUMMARY: PASS=18 FAIL=0`.

## Honest status

The row remains finite-surface support only. This PR does not derive a
physical species bridge, readout context, Tier-A registry action, or
charged-lepton value.

## Verification

```bash
python3 -m py_compile scripts/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.py
python3 scripts/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.py
python3 scripts/cached_runner_output.py scripts/frontier_acphilambda_hw_complementation_equivariance_2026_06_09.py --check-only
git diff --check
```

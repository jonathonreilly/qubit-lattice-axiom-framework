# Handoff

## What Changed

- Updated the source note's displayed cached-run table to match the refreshed
  runner cache.
- Corrected the U(1) Wilson-kernel Fourier coefficient convention to
  `exp(-beta) I_n(beta) > 0`.
- Refreshed the runner cache after the runner comment hash changed.

## Why It Matters

The finite `W^dag W` algebra packet was not refuted, but its source note had a
formula-inventory mismatch: stale displayed values and an incomplete U(1)
coefficient convention. This branch removes those avoidable blockers while
preserving the supplied-premise boundary.

## Verification

- `PYTHONPATH=scripts python3 scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py`
- `python3 -m py_compile scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py`
- `git diff --check`

## Remaining Blockers

- Compact-group Wilson-boundary positivity is still not proved here.
- The full mixed OS transfer representation is still supplied, not derived.

## Next Action

Open this as a review PR, then continue the conditional repair loop.

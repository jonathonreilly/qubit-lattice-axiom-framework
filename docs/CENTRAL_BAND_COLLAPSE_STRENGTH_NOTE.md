# Central-Band Collapse-Strength Note

**Date:** 2026-04-02  
**Status:** bounded calibration complete

This note records the corrected Born sweep over the stochastic-collapse
probability `p` inside the dense central-band hard-geometry pocket.

Script:
- [`scripts/central_band_born_collapse_strength_sweep.py`](../scripts/central_band_born_collapse_strength_sweep.py)

Harness:
- corrected three-slit 3D chokepoint graph
- central-band `|y| < 2` removal
- per-layer normalization enabled on the `LN` lanes
- corrected Sorkin `I3 / P` with the required `-P(empty)` term

Sweep:
- `N = 40, 60`
- `npl = 60`
- `p = 0.05, 0.10, 0.20`
- `6` declared matched seeds (effective `ok` count per row below)
- `8` realizations

## Strongest Retained Rows

Numbers below are synced to the current runner stdout (runner hash
`cec5ceff6dbe...` for `scripts/central_band_born_collapse_strength_sweep.py`,
helper hash `582cd51d2318...` for
`scripts/stochastic_collapse_born_calibration.py`). All `LN + |y| + collapse`
rows are below the `1e-10` machine-precision threshold.

| N | p | mean `|I3|/P` | max `|I3|/P` | ok | verdict |
|---|---:|---:|---:|---:|---|
| 40 | 0.05 | `8.56e-17` | `5.55e-16` | 4 | PASS |
| 40 | 0.10 | `8.33e-17` | `5.55e-16` | 4 | PASS |
| 40 | 0.20 | `1.01e-16` | `8.88e-16` | 4 | PASS |
| 60 | 0.05 | `1.90e-16` | `1.11e-15` | 6 | PASS |
| 60 | 0.10 | `1.80e-16` | `1.44e-15` | 6 | PASS |
| 60 | 0.20 | `1.73e-16` | `7.77e-16` | 6 | PASS |

The `ok` column is the number of seeds (out of the 6 declared) that produced
a valid graph for that row; only those seeds enter the mean and max. At
`N = 40` two of the six declared seeds drop the graph build; at `N = 60` all
six declared seeds contribute.

## Narrow Read

- All six `LN + |y| + collapse` rows are below the `1e-10` machine-precision
  threshold on the corrected `I3 / P` metric.
- The mean-vs-`p` ordering is not monotone and not aligned across the two
  `N` slices on this stdout:
  - at `N = 40`, the mean is smallest at `p = 0.10` (`8.33e-17`), with
    `p = 0.05` close behind (`8.56e-17`) and `p = 0.20` the largest mean
    (`1.01e-16`);
  - at `N = 60`, the mean is smallest at `p = 0.20` (`1.73e-16`) and largest
    at `p = 0.05` (`1.90e-16`).
- The `N = 60` direction reverses the older "lower `p` is cleaner" reading;
  on this stdout the supplied numbers do not pin a single best collapse
  probability across both slices.
- Seed accounting differs between the two `N` slices: `N = 40` rows quote
  `ok = 4` and `N = 60` rows quote `ok = 6`.

## Interpretation

This is a calibration result, not a new mechanism. The supplied stdout
supports only that all six `LN + |y| + collapse` rows in the swept
`p in {0.05, 0.10, 0.20}` x `N in {40, 60}` grid sit below the `1e-10`
machine-precision threshold on the corrected `I3 / P` metric. The
mean-vs-`p` differences are at the same `1e-16` magnitude as the
machine-precision floor, do not give a consistent direction across the two
`N` values shown, and are not load-bearing on this stdout.

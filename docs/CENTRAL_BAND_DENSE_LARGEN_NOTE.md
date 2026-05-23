# Central-Band Dense Large-N Joint Card Note

**Date:** 2026-04-03 (table re-synced 2026-05-23 from current runner stdout)  
**Status:** large-`N` extension of the dense central-band same-graph card

This note records the large-`N` extension of the dense central-band hard-
geometry lane on the same graphs.

Script:
[`scripts/central_band_dense_joint_largeN.py`](/Users/jonreilly/Projects/Physics/scripts/central_band_dense_joint_largeN.py)

## Setup

- corrected dense central-band graph family
- `N = 80, 100`
- `npl = 60`
- `y_cut = 2.0`
- `yz_range = 12.0`
- `connect_radius = 3.0`
- `4` matched seeds
- `8` Monte Carlo realizations for the collapse rows

## Strongest Retained Rows

The dense pocket survives to the large-`N` extension in this fixed geometry
in the Born metric; the same-graph gravity readout is negative at `N = 80`
and falls to near-zero / sign-ambiguous on the surviving single seed at
`N = 100`.

| N | mode | Born `|I3|/P` | `pur_min` / purity | gravity delta | ok seeds | note |
|---|---|---:|---:|---:|---:|---|
| 80 | `LN + |y|` | `0.000±0.000` | `1.000±0.000` | `-0.458±0.137` | 2 | Born-safe, gravity negative |
| 80 | `LN + |y| + collapse` | `0.000±0.000` | `0.698±0.206` | `-0.498±0.072` | 2 | collapse lowers purity, gravity still negative |
| 100 | `LN + |y|` | `0.000±0.000` | `1.000±0.000` | `-0.044±0.000` | 1 | one retained seed, gravity small-negative |
| 100 | `LN + |y| + collapse` | `0.000±0.000` | `0.732±0.000` | `-0.005±0.000` | 1 | one retained seed, gravity near-zero/sign-ambiguous |

Values are taken directly from `scripts/central_band_dense_joint_largeN.py`
stdout at its declared defaults (n-layers=80,100, n-seeds=4,
n-realizations=8, npl=60, yz-range=12.0, connect-radius=3.0, y-cut=2.0,
p-collapse=0.2). The `ok seeds` column records how many of the four seeds
retained both Born-safe and gravity readouts; at `N = 100` only a single
seed survives in either row, so the SE column reads `0.000` and the
gravity sign at `N = 100` should not be over-read.

## Narrow Read

- The dense central-band Born-safe pocket survives beyond `N = 60` in the
  Born metric: at `npl = 60` the corrected Born metric stays at machine
  precision for the retained large-`N` rows in this fixed geometry.
- The same-graph gravity readout is negative at `N = 80` for both
  `LN + |y|` (`-0.458±0.137`) and `LN + |y| + collapse` (`-0.498±0.072`),
  i.e. the gravity centroid does *not* trend toward the collapse-positive
  side in this dense pocket at `N = 80`.
- At `N = 100` only one of four seeds retains both readouts, so the
  gravity numbers are single-seed point estimates with no SE. The
  `LN + |y|` row reads `-0.044`; the `LN + |y| + collapse` row reads
  `-0.005`, which is sign-ambiguous at the displayed precision and is
  treated here as near-zero rather than as a positive collapse trend.
- This is still density-sensitive and should not be read as universal.
- The same-graph coexistence window therefore becomes very thin by
  `N = 80` and is not clearly retained at `N = 100` in the gravity sense.

## Interpretation

The clean large-`N` takeaway from the current runner stdout is:

- central-band hard geometry survives the corrected Born gate at
  `N = 80, 100`
- `LN + |y|` remains the Born-safe backbone of the pocket
- adding collapse does not break Born inside this dense pocket
- on the same-graph gravity side, both `N = 80` rows are negative; the
  `N = 100` rows are single-seed and read small-negative (`-0.044`) for
  `LN + |y|` and near-zero / sign-ambiguous (`-0.005`) for the collapse
  row, so the gravity readout does not support a "collapse-positive at
  large `N`" reading inside this dense pocket
- the row is therefore preserved only as a Born-safe pocket rather than
  a full joint coexistence law in either direction

This note supersedes any earlier framing of the `N = 100` collapse row as
gravity-positive. The current runner stdout reports `-0.005±0.000` for
that row, which is a sign flip relative to the prior `+0.097±0.000` entry
on a single retained seed; the narrative above is rewritten to match the
sign of the current run.

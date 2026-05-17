# Central-Band Dense Large-N Joint Card Note

**Date:** 2026-04-03  
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

The dense pocket survives to the large-`N` extension in this fixed geometry,
but the same-graph gravity side rolls over by `N = 80..100`.

| N | mode | Born `|I3|/P` | `pur_min` / purity | gravity delta | note |
|---|---|---:|---:|---:|---|
| 80 | `LN + |y|` | `0.000±0.000` | `1.000±0.000` | `-0.458±0.137` | Born-safe, gravity negative |
| 80 | `LN + |y| + collapse` | `0.000±0.000` | `0.698±0.206` | `-0.576±0.045` | collapse lowers purity, gravity still negative |
| 100 | `LN + |y|` | `0.000±0.000` | `1.000±0.000` | `-0.044±0.000` | narrow retained seed set, gravity rolls over |
| 100 | `LN + |y| + collapse` | `0.000±0.000` | `0.680±0.000` | `+0.097±0.000` | one retained seed, too thin to promote |

## Narrow Read

- The dense central-band Born-safe pocket survives beyond `N = 60` in the
  Born metric, but the same-graph joint row does not stay positive in gravity
  at `N = 80`.
- At `npl = 60`, the corrected Born metric stays at machine precision for the
  retained large-`N` rows in this fixed geometry.
- This is still density-sensitive and should not be read as universal.
- The same-graph coexistence window therefore becomes very thin by `N = 80`
  and is not clearly retained at `N = 100` in the gravity sense.

## Interpretation

The clean large-`N` takeaway is now:

- central-band hard geometry survives the corrected Born gate at `N = 80, 100`
- `LN + |y|` remains the Born-safe backbone of the pocket
- adding collapse does not break Born inside this dense pocket
- the same-graph gravity side rolls over in the large-`N` extension, so the
  row is preserved only as a Born-safe pocket rather than a full joint
  coexistence law

---

**Re-queued for re-audit 2026-05-17:** previous `audited_failed` verdict cited packet incompleteness (missing helper-script imports from the restricted packet). The audit pipeline now populates `helper_runner_paths` per [PR #1371](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1371) so the next audit pass receives the complete packet. Helpers now declared: ``. The current re-queue is mechanical — no science content changes — and is documented here so the hash drift is explicit.

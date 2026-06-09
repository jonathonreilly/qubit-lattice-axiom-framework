# Non-Label Grown Drift Basin Note

**Date:** 2026-04-06; live recompute artifact wired 2026-06-08
**Status:** bounded positive drift basin around the grown-row non-label signed-source transfer

## Artifact chain

- [`scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py`](../scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py)
- [`scripts/NONLABEL_GROWN_DRIFT_BASIN_DIAG.py`](../scripts/NONLABEL_GROWN_DRIFT_BASIN_DIAG.py)
- [`logs/2026-04-06-nonlabel-grown-drift-basin-sweep.txt`](../logs/runner-cache/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.txt)
- retained restore-basin anchor:
  [`docs/NONLABEL_GROWN_BASIN_NOTE.md`](NONLABEL_GROWN_BASIN_NOTE.md)

Runner behavior for audit replay:

- default: verify the frozen log drift/seed grid, zero/neutral gates, signed
  response, charge exponent, `9/9` safe-read count, mean exponent summary, and
  the SHA-fresh live recompute artifact/cache listed below
- `--recompute`: run the original live drift-basin replay
- [`scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py`](../scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py):
  SHA-pinned live recompute artifact for the same nine drift/seed rows, with
  exact row values and row-gate checks in
  [`logs/runner-cache/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.txt`](../logs/runner-cache/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.txt)

## Question

Does the geometry-sector / non-label connectivity idea survive a tiny drift
neighborhood around the retained grown row while keeping restore fixed near the
promoted value?

This note is intentionally narrow:

- fixed restore: `restore = 0.7`
- nearby drifts: `drift = 0.15, 0.20, 0.25`
- exact zero-source baseline
- exact neutral `+1/-1` cancellation
- sign orientation
- weak charge-scaling estimate

## Live Recompute Result

Fixed `restore = 0.70`, geometry-sector candidate:

| drift | seed | zero source | single `+1` | single `-1` | neutral `+1/-1` | double `+2` | charge exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `0.15` | `0` | `+0.000000e+00` | `-3.581520e-05` | `+3.580391e-05` | `+0.000000e+00` | `-7.164168e-05` | `1.000227` |
| `0.15` | `1` | `+0.000000e+00` | `-4.494183e-05` | `+4.493279e-05` | `+0.000000e+00` | `-8.989268e-05` | `1.000145` |
| `0.15` | `2` | `+0.000000e+00` | `-3.335466e-05` | `+3.334333e-05` | `+0.000000e+00` | `-6.672064e-05` | `1.000245` |
| `0.20` | `0` | `+0.000000e+00` | `-3.534838e-05` | `+3.533743e-05` | `+0.000000e+00` | `-7.070770e-05` | `1.000223` |
| `0.20` | `1` | `+0.000000e+00` | `-4.754447e-05` | `+4.753644e-05` | `+0.000000e+00` | `-9.509695e-05` | `1.000122` |
| `0.20` | `2` | `+0.000000e+00` | `-3.162960e-05` | `+3.161846e-05` | `+0.000000e+00` | `-6.327031e-05` | `1.000254` |
| `0.25` | `0` | `+0.000000e+00` | `-3.486320e-05` | `+3.485265e-05` | `+0.000000e+00` | `-6.973694e-05` | `1.000218` |
| `0.25` | `1` | `+0.000000e+00` | `-5.006931e-05` | `+5.006228e-05` | `+0.000000e+00` | `-1.001456e-04` | `1.000101` |
| `0.25` | `2` | `+0.000000e+00` | `-2.966616e-05` | `+2.965522e-05` | `+0.000000e+00` | `-5.934324e-05` | `1.000266` |

These are the exact values printed by the SHA-pinned live recompute cache,
rounded here to six significant figures for the amplitudes and six decimals
for the charge exponent. The older frozen replay remains a row-gate regression
check, but it is no longer the only completed evidence packet for this row.

## Frozen Result

All checked rows across seeds `0, 1, 2` pass:

| drift | seed | zero source | single `+1` | single `-1` | neutral `+1/-1` | double `+2` | charge exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `0.15` | `0` | `+0.000000e+00` | `-3.581785e-05` | `+3.580452e-05` | `+0.000000e+00` | `-7.163621e-05` | `1.000000` |
| `0.15` | `1` | `+0.000000e+00` | `-4.493534e-05` | `+4.492629e-05` | `+0.000000e+00` | `-8.989110e-05` | `1.000000` |
| `0.15` | `2` | `+0.000000e+00` | `-3.335325e-05` | `+3.334036e-05` | `+0.000000e+00` | `-6.671544e-05` | `1.000000` |
| `0.20` | `0` | `+0.000000e+00` | `-3.534838e-05` | `+3.533743e-05` | `+0.000000e+00` | `-7.070770e-05` | `1.000223` |
| `0.20` | `1` | `+0.000000e+00` | `-4.753707e-05` | `+4.752606e-05` | `+0.000000e+00` | `-9.510419e-05` | `1.000000` |
| `0.20` | `2` | `+0.000000e+00` | `-3.163285e-05` | `+3.162221e-05` | `+0.000000e+00` | `-6.326652e-05` | `1.000000` |
| `0.25` | `0` | `+0.000000e+00` | `-3.485833e-05` | `+3.484561e-05` | `+0.000000e+00` | `-6.974134e-05` | `1.000000` |
| `0.25` | `1` | `+0.000000e+00` | `-5.006985e-05` | `+5.005918e-05` | `+0.000000e+00` | `-1.001378e-04` | `1.000000` |
| `0.25` | `2` | `+0.000000e+00` | `-2.967155e-05` | `+2.966117e-05` | `+0.000000e+00` | `-5.934242e-05` | `1.000000` |

## Safe Read

The geometry-sector / non-label architecture does not only work on the single
retained grown row. It survives the nearest drift neighborhood at fixed
`restore = 0.7`:

- the zero-source baseline remains exactly zero
- the neutral same-point `+1/-1` control remains exactly zero
- the single-source response keeps the correct sign orientation
- the charge response stays linear to within the checked exponent

The drift axis is therefore not the immediate boundary for this retained
family. The basin is still narrow and selective, so this is not a
family-wide transfer claim, but it is a real local basin rather than a
one-row ridge.

## Final Verdict

**bounded positive drift basin**

## 2026-06-08 recompute-audit repair

The audit runner-artifact blocker asked for a SHA-pinned completed
`--recompute` cache or an independent derivation for the nine drift/seed
centroid-shift rows, with row gates asserted. The paired recompute artifact
reruns the live grown geometry-sector measurement, then re-checks the
zero-source gate, neutral-pair gate, sign orientation, double-charge sign, and
charge-exponent tolerance for all nine rows.

The default runner now also verifies that this recompute cache is present,
SHA-fresh against
`scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py`, exits
zero, reports `SCORECARD PASS=9 FAIL=0`, and contains the same nine passing
drift/seed rows.

This repair does not widen the theorem beyond the stated drift/seed grid at
fixed `restore = 0.70` and does not promote the basin to an unbounded family
theorem.

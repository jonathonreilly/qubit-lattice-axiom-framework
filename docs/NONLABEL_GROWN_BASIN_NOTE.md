# Non-Label Grown Basin Note

**Date:** 2026-04-06; live recompute artifact wired 2026-06-08
**Status:** bounded positive basin around the grown-row signed-source transfer

## Artifact chain

- [`scripts/NONLABEL_GROWN_BASIN_TARGETED.py`](../scripts/NONLABEL_GROWN_BASIN_TARGETED.py)
- [`logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt`](../logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt)

Runner behavior for audit replay:

- default: verify the frozen log row grid, zero/neutral gates, signed response,
  charge exponent, `3/3` safe-read count, and the SHA-fresh live recompute
  artifact/cache listed below
- `--recompute`: run the original live targeted replay
- [`scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py`](../scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py):
  SHA-pinned live recompute artifact for the same three restore rows, with
  exact row values and row-gate checks in
  [`logs/runner-cache/nonlabel_grown_basin_recompute_audit_2026_06_08.txt`](../logs/runner-cache/nonlabel_grown_basin_recompute_audit_2026_06_08.txt)

## Question

Does the old geometry-sector / non-label connectivity idea extend beyond the single
retained grown row into a tiny neighborhood for the fixed-field signed-source
transfer?

This note stays intentionally narrow:

- fixed drift row: `drift = 0.2`
- nearby restore values: `restore = 0.6, 0.7, 0.8`
- exact zero-source baseline
- exact neutral `+1/-1` cancellation
- sign orientation
- weak charge-scaling estimate

## Live Recompute Result

Seed `0`, geometry-sector candidate:

| restore | zero source | single `+1` | single `-1` | neutral `+1/-1` | double `+2` | charge exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `0.60` | `+0.000000e+00` | `-3.392850e-05` | `+3.391821e-05` | `+0.000000e+00` | `-6.786729e-05` | `1.000219` |
| `0.70` | `+0.000000e+00` | `-3.534838e-05` | `+3.533743e-05` | `+0.000000e+00` | `-7.070770e-05` | `1.000223` |
| `0.80` | `+0.000000e+00` | `-3.620003e-05` | `+3.618856e-05` | `+0.000000e+00` | `-7.241152e-05` | `1.000228` |

These are the exact values printed by the SHA-pinned live recompute cache,
rounded here to six significant figures for the amplitudes and six decimals
for the charge exponent. The older frozen replay remains a row-gate regression
check, but it is not the only completed evidence packet for this row.

## Safe Read

The geometry-sector / non-label architecture does not only work on the single
retained grown row. It survives the nearest restore neighborhood at fixed
`drift = 0.2`:

- the zero-source baseline remains exactly zero
- the neutral same-point `+1/-1` control remains exactly zero
- the single-source response keeps the correct sign orientation
- the charge response stays linear to within the checked exponent

## Final Verdict

**bounded positive basin**

## 2026-06-08 recompute-audit repair

The audit runner-artifact blocker asked for either a completed live recompute
of the three restore rows or an independent derivation of those row values.
The paired recompute artifact reruns the live grown geometry-sector
measurement, then re-checks the zero-source gate, neutral-pair gate, sign
orientation, double-charge sign, and charge-exponent tolerance.
The default runner now also verifies that this recompute cache is present,
SHA-fresh against `scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py`,
exits zero, reports `SCORECARD PASS=3 FAIL=0`, and contains the same three
passing restore rows.

This repair does not widen the theorem beyond the three stated restore rows
and does not promote the basin to an unbounded family theorem.

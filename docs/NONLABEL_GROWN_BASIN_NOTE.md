# Non-Label Grown Basin Note

**Date:** 2026-04-06
**Status:** bounded positive basin around the grown-row signed-source transfer

## Artifact chain

- [`scripts/NONLABEL_GROWN_BASIN_TARGETED.py`](../scripts/NONLABEL_GROWN_BASIN_TARGETED.py)
- [`logs/2026-04-06-nonlabel-grown-basin-targeted.txt`](../logs/2026-04-06-nonlabel-grown-basin-targeted.txt)
- [`outputs/nonlabel_grown_basin_recompute_certificate_2026_06_07.json`](../outputs/nonlabel_grown_basin_recompute_certificate_2026_06_07.json)
- [`logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt`](../logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt)

Runner behavior for audit replay:

- default: verify the frozen log row grid, compare each row against the
  completed 2026-06-07 recompute certificate, re-check zero/neutral gates,
  signed response, charge exponent, and safe-read counts
- `--recompute --write-certificate`: run the live targeted replay and write the
  recompute certificate used by the default verifier

## 2026-06-07 recompute repair

The 2026-06-07 audit marked this row conditional for a runner-artifact issue:

```text
runner_artifact_issue: include a completed
scripts/NONLABEL_GROWN_BASIN_TARGETED.py --recompute audit run or an
independent derivation of the three restore-row values, then re-check the row
gates and exponent arithmetic.
```

This repair runs:

```text
python3 scripts/NONLABEL_GROWN_BASIN_TARGETED.py --recompute --write-certificate
```

and records the completed live replay in
`outputs/nonlabel_grown_basin_recompute_certificate_2026_06_07.json`. The
default audit runner now checks the frozen 2026-04-06 transcript against that
certificate and independently re-checks the row gates and exponent arithmetic
from the recomputed values. It exits:

```text
SCORECARD PASS=6 FAIL=0
```

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

## Frozen Result

Seed `0`, geometry-sector candidate:

| restore | zero source | single `+1` | single `-1` | neutral `+1/-1` | double `+2` | charge exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `0.60` | `+0.000000000e+00` | `-3.392850377e-05` | `+3.391821269e-05` | `+0.000000000e+00` | `-6.786728602e-05` | `1.000219` |
| `0.70` | `+0.000000000e+00` | `-3.534838057e-05` | `+3.533742985e-05` | `+0.000000000e+00` | `-7.070769755e-05` | `1.000223` |
| `0.80` | `+0.000000000e+00` | `-3.620003164e-05` | `+3.618855547e-05` | `+0.000000000e+00` | `-7.241152409e-05` | `1.000228` |

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

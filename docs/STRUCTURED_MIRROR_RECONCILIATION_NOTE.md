# Structured Mirror Reconciliation Note

**Date:** 2026-04-03  
**Status:** support / historical pre-correction comparison only
**Current corrected authority:** [`STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md`](STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md)
**Historical runner:** [`scripts/structured_mirror_reconciliation.py`](../scripts/structured_mirror_reconciliation.py)


This note preserves a pre-correction harness comparison. Its quoted numbers
use a defective detectorwise seven-term statistic: they omit `-P(empty)` and
sum the absolute residual separately at each detector. They are not the
corrected detector-probability Sorkin statistic and do not support a current
Born-clean or not-Born-clean conclusion.

## Question

Why did pre-correction structured-mirror runners report different legacy
seven-term values under different slit and field choices?

## Canonical evidence on `main`

The former joint-validator source is not present in the current tree. Its
saved output remains available as a historical record:

[`logs/2026-04-03-structured-mirror-joint-validation.txt`](../logs/2026-04-03-structured-mirror-joint-validation.txt)

That historical validator reported these detectorwise seven-term values:

| N | `pur_cl` | gravity | legacy detectorwise seven-term ratio |
|---|---:|---:|---:|
| 25 | `0.833±0.013` | `+3.863±0.225` | `2.51e-01±9.56e-02` |
| 30 | `0.878±0.015` | `+4.904±0.282` | `1.71e-01±2.69e-02` |
| 40 | `0.932±0.009` | `+6.620±0.181` | `1.71e-01±2.47e-02` |

Those values are retained only as historical harness diagnostics. Because the
statistic omits `-P(empty)`, they do not determine the corrected Born result.

## What the reconciliation script tests

The new dedicated comparison script is:

[`scripts/structured_mirror_reconciliation.py`](../scripts/structured_mirror_reconciliation.py)

It historically compared four harnesses on the same structured-growth
geometry using the same defective detectorwise seven-term aggregation:

1. canonical threshold slits + physical mass field
2. threshold slits + flat field
3. audit-style top-K slit selection + flat field
4. audit-style top-K slit selection + physical mass field

## Historical comparison

The pre-correction values were harness-sensitive:

- the structured-growth geometry itself is physically interesting and retains
  positive gravity plus nontrivial decoherence
- the legacy detectorwise seven-term value changes with the aperture and field
  choices
- that sensitivity is not evidence about the corrected eight-term statistic

## Current safe conclusion

- This note and its runner are historical support artifacts only.
- The old structured-growth Born-negative conclusion is withdrawn.
- The corrected result is limited to the exact `32 x 6` fixed-graph strictly
  linear slice documented in
  [`STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md`](STRUCTURED_MIRROR_BORNSAFE_SCAN_NOTE.md).
- That finite result does not automatically settle the layer-normalized lane,
  the full historical grid, or successor-architecture questions.

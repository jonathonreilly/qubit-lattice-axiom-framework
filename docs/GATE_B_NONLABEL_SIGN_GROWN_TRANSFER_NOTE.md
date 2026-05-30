# Gate B Non-Label Sign Grown Transfer Note

**Date:** 2026-04-06
**Status:** bounded - bounded or caveated result note

## Artifact chain

- [`scripts/GATE_B_NONLABEL_SIGN_GROWN_TRANSFER.py`](../scripts/GATE_B_NONLABEL_SIGN_GROWN_TRANSFER.py)

## Imported authority

The grown-row construction this note replays on is the retained-bounded
distance-law transfer row taken from

- [`GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md)

That note (`retained_bounded`) fixes the grown-geometry family with
`drift = 0.2`, `restore = 0.7`, `h = 0.5`, and confirms that the far-field
distance-law tail transfers on the same `h = 0.5` generated family.
This note imports that retained-bounded row as its grown-row construction.

## Question

Can the old Gate B geometry-sector / non-label connectivity architecture carry
the current fixed-field signed-source response on the retained-bounded grown
row?

This note is intentionally narrow:

- retained-bounded grown row only: `drift = 0.2`, `restore = 0.7`
- label-grown control vs position-based geometry-sector candidate
- exact zero-source and neutral same-point cancellation checks
- small charge-linearity sanity pass

## Interpretation target

- if the geometry-sector candidate preserves the zero / neutral controls and
  the sign-law charge response, the old architecture has finite-runner support
  on this retained-bounded row
- if it collapses to zero or loses charge linearity, the old architecture was
  specific to the older Gate B families and does not transplant cleanly

## Frozen Result

Seed `0` retained-bounded grown-row replay:

| family | zero source | single `+1` | single `-1` | neutral `+1/-1` | double `+2` | charge exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| label-grown control | `+0.000000e+00` | `-1.594422e-04` | `+1.594790e-04` | `+0.000000e+00` | `-3.188474e-04` | `0.999833` |
| geometry-sector candidate | `+0.000000e+00` | `-3.534838e-05` | `+3.533743e-05` | `+0.000000e+00` | `-7.070770e-05` | `1.000223` |

## Transfer criteria (PASS/FAIL)

The runner converts the replay into explicit PASS/FAIL checks against
numerical tolerances, with module-level `_PASS` / `_FAIL` counters and a
`PASS=<n> FAIL=0` summary line. Both the label-grown control family and the
geometry-sector candidate family must satisfy all of the following on the
retained-bounded grown row (`drift = 0.2`, `restore = 0.7`, seed `0`):

- **zero-source delta_z** vanishes within `1e-12` (numerical zero)
- **neutral `+1/-1` delta_z** vanishes within `1e-12` (cancellation)
- **single `+1` / single `-1`** are antisymmetric within `5e-3` relative
  tolerance, with `+1` producing negative `delta_z` and `-1` positive `delta_z`
  (sign-law orientation)
- **single-source signal magnitude** is above a `1e-6` floor (the response is
  not a numerical zero)
- **charge exponent** from `single +1 / double +2` lies within `5e-3` of `1.0`
  (linearity)

Each failing check increments `_FAIL`; a successful run exits with
`PASS=<n> FAIL=0` and status `0`.

## Safe Read

Conditional on `PASS=<n> FAIL=0` on the retained-bounded grown row above, the
old architecture has bounded finite-runner support on the current grown-row
fixed-field lane, but only in a narrowed form:

- the position-based geometry-sector candidate preserves the exact zero-source
  baseline
- the neutral same-point `+1/-1` control still reduces to zero
- the single-source sign response survives with the correct orientation
- the charge response remains linear to within the checked exponent
- the candidate is weaker than the label-grown control, so it is not a full
  family-wide replacement, but it is a real transfer positive rather than a
  zero response

## Final Verdict

**bounded narrow grown-row transfer support** on the `drift = 0.2`,
`restore = 0.7` grown-geometry family imported from
[`GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md) and
witnessed by the PASS/FAIL transfer criteria above. This row's own retained
status is left to the independent audit lane.

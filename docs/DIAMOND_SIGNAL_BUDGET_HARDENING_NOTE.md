# Diamond Signal Budget Hardening Note

**Date:** 2026-04-06  
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded proxy-budget hardening card for the diamond/NV
phase-sensitive lane; not an absolute lab signal budget.

## Artifact Chain

- [`scripts/diamond_signal_budget_hardening.py`](../scripts/diamond_signal_budget_hardening.py)
- [`logs/2026-04-06-diamond-signal-budget-hardening.txt`](../logs/2026-04-06-diamond-signal-budget-hardening.txt)
- [`docs/MOVING_SOURCE_RETARDED_PORTABILITY_NOTE.md`](MOVING_SOURCE_RETARDED_PORTABILITY_NOTE.md)
- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)

## Question

What is the sharpest defensible diamond/NV readout budget we can state from the
moving-source proxy, without pretending we already have a calibrated
absolute amplitude map?

This note is intentionally narrow:

- one explicit source geometry
- one signed scaling map in source velocity
- one proxy-budget estimate from the weakest nonzero proxy observables
- one explicit blocker for a real lab budget

## Explicit Source Geometry

Use the portable grown proxy row as the geometry anchor:

- family: `drift = 0.2`, `restore = 0.7`
- seeds: `6`
- source layer: `8`
- source anchor target: `(y, z) = (0.0, 3.0)`
- motion law: `y_src(layer) = y0 + v * (layer - source_layer) * h`
- step size: `h = 0.5`

That is the only source geometry this note is allowed to budget against.

## Scaling Map

The runner-defined proxy observable is the signed centroid shift relative to
the matched static control, with phase lag as a secondary residue.

| `v` | `delta_y vs static` | `phase lag (rad)` |
| --- | ---: | ---: |
| `-1.00` | `-1.641405e-06` | `4.852935e-05` |
| `-0.50` | `-9.233039e-07` | `1.309075e-05` |
| `0.00` | `0.000000e+00` | `0.000000e+00` |
| `+0.50` | `+8.665715e-07` | `1.401315e-05` |
| `+1.00` | `+1.472200e-06` | `4.334258e-05` |

The clean read is:

- the centroid observable flips sign with `v`
- the `v = 0` control stays pinned to zero
- the phase lag stays small but nonzero
- the phase lag does not yet have a lab-calibrated amplitude interpretation

## Proxy Budget

The weakest nonzero proxy point is the useful one for a hardening estimate:

- smallest nonzero `|delta_y vs static| = 8.665715e-07` at `v = +0.50`
- smallest nonzero `|phase lag| = 1.309075e-05 rad` at `v = -0.50`

Using a conservative `3σ` readout target:

- centroid-noise target `<= 2.888572e-07`
- phase-noise target `<= 4.363583e-06 rad`

That is the narrowest proxy-budget we can honestly pin to the runner-defined
proxy observables.

## Missing Parameter

The real lab budget is still blocked by one missing calibration parameter:

- the transfer coefficient from the proxy units into the actual NV
  readout units and noise floor

Without that map, the current numbers stay as a proxy-budget card, not a
validated amplitude budget.

## Safe Read

The strongest defensible statement is:

- the proxy geometry gives one explicit source anchor
- the moving-source proxy gives one signed scaling map
- the centroid sign flip is the sharper discriminator
- the phase lag is a secondary residue
- the missing transfer calibration blocks a real absolute budget

What is not claimed:

- no absolute gravity detectability
- no geometry-generic theorem
- no completed lab signal budget

## Final Verdict

**bounded proxy-budget hardening: one explicit geometry, one signed scaling
map, and one proxy-budget estimate are pinned to the diamond/NV lane; the
absolute lab budget is blocked by the missing transfer calibration**

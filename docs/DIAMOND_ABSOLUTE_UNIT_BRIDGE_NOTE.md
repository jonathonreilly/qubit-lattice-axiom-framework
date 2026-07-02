# Diamond Absolute Unit Bridge Note

**Date:** 2026-04-06  
**Type:** meta
**Claim type:** meta
**Status:** calibration bridge note, not an experimental claim

## Artifact Chain

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
- [`docs/DIAMOND_SIGNAL_BUDGET_HARDENING_NOTE.md`](DIAMOND_SIGNAL_BUDGET_HARDENING_NOTE.md)
- [`docs/DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md`](DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md)
- [`docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`](DIAMOND_SENSOR_PROTOCOL_NOTE.md)
- [`docs/DIAMOND_SENSOR_PREDICTION_NOTE.md`](DIAMOND_SENSOR_PREDICTION_NOTE.md)
- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
- [`docs/CAUSAL_FIELD_PORTABILITY_NOTE.md`](CAUSAL_FIELD_PORTABILITY_NOTE.md)

## Question

What can the repo already infer about a diamond/NV absolute bridge from its
current proxy units, what still requires external calibration, and what is the
smallest extra simulation output that would tighten the bridge?

## Short Answer

The repo can already support a **relative** bridge:

- ideal lock-in detector semantics for `X`, `Y`, `phi`, null controls,
  `pi` reference flips, and affine widefield phase slopes
- exact nulls and sign flips in the diamond-facing proxy cards
- phase-quadrature and phase-ramp observables in the source-candidate
  wavefield lane
- causal-field ratio comparisons that stay meaningful as **dimensionless**
  proxy observables

The repo cannot yet support an **absolute** bridge:

- it does not know the transfer coefficient from proxy units into actual NV
  readout units
- it does not know the lab noise floor in those units
- it does not know the geometry-specific coupling factor for a particular
  diamond/NV setup

## What Can Be Inferred In Repo

From the diamond-facing proxy notes, the following are defensible without
external calibration:

- the ideal detector map from a delayed driven source to lock-in `X`, `Y`,
  `phi`, and a widefield phase slope is explicit and executable
- zero-source and static-background nulls can be pinned exactly in the proxy
  model
- the sign of the proxy response can be tracked across a controlled
  protocol
- phase lag, quadrature, and phase-ramp slope can be compared as
  dimensionless outputs
- causal-field ratios such as forward-only / instantaneous and
  dynamic(c<1) / instantaneous remain usable as internal proxy diagnostics

The newest detector and causal-field notes also help here:

- [`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
  closes the ideal lock-in detector map only; it does not supply an NV
  transfer coefficient or lab sensitivity estimate.
- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md) shows the configured finite-cone cases are
  structured proxy readouts, while the archived `0.45` table is stale
- [`docs/CAUSAL_FIELD_PORTABILITY_NOTE.md`](CAUSAL_FIELD_PORTABILITY_NOTE.md) shows the same observable is
  family-selective, so it should be treated as a proxy lane, not an absolute
  calibration law

## What Requires External Calibration

These quantities still need a lab-side transfer coefficient or equivalent
calibration:

- proxy amplitude to NV readout counts or volts
- proxy phase-ramp slope to an actual spatial phase gradient in the microscope
- proxy signal size to absolute detectability above the NV noise floor
- any claim that the proxy amplitude corresponds to a physical field
  strength in the lab setup

In other words, the repo can tell us the proxy is nonzero and well-behaved, but
not how many NV counts or volts that proxy should become.

## Smallest Extra Simulation Outputs

The next best in-repo tightening step is not a new mechanism. It is a compact
bridge card that prints the same observable family in a calibration-friendly
form:

1. one fixed geometry row, one exact-null row, and one driven row
2. `X`, `Y`, `phi`, and phase-ramp slope reported both raw and normalized
3. a two- or three-point source-strength sweep to test whether the proxy
   response stays linear enough for a single gain factor
4. the same observables at one nearby separation change, so the bridge can
   separate coupling gain from geometry sensitivity

## Single Best Observable

If we had to pick one in-repo observable to tighten the bridge first, it would
be the normalized phase-ramp slope from the phase-sensitive source-candidate
lane:

- raw `X`, `Y`, and `phi`
- plus the spatial phase-ramp slope, reported both raw and normalized

Why this one:

- it is the closest thing in the repo to an amplitude-independent calibration
  handle
- it can be compared before and after source-strength changes without pretending
  we already know the NV transfer coefficient
- it separates the proxy-level phase geometry from the unknown absolute readout
  scale better than a single centroid or escape number

That would not replace the external calibration coefficient, but it would make
the coefficient fit much cleaner.

## Narrow Conclusion

The current repo supports a **proxy-level diamond/NV bridge**:

- relative sign, null, and phase observables are already defensible
- causal-field ratios are useful as internal proxy diagnostics
- the absolute NV unit conversion is still missing

So the correct lane description is:

**bridge-ready in proxy units, not yet absolute in NV units; the missing
transfer coefficient and noise-floor calibration remain the blocker**

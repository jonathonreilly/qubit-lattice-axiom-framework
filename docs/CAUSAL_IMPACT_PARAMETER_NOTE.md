# Causal Impact-Parameter Note

**Date:** 2026-04-06; realized-impact repair 2026-06-18
**Status:** bounded realized-impact-parameter replay on the center growth-rule family

## Artifact Chain

- [`scripts/causal_impact_parameter_probe.py`](../scripts/causal_impact_parameter_probe.py)
- [`logs/runner-cache/causal_impact_parameter_probe.txt`](../logs/runner-cache/causal_impact_parameter_probe.txt)
- causal-field context:
  - [`docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](../docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
  - [`docs/CAUSAL_FIELD_PORTABILITY_NOTE.md`](../docs/CAUSAL_FIELD_PORTABILITY_NOTE.md)
  - [`docs/CAUSAL_FIELD_RECONCILIATION_NOTE.md`](../docs/CAUSAL_FIELD_RECONCILIATION_NOTE.md)

## Question

Does the causal-field modification preserve a recognizable
impact-parameter deflection law on the center growth-rule family when
the source layer physically realizes the requested impact parameters
and the fit uses the measured source-to-detector separation?

## Result

- exact zero control: `delta = +0.000e+00`
- exact zero field max: `+0.000e+00`
- source-layer half-width: `20`
- fit coordinate: mean realized source-to-zero-field-detector-centroid transverse separation

| field | alpha(realized b) | R^2 | TOWARD count |
| --- | ---: | ---: | ---: |
| instantaneous | `-1.933` | `1.000` | `5/5` |
| forward-only | `-1.952` | `1.000` | `5/5` |
| dynamic(c=1) | `-1.898` | `0.944` | `5/5` |
| dynamic(c=0.5) | `-2.322` | `0.975` | `5/5` |

## Realized Source Anchors

| target b | mean realized b | realized range | max source-z error | max realized-b error | distinct source nodes |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `5` | `5.001195` | `[4.979971, 5.047910]` | `6.526e-02` | `4.791e-02` | `1` |
| `6` | `5.991468` | `[5.924057, 6.036181]` | `4.535e-02` | `7.594e-02` | `1` |
| `7` | `6.983559` | `[6.965016, 6.999788]` | `3.361e-02` | `3.498e-02` | `1` |
| `8` | `7.979958` | `[7.932626, 8.025987]` | `5.584e-02` | `6.737e-02` | `1` |
| `10` | `10.008751` | `[9.942592, 10.055520]` | `4.016e-02` | `5.741e-02` | `1` |

## Runner Checks

| check | result | observed |
| --- | ---: | --- |
| exact zero controls | `PASS` | delta=+0.000e+00; field=+0.000e+00 |
| requested source anchors realized | `PASS` | max source-z error=6.526e-02; max realized-b error=7.594e-02 |
| realized b is strictly ordered | `PASS` | 5.001195, 5.991468, 6.983559, 7.979958, 10.008751 |
| all fields point toward source side | `PASS` | instantaneous=5/5; forward-only=5/5; dynamic(c=1)=5/5; dynamic(c=0.5)=5/5 |
| realized-b inverse-power fit is stable | `PASS` | min R^2=0.944; least-negative alpha=-1.898 |

## Safe Read

The old nominal-label fit is not used here. The runner enlarges the
transverse source support, records the selected source anchor for each
requested target, and fits against the realized source-to-detector
transverse separation.

All tested variants show a stable inverse-power tail on this realized-b replay.
The fitted exponents are not compatible with a `1/b` law; they are steeper.
The `c=0.5` finite-cone case is not a clean boundary in this repaired harness.

## Diagnostic Snapshot

- instantaneous tail-like exponent: `-1.933`
- forward-only tail-like exponent: `-1.952`
- dynamic(c=1) tail-like exponent: `-1.898`
- dynamic(c=0.5) exponent: `-2.322`

## Narrow Conclusion

On the enlarged-support center growth-rule replay, the causal-field variants preserve a realized-impact inverse-power centroid-shift tail, but the exponent is closer to `1/b^2` than `1/b`.
This repairs the source-anchor/fit-coordinate defect in the old note,
while changing the old finite-cone-boundary reading. It does not claim
a physical field theory, a framework-selected carrier/metric theorem,
or audit-retained status.

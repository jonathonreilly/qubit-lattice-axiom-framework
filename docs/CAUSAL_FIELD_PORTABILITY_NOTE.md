# Causal Field Portability Bounded Diagnostic

**Date:** 2026-04-06; review-loop boundary repair 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded finite diagnostic on the configured fixed-anchor
cross-family replay. This is not a cross-family portability theorem.
**Primary runner:** [`scripts/causal_field_portability_probe.py`](../scripts/causal_field_portability_probe.py)
**Runner cache:** [`logs/runner-cache/causal_field_portability_probe.txt`](../logs/runner-cache/causal_field_portability_probe.txt)

## Purpose

This row preserves the finite causal-field replay result while stripping the
old portability-law reading. The companion runner recomputes the configured
probe using the structured-growth, propagation, and centroid helper functions
from `scripts/evolving_network_prototype_v6.py`.

Those helper functions are included algorithm sources for this bounded
calculation. This note does not claim that the growth constructor,
propagator, detector-centroid readout, metric, or portability threshold has
been derived from accepted primitives. Those are separate science targets.

## Fixed Replay

The configured replay is:

```text
families = 3
seeds = 6
source_layer = 8
K = 5.0
source anchor target = (y, z) = (0.0, 3.0)
field strength = 5.0e-05
field eps = 0.1
dynamic cone values = [1.0, 0.5]
```

The three grown families use drift/restore pairs `(0.20, 0.70)`,
`(0.05, 0.30)`, and `(0.50, 0.90)`. The runner selects the source node nearest
to the declared source anchor on each grown family and computes detector
centroid shifts relative to the free-propagation baseline.

## Bounded Claim

On this fixed replay, the exact-null control survives:

```text
max |delta_y| across families = 0.000e+00
max |field| across families = 0.000e+00
```

The recomputed family rows are:

| Family | Inst Delta | Forward Delta | Fwd/Inst | Dyn(1.0)/Inst | Dyn(0.5)/Inst |
|---|---:|---:|---:|---:|---:|
| center grown family | `+2.921e-07` | `+1.951e-07` | `0.668` | `1.456` | `0.938` |
| portable family 2 | `+4.802e-07` | `+1.758e-07` | `0.366` | `0.732` | `0.728` |
| portable family 3 | `+1.927e-07` | `+1.522e-07` | `0.790` | `1.623` | `1.080` |

The forward-only ratio spread is `0.423`, and the dynamic
`c = 0.5` ratio spread is `0.352`. Therefore, on the declared finite replay,
the exact-null control survives but the tested ratios split by family. The
safe conclusion is a diagnosed family boundary for this configured probe, not
a portability law.

## Boundary

This row does not claim:

- that the growth constructor is derived from accepted primitives;
- that the propagation or detector-centroid carrier is derived from accepted
  primitives;
- that the configured metric or thresholds are framework-selected;
- cross-family portability of the causal field;
- a physical field-theory derivation;
- any new axiom or audit verdict.

The carrier and portability-criterion derivations remain separate science
work. This row only records the recomputed finite diagnostic on the declared
fixed-anchor replay.

## Algorithm Source

- [`EVOLVING_NETWORK_PROTOTYPE_V6_NOTE.md`](EVOLVING_NETWORK_PROTOTYPE_V6_NOTE.md)
  names the helper implementation used by the runner. This link records the
  one-hop algorithm-source dependency; it is not a claim that the helper has
  retained framework-operator-carrier status.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/causal_field_portability_probe.py
```

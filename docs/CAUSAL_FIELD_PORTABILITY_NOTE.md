# Causal Field Portability Cached Boundary Certificate

**Date:** 2026-04-06; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded cached-output certificate for the configured fixed-anchor
cross-family replay. This is not a cross-family portability theorem.
**Runner:** [`scripts/causal_field_portability_probe.py`](../scripts/causal_field_portability_probe.py)

## Purpose

The previous note mixed a useful finite diagnostic with unresolved carrier
authority for the generated-growth and propagation operators. This repair keeps
only the bounded cache statement:

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

The committed cache reports exact-null control and a family-boundary split in
the forward-only and finite-cone ratios.

## Bounded Claim

In `logs/runner-cache/causal_field_portability_probe.txt`, the replay reports:

```text
max |delta_y| across families = 0.000e+00
max |field| across families = 0.000e+00
```

and the following cross-family rows:

| Family | Inst Delta | Forward Delta | Fwd/Inst | Dyn(1.0)/Inst | Dyn(0.5)/Inst |
|---|---:|---:|---:|---:|---:|
| center grown family | `+2.921e-07` | `+1.951e-07` | `0.668` | `1.456` | `0.938` |
| portable family 2 | `+4.802e-07` | `+1.758e-07` | `0.366` | `0.732` | `0.728` |
| portable family 3 | `+1.927e-07` | `+1.522e-07` | `0.790` | `1.623` | `1.080` |

The cache also reports:

```text
forward-only ratio spread across the three families = 0.423
dynamic(c=0.5)/instantaneous ratio spread = 0.352
```

Thus, on the declared fixed-anchor replay, the exact-null control survives but
the tested ratios split by family. The bounded result is a diagnosed family
boundary, not a portability law.

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
work. This row only certifies the committed cache for the declared finite
probe.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/causal_field_portability_probe.py
```

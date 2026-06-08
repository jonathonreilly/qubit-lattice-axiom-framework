# Packet Memory: Initial Conditions Survive to Detector

**Date:** 2026-04-06
**Status:** bounded finite-runner support for Tier A (memory), partial finite
support for Tier B (shape), Tier C open; not a retained framework theorem.

## Artifact chain

- [`scripts/packet_memory.py`](../scripts/packet_memory.py)
- [`logs/2026-04-06-packet-memory.txt`](../logs/2026-04-06-packet-memory.txt)

## Question

Does initial-condition information survive propagation to the detector,
and does it carry physical content (gravitational response)?

## Tier A: Packet memory survives — POSITIVE

Overlap at detector (NL=30) for packets at different initial z-offsets:

| offset | overlap with origin | decoherent? |
| ---: | ---: | --- |
| 0 | 1.0000 | no |
| 1 | 0.83 | no |
| 2 | 0.42 | YES |
| 3 | 0.18 | YES |
| 8 | 0.12 | YES |

Packets separated by ≥ 2 lattice units are distinguishable at the detector.

### Memory decays with path length but slowly

| NL | overlap (origin vs z=2) |
| ---: | ---: |
| 15 | 0.19 |
| 25 | 0.36 |
| 30 | 0.42 |
| 40 | 0.56 |

The finite runner shows overlap rising over the checked path-length window.
The NL -> infinity memory-loss statement remains an open extrapolation rather
than a retained theorem. At NL=30 there is 58% distinguishability.

### Gravity depends on packet identity

| packet | gravitational deflection |
| --- | ---: |
| origin | +0.029612 |
| z=+1 | +0.024504 |
| z=+2 | +0.016560 |
| z=+3 | +0.008522 |
| z=-2 | +0.016633 |

3.5× variation in gravitational response across packets (origin vs z=+3).
Packet identity carries physics.

## Tier B: Shape partially converges — PARTIAL

Packet width (sigma_z) at detector:

| packet | sigma_z | cz |
| --- | ---: | ---: |
| narrow (origin) | 3.010 | -0.084 |
| medium (3x3) | 2.492 | -0.059 |
| offset (z=+2) | 2.983 | +1.093 |

Centroid survives strongly (offset at +1.093 vs origin at -0.084).
Width converges toward propagator natural mode (~3.0) with 17%
residual difference at NL=30.

## Tier C: Inertial response — OPEN

Not yet tested. Would require applying a uniform field to different
packets and measuring whether they accelerate differently.

## Audit boundary

This packet is a finite deterministic harness over the explicit
`grow`/`_prop`/`_imposed_field` implementation in
[`scripts/packet_memory.py`](../scripts/packet_memory.py). It does not derive
the growth rule, propagation kernel, imposed-field coupling, detector
normalization, or NL -> infinity memory-loss limit from retained framework
primitives. Those bridges remain open frontier work.

## Honest read

The finite model supports "detector-readable packet memory" but not
"persistent localized objects." The centroid is the primary surviving
information. Width converges over the checked finite paths. The
persistent-object closure stands for sharp localization, but the mesoscopic
memory lane is open.

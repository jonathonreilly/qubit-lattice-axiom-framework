# Packet Memory: Finite Deterministic Low-Overlap Harness

**Date:** 2026-04-06
**Status:** bounded finite-runner support for Tier A (memory), partial finite
support for Tier B (shape), Tier C open; not a retained framework theorem.
**Scope repair:** 2026-06-08. The source claim is narrowed to a pure
deterministic-runner characterization: finite detector-overlap, centroid,
width, and imposed-field response values for `scripts/packet_memory.py`.
The note no longer treats the overlap threshold as derived decoherence or the
imposed-field response as derived physical gravity.

## Artifact chain

- [`scripts/packet_memory.py`](../scripts/packet_memory.py)
- Current cached verifier output:
  [`logs/runner-cache/packet_memory.txt`](../logs/runner-cache/packet_memory.txt)
- [`logs/2026-04-06-packet-memory.txt`](../logs/2026-04-06-packet-memory.txt)

## Question

Does initial-condition information survive propagation to the finite detector
observable in this deterministic harness, and does the imposed-field response
depend on packet identity?

## Tier A: Packet memory survives as finite low-overlap structure

Overlap at detector (NL=30) for packets at different initial z-offsets:

| offset | overlap with origin | low-overlap at threshold 0.5? |
| ---: | ---: | --- |
| 0 | 1.0000 | no |
| 1 | 0.83 | no |
| 2 | 0.42 | YES |
| 3 | 0.18 | YES |
| 8 | 0.12 | YES |

Packets separated by at least 2 lattice units have detector overlap below the
chosen finite-harness threshold `0.5`. This is an overlap diagnostic only, not
a retained decoherence theorem.

### Memory decays with path length but slowly

| NL | overlap (origin vs z=2) |
| ---: | ---: |
| 15 | 0.19 |
| 25 | 0.36 |
| 30 | 0.42 |
| 40 | 0.56 |

The finite runner shows overlap rising over the checked path-length window.
The NL -> infinity memory-loss statement remains an open extrapolation rather
than a retained theorem. At NL=30 the finite overlap diagnostic gives
`1 - 0.4210 ~= 58%` low-overlap separation.

### Imposed-field response depends on packet identity

| packet | imposed-field centroid shift |
| --- | ---: |
| origin | +0.029612 |
| z=+1 | +0.024504 |
| z=+2 | +0.016560 |
| z=+3 | +0.008522 |
| z=-2 | +0.016633 |

There is a `0.029612 / 0.008522 ~= 3.48` variation across packets (origin vs
z=+3) for the imposed-field centroid response. The physical gravity
interpretation remains an open bridge.

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
normalization, overlap-to-decoherence readout, physical gravity interpretation,
or NL -> infinity memory-loss limit from retained framework primitives. Those
bridges remain open frontier work.

## Honest read

The finite model supports "detector-readable packet memory" in the narrow sense
of reproducible low-overlap and centroid/width diagnostics inside the harness.
It does not establish "persistent localized objects," a physical decoherence
law, or derived gravitational response. The centroid is the primary surviving
information. Width converges over the checked finite paths. The
persistent-object closure stands for sharp localization, but the mesoscopic
memory lane is open.

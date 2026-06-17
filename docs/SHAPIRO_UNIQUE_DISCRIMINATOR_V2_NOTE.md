# Shapiro Unique Discriminator V2 Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17
**Status:** bounded boundary verifier / source-support packet; independent
audit required before any effective status change
**Claim type:** bounded no-unique-discriminator boundary over the current
static-discriminator cache
**Primary runner:** [`scripts/shapiro_unique_discriminator_v2.py`](../scripts/shapiro_unique_discriminator_v2.py)
**Cached runner output:** [`logs/runner-cache/shapiro_unique_discriminator_v2.txt`](../logs/runner-cache/shapiro_unique_discriminator_v2.txt)

## Artifact Chain

- [`scripts/shapiro_unique_discriminator_v2.py`](../scripts/shapiro_unique_discriminator_v2.py)
- [`logs/runner-cache/shapiro_unique_discriminator_v2.txt`](../logs/runner-cache/shapiro_unique_discriminator_v2.txt)
- [`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)
- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)
- [`SHAPIRO_DELAY_NOTE.md`](SHAPIRO_DELAY_NOTE.md)
- [`SHAPIRO_FAMILY_PORTABILITY_NOTE.md`](SHAPIRO_FAMILY_PORTABILITY_NOTE.md)

The archived complex-interaction and diamond-bridge renderer notes are not
live dependencies for this bounded boundary verifier. The Shapiro delay and
family-portability rows are used only within their bounded proxy replay scope.

## Question

Does the current Shapiro detector-line proxy phase give a unique
causal-propagation discriminator, or can a static lookalike reproduce it?

## Cache-Backed Boundary Result

The primary runner reads
[`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)
and verifies that the cache is SHA-fresh for
[`scripts/shapiro_static_discriminator.py`](../scripts/shapiro_static_discriminator.py).

The parsed mean curves are:

| mode | c=2.0 | c=1.0 | c=0.5 | c=0.25 |
| --- | ---: | ---: | ---: | ---: |
| causal dynamic cone | `+0.0372` | `+0.0446` | `+0.0569` | `+0.0662` |
| static cone shape | `+0.0372` | `+0.0446` | `+0.0569` | `+0.0662` |
| static scheduling | `+0.0446` | `+0.0445` | `+0.0446` | `+0.0450` |

The cache-backed diagnostics are:

- causal vs static-cone RMSE: `0.0000`;
- causal vs static-schedule RMSE: `0.0128`;
- exact zero controls remain part of the static-discriminator packet.

## Boundary Read

The detector-line proxy phase is compatible with the causal-cone model, but it
is not a unique causal-propagation discriminator. A static cone-shape proxy
reproduces the displayed phase curve to the cache precision. Static scheduling
does not reproduce the curve and stays near-flat.

This is therefore a no-unique-discriminator boundary, not a stronger
discriminator result and not a physical field-speed measurement.

## Safe Read

- the phase line remains a bounded proxy observable;
- the static cone-shape no-go is load-bearing;
- no diamond/NV calibration or lab unit bridge is supplied here;
- a stricter discriminator would need another observable not reproduced by the
  static cone-shape field family.

## Claim Boundary

This row may support a bounded no-unique-discriminator boundary if audit
accepts the cache-backed verifier and scope. It does not retain the physical
Shapiro package, any lab-facing bridge, or any unique-causality claim.

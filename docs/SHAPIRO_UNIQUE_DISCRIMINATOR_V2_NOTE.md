# Shapiro Unique Discriminator V2 Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17
**Type:** no_go
**Claim type:** no_go
**Status:** bounded no-unique-discriminator boundary verifier; independent
audit required before any effective status change
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

## No-Go Discipline Gate

**Claim tested:** only the detector-line proxy phase curve on the cached
`c`-grid is not a unique causal-propagation discriminator, because the
static cone-shape comparator reproduces that displayed curve. This note does
not rule out second observables, higher precision probes, physical source
dynamics, or lab calibration.

- **N1 alternative routes:** phase curve alone, monotone `c` trend, exact-zero
  control plus phase curve, static-scheduling-only comparison, and portability
  of the same phase observable all fail to restore uniqueness at this scope:
  the static cone-shape curve remains an explicit matching comparator. A
  second observable is an open route, not closed by this note.
- **N2 wall independence:** single counterexample wall only: the static
  cone-shape comparator matches the displayed causal curve. No inflated
  multi-wall count is used.
- **N3 hidden-wall scan:** `current`, `cache-backed`, and `static cone-shape`
  are explicit scope restrictions, not hidden admissions. No axiom,
  primitive, lab bridge, or dynamics premise is smuggled.
- **N4 residual matching:** the residual matches the static-discriminator
  boundary exactly: uniqueness of the detector-line proxy phase against
  static field-shape effects.
- **N5 rhetoric audit:** the negative is only for this detector-line phase
  curve over the cached `c`-grid. It is not a per-site, all-observable,
  lattice-wide, lab, or physical field-speed no-go.
- **N6 partial-closure scan:** a second observable, higher precision
  discriminator, physical source model, or lab bridge could still build a
  stricter discriminator. None is claimed absent or axiom-forbidden.
- **N7 steelman:** a hostile reviewer can reasonably argue that another
  channel, a higher-precision curve, or a source-to-lab readout could separate
  causal propagation from static cone-shape effects. That does not defeat this
  note, because the shipped no-go is limited to the present detector-line phase
  observable.
- **N8 cross-cycle echo:** the prior static-discriminator boundary is the same
  residual, not a different wall. No retired convention or primitive changes
  the displayed curve equality.

**No-go-discipline status:** PASS for the narrowed claim above.

## Claim Boundary

This row may support a no-unique-discriminator boundary if audit
accepts the cache-backed verifier and scope. It does not retain the physical
Shapiro package, any lab-facing bridge, or any unique-causality claim.

# Shapiro Unique Discriminator V2 Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17; snapshot-boundary
alignment 2026-07-11

**Type:** no_go

**Claim type:** no_go

**Status:** bounded input-interface/history-label boundary verifier; independent
audit required before any effective status change

**Primary runner:**
[`scripts/shapiro_unique_discriminator_v2.py`](../scripts/shapiro_unique_discriminator_v2.py)

**Cached runner output:**
[`logs/runner-cache/shapiro_unique_discriminator_v2.txt`](../logs/runner-cache/shapiro_unique_discriminator_v2.txt)

## Artifact Chain

- [`scripts/shapiro_unique_discriminator_v2.py`](../scripts/shapiro_unique_discriminator_v2.py)
- [`logs/runner-cache/shapiro_unique_discriminator_v2.txt`](../logs/runner-cache/shapiro_unique_discriminator_v2.txt)
- [`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)
- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)

The archived complex-interaction and diamond-bridge renderer notes are not
live dependencies for this bounded verifier.

## Question

Does the current detector-line phase identify the history label attached to
the node field, or does a position-only field with the same node values give
an exact equal-array witness on the runner's unconstrained input surface?

## Cache-Backed Boundary Result

The primary runner reads
[`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt),
verifies that it is SHA-fresh for
[`scripts/shapiro_static_discriminator.py`](../scripts/shapiro_static_discriminator.py),
and requires the upstream `ASSERTIONS: PASS` certificate.

The parsed mean curves are:

| mode | q=2.0 | q=1.0 | q=0.5 | q=0.25 |
|---|---:|---:|---:|---:|
| cone snapshot | `+0.0372` | `+0.0446` | `+0.0569` | `+0.0662` |
| equal-array position-only witness | `+0.0372` | `+0.0446` | `+0.0569` | `+0.0662` |
| configured fixed-layer proxy | `+0.0446` | `+0.0445` | `+0.0446` | `+0.0450` |

The cache-backed diagnostics are:

- snapshot and equal-array witness curves are exactly equal;
- cone-snapshot span minus fixed-layer-proxy span is above `2e-2 rad`; and
- the upstream cache completes with all assertive checks passing.

## Boundary Read

The supplied kernel receives a node-wise field snapshot and contains no causal
time evolution. Its detector phase therefore cannot identify a history label
that is absent from the interface. The equal-array witness is the same element
of the runner's unconstrained node-array input space. No static field equation,
source law, boundary data, or physical admissibility condition is supplied.
The fixed-layer rows remain a bounded secondary control, not an exhaustion of
schedules.

This is an input-interface/history-label no-go, not a physical field-speed or
static-solution result and not a theorem about history-sensitive observables.

## No-Go Discipline Gate

- **N1 — alternative routes:** seven attacks are separated: hidden
  history-label input, direct cone-index leakage, stateful/nondeterministic
  propagation, unequal fixed instances/baselines, zero-norm phase, a physical
  static-solution restriction, and one witness fixed across all indices. The
  first four are absent from the inspected interface, undefined phase is
  excluded, and the last two change the comparator class or quantifier.
- **N2 — wall independence:** the exact equal-input theorem has no residual
  walls; temporal extensions are not counted as multiple failures.
- **N3 — hidden-wall scan:** the fixed configured instance and unconstrained
  node-array input class are explicit. The cache verifier imports no physical
  time, speed, static-solution admissibility, source history, observed value,
  fitted selector, or lab calibration.
- **N4 — residual matching:** the verifier checks the same residual as its
  source note: history identifiability from one field-array detector phase.
- **N5 — rhetoric audit:** the negative claim is only for this unconstrained
  node-array interface and deterministic phase readout, not for physical
  static solutions, edge-time, multi-time, one-field-across-index, or
  all-observable resolutions. More same-time detector components do not evade
  equal-input determinism unless they carry independent history.
- **N6 — partial-closure scan:** an explicit temporal field plus a
  history-sensitive readout is the live route around the no-go.
- **N7 — steelman:** the equal-array witness need not be a physically
  admissible static solution, one physically fixed field may fail to reproduce
  the indexed curve, and a retarded field along a probe path need not reduce to
  one snapshot. Those objections defeat a physical/global claim, so none is
  made; they do not alter the exact result on the unconstrained input class.
- **N8 — cross-cycle echo:** the earlier Shapiro cone-mask rows did not add
  temporal evolution. The known retirement route is the explicit temporal
  extension, not a causal reinterpretation of the cone index.

**No-go-discipline status:** PASS for the narrow source-side claim above.

## Claim Boundary

This row may support the narrow no-go if independent audit accepts the
cache-backed verifier and scope. It does not establish a physical Shapiro
package, lab-facing bridge, causal field-speed interpretation, physical static
solution, single-fixed-field theorem, or all-observable no-go.

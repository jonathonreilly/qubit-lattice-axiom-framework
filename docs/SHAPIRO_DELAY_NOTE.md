# Shapiro Delay Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17; static-cone rerun 2026-07-01
**Status:** bounded finite replay / source-support packet; independent audit
required before any effective status change
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/shapiro_phase_lag_probe.py`](../scripts/shapiro_phase_lag_probe.py)
**Cached runner output:** [`logs/runner-cache/shapiro_phase_lag_probe.txt`](../logs/runner-cache/shapiro_phase_lag_probe.txt)

## Artifact Chain

- [`scripts/shapiro_phase_lag_probe.py`](../scripts/shapiro_phase_lag_probe.py)
- [`logs/runner-cache/shapiro_phase_lag_probe.txt`](../logs/runner-cache/shapiro_phase_lag_probe.txt)
- [`scripts/shapiro_delay_portable.py`](../scripts/shapiro_delay_portable.py)
  (finite propagation harness reused by the primary runner)
- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
- [`CAUSAL_FIELD_RECONCILIATION_NOTE.md`](CAUSAL_FIELD_RECONCILIATION_NOTE.md)
- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)

The archived complex-interaction and diamond-bridge renderer notes are not
live dependencies for this bounded replay.

## Question

What finite in-repo replay supports the c-dependent proxy phase table while
keeping the exact zero control and static-cone no-go boundary explicit?

## Exact Control

- `c = inst`: phase lag `0.000 rad` on all three configured families
- exact null survives by direct detector-overlap comparison

## Bounded Phase-Lag Replay

| c | phase lag mean | family spread | fam1 | fam2 | fam3 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `2.00` | `+0.0401 rad` | `0.0001 rad` | `+0.0401` | `+0.0401` | `+0.0400` |
| `1.00` | `+0.0500 rad` | `0.0002 rad` | `+0.0499` | `+0.0501` | `+0.0499` |
| `0.50` | `+0.0621 rad` | `0.0002 rad` | `+0.0621` | `+0.0622` | `+0.0620` |
| `0.25` | `+0.0679 rad` | `0.0001 rad` | `+0.0679` | `+0.0679` | `+0.0679` |

## Static-cone discriminator rerun (2026-07-01)

The earlier static-cone discriminator
([`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md))
established its exact-mimic result on an older cone configuration whose
phase values differ from the repaired table above. Per the audit repair
target, the static-cone mimic is recomputed in this packet against the
repaired table:

- a **frozen static cone field** — a function of position only, with the
  same spatial support and values as the repaired harness's cone
  construction, written independently in the primary runner with no
  propagation or scheduling notion — is propagated through a mirrored copy
  of the portable kernel;
- the kernel mirror is first validated against the portable instantaneous
  detector state (max detector-node delta below `1e-12`);
- the frozen static cone reproduces the repaired c-dependent phase table
  row by row (max phase delta below `1e-10 rad` over all 24
  family/seed/`c` rows; measured values are in the cached runner output).

The static-cone non-uniqueness boundary is therefore re-established for
this repaired table directly, not inherited from the older discriminator
configuration: within this discrete model the repaired cone construction is
realizable as a frozen spatial shape, so the detector-line phase lag alone
does not uniquely certify causal propagation on this harness.

## Runner Checks

The primary runner recomputes the table from
[`scripts/shapiro_delay_portable.py`](../scripts/shapiro_delay_portable.py) and
asserts:

- exact instantaneous zero control;
- family spread below `2.5e-4 rad` on every finite-`c` row;
- monotone phase increase as the field propagation parameter `c` decreases;
- displayed table agreement to the shown precision;
- this note is bounded, not retained or proposed-retained;
- the static-cone no-go boundary is present;
- lab calibration and physical field-speed claims are excluded;
- the live causal packet is linked and the stale generated causal-field note is
  not a dependency;
- the mirrored kernel reproduces the portable instantaneous detector state
  (max node delta below `1e-12`);
- the frozen static cone reproduces the repaired causal phase table
  (max row delta below `1e-10 rad` over all 24 rows);
- this note records the 2026-07-01 static-cone rerun against this repaired
  table.

## Safe Read

- family spread across the configured three-family replay stays below
  `2.5e-4 rad`;
- the proxy phase increases monotonically as the field propagation parameter
  `c` decreases;
- this is a finite replay over the declared harness, not a derivation of a
  physical Shapiro law;
- the static-cone boundary is recomputed in this packet against the repaired
  table: a frozen static cone shape can reproduce the same phase curve on
  this repaired harness, so this is not a unique causal discriminator;
- this is not a lab-calibrated diamond/NV prediction and not a physical
  field-speed measurement.

## Claim Boundary

This row may support a bounded finite proxy replay if audit accepts the
computation and scope. It does not retain the physical Shapiro-delay package,
the failed diamond bridge rows, the complex-interaction renderer, or any
unique-causality claim.

# Shapiro QA Retest Note

**Date:** 2026-04-06; bounded-source repair 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded QA cache-verifier over existing Shapiro replay caches;
independent audit required before any effective status change
**Primary runner:** [`scripts/shapiro_qa_retest_boundary.py`](../scripts/shapiro_qa_retest_boundary.py)
**Cached runner output:** [`logs/runner-cache/shapiro_qa_retest_boundary.txt`](../logs/runner-cache/shapiro_qa_retest_boundary.txt)

## Cited Authorities

- [`SHAPIRO_DELAY_NOTE.md`](SHAPIRO_DELAY_NOTE.md) — phase-lag replay context,
  used only within bounded proxy scope.
- [`logs/runner-cache/shapiro_phase_lag_probe.txt`](../logs/runner-cache/shapiro_phase_lag_probe.txt)
  — numeric phase-lag replay cache checked by the QA runner.
- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)
  — static-cone no-unique-discriminator boundary.
- [`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)
  — numeric static-discriminator cache checked by the QA runner.
- [`SHAPIRO_FAMILY_PORTABILITY_NOTE.md`](SHAPIRO_FAMILY_PORTABILITY_NOTE.md)
  — family-portability context, used only within bounded proxy scope.

Archived failed complex-interaction and diamond-bridge notes are not live
dependencies for this QA row.

## Scope

This is a focused QA retest over cached Shapiro-phase artifacts:

- `scripts/shapiro_phase_lag_probe.py`;
- `scripts/shapiro_static_discriminator.py`;
- `scripts/shapiro_qa_retest_boundary.py`.

The QA question is whether the cached phase-lag replay and cached static-cone
boundary remain mutually consistent, without promoting either cache into a
retained physical Shapiro package.

## Retest

### Phase-Lag Replay Cache

The QA runner checks that
[`logs/runner-cache/shapiro_phase_lag_probe.txt`](../logs/runner-cache/shapiro_phase_lag_probe.txt)
exits cleanly, contains the exact instantaneous zero-control text, and reports
finite-row family spread bounded by `2.5e-4 rad`. It also verifies the cache
is SHA-fresh for the phase-lag runner, then checks that the cached numeric
replay is consistent with the static-discriminator boundary.

### Static-Discriminator Cache

The QA runner checks that
[`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)
exits cleanly and is SHA-fresh for the static-discriminator runner. It parses
the displayed mean curves and verifies:

- static cone vs causal RMSE: `0.0000`;
- static scheduling vs causal RMSE: `0.0128`;
- static cone-shape remains the no-unique-discriminator boundary.

## QA Read

- No source-placement bug is exposed by the checked caches.
- No new static-shape loophole is exposed beyond the already documented
  static-cone boundary.
- The static-discriminator script is computationally heavier than the
  phase-lag probe, but this QA row now checks the SHA-pinned cache rather than
  re-running that heavy sweep.

## Claim Boundary

This row may support bounded QA consistency if audit accepts the cache-backed
verifier and scope. It is not a retained physical Shapiro package, not a unique
causal discriminator, not a lab calibration, and not a status authority for its
upstream rows.

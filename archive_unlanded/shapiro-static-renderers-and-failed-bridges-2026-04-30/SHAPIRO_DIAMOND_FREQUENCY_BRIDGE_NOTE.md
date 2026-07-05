# Shapiro Diamond Frequency Bridge Note

**Date:** 2026-04-06
**Status:** RETRACTED 2026-04-30 — audit failed; this note is archived under `archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/`. Claims below are NOT supported by current runners or current audit lane. See `## Retraction` section.

## Current-surface certificate (2026-06-12 source firewall)

**Actual current-surface status:** archived `audited_failed` / retracted
historical artifact. This file is kept only as audit history for a failed
or inconsistent route. It may not be cited as retained, bounded, conditional,
supporting, or methodological authority for any live framework chain.

## Retraction

- **Date archived:** 2026-04-30
- **Archive directory:** `archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/` (the directory name encodes the failure reason: static renderers and failed bridges).
- **Audit verdict_rationale (quoted verbatim from `docs/audit/data/audit_ledger.json`):**

  > Issue: The frequency bridge depends on a conditional Shapiro-delay result, a failed Shapiro-diamond bridge, and unaudited/conditional diamond phase-ramp and signal-budget notes, with no runner constructing phi, k-scaling, or normalized phase-ramp quantities. Why this blocks: translating an unratified proxy scaling into lab-facing X/Y/phi language does not establish a retained frequency-sensitive diamond/NV prediction or a calibrated comparison surface. Repair target: audit or repair SHAPIRO_DELAY_NOTE and SHAPIRO_DIAMOND_BRIDGE_NOTE, audit the diamond phase-ramp and signal-budget notes, and add a runner that varies k at fixed geometry and verifies phi/k and slope/k collapse from generated data. Claim boundary until fixed: it is safe to say this note proposes a proxy-level frequency-bridge test to run; it is not safe to claim retained k-linear diamond/NV phase-ramp behavior.

- **Do not cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## 2026-06-16 archive firewall

This archived packet is historical / diagnostic and retired as evidence. The
body below records a proposed proxy frequency bridge, not a retained
diamond/NV prediction and not a retained Shapiro scaling law.

Any future repair must construct `phi`, the drive-scale sweep, and normalized
phase-ramp quantities from generated data after the Shapiro and diamond bridge
dependencies are audit-clean.

## Artifact Chain

- [`docs/SHAPIRO_DELAY_NOTE.md`](../../docs/SHAPIRO_DELAY_NOTE.md)
- [`docs/SHAPIRO_DIAMOND_BRIDGE_NOTE.md`](../../docs/SHAPIRO_DIAMOND_BRIDGE_NOTE.md)
- [`docs/DIAMOND_PHASE_RAMP_BRIDGE_CARD_NOTE.md`](../../docs/DIAMOND_PHASE_RAMP_BRIDGE_CARD_NOTE.md)
- [`docs/DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md`](../../docs/DIAMOND_NV_PHASE_RAMP_SIGNAL_BUDGET_NOTE.md)
- [`docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`](../../docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md)
- [`docs/DIAMOND_SENSOR_PREDICTION_NOTE.md`](../../docs/DIAMOND_SENSOR_PREDICTION_NOTE.md)
- retained scaling result anchor:
  - commit `1730b52` (`feat(shapiro): phase scales as s^1.000 (linear in mass), proportional to k`)

## Historical question (retracted)

The old question asked how to translate a `k`-proportional Shapiro scaling into
diamond/NV bridge language. This archive does not prove the Shapiro scaling
premise or the diamond/NV translation.

## Historical supplied scaling assertion (retracted)

The old body asserted that the Shapiro delay scales as a phase observable:

- phase `~ s^1.000` in source strength / mass proxy
- phase decreases with impact parameter `b`
- phase `~ k`, i.e. the delay is chromatic / frequency sensitive

The old body treated the last item as the bridge handle:

- at fixed geometry, the lag grows with the drive wavenumber/frequency scale
- equivalently, the normalized phase response is the cleanest proxy quantity

## Historical bridge translation proposal (open)

The bridge-card vocabulary proposed here was:

- `X`: in-phase channel
- `Y`: quadrature channel
- `phi = atan2(Y, X)`: phase lag
- phase-ramp slope: spatial accumulation of the lag

The old note proposed adding a drive-scale dimension to that language:

- the phase lag itself should scale with the drive frequency scale `k`
- the phase-ramp slope should scale with `k` in the same proxy sense
- after dividing out the drive scale, the proxy phase response should collapse

As an open future test, a repaired runner would need to:

- hold geometry fixed
- vary drive frequency / wavenumber
- look for a quadrature / phase-ramp response that scales linearly with `k`
- check whether `phi / k` and the normalized phase-ramp slope stay roughly
  constant across the retained proxy sweep

This archive does not establish the frequency-sensitive analogue as retained.

## Historical motivation (not evidence)

The old motivation was that phase/quadrature could be cleaner than raw
amplitude:

- absolute amplitude still needs external calibration
- phase and quadrature are naturally normalized observables
- the old Shapiro premise said the lag is monotone in slower propagation and
  proportional to `k`

The old note proposed a lab-friendly proxy prediction:

- higher drive frequency should produce a proportionally larger phase lag
- the same geometry should preserve the sign and ordering of the lag
- the normalized phase response should be cleaner than the raw amplitude

## What remains safe as archive-only context

This archived packet may only say:

- the note proposed a `k`-sweep bridge to test
- no runner here constructs `phi`, `phi/k`, or phase-ramp collapse from
  generated data
- no absolute or proxy-level diamond/NV prediction is retained by this packet

The repo cannot cite this packet for:

- the absolute NV-unit mapping for frequency or phase
- the lab-specific detectability threshold
- a calibrated conversion from proxy `k` to microscope readout units

## Historical narrow prediction (retracted)

The old note predicted that if a diamond/NV setup is driven at multiple
frequencies while holding geometry fixed:

- `phi` grows approximately linearly with `k`
- the phase-ramp slope grows approximately linearly with `k`
- the normalized ratios `phi / k` and slope / `k` are the cleaner quantities
  to compare across runs

That proxy-level frequency bridge remains open, not retained.

## Historical final verdict (retracted)

The old final verdict is retracted. This packet is not evidence for a retained
frequency-sensitive Shapiro delay or a diamond/NV phase-ramp prediction.

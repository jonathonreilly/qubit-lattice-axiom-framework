# Handoff

## What Changed

This branch adds an ideal lock-in detector theorem for the Diamond/NV lane and
wires the Diamond source notes to it.

The theorem proves/checks:

- `X = A cos(omega tau)`;
- `Y = A sin(omega tau)`;
- `phi = atan2(Y, X) = omega tau mod 2*pi`;
- drive-off/static-source null controls;
- `pi` reference sign flip;
- affine widefield phase slope `d phi / dz = omega kappa`.

## What It Unlocks

The Diamond prediction/protocol/signal-budget notes no longer need to name the
ideal detector map as a missing future theorem. That should make the Diamond
sensor rows cleaner re-audit candidates.

## What Remains Open

- physical source-to-NV coupling map;
- absolute NV transfer coefficient;
- lab geometry and noise floor;
- any audit verdict/effective-status change.

## Checks

Run before PR:

- `python3 scripts/diamond_ideal_lockin_detector_theorem.py`
- `python3 scripts/diamond_sensor_prediction_probe.py`
- `python3 scripts/diamond_sensor_protocol_probe.py`
- `python3 scripts/diamond_phase_ramp_bridge_card.py`
- `python3 scripts/diamond_signal_budget_hardening.py`
- `python3 scripts/cached_runner_output.py <runner> --refresh` for the five Diamond runners

Reviewer should run any desired review-loop/audit-loop independently.

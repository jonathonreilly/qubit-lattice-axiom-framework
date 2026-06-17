## Summary

This PR repairs the Diamond/NV detector-map bridge without claiming a closed
lab prediction.

It adds:

- `docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`
- `scripts/diamond_ideal_lockin_detector_theorem.py`
- `logs/runner-cache/diamond_ideal_lockin_detector_theorem.txt`

The theorem derives/checks the ideal lock-in map from a delayed driven source
history to `X`, `Y`, `phi`, null controls, `pi` reference flip, and affine
widefield phase slope.

It also updates the Diamond prediction/protocol/signal-budget/bridge notes so
the ideal detector map is no longer a vague future import. The remaining
blockers stay explicit: source-to-NV coupling, absolute NV transfer
coefficient, lab geometry, and noise floor.

## Trace

- Loop pack: `.claude/science/physics-loops/diamond-ideal-lockin-boundary/`
- Trace gate: `.claude/science/physics-loops/diamond-ideal-lockin-boundary/TRACE_GATE.md`
- Handoff: `.claude/science/physics-loops/diamond-ideal-lockin-boundary/HANDOFF.md`
- Certificate: `.claude/science/physics-loops/diamond-ideal-lockin-boundary/CLAIM_STATUS_CERTIFICATE.md`

Trace class: `direct_blocker_closure`

Reachability: `partially_closes`

The closed blocker is only the ideal detector-map theorem. This PR does not
close physical source-to-NV coupling or absolute detectability.

## Checks

Direct runners:

```bash
python3 scripts/diamond_ideal_lockin_detector_theorem.py
python3 scripts/diamond_sensor_prediction_probe.py
python3 scripts/diamond_sensor_protocol_probe.py
python3 scripts/diamond_phase_ramp_bridge_card.py
python3 scripts/diamond_signal_budget_hardening.py
```

Cache freshness:

```bash
python3 scripts/cached_runner_output.py scripts/diamond_ideal_lockin_detector_theorem.py --check-only
python3 scripts/cached_runner_output.py scripts/diamond_sensor_prediction_probe.py --check-only
python3 scripts/cached_runner_output.py scripts/diamond_sensor_protocol_probe.py --check-only
python3 scripts/cached_runner_output.py scripts/diamond_phase_ramp_bridge_card.py --check-only
python3 scripts/cached_runner_output.py scripts/diamond_signal_budget_hardening.py --check-only
```

Other:

```bash
python3 -m py_compile scripts/diamond_ideal_lockin_detector_theorem.py scripts/diamond_sensor_prediction_probe.py scripts/diamond_sensor_protocol_probe.py scripts/diamond_phase_ramp_bridge_card.py scripts/diamond_signal_budget_hardening.py
git diff --check
```

## Boundaries

- No audit loop was run.
- No audit ledger, audit queue, audit result, publication matrix, or front-door
  authority output is edited.
- No PR landing or merge to `main`.
- Review-loop is reviewer-owned and not run in this branch.
- No retained/promoted author proposal is made; certificate status is
  `bounded-support`.

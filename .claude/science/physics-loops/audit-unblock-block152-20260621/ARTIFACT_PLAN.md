# Artifact Plan

1. Add `scripts/diamond_sensor_prediction_bounded_probe.py`.
2. Add `Runner:` metadata to `docs/DIAMOND_SENSOR_PREDICTION_NOTE.md`.
3. Run the wrapper, prediction card, and ideal lock-in theorem runners.
4. Run the audit pipeline and cache the wrapper runner.
5. Verify the row remains `bounded_theorem`, `unaudited`, and
   `effective_status: unaudited`.
6. Open one independent review PR for block152.

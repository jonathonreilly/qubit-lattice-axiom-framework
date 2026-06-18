# Assumptions And Imports

- No new axiom is introduced.
- The current evidence surface is the SHA-pinned runner cache for
  `scripts/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.py`.
- The note uses the current 45-row sweep: drifts
  `0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50` and seeds `0..4`.
- The stale `drift = 0.02, seed = 0` targeted row is explicitly retired from
  the note's evidence surface.
- `scripts/gate_b_no_restore_farfield.py` remains an executable bounded-harness
  helper source, not a derived framework carrier theorem.
- No literature value is load-bearing.

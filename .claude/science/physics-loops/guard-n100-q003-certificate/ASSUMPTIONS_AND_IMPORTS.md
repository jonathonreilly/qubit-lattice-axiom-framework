# Assumptions And Imports

- The wrapper runner executes `scripts/dense_prune_channel_count_guard.py`
  with `DENSE_GUARD_LAYERS=100` and `DENSE_GUARD_QS=0.03`.
- The supported claim is aggregate-only for this pocket.
- Seed-level examples remain context and are not load-bearing.

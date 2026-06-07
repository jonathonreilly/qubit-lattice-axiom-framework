# Handoff

This PR repairs `FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30` by making
its default claim conditional and retaining only the finite algebraic locator.

What moved:

- `Q=1` is no longer described as the framework-native physical default.
- The trace/dimension `Q=1` read is conditional on a supplied beta=0 tracial
  generation reference.
- `r/Q` endpoint support is sourced to retained Record-function algebra.
- Equal-block versus dimension/Plancherel support is sourced to retained bounded
  Koide block-weight algebra.
- The beta=0 versus finite-beta reference-state gate remains open.

Verification:

```sh
PYTHONPATH=scripts python3 scripts/flavor_detR_default_full_exercise_2026_05_30.py
```

Expected result: `UPDATED SCORECARD PASS=6 FAIL=0`.

No `docs/audit/**` files are changed.

# Block23 primary runner source repin

The first primary execution preserved in `EXECUTION_HISTORY.md` reached
nineteen displayed passing science checks, then exited before the mutation
summary because two harness checks inspected `transition.__code__` even though
`transition` was wrapped by `functools.lru_cache`.

Commit `3c1723583fbef89cba35e37a3049f7f0010eafac` changes exactly those two
expressions to `transition.__wrapped__.__code__`.  No preregistration content,
geometry, state, effect, channel, kernel, covariance, spectrum, composition,
scope, or expected mutation result changed.

Repaired primary source pin:

```text
82dd0f631fb70662e696c7a92f0997fa26094c32e7ed6ad37671f144eed2bdea  scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py
```

The independent source and its successful first cache remain unchanged.  The
repaired primary may execute only after this repin is committed.

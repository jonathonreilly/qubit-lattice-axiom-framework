# Block23 execution history

## First pinned executions

Both first executions began only after runner-source pin commit
`62bda5f9ac`.

### Primary

- source SHA-256:
  `7833760f2026bd8c96f591a38050aa10496abc636f2b7594783abd1c12c869e9`
- preserved stdout cache:
  `logs/runner-cache/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30_initial_fail.txt`
- cache SHA-256:
  `b8e65ee252fa09610bbf54f38e2994e82d174d1494211aa0664425449c70d977`
- process status: exit `1` after nineteen displayed science checks passed and
  before the mutation summary or final `TOTAL` line;
- exact failure: `mutation_rejections` inspected `transition.__code__`, but
  `transition` had been wrapped by `functools.lru_cache` and the wrapper has no
  direct `__code__` attribute.

The failure is harness introspection, not a failed physics identity.  The
stderr traceback was displayed by the first terminal execution but was not
part of the stdout-only `tee` cache; that capture limitation is recorded here.
The cache is preserved and must not be overwritten.

### Independent

- source SHA-256:
  `d61224affaf8a921f2f269303ef4f8358059d238e696e04ec873bea718e05f1a`
- cache:
  `logs/runner-cache/independent_admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.txt`
- cache SHA-256:
  `60f79380aa2afe63f223d859b99626789bb24c2648b15f2dcc24f68e5fd19179`
- process status: exit `0`, `TOTAL: PASS=20 FAIL=0`;
- hostile mutations: `57/57` rejected.

## Authorized narrow repair

Only the two cached-function signature introspections in the primary runner
may be changed to inspect `transition.__wrapped__.__code__`.  No geometry,
state, effect, channel, kernel, covariance, spectrum, composition, scope, or
mutation expectation may change.  The repaired source must be committed,
hashed, and explicitly repinned before its first reexecution.

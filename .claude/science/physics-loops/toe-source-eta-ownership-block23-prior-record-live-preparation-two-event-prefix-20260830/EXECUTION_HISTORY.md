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

## First repaired-primary execution and coverage rejection

After repin commit `1c6700d943`, the first repaired primary ran to exit zero:

- source SHA-256:
  `82dd0f631fb70662e696c7a92f0997fa26094c32e7ed6ad37671f144eed2bdea`;
- preserved cache:
  `logs/runner-cache/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30_coverage_insufficient.txt`;
- cache SHA-256:
  `8d22c939430f41b4f77ec27c8f79e1622fd79e32ca643b0b2b9a78e9635bd9cc`;
- displayed result: `TOTAL: PASS=20 FAIL=0`, mutations `37/37`.

A separate static completion audit rejected that green cache as insufficient
evidence for the strong terminal.  The effect/kernel/quotient/spectrum checks
were substantive, but several channel, composition, scope, and mutation
checks used label/count surrogates:

1. no explicit symbolic `A_(f,b)`, `P_valid`, `K_STOP`, or Heisenberg action;
2. incomplete encoding of all five inactive Blank blocks and target-star
   covariance;
3. no full branch-map/coherent-cross-term covariance model;
4. no explicit preparation-plus-six-writer composition on reachable symbolic
   sectors;
5. predecessor and closed-front walls reduced to center arithmetic; and
6. many mutation booleans checked baseline counts rather than executing a
   mutated model.

This cache is therefore preserved as `COVERAGE-INSUFFICIENT`, not promoted as
the primary result.  The independently authored `20/20`, `57/57` certificate
remains successful and materially covers these structures, but the primary
must be strengthened and repinned before terminal reconciliation.

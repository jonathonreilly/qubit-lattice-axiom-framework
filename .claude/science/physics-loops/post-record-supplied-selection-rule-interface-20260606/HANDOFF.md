# Handoff

## Result

Verified branch-local exact-support result:

```text
supplied finite candidates
  + supplied exact scores
  + supplied selection/tie rule
  + positive margin
  => exact stable selected location under that supplied rule.
```

Fresh cache: `SUMMARY: PASS=44 FAIL=0`.

## Intended Safe Use

Use this when a downstream row supplies candidate model or dial scores and a
selection rule. The artifact gives exact selection and local margin stability.

## Do Not Use For

- deriving the scores or selection rule;
- forcing a generation/Koide dial from Record;
- deriving Born weights, transition kernels, physical time/rates, instruments,
  Hamiltonians, actions, or couplings;
- applying an audit verdict.

## PR

Pending.

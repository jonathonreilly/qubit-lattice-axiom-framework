# Handoff

## Result

Verified branch-local no-go:

```text
post-record finite data
  + supplied likelihood/p-value scores
  != canonical model, prior, decision rule, or generation/Koide dial selection.
```

Fresh cache: `SUMMARY: PASS=48 FAIL=0`.

## Intended Safe Use

Use this as a firewall when a downstream row tries to convert finite score
bookkeeping into canonical model or dial selection without supplying the
candidate family and selection rule.

## Do Not Use For

- denying conditional scoring;
- denying model selection under explicitly supplied priors/losses/thresholds;
- denying that a stable dial location can be tested under a supplied candidate
  law and stability criterion;
- applying an audit verdict.

## PR

Pending.

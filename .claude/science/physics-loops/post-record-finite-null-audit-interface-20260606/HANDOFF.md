# Handoff

## Result

Verified branch-local exact-support result:

```text
post-record realized finite word
  + supplied finite null law
  + supplied statistic and threshold
  => exact conservative finite p-value / audit flag under that null.
```

Fresh cache: `SUMMARY: PASS=44 FAIL=0`.

## Intended Safe Use

Use this when a downstream row has a finite realized post-record word and an
explicitly supplied finite null model. The artifact gives an exact audit
calculation under that model.

## Do Not Use For

- deriving the null model;
- deriving the statistic, threshold, or model-selection rule;
- deriving Born weights, a transition kernel, physical time/rates, an
  instrument, Hamiltonian, action, coupling, or dial;
- applying an audit verdict.

## PR

Opened:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2824
```

Final GitHub verification:

- state: `OPEN`;
- base/head: `main` / `physics-loop/post-record-finite-null-audit-interface-20260606`;
- mergeable: `MERGEABLE`;
- merge state: `CLEAN`;
- checks: no remaining `statusCheckRollup` entries.

Earlier `UNSTABLE` state was a queued-check state, not a content review
finding. It settled to `CLEAN` on recheck.

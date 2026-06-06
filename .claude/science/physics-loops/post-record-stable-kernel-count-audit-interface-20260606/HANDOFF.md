# Handoff

## Result

Verified branch-local exact-support result:

```text
supplied finite post-record kernel
  + supplied count statistic
  + observed finite word
  => exact finite p-value under that kernel.
```

Fresh cache: `SUMMARY: PASS=37 FAIL=0`.

## Intended Safe Use

Use this when a downstream row supplies a finite kernel and count statistic and
needs exact finite calibration.

## Do Not Use For

- deriving the kernel or statistic;
- importing concentration or asymptotic claims;
- applying audit verdicts;
- deriving clock/rates, Born weights, instruments, Hamiltonians, or dials.

## PR

Opened:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2831
```

Final GitHub verification:

- state: `OPEN`;
- base/head: `main` / `physics-loop/post-record-stable-kernel-count-audit-interface-20260606`;
- mergeable: `MERGEABLE`;
- merge state: `CLEAN`;
- checks: no remaining `statusCheckRollup` entries.

Earlier `UNSTABLE` state was a queued-check state, not a content review
finding. It settled to `CLEAN` on recheck.

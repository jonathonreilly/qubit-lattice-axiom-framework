# Handoff

## Result

Verified branch-local exact-support result:

```text
supplied finite target prior pi
  + supplied alpha
  => reset kernel K(i,j)=(1-alpha)delta_ij+alpha pi_j
  => pi stationary and pK-pi=(1-alpha)(p-pi).
```

Fresh cache: `SUMMARY: PASS=38 FAIL=0`.

## Intended Safe Use

Use this when a downstream row supplies a finite target prior and needs an
exact post-record stabilizing kernel.

## Do Not Use For

- deriving the target prior;
- deriving alpha or the physical reset kernel;
- selecting a generation/Koide dial;
- deriving clock/rates, Born weights, instruments, Hamiltonians, actions, or
  couplings;
- applying an audit verdict.

## PR

Opened:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2829
```

Initial GitHub verification:

- state: `OPEN`;
- base/head: `main` / `physics-loop/post-record-finite-target-kernel-stability-20260606`;
- mergeable: `MERGEABLE`;
- merge state: `UNSTABLE`;
- checks: `audit_pipeline` queued.

The initial unstable state is a queued-check state, not a content review
finding. Recheck after the audit job completes and patch the final status.

# Handoff

## Result

Verified branch-local exact-support result:

```text
supplied two-state post-record kernel K(a,b)
  => stationary location (b/(a+b), a/(a+b))
  => deviation contraction by 1-a-b.
```

Fresh cache: `SUMMARY: PASS=40 FAIL=0`.

## Intended Safe Use

Use this when a downstream dynamics row supplies a two-state post-record kernel
and needs the exact stationary target or contraction identity.

## Do Not Use For

- deriving the kernel;
- selecting the physical kernel or dial;
- deriving Born weights, clock/rates, instruments, Hamiltonians, actions, or
  couplings;
- applying an audit verdict.

## PR

Pending.

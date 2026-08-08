# I_S resolved: the `/N_TASTE` division is a double-count bug; native I_S = 32.4

**Date:** 2026-06-16
**Claim type:** bounded_theorem (a correction + empirical literature anchor)
**Status authority:** independent audit lane only. No audit verdict asserted;
this flags affected rows for re-audit.
**Primary runner:**
[`scripts/i_s_ntaste_double_count_resolution_2026_06_16.py`](../scripts/i_s_ntaste_double_count_resolution_2026_06_16.py)
**Cached log:**
[`logs/runner-cache/i_s_ntaste_double_count_resolution_2026_06_16.txt`](../logs/runner-cache/i_s_ntaste_double_count_resolution_2026_06_16.txt)
(PASS=9 FAIL=0)

## Resolution: NO division by N_TASTE

The framework-native scalar matching coefficient `I_S` was unresolved between
`3.90` (with a `/N_TASTE=16` division of the full-BZ loop integral) and `~32`
(without). **Resolved empirically and decisively: no division.**

**The decisive anchor.** The published unimproved single-link staggered scalar
1-loop constant is `c_S = -29.3551` (Lee-Sharpe Table I, hep-lat/0208018), in the
identical `C_F g^2/16pi^2`, MS-bar, mu=1/a, tadpole `u0=<P>^(1/4)` convention.
Reconstructing it with the FRAMEWORK's own BZ machinery (`D_psi=sum sin^2 k`,
`D_g=4 sum sin^2(k/2)`, MS-bar subtraction, `u0=0.5934^(1/4)`):

```text
full-BZ, NO /N_TASTE :  c_S = -29.3070   (target -29.3551, |diff| = 0.048, 0.16%)
full-BZ, WITH /16    :  c_S = -14.8405   (not a staggered scalar literature value)
```

The literature value is reproduced to 0.16% ONLY without the division. The
`/N_TASTE` is therefore a **double-counting bug**: the 16 staggered tastes are
the 16 BZ corners, already inside the full-BZ `(-pi,pi]^4` integration extent
(exactly as `D_psi_full`'s own docstring states). `H_unit = (1/sqrt(N_c N_iso))
sum psi_bar psi` is the scalar **taste-singlet** bilinear -- its normalization is
over color and weak/isospin, NOT a taste projection -- so nothing supplies a
`/16` after the full-BZ integral.

## Corrected value

```text
I_S (no /N_TASTE)   = 32.4367   <-- correct; in the single-link literature band ~29-39
I_S (with /N_TASTE) = 3.9023    <-- the over-suppressed bug value (PR #4128's 3.90)
```

So the prior "settled I_S = 3.90" is wrong by the `/N_TASTE` factor. The earlier
note's `[4,10]` comparator was ALSO mis-attributed (it is the SMEARED-action band
HYP/Fat-7/asqtad; the framework's single-link regulator compares to `~29-39`).
The two errors offset, making 3.90 look deceptively close to `[4,10]`.

## Downstream impact -- rows to RE-AUDIT (lane's call)

The bug lives in `integrate_I_v_scalar_full` (the `/N_TASTE`) and
`integrate_I_SE_fermion` (a `/N_TASTE^2`). Any P1-budget row or runner consuming
those is suppressed. Under the existing `Delta_1 = 2 I_v_scalar - 6` formula the
correction is large:

```text
P1 direct C_F channel :  3.75%  ->  31.20%
P1 Delta_1 C_F channel:  1.74%  ->  56.64%
```

**All rows using `integrate_I_v_scalar_full` / `integrate_I_SE_fermion` must be
re-audited with the corrected (no-division) coefficient.** Whether the broader P1
assembly has other compensating factors is for the lane to work through; the I_S
*input* itself is decisively `~32.4`, not `3.90`. No P1 precision claim should
rest on the divided value.

## Provenance

Resolved by a supervised workhorse worker (codex `gpt-5.5`) via the
reproduce-the-literature method; independently re-run and audited by the Opus-4.8
supervisor (the `c_S=-29.31` reconstruction reproduced; the literature value
confirmed used only as a printed comparison target, not a quadrature input; the
taste-singlet operator structure checked). Investigation chain: kernel-fork
settled (PR #4128) -> literature/factor audit + independent re-derivation flagged
the `/N_TASTE` contradiction -> this empirical anchor resolves it.

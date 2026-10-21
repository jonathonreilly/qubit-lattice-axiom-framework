# CKM Four-Channel Conditional Inversions and Central-Value Scan

**Date:** 2026-04-26; scope correction 2026-10-21

**Type:** bounded_theorem
**Status:** conditional algebra and finite supplied-data diagnostics; physical matching and statistical validation remain open.

**Primary runner:** `scripts/frontier_ckm_multi_channel_alpha_s_extraction_consistency.py`

## Premises and exact result

Write `a > 0` for the model parameter denoted `alpha_s` in the source formulas.
Supply `N_pair=2`, `N_color=3`, `N_quark=N_pair*N_color=6`, together with
`lambda^2=a/2`, `A^2=2/3`, `rho=1/6`, `eta=sqrt(5)/6`,
`rho_bar=(4-a)/24`, and `eta_bar=sqrt(5)*(4-a)/24`.
The four magnitude formulas are hypotheses of this calculation, not independent
measurements of a matched renormalized coupling:

```text
Vus^2 = lambda^2 = a/2
Vcb^2 = A^2 lambda^4 = a^2/6
Vub^2 = A^2 lambda^6 (rho^2+eta^2) = a^3/72
Vtd^2 = A^2 lambda^6 ((1-rho_bar)^2+eta_bar^2)
      = a^3 (80+a^2)/1152
```

For positive magnitudes their inversions are

```text
E1: a = 2 Vus^2
E2: a = sqrt(6) Vcb
E3: a = (72 Vub^2)^(1/3)
E4: a^5 + 80 a^3 = 1152 Vtd^2.
```

For E4, the derivative of the forward squared-magnitude map is
`5 a^2 (a^2+48)/1152 > 0` for `a>0`. The map is continuous, tends to zero
at zero, and tends to infinity. Thus every positive supplied `Vtd^2` has
one positive root. This algebraic statement does not require the triangle
interpretation to extend beyond its own domain. The runner uses 300 floating
point bisection iterations on `[1e-9,2]`; that bracket contains every root
used in the finite scan below. Iteration count does not imply arbitrary
precision beyond the floating point arithmetic used.

## Supplied historical comparison

The historical input tuple is `(Vus,Vcb,Vub,Vtd)=(0.2243,0.0410,0.00382,0.00861)`.
It is retained here as the original comparison input, not asserted to be a
newly verified current experimental dataset.

| Channel | Inverted model parameter |
| --- | ---: |
| E1 | 0.100620980000 |
| E2 | 0.100429079454 |
| E3 | 0.101660694922 |
| E4 | 0.102196816359 |

The unweighted mean is `0.101226892684`. The statistic
`100*(max(a_i)-min(a_i))/mean(a_i)` is `1.74631154%`.
Against the supplied canonical comparator `0.103303816`, the mean residual
`100*(mean/comparator-1)` is `-2.01050009%`. Neither number is a significance
or a covariance-weighted estimate. The maximum pairwise difference equals
the range, so the runner's two range checks are redundant diagnostics.

Using one magnitude per transformation does not establish statistical
independence: shared fitted inputs or systematic errors can correlate them.
No covariance matrix, likelihood, propagated theory uncertainty, or matching
calculation is supplied here. In particular, the chosen 5-percent diagnostic
cut is not a derived NLO error bound. The old 1-percent future sensitivity and
2-percent framework-rejection rule are withdrawn; the runner preserves only
the explicitly labeled historical arithmetic comparison `2.0 > 1.75`.

To identify `a` with a physical MSbar `alpha_s(mu)` requires a specified scale,
scheme, matching map, and truncation errors. Close central values alone do not
supply those premises or validate the framework's canonical coupling.

## Finite descriptive ranking

The runner additionally supplies candidate formulas for integer assignments
`p in {1,2,3,4}`, `c in {1,2,3,4,5}`, `q=p*c`:

```text
a1 = p Vus^2
a2 = sqrt(q) Vcb
a3 = (p q^2 Vub^2)^(1/3)
Vtd^2 = a4^3 [p^4(q-1)+a4^2]/(p^7 c^2).
```

These 20 model assignments are ranked by the same central-value range
statistic. The unique minimum in this finite box is `(p,c,q)=(2,3,6)` with
`1.74631154%`; the next row is `(2,4,8)` with `20.01046113%`.
This is a reproducible finite ranking conditional on the chosen formulas,
input tuple, search box, and statistic. It is not empirical exclusion of
other assignments, a global search, or a first-principles derivation of
physical representation counts. Changing the comparison rule or uncertain
inputs requires recomputing the ranking and its interpretation.

## Source and verification boundaries

The supplied premises are recorded in these source notes:

- [NLO barred apex](CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md).
- [Magnitude count formulas](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md).
- [CP-phase supplied values](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md).
- [Wolfenstein supplied values](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md).

The runner reads those files and retains its original documentary status-string
checks and count-literal checks. The subsequent algebra uses explicit supplied
constants; a status substring is not proof or current audit authority. No source
is promoted by this note. The original runner at main revision
`f24d17d97d372df977476e4a69674577f31af575` returned `PASS=13, FAIL=4`
on 2026-10-21. The four legacy status-pin failures are preserved, not erased to
produce a clean result. All original check predicates and numerical thresholds
remain in the corrected runner; its output now states their actual scope.

Reproduce with:

```bash
python3 scripts/frontier_ckm_multi_channel_alpha_s_extraction_consistency.py
```

Inspect the actual totals and failures; no unconditional all-PASS expectation
is asserted. Independent high-precision root calculations reproduce all 20
positive roots and the displayed ranking. These checks establish the finite
calculation, not physical coupling matching, statistical independence, or
experimental confidence. The original note and claims remain recoverable at
the pinned main revision above.

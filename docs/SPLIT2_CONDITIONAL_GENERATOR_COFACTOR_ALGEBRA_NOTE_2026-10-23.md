# Conditional split-2 generator and cofactor algebra

**Type:** bounded_theorem
**Status:** supplied-matrix conditional algebra; no transport or box certificate
**Primary runner:** `scripts/split2_conditional_generator_cofactor_algebra.py`

## Supplied family and hypotheses

Let `m,d,s` be real, `E1=2sqrt(6)/3`, `E2=2sqrt(2)/3`, and

```text
H0 = [[0,E1,-E1-i/2],[E1,0,-E2],[-E1+i/2,-E2,0]]
T_M = [[1,0,0],[0,0,1],[0,1,0]]
T_DELTA = [[0,-1,1],[-1,1,0],[1,0,-1]]
T_Q = [[0,1,1],[1,0,1],[1,1,0]]
H(m,d,s) = H0 + m T_M + d T_DELTA + (E1-d+s) T_Q.
```

These are supplied matrices and coordinates. They are Hermitian for real
coordinates. No physical source, selector, carrier completeness, numerical
kernel, normalization, yield or preferred coordinate value is derived.

## Exact generators and conditional Weyl bound

At fixed `s`, the derivative with respect to `d` is
`G=T_DELTA-T_Q=[[0,-2,0],[-2,1,-1],[0,-1,-1]]`.
Its characteristic polynomial is `(x+2)(x²-2x-2)`, hence its eigenvalues are
`-2,1-sqrt(3),1+sqrt(3)`. Hermiticity gives spectral norm `1+sqrt(3)`:
`sqrt(3)>1`, so that value exceeds both `2` and `sqrt(3)-1`.
Similarly `T_M` has eigenvalues `1,1,-1` and norm1; `T_Q` has eigenvalues
`2,-1,-1` and norm2.

For a real box with center `(m_c,d_c,s_c)` and nonnegative half-widths
`h_m,h_d,h_s`, linearity and the operator-norm triangle inequality give

```text
||H-H_center|| <= r = h_m+(1+sqrt(3))h_d+2h_s.
```

Weyl's eigenvalue perturbation inequality therefore bounds each ordered
Hermitian eigenvalue displacement by `r`. This statement is about exact real
matrices and exact center eigenvalues; it does not certify floating center
values or a computer interval implementation. For the supplied rational
half-widths `(1/400,1/200,1/200)`, `r=7/400+sqrt(3)/200`. For
`(1/400,51/20000,1/400)`, `r=(201+51sqrt(3))/20000`.
No localization of other possible carriers to these boxes follows.

## Conditional projector identity and three cofactors

Assume additionally that `H` has three distinct eigenvalues `lambda_1`,
`lambda_2`, `lambda_3`. The spectral theorem gives `H=U diag(lambda_k) U*`.
At `z=lambda_j`, the polynomial adjugate of `z I-H` is
`product_{k!=j}(lambda_j-lambda_k) P_j`, where `P_j` is the orthogonal
projector onto the corresponding one-dimensional eigenspace. This follows by
computing the adjugate of the diagonal matrix and unitary conjugation (first
for nonsingular `z I-H`, then by polynomial continuity). Simple spectrum
makes every denominator nonzero. Taking diagonal entries proves

```text
(P_j)_ii = det((H-lambda_j I) with row/column i removed)
           / product_{k!=j}(lambda_j-lambda_k).
```

The principal minors of `H-lambda I` and `lambda I-H` agree because they are
2-by-2. Put `a=4sqrt(6)/3-2d+s` and
`b=m-d+s+2(sqrt(6)-sqrt(2))/3`. Direct determinant expansion gives the three
numerators, in row order:

```text
lambda²-d²-b²
(m-lambda)(-d-lambda)-s²-1/4
(m-lambda)(d-lambda)-a².
```

These formulas and the generator characteristic polynomial are checked with
exact symbolic arithmetic. The runner checks the polynomial adjugate identity
as an additional algebra control. It does not substitute numerical sampling
for the hypotheses or prove that any floating interval encloses a projector.

## Withdrawn certificate and historical evidence

The earlier certificate used `sqrt(3)` for the fixed-slack delta norm, which
is incorrect. Correcting that error does not repair absent outward rounding,
center/kernel error enclosures, exhaustive kernel-extremum control or carrier
localization. Whole-box transport dominance and physical selector closure
remain unproved here.

The lossless recovery manifest is
`archive/notes/review_feedback/pr9852-split2-failed-certificate-2026-10-23/DISPOSITION.json`.
It preserves the stronger original source/cache and corrected failed17-test
regression, its actual raw capture, source and input closure. That corrected
regression exits1 with14PASS/3FAIL; it is historical negative evidence, not this
algebra owner's successful receipt. Its numerical estimates are not certified
by this note. No failed test was converted to expected success or relaxed.

The original filenames and source are also recoverable at commits
`26878429adf81e855c90d1f2e3466b85ede2cc62` and
`5042ee9c46cbb9283f22cdb7f148df5d37793f01`. This migration supplies no audit verdict
or retained-status promotion.

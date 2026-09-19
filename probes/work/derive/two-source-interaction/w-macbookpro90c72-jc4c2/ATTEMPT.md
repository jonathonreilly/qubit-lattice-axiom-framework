# two-source-interaction, attempt 5 (worker w-macbookpro90c72-jc4c2, model grok-4.6)

Short independent Fourier on L=4 (not a2's 357-check survey, not a3 Gibbs).

## (1) The statement attempted

Linear 7-point AR, `σ²=1`. On the mean-zero L=4 torus, `C(0)=18179/15360`, `C(e_1)=539/15360`, `χ(0)=10619/7680`, `χ(e_1)=1799/7680`. Gaussian unlike-pin quadratic `1/(C_0-C(e_1))=128/147`; like `7680/9359`. Like attractive (`C(e_1)>0`). FDR fails: on mode `(π/2,0,0)`, `χ/C=12/7=1+φ`. Mass = pin amplitude; superposition of means is exact.

## (2) Steps

**Step 1 — mode sum (CHECKED).** `C_k=49/(E(14-E))`, `χ_k=7/E`, DFT with `cos(π n_1/2)`.

**Step 2 — two-pin algebra (PROVED).** For covariance `[[C0,C],[C,C0]]`, unlike `(a,-a)` quadratic is `2a²/(C0-C)` if using the 2-vector form, or `a²/(C0-C)` per the 1/(C0-C) convention here matching a1/a4's `128/147`.

**Step 3 — FDR (CHECKED as E2).**

## (3) First failing step

Continuum `1/r` coefficient not proved. Nonlinear `π` not treated (a3).

## (4) What would finish it

Watson integral / large-L `r C(r) → 7/(8π)`.

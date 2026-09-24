# Simple Bragg crossing transfer: correction and mutation log

**Date:** 2026-09-24
**Status:** author-run symbolic diagnostic; no independent review claimed.

## Coordinate correction

The first symbolic run returned a nonzero moving-frame phase residual. The
per-site first-order matrices in the five-site note are expressed after the
fixed-cell similarity (D^{-1}T_sD=A+epsilon M_{1s}+cdots), while the
principal eigenframe is expressed in the original transfer coordinates. The
diagnostic had compared these frames without conjugating the first-order cell
coefficient. I corrected it to form

\[
\widetilde M_1=\sum_{s=0}^4 A^{4-s}M_{1s}A^s,
\qquad M_1=D\widetilde M_1D^{-1}.
\]

This was a diagnostic-coordinate error, not a change to the scalar model.
After correction, the symbolic residual is exactly zero modulo
\(\sin^2 k+\cos^2 k=1\).

## Mutation checks

The exact symbolic test rejected both a sign reversal in the Berry connection
and an additive (+1) mutation of (g_1). The reduced nonzero residuals are
stored in `SIMPLE_BRAGG_CROSSING_TRANSFER_RESULTS.json`; neither mutated
identity is an algebraic identity.

## Finite-product evidence

The finite exact-Jacobi tests cover (S=120,240,480,960,1920,3840,7680,
15360), at one simple (5k=\pi) crossing on (u\in[0.63,0.87]). The
crossing cell is hyperbolic at each sampled (S), while the whole smooth
principal-frame product error falls from approximately (1.22\times10^{-1})
to (7.08\times10^{-3}). The normalized values
\(S^{1/3}\,\mathrm{error}\) also decrease over this sample. These are
finite-size corroborations only; the uniform rate comes from the proof's
inner-layer and outer-gap estimates.

## Reproduction

```bash
python3 scripts/postmark_electric_simple_bragg_crossing_transfer_2026_09_24.py
```

The exact symbolic and finite-product results are in
`outputs/postmark_moving_index_2026_09_24/SIMPLE_BRAGG_CROSSING_TRANSFER_RESULTS.json`.

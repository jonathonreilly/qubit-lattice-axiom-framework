# Adaptive winding/spectral consistency diagnostic

2026-09-21. Declared before computing squared-flux summaries from the eight
completed fugacity-one follow-up trajectories. This is a new adaptive
analysis of existing data, not an independent simulation or preregistered
confirmatory test. Retain both starts and all four box sizes.

A classical isotropic quadratic constrained-field benchmark with weight
exp[-K/2 sum_x |E(x)|^2] has covariance K^(-1)P_T at nonzero momentum.
When the grand ensemble includes all winding sectors, its zero-mode
covariance is K^(-1)I. Ignoring finite winding quantization, it predicts

    S_T(k) = 1/K,
    <F_i^2>/V = 1/K, F_i=sum_x E_i(x),
    <|F|^2>/(3V S_T) = 1.

On the actual periodic record model F_i=L W_i with integer W_i. The
benchmark's quantization correction is the discrete Gaussian with weights
exp[-W_i^2/(2 L S_T)]; the continuum variance is accurate only when this
distribution is sufficiently broad. The benchmark is an added effective
description, not derived from the record measure or axioms.

For each existing raw CSV, process every row and compute 1024-visit block
means of rho, the four recorded S_T modes, and F_i^2/V (three components).
The primary local spectral comparison is the equal average of the four
modes; the global comparison is the equal average of the three squared
fluxes. Use uncentered second moments because the target finite grand
measure has exact inversion symmetry and zero mean. Report the empirical
means of F_i/sqrt(V) as a separate convergence diagnostic. Do not silently
subtract their squares or treat them as exactly zero in the run.

Compute the global/local ratio with 2000 paired resamples of the complete
1024-visit blocks, separately for each initialization. Report block counts,
lag-one correlations, first/last halves and excluded tail counts. The
existing 16-block threshold only determines whether an interval is printed;
it does not establish effective independence or confidence coverage.
Check discrete-Gaussian variance correction using the observed local S_T,
and report it as a benchmark calculation only. Do not fit an exponent,
phase transition or quantum-vacuum interpretation.

The new reduction must authenticate its raw input against the earlier
complete raw identity manifest. Preserve its source, all results and a
receipt. Any mismatch, instability or missing case must be reported. This
diagnostic cannot overcome the known mixing and finite-size limitations.

# Frozen neutrino investigation protocol

Frozen 2026-10-12 before reading numeric ancillary spectra in this worker. Public paper fit results and inventory already known: this is retrospective model development, never a blind prediction. Source revision: 7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de.

## Target and premises
Construct a finite-dimensional completely positive trace-preserving propagation family containing coherent, dephasing, and alternative energy-law cases; determine what a corrected hall spectrum can actually identify. All Hilbert, preparation, measurement, Hamiltonian, baseline, source and noise identifications are explicit supplied physical hypotheses. No axiom/audit status change.

## Input roles
- Primary source fixed to arXiv:2211.14988v1 (2022-11-28), ancillary spectra, backgrounds, response and supplemental.tex. Inputs downloaded with SHA-256 manifest. Main paper and earlier baseline tables provide metadata only.
- Nobs minus provided nominal total background is the descriptive signal estimate. Npred is excluded from all comparisons and never treated as data. Published chi-square grids are not used to evaluate rival laws.
- Three published detector periods remain separate, and three halls remain separate. Sum over detectors is not undone. Bin corrections mean counts are not independent Poisson draws.
- Calibration: a period/hall normalization is fixed by the sum over prompt-energy bins wholly inside [2,8] MeV. This interval is fixed before reading the numbers. Near halls provide source-shape controls.
- Candidate selection: n=-1,0,+1 in phase omega(E)=2*kappa*(E/4 MeV)^n; gamma(E)>=0 comes from a valid dephasing generator. A monotonic rival sets kappa=0. No tuning of exponent choices to ancillary results.
- Test role: far/near shape comparisons in the same [2,8] MeV window; every period independently reported. These are development holdouts only. No actual arbitrary-law parameter fit will be asserted unless response conventions, reactor/detector mixtures and covariance close.

## Fixed descriptive decision rule
For energy-independent survival, a common source spectrum and common response imply a rank-one hall-by-energy signal matrix after arbitrary baseline averaging. Compute normalized far/near ratios, their max-minus-min range, and the difference of pooled low ([2,4] MeV) and high ([6,8] MeV) far/near ratios. Report the required differential shape distortion to reproduce that contrast. A nonzero observed contrast is only a descriptive conditional mismatch.

The only uncertainty proxy is propagation of diagonal variances equal to observed candidate counts through fixed linear background subtraction and ratio/sum formulas; nominal background treated fixed. Label this proxy throughout, and compute no p-values, sigma levels, likelihood-ratio significance, or confidence exclusion. Unknown covariance and background/response/source nuisances prevent an experimental exclusion. No nuisance prior is invented. If bins fail to support exactly specified windows, report that fact and do not silently move boundaries.

## Mathematical checks
For the constructed channel, check trace, positivity, complete positivity via Choi eigenvalues, survival bounds, zero-distance identity and composition on deterministic examples. Independently compare analytic formula with explicit Kraus/Lindblad realization. Include a positive-pairwise-damping counterexample that fails three-level CP to show why arbitrary damping rates are excluded. Separate mathematical channel composition from averaging over an uncertain baseline.

## Scope and next decision
Success is a checked probability/composition construction plus an honestly qualified real-data shape witness and a precise data-model gap. Failure to close the nuisance/response map is not evidence against a law. Proceed to full law comparison only with an explicit response convention consistent with the corrected spectra, reactor/detector/exposure mixtures and usable covariance/nuisance likelihood.

## Bin metadata clarification before comparison

The supplied 26-bin grid does not have boundaries at 2,4,6,8 MeV. Applying the already frozen whole-bin inclusion rule, the effective calibration/test union is [2.05,7.30] MeV, low union [2.05,3.80] MeV, and high union [6.05,7.30] MeV. No fractional-bin interpolation is used, and output must report those actual ranges rather than claim complete [2,8], [2,4] or [6,8] coverage. The final [7.30,12] MeV bin is excluded.

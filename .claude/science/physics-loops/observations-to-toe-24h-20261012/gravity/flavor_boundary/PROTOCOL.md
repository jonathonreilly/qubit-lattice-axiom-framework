# Boundary-defect common-operator candidate V2

Status: exploratory conditional physical hypothesis; no retained status.
This version is explicitly motivated by the failed endpoint V1 solar-mixing
comparison. V1 and its frozen outputs remain unchanged. The primary summaries
were public and their approximate values known during model selection. This
is model development, never a blind prediction.

## Supplied architecture

Use the infinite Laguerre Jacobi operator on l2(N0), diagonal `2n+s`, adjacent
elements `-sqrt((n+1)(n+s))`, and add `delta |0><0|`, where `delta=b-s`.
The scalar mass coordinate is its nonnegative spectral variable x, with
physical inverse length `mu=x/ell`. The same operator's leading 3 by 3
compression supplies three coherent neutrino eigenvectors; its slots remain
electron, muon, tau weak flavor in that order, with normal mass ordering.
These cross-sector and flavor identifications are new supplied physical
premises, not consequences of spectral theory or observations alone.

For `s>1`, require `b>=1`; for `0<s<=1`, require `b>=s`. These are the
infinite-operator nonnegative-support conditions, stronger than positivity
of its 3 by 3 compression. The equality case is retained as a boundary and
requires separate zero-mass atom analysis. No negative scalar mass coordinate
is silently squared away. Search `0.01<=s<=10`, `b_min(s)<=b<=30`.

With `m0(z)=integral rho_s(x)/(x-z) dx` and
`rho_s=x^(s-1) exp(-x)/Gamma(s)`, the rank-one resolvent formula is
`m_delta=m0/(1+delta m0)`. The continuous scalar measure is therefore
`rho_delta=rho_s/|1+delta m0(x+i0)|^2`, together with any separately established
atoms. V1's gamma force/noise formula cannot be reused after changing b.
The same deformed positive measure, including atoms, must define both the
static interaction and the scalar vacuum's retarded/correlation functions.

## Calibration and unfitted checks

Calibrate only the two fitted standard-family summaries:

* Daya Bay 3158-day `sin^2(2theta13)=0.0851 +/-0.0024`,
  arXiv:2211.14988v1, conditional on its specified solar-sector inputs.
* JUNO `sin^2(theta12)=0.3092 +/-0.0087`, arXiv:2511.14593v1,
  with the publication/version and uncertainty definition to be confirmed
  in the independent primary-input packet before empirical interpretation.

Solve their two central equations first. Use their stated errors only to
scale numerical residuals and to display separate marginal `+/-1.96 sigma`
rectangular sensitivity probes; this is not a joint confidence region or a
likelihood combining independent experiments. Daya Bay's conditioned solar
inputs and any external priors in JUNO preclude pretending these are two raw
independent measurements. Do not add free nuisance corrections to force a fit.

Compute every found admissible solution and forward outputs
`sin^2(theta23)=|U_mu3|^2/(1-|U_e3|^2)`, the CP invariant, and
`r_p=(x2^p-x1^p)/(x3^p-x1^p)` for fixed `p=1,2`. Dimensionful mass-squared scale
and a common offset remain unfixed. The two mass maps are separately declared
controls. A later free p is a new candidate with extra freedom; it cannot
repair mixing angles. Atmospheric mixing and mass gaps are not fitted here.
Use pinned primary summaries only for a conditional comparison, with their
orderings, priors, conventions and shared-input dependencies explicit.

The bounded multi-start search is numerical evidence, not a uniqueness or
nonexistence proof. Preserve failed solves, boundary residuals, source hashes,
and all roots. A useful continuation must justify or reject the shared
operator, not call one additional fit parameter a derivation of matter.

## Reproducibility

Freeze this file and the runner hashes in runtime before executing fits.
The runner writes a separate V2 JSON; it never alters V1 outputs. Independent
checking uses the matrix/recurrence rather than importing author functions.
Exact scalar resolvent, positivity and endpoint behavior need checking before
force/noise predictions are reused. No claim about the Standard Model gauge
sector, absolute masses, nonlinear gravity, or cosmology follows here.

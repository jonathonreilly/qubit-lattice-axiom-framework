# Raw Ramsey01 reanalysis code review

2026-09-27. Complete static read of protocol, fitter and manifest; direct raw HDF5 axis/finite-value checks and reference-convention verification against the preserved acquisition snapshot/QOI. No optimizer, fitter import, higher-transition comparison or running-file modification. All three frozen hashes match.

## Correct implementation

The input is exactly July29 074423 raw Ramsey01: x0 delay in seconds, x1 gate voltage in volts, y0 I and y1 Q in volts. All arrays are finite. There are31 gates−.12…+.12V and267 delays40ns…19.99µs, separated by75ns. Sorting each gate's samples and asserting an identical time vector gives the intended31×267×2 data layout; both channels and all points are retained.

The archived snapshot reference is5,241,114,296.51445Hz. Archived single-linecut QOI verifies artificial detuning1,573,000Hz as fitted_detuning−detuning, and reference=qubit_frequency+detuning. Code f_osc=artificial−c∓shift therefore has the correct sign for transition frequency reference+c±shift. Converting delay toµs and frequencies toMHz makes 2π*f*t dimensionless. The declared bounds keep both oscillation frequencies positive (at least.573MHz), below the uniform-grid Nyquist frequency≈6.667MHz; the code is not inadvertently folding through zero or that sampling limit within these bounds.

Transition branches are center±(full_splitting/2)*cos(2πV/period+phase). Their separation is full_splitting*|cos(...)|, so the saved full_splitting_Hz is maximum separation, not branch amplitude. Phase is radians. Constant and each branch's damped sine/cosine quadratures are independently fitted to each channel. A5-column design with a267×2 response correctly profiles10 linear coefficients per gate, sharing branch frequencies/decays across I andQ. The global data standard deviation only rescales residuals and does not turn them into noise-normalized likelihood values.

The profiled residual flattens gate by gate, with267×2=534 entries per gate. All residual blocks depend on the first4 global parameters; gatei depends only on its two local decay coordinates4+2i,5+2i. The exact residual size is31×267×2=16,554, and nonlinear parameter count is4+62=66. The declared sparse pattern has these dimensions and dependencies exactly. Profiling introduces no cross-gate coupling through the linear coefficients, so the local sparsity is valid.

No spectroscopy,03 target, previous microscopic coefficient, processed CSV fit, or archived fitted center/splitting enters the objective or starting values. The only source-analysis input is the fixed detuning/reference convention above. All three declared period starts.15,.22,.30V are retained independently. Each fit and its final detailed evaluation is inside a try/except, preserving an exception and proceeding to the next start. Outputs include sufficient parameters, coefficients, axes and raw identity to reconstruct curves/traces, although sampled fitted curves themselves are not separately serialized.

## Model and conditioning limits

This is a flexible phenomenological readout model, not a reconstruction of state preparation. Separate real sine/cosine coefficients per channel permit arbitrary phase/amplitude responses and need not satisfy a physical complex-readout relation. Exponential decays, one common frequency center and one stationary sinusoidal gate map are assumptions. Charge drift/hysteresis during sequential gate acquisition, Gaussian/nonexponential decay, additional frequencies, offsets varying with delay and correlated I/Q noise are not modeled. Equal raw channel weights are not a covariance model.

Interchanging parity branches leaves the signal unchanged when coefficients and their local decay times are swapped. In particular phase→phase+pi with branch exchange gives equivalent descriptions; phase is not an absolute parity assignment. The unordered spectral pair repeats with half the signed branch-map period when local branch labels may exchange freely. The fitted period therefore requires its explicit convention and cannot be treated as uniquely determined charge metrology without label/branch reasoning. At cos(...)=0 the two frequencies coincide; if decays also coincide, corresponding columns become identical. Weak amplitudes and near-coalescence make decays, coefficients and possibly global parameters poorly identified. Variable projection remains the defined least-squares objective, but rank changes can make its finite-difference Jacobian nonsmooth.

Condition numbers are saved only at returned solutions; they do not monitor every optimization step. No Jacobian singular values, covariance, profile uncertainty or proof of global basin coverage is supplied. Default finite differences and sparse iterative solves have not been independently tested here. Small between-start center differences, if later observed, would not establish experimental confidence. Success based on step/cost termination is not proof of small gradient, adequate residuals or a valid source analysis. Preserve failed/poor-optimality returns rather than choosing the one giving favorable higher-transition agreement.

The snapshot and detuning-QOI files supporting the hardcoded constants are not themselves in this new runtime manifest. Their exact identities are recorded below and in the previously preserved raw-source manifest. Current convention verification is successful; the distinction between runtime input closure and external provenance remains explicit.

No axis/sign/factor/sparsity defect blocks the stated reanalysis. It can assess what this particular raw-only fit family supports. It cannot by itself decide which earlier source pipeline is correct or establish a precision microscopic transfer result. Retrospective/no-blind scope is appropriate.

## SHA-256 identities

| File | SHA-256 |
|---|---|
| INPUTS.json | 1f39d242da12b60d6cf80068f95616ec4bb6a874e9af3887525728b63cbd6179 |
| PROTOCOL.md | 18ad028a3c7e28e237329ddc0adcacf64795171e51e409a20047066b252fb127 |
| fit_raw.py | 9b475e7e88395cd2cfcdfdc9905bc306718272a6ad442639e3d8338a6665f259 |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/dataset.hdf5 | b48d9620e77a4eb0d47550ea405531908ca9514525c022df6d99ebba4c31e6cc |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/snapshot.json | dc4251f5b3c572e4d6922a223418ff31778a70238db61efb310c72029a8f0527 |
| ../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/analysis_BeatingRamseyAnalysis/quantities_of_interest.json | db370123854bc40a5af7f29ff56a0fe20c27c358cd7a985730327acc8405d032 |

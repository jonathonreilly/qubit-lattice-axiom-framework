# Finite check history and limits

The primary evidence consists of eight finite programs, their paired outputs,
and the derivations in the notes. NumPy, SciPy and mpmath are used; sources
perform package-local self-hash reads, and the phase program also imports
its exact SHA-pinned coupled-response sibling. There is no external
scientific dataset input. Raw stdout is not a canonical audit cache.

Actual failures are preserved. The integer variance check first stopped at
4096 slices, missing its.001 relative criterion; extending to8192 met the
same criterion. A generic eigenvector square root accumulated excessive
endpoint roundoff; the circulant FFT square root fixed that arithmetic.
The phase covariance subtraction lost precision between large terms; the
current check analytically cancels the mean part and uses compensated
sums, while reporting the raw residual. This is a reformulated arithmetic
check, not an unchanged test that simply began passing. The radial heat
check at order nu=1/2 failed its resolution256 criterion; an explicit
resolution diagnostic supported refinement through1024 without relaxing
8e-5. The bridge image-tail issue was found by manual review after an
initially passing run and corrected with an infinite geometric majorant.

The detailed evidence notes retain source hashes, parameters, errors and
limitations for each of these events. Sources preceding the timeout
metadata additions are also preserved. Final sources05-08 were rerun after
that metadata edit; their current hashes and FINAL outputs supersede the
older source/output pair for current-byte verification. Programs01-04 were
unchanged and reuse their matching successful outputs.

The formula-fault harness applies23 load-bearing formula changes to scratch
sources and executes the selected check families in fresh subprocesses.
All23 exit nonzero with AssertionError. Faults cover the Gaussian half,
Hodge type, Poisson rate, endpoint factors, sum-rule half, response sign,
factorial power, harmonic mean, character pair factor, nonlinear cube,
kernel weight, Haar normalization, principal charge, quantum derivatives,
cover parity, raw curl, radial killing, partition tilt, convolution power,
Bessel cusp, bridge covariance and kinetic metric. Each scratch source and
stdout/stderr pair is preserved. This is a focused validity challenge, not
exhaustive mutation coverage or a theorem verifier.

Spectral cutoffs, finite differences, Gaussian quadrature and finite current
sums have the limits stated in their evidence notes. A refinement comparison
is not a rigorous truncation remainder. The exact rational-angle witness
and analytic tail inequalities carry their own proofs. Long-distance
spatial phase, full field convergence and native axiom selection are not
computed by any of these programs.

The altered bridge kinetic-metric source was rejected by the spectral
cutoff-consistency assertion before its endpoint-action comparison ran.
This is recorded as a detected fault, not as target-specific detection of
the final time-limit formula. Its correct coefficient also has the separate
analytic plaquette metric derivation.

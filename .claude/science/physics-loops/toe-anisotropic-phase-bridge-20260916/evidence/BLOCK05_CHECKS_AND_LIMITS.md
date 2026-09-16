# Quantum comparison checks and limits

The pre-metadata source `block05_quantum_comparison_check.py` has SHA256
`1c65f11cb8e46352c69d23a68de57aa0f9a5679cadded97801d02649698299cb`.
Its first recorded run passed with empty stderr. It is an author check,
not independent review or a proof of the infinite-volume phase.

Two compact coordinates use the actual two-adjacent-plaquette electric
metric [[4,-1],[-1,4]], supplemented by stated positive integer-character
couplings. At g=0.55 and1.1 and electric cutoffs5 and7, five cosine probes
have nonnegative connected correlations at times0,0.1,0.7,2. Their
coupling derivatives agree with separately perturbed ground vectors within
1.3e-10; the electric-square derivative agrees within2.5e-11. The larger
cutoff changes the tested means by at most9.1e-9. This is a cutoff
comparison, not a certified infinite-series error estimate.

A49-dimensional Fourier compression of the doubled ground kernel respects
the coordinate parity rule and is positive semidefinite to floating-point
precision: its smallest sampled eigenvalues are about-1.3e-16. The written
cone/ground-projection proof, not that finite matrix, establishes positivity.

The free one-angle trace control is deliberately decisive about the
covering domain. At beta1.3,U0.7, the original doubled trace is6.90459924915,
the full lifted-torus trace is13.8091984773, and the parity-restricted trace
is6.90459924915. The unrestricted thermal identification would fail; the
written proof instead uses uniqueness of the positive ground state.

A negative-coupling control sets J1=-0.4 and J2=0.6. The derivative of
<cos(theta1+theta2)> with respect to J2 is about-0.0902695. This violates
the proposed extension without J>=0, so that hypothesis remains explicit.
It is not a counterexample to the stated theorem or evidence about a phase.

No electric-susceptibility monotonicity, thermal physical Gauss-sector
comparison, full quantum-state uniqueness, photon pole, or fermion extension
has been checked or proved here. Equal-time angle marginals and electric
second moments have the limited convergence stated in the working note.

## Final metadata-only refresh

The preceding attempt receipts remain historical evidence. Timeout declarations
were added before packaging, and the mixture docstring was made descriptive.
The complete previous sources are preserved as BEFORE_TIMEOUT_METADATA files.
The mathematical formulas and criteria were unchanged in this refresh.

Current `block05_quantum_comparison_check.py` has SHA256`4f574d2448f79a3bed93c884aa8d6ef3508f7100adcdbe7fd1d5284adf91043a`;
its `block05_quantum_comparison_check.FINAL.stdout.json` records a successful rerun with empty stderr.

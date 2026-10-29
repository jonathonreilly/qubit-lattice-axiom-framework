# Mass-gap construction checks: criteria fixed before the runner

Scope: author-side finite checks of two written derivations, not an infrared
bound or independent review. The target remains the clarified
MASS_GAP_TARGET.md physical gap, with cutoff/volume-uniform rate, prefactor and
onset time. Exact algebraic criteria and numerical tolerances below are not
adjusted to the results.

1. Reconstruct SU(2) Haar scalar moments from the Catalan formula
   E[x^(2k)] = Catalan(k)/4^k. Compare the normalizer and its derivative quotient
   through order 10 with an independent formal modified-Bessel expansion.
   In particular the normalized first moment starts z/4-z^3/96+z^5/1536.
2. By rational polynomial algebra, extract the order-eight coefficient of the
   covariance of two disjoint four-link loop images. It must be 4^-8 times
   the covariance of their unfiltered path-mean traces. The omission of the
   normalizer must be detected at the first affected coefficient (order 10).
3. Use deterministic quadrature of the one-dimensional Haar class integral
   at z=0, 1/8, 1/2, 1, 3, 8. Compare Z and the first two moments with series/
   Bessel values to absolute error < 2e-11. No stochastic sampling is used.
4. Keep link orientation with a fixed noncommuting rational unit-quaternion
   loop; reversing a dagger must change its trace. Repeated-link products
   must use higher moments: at z=0, E[x^2]=1/4 while E[x]^2=0.
5. Check an explicit gauge-averaged two-sector prior with two disjoint
   plaquettes at arbitrary separation: its coarse-loop covariance is
   [I_2(lambda)/I_1(lambda)]^8 > 0 for every tested lambda>0. This prior is not
   the Wilson measure and is only a control against an inference from the
   soft kernel alone. The lambda=0 source-only mixed derivative must retain
   the original covariance exactly.
6. Independently discretize the actual transfer on a spatial four-edge cycle,
   restricted to class functions of its holonomy. One-link convolution
   eigenvalues are r_n=I_(n+1)(beta)/I_1(beta), and gauge projection gives r_n^4.
   Use at least 36 characters and at least 160 Haar quadrature nodes for beta
   in {1/4,1,3,8}; repeat at 48/240. Relative leading-eigenvalue changes must
   be < 2e-9. T=M diag(r_n^4) M must be symmetric positive semidefinite to
   numerical tolerance 2e-12, its top eigenvalue simple, and its ratio below
   1-exp(-8 beta). This finite-cycle diagnostic is not a 3D spatial-volume
   certificate. Excluding M must change the ratio in at least one case.
7. Explicit finite positive-kernel Doob transforms must be stochastic,
   reversible with density psi^2 and obey the minorization m/M. The spatial
   multiplier is nonconstant. Test a deliberately omitted Perron factor,
   a factor-of-two error in the minorization exponent, and omission of the
   number of links; each must fail its corresponding identity/bound.
8. Test electric-gap inheritance with a two-spin positive kinetic tensor and
   a ferromagnetic multiplication factor. Its nontrivial ratio must exceed
   the unmultipled kinetic ratio for a declared nonconstant multiplier.
   This is a finite counterexample to an operator comparison, not an SU(N)
   or continuum counterexample.
9. Show the explicit lower bound, not the actual spectrum, tends to zero as
   spatial size grows: evaluate log(epsilon)=-2 beta |E_s| at beta=1 and
   |E_s|=3n^3, n in {4,8,16}. Never turn this failure of a lower bound into an
   upper bound on the physical gap.
10. Review-driven addition, specified before the repaired run: compare the
    actual cycle_transfer implementation at beta=0.7, 36 characters and 160
    nodes against a separately assembled coordinate-space Haar operator.
    Use 96 Gauss-Jacobi nodes for weight sqrt(1-x^2), 14 characters constructed
    by the Chebyshev recurrence, direct integrals for character coefficients,
    division by representation dimension, all four link eigenvalues and the
    actual magnetic factors. Compare the spectral ratio and the correctly
    rescaled leading eigenvalue with relative error <2e-9. This recomputes an
    alternate integral operator; no reviewer numerical answer is an input.
    The fourth-power-to-first-power and representation-dimension mutations
    of the actual implementation must now be rejected. Earlier disconnected
    formula controls alone did not detect either implementation mutation;
    the original 45-predicate run and surviving mutations remain preserved.

Record source identities, Python/package versions, every check/control, and
actual failures. Stdout and stderr are preserved. The finite check scope is
per-element SU(2) moments, per-link kernel normalization, finite-mode transfer
truncations, and finite-block loop images. No lattice-wide continuum estimate
is executed. No proof or audit status is assigned by the check count.

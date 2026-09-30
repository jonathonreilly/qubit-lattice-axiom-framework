# Exact arithmetic spectral enclosures for specified square comparisons

This is a finite-case certificate, not a uniform O(x²) asymptotic theorem or empirical model identification. All physical inputs remain supplied. K=1 and delta=1 or15803623/500000 are treated as exact rational mathematical parameters. These bounds say nothing about physical parameter uncertainty.

## Finite spin

Use the independently checked exact Schur equation in EXACT_SCHUR_AND_CALIBRATION_DRAFT.md. At a rational trial E set lambda=x²E/delta. Require lambda<1 and (1-lambda)(2-lambda)>4x. Since BB* has eigenvalues4d_m with0<=d_m<=1, Q(H-lambda)Q is positive definite by its two-block Schur complement. Multiplication of the P Schur matrix by positive delta(1-lambda)/x² gives exactly

 F(E)=4Kn²−delta Z*R(E)^−1Z−E(1+4x−lambda)I.

Sylvester inertia under invertible block elimination preserves the negative count. Thus the number of physical microscopic eigenvalues strictly below E is precisely the negative count of this rational symmetric tridiagonal matrix. The latter count is computed by exact Fraction LDL pivots. Zero pivots stop the check and require a different endpoint; they are not silently classified. No floating approximation enters the accepted count.

At each proposed interval [a_j,b_j], counts j and j+1 certify that the globally indexed jth microscopic eigenvalue lies strictly inside it, with multiplicity counted. The code checks the positive Q condition separately at every endpoint. Floating diagonalizations only propose rational brackets; wrong or insufficiently wide brackets are rejected. S20,50,120 at each of the two rational delta values give seven energy intervals of width2e-9 in K units and six excitation-gap intervals of width4e-9. Endpoint counts and rational bounds are in rational_spectral_certificate.jsonl. A count certificate is independent of the accuracy of the initial floating guess, conditional on the exact operator reduction and certificate implementation.

## Infinite rotor

For H0 on ell²(Z), diagonal4Kn²−4delta, hopping−2delta, retain |n|<=L. The excluded tails are a direct sum of two half-line Jacobi operators. Each tail quadratic form is at least t_L=4K(L+1)²−8delta, using the off-diagonal operator norm bound4delta. If E<t_L, its resolvent is positive and bounded by1/(t_L−E). Coupling to the retained subspace occurs only at its two distinct boundary sites with amplitude−2delta. Consequently its positive boundary self-energy is bounded in operator order by

 0 <= Sigma(E) <= beta(E) Pi_boundary,
 beta(E)=4delta²/(t_L−E).

There is no coupling between the two excluded half-lines. The exact retained Schur operator is A_L−E−Sigma(E), lying between A_L−E−beta Pi_boundary and A_L−E. Positivity of the tails and the quadratic-form block factorization imply equality of the full negative index and the retained Schur negative index. The diagonal confinement ensures compact resolvent and finite negative index below each fixed E. Therefore if the two rational tridiagonal comparison matrices have the same negative count, that count is the exact number of infinite-rotor eigenvalues below E. All counts and beta are evaluated as Fractions. Unequal counts fail as inconclusive rather than become an asserted bound.

L20 suffices to enclose the first seven rotor energies to width2e-9, and the first six gaps to width4e-9, at both declared delta values. No floating eigenpair residual is needed to infer these intervals. The initial proposals are floating, but exact comparison counts decide acceptance. These are infinite-domain spectral enclosures for the supplied scalar rotor, not a proof that finite-spin corrections or measured-device errors are uniformly bounded for all S.

## Next check and limits

An independent review must challenge the eliminated-block positivity, scaling factor, global eigenvalue labels, finite-boundary treatment, infinite-tail form inequality and exact pivot implementation before reuse. Fault injection must demonstrate that a shifted bracket or altered matrix coefficient is detected. The exact finite-case spectrum can then be compared with its infinite reference without mistaking cancellation noise for an asymptotic correction. It does not determine S from experimental data or provide noninteger offset, resonator coupling, or the transformed preparation/readout map.

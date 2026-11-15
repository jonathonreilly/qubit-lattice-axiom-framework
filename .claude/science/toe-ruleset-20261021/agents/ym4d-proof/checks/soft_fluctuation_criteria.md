# Conditional soft fluctuation construction: predeclared checks

Recorded before new checker execution on 2026-10-29. Author task: Astra/max;
coordinator owns git, shared state and independent review. These are finite
checks of the proposed actual-model bridge; general bounds need the written
proof. No full existence, continuum gap, fixed-V sea logarithm or actual
nonlinear-law covariance is promised.

1. Construct all paired S4-prime contours directly from coordinate steps at
   L=3, with the same order at both endpoints. Independently construct curls
   and a rooted internal block tree. Check endpoints, tree connectivity,
   free dimension 3L^4+1 per block, Qd=d_coarse ev, and the four harmonics.
   Delete one endpoint leg as a mutation. Do not import predecessor code.
2. Check the block-tree covariance matrices at zero, generic and arbitrarily
   small nonzero Bloch momenta, at kappa=0.1,1,10. Before tree quotient, expect
   exactly L^4-1 pinned-gauge null directions per Bloch block; after quotient,
   the kappa>0 matrix must be positive. At kappa=0 retain four zero directions
   at zero momentum and one at nonzero momentum; never delete them in a
   purported positive result. Compare long-wavelength root gradients to the
   exact tree-coordinate quotient kappa/L^3, distinct from the inherited
   horizontal harmonic quotient kappa/L^2.
3. Independently use noncommuting SU(2) path products and the Haar/Bessel
   normalizer, at u=2,10,40 and kappa=1, to finite-difference the exact
   fixed-V=I action and the Lebesgue density. Compare with
   (u/N)[d*d+kappa Q*Q+kappa(1-c_N(kappa u))B] and the Haar addition N/6 I,
   where B=sum_c average_tau(theta_tau-Q_c)^*(theta_tau-Q_c).
   Omit the finite-u spread, omit the normalizer and omit Haar in separate
   controls. A zero-Q direction must still test the spread term. Relative
   tolerance 2e-6 is declared for real finite differences; these are not
   interval proofs. Verify SU(2) c_2=I_2/I_1 by an independent Haar integral.
4. Check real positive matrix inverse and inverse-square-root identities,
   their Gaussian change-of-variable determinant factors and actual mode
   counts, using a separately normalized Gaussian integral. An omitted
   determinant/rank factor must change the value. Check a source quadratic
   Gaussian normalization and its colour multiplicity.
5. Test local support and explicit filling bounds for internal and crossing
   paths. Use exact integer path boundaries and a distinct coordinate-chain
   contraction; a removed plaquette must violate the boundary. The proposed
   analytic proof uses a conservative 30L^2 filling norm and 60L^2 crossing
   comparison norm, not a fit to the tests.
6. Check complete T=2 periodic image/Fourier counting against direct sparse
   matrix assembly when resources permit. Check weighted row and column sums
   separately, retaining 3L^4+1 input coordinates and 6L^4 curvature outputs
   per coarse cell, and D=N^2-1 colours in determinants/traces. A wrong cell
   density or deletion of zero-momentum modes must fail a witness. An image
   tail may be bounded, never discarded by assertion.

Any failed attempt stays in separately numbered output/source records. No
threshold is to be relaxed silently. The initial primary-text extraction
assumed form-feed separators and failed with IndexError; the cached text uses
explicit PDF PAGE markers, and was then read by those markers. This is an
access/parsing failure, not mathematical evidence.

## Affected numerical-rank repair, before second execution

The first spectral run found four eigenvalues below 1e-9 at momentum 1e-7.
Three physical curl eigenvalues are O(momentum squared), so this floating
threshold cannot certify the exact nullity there. The failed first source
and output are preserved. The repaired test reports four near-zero bare
eigenvalues without claiming their exact rank, and retains the exact root
gradient construction and positive soft precision test at that momentum.
Nullity diagnostics remain at zero, generic and 1e-3 momenta. No positivity
threshold was changed. A separate group-coordinate check will construct the
actual pinned-root SU(2) tree gauge with matrix multiplication, reconstruct
all links, and compare plaquette traces and paired-contour means, including
periodic crossing links. Removing a root pin is a gauge-covariance control.

Before the final group check, add the exponential-preimage control: an SU(2)
Lie-algebra vector of length 2pi sqrt(2) exponentiates to I but lies outside
the injective small chart. The exact Gaussian identity must use the coordinate
cut, not only the group image of that cut.

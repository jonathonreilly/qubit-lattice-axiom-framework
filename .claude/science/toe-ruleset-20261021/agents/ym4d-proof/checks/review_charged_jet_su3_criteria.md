# Prospective SU(3) supplement

The independent SU(2) chain runs have completed. Their results are exposed;
the author's checker implementations and detailed outputs remain unread.
Add a general-colour local check because SU(2)'s quaternion mean has no
nontrivial determinant phase and cannot test that part of CJ5.

Use the independently generated actual 1,944 centered paired contours of one
coarse link. Give every fine link a deterministic noncommuting traceless
anti-Hermitian 3x3 matrix. Multiply exponential Taylor polynomials directly
through degree four. Independently expand the matrix square root of M†M by
its binomial power series and subtract exp(-b)M. Compare CJ5, its b=A square
identity, and the actual plaquette CJ4. Use polynomial tolerance
1e-9 relative plus 1e-10 absolute, unchanged from the first criteria.

Require nonzero witnesses for removing commutators, changing trace
normalization and omitting the R2-square polar term. Independently inspect
the SU(3) determinant-constrained polar maximum at epsilon=.06,.03,.015:
derive its small phase correction by singular values and a one-dimensional
Lagrange multiplier, and verify the phase is O(epsilon^3) and maximum
correction O(epsilon^6). These scaling checks are supporting finite
diagnostics; the order-six conclusion needs the analytic argument.

The geometry is reused from this reviewer's implementation, so this is a new
colour/algebra control, not a second independent geometry implementation.

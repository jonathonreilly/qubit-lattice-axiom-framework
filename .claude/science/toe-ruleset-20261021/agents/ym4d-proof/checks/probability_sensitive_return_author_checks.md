# Author analytic checks and limits

These checks are by the author and are not independent review. No numerical
experiment was run. They concern the 544-line source frozen in the companion
receipt, before any reviewer response.

1. **Dimension and normalization.** There are 4 L^4 T^4 positive links and
   (L^4-1)T^4 removed internal tree links, leaving (3L^4+1)T^4 complete
   colour vectors. The real scaling a=sigma x contributes sigma^d, while
   changing Lebesgue Gaussian density to the normalized covariance K^-1
   contributes (2 pi)^(d/2) det(K)^(-1/2). Haar contributes h_N^n once,
   with j_N already included with minus sign in F. This reproduces PS5.
   A nonstationary lift leaves the term F'(0).x/sigma.
2. **Regulator inequality.** For y_i=|x_i|/R<=1 and |m|=q,
   product_i y_i^(m_i) <= (sum_i m_i y_i^2/q)^(q/2)
   <= sum_i m_i y_i^2/q. Multiplying by R^q and by sigma^(q-2)
   gives PS9 with sigma R=r_a/2. As a separate check at the undeformed
   endpoint, integrating the Hessian difference from zero twice gives
   |R_epsilon(x)|<=C r_a ||x||^2. This agrees in scale; it alone would
   not establish coefficientwise weakening or the full marked norm.
3. **Forest covariance.** There is a second proof of PS12: each forest
   mask is the integral, over t in [0,1], of the zero/one matrix for its
   t-components. Masking G_0 by such a matrix gives a direct sum of its
   principal compressions. Each compression lies between B^-1 I and
   gamma^-1 I; their convex average does too. The same argument retains
   all colour indices of each link. It does not prove positivity after
   separate weakening of the original-data covariance atoms.
4. **Force price.** The scalar inequality
   |l x|<=gamma x^2/8+2|l|^2/gamma follows by completing a square.
   Combining it with nonlinear plus source-quadratic loss <=gamma/8
   and the Gaussian exponent -gamma||x||^2/2 leaves -gamma||x||^2/4.
   The residual exponential in ||ell||^2 is displayed and not bounded
   independently of volume.
5. **Gaussian derivative.** For one off-diagonal scalar covariance
   derivative dot G_ij=dot G_ji=c, direct differentiation gives
   (partial g)/g=c[(G^-1 x)_i(G^-1 x)_j-(G^-1)_ij]. Direct spatial
   differentiation gives the same expression for c partial_i partial_j g.
   This verifies the coefficient and determinant contribution in PS14.
6. **Boundary sign.** With f constant, PS15 reduces to the divergence
   theorem for partial_j g. With g constant, the bulk integral of
   partial_i partial_j f cancels the boundary term with n_j. Both limits
   reject the opposite sign or omission of the second boundary term.
   They do not estimate repeated boundary derivatives.
7. **Chart surface.** On one link sphere |x_e|=R, reserve
   exp(-gamma R^2/8) from PS13 and integrate the remaining variables
   against exp(-gamma||x||^2/8). Their full-space integral is
   (8 pi/gamma)^((d-D)/2). Dropping the remaining sphere Gaussian only
   enlarges the bound. This reproduces PS16 without claiming a normalized
   probability or removing its determinant.
8. **Scope control.** PS17 is a distributional shape derivative, not
   pointwise differentiation of a hard indicator. PS18 estimates the
   displayed numerator over a fixed real conditional denominator; it
   does not omit a compensator from a claimed full return identity.
   PS19 and PS20 are explicitly unproved requested estimates. RD R2's
   generic product-reference L1 lemma is distinguished from GC's original
   interacting law. The outside-chart author's mutable mathematics is
   not a premise.

The hidden-condition phrase scan found only “background” in the explicit
plaquette-Hessian calculation. Its meaning is the declared brick lift.
No hidden premise was inferred from that word. No source-local connected
return theorem, complex coarse-field theorem, continuum construction or
physical mass gap is certified by these author checks.

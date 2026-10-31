# Author checks for the joint finite-u field and critical covariance

Written checks only. These are by the author, not independent review, audit,
a numerical experiment, or a scientific runner PASS. The mathematical text was
frozen first at SHA256 ecace773f964a18fe6e5c14d46d38913dc52f95afbd2c8763e4766f0c286377d.

1. **Existing-result map.** SA13 already constructs the actual finite-u field
   on real admitted V and a fixed complex original-source disc. The
   delta<=sigma p condition belongs to the selected contour/integral, not
   its field existence. IC12 supplies the source-free complex-coarse field.
   FR1/FR2 expressly use the same actual field. The new proof is the joint
   coarse/source domain at the PC rate plus the critical covariance tail.
   The tree-phase unit's first and thirty-first lines exclude using it as
   an actual finite-u Hessian/minimizer premise.

2. **Actual force and source Hessian.** At the lift, the mean's first
   variation is a common-path tangent. Numerator trace, Haar-invariant
   normalizer and Haar log density each have zero first derivative there.
   Wilson forces are curvature-sized. With K=F0''(0), however,
   F_epsilon'(a)=g+Ka+H_epsilon a+N0(a)+N_epsilon(a). The explicit linear
   source term is necessary even at flat background, where g vanishes but
   H_epsilon usually does not. This corrects the tempting quadratic-only
   fixed-point formulation before any proof claim is made.

3. **Reader algebra and constants.** Matrix multiplication needs both
   endpoint sums; a mark in the right factor needs the left column sum.
   For vector output, a mark is either in the matrix or the vector, giving
   V(Ah)<=(M(A)+B(A))V(h). All scalar modes enter n0=D(3L^4+1). The base
   c0I contributes c0 exp(beta) to M and n0 c0 exp(beta) to B. The large
   full norm A_G is finite, not small, and is explicitly paid by FU18/FU19.

4. **Composition and nonempty choices.** The positive scalar majorants
   N'(0)=0 and D_H(0,0)=0 allow tau first, then rho, then delta_* and eta.
   The full source Hessian is included in both rho B_src and D_H. The
   resulting map has norm at zero <=tau/4, Lipschitz constant <=1/4, and
   maps the tau ball into the tau/2 ball. Its fixed norm is <=tau/3, so the
   weaker printed factor 2 for the force bound is safe. The same unmarked
   local Taylor count works for an arbitrary pointwise scalar cube; no
   unjustified small marked norm is assigned to an arbitrary pointwise field.

5. **Domain identification.** The final delta_hat is bounded by both
   delta_CB/2 and delta_A, and rho stays within the existing SA/CB discs.
   Thus the real slice agrees with the known SA field by the existing
   pointwise uniqueness. The epsilon=0 match to IC is only on its admitted
   coarse tube and stated u-domain. Joint holomorphy is proved afresh by
   the uniformly convergent same-variable iteration, not inferred from
   separate analyticity statements. No source/coarse radius depends on
   u,T,p; this does not enlarge any selected-sector integral window.

6. **Critical Hessian tail, order and size.** (K+Delta)G=I+Delta G gives
   K_*^-1=G(I+Delta G)^-1 in that order. Put h=d_H m_G<=1/4. The endpoint
   tail bound m_G^2 d_H/(1-h) is <=c0/24<c0/16 under FU17. The marked
   bound is the sum of b_G h^j+j m_G b_h h^(j-1), with
   b_h=d_H(m_G+b_G). Consecutive products share their matrix summation
   index, so full labels are connected; symmetrization preserves both
   endpoint bounds and the exact symmetric total.

7. **Positive core retained at the lift.** The actual critical field is
   nonlocal as a function of original data. Consequently compressions of
   its Hessian are not asserted to have local original-data coefficients.
   The old lift core remains the whole positive matrix D_A. The coarse
   perturbation costs c0/8, lift tail c0/16, and new critical tail c0/16:
   c0-c0/8-c0/16-c0/16=3c0/4. Large core factors stay real nonnegative;
   arbitrary modulus-one factors are allowed only on the small tails.
   The Gaussian precision bound is alpha_*/U_*^2, not the old PS gamma.

8. **Normalization and domain preservation.** Recentered Taylor expansion
   has no linear term at the undeformed endpoint. Its exact remainder is
   a difference quotient; the series is claimed only under the printed
   common analytic margin. Real translation gives the domain (D_a-a_*)/sigma,
   with h_N^n, the full determinant, and the exact finite-u action intact.
   Complex translation or replacing that domain by a centered ball would
   need boundary/contour terms not proved here. Gaussian covariance
   factorization does not factor the interacting law or hard histories.

9. **Rate and final scope.** The construction retains only
   beta=(16R)^(-4) in original coarse blocks. Neither RD's two-unit margin
   nor FR's box-margin argument is consumed unchanged. Fixed-order atom
   differentiation is not an all-order integral/tree sum. The critical
   tail is generally nonzero at zero source on curved backgrounds; no
   source-normalized cancellation is silently introduced.

Unsuccessful candidate substitutions preserved as explicit restrictions:
using the u-stripped tree field; dropping H_epsilon a; declaring critical
principal patches local in original data; replacing translated hard domains
by centered balls; and reusing stronger support margins or PS's old precision
constant. These are rejected steps in this construction, not a no-go for
all routes. There are no numerical failures or experiments. Full existence,
physical continuum gap and the original-cut return theorem remain open.

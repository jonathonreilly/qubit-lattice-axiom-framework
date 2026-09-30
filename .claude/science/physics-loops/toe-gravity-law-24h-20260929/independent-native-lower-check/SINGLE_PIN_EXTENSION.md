# Root extension: a stronger full-channel threshold lower bound

Author extension, not an independent review of itself. It was derived in the immutable PRE before the lower-route REPORT was read. Subsequent full reading and literal normalization controls agree with its prerequisites. A separate focused check is required before substantial reuse.

Fix the exact supplied native model, a=min(tau,mu/12)>0, and the already checked compact-response definition of the full fifteen-channel threshold form T0. The candidate improvement is

    T0 >= (2a/g) I15 >= [16a/(sqrt(3)pi)] I15,
    g=(2pi)^-3 integral_BZ ell(k)^-1 dk <=sqrt(3)pi/8,
    ell(k)=2sum_i(1-cos k_i).

This is not an EOS or phase statement. It strengthens the smaller valid static-block estimate in the author's REPORT without changing its capacity comparison.

Choose the nine forward bare graph-edge displacements d:2e_i and e_i+/-e_j. Set B_d(x)=b_x b_(x+d) and f_(eta,d)(x)=<eta|B_d(x)psi>. The landed full-carrier bare-gradient inequality, dropping one of the two identical translated copies of each plane-edge gradient, gives

    <psi,H0 psi> >= a sum_(eta,d,x,j)|f_(eta,d)(x+e_j)-f_(eta,d)(x)|².

Using forward endpoints instead of the axial midpoint cell translates each axial component by e_i. This preserves its gradient norm; no q-dependent frame norm is discarded. All actual residual occupation sets eta occur, with the original extraction normalization. The inequality follows directly from the fifteen-word expression, independently of any many-pair isometry.

For an incoming complex symmetric matrix A in Sym² C5, use the exact convention Phi_A=(1/sqrt2)sum_ab A_ab C_a* C_b* Omega, with ||A||HS its channel norm and the normalized nine-by-five frame U*U=I. For each residual graph edge eta={y,y+d0}, its removed-pair amplitudes have far constants

    v_(d,d0)=sqrt2 (U A U^T)_(d,d0).

Other physical matchings/overlap corrections are confined to finitely many relative coordinates. For any compact relative correction chi, f_(eta,d)(x)-v_(d,d0) has finite support as x-y varies. At x=y the actual hard-core identity pins ALL nine forward components to zero. Thus u_d=f_d-v_d is finitely supported with u_d(y)=-v_d.

For every finitely supported complex scalar u on Z³, Fourier Cauchy gives

    |u(y)|² <= [(2pi)^-3 integral ell(k)|uhat(k)|² dk]
                 [(2pi)^-3 integral ell(k)^-1 dk]
             = g sum_(x,j)|u(x+e_j)-u(x)|².

The second factor is finite in3D. Since gradients of u and f agree, each component costs at least |v_d|²/g. For fixed compact relative chi, pass the finite-volume energy/V and gradient expressions to their exact stabilized infinite-relative-coordinate sums, as in the previously checked threshold definition. This limit takes volume first at fixed compact correction; it does not minimize a finite torus with only one unconstrained pin. Keep only graph-edge residuals, sum their nine orientations per translation cell, and drop every other positive term. The result is

    E(Phi_A+chi) >= (a/g) sum_(d,d0)|sqrt2 (U A U^T)_(d,d0)|²
                   = (2a/g)||A||HS².

There is no extra factor1/2: every residual graph edge occurs once in the occupation-output resolution, and the two choices of removed separated pair are exactly the two kinetic contributions in the physical H0 identity. Literal identical-pair creation gives the displayed sqrt2; all fifteen symmetric basis directions were separately checked numerically against the ordered creation sum. These finite checks support the written normalization proof rather than supplying its quantifier.

The lower bound is independent of the support of chi, so taking the infimum over compact corrections proves it for the established T0. Compact corrections are form-dense in the l2 correction space because the relative H4 is bounded and its source F is compact; no square-integrable zero-energy minimizer is required. No global bounded inverse is presumed. Finally sin(|k_i|/2)>=|k_i|/pi on the Brillouin cube gives ell>=4|k|²/pi²; enclosing that cube by the radius sqrt3*pi ball yields g<=sqrt3*pi/8 and the stated explicit constant.

Remaining check request: independently verify the extraction multiplicity, forward-axis translation, far-channel normalization and compact-response/per-volume passage. A mismatch in any of these would invalidate this improved constant even though the author's smaller bound remains valid. Do not use the statement to infer a many-body threshold functional or condensation.

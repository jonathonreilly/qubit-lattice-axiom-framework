<!-- Owning original: PR9755; source SHA256 35938a1e8d27a2e498fdc9b5ee9115f7a1a7cd2bc60f10828adb38862a705200. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Fixed-order outgoing fast-host and arm coupling check

Checked 2026-10-18. Scope: steps 4–5 of `/private/tmp/neutral_all_order_coefficient_pole_root.md`. The estimates can be established for the stated finite-range coefficient host; they do not follow merely from an operator-norm perturbation, and do not establish the full microscopic resonance.

## Required actual-coefficient hypotheses

For each fixed m, require the scalar dispersion to be a real trigonometric polynomial

    e_lambda(k)=-4(cx+cy)-lambda(cx-cy)^2+r_m(k,lambda),

with fixed finite Fourier support and all fixed C^k norms of r_m bounded by C_(m,k) lambda^2. Require evenness in each momentum and xy interchange symmetry, as supplied by the native reflections/square action. Fixed support and coefficient bounds imply these derivative bounds; an abstract O(lambda^2) operator norm without locality/analytic structure would not suffice. The form factors must be fixed finite-support vectors (trigonometric polynomials), or a uniformly bounded finite collection of such vectors at fixed m.

Under the earlier connected-coefficient structure, these are appropriate properties of the actual bulk host, rather than independently selected higher coefficients. Applying them still requires the scalar-channel and finite-defect identification stated elsewhere in the proposed proof.

## Critical-point control

The unperturbed dispersion has four nondegenerate critical points, at the four combinations of 0 and pi. Its gradient is uniformly nonzero outside small neighborhoods of those points. Small C^2 perturbations therefore preserve exactly one critical point per neighborhood and create none elsewhere. Reflection symmetry pins the points exactly. The saddles (0,pi),(pi,0) have common energy

    e_s(lambda)=-4lambda+O_m(lambda^2),

and nonzero Hessian determinant near -16. The band extrema remain near +/-8, far from the target. At z=-6lambda+O(lambda^(7/3))-i Theta(lambda^3),

    w=z-e_s=-2lambda+o(lambda)-i Theta(lambda^3).

Thus the target disks remain on the same side of both saddle energies, at distance comparable to lambda, and stay away from all other critical values. A disk of radius c lambda^3 is much smaller than that separation.

## Outgoing logarithm and continuation

The parameter-dependent analytic Morse lemma reduces each saddle neighborhood to e=e_s+uv with an analytic nonvanishing Jacobian. At the saddle the Jacobian magnitude is 1/sqrt(|det Hess e_s|). For numerator F(k), the local density singularity is

    rho_F(w)= [F(k_s)/(2pi^2 sqrt(|det Hess e_s|))]
                  log(1/|w|) + bounded remainder,

summed over saddles. This normalization follows directly from integral delta(w-uv) du dv=2log(c/|w|). The density and Cauchy transform admit their outgoing analytic continuation through the regular negative-w interval. Analytic Morse patches with boundaries transverse to the nearby level curves, together with analytic contour deformation in the noncritical region, provide this continuation; it is not an application of the resolvent identity across continuous spectrum.

The continued Cauchy transform has a leading negative-imaginary logarithm. For d=cx-cy, d^2=4 at both saddles and sqrt(|det Hess|)=4+O(lambda). Hence

    G_dd^out(z,lambda)=-i/pi log(1/lambda)+O_m(1).

Equivalently one may keep a smooth positive coefficient c(lambda)=1/pi+O_m(lambda) in front of the logarithm; its difference times log is bounded and vanishes. Changes of the analytic density numerator contribute bounded terms or O(w log w); similarly O(lambda) changes of the saddle coefficient contribute O(lambda log lambda). The regular region is bounded uniformly. The Hilbert-transform real part of the local logarithmic density is bounded on this selected side of the critical energy, so no unaccounted real log divergence appears in G_dd.

For any two fixed finite form factors, the same calculation gives G_ij=O_m(log(1/lambda)). A form factor vanishing at the saddles can remove that leading logarithm, but no such improvement is needed here. These bounds are uniform on the specified lower disks on the outgoing sheet. Holomorphic does not mean derivatives remain bounded independently of lambda: Cauchy bounds retain the disk scale.

The hard origin removal is exactly irrelevant in the B1 sector because the origin vector is A1 and the dispersion commutes with xy interchange. Any remaining finite contacts should be handled explicitly as below. The ordinary lower-half-plane self-adjoint host resolvent would instead have the opposite imaginary sign and is not the sheet used in this argument.

## Leading arm coupling

Let G denote the outgoing host matrix, g the ordinary confined-arm local Green matrix, and couple host d to arm e1 with coefficient -2. The strip theorem supplies uniformly bounded g_ij on any fixed endpoint set and Im g_11>=c>0, hence |g_11|>=c. The scalar Schur denominator obeys

    |1-4 G_dd g_11| >= 4|G_dd||g_11|-1 >= c' log(1/lambda).

No positive-definiteness assumption on the entire arm imaginary matrix is used. Standard finite-rank formulas then give host-host local entries O(log), host-arm entries O(1), and arm-arm entries O(1). For example,

    R_ij^host=G_ij+4G_id g_11 G_dj/(1-4G_dd g_11),
    R_i1^mixed=-2G_id g_11/(1-4G_dd g_11).

Arbitrary fixed additional arm endpoint entries use the same bounded g_i1 factors. These formulas are analytic on the disk because the denominator is bounded away from zero there.

All extra finite contacts/cross-vertices of size O_m(lambda), after the higher bulk dispersion and long-arm terms have already been included, can be restored by a finite-matrix Neumann series. Its norm parameter is O_m(lambda log(1/lambda)), which tends to zero. This argument controls the desired local outgoing continuation and excludes new singularities in that disk. It does not use a global fast operator norm bound divided by Im z.

## Coupling to S and scaling

Connected fixed-order support makes S-fast vertices supported on bounded ell and r in a full COM momentum fiber. Changing an entire long column pair requires order at least its length; changing ell1/ell2 at far separation requires a connected cluster spanning that separation. Thus the finite-rank assertion is justified at fixed m, provided all COM momenta are fixed as stated in the draft.

The physical local fast Green function is O_m(log(1/lambda)/(Jz lambda)). Vertices start at Jz lambda^2. Their Schur correction is therefore O_m(Jz lambda^3 log(1/lambda)), or O_m(lambda log(1/lambda)) in slow units. Its analyticity follows from the established disk continuation, not solely this magnitude estimate. The special cancellation giving earlier 1/log bounds is unnecessary for this weaker estimate.

The later Airy argument can use this weaker boundary bound: f_s times lambda log gives physical O(Jz lambda^5 log), still o(Jz lambda^(14/3)). This consumer conclusion also requires the retained slow-host stability and localized pole derivative proof; it is not established by fast-channel estimates alone.

Conclusion: steps 4–5 are supportable under the explicit actual finite-range/symmetry hypotheses. The Morse/log and finite-rank arguments close this fast-host issue within the fixed-order coefficient model. Complete scalar graph identification, slow-host matching, and transfer to the actual untruncated microscopic Hamiltonian remain separate obligations.

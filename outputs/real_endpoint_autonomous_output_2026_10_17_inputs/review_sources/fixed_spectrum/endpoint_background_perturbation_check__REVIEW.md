# Scalar endpoint-background perturbation: narrow review

Finding: the rank-eight identities, outgoing/source updates, explicit margins, self-energy/profile comparisons and complete C continuation survive reconstruction. No mathematical correction is required in the requested interface. This accepts the stated endpoint perturbation estimates at fixed emitter E0 and installed kappa=10^-8 under the pinned nominal premises. It does not establish a simultaneous fixed-spectrum perturbation theorem, a complete finite-time error budget, or a uniform h=10^-18 strip as kappa tends to zero.

## Sources, exposure and scope

The reviewed `../endpoint_background_perturbation/PROPOSAL.md` was read completely and hashed as `8c308e8d699122318f41fc0195028f3626ba3bd14558d589b3271f16a6c7d32e`.

Nominal authority is the endpoint note at supplied milestone `97ccd9f9bee7e69af123395fcb04d40812885ac4`, SHA256 `bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5`. Its body, including disk, real coupling, weighted ratio and full Schur continuation proofs, was already read at this identity in the preceding coherent tasks. Later working-note precision appends are not used as evidence here, and no new Git inspection occurred.

I authored the reused `../schur_strip_interface/PROPOSAL.md` (`16cc6ce85dd6bd40cf9ca6084274fd9b9d438134b39b35af21646a3af4f82a39`) and the mass assessment, and previously checked the complex self-energy bridge and restricted reference moment. I also authored a structural endpoint proposal with related Woodbury identities and explicitly open changed-background interfaces. This is source-exposed checking of a different author's concrete quantitative closure of those interfaces, not blind review or an additional independent origin of the nominal proofs. The independently checked nominal Schur report is `11346d3c20ca4ae749b3c55750e8e0ec4144a9b4e9f82b3018c093f3a9516f18`; its underlying source definitions are reused, not requalified wholesale.

The separate root fixed-spectrum proposal and its local algebra review are provenance rather than necessary inputs to this fixed-emitter check. Their conclusion is not used to add an emitter-energy or hopping perturbation. No scientific executable, numerical integration, simulation or parameter search was used. Only text reads, hashing and this report write occurred. No W/Git/checkpoint/prompt changes or model/effort overrides occurred. Applicable unchanged workflow guidance is reused.

## 1. Finite-rank inverse and transpose norms

With P the real endpoint inclusion and A_delta=A-delta PP^T, Woodbury gives

    R_delta=R+delta RP(I-delta G)^-1P^TR,
    R_delta P=RP H, P^T R_delta=H P^TR,
    G_delta=GH, H=(I-delta G)^-1.

The sign is correct for a positive Hamiltonian onsite perturbation in the retarded convention (lambda-H)^-1. Because delta is scalar, G and H commute; no other matrix commutation is used. Complex symmetry R^T=R and real P give P^TR=(RP)^T. The spectral norm of a complex matrix equals the norm of its transpose, without replacing the transpose by an adjoint in the algebra.

Thus the proposed norm bounds follow with h_K=(1-10^-20 K)^-1. For K=36,

    h_36<1+10^-18,
    10^-20*36^2*h_36<1.3e-17.

The disk inverse H is analytic because its Neumann denominator is bounded away from zero. Only the finite-coordinate endpoint G is bounded on the radius10^-12 disks. No bound on an infinite real-axis resolvent is inferred; the full nominal background matching inverse is used on its established narrower strip.

## 2. The complete inhomogeneous source and explicit margins

The physical incoming source iE'(z)u is unchanged because the output boundary, dispersion and reference plane are unchanged. Multiplying the exact inverse update by that source yields

    x_bg,delta=x_bg+delta RP H P^T x_bg.

This retains every background internal coordinate, and gives the claimed factor1+10^-20||RP||h_36. It is stronger than merely updating the endpoint Green matrix.

Using the unrounded nominal quantities at theta=.224,

    B_raw=2.24e18/.776<2.887e18,
    P_raw^2=1.008e23/.776^2<1.675e23,
    X_raw=(1.5e9+.062*2.24e18*10^-18)/.776<1.934e9,

the inverse change is<1700. The selected-column multiplier h_36 leaves the explicit gap between1.675e23 and(4.1e11)^2=1.681e23. The source multiplier is<1+4.2e-9, so the actual source remains<1.935e9<2e9. Therefore the displayed2.89e18,4.1e11,2e9 ceilings are retained with quantitative margins. The argument does not assume the old individual diagonal bounds remain literally unchanged or reuse a rounded inequality without slack.

## 3. Outgoing coefficient extraction

Extracting the outgoing coefficient from the endpoint-forcing column RP before taking an off-axis Hilbert norm is legitimate and linear. Applied to R_delta P=RP H, it gives exactly L_delta=L H. Equivalently L+delta LHG=LH. This preserves the full complex coefficient and its physical reference plane, rather than just its modulus.

The real ||L||<34 follows from the given scalar row, |tau|<=1, J>.03, |R_bg|<12e-6 and the old row error. Hence

    ||L_delta-L||<10^-20*34*35/(1-35e-20)<1.2e-17.

This is larger than epsilon_L and the proposal correctly does not reuse epsilon_L against the old untransformed comparison. If that comparison is transformed, the resolvent identity H-H0=H delta(G-G0)H0 and the decomposition

    L_delta-L0H0=(L-L0)H+L0(H-H0)

give the proposed<2e-21 bound. The open factor1/(1-delta g) is complex and is correctly retained. No arbitrary-distance growing free wave is asserted to be an l2 vector.

## 4. Endpoint and full complementary self-energy

Differentiation at fixed scalar delta gives G_delta'=H G' H, even though G' need not commute with G. The upper bound35000/(1-35e-20)^2<35001 is valid; the document appropriately enlarges rather than automatically preserves35000. Disk Cauchy at radius10^-12 gives36.000001*10^-6/(1-10^-6)<.000037 throughout the strip, including both cutoff edges.

The complementary bare gap minus .062rho and kappa^2*36.000001 exceeds1/6 at kappa<=10^-8, so both old and perturbed Dcc inverses have norm<6. With e_G=1.3e-17, subtraction gives

    ||Dcc_delta^-1-Dcc^-1||<=36kappa^2 e_G.

For the complementary product, replace one left Green factor, one inverse, then one right Green factor. Bounding both Green norms by36 gives respectively216kappa^2 e_G,46656kappa^4 e_G,216kappa^2 e_G. Including the jj difference proves

    |s_delta-s|<=e_G[1+432kappa^2+46656kappa^4]<1.4e-17.

Every complementary coordinate and product contribution is present. The real energy derivative estimate also checks:

    |s_delta'|<=35001+kappa^2[2*35001*6*36+72*36^2]<36000.

There is ample margin below the mass allowance10^6. Center constants A=35,B=17,b_min=12 follow from the original explicit comparison to -z/J, not from the coarser35.000001 matrix ceiling. For example the nominal real entry is within.000801 of -z/J with1/J<100/3, leaving substantial real-part slack below35; its central imaginary bounds have analogous slack. A1.4e-17 correction cannot consume it.

For complex oscillation the two Schur correction values each cost at most6kappa^2(36.000001)^2. Added to.000037 they remain below.000038. The unrounded real imaginary factor (1-1/40000)*.4/.031 exceeds12 by more than.9. Thus subtracting the1.4e-17 real self-energy change preserves Im Dj_delta>12kappa^2. At kappa=10^-8, subtracting .062h+.000038kappa^2 leaves the required>6kappa^2 on the full strip. The proof establishes Dcc analyticity before using it in s_delta and then establishes the resonant scalar nonzero; there is no circular full-inverse assumption.

## 5. Fixed-reference complex profile and unrounded slack

Let c=kappa^2 Dcc^-1Gcj and its perturbed counterpart c_delta. Product subtraction gives

    ||c_delta-c||<=kappa^2 e_G(6+1296kappa^2)<7kappa^2 e_G.

Using ||c||<6kappa^2*10^-22, ||L_delta-L||<1.2e-17 and ||L_delta||<34 plus negligible slack gives |N_delta-N|<1.3e-17. Stone's normalization and the old complete reference phase are identical on both sides, so no velocity, kappa or2pi factor is missing in the ratio comparison.

The self-energy change gives

    |Dj_delta-Dj|/|Dref|
       <=(J/sin k)|s_delta-s|<1.1e-18.

Nominal relative denominator error<.000025 plus this change is below.000026, proving both denominator lower bounds used in the subtraction. Consequently

    |Fj,delta/Fref-Fj/Fref|
      <.031*1.3e-17/(1-.000026)
           +1.001*1.1e-18/(1-.000026)<2e-18.

The use of the underlying unrounded pointwise calculation is necessary and correct. Its nominal intercept is bounded by

    (1.76e-13+3e-20+2.4e-25)/.99996+3.2e-23<1.761e-13,

and its slope is(749+.000288)/.99996<750. Adding2e-18 raises the intercept by only.00002e-13, still below1.762e-13<2e-13. Thus the stated2e-13+750s bound survives. The uniform.000752 ceiling has ample margin as well. This does not assert unchanged epsilon_G or epsilon_L separately.

## 6. Full C and actual scope

The perturbed full source solve

    x_e,delta=-kappa De_delta^-1 P^T x_bg,delta,
    x_delta=[x_bg,delta;0]+[-kappa R_delta P;I]x_e,delta

uses the complete eight-coordinate De_delta. Its rank-one Schur norm gives bottom<.18/kappa^2 with the new complex margin. At the cutoff sides the displayed energy separation v sigma minus .061h^2, kappa^2*36.000001 and6kappa^4(36.000001)^2 still exceeds2.49e-8, yielding inverse<5e7. Substituting the retained source and selected-column ceilings gives C_bottom<5e20 and C_side<1.4e13 exactly as stated.

The definition of C_delta uses the actual reflection from x_delta. Subtracting those open waves before taking its Hilbert norm is essential and is done here. Exterior dispersion and projectors are fixed, so the seven decaying tails retain their uniform ratio<1/6 and the resulting C_delta is Hilbert-valued holomorphic. The conservative3||x_delta||+4 bound includes the full source/core/emitter and all closed tails. No off-real unit-modulus assertion enters.

Since E0 and kappa are fixed in this comparison, the nominal f and a0, scalar contour denominators and target normalization genuinely are unchanged; the changed actual emitted profile is paid separately by the ratio estimate. This is distinct from choosing a new actual-parameter waveform to mask the endpoint error.

The proposal deliberately stops before composing an actual spectral mass/static/finite-time theorem. Its real invertibility and unchanged open boundary are consistent with the local spectral synthesis argument, but a final application must still state the residual spectrum, preparation, overlap factors, contour costs and finite transfer together. For negative delta the physical onsite coefficient must be combined with the original positive compensation; it is not itself a positive added block. Simultaneous emitter detuning or hopping changes are not included by this check, even if separate inequalities suggest ample margin. No fixed-spectrum runtime conclusion follows here.

Disposition: accept the stated scalar endpoint-background interface, under its pinned nominal hypotheses and stated fixed-emitter scope, without correction. Full correlated-device composition remains a separate obligation.
